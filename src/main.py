import re
import json
import os

# Opening and reading the raw text file

with open("../input/raw-text.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Regex pattern used for matching email addresses

email_pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'

emails = re.findall(email_pattern, text)

# categorizing extracteed emails

alu_official = []
alu_alumni = []
alu_si = []
regular_emails = []

for email in emails:
    if email.endswith("@alueducation.com"):
        alu_official.append(email)

    elif email.endswith("@alumni.alueducation.com"):
        alu_alumni.append(email)

    elif email.endswith("@si.alueducation.com"):
        alu_si.append(email)

    else:
        regular_emails.append(email)

url_pattern = r'(https?://[^\s<>"]+|www\.[^\s<>"]+)'

urls = re.findall(url_pattern, text)

safe_urls = []

for url in urls:
    if "javascript:" in url.lower():
        continue

    if "<script>" in url.lower():
        continue

    safe_urls.append(url)

phone_pattern = r'(\+\d{1,3}[\s-]?\(?\d+\)?[\s-]?\d+[\s-]?\d+[\s-]?\d+|\(\d{3}\)\d{3}[- ]?\d{4})'

phones = re.findall(phone_pattern, text)

card_pattern = r'\b(?:\d{4}[- ]?){3}\d{4}\b|\b\d{4} \d{6} \d{5}\b'

cards = re.findall(card_pattern, text)

valid_cards = []

for card in cards:
    digits = re.sub(r'\D', '', card)

    if len(digits) not in [15, 16]:
        continue

    if len(set(digits)) == 1:
        continue

    valid_cards.append(card)

masked_cards = []

for card in valid_cards:
    digits = re.sub(r'\D', '', card)
    masked = "*" * (len(digits) - 4) + digits[-4:]
    masked_cards.append(masked)

results = {
    "emails": regular_emails,
    "alu_official_emails": alu_official,
    "alu_alumni_emails": alu_alumni,
    "alu_si_emails": alu_si,
    "urls": safe_urls,
    "phone_numbers": phones,
    "credit_cards_masked": masked_cards
}

with open("../output/sample-output.json", "w", encoding="utf-8") as file:
    json.dump(results, file, indent=4)

print("=== Extraction Summary ===")

print("Regular Emails:", len(regular_emails))
print("ALU Official Emails:", len(alu_official))
print("ALU Alumni Emails:", len(alu_alumni))
print("ALU SI Emails:", len(alu_si))
print("URLs:", len(safe_urls))
print("Phone Numbers:", len(phones))
print("Valid Credit Cards:", len(masked_cards))

print("\nResults saved to output/sample-output.json")
