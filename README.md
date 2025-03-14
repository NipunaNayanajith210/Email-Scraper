📌 Email Scraper Tool – Extract Emails from Any Website

🚀 A Python-based tool to scrape emails from websites and save them to a text file.

🔹 Features
✔ Extracts all email addresses from a given website
✔ Automatically saves emails in a .txt file
✔ Handles SSL certificate errors
✔ Skips broken or unreachable URLs
✔ Uses BeautifulSoup and requests for efficient scraping

🛠️ Installation Guide
1️⃣ Install Python (if not installed)
📥 Download and install Python from python.org

2️⃣ Install Required Libraries
Open Command Prompt (cmd) or Terminal and run:

CMD 
Copy code
pip install requests beautifulsoup4 lxml certifi
🚀 How to Use the Tool
1️⃣ Open a terminal (cmd, PowerShell, or terminal)
2️⃣ Run the script using:

CMD
Copy code
python email_scraper.py
3️⃣ Enter the target website URL when prompted.
4️⃣ The script will scan the site and extract emails.
5️⃣ Extracted emails will be saved in a .txt file inside the scraped_emails folder.

✅ Example:

bash
Copy code
Enter Target URL To Scan: https://www.example.com
[1] Processing: https://www.example.com
✅ Emails saved to: scraped_emails/example.com_emails.txt
📂 Output File Format
All extracted emails are saved inside scraped_emails/
Example file: scraped_emails/example.com_emails.txt

graphql
Copy code
info@example.com
support@example.com
admin@example.com

⚠️ Troubleshooting Errors
🔴 1. SSL Certificate Verification Failed
Fix: Run this command:

cmd
Copy code
pip install --upgrade certifi

🔴 2. No Emails Found
Possible Causes:
✔ Website may not have any visible email addresses
✔ The site may block bots from scraping
✔ The tool only scrapes visible emails, not hidden ones

🔴 3. ‘ModuleNotFoundError’
Fix: Ensure all required libraries are installed using:

cmd
Copy code
pip install requests beautifulsoup4 lxml certifi


📌 License & Legal Disclaimer
🔹 This tool is for educational purposes only.
🔹 Do NOT use it for illegal activities or unauthorized data collection.
