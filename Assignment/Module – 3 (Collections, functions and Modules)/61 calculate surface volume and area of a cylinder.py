# 1). Write a Python program to calculate surface volume and area of a cylinder ?

"""
Note :- A cylinder is one of the most basic curvilinear geometric shapes, 
                        the surface formed by the points at a fixed distance from a given straight line, the axis of the cylinder.
FORMULA OF SURFACE VOLUME AND AREA OF A CYLINDER :
                            Volume = ( pi * radian * radian * height )
                            Surface Area = (( 2 * pi * radian ) * height ) + (( pi * radian ** 2 ) * 2 )
""" 

pi=22/7

height = float(input('Height of cylinder: '))
radian = float(input('\nRadius of cylinder: '))

volume = pi * radian * radian * height
sur_area = ((2*pi*radian) * height) + ((pi*radian**2)*2)

print("\nVolume is: ", volume)
print("Surface Area is: ", sur_area)
