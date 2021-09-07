# I tried my best for questions 3 - 5. I really think I
# just need more practice with python since I don't really
# know what functions do what and how to initialize them correctly

import csv
import json

#1) FizzBuzz Game
for i in range(100):

    # Fizz function
    if i % 3 == 0:
        print("fizz")
        continue

    # Buzz function
    if i % 5 == 0:
        print("buzz")
        continue

    print(i)

#2) Volume of Sphere
PI = 3.14159
print("Please input a number for radius ")
radius = input() # asks for user input
radius = int(radius)
v = 4.0/3.0 * PI * radius**3

print("The volume of your sphere is ", v)

#3) CSV Writing
FIELDS = ['Title', 'Author', 'ISBN13', 'Pages']

ROWS = [['1984', 'George Orwell', '1948', '384'],
        ['Animal Farm', 'George Orwell', '1944', '112']]

with open('books.csv', encoding = 'utf-8') as csvfile:
    bookwriter = csv.writer(csvfile)
    bookwriter.writerow(FIELDS)
    bookwriter.writerows(ROWS)

#4) CSV Return Dictonary Map
mydict = [{'1234': '5678', '4321': '8765', '2341': '6785'}]
with open('books.csv', encoding = 'utf-8') as csvfile:
    bookwriter = csv.DictWriter(csvfile, fieldnames = FIELDS)
    bookwriter.writerow(FIELDS)
    bookwriter.writerows(mydict)

#5) Function Testing and Tempfiles
temp = tempfile.mkdtemp()
path = os.path.join(temp)
cred_data = ['information']

with open(path + '/cred.json', encoding = 'a') as cred:
    cred.write(cred_data)
    json.dump(cred_data, cred)

    information = (path + '/cred.json')
    print(information)
