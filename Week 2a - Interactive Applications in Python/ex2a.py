#1
def print_goodbye():
    message = "Goodbye"
    print message

#2
def set_goodbye():
    global message
    message = "Goodbye"
    print message

#3
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

#4
import simplegui
message = "My first frame!"

# Handler for mouse click
def click():
    print message

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("My first frame", 100, 200)
frame.add_button("Click me", click)
frame.start()

#5
import simplegui 
message = "My second frame!"
frame = simplegui.create_frame(message, 200, 100)

# Handler for mouse click
def click():
    print message

# Assign callbacks to event handlers
frame.add_button("Click me", click)

# Start the frame animation
frame.start()