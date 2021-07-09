from vpython import *

# GlowScript 3.1 VPython

################################################################################
# WIDGETS

running = True


def Run(b):  # b = button
    global running, remember_dt, dt
    running = not running
    if running:
        b.text = "Pause"
        dt = remember_dt
    else:
        b.text = "Run"
        remember_dt = dt
        dt = 0
    return


button(text="Pause", bind=Run)


################################################################################
# FUNCTIONS

# Calculate the force vector exerted on b1 by b2
def f_g(b1, b2):
    # If you're calculating the force of a body on itself
    if b1.pos == b2.pos:
        return vec(0, 0, 0)
    # Use 6.67430E-11 for real world values; 1 is more convenient
    G = 1
    # Vector from b1 to b2
    r_vec = b2.pos - b1.pos
    # Equation for magnitude of the force of gravity
    force_mag = G * b1.mass * b2.mass / mag(r_vec) ** 2
    # Unit vector from b1 to b2 (same direction, but length 1)
    r_hat = r_vec / mag(r_vec)
    # Make the magnitude into a vector pointing towards b2
    force_vec = force_mag * r_hat
    # Return the force vector
    return force_vec


################################################################################
# BODIES

bodies = []

# index 0:
bodies.append(
    sphere(
        pos=vec(0, 0, 0),
        radius=0.03,
        color=color.orange,
        mass=1,
        # p = vec(-0.3,0.5,0.3), # momentum
        p=vec(0.3, 0.5, 0.3),
        make_trail=True,
    )
)


# index 1:
bodies.append(
    sphere(
        pos=vec(0.3, 0, 0),
        radius=0.03,
        color=color.green,
        mass=1,
        # p = vec(0.2,-0.3,0),
        p=vec(0.2, -0.3, 0),
        make_trail=True,
    )
)

# index 2:
bodies.append(
    sphere(
        pos=vec(-1, 0.4, 0),
        radius=0.03,
        color=color.red,
        mass=2,
        # p = vec(-1,0.4,0),
        p=vec(1, 0.4, 0),
        make_trail=True,
    )
)


# conservation of momentum check
print("Initial Momentum: ")
print("Components: " + str(bodies[0].p + bodies[1].p + bodies[2].p))
print("Magnitude: " + str(mag(bodies[0].p + bodies[1].p + bodies[2].p)))

################################################################################
# EULER'S METHOD (ANIMATION)

t = 0
dt = 0.00001

while True:
    rate(30 / dt)

    # Calculate net force at a moment
    for b1 in bodies:  # The body whose net force we want to calculate
        b1.force = vec(0, 0, 0)
        for b2 in bodies:  # The bodies that exert a gravitational force on b1
            b1.force = b1.force + f_g(b1, b2)

    # Update momentum
    for b in bodies:
        b.p = b.p + b.force * dt

    # Update positions (animate)
    for b in bodies:
        b.pos = b.pos + (b.p / b.mass) * dt

    # Increment time
    t = t + dt

