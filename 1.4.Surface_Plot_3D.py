from vpython import *

# GlowScript 3.1 VPython


def f(x, y):
    #######################################################
    # INPUT FUNCTION TO MAKE A SURFACE PLOT FOR
    f = sin(x) * sin(y)

    # Examples:
    #    f = exp(-((x-1)**2 + (y-1)**2)) - exp(-((x+1)**2 + (y+1)**2))
    #    f = sin(x)*sin(y)
    #    f = exp(-(x**2 + y**2)*0.1) * cos(x)*cos(y)
    #######################################################
    return f


print('To change f(x,y) click on "Edit this program" and modify line 7.')


# Setup values

bounds = 4
x_max = y_max = bounds
x_min = y_min = -bounds
step = 0.1
z_max = -1e100
z_min = -z_max


# Fill verticies list with x, y, and z values

verticies = []

for x in range(x_min, x_max, step):
    temp = []
    for y in range(y_min, y_max, step):
        z = f(x, y)
        z_max = max(z, z_max)
        z_min = min(z, z_min)
        temp.append(vertex(pos=vec(x, y, z), color=color.red))
    verticies.append(temp)


# Assign colors to each vertex based on distance between min and max z value

n = len(verticies)

for x in range(0, n):
    for y in range(0, n):
        red = (verticies[x][y].pos.z - z_min) / (z_max - z_min)
        blue = 1 - red
        green = 0
        verticies[x][y].color = vec(red, green, blue)


# Connect all verticies. The 4 triangles about each vertex combine to form a diamond shape. The `triangle` function naturally creates a color gradient.

for x in range(1, n - 1):
    for y in range(1, n - 1):
        triangle(vs=[verticies[x][y], verticies[x + 1][y], verticies[x][y + 1]])
        triangle(vs=[verticies[x][y], verticies[x - 1][y], verticies[x][y + 1]])
        triangle(vs=[verticies[x][y], verticies[x + 1][y], verticies[x][y - 1]])
        triangle(vs=[verticies[x][y], verticies[x - 1][y], verticies[x][y - 1]])
