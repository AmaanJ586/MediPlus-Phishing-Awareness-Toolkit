#!/bin/bash

echo " MEDIPLUS PHARMACY LOG ANALYSIS"

echo ""
echo "1. Failed requests (401/403):"
grep -E "STATUS=401|STATUS=403" mail.log

echo ""
echo "2. Extracted timestamps and IP addresses:"
grep -E "STATUS=401|STATUS=403" mail.log | awk '{print $1, $2, $3}'

echo ""
echo "3. Suspicious user agents:"
grep -E "curl|python-requests|BotScanner" mail.log

echo ""
echo "4. Total failed requests:"
grep -Ec "STATUS=401|STATUS=403" mail.log

echo ""
echo "5. Total suspicious user agents:"
grep -Ec "curl|python-requests|BotScanner" mail.log

echo ""
echo "Analysis completed."