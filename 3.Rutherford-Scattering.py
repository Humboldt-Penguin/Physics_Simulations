from vpython import *
#GlowScript 3.1 VPython

# scene.autoscale = False

################################################################################
# BUTTONS

# Delete the alpha particles (sphere and trail) that have "hit" the borders and are no longer in motion
def clear_dead_particles(b):
    for p in particles:
        if (p.dead):
            p.clear_trail()
            p.visible = False
            del p

clear_dead_particles_button = button(bind=clear_dead_particles, text="Clear Dead Particles")


# Determines how long the "trail" behind each alpha particle is
def trail_length(s):
    for p in particles:
        p.retain = s.value
    trail_length_button_caption.text = "Trail = "+"{:1.2f}".format((s.value-1)/10)+"\n\n"

trail_length_button = slider(bind=trail_length, min=1, max=1001, value=11, step = 10)
trail_length_button_caption = wtext(text="Trail = "+"{:1.2f}".format((trail_length_button.value-1)/10)+"\n\n")



################################################################################
# FUNCTIONS

# Reference/GravityFunction modified such that the force is repulsive, as opposed to attractive
def f_e(p1, p2):
    if (p1.pos == p2.pos):
        return vec(0,0,0)
    k = 2.5
    r_vec = p2.pos - p1.pos
    force_mag = k * p1.charge * p2.charge / mag(r_vec)**2
    r_hat = r_vec/mag(r_vec)
    force_vec = -force_mag * r_hat
    return force_vec



################################################################################
# PARTICLES

# Distance between alpha particle source and nucleus
xrange = 30
# y-axis bounds for alpha particle spawning point
yrange = 10
# Rate at which alpha particles are "shot" out
alpha_rate = 1000
# Time step
dt = 0.001





nucleus = simple_sphere(
    pos = vec(xrange/2, 0, 0),
    radius = 0.5,
    color = color.red, #vec(0.867, 0.467, 0.467),
    charge = 1
)

particles = []

i = 0

for time in range(0,1000,dt):
    rate(5/dt)
    
    
    i += 1
    
    if (i % alpha_rate == 0):
        
        i = 0

        particles.append(
            simple_sphere(
                pos = vec(-xrange/2, -yrange/2 + random()*yrange, 0),
                radius = 0.3,
                color = vec(1,50,40),
                momentum = vec(2,0,0),
                mass = 1,
                charge = 1,
                make_trail = True,
                retain = trail_length_button.value,
                dead = False
            )
        )
        


    for p in particles:
        if (not p.dead):
            p.force = f_e(p,nucleus)
            p.momentum = p.momentum + p.force * dt
            p.pos = p.pos + (p.momentum / p.mass) * dt
        
        if (abs(p.pos.y) > yrange or abs(p.pos.x) > xrange):
            # particles.remove(p)
            p.momentum = vec(0,0,0)
            p.dead = True
    
            
            
    time += dt
    
