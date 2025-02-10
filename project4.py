# Project 4 By FA24-BCS-110
while(True):          
    value=input("Enter the unit (kgs, lbs, celsius, fahrenheit,ft, inch, cm) or write 'stop' if you want to exit:")
    if value=="kgs":
        kgs=float(input("Enter The Amount in Kgs: "))
        lbs=kgs*2.20462
        print("Amount in Pounds is: ", lbs)
    elif value=="lbs":
        lbs=float(input("Enter the Amount in pounds: "))
        kgs=lbs/2.20462
        print("The amount in kgs is: ", kgs)
    elif value=="celsius":
        celsius=float(input("Enter the temperature in Celsius: "))
        fahrenheit=(celsius*(9/5))+32
        print("The Temperature in fahrenheit is: ", fahrenheit)
    elif value=="fahrenheit":
        fahrenheit=float(input("Enter the temperature in Fahrenheit: "))
        celsius =(fahrenheit-32)*5/9
        print("The Temperature in celsius is: ", celsius)
    elif value=="inch":
        inch=float(input("Enter Your length in inches: "))
        cm=inch*2.54
        print("The length in centimeter is: ", cm)
    elif value=="cm":
        cm=float(input("Enter your length in centimeters: "))
        inch=cm/2.54
        print("The length in inches is: ", inch)
    elif value=="ft":
        ft=float(input("Enter your length in feet: "))
        inch=float(input("'"))
        total=(ft*12)+inch
        print("The length in inches is: ", total)
    elif value=="stop":
        break    
    else:
        print("Invalid Input.")