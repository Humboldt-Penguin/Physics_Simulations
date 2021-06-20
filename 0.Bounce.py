from vpython import *
#GlowScript 3.0 VPython

scene.autoscale = False

ball = sphere(
    pos=vec(0,10,0),
    momentum=vec(3,5,0),
    make_trail=True,
    color=color.red,
)

floor = box(
    pos=vec(60,-0.5,0),
    length=130,
    width=20,
)

f_g = vec(0,-9.81,0)
dt = 0.001

for time in range(0, 40, dt):
    rate(5/dt)
    
    ball.momentum += f_g*dt
    ball.pos += ball.momentum*dt
    
    if ball.pos.y <= 1:
        ball.momentum.y *= -0.97
        
print("Complete")