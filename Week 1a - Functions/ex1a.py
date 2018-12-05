#1 
def miles_to_feet (miles):
    return miles * 5280

#2
def total_seconds(hours, minutes, seconds):
    return (hours * 60 * 60) + (minutes * 60) + seconds

#3
def rectangle_perimeter(width, height):
    return (2 * width) + (2 * height)

#4
def rectangle_area(width, height):
    return width * height

#5
import math
def circle_circumference(radius):
    return  2 * math.pi * radius

#6
import math
def circle_area(radius):
    return  math.pi * radius ** 2

#7
import math
def future_value(present_value, annual_rate, years):
    return present_value * ((1 + annual_rate/100.00) ** years)

#8
def name_tag(first_name, last_name):
    return 'My name is ' + first_name + ' ' + last_name 

#9
def name_and_age(name, age):
    return name + ' is ' + str(age) + ' years old.'

#10
import math
def point_distance(x0, y0, x1, y1):
    return math.sqrt((y1 - y0) ** 2 + (x1 - x0) ** 2)

#11 
import math
def triangle_area(x0, y0, x1, y1, x2, y2):
    distanceA = math.sqrt( (x0 - x1)**2 + (y0 - y1)**2 )
    distanceB = math.sqrt( (x1 - x2)**2 + (y1 - y2)**2 )
    distanceC = math.sqrt( (x0 - x2)**2 + (y2 - y0)**2 )
    s = 0.5 * (distanceA + distanceB + distanceC)
    area = math.sqrt( s * (s - distanceA) * (s - distanceB) * (s - distanceC) )
    return area

#12
def print_digits(number):
    tens = number // 10
    remainder = number % 10
    print 'The tens digit is ' + str(tens) + ' and the ones digit is ' + str(remainder) + '.'

#13
import random
def powerball():
    random.seed()
    no1 = str(random.randint(1, 59))
    no2 = str(random.randint(1, 59))
    no3 = str(random.randint(1, 59))
    no4 = str(random.randint(1, 59))
    no5 = str(random.randint(1, 59))
    pball = str(random.randint(1, 35))
    print "Today's number are " + no1 + ", " + no2 + ", " + no3 + ", " + no4 + ", " + no5 + ". The Powerball number is " + pball + "."
    