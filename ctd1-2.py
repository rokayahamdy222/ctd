numbers = []
while True:
    userinput = input("Enter your number or press 'q' to quit: ")
    
    if userinput.lower() != 'q':
     number = int(userinput)
     numbers.append(number)
        
    else:
       break
         

if numbers: 
    largest = max(numbers)
    smallest = min(numbers)
    print(f"The largest number is: {largest}")
    print(f"The smallest number is: {smallest}")
else:
    print("No numbers were entered.")