import imgui
import numpy as np
from utils.graphics import Object, Camera, Shader
from assets.objects.objects import transporterProps, pirateProps, planetProps, laserProps, spacestationProps, cube_props
from assets.shaders.shaders import standard_shader, edge_shader

class Game:
    def __init__(self, height, width, gui):
        self.gui = gui
        self.height = height
        self.width = width
        self.screen = 0

    def InitScene(self):
        if self.screen == 1:
            print("Initializing scene")
            ############################################################################
            # Define world state
            self.camera = Camera(self.height, self.width)
            self.shaders = [Shader(standard_shader["vertex_shader"], standard_shader["fragment_shader"])]
            self.edge_shader = Shader(edge_shader["vertex_shader"], edge_shader["fragment_shader"])
            self.gameState = {
                'transporter': None,
                'pirates': [],
                'planets': [],
                'spaceStations': [],
                'cube': None
            } # Can define keys as 'transporter', 'pirates', etc. Their values being Object() or list of Object()
            ############################################################################
            # Define world boundarie
            self.worldMin = np.array([-5000, -5000, -5000], dtype=np.float32)
            self.worldMax = np.array([5000, 5000, 5000], dtype=np.float32)
            ############################################################################
            # Initialize Planets and space stations (Randomly place n planets and n spacestations within world bounds)
            self.n_planets = 20
            self.n_spaceStations = 20
            for _ in range(self.n_planets):
                position = np.random.uniform(self.worldMin, self.worldMax)
                new_planet = Object('planet', self.shaders[0], planetProps)
                new_planet.properties['position'] = position
                self.gameState['planets'].append(new_planet)

                new_spaceStation = Object('spaceStation', self.shaders[0], spacestationProps)
                new_spaceStation.properties['position'] = position 
                self.gameState['spaceStations'].append(new_spaceStation)
            # print("Planet and spacestation initialized")
            ############################################################################
            # Initialize transporter (Randomly choose start and end planet, and initialize transporter at start planet)
            start_planet = np.random.choice(self.gameState['planets'])
            self.gameState['transporter'] = Object('transporter', self.shaders[0], transporterProps)
            # self.gameState['transporter'].properties['position'] = start_planet.properties['position']
            self.gameState['transporter'].properties['position'] = np.array([0, 0, 0], dtype=np.float32)    
            # print("Transporter initialized")
            ############################################################################
            # Initialize Pirates (Spawn at random locations within world bounds)
            self.n_pirates = 20 # for example
            for _ in range(self.n_pirates):
                position = np.random.uniform(self.worldMin, self.worldMax)
                new_pirate = Object('pirate', self.shaders[0], pirateProps) 
                new_pirate.properties['position'] = position
                self.gameState['pirates'].append(new_pirate)
            # print("Pirate initialized")

            cube = Object('cube', self.shaders[0], cube_props)
            self.gameState['cube'] = cube
            ############################################################################
            # Initialize minimap arrow (Need to write orthographic projection shader for it)
            self.camera.position = np.array([5,5,5], dtype=np.float32)
            self.camera.lookAt = np.array([-1,-1,-1], dtype=np.float32)

            self.gameState['cube'].properties["scale"] = np.array([0.5, 0.5, 0.5], dtype=np.float32)

            ############################################################################

    def ProcessFrame(self, inputs, time):

        self.UpdateScene(inputs, time)
        self.DrawScene()
        self.DrawText()

    def DrawText(self):
        if self.screen == 0:
            pass

        if self.screen == 2: # YOU WON Screen
            pass

        if self.screen == 3: # GAME OVER Screen
            pass
        
    def UpdateScene(self, inputs, time):
        if self.screen == 0: # Example start screen
            # print(f'screen: {self.screen}')
            # if inputs["1"]:
            #     self.screen = 1
            #     self.InitScene()
            pass
        if self.screen == 2: # YOU WON
            pass
        if self.screen == 3: # GAME OVER
            pass
        
        if self.screen == 1: # Game screen
            # print(f'screen: {self.screen}')
            ############################################################################
            # Manage inputs 
           

            ############################################################################
            # Update transporter (Update velocity, position, and check for collisions)
           

            ############################################################################
            # Update spacestations (Update velocity and position to revolve around respective planet)
            

            ############################################################################
            # Update Minimap Arrow: (Set direction based on transporter velocity direction and target direction)
            

            ############################################################################
            # Update Lasers (Update position of any currently shot lasers, make sure to despawn them if they go too far to save computation)
           
            
            ############################################################################
            # Update Pirates (Write logic to update their velocity based on transporter position, and check for collision with laser or transporter)
            

            ############################################################################
            # Update Camera (Check for view (3rd person or 1st person) and set position and LookAt accordingly)
            

            ############################################################################
            pass
    
    def DrawScene(self):
        if self.screen == 1: 
            # print("Drawing scene")
            ######################################################
            # Example draw statements

            
            for i, shader in enumerate(self.shaders):
               self.camera.Update(shader)
            self.camera.Update(self.edge_shader)

            # self.gameState["cube"].Draw()

            self.gameState["transporter"].Draw()
            # self.gameState["transporter"].DrawEdges(self.edge_shader, self.camera.viewMatrix, self.camera.projectionMatrix)
            # print("Transporter drawn")
            # self.gameState["stars"].Draw()
            # self.gameState["arrow"].Draw()

            # if self.gameState["transporter"].properties["view"] == 2: # Conditionally draw crosshair
            #     self.gameState["crosshair"].Draw()

            # for laser in self.gameState["lasers"]:
            #     laser.Draw()
            for planet in self.gameState["planets"]:
                planet.Draw()
                # planet.DrawEdges(self.edge_shader, self.camera.viewMatrix, self.camera.projectionMatrix)
            # print("Planets drawn")
            for spaceStation in self.gameState["spaceStations"]:
                spaceStation.Draw()
                # spaceStation.DrawEdges(self.edge_shader, self.camera.viewMatrix, self.camera.projectionMatrix)
            # print("Spacestations drawn")
            for pirate in self.gameState["pirates"]:
                pirate.Draw()
                # pirate.DrawEdges(self.edge_shader, self.camera.viewMatrix, self.camera.projectionMatrix)
            # print("Pirates drawn")
            ######################################################

