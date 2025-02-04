 SOC-Automation-Scripts

A collection of Python and PowerShell scripts designed to automate various tasks for SOC teams, enhancing their efficiency in detecting and responding to security incidents.

## Scripts

### 1️⃣ Log Parser for SIEM
**File**: [log_parser.py]  
**Description**: A Python script that extracts failed login attempts from log files. It can be used to enhance SIEM (Security Information and Event Management) platforms by providing automated log analysis for potential security incidents.

### 2️⃣ Threat Intelligence Feed Fetcher
**File**: [threat_feed_fetcher.py]  
**Description**: A Python script that fetches threat intelligence Indicators of Compromise (IOCs) from sources like VirusTotal. The script enables SOC teams to retrieve critical threat intelligence quickly.

**Usage Example**:
```bash
python threat_feed_fetcher.py
python
Copy
api_key = "your_api_key_here"
domain = "example.com"
print(fetch_virus_total(api_key, domain))
3️⃣ Windows Security Event Log Extractor (PowerShell)
File: [windows_log_extractor.ps1]
Description: A PowerShell script that extracts security-related Windows Event Logs. This script helps SOC teams efficiently collect logs related to security incidents for further analysis.

4️⃣ Network Traffic Monitor (Python)
File: [network_traffic_monitor.py]
Description: A Python script that monitors network traffic for suspicious activities. It listens for anomalous traffic patterns and generates alerts for potential security incidents such as DDoS attacks or unusual outbound traffic.

Usage Example:

bash
Copy
python network_traffic_monitor.py

5️⃣ Malware Hash Checker (Python)
File: [malware_hash_checker.py]
Description: A Python script that checks if a given file hash matches known malware hashes by querying threat intelligence services like VirusTotal.

Usage Example:

bash
Copy
python malware_hash_checker.py
