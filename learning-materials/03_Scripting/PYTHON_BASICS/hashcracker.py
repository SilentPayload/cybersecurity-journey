import hashlib

def hash_word(word):
    return hashlib.sha256(word.encode()).hexdigest()

def crack_password(target_hash, wordlist):
    with open(r'C:\Users\praise\Documents\wordlist.txt', 'r') as file:
        for word in file:
            word = word.strip()
            

            mutations = mutate(word)
            for mutation in mutations:
                hashed = hash_word(mutation)

                if hashed == target_hash:
                    return f"Password has been cracked: The password is {mutation}"
            
        return 'No hash match found'
    

def mutate(word):
    mutations = []

    mutations.append(word)
    mutations.append(word.capitalize())
    mutations.append(word.upper())
    mutations.append(word + "1")
    mutations.append(word + "123")
    mutations.append(word + "!")
    

    leet = word.replace("a", "@")
    if leet != word:
        mutations.append(leet)

    leet = word.replace("e", "3")
    if leet != word:
        mutations.append(leet)

    leet = word.replace("o", "0")
    if leet != word:
        mutations.append(leet)

    leet = word.replace("I", "1")
    if leet != word:
        mutations.append(leet)

    return mutations

    



target = "7c6599a8f52ed25714f85a226d4c9fe8fc3d7fdc60b62f1a2c9da49a3c7c516a"
print(crack_password(target, "wordlist.txt"))


