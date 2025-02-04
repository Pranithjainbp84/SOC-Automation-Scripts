SOC Automation Scripts

A collection of automation scripts for Security Operations Centers (SOC) designed to streamline the process of monitoring, analyzing, and responding to security incidents. These scripts help automate tasks like log parsing, threat intelligence fetching, and Windows event log extraction.

Scripts:

1️⃣ Log Parser for SIEM

File: [log_parser.py]

Description: A Python script that extracts failed login attempts from log files. It can be used to enhance SIEM (Security Information and Event Management) platforms by providing automated log analysis for potential security incidents.

2️⃣ Threat Intelligence Feed Fetcher

File: [threat_feed_fetcher.py]

Description: A Python script that fetches threat intelligence Indicators of Compromise (IOCs) from sources like VirusTotal. The script enables SOC teams to retrieve critical threat intelligence quickly.

Usage Example:

python
Copy
api_key = "your_api_key_here"
domain = "example.com"
print(fetch_virus_total(api_key, domain))

3️⃣ Windows Security Event Log Extractor (PowerShell)

File: [windows_log_extractor.ps1]

Description: A PowerShell script that extracts security-related Windows Event Logs. This script helps SOC teams efficiently collect logs related to security incidents for further analysis.
