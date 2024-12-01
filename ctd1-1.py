while True:
 mode = int(input("Enter 1 to convert from celsius to fahrenheit and 2 for vice versa, and enter 0 to exit"))
 if mode==0:
    break
 if mode==1:
     celsius = float(input("Enter your temperature in celsius"))
     farenheit = (celsius*(9.0/5.0)) + 32
     print("Temprature in farenheit: ")
     print(farenheit)
 elif mode==2:
     farenheit = float(input("Enter your temperature in farenheit"))
     celsius = (farenheit-32)*(5.0/9.0)
     print("Temprature in celsius: ")
     print(celsius)
 else: print("Invalid, please enter 1 or 2") 
