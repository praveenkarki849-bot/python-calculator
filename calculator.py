print("simple calculator")

while True :

  try :
        num1 = float(input("enter your first number :"))
        operators = input("enter operator (+,-,*,/,**,%,//):")
        num2 = float(input("enter your second number :"))

  except ValueError:
     print("Invalid input ! please enter numbers only .")
     continue

  if operators == "+" :
            print("result:",num1 + num2)

  elif operators == "-" :
    print("result:", num1 - num2)   

  elif operators == "*" :
    print("result:", num1 * num2)   

  elif operators == "/" :
    if num2 != 0 :
        print("result:", num1 / num2)
    else :
        print("cannot divide by zero !")

  elif operators == "**" :  
    print("result:",num1 ** num2)

  elif operators == "%" :
    if num2 != 0 :
        print("result:",num1 % num2)    
    else :
        print("cannot divide by zero !")            

  elif operators == "//" :
    if num2 != 0 :
        print("result:",num1 // num2)    
    else :
        print("cannot divide by zero !")  
    print("result:",num1 // num2)
  else :
    print("invalid operator")        

  choice = input("\nDo you want another calculation? (y/n): ")

  if choice.lower() != "y":
        print("Thank you for using the calculator!")
        break









