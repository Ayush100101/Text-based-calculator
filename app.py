def get_number(number):
 while True:
    number =  input("enter the first number" + str(number) + ":")
    try:
        return float(number)
        
    except:
        print("invalid output")   
number = get_number(1)
number2 = get_number(2)    
operation = input("enter the operation you want to perform: ")
result = 0
if operation == "+" :
   result = float(number) + float(number2)
   print(result)
elif operation == "-" :
   result = float(number) - float(number2)
   print(result)
elif operation == "/" :
   if float(number2) != 0:
        result = float(number) / float(number2)
        print(result)
   else:
        print("this division is not possible")
elif operation == "*" :
   result = float(number) * float(number2)
   print(result)

