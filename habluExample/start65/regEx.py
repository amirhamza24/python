import re

text = "The rain in Spain"

a = re.findall("[a-m]", text)
print(a)


# ekhon ekta kichu ache kina seta khuje ber kori
text2 = "1 is the special character"

x = re.findall("^1", text2)  # ekhane ^1 eta diye bujhacchi oi value ta 1 diye start hoiche kina.. ^ mane start with
if x:
    print("1 is the special character.")
else:
    print("No, 1 is not special character.")