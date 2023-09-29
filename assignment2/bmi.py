#Kanyi Mwenda sct211-0012/2022

print("The BMI calculator is running!\n")
print("Enter Your weight(in kg): ")
weight = float(input())
print("Enter Your height(in cm): ")
height = float(input())/100.0
bmi = round(weight/(height**2), 1)
if bmi < 18.5:
    print(f"Your bmi is: {bmi}\n You are : underweight")

elif bmi >= 18.5 and  bmi<25.0:
    print(f"Your bmi is: {bmi}\n You are : normal weight")

else:
    print(f"Your bmi is: {bmi}\n You are :  Overweight")    
        