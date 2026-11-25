# MediPlus Pharmacy – Phishing Awareness Toolkit & Log Audit

## Internship Project
**Organization:** Ezitech Software House  
**Intern:** Amaan Jahangir  
**Field:** Cyber Security  
**Client:** MediPlus Pharmacy  
**Task:** Task 1 – Analyze Sample Mail Logs for Phishing Patterns

---

## Project Overview

This project focuses on analyzing sample mail server logs to identify suspicious activity, failed authentication requests, and potentially automated requests.

A simulated log file containing 50 entries was generated using Python. Bash, grep, and awk were then used to filter and investigate suspicious entries.

## Objectives

- Generate a sample mail log containing 50 entries.
- Identify failed requests with HTTP status codes 401 and 403.
- Extract timestamps and IP addresses from suspicious requests.
- Identify suspicious user-agent strings.
- Automate log analysis using Bash.
- Document findings and security recommendations.

## Technologies Used

- Python
- Bash
- grep
- awk
- Git
- GitHub

## Project Files

| File | Description |
|---|---|
| `generate_logs.py` | Generates the sample mail log |
| `mail.log` | Contains 50 simulated log entries |
| `analyze.sh` | Automates the log analysis |
| `failed_requests.log` | Contains failed requests |
| `extracted_data.txt` | Contains extracted timestamps and IP addresses |
| `suspicious_agents.log` | Contains suspicious user-agent entries |
| `findings.md` | Documents the analysis and findings |

## Analysis Results

- **Total log entries:** 50
- **401 unauthorized requests:** 5
- **403 forbidden requests:** 0
- **Suspicious user-agent entries:** 3
- **Repeated suspicious IP:** `185.199.110.153`

The analysis identified repeated unauthorized requests from one IP address and multiple requests associated with suspicious or automated user-agent strings.

## How to Run

### 1. Generate the sample log

```bash
python generate_logs.py
```

### 2. Run the analysis

```bash
bash analyze.sh
```

The script displays failed requests, timestamps, IP addresses, suspicious user agents, and summary counts.

## Key Learning Outcomes

- Understanding basic mail/server log analysis.
- Using grep to filter suspicious entries.
- Using awk to extract specific fields.
- Automating analysis with Bash scripts.
- Identifying patterns that may indicate unauthorized access or automated activity.
- Writing a basic security findings report.

## Disclaimer

This project uses simulated log data for educational and cybersecurity training purposes. The IP addresses and activity patterns are not evidence of real attacks.

---

**Completed as part of my Cyber Security Internship at Ezitech Software House.**