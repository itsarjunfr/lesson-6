marks = int(input('Enter marks: '))
if marks<0 or marks>100:
    print('Enter valid mark.')
income = int(input('Enter monthly gross household income: '))
if income<0:
    print('Enter valid income.')
attendance = int(input('Enter attendance rate: '))
if attendance<0 or attendance>100:
    print('Enter valid attendance.')
if marks>=85 and income<=2500 and attendance>=75:
    print('You are eligible for th4e scholarship.')
if marks>=75 and income<=3500 and attendance>=75:
    print('You are in the waiting list to receive the scholarship.')
else:
    print('You are not eligible for this scholarship.')