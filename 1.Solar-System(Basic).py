from vpython import *
#GlowScript 3.1 VPython


################################################################################
# WIDGETS


# Determines how long the trail behind each planet is
def trail_length(s):
    for b in bodies:
        b.retain = s.value
    trail_length_button_caption.text = "Trail = "+"{:1.2f}".format((s.value-1)/10)+"\n\n"

trail_length_button = slider(bind=trail_length, min=1, max=5001, value=51, step = 10)
trail_length_button_caption = wtext(text="Trail = "+"{:1.2f}".format((trail_length_button.value-1)/10)+"\n\n")




################################################################################
# FUNCTIONS

# Calculate the force vector exerted on b1 by b2
def f_g(b1, b2):
    # The force of a body on itself is 0
    if (b1.pos == b2.pos):
        return vec(0,0,0)
    # Use 6.67430E-11 for real world values; 1 is more convenient
    G = 1
    # Vector from b1 to b2
    r_vec = b2.pos - b1.pos
    # Equation for magnitude of the force of gravity
    force_mag = G * b1.mass * b2.mass / mag(r_vec)**2
    # Unit vector from b1 to b2 (same direction, but length 1)
    r_hat = r_vec/mag(r_vec)
    # Make the magnitude into a vector pointing towards b2
    force_vec = force_mag * r_hat
    # Return the force vector
    return force_vec


################################################################################
# BODIES

bodies = []


# index 0: star (same star from demo 1)
bodies.append(
    sphere(
        pos = vec(0,0,0),
        radius = 0.3,
        color = color.yellow,
        mass = 1000,
        p = vec(0,0,0), # momentum
        make_trail = True,
        retain = trail_length_button.value
    )
)


# index 1: green planet (same planet from demo 1)
bodies.append(
    sphere(
        pos = vec(1,0,0),
        radius = 0.1,
        color = color.green,
        mass = 1,
        p = vec(0,30,0),
        make_trail = True,
        retain = trail_length_button.value
    )
)

# index 2: red planet
bodies.append(
    sphere(
        pos = vec(0,3,0),
        radius = 0.09,
        color = color.red,
        mass = 2,
        p = vec(-35,0,0),
        make_trail = True,
        retain = trail_length_button.value
    )
)

# index 3: orange planet
bodies.append(
    sphere(
        pos = vec(0,-4,0),
        radius = 0.1,
        color = color.orange,
        mass = 10,
        p = vec(160,0,0),
        make_trail = True,
        retain = trail_length_button.value
    )
)

# index 4: comet
bodies.append(
    sphere(
        pos = vec(-6,6,0),
        radius = 0.05,
        color = color.white,
        mass = 0.5,
        p = vec(-1,-1,0),
        make_trail = True,
        retain = trail_length_button.value
    )
)




# OPTIONAL TAIL FOR COMET

tail = cone(
    pos = bodies[4].pos, 
    axis = bodies[4].pos - bodies[0].pos, 
    size = vec(1,1,1) * bodies[4].radius, 
    color = color.white,
)



################################################################################
# EULER'S METHOD (ANIMATION)

t = 0
dt = 0.001

while True:
    rate(1/(5*dt))
    
    
    # Calculate net force at a moment
    for b1 in bodies: # The body whose net force we want to calculate
        
        b1.force = vec(0,0,0) # Each body starts with a net force of 0
        
        for b2 in bodies: # The bodies that exert a gravitational force on b1
            b1.force = b1.force + f_g(b1,b2) # A net force is the sum of component forces
    
    
    
    # Update momentum
    for b in bodies:
        b.p = b.p + b.force * dt



    # Update positions (animate)
    for b in bodies:
        b.pos = b.pos + (b.p/b.mass) * dt
        
        
        
#    OPTIONAL TAIL FOR COMET
    
    tail.pos = bodies[4].pos + bodies[4].radius * vec(1,1,1)
    tail.axis = bodies[4].pos - bodies[0].pos
    tail.axis = tail.axis / mag(tail.axis)
    
    
    
    # Increment time
    t = t + dt
    



