import re


text = '''Nordstrom Rack and HauteLook
Nordstrom Rack is the off-price retail division of Nordstrom Inc., which was founded in 1901 in Seattle, Washington, by John W. Nordstrom.

Nordstrom encourages contact from its customers and has supplied contact details to us.

700 S. Flower Street
Suite 1700
Los Angeles, CA 90017
https://www.nordstromrack.com/

Phone Contacts
Main: (206) 628-2111
Customer Service: (888)966-6283
International: (319) 846-4140

Nordstrom Customer Service: (888)282-6060



Email Contacts
Contact@nordstrom.com

Social Media Contacts
Facebook
Twitter

Executive Contacts
Primary Contact
Andrew Breen
Director Customer Care
700 S. Flower Street
Suite 1700
Los Angeles, CA 90017
Andrew.Breen@HauteLook.com

Secondary Contact
James F. Nordstrom
Executive Vice President and President of Nordstrom Stores
1600 Seventh Avenue
Suite 2600
Seattle, WA 98101
Jamie.nordstrom@nordstrom.com

Geevy Thomas
President of Nordstrom Rack
1600 Seventh Avenue
Suite 2600
Seattle, WA 98101
Geevy.Thomas@nordstrom.com

Chief Executive
See Notes Below
700 S. Flower Street
Suite 1700
Los Angeles, CA 90017

Erik B. Nordstrom
Co-President
erik.nordstrom@nordstrom.com

Peter E. Nordstrom
Co-President
Pete.Nordstrom@nordstrom.com'''


address = re.findall('\d{1,4}\s[A-Z][\.|a-z]+[\s|a-z|A-Z]+\d+\n[A-Z|a-z|\s|\,]+\d+', text)
print(address)
print(type(address))
email = re.findall('\S+[@]\S+', text)
print(email)
# mail = re.findall('[a-z|A-Z|\.]+@[A-Z|a-z|\.]+', text)
# print(mail)
phone = re.findall('\(\d+\)\s*[\d|\-]+', text)
print(phone)


