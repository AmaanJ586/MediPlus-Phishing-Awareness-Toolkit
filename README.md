# MediPlus Pharmacy – Phishing Awareness Toolkit & Log Audit

## Internship Project

| Detail | Information |
|---|---|
| Organization | Ezitech Software House |
| Intern | Amaan Jahangir |
| Field | Cyber Security |
| Client | MediPlus Pharmacy |
| Project | Phishing Awareness Toolkit and Log Audit |
| Status | Completed |

---

## Project Overview

This project was developed as part of my Cyber Security Internship at Ezitech Software House for MediPlus Pharmacy.

The goal was to analyze simulated server logs, identify suspicious activity patterns, develop phishing awareness email templates, and create a browser-based training landing page.

The final package combines technical log analysis with practical security awareness materials to help employees recognize phishing attempts and follow safer security practices.

## Project Objectives

- Analyze simulated mail/server logs for suspicious activity.
- Identify unauthorized requests and suspicious user-agent entries.
- Extract timestamps and IP addresses from log entries.
- Automate log analysis using Bash.
- Develop three phishing awareness email templates.
- Create a phishing awareness training landing page.
- Document findings, risks, recommendations, and usage instructions.

---

## Repository Contents

### Log Analysis

| File | Description |
|---|---|
| [`generate_logs.py`](generate_logs.py) | Generates the sample log file. |
| [`mail.log`](mail.log) | Contains 50 simulated log entries. |
| [`analyze.sh`](analyze.sh) | Bash script that automates log analysis. |
| [`failed_requests.log`](failed_requests.log) | Contains failed requests identified during analysis. |
| [`extracted_data.txt`](extracted_data.txt) | Contains extracted timestamps and IP addresses. |
| [`suspicious_agents.log`](suspicious_agents.log) | Contains suspicious user-agent entries. |
| [`findings.md`](findings.md) | Detailed log analysis findings. |

### Phishing Awareness Materials

| File | Description |
|---|---|
| [`invoice_template.html`](invoice_template.html) | Demonstrates invoice-related phishing techniques. |
| [`password_reset_template.html`](password_reset_template.html) | Demonstrates account-security phishing techniques. |
| [`delivery_template.html`](delivery_template.html) | Demonstrates delivery-notification phishing techniques. |
| [`index.html`](index.html) | Browser-based phishing awareness training page. |

### Final Documentation

| File | Description |
|---|---|
| [`final_report.md`](final_report.md) | Complete project report, findings, awareness materials, usage guide, and recommendations. |

---

## Log Analysis Results

The sample dataset contained 50 simulated entries.

| Finding | Result |
|---|---:|
| Total log entries | 50 |
| Unauthorized requests (401) | 5 |
| Forbidden requests (403) | 0 |
| Suspicious user-agent entries | 3 |
| Repeated suspicious IP | `185.199.110.153` |

The analysis identified repeated unauthorized requests and suspicious user-agent activity that could indicate automated or unauthorized access attempts.

These findings are based on simulated data and do not represent confirmed incidents involving MediPlus Pharmacy.

For detailed findings and business risks, see [`findings.md`](findings.md) and [`final_report.md`](final_report.md).

---

## How to Run the Log Analysis

### Requirements

- Python 3
- Bash-compatible terminal (Git Bash recommended on Windows)

### Step 1 – Clone the Repository

```bash
git clone https://github.com/AmaanJ586/MediPlus-Phishing-Awareness-Toolkit.git
```

### Step 2 – Navigate to the Project Folder

```bash
cd MediPlus-Phishing-Awareness-Toolkit
```

### Step 3 – Generate the Sample Logs (Optional)

```bash
python generate_logs.py
```

This creates the simulated log dataset used for analysis.

### Step 4 – Run the Analysis Script

```bash
bash analyze.sh
```

The script analyzes the log file and displays a summary of the results, including failed requests, extracted IP addresses, suspicious user-agent activity, and counts.

The generated output files can be reviewed afterward.

---

## Awareness Training Guide

### 1. Invoice Email

**File:** [`invoice_template.html`](invoice_template.html)

Demonstrates how phishing emails may exploit authority and financial pressure.

**Training focus:** Verify unexpected invoices and payment requests before taking action.

### 2. Password Reset Email

**File:** [`password_reset_template.html`](password_reset_template.html)

Demonstrates how attackers may exploit fear and urgency regarding account security.

**Training focus:** Verify password-reset notifications through official channels.

### 3. Delivery Notification Email

**File:** [`delivery_template.html`](delivery_template.html)

Demonstrates how unexpected delivery notifications may exploit curiosity and uncertainty.

**Training focus:** Avoid clicking unexpected links and verify notifications independently.

### 4. Awareness Landing Page

**File:** [`index.html`](index.html)

A simulated staff login page designed to demonstrate how fake login interfaces may appear convincing.

**How to use it:**

1. Open `index.html` in a web browser.
2. Review the simulated login interface.
3. Enter demonstration text if desired.
4. Submit the form.
5. Read the training completion message and security guidance.

The landing page does not store or transmit credentials.

---

## Security Recommendations

- Verify unexpected emails and requests using official communication channels.
- Avoid clicking unknown links or opening unexpected attachments.
- Use strong, unique passwords.
- Enable multi-factor authentication wherever supported.
- Regularly review server and mail logs.
- Report suspicious emails to the IT/security team.
- Inspect website addresses before entering account information.

---

## Technologies Used

- Python
- Bash
- HTML
- CSS
- JavaScript
- Git
- GitHub
- grep
- awk

---

## Disclaimer

This project is intended for cybersecurity education and awareness training.

All log data is simulated. The email templates and landing page are training simulations and must not be used for unauthorized phishing, credential collection, or deceptive activities.

---

## Final Report

The complete handover report is available here:

**[Read the Final Report](final_report.md)**

---

Completed as part of my Cyber Security Internship at Ezitech Software House.