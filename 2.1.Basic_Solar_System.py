from vpython import *

# GlowScript 3.1 VPython

################################################################################
# WIDGETS

# Determines how long the trail behind each planet is
def trail_length(s1):
    for b in bodies:
        b.retain = s1.value
    trail_length_slider_caption.text = (
        "Trail = " + "{:1.0f}".format((s1.value - 1) / 10) + "\n\n"
    )


trail_length_slider = slider(bind=trail_length, min=1, max=3001, value=101, step=10)
trail_length_slider_caption = wtext(
    text="Trail = " + "{:1.0f}".format((trail_length_slider.value - 1) / 10) + "\n\n"
)


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


# def set_speed(s2):
#    speed = s2.value
#    set_speed_slider_caption.text = (
#        "Speed = " + "{:1.2f}".format(s2.value) + "\n\n"
#    )
#
#
# set_speed_slider = slider(bind=set_speed, min=1, max=10000, value=200, step=100)
# set_speed_slider_caption = wtext(
#    "Speed = " + "{:1.2f}".format(set_speed_slider.value) + "\n\n"
# )


################################################################################
# FUNCTIONS

# Calculate the force vector exerted on b1 by b2
def f_g(b1, b2):
    # The force of a body on itself is 0
    if b1.pos == b2.pos:
        return vec(0, 0, 0)

    # Use 6.67430E-11 for real world values; 1 is more convenient
    G = 1

    # Vector from b1 to b2
    r_vec = b2.pos - b1.pos

    # Prevent gravitational force becoming absurdly large when bodies pass through each other
    if mag(r_vec) < (b1.radius + b2.radius):
        r_mag = b1.radius + b2.radius
    else:
        r_mag = mag(r_vec)

    # Equation for magnitude of the force of gravity
    force_mag = (G * b1.mass * b2.mass) / (r_mag ** 2)
    # Unit vector from b1 to b2 (same direction, but length 1)
    r_hat = r_vec / mag(r_vec)
    # Make the magnitude into a vector pointing towards b2
    force_vec = force_mag * r_hat

    # Return the force vector
    return force_vec


################################################################################
# BODIES (planetry)

bodies = []

# index 0: star (same star from demo 1)
bodies.append(
    simple_sphere(
        pos=vec(0, 0, 0),
        radius=0.3,
        color=color.yellow,
        mass=1000,
        p=vec(0, 0, 0),  # momentum
        make_trail=True,
        retain=trail_length_slider.value,
    )
)


# index 1: dark red planet
bodies.append(
    simple_sphere(
        pos=vec(1, 0, 0),  # pos=vec(1, 0, -0.2), is a bit more realistic
        radius=0.1,
        color=vec(0.545, 0, 0),
        mass=1,
        p=vec(0, 30, 0),
        make_trail=True,
        retain=(
            trail_length_slider.value / 15
        ),  # retain= (trail_length_slider.value ** (1/3)),
    )
)

# index 2: cyan planet
bodies.append(
    simple_sphere(
        pos=vec(0, 3, 0.2),  # vector(1,0.7,0.2) very interesting!!!!
        radius=0.09,
        color=color.cyan,
        mass=2,
        p=vec(-35, 0, -1),
        make_trail=True,
        retain=trail_length_slider.value,
    )
)

# index 3: orange planet
bodies.append(
    simple_sphere(
        pos=vec(0, -4, 0.5),
        radius=0.1,
        color=color.orange,
        mass=10,
        p=vec(160, 0, -3),
        make_trail=True,
        retain=trail_length_slider.value,
    )
)

# index 4: comet
bodies.append(
    simple_sphere(
        pos=vec(-6, 6, 0),
        radius=0.05,
        color=color.white,
        mass=0.5,
        p=vec(-1, -1, 0.25),
        make_trail=True,
        retain=trail_length_slider.value,
    )
)

## OPTIONAL TAIL FOR COMET

tail = cone(
    pos=bodies[4].pos,
    axis=bodies[4].pos - bodies[0].pos,
    size=vec(1, 1, 1) * bodies[4].radius,
    color=color.white,
)


# # index 4: purple
# bodies.append(
#     simple_sphere(
#         pos=vec(0, -7, -0.5),
#         radius=0.1,
#         color=color.purple,
#         mass=30,
#         p=vec(400, 0, 0),
#         make_trail=True,
#         retain=trail_length_slider.value,
#     )
# )


################################################################################
# ASTEROID BELT

asteroids = []

pos_min = 6
pos_max = 7
mass_min = 0.01
mass_max = 0.10

for i in range(100):

    this_pos = pos_min + random() * (pos_max - pos_min)
    this_theta = 2 * pi * random()
    this_mass = mass_min + random() * (mass_max - mass_min)
    this_p = this_mass * sqrt(bodies[0].mass / this_pos)

    asteroids.append(
        simple_sphere(
            pos=this_pos * vec(cos(this_theta), sin(this_theta), 0),
            radius=0.03,
            color=color.white,
            mass=this_mass,
            p=this_p * vec(-sin(this_theta), cos(this_theta), 0),
        )
    )


################################################################################
# EULER'S METHOD (ANIMATION)

t = 0
dt = 0.001

speed = 1 / (5 * dt)

while True:
    rate(speed)

    # Calculate net force at a moment
    for b1 in bodies:  # The body whose net force we want to calculate
        b1.force = vec(0, 0, 0)  # Each body starts with a net force of 0
        for b2 in bodies:  # The bodies that exert a gravitational force on b1
            b1.force += f_g(b1, b2)  # A net force is the sum of component forces

    for a in asteroids:
        a.force = vec(0, 0, 0)
        for b in bodies:
            a.force += f_g(a, b)

    # Update momentum
    for b in bodies:
        b.p += b.force * dt

    for a in asteroids:
        a.p += a.force * dt

    # Update positions (animate)
    for b in bodies:
        b.pos += (b.p / b.mass) * dt

    for a in asteroids:
        a.pos += (a.p / a.mass) * dt

    # OPTIONAL TAIL FOR COMET
    tail.pos = bodies[4].pos + bodies[4].radius * vec(1, 1, 1)
    tail.axis = bodies[4].pos - bodies[0].pos
    tail.axis = tail.axis / mag(tail.axis)

    # Increment time
    t = t + dt
