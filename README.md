# Regex Data Extraction and Validation

## Project Overview

This project is a regex-based text processing program developed in Python. It simulates a real-world backend system that receives raw text data from an external API and extracts structured information using Regular Expressions (Regex).

The program focuses on:

- Extracting structured data from messy production-style text
- Validating input patterns carefully
- Handling realistic formatting variations
- Demonstrating defensive programming and security awareness

The system processes raw text stored in a separate input file and generates structured JSON output.

---

## Project Structure

text
alu-regex-data-extraction_{GithubUsername}/
├── input/
│   └── raw-text.txt
├── src/
│   └── main.py
├── output/
│   └── sample-output.json
└── README.md


### Folder Explanation

### input/
Contains the raw text file used as input.

### src/
Contains the Python source code responsible for extraction and validation.

### output/
Stores generated structured output in JSON format.

### README.md
Provides project documentation and usage instructions.

---

## Data Types Extracted

This project extracts and validates the following data types:

1. Email addresses
2. URLs
3. Phone numbers
4. Credit card numbers

The assignment requirement of four regex patterns is satisfied.

---

## Regex Patterns Used

---

### 1. Email Address Extraction

Regex:

python
r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'


This pattern extracts valid email addresses by matching:

- Username section
- @ symbol
- Domain name
- Valid top-level domain

Example matches:

- john@gmail.com
- support@company.org
- student@alueducation.com

---

### ALU Email Validation

The system performs additional validation for ALU-specific email types.

### ALU Official Emails

Accepted format:

text
@alueducation.com


Example:

text
student@alueducation.com


---

### ALU Alumni Emails

Accepted format:

text
@alumni.alueducation.com


Example:

text
graduate@alumni.alueducation.com


---

### ALU SI Emails

Accepted format:

text
@si.alueducation.com


Example:

text
mentor@si.alueducation.com


Emails are categorized into:

- ALU official
- ALU alumni
- ALU SI
- Regular email addresses

Only properly formed addresses are accepted.

---

### 2. URL Extraction

Regex:

python
r'(https?://[^\s<>"]+|www\.[^\s<>"]+)'


This pattern extracts:

- HTTP links
- HTTPS links
- WWW-based links

Examples:

- https://example.com
- http://company.org
- www.site.com

---

### URL Security Validation

The program does not automatically trust extracted URLs.

URLs containing suspicious content are ignored:

Examples:

- javascript:
- <script>

This helps prevent unsafe or malicious links from being treated as valid.

---

### 3. Phone Number Extraction

Regex:

python
r'(\+\d{1,3}[\s-]?\(?\d+\)?[\s-]?\d+[\s-]?\d+[\s-]?\d+|\(\d{3}\)\d{3}[- ]?\d{4})'


This pattern supports realistic phone number formats including:

International format:

text
+250 788 123 456
+1-202-555-0178


US-style format:

text
(202)555-0178


The regex handles:

- Country codes
- Spaces
- Dashes
- Parentheses

---

### 4. Credit Card Extraction

Regex:

python
r'\b(?:\d{4}[- ]?){3}\d{4}\b|\b\d{4} \d{6} \d{5}\b'


Supported card formats:

16-digit cards:

text
4111 1111 1111 1111
4111-1111-1111-1111


15-digit cards:

text
3782 822463 10005


---

## Credit Card Security Validation

The program applies additional checks before accepting card numbers.

Validation includes:

### Length Validation

Only:

- 15-digit
- 16-digit

cards are accepted.

---

### Repeated-Digit Rejection

Cards made from repeated digits are rejected.

Example:

text
1111111111111111


This helps ignore clearly fake values.

---

### Data Masking

Sensitive information is never fully exposed.

Extracted cards are masked before output.

Example:

Before:

text
4111111111111111


After:

text
************1111


This demonstrates secure handling of sensitive data.

---

## Security Considerations

This project assumes that external input is untrusted.

Security-focused practices include:

### 1. Unsafe URL Filtering

Potentially malicious URLs containing:

- javascript:
- script injection attempts

are ignored.

### 2. Sensitive Data Protection

Credit card numbers are masked to avoid unnecessary exposure.

### 3. Validation Before Acceptance

Extracted patterns are checked before being included in output.

The program avoids automatically trusting raw text.

This demonstrates defensive programming and awareness of hostile input.

---

## Sample Input

The input file:

text
input/raw-text.txt


contains realistic and messy production-style text that may include:

- Multiple email formats
- API logs
- Phone numbers
- URLs
- Credit card data
- Mixed formatting

---

## Sample Output

Results are saved in:

text
output/sample-output.json


Example:

json
{
    "emails": [
        "john@gmail.com"
    ],
    "alu_official_emails": [
        "student@alueducation.com"
    ],
    "urls": [
        "https://example.com"
    ],
    "phone_numbers": [
        "+250 788 123 456"
    ],
    "credit_cards_masked": [
        "************1111"
    ]
}


---

## How to Run the Program

### Step 1

Navigate into the project folder.

bash
cd alu-regex-data-extraction_{GithubUsername}


### Step 2

Run the Python program.

bash
python src/main.py


---

## Expected Console Output

Example:

text
=== Extraction Summary ===

Regular Emails: 3
ALU Official Emails: 1
ALU Alumni Emails: 1
ALU SI Emails: 1
URLs: 4
Phone Numbers: 3
Valid Credit Cards: 2

Results saved to output/sample-output.json


---

## Technologies Used

- Python 3
- Regular Expressions (Regex)
- JSON
- File handling

---

## Conclusion

This project demonstrates how regex can be used in realistic backend systems to extract and validate structured data from raw text while maintaining awareness of malformed or unsafe input.

The solution emphasizes:

- Accuracy
- Validation
- Security awareness
- Practical real-world formatting
