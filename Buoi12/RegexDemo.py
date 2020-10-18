import re
pattern = "[a-z0-9!#$%&\'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&\'*+\/=?^_`{|}~-]+)*@([a-z0-9\-]+\.)+[a-z0-9]{2,8}"
list = re.findall(pattern=pattern, string="my name is d 861583 7")
print(list)

email = re.fullmatch(pattern=pattern, string="tranbaotoan@gmail.com")
print(email)
