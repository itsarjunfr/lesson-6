height = float(input('Enter you height in m: '))
weight = float(input('Enter your weight in kgs: '))
bmi = weight/(height**2)
print('Your BMI is:', bmi)
if bmi<18:
    print('You are underweight.')
elif 18<bmi and bmi<25:
    print('You are in the healthy range.')
elif 25<bmi and bmi<30:
    print('You are overweight.')
else:
    print('You are obese.')