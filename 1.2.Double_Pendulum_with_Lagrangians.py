from vpython import *

# GlowScript 3.1 VPython

# scene.autoscale = False
# canvas(twidth=450, height=450, center=vec(0, -1.5, 0))

################################################################################
# WIDGETS

# Pause/play
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


# Determines how long the trail behind bob[2] is
def trail_length(s):
    bob[2].retain = s.value
    trail_length_button_caption.text = (
        "Trail = " + "{:1.0f}".format((s.value) / 10) + "\n\n"
    )


trail_length_button = slider(bind=trail_length, min=1, max=2000, value=250, step=10)
trail_length_button_caption = wtext(
    text="Trail = " + "{:1.0f}".format((trail_length_button.value) / 10) + "\n\n"
)


################################################################################
# SETUP

# Initial conditions and constants
g = 9.81
m = None, 1, 1
l = None, 2, 2
theta = None, (pi * 0.5), (pi * 0.75)
d_theta = None, 0, 0


bob = []

bob[1] = simple_sphere(
    pos=vec(l[1] * sin(theta[1]), -l[1] * cos(theta[1]), 0),
    radius=l[1] / 20.0,
    color=color.red,
)

bob[2] = simple_sphere(
    pos=bob[1].pos + vec(l[2] * sin(theta[2]), -l[2] * cos(theta[2]), 0),
    radius=l[2] / 20.0,
    color=color.green,
    make_trail=True,
    retain=250,
    interval=20,
    trail_type="points",
)


rod = []

rod[1] = cylinder(pos=vec(0, 0, 0), axis=bob[1].pos, radius=0.01, color=color.white,)


rod[2] = cylinder(
    pos=bob[1].pos, axis=bob[2].pos - bob[1].pos, radius=0.01, color=color.white,
)


## graph trajectory of second bob
# graph(xtitle='x-coordinate', ytitle='y-coordinate')
# pos_plot = gcurve(color=color.red)


################################################################################
# ANIMATION

# Time step
dt = 0.001

for time in range(0, 1000, dt):
    rate(1 / dt)

    # Calculate dd_theta values using Euler-Lagrange equations

    ## Common expressions

    ### Shorthand
    sin1 = sin(theta[1])
    cos1 = cos(theta[1])
    sin2 = sin(theta[2])
    cos2 = cos(theta[2])
    sin1m2 = sin(theta[1] - theta[2])
    cos1m2 = cos(theta[1] - theta[2])
    m12 = m[1] + m[2]

    ### Numerator terms
    A = m[2] * sin1m2 * cos1m2
    B = g * cos1m2
    C = sin1m2
    D = m12 * g

    ### Denominator terms
    E = m12 - m[2] * cos1m2 ** 2

    ## Calculations
    dd_theta = []

    dd_theta[1] = (
        (-A * l[1] * d_theta[1] ** 2)
        + (B * m[2] * sin2)
        + (-C * m[2] * l[2] * d_theta[2] ** 2)
        + (-D * sin1)
    ) / (E * l[1])

    dd_theta[2] = (
        (A * l[2] * d_theta[2] ** 2)
        + (B * sin1 * m12)
        + (C * l[1] * d_theta[1] ** 2 * m12)
        + (-D * sin2)
    ) / (E * l[2])

    # Euler's Method

    ## Update thetas
    d_theta[1] += dd_theta[1] * dt
    d_theta[2] += dd_theta[2] * dt

    theta[1] += d_theta[1] * dt
    theta[2] += d_theta[2] * dt

    ## Update bobs/rods
    bob[1].pos = vec(l[1] * sin(theta[1]), -l[1] * cos(theta[1]), 0)
    rod[1].axis = bob[1].pos

    bob[2].pos = bob[1].pos + vec(l[2] * sin(theta[2]), -l[2] * cos(theta[2]), 0)
    rod[2].pos = bob[1].pos
    rod[2].axis = bob[2].pos - bob[1].pos

    time += dt


#    # Update graph
#    pos_plot.plot(bob[2].pos.x, bob[2].pos.y)
