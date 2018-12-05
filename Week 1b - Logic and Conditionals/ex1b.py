#1
def is_even(number):
    return number % 2 == 0

#2
def is_cool(name):
    return  name == 'Joe' or 
            name == 'John' or 
            name == 'Stephen'

#3
def is_lunchtime(hour, is_am):
    return is_am and (hour == 11 or hour == 12)

#4
def is_leap_year(year):
    return  (year % 400 == 0) or 
            (year % 4 == 0 and not year % 100 == 0)

#5
def interval_intersect(a, b, c, d):
    return (c <= b) and (a <= d)

#6
def name_and_age(name, age):
    if (age < 0):
        return 'Error: Invalid age'
    return name + ' is ' + str(age) + ' years old.'

#7
def print_digits(number):
    if (number < 0 or number >= 100):
        print 'Error: Input is not a two-digit number.'
        return
    print 'The tens digit is ' + str(number / 10) + ', and the ones digit is ' + str(number % 10) + '.'

#8
def name_lookup(first_name):
    if first_name == 'Joe':
        return 'Warren'
    elif first_name == 'Scott':
        return 'Rixner'
    elif first_name == 'John':
        return 'Greiner'
    elif first_name == 'Stephen':
        return 'Wong'
    else:
        return 'Error: Not an instructor'

#9
def pig_latin(word):
    if word[0] != 'a' and word[0] != 'e' and word[0] != 'i' and word[0] != 'o' and word[0] != 'u':
        return word[1: ] + 'ay'
    return word + 'way'

#10
import math
def smaller_root(a, b, c):
    discriminant = (b ** 2) - 4 * a * c
    if (discriminant < 0):
        return 'Error: No real solutions'
    else:
        sol1 = -b - math.sqrt(discriminant) / (2 * a)
        sol2 = -b + math.sqrt(discriminant) / (2 * a)
        if sol1 < sol2:
            return sol1
        else:
            return sol2

#10 (Ternary Solution)
import math
def smaller_root(a, b, c):
    discriminant = (b ** 2) - 4 * a * c
    if (discriminant < 0):
        return 'Error: No real solutions'
    else:
        sol1 = -b - math.sqrt(discriminant)) / 2 * a
        sol2 = -b + math.sqrt(discriminant)) / 2 * a
        lesserRoot = sol1 if sol1 < sol2 else sol2
        return lesserRoot
    
