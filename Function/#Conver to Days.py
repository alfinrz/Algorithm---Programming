#Conver to Days

def get_days(h,m,s):
    h = h * 60 *60
    m = m * 60
    s = s
    x = h + m + s
    return x
def convert_to_days():
    h = eval(input("Enter number of hours:"))
    m = eval(input("Enter number of minutes:"))
    s = eval(input("Enter number of seconds:"))
    tts = get_days(h,m,s)
    d = tts / 86400
    print("Number of days is: %.4f"% d)

D = convert_to_days()
