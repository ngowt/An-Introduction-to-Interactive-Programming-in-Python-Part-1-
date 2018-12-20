#1
import simplegui 

counter = 0

# Timer handler
def tick():
    global counter
    print counter
    counter += 1

# create timer
timer = simplegui.create_timer(1000, tick)
timer.start()

#2
import simplegui 

counter = 0

# Timer handler
def tick():
    global counter
    print counter
    counter += 1
    
# Event handlers for buttons
def resume():
    timer.start()
    
def pause():
    timer.stop()

def restart():
    global counter
    counter = 0
       
# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
resumeButton = frame.add_button('Resume', resume, 100)
pauseButton = frame.add_button('Pause', pause, 100)
restartButton = frame.add_button('Restart', restart, 100)
timer = simplegui.create_timer(1000, tick)
frame.start()

#3
import simplegui 

color = "Red"

# Timer handler
def tick():
    global color
    color = 'Blue' if color == 'Red' else 'Red'
    frame.set_canvas_background(color)
    
    
# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
timer = simplegui.create_timer(3000, tick)

# Start timer
frame.start()
timer.start()

#4
import simplegui 

WIDTH = 200
HEIGHT = 200
radius = 1


# Timer handler
def tick():
    global radius
    radius += 1
    
# Draw handler
def draw_handler(canvas):
    canvas.draw_circle((WIDTH / 2, HEIGHT / 2), radius, 1, 'Green')
        
# Create frame and timer
frame = simplegui.create_frame('#4', 200, 200)
timer = simplegui.create_timer(100, tick)
frame.set_draw_handler(draw_handler)

# Start timer
frame.start()
timer.start()

#5
import simplegui 

total_ticks = 0
first_click = True


# Timer handler
def tick():
    global total_ticks
    total_ticks += 1
    
# Button handler
def click():
    global first_click
    global total_ticks
    if first_click == True:
        first_click = False
        timer.start()
    else:
        first_click = True
        timer.stop()
        print 'Your reaction time is ' + str(total_ticks / 100.0) + 's'
        total_ticks = 0
        
# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
frame.add_button("Start/Stop", click, 200)
timer = simplegui.create_timer(10, tick)

# Start timer
frame.start()
