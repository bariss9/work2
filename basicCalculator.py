def basicCalculator(num1 , num2 , operation):
    if(operation == '+'):
        print(f"{num1} + {num2} = {num1 + num2}")
    if(operation == '-'):
         print(f"{num1} - {num2} = {num1 - num2}")
    if(operation == '*'):
        print(f"{num1} x {num2} = {num1 * num2}")
    if(operation == '/'):
        if(num2 == 0):
            print("Second number cannot 0 for division!")
            return False
        print(f"{num1} / {num2} = {num1 / num2}")

basicCalculator(1,4,'+')
basicCalculator(1,4,'-')
basicCalculator(1,4,'*')
basicCalculator(1,4,'/')
basicCalculator(1,0,'/')



