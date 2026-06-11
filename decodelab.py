import string
import secrets

print("--- RANDOM PASSWORD GENERATOR ---")
try:
    password_length = int(input("Enter password length (e.g., 8, 12, 15): "))
    if password_length <= 0:
        print("Error: Length must be greater than 0!")
    else:
        all_characters = string.ascii_letters + string.digits + string.punctuation
        

        password_list = []
        
        for i in range(password_length):
            random_char = secrets.choice(all_characters)
            password_list.append(random_char)
            
        final_password = "".join(password_list)
        
        print("---------------------------------")
        print("Your Generated Password is: " + final_password)
        print("---------------------------------")

except ValueError:
    print("Invalid Input! Please enter a valid number for the length.")