#1
feet = miles * 5280

#2
total_seconds = (hours * 60 * 60) + (minutes * 60) + seconds

#3
perimeter = (2 * width) + (2 * height)

#4
area = width * height

#5
circumference = 2 * PI * radius

#6
area = PI * 8 ** 2

#7
future_value = present_value * (1 + 0.01 * annual_rate) ** years

#8
name_tag = "Hi, my name is " + first_name + " " + last_name

#9
statement = name + " is " + str(age) + " years old."

#10
import math
distance = math.sqrt( (x0 - x1)**2 + (y0 - y1)**2 )

#Challenge
import math
distanceA = math.sqrt( (x0 - x1)**2 + (y0 - y1)**2 )
distanceB = math.sqrt( (x1 - x2)**2 + (y1 - y2)**2 )
distanceC = math.sqrt( (x0 - x2)**2 + (y2 - y0)**2 )
s = 0.5 * (distanceA + distanceB + distanceC)
area = math.sqrt( s * (s - distanceA) * (s - distanceB) * (s - distanceC) )