import tempmail

email = tempmail.new_email()
print(email)
title, body, links = tempmail.get_mail()
index = 0
valid = []
for l in links:
    print(str(index) + " - " + l)
    valid.append(str(index))
    index += 1
