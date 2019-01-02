#1
prime_numbers = [2, 3, 5, 7, 11, 13]
print prime_numbers[1], prime_numbers[3], prime_numbers[5]

#2
a = [5, 3, 1, -1, -3, 5]
b = a
b[0] = 0
print a

# Since b is pointing to the same list as a, modifying b[0] is also modifying a[0]. 
# Therefore when we changed b[0] = 0, we also changed a[0] = 0

#3
a = [5, 3, 1, -1, -3, 5]
b = list(a)
b[0] = 0
print a

# Calling the list() function creates a new copy of the list passed in the argument, 
# since both a and b are pointing to different objects. Modifying b[0] does not modify a[0]

#4
def add_vector(v, w):
    return [v[0] + w[0], v[1] + w[1]]

#5
import simplegui

# Initialize two counters.
counter1 = [0, 0]
counter2 = list(counter1)


# Define event handlers.
def start1():
    timer1.start()
    
def stop1():
    timer1.stop()
    
def start2():
    timer2.start()
    
def stop2():
    timer2.stop()
    
def tick1():
    global counter
    if counter1[1] == 9:
        counter1[0] += 1
        counter1[1] = 0
    else:
        counter1[1] += 1

def tick2():
    global counter
    if counter2[1] == 9:
        counter2[0] += 1
        counter2[1] = 0
    else:
        counter2[1] += 1
        
        
# Define draw handler.
def draw(canvas):
    canvas.draw_text("Timer 1:     " + str(counter1[0] % 10) + "." + str(counter1[1]), [50, 100], 24, "White")
    canvas.draw_text("Timer 2:     " + str(counter2[0] % 10) + "." + str(counter2[1]), [50, 200], 24, "White")

# Register event handlers.
frame = simplegui.create_frame("Mystery bug", 300, 300)
frame.add_button("Start timer1", start1, 200)
frame.add_button("Stop timer1", stop1, 200)
frame.add_button("Start timer2", start2, 200)
frame.add_button("Stop timer2", stop2, 200)
frame.set_draw_handler(draw)

timer1 = simplegui.create_timer(100, tick1)
timer2 = simplegui.create_timer(100, tick2)


# Start frame.
frame.start()