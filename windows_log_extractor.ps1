Get-WinEvent -LogName Security | Where-Object { $_.Id -eq 4625 } | Format-Table
