first_number=int(input("Enter first number:",))
second_number=int(input("Enter second number:",))
third_number=int(input("Enter third number:",))
if((first_number>second_number)or(first_number>third_number)):
    print("First number entered was greatest which was:",first_number)
elif((second_number>first_number)or (second_number> third_number)):
    print("Second number entered was greatest which was:",second_number)
elif((third_number>first_number)or(third_number>second_number)):
    print("Third number entered was greatest which was:",third_number)
else:
    print("Enter valid input.")