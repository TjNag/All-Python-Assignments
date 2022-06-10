import re
str = "From abc@gmail.com to xyz@mail.com"
email = re.findall('\S+@\S+', str)
print(email)