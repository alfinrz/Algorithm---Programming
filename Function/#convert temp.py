#convert temp

def convert_celcius(Tf):
    Tc = 5/9*(Tf-32)
    return Tc

def convert_kelvin(Tf):
    Tk = convert_celcius(Tf) + 273.15
    return Tk

def convert_temp():
    Tf = eval(input("Enter temperature in fahrenheit:"))
    
    print("The temperature in celcius is:", convert_celcius(Tf))
    print("The temperature in kelvin is:", convert_kelvin(Tf))

c = convert_temp()