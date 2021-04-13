#   IMPORT MATH MODULE SO WE HAVE ACCESS TO THE METHODS AND PROPERTIES INSIDE
import math

#   GET THE RADIUS FROM THE USER
radius = input()
#   CONVERT radius FROM A STRING TO AN INT
radius = int(radius)
#   TO CALCULATE THE AREA OF A CIRCLE - USE pi * r SQUARED
area = math.pi * pow(radius, 2)
print(area)









#   TASK 2 - SAMPLE ANSWER
#   TAKE THE USER INPUT AND CONVERT IT TO A INTEGER
radius = int(input("Please input the radius: "))
_pi = 3.14
area = _pi * radius ** 2
print("THe area of the circle is: " + str(area))



#   TASK 3 - MY ANSWER
#   CALCULATE DIAMETER
print("The diameter is: " + str(radius * 2))

#   CALCULATE CIRCUMFERENCE
#   USE THE FORMULA - 2 * pi * radius
circumerence = 2 * _pi * radius
print("The circumference is: " + str(circumerence))