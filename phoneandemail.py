# Program to extract Phone number (in defined format) and email address from documents copied in clipbord (using Ctrl-C to copy to clipboard)
# And return results back to clipboard and ready for paste (using CTRL-V)
# using pyperclip module which needs to be installed

import re, pyperclip

# Create a regex for phone numbers
phoneRegex = re.compile(r'''
# Phone number formats could be: 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
(((\d\d\d)|(\(\d\d\d\)))?   # area code (optional)
(\s|-)                     # first seperator
\d\d\d                     # first 3 digits
-                          # second seperator
\d\d\d\d		   # last 4 digits
(((ext(\.)?\s)|x)          # extension word-part (optional) ext. or ext or x
(\d{2,5}))?)                # extension number part (optional)
''', re.VERBOSE)

# Create a regex for email address
emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+        # name part
@                      # symbol
[a-zA-Z0-9_.+]+        # domain name part

''', re.VERBOSE)

# Get the text off the clipboard
text = pyperclip.paste()

# Extract the email/phone from text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phonenumber in extractedPhone:
    allPhoneNumbers.append(phonenumber[0])
#print(allPhoneNumbers)
#print(extractedEmail)

# Copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n'.join(extractedEmail)
pyperclip.copy(results) 
