from bs4 import BeautifulSoup
import requests
import urllib.parse
from collections import deque
import re
import os
import certifi

# User input for target URL
user_url = input("Enter Target URL To Scan: ").strip()

# Ensure the URL has HTTP/HTTPS
if not user_url.startswith("http"):
    user_url = "https://" + user_url

# Create a directory to store results
output_dir = "scraped_emails"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# File path for saving emails
domain_name = urllib.parse.urlparse(user_url).netloc.replace("www.", "")
output_file = os.path.join(output_dir, f"{domain_name}_emails.txt")

# Initialize scraping lists
urls = deque([user_url])
scraped_urls = set()
email_data = set()  # Store found emails in memory

count = 0  # Request counter

try:
    while urls:
        count += 1
        if count > 20:  # Limit requests to avoid excessive scraping
            break

        url = urls.popleft()
        scraped_urls.add(url)

        print(f"[{count}] Processing: {url}")

        try:
            response = requests.get(url, timeout=5, verify=certifi.where())  # Secure SSL verification
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"[-] Request failed: {e}")
            continue

        # Extract emails
        found_emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", response.text, re.I)

        if found_emails:
            print("\n[+] Found Emails:")
            for email in found_emails:
                if email not in email_data:
                    print(email)
                    email_data.add(email)  # Store in memory to avoid duplicates

        # Parse the page for links
        soup = BeautifulSoup(response.text, "lxml")
        for anchor in soup.find_all("a", href=True):
            link = anchor['href']

            if link.startswith('/'):
                link = urllib.parse.urljoin(user_url, link)  # Convert to full URL

            if link.startswith("http") and link not in scraped_urls:
                urls.append(link)

except KeyboardInterrupt:
    print("\n[-] Process interrupted by user.")

# Save emails to file (APPEND MODE)
if email_data:
    with open(output_file, "a", encoding="utf-8") as file:  # 'a' mode appends instead of overwriting
        for email in sorted(email_data):
            file.write(email + "\n")
    print(f"\n✅ Emails appended to: {output_file}")
else:
    print("\n[-] No new emails found to save.")
