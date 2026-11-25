# MediPlus Pharmacy – Mail Log Analysis Findings

## 1. Project Overview

This report analyzes a sample mail log generated for MediPlus Pharmacy to identify failed requests and potentially suspicious activity.

## 2. Analysis Summary

- Total log entries analyzed: 50
- Failed requests (401): 5
- Failed requests (403): 0
- Suspicious user-agent entries: 3
- Suspicious IP address: 185.199.110.153

## 3. Suspicious Log Entries

### Finding 1: Repeated Unauthorized Requests

**IP Address:** 185.199.110.153  
**Status Code:** 401  
**Occurrences:** 5

This IP address generated five unauthorized requests. Repeated authentication failures may indicate password guessing or an attempt to access an account without permission.

### Finding 2: Automated Request Tool

**IP Address:** 10.0.0.5  
**User-Agent:** python-requests/2.28.1  
**Occurrences:** 2

The Python Requests library can be used to automate HTTP requests. Its repeated appearance may indicate automated activity that requires investigation.

### Finding 3: Suspicious Bot Activity

**IP Address:** 192.168.1.15  
**User-Agent:** BotScanner/1.0  
**Status Code:** 200

The BotScanner user-agent is unusual and may represent automated scanning activity. The request returned status 200, meaning it was successful, and should be investigated.

## 4. Tools Used

- Python – Generated the sample log file.
- grep – Filtered failed requests and suspicious user agents.
- awk – Extracted timestamps and IP addresses.
- Bash – Automated the log analysis process.

## 5. Conclusion

The analysis identified repeated unauthorized requests from a single IP address and three suspicious user-agent entries. These patterns may indicate automated activity or attempted unauthorized access.

This dataset is simulated for educational purposes. The findings demonstrate how basic command-line tools can help identify suspicious patterns in logs.

## 6. Recommendations

- Monitor repeated failed authentication attempts.
- Investigate suspicious user-agent activity.
- Consider blocking or limiting repeated unauthorized requests.
- Encourage employees to report suspicious emails and links.
- Regularly review mail server logs.
