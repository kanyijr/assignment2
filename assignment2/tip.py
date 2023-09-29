#Kanyi Mwenda sct211-0012/2022

# getting the values
print("Welcome to the tipping system: \n")
print("Enter Bill amount(ksh): ")
bill = float(input())
print("Enter number of people splitting bill(valid answer is 1 and above): ")
people = int(input())


print('''Choose Option of tip as a percentage of the total bill amount
      \n 1. 10%\n 2. 12%\n 3. 15%\n
      reply with number''')

opt = input()
match opt:
    case "1":
        tip = bill*0.1
        payment = round((tip + bill)/people, 2)
        print(f"Each person should pay: Ksh.{payment}")
    case "2":
        tip = bill*0.12
        payment = round((tip + bill)/people, 2)
        print(f"Each person should pay: Ksh.{payment}")    
    case "3":
        tip = bill*0.15
        payment = round((tip + bill)/people, 2)
        print(f"Each person should pay: Ksh.{payment}")

        

