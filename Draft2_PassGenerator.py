def Password_Generator():
    
    import random
    import string
    
    ch = string.printable
    symb = "!#$%@&*_-+./?"
    
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
    
    unrand = random.sample(symb, symb_amt)+random.sample(ch[10:36], alpha)+random.sample(ch[36:62], Up_Cs)+random.sample(ch[0:9], num_amt)
    random.shuffle(unrand)
    Password = "".join(unrand)
    print(Password)
