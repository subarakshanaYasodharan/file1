weight=float(input("enter weight in kgs  "))
height=float(input("enter height in meters  "))
BMI=weight/(height)**2
if BMI <= 18.5:  
    print("You are underweight.")  
elif BMI <= 24.9:  
    print("You are healthy.")  
elif BMI <= 29.9:  
    print("You are overweight.")  
else:  
    print("You are obese.")