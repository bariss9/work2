def basicCalculator(num1, num2, operation):
    operations = {'+', '/', '*', '-'}  
    
    if operation in operations:
        if operation == '+':
            print(f"{num1} + {num2} = {num1 + num2}")
        elif operation == '-':
            print(f"{num1} - {num2} = {num1 - num2}")
        elif operation == '*':
            print(f"{num1} x {num2} = {num1 * num2}")
        elif operation == '/':
            if num2 == 0:
                print("Second number cannot be 0 for division!")
                return False
            print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Invalid Operation!")
        return False
        
basicCalculator(1, 4, '+')
basicCalculator(1, 4, '-')
basicCalculator(1, 4, '*')
basicCalculator(1, 4, '/')
basicCalculator(1, 0, '/')  
basicCalculator(1, 4, '%')  




