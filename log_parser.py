import re

log_file = "security_logs.txt"

with open(log_file, "r") as logs:
    for line in logs:
        if re.search(r"Failed login attempt", line):
            print("Suspicious Activity Detected:", line)
