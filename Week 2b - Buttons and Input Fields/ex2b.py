#1
import simplegui 

def print_hello():
    print "Hello"
    
def print_goodbye():
    print "Goodbye"

#2
import simplegui
color = ""

# Handlers for buttons
def set_red():
    global color
    color = "red"
    
def set_blue():
    global color
    color = "blue"
    
def print_color():
    print color

# Create frame
frame = simplegui.create_frame("Set and print colors", 200, 200)
frame.add_button('Red', set_red, 100)
frame.add_button('Blue', set_blue, 100)
frame.add_button('Print Color', print_color, 100)

# Start the frame animation
frame.start()

#3
import simplegui
count = 0

# Define event handlers for four buttons
def reset():
    global count
    count = 0

def increment():
    global count
    count += 1
    
def decrement():
    global count
    count -= 1
    
def print_count():
    global count
    print count
    
# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame('Q3', 400, 800)
frame.add_button('Increment', increment, 200)
frame.add_button('Decrement', decrement, 200)
frame.add_button('Print Count', print_count, 200)

# Start the frame animation
frame.start()

#4
import simplegui 

# Handlers for input field
def get_input(text):
    print text
    
# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Echo input", 200, 200)
input = frame.add_input("Input Field", get_input, 100)

# Start the frame animation
frame.start()

#5
import simplegui 

# Pig Latin helper function
def pig_latin(word):
    if word[0] != 'a' and word[0] != 'e' and word[0] != 'i' and word[0] != 'o' and word[0] != 'u':
        return word[1: ] + 'ay'
    return word + 'way'

# Handler for input field
def get_input(word):
    print pig_latin(word)

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Pig Latin translator", 400, 200)
inp = frame.add_input('Enter Word Here', get_input, 200)

# Start the frame animation
frame.start()