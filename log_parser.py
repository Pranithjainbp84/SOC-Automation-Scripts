import re

# Define log file path
LOG_FILE_PATH = 'path_to_your_log_file_here'

# Function to parse logs and find failed login attempts
def parse_failed_logins():
    failed_logins = []
    
    with open(LOG_FILE_PATH, 'r') as file:
        for line in file:
            # Example pattern for failed login attempt
            if re.search(r'failed login', line, re.IGNORECASE):
                failed_logins.append(line)
    
    return failed_logins

# Function to display failed login attempts
def display_failed_logins():
    failed_logins = parse_failed_logins()
    if failed_logins:
        print(f"Found {len(failed_logins)} failed login attempts:")
        for attempt in failed_logins:
            print(attempt)
    else:
        print("No failed login attempts found.")

if __name__ == "__main__":
    display_failed_logins()
