text = "number is 125-325-5555 number"
import re

phone = re.search(r'\d{3}-\d{3}-\d{4}',text)
print(phone)
print(phone.group())
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')

results = re.search(phone_pattern,text)
print("\n")
print(results.group())
print("\n")
print(results.group(3))

