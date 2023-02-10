def Password_Generator():
    
    import random
    import string
    
    print("Lets begin generating your password. ")
    symb_req = input("Do you need any symbols? ").lower()
    if symb_req == "yes":
        symb_amt = int(input("How many symbols do you require? "))
    else:
        symb_amt = 0
        print("No symbols will be included in your password.")
        
    alpha = int(input("How many letters do you need?"))
    Up_Cs = int(input("How many letters need to be uppercase?"))
    
    num_req = input("Do you need any numbers?").lower()
    if num_req == "yes":
        num_amt = int(input("How many numbers do you need?"))
    else:
        num_amt = 0
        print("No numbers will be included in your password.")
    
    unrand = random.sample(string.punctuation, symb_amt)+random.sample(string.ascii_lowercase, alpha)+random.sample(string.ascii_uppercase, Up_Cs)+random.sample(string.ascii_digits, num_amt)
    random.shuffle(unrand)
    Password = "".join(unrand)
    print(Password)

gen = input("Would you like to begin generating a password? ").lower()
    if gen == "yes":
        Password_Generator()
    else:
        print("No problem! Come back any time! ")
        
