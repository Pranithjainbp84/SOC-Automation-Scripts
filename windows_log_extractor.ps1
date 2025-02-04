# PowerShell script to extract Windows Event Logs related to security incidents

# Define the output file
$outputFile = "C:\path_to_output\event_logs.txt"

# Get security logs from Event Viewer
Get-WinEvent -LogName Security | Where-Object {$_.Id -eq 4625 -or $_.Id -eq 4624} | Select-Object TimeCreated, Id, Message | Format-Table -AutoSize | Out-File -FilePath $outputFile

# Print completion message
Write-Host "Security event logs have been extracted to: $outputFile"

