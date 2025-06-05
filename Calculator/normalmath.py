def yaku(number1,number2,operator):
    b = 0
    if operator == "+":
       b = number1 + number2
    elif operator == "-":
        b = number1 - number2
    elif operator =="*":
        b = number1 * number2
    elif operator =="/":
        b = number1 / number2 
    return b       

    
    







var = yaku(1,2,"/")
print(var)