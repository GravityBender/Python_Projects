import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
           "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
           "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "&", "(", ")", "*", "+"]

password_len = int(input("Enter the length of the password "))
letter_no = int(input("Enter the number of letters in the password "))
if letter_no > password_len:
    print("The number of letters specified is greater than the password length itself")
    exit()

numbers_no = int(input("Enter the number of digits in the password "))
if letter_no + numbers_no > password_len:
    print("The number of letters and numbers is greater than the password length itself")
    exit()

symbols_no = int(input("Enter the number of symbols in the password "))
if  letter_no + numbers_no + symbols_no > password_len:
    print("The number of letters, numbers and symbols is greater than the password length itself")
    exit()

password_list = []
for i in range(0, letter_no):
    password_list.append(random.choice(letters))
for i in range(0, numbers_no):
    password_list.append(random.choice(numbers))
for i in range(0, symbols_no):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)
password = ""
for char in password_list:
    password += char
print(f"Your password is: {password}")
