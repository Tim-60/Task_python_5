import random
import json
import string

name = str(''.join(random.sample(string.ascii_uppercase, 1) + random.sample(string.ascii_lowercase, random.randint(2, 8))))
surname = str(''.join(random.sample(string.ascii_uppercase, 1) + random.sample(string.ascii_lowercase, random.randint(2, 12))))
age = str(random.randint(1, 100))
email = str(''.join(random.sample(string.ascii_letters + string.digits, random.randint(5, 20)))) + '@example.com'
password = str(''.join(random.sample(string.ascii_letters + string.digits + string.punctuation, 12)))
print(name, surname, age, email, password)
json_object = {'name': name + ' ' + surname, 'age': age, 'email': email, 'password': password}
with open('C:\\Users\\tim\\Desktop\\json.txt', 'w') as file:
    json.dump(json_object, file, indent = 4)
    file.close()
with open('C:\\Users\\tim\\Desktop\\json.txt', 'r') as file:
    print(file.read())
    file.close()
