def Password_Generator():
    
    import random
    
    symbols = "!#@%$^&*"
    alpha = "qwertyuiopasdfghjklzxcvbnm"
    alpha_Up = alpha.upper()
    nums = "1234567890" 
    
    symb_req = input("Do you need any symbols?").lower()
    if symb_req == "yes":
        sym_amount = int(input("How many symbols do you need?"))
    else:
        sym_amount = 0
        print("No symbols will be included in your password.")
    
    alphletters = int(input("How many letters do you need?"))
    Up_Cs = int(input("How many letters need to be uppercase?"))
    
    num_req = input("Do you need any numbers?").lower()
    if num_req == "yes":
        num_amount = int(input("How many numbers do you need?"))
    else:
        num_amount = 0
        print("No numbers will be included in your password.")
    
    Pass = random.sample(symbols, sym_amount)+random.sample(alpha, alphletters-Up_Cs)+random.sample(alpha_Up, Up_Cs)+(random.sample(nums, num_amount))
    Password = "".join(Pass)
    
    print("Your password is: "+Password)    


   
    
    
    
    
