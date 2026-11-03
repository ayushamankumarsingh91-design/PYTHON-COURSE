# password validator
# string question
# write a function to validate the given password.
#conditions : 1. 8-12 character 2.small 3.capital 4.special character any one ($#@&*^!?) 5.use digit 6. No space 

s = input()
clean_s = s.strip()

def password_validator(s):
    if len(s) < 8 or len(s) > 12:
        return "Password must be between 8 and 12 characters."
    if not any(char.islower() for char in s):
        return "Password must contain at least one lowercase letter."
    if not any(char.isupper() for char in s):
        return "Password must contain at least one uppercase letter."
    if not any(char.isdigit() for char in s):
        return "Password must contain at least one digit."
    if not any(char in "$#@&*^!?" for char in s):
        return "Password must contain at least one special character ($#@&*^!? )."
    if ' ' in s:
        return "Password must not contain spaces."
    
    return "Password is valid."
print(password_validator(clean_s))
