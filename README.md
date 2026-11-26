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

---

## Task 2 – Phishing Awareness Email Templates

Created three HTML-based phishing awareness simulations for MediPlus Pharmacy employees. Each template contains a visible **TRAINING ONLY** banner and HTML comments explaining the psychological triggers used in phishing attacks.

### Templates

### 1. Invoice Template – [invoice_template.html](invoice_template.html)  
   Demonstrates how attackers may exploit authority and financial pressure through fake invoice notifications.

### 2. Password Reset Template – [password_reset_template.html](password_reset_template.html)  
   Demonstrates how fear and urgency surrounding account security may pressure employees into unsafe actions.

### 3. Delivery Notification Template – [delivery_template.html](delivery_template.html)  
   Demonstrates how curiosity and uncertainty about unexpected deliveries may make employees vulnerable to phishing.

### Common Phishing Techniques

- Authority: Impersonating departments such as Accounts or IT Support.
- Fear and Urgency: Creating concerns about account security or pending actions.
- Curiosity: Using unexpected delivery notifications to attract attention.
- Financial Pressure: Using invoices or payment-related concerns to encourage rushed decisions.

### Security Recommendations

- Verify unexpected emails through official communication channels.
- Never share passwords or sensitive information through email.
- Avoid opening unexpected attachments or following unknown links.
- Check the sender's identity carefully before taking action.
  

---

## Task 3 – Phishing Awareness Landing Page

Created a single-page HTML landing page simulating a generic MediPlus Pharmacy staff login portal for cybersecurity awareness training.

### Features

- Username and password input fields.
- Corporate-style login interface using HTML and CSS.
- JavaScript hides the login form after submission and displays a **Training Complete** message.
- No credentials are stored, collected, or transmitted.
- Includes phishing-awareness guidance to help staff identify suspicious login pages.
- Includes a visible simulation notice.

### Security

The page operates entirely in the browser. Form submission is prevented from sending data to any server.

**Footer disclaimer:** This is a simulation for MediPlus Pharmacy staff training.

### File

- [index.html](index.html) – Contains the complete HTML, CSS, and JavaScript for the training page.


## Disclaimer
All three templates are fictional awareness-training examples. They contain no functional phishing links, credential collection forms, or real attachments.

This project uses simulated log data for educational and cybersecurity training purposes. The IP addresses and activity patterns are not evidence of real attacks.

---

**Completed as part of my Cyber Security Internship at Ezitech Software House.**