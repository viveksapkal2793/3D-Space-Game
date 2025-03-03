# 3D-Space-Game
##### Name: Vivek Sapkal
##### Roll No.: B22AI066
A three-dimensional game built using PyOpenGL and based on a space theme.
## Description


In this game, you control a transporter navigating through space. Your goal is to reach the destination space station while avoiding obstacles and enemies. The game features a 3rd person and 1st person view, lasers for shooting enemies, and a minimap arrow to guide you to your destination.


## Dependencies


To run this game, you need the following dependencies:


- Python 3.8+
- PyOpenGL
- GLFW
- NumPy
- ImGui


You can install the required dependencies using pip:


```sh
pip install PyOpenGL glfw numpy imgui[glfw]
```


## How to Run the Game


1. Clone the repository (or download the zip file and extract it):


```sh
git clone https://github.com/viveksapkal2793/3D-Space-Game.git
cd 3D-Space-Game
```


2. Run the game:


```sh
python main.py
```


## Controls


- **W**: Pitch down (3rd person view)
- **S**: Pitch up (3rd person view)
- **A**: Yaw left (3rd person view)
- **D**: Yaw right (3rd person view)
- **Q**: Roll left (3rd person view)
- **E**: Roll right (3rd person view)
- **SPACE**: Accelerate forward (3rd person view)
- **LEFT SHIFT**: Decelerate (3rd person view)
- **RIGHT CLICK**: Switch to 1st person view
- **LEFT CLICK**: Shoot laser (1st person view)


## Game Screens


- **Main Menu**: Start a new game.
- **Game Over Screen**: Displayed when the transporter collides with an obstacle or enemy.
- **You Won Screen**: Displayed when the transporter reaches the destination space station.


## Basic Game Mechanics


- **Transporter**: The main object controlled by the player.
- **Pirates**: Enemies that the player needs to avoid or shoot.
- **Planets and Space Stations**: Obstacles and destinations in the game.
- **Lasers**: Used to shoot enemies in 1st person view.
- **Minimap Arrow**: Guides the player to the destination space station.


## File Structure


- main.py: Entry point of the game.
- game.py: Contains the main game logic.
- window_manager.py: Manages the game window and input handling.
- objects.py: Contains object loading and creation logic.
- graphics.py: Contains graphics-related classes and functions.
- shaders.py: Contains shader programs for rendering.


## Acknowledgements

- PyOpenGL
- GLFW
- NumPy
- ImGui