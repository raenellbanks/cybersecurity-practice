from datetime import datetime, timedelta
import re

log_file = 'auth.log'

pattern = re.compile(r'(\w{3} \d{2} \d{2}:\d{2}:\d{2}).*from ([0-9]{1,3}(?:\.[0-9]{1,3}){3})')

entries = []
with open(log_file) as f:
    for line in f:
        match = pattern.search(line)
        if match:
            timestamp_str = match.group(1)
            ip = match.group(2)
            timestamp = datetime.strptime(timestamp_str, '%b %d %H:%M:%S')
            entries.append((timestamp, ip))

time_window = timedelta(minutes=5)
ip_attempts = {}

for ts, ip in entries:
    if ip not in ip_attempts:
        ip_attempts[ip] = []
    ip_attempts[ip].append(ts)

print("IPs with multiple attempts within 5 minutes:")

for ip, times in ip_attempts.items():
    times.sort()
    for i in range(len(times)-1):
        if times[i+1] - times[i] <= time_window:
            print(f"{ip} had multiple attempts between {times[i]} and {times[i+1]}")

