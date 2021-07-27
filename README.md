# Physics Simulations

Zain Kamal | z.kamal2021@gmail.com | zk73@njit.edu

Click on the images to run the simulations on GlowScript/Google Colab!

[My Video Lessons](https://sites.google.com/view/space-science-with-spice)

---
## 0. Background Information

* [VPython](https://www.glowscript.org/docs/VPythonDocs/index.html) is a library that uses a 3D graphics module called Visual to display 3D objects. GlowScript is a browser-based Python IDE that comes with VPython and Matplotlib.
  - [My GlowScript Repository](https://www.glowscript.org/#/user/ZainKamal/folder/MyPrograms/)
* [Colaboratory](https://research.google.com/colaboratory/faq.html), or “Colab” for short, by Google Research is a hosted Jupyter notebook service that provides free access to computing resources, including GPUs. It is especially well suited to machine learning, data analysis and education.




Controls for GlowScript: 
* Pan ⟶ Shift + left click + drag 
* Rotate ⟶ Right click + drag
* Zoom ⟶ Scroll wheel
* Resize ⟶ click + drag at bottom right of display window
* View code ⟶ "Edit this Program" at top left

---
## 1. Basic Systems

### 1.1. Bouncing Ball

[![bounce](https://i.imgur.com/c815PVR.png)](https://www.glowscript.org/#/user/ZainKamal/folder/MyPrograms/program/1.1.Bouncing-Ball "Click to Run 1.1.Bouncing-Ball")

### 1.2. Double Pendulum (with Lagrangian Mechanics)

* [LaTeX document deriving the differential equations of motion using Lagrangians](https://drive.google.com/file/d/1_wVI0pXhXFBpD_LGQajf5SA7iYAqrEKx/view?usp=sharing)

[![double_pendulum](https://i.imgur.com/SAzf8No.png)](https://www.glowscript.org/#/user/ZainKamal/folder/MyPrograms/program/1.2.Double-Pendulum-with-Lagrangians "Click to Run 1.2.Double-Pendulum-with-Lagrangians")

### 1.3. Rolling without Slipping (in a circle)

[![rolling without slipping](https://i.imgur.com/vt6Cqm6.png)](https://www.glowscript.org/#/user/ZainKamal/folder/MyPrograms/program/1.3.Rolling-Without-Slipping "Click to Run 1.3.Rolling-Without-Slipping")

### 1.4. 3D Surface Plotter

[![3D surface plotter](https://i.imgur.com/E7WBVpo.png)](https://www.glowscript.org/#/user/ZainKamal/folder/MyPrograms/program/1.4.Surface-Plot-3D "Click to Run 1.4.Surface-Plot-3D")


## 2. Gravitation

### 2.1. Basic Solar System

[![solar_system](https://i.imgur.com/djn84Vb.png)](https://www.glowscript.org/#/user/ZainKamal/folder/MyPrograms/program/2.1.Basic-Solar-System "Click to Run 2.1.Basic-Solar-System")

### 2.2.1. Randomized N-Body Simulations (collisionless)

[![n body sim](https://i.imgur.com/XZcBKPG.png)](https://www.glowscript.org/#/user/ZainKamal/folder/MyPrograms/program/2.2.1.Randomized-N-Body-Sim "2.2.1.Randomized-N-Body-Sim")

[This version (2.2.2.) has the initial conditions that led to the picture above](https://www.glowscript.org/#/user/ZainKamal/folder/MyPrograms/program/2.2.2.Three-Body-Sim)

This simulation can smoothly support up to 100 bodies on my computer, but enabling the trails behind each particle limits it to 4-6 bodies. I leave trails on in spite of this because the resutls look cooler and more patterns are observable. Once I implement collisions, I will probably disable trails.

### 2.3. Spaghettification

[![spaghettification](https://i.imgur.com/VuFjz83.png)](https://www.glowscript.org/#/user/ZainKamal/folder/MyPrograms/program/2.3.Spaghettification "2.3.Spaghettification")

## 3. Electricity and Magnetism

### 3.1. Rutherford Scattering

[![rutherford scattering](https://i.imgur.com/xH63Vw4.png)](https://www.glowscript.org/#/user/ZainKamal/folder/MyPrograms/program/3.1.Rutherford-Scattering "3.1.Rutherford-Scattering")

> The Geiger–Marsden experiments (also called the Rutherford gold foil experiment) were a landmark series of experiments by which scientists learned that every atom has a nucleus where all of its positive charge and most of its mass is concentrated. They deduced this after measuring how an alpha particle beam is scattered when it strikes a thin metal foil. ([Source](https://en.wikipedia.org/wiki/Geiger-Marsden_experiments))

![Source: https://flexbooks.ck12.org/cbook/ck-12-chemistry-flexbook-2.0/section/4.14/primary/lesson/rutherfords-atomic-model-chem](https://i.imgur.com/PDaoq7b.png)

A fun little quote from Rutherford himself:
> It was quite the most incredible event that has ever happened to me in my life. It was almost as incredible as if you fired a 15-inch shell at a piece of tissue paper and it came back and hit you.

### 3.2. Magnetic Vector Field

[![biot savart](https://i.imgur.com/JYBiuA7.png)](https://colab.research.google.com/drive/1Khgv889lU17A6rbwUNVpBbcST8nCBcgB?usp=sharing "3.2.Magnetic-Vector-Field")



---

## Future Project Ideas

- [ ] Account for collisions in Project 2.2. (N-Body Simulations) to prevent infinite gravitational force when bodies are extremely close
- [ ] 3D game of life inspired by [this video](https://www.youtube.com/watch?v=dQJ5aEsP6Fs)
- [ ] Model a piece of rope with vpython springs
