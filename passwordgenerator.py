#.....................PASSWORD GENERATOR................................
import random
import string

print("...........................  \"Hello user !! Welcome to PASSWORD GENERATOR\"  .........................\n")

retry = 'yy'
while retry.lower() == 'yy':
    print("\n.........     Let's start  !!     ...........")

    while True:
        try:
            length = int(input("Enter the length of Password : "))
            ask =  int(input("\nEnter 1 : Easy  (only Alphabatic letters)\nEnter 2 : Medium  (Alphabatic letter + Numbers)\nEnter 3 : Hard  (Alphabatic letter + Numbers + punctuation)\n"))
            if ask in [1,2,3]:
                break
            print("ENter correct input....")
        except:
            print("Enter correct input")
    ret = 'y'
    while ret.lower() == 'y' :
        if ask == 1 :
            password = ''.join(random.choices(string.ascii_letters , k = length))
            print(f"............Generated password : {password}\n")
        
        elif ask == 2 : 
            password = ''.join(random.choices(string.ascii_letters + string.digits , k = length))
            print(f"............Generated password : {password}\n")
            
        elif ask == 3 : 
            password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation , k = length))
            print(f"............Generated password : {password}\n")
            
            
        ret = input("Enter 'Y' or 'y' for regenerate with.....SAME parameter\nOR Something else to Exit this operation : ")    
        
    if ret.lower() != 'y':
        retry = input("\nEnter 'yy' or 'YY' for regenerate with.....NEW parameter\nOR press any other key to Exit...!!! : ")
        
        
print("\n....................Thank You....Visit agin.........................")
