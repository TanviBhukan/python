pi=22/7
radian = float(input('Radius of sphere: '))
s_area = 4 * pi * radian **2
volume = (4/3) * (pi * radian ** 3)
print("Surface Area is: ", s_area)
print("Volume is: ", volume)
# find area
# total surface area of cube
def areaCube( a ):
    return (a * a * a)
def surfaceCube( a ):
    return (8 * a * a)
a = 4
print("Area =", areaCube(a))
print("Total surface area =", surfaceCube(a))