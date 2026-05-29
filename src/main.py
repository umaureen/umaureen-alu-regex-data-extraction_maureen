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

#categorizing emails using ALU tags
for email in emails:
    if email.endswith("@alueducation.com"):
        alu_official.append(email)

    elif email.endswith("@alumni.alueducation.com"):
        alu_alumni.append(email)

    elif email.endswith("@si.alueducation.com"):
        alu_si.append(email)

    else:
        regular_emails.append(email)

        #pattern for extractinng URLss
url_pattern = r'(https?://[^\s<>"]+|www\.[^\s<>"]+)'

#Extracting all URLs
urls = re.findall(url_pattern, text)

# storing safe URLs only
safe_urls = []

#filteriing unsafe URLs
for url in urls:

    # Ignore JavaScript injection attempts
    if "javascript:" in url.lower():
        continue

  # Ignore script injection attempts
    if "<script>" in url.lower():
        continue

    # Add safe URLs to the final list
    safe_urls.append(url)

# matchiing phone numbers using regex pattern
phone_pattern = r'(\+\d{1,3}[\s-]?\(?\d+\)?[\s-]?\d+[\s-]?\d+[\s-]?\d+|\(\d{3}\)\d{3}[- ]?\d{4})'

#extracting phone numbers
phones = re.findall(phone_pattern, text)

#matching credit card numbers
card_pattern = r'\b(?:\d{4}[- ]?){3}\d{4}\b|\b\d{4} \d{6} \d{5}\b'

#extracting credit card numbers
cards = re.findall(card_pattern, text)

#Storing only valid credit card numbers
valid_cards = []

# Validate extracted card numbers
for card in cards:

       # Removing spaces and dashes
    digits = re.sub(r'\D', '', card)

#limiiting. to 15 or 16 digits only
    if len(digits) not in [15, 16]:
        continue

    # Reject repeated fake card numbers like 1111-1111-1111-1111
    if len(set(digits)) == 1:
        continue

    # Add valid card to list
    valid_cards.append(card)

#masked credit card nnumbers
masked_cards = []

# Masking sensitive credit card information
for card in valid_cards:
    digits = re.sub(r'\D', '', card)

        # Replace all digits except the last 4 with *
    masked = "*" * (len(digits) - 4) + digits[-4:]
    masked_cards.append(masked)

# Storing extracted results in dictionary format
results = {
    "emails": regular_emails,
    "alu_official_emails": alu_official,
    "alu_alumni_emails": alu_alumni,
    "alu_si_emails": alu_si,
    "urls": safe_urls,
    "phone_numbers": phones,
    "credit_cards_masked": masked_cards
}

# Saving extracted results to a JSON output file
with open("../output/sample-output.json", "w", encoding="utf-8") as file:
    json.dump(results, file, indent=4)

# Print extraction summary to console
print("=== Extraction Summary ===")

print("Regular Emails:", len(regular_emails))
print("ALU Official Emails:", len(alu_official))
print("ALU Alumni Emails:", len(alu_alumni))
print("ALU SI Emails:", len(alu_si))
print("URLs:", len(safe_urls))
print("Phone Numbers:", len(phones))
print("Valid Credit Cards:", len(masked_cards))

# Printing output file location
print("\nResults saved to output/sample-output.json")
