#  create a password validation function - length between 8 -20 char , 1 upper char , 1 lower char and  1 sqeacial char  , 1 numeric


def pass_validator(password):
  is_upper = False
  is_lower = False
  is_char = False
  is_digit = False

  if len(password) >=8 and len(password) <=20:
    for char in password:
      if char.isupper():
        is_upper = True
      elif char.islower():
        is_lower = True
      elif char.isdigit():
        is_digit = True
      elif char in "!@#$%":
        is_char = True

    if is_upper and is_lower and is_char and is_digit:
      print("password is valid")
    else:
      print('passowrd is not having valid chars')
  else:
    print('password lewngth is incorrect')

password = input("Enter your password: ")
pass_validator(password)