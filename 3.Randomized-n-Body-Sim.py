from vpython import *
#GlowScript 3.1 VPython

################################################################################
# FUNCTIONS

# Calculate the force vector exerted on b1 by b2
def f_g(b1, b2):
    # If you're calculating the force of a body on itself
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

posmin = -0.5
posmax = 0.5
massmin = 1
massmax = 5
velmin = -3
velmax = 3

numbodies = input("Number of bodies to simulate (recommended 4)")

for i in range(numbodies):
    
    m = massmin + random()*(massmax-massmin)
    
    bodies.append(
        sphere(
            pos = vec(
                posmin + random()*(posmax-posmin),
                posmin + random()*(posmax-posmin),
                posmin + random()*(posmax-posmin)
            ),
            radius = 0.03,
            color = vec(random(),random(),random()),
            mass = m,
            p = vec(
                m * (velmin + random()*(velmax-velmin)),
                m * (velmin + random()*(velmax-velmin)),
                m * (velmin + random()*(velmax-velmin)),
            ),
            make_trail = True,
            # retain = 500,
        )
    )
    
    print(bodies[i].pos)
    print(bodies[i].mass)
    print(bodies[i].p)




################################################################################
# EULER'S METHOD (ANIMATION)

t = 0
dt = 0.00001

while True:
    rate(30/dt)
    
    
    # Calculate net force at a moment
    for b1 in bodies: # The body whose net force we want to calculate
        b1.force = vec(0,0,0)
        for b2 in bodies: # The bodies that exert a gravitational force on b1
            b1.force = b1.force + f_g(b1,b2)
    
    
    # Update momentum
    for b in bodies:
        b.p = b.p + b.force * dt


    # Update positions (animate)
    for b in bodies:
        b.pos = b.pos + (b.p/b.mass) * dt
   
   
    # Increment time
    t = t + dt
    



