import csv 
total_events = 0
critical_severity = 0
high_severity = 0
blocked_ip = 0
success = 0
failed = 0
failed_logins = {}
with open(r'C:\Users\praise\Documents\Siem_analysis_enterprise.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        total_events += 1
        action = row['action']
        severity = row['severity']
        event_type = row['event_type']


        if action == 'blocked':
            blocked_ip += 1

        elif action == 'success':
            success += 1

        elif action == 'failed':
            failed += 1

        if severity == 'critical':
            critical_severity += 1

        elif severity == 'high':
            high_severity += 1


        if row['event_type'] == 'login' and action == 'failed':
            print(f"Timestamp: {row['timestamp']}")
            print(f"Source IP: {row['source_ip']}")
            print(f"Username: {row['username']}")
            print(f"Country: {row['country']}")
            print("-"*30)
            if row['source_ip'] in failed_logins:
                failed_logins[row['source_ip']] += 1
            else:
                failed_logins[row['source_ip']] = 1


                if severity in ['critical', 'high']:
                    print(f'Timestamp: {row["timestamp"]}')
                    print(f'Username: {row["username"]}')
                    print(f'Event type: {row["event_type"]}')
                    print(f'Severity: {row["severity"]}')
                    print("-"*30)

        if event_type == 'login' and row['country'] != 'US':
            suspicious_login += 1
            print(f'Source ip: {row["source_ip"]}')
            print(f'Username: {row["username"]}')
            print(f'Country: {row["country"]}')
            print(f'Action: {row["action"]}')
            print("-"*30)


        
        

    for ip, count in failed_logins.items():
        if count >= 3:
            print(f'Brute Force Detected - IP: {ip}, Attempts: {count}')




print("="*50)
print(f'total_events: {total_events}')
print(f'Successful Login: {success}')
print(f'Failed Login: {failed}')
print(f'blocked_ips: {blocked_ip}')
print(f'critical Severity: {critical_severity}')
print(f'high severity: {high_severity}')
print(f'Suspicious Foreign Logins: {suspicious_login}')
print("="*50)