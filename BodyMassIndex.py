height= input ("Enter height : ")
height=float(height)
weight= input ("Enter weight : ")
weight=float(weight)
BMI=weight/(height**2)
print (BMI)
if BMI<18:
    print (f" Having {BMI} BMI - person is underweight")
if BMI>=18 and BMI<=25:
    print (f" Having {BMI} BMI - person is normal")
elif BMI>25 and BMI<=29:
    print (f" Having {BMI} BMI - person is overweight")
elif BMI>29:
    print (f" Having {BMI} BMI - person is fat")



