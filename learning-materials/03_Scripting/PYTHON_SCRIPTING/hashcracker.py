
"""
pycrack - a dictionary hash cracker (educational).

Architecture mirrors John/hashcat's dictionary mode:
    wordlist  ->  rule engine (mutations)  ->  hash  ->  compare

For AUTHORISED use only: your own hashes, CTFs, or engagements you have
written permission to test.
"""

import argparse
import hashlib
import itertools
import sys
import time


# ---------------------------------------------------------------------------
# 1. Hash algorithms
# ---------------------------------------------------------------------------
# One place to register algorithms. Each is a callable taking bytes -> hex str.

def _ntlm(data: bytes) -> str:
    # NTLM = MD4 of the UTF-16LE password. MD4 is disabled in many modern
    # OpenSSL builds, so this may raise; we surface that cleanly at runtime.
    h = hashlib.new("md4")
    h.update(data.decode("utf-8", "replace").encode("utf-16le"))
    return h.hexdigest()


HASH_ALGOS = {
    "md5":    lambda d: hashlib.md5(d).hexdigest(),
    "sha1":   lambda d: hashlib.sha1(d).hexdigest(),
    "sha224": lambda d: hashlib.sha224(d).hexdigest(),
    "sha256": lambda d: hashlib.sha256(d).hexdigest(),
    "sha384": lambda d: hashlib.sha384(d).hexdigest(),
    "sha512": lambda d: hashlib.sha512(d).hexdigest(),
    "ntlm":   _ntlm,
}

# Map digest length (hex chars) -> candidate algorithms, for auto-detection.
LENGTH_TO_ALGOS = {
    32:  ["md5", "ntlm"],      # ambiguous: same length
    40:  ["sha1"],
    56:  ["sha224"],
    64:  ["sha256"],
    96:  ["sha384"],
    128: ["sha512"],
}


def detect_algos(target_hash: str):
    """Return the list of plausible algorithms for a hash, by length."""
    return LENGTH_TO_ALGOS.get(len(target_hash), [])


# ---------------------------------------------------------------------------
# 2. Rule engine (mutations)
# ---------------------------------------------------------------------------
LEET_MAP = {"a": "@", "e": "3", "o": "0", "i": "1", "s": "$", "t": "7"}
APPENDS = ["", "1", "12", "123", "1234", "!", "!!", "@", "2024", "2025", "01"]
PREPENDS = ["", "!"]


def _leet_variants(word: str, max_variants: int = 16):
    """
    Generate combined leet substitutions, not one-at-a-time.
    We take every leetable position and toggle it on/off, so 'password'
    can become 'p@ssw0rd', 'p@$$w0rd', etc. Capped to avoid explosion.
    """
    positions = [i for i, c in enumerate(word) if c.lower() in LEET_MAP]
    if not positions:
        return {word}
    positions = positions[:4]  # cap combinatorial blowup on long words
    out = set()
    for bits in itertools.product([False, True], repeat=len(positions)):
        chars = list(word)
        for pos, on in zip(positions, bits):
            if on:
                chars[pos] = LEET_MAP[word[pos].lower()]
        out.add("".join(chars))
        if len(out) >= max_variants:
            break
    return out


def mutate(word: str):
    """Yield unique candidate passwords derived from one wordlist entry."""
    seen = set()
    # Case bases
    bases = {word, word.lower(), word.upper(), word.capitalize()}
    # Add leet forms of each base
    leeted = set()
    for b in bases:
        leeted |= _leet_variants(b)
    bases |= leeted
    # Apply affixes
    for b in bases:
        for pre in PREPENDS:
            for suf in APPENDS:
                cand = f"{pre}{b}{suf}"
                if cand not in seen:
                    seen.add(cand)
                    yield cand


# ---------------------------------------------------------------------------
# 3. Cracking loop
# ---------------------------------------------------------------------------
def crack(target_hash, wordlist_path, algo, salt="", salt_pos="suffix",
          report_every=50000):
    target_hash = target_hash.strip().lower()
    hash_fn = HASH_ALGOS[algo]

    attempts = 0
    start = time.time()

    with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as fh:
        for raw in fh:
            word = raw.strip()
            if not word:
                continue
            for cand in mutate(word):
                salted = (salt + cand) if salt_pos == "prefix" else (cand + salt)
                try:
                    digest = hash_fn(salted.encode("utf-8"))
                except Exception as e:
                    return None, attempts, f"algorithm '{algo}' unavailable: {e}"

                attempts += 1
                if digest == target_hash:
                    return cand, attempts, None

                if attempts % report_every == 0:
                    rate = attempts / (time.time() - start + 1e-9)
                    print(f"  ...{attempts:,} tried  ({rate:,.0f}/s)",
                          file=sys.stderr)

    return None, attempts, None


# ---------------------------------------------------------------------------
# 4. CLI
# ---------------------------------------------------------------------------
def main():
    p = argparse.ArgumentParser(description="pycrack - dictionary hash cracker")
    p.add_argument("target_hash", help="the hash to crack")
    p.add_argument("-w", "--wordlist", required=True, help="path to wordlist")
    p.add_argument("-a", "--algo", choices=list(HASH_ALGOS),
                   help="hash algorithm (auto-detected if omitted)")
    p.add_argument("--salt", default="", help="salt string, if any")
    p.add_argument("--salt-pos", choices=["prefix", "suffix"], default="suffix")
    args = p.parse_args()

    algos = [args.algo] if args.algo else detect_algos(args.target_hash)
    if not algos:
        sys.exit(f"[!] Can't detect algorithm from length "
                 f"{len(args.target_hash)}. Specify with -a.")

    if len(algos) > 1:
        print(f"[*] Ambiguous length -> trying: {', '.join(algos)}")

    t0 = time.time()
    for algo in algos:
        print(f"[*] Trying {algo}...")
        found, attempts, err = crack(
            args.target_hash, args.wordlist, algo,
            salt=args.salt, salt_pos=args.salt_pos)
        if err:
            print(f"[!] {err}")
            continue
        if found is not None:
            elapsed = time.time() - t0
            print(f"\n[+] CRACKED ({algo}): {found!r}")
            print(f"[+] {attempts:,} candidates in {elapsed:.2f}s")
            return
    print("\n[-] Not found. Try a bigger wordlist or more rules.")


if __name__ == "__main__":
    main()