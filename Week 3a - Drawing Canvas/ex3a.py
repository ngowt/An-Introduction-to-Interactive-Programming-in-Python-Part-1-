#1
import simplegui 

# Draw handler
def draw(canvas):
    canvas.draw_text("It works!",[120, 112], 48, "Red")
    

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("It works", 400, 200)
frame.set_draw_handler(draw)
frame.start()

#2
import simplegui 

# Draw handler
def draw(canvas):
    canvas.draw_text("This is easy", [100, 50], 48, "Red")
    

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("This is easy", 400, 200)
frame.set_draw_handler(draw)


# Start the frame animation
frame.start()

#3
import simplegui 

# Draw handler
def draw(canvas):
    canvas.draw_text('X', [0, 32], 48, 'Red')

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Ex3", 96, 96)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()

#4
def format_time(seconds):
    mins = seconds / 60
    secs = seconds % 60
    return str(mins) + ' minutes and ' + str(secs) + ' seconds'

#5
import simplegui 

# Define globals - Constants are capitalized in Python
HEIGHT = 400
WIDTH = 400
RADIUS_INCREMENT = 5
ball_radius = 20

# Draw handler
def draw(canvas):
    canvas.draw_circle((WIDTH / 2, HEIGHT / 2), ball_radius, 1, 'Green')
    
# Event handlers for buttons
def increase_radius():
    global ball_radius
    global RADIUS_INCREMENT
    ball_radius += RADIUS_INCREMENT
    
def decrease_radius():
    global ball_radius
    global RADIUS_INCREMENT
    
    if ball_radius - RADIUS_INCREMENT <= 0:
        ball_radius = 1
    else:
        ball_radius -= RADIUS_INCREMENT

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Ball control", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.add_button("Increase radius", increase_radius)
frame.add_button("Decrease radius", decrease_radius)

# Start the frame animation
frame.start()