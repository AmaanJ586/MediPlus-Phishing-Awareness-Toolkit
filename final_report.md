# MediPlus Pharmacy – Phishing Awareness Toolkit & Final Report

## 1. Project Overview

This project was developed as part of my Cyber Security Internship at Ezitech Software House for MediPlus Pharmacy. The objective was to create a practical phishing awareness toolkit and analyze sample server logs to identify suspicious activity.

The project includes simulated mail log analysis, three phishing awareness email templates, and a browser-based training landing page. These materials are designed to help employees recognize phishing attempts, understand common attack techniques, and follow safer security practices.

## 2. Log Findings

### Analysis Summary

The sample log file contained 50 simulated entries. The analysis was performed using Bash commands and a script to identify unauthorized requests, forbidden requests, and suspicious user-agent activity.

| Finding | Result |
|---|---|
| Total log entries | 50 |
| Unauthorized (401) requests | 5 |
| Forbidden (403) requests | 0 |
| Suspicious user-agent entries | 3 |
| Repeated suspicious IP address | 185.199.110.153 |

### Key Observations

- Five unauthorized requests were identified, indicating attempts to access resources without successful authentication.
- No forbidden (403) requests were detected in the sample.
- Three entries contained suspicious user-agent strings that may indicate automated activity.
- The IP address `185.199.110.153` appeared repeatedly in suspicious activity.

### Business Risk

Repeated unauthorized requests may indicate attempts to discover valid accounts or gain access to protected systems. If similar activity occurs on a real pharmacy network, successful unauthorized access could expose sensitive employee or business information, disrupt pharmacy operations, and potentially affect the confidentiality of customer information.

Suspicious automated requests may also increase server activity and make it harder for IT staff to distinguish legitimate traffic from malicious activity.

### Conclusion of Log Analysis

The sample logs demonstrate patterns that security teams should investigate, including repeated unauthorized requests and suspicious automated activity. These findings highlight the importance of monitoring server logs, reviewing unusual access patterns, and maintaining appropriate security controls.

**Important:** This analysis is based entirely on simulated log data. It does not confirm that MediPlus Pharmacy experienced an actual attack.

## 3. Awareness Materials

The awareness toolkit contains three simulated phishing email templates and a browser-based training landing page. These materials demonstrate common social engineering techniques employees may encounter in their workplace emails.

### 3.1 Phishing Email Templates

**1. Invoice Notification Template (`invoice_template.html`)**

This template demonstrates a fake invoice notification designed to exploit authority and financial pressure. Employees may feel compelled to review invoices or payment requests quickly, especially when the message appears to come from a trusted department.

**Psychological triggers:** Authority, financial pressure, urgency.

**Training objective:** Teach employees to verify unexpected invoices and payment requests through official channels before opening attachments or taking action.

**2. Password Reset Template (`password_reset_template.html`)**

This template simulates an account security notification that may cause employees to worry about their accounts. Fear and urgency can make recipients act without properly checking the sender or the destination of a link.

**Psychological triggers:** Fear, urgency, account-security concerns.

**Training objective:** Teach employees to verify password-reset notifications independently and never enter credentials through unverified links.

**3. Delivery Notification Template (`delivery_template.html`)**

This template demonstrates how an unexpected delivery notification can attract attention. Employees may click a link because they are curious about a package or uncertain about its delivery status.

**Psychological triggers:** Curiosity, uncertainty.

**Training objective:** Teach employees to carefully inspect unexpected delivery messages and verify them through official delivery services.

All three templates contain a visible training notice and comments explaining the psychological techniques being demonstrated. They are intended for awareness and education, not for collecting credentials or conducting real phishing attacks.

### 3.2 Phishing Awareness Landing Page (`index.html`)

The landing page is a simulated MediPlus Pharmacy staff login interface created using HTML, CSS, and JavaScript.

**Features:**

- Simulated staff login interface.
- Username and password input fields for demonstration.
- Training completion message displayed after form submission.
- Security awareness guidance explaining phishing risks.
- Visible simulation notice.
- No credentials are stored, collected, or transmitted.

**Training purpose:**

The page demonstrates how a fake login portal may appear convincing and why employees should carefully check website addresses before entering account information.

When the form is submitted, the page displays an educational message explaining the simulation and encouraging safer online behavior.

The landing page operates locally in the browser and does not send entered information to a server.

## 4. Usage Guide

This section explains how MediPlus Pharmacy staff or a reviewer can use the toolkit for security awareness training and review the sample log analysis.

### 4.1 Running the Log Analysis

The log analysis script can be executed using Git Bash or another Bash-compatible terminal.

**Steps:**

1. Download or clone the project repository from GitHub.
2. Open the project folder in Git Bash.
3. Run the following command:

   ```bash
   bash analyze.sh
   ```

4. Review the displayed summary, including failed requests, extracted IP addresses, suspicious user-agent entries, and total counts.

The script analyzes the existing sample log file `mail.log`. The generated results can be reviewed in `failed_requests.log`, `extracted_data.txt`, and `suspicious_agents.log`.

To regenerate the sample log before analysis, run:

```bash
python generate_logs.py
```

Then execute `bash analyze.sh` again.

### 4.2 Using the Email Templates

The three HTML email templates can be opened individually in a web browser.

**Steps:**

1. Locate `invoice_template.html`, `password_reset_template.html`, or `delivery_template.html`.
2. Open the selected file in a browser.
3. Review the email's content and identify suspicious characteristics.
4. Ask trainees to identify warning signs, such as urgency, unexpected requests, suspicious sender details, and psychological pressure.
5. Discuss the security recommendations and explain how employees should respond to similar messages.

These templates are for supervised awareness demonstrations and should not be sent to unsuspecting recipients.

### 4.3 Using the Landing Page

The awareness landing page is stored in `index.html` and can be opened locally.

**Steps:**

1. Locate `index.html` in the project folder.
2. Double-click the file to open it in a web browser.
3. Review the simulated login interface.
4. Enter demonstration text in the input fields if desired.
5. Submit the form to display the training completion message.
6. Review the awareness message and discuss how to recognize suspicious login pages.

The landing page is a local training simulation. It does not store or transmit entered credentials.

## 5. Security Recommendations

Based on the simulated log findings and awareness materials, the following recommendations are provided for MediPlus Pharmacy:

1. **Employee Awareness Training:** Conduct regular phishing awareness sessions to help employees recognize suspicious emails, unexpected attachments, and misleading links.
2. **Verify Unexpected Requests:** Employees should independently verify invoice, password-reset, and delivery notifications before taking action.
3. **Strong Authentication:** Use strong, unique passwords and multi-factor authentication wherever supported.
4. **Log Monitoring:** Regularly review server and mail logs for repeated unauthorized requests, suspicious user-agent activity, and unusual access patterns.
5. **Incident Reporting:** Establish a clear process for employees to report suspicious emails or potential security incidents to the IT team.
6. **Safe Browsing Practices:** Encourage employees to inspect website addresses and avoid entering credentials on unfamiliar or unverified pages.

## 6. Conclusion

The MediPlus Pharmacy Phishing Awareness Toolkit combines basic log analysis with practical employee awareness materials. The simulated log analysis demonstrates how suspicious access patterns can be identified, while the email templates and landing page provide examples of common phishing techniques.

This package can help employees understand the risks associated with phishing, improve their ability to recognize suspicious communications, and encourage safer handling of emails and login requests.

The project provides a foundation for continued security awareness training and routine log monitoring.

## 7. Disclaimer

All logs, email templates, and landing page interactions included in this project are intended for educational and awareness purposes only. The log data is simulated and does not represent confirmed incidents involving MediPlus Pharmacy.

The phishing templates and landing page are training simulations. They must not be used to deceive real users, collect credentials, or conduct unauthorized activities.