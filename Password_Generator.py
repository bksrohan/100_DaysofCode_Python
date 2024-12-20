#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ""

for letter in range(1, nr_letters + 1):
    random_letter = (random.choice(letters))
    password += random_letter

for number in range (1, nr_numbers + 1):
    random_number = (random.choice(numbers))
    password += random_number

for symbol in range(1, nr_symbols + 1):
    random_symbol = (random.choice(symbols))
    password += random_symbol 

print(password)
# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

hard_password = []
new_password = ""

for letter in range(1, nr_letters + 1):
    random_letter = (random.choice(letters))
    hard_password += random_letter

for number in range (1, nr_numbers + 1):
    random_number = (random.choice(numbers))
    hard_password += random_number

for symbol in range(1, nr_symbols + 1):
    random_symbol = (random.choice(symbols))
    hard_password += random_symbol 

print("This is password before shuffle", hard_password)
random.shuffle(hard_password)
print("This is password after shuffle", hard_password)
for char in hard_password:
    new_password += char
print("THis is the new pass", new_password)