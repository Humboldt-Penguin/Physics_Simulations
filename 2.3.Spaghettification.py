from vpython import *

# GlowScript 3.1 VPython

# Space themed background
scene.autoscale = False
sphere(pos=vec(1,1,1), radius=50, texture="https://i.imgur.com/f83bQ2P.png")

# canvas( background = vec(0.2, 0.2, 0.2) )

################################################################################
# FUNCTIONS

# Calculate the force vector exerted on b1 by b2
def f_g(b1, b2):
    if b1.pos == b2.pos:
        return vec(0, 0, 0)  # The force of a body on itself is 0
    G = 1  # Use 6.67430E-11 for real world values; 1 is more convenient
    r_vec = b2.pos - b1.pos  # Vector from b1 to b2
    return ((G * b1.mass * b2.mass) / (mag(r_vec) ** 2)) * hat(
        r_vec
    )  # Equation for gravity force vector


# Calculate the spring force exerted on spring s1 by spring s2, which represents the force holding your body together
def f_s(s1, s2):
    r_vec = s2.pos - s1.pos
    force_vec = (
        -k * (mag(r_vec) - dy) * hat(r_vec)
    )  # Spring force according to Hooke's Law
    return force_vec


################################################################################
# CREATING OBJECTS

# Atoms representing the human body
atoms = []
y_pos = 3
dy = 0.25

# fmt: off
while y_pos < 5.51:
    atoms.append(
        simple_sphere(
            pos=vec(-1, y_pos, 0), 
            v=vec(0, 0, 0), 
            mass=1.0, 
            radius=0.1, 
            color=color.red,
        )
    )

    y_pos += dy
# fmt: on


# Springs representing force that holds the atoms in the body together
springs = []
k = 1.0

for i in range(0, len(atoms) - 1):
    springs.append(
        helix(
            pos=atoms[i].pos,
            axis=atoms[i + 1].pos - atoms[i].pos,
            radius=atoms[i].radius / 3,
        )
    )

# Create black hole
black_hole = sphere(
    pos=vec(0, 0, 0),
    radius=0.5,
    mass=10,
    color=color.black
)


################################################################################
# ANIMATION

t = 0
dt = 0.01
total_length_graph = gcurve(color=color.red)

while atoms[0].pos.x < 0:
    rate(2 / (5 * dt))

    for i in range(0, len(atoms)):

        atoms[i].force = f_g(atoms[i], black_hole)

        if i > 0:
            atoms[i].force += f_s(atoms[i], atoms[i - 1])
        if i > len(atoms) - 1:
            atoms[i].force += f_s(atoms[i], atoms[i + 1])

    for i in range(0, len(atoms)):
        atoms[i].v += (atoms[i].force / atoms[i].mass) * dt
        atoms[i].pos += atoms[i].v * dt

    for i in range(0, len(springs)):
        springs[i].pos = atoms[i].pos
        springs[i].axis = atoms[i + 1].pos - atoms[i].pos

    total_length_graph.plot(t, mag(atoms[0].pos - atoms[len(atoms) - 1].pos))
    t += dt
