#weight calculator


def calc_weight_planet(w,g2=23.1):
    w = eval(input("Enter your weight in pound:"))
    g1 = 9.8
    g2 = 23.1
    m = (w * g2)/g1
    print(m)

g1 = 9.8

g = 9.8

c = calc_weight_planet(w,g1)