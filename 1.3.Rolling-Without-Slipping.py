from vpython import *

# GlowScript 3.1 VPython

################################################################################
# INPUTS

# These two determine the pattern you trace
inner_radius = 1
outer_radius = 2 * sqrt(2)

################################################################################
# CREATE OBJECTS

# Thickness of lines
draw_size = 0.01

# Create outer circle
outer_points = []
d_theta = 0.01
for theta in range(0, 2 * pi, d_theta):
    outer_points.append(outer_radius * vec(cos(theta), sin(theta), 0))
# outer_points.append(vec(1,0,0))
outer_circle = curve(color=color.white, pos=outer_points)

# Create inner disk
inner_circle = cylinder(
    texture=textures.wood,
    axis=vec(0, 0, draw_size),
    opacity=0.5,
    size=vec(draw_size, 2 * inner_radius, 2 * inner_radius),
    pos=vec(outer_radius - inner_radius, 0, 0),
    theta=0,
    omega=1,
    make_trail=False,
)

# Draw point on edge being "traced"
rod = cylinder(
    color=color.white,
    axis=vec(1, 0, 0),
    pos=inner_circle.pos,
    size=vec(inner_radius, draw_size, draw_size),
    theta=0,
)

# Calculate inner circle rotation speed to roll without slipping
rod.omega = -inner_circle.omega * ((outer_radius - inner_radius) / inner_radius)

# Create point to trace hypocyloid
point = sphere(
    radius=draw_size,
    color=color.red,
    make_trail=True,
    pos=rod.pos + rod.axis,
    retain=2000,
)

################################################################################
# ANIMATE

dt = 0.01
t = 0
scene.autoscale = False

while True:
    rate(1000)

    # Update angular velocity
    inner_circle.theta += inner_circle.omega * dt
    rod.theta += rod.omega * dt

    # Move & rotate inner cicle
    inner_circle.pos = (outer_radius - inner_radius) * vec(
        cos(inner_circle.theta), sin(inner_circle.theta), 0
    )
    inner_circle.rotate(angle=rod.omega * dt, axis=vec(0, 0, 1))

    # Move & rotate rod/ point
    rod.pos = inner_circle.pos
    rod.axis = rod.size.x * vec(cos(rod.theta), sin(rod.theta), 0)
    point.pos = rod.pos + rod.axis

    t += dt
