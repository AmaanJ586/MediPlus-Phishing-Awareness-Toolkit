import random
from datetime import datetime, timedelta

# Sample IP addresses
normal_ips = [
    "192.168.1.10",
    "192.168.1.15",
    "192.168.1.20",
    "10.0.0.5",
    "10.0.0.8"
]

suspicious_ip = "185.199.110.153"

# Normal and suspicious user agents
user_agents = [
    "Mozilla/5.0 Chrome/120.0",
    "Mozilla/5.0 Firefox/121.0",
    "Mozilla/5.0 Edge/119.0"
]

suspicious_agents = [
    "curl/7.68.0",
    "python-requests/2.28.1",
    "BotScanner/1.0"
]

# Generate 50 log entries
logs = []

start_time = datetime.now() - timedelta(hours=2)

for i in range(50):
    timestamp = start_time + timedelta(minutes=i)

    ip = random.choice(normal_ips)
    user_agent = random.choice(user_agents)
    status = 200

    # Create 5 failed login attempts
    if i in [5, 12, 20, 30, 40]:
        ip = suspicious_ip
        status = 401

    # Create 3 suspicious user-agent entries
    if i in [8, 25, 45]:
        user_agent = random.choice(suspicious_agents)

    log_entry = (
        f"{timestamp.strftime('%Y-%m-%d %H:%M:%S')} "
        f"IP={ip} STATUS={status} USER_AGENT='{user_agent}'"
    )

    logs.append(log_entry)

# Save logs to mail.log
with open("mail.log", "w") as file:
    file.write("\n".join(logs))

print("Successfully generated 50 log entries in mail.log")