score = int(input('enter your score'))
if score > 85 and score <= 100:
    print('grade is A')
elif score > 70 and score <= 85:
    print('grade is B')
elif score > 50 and score <= 70:
    print('grade is C')
elif score <= 50:
    print('grade is D')