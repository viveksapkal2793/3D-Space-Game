import numpy as np
import os
from utils.graphics import Object, Camera, Shader
from assets.shaders.shaders import standard_shader

###############################################################
# Write logic to load OBJ Files:
    # Will depend on type of object. For example if normals needed along with vertex positions 
    # then will need to load slightly differently.

# Can use the provided OBJ files from assignment_2_template/assets/objects/models/
# Can also download other assets or model yourself in modelling softwares like blender

###############################################################
# Create Transporter, Pirates, Stars(optional), Minimap arrow, crosshair, planet, spacestation, laser


###############################################################

def load_obj(filepath):
    vertices = []
    faces = []
    with open(filepath, 'r') as file:
        for line in file:
            if line.startswith('v '):
                parts = line.split()
                vertices.append([float(parts[1]), float(parts[2]), float(parts[3])])
            elif line.startswith('f '):
                parts = line.split()
                face = [int(part.split('/')[0]) - 1 for part in parts[1:]]
                faces.append(face)
    vertices = np.array(vertices, dtype=np.float32)
    faces = np.array(faces, dtype=np.int32)
    faces = faces.flatten()
    return vertices, faces

def create_object(filepath, shader, objType='generic'):
    vertices, faces = load_obj(filepath)
    properties = {
        'vertices': vertices,
        'indices': faces.flatten(),
        'position': np.array([0.0, 0.0, 0.0], dtype=np.float32),
        'rotation': np.array([0.0, 0.0, 0.0], dtype=np.float32),
        'scale': np.array([1.0, 1.0, 1.0], dtype=np.float32),
        'colour': np.array([1.0, 1.0, 1.0, 1.0], dtype=np.float32)
    }
    return Object(objType, shader, properties)

# Create shader
# shader = Shader(standard_shader["vertex_shader"], standard_shader["fragment_shader"])

# Create objects
# transporter = create_object('/home/vivek/CG/3D-Space-Game/assets/objects/models/transporter.obj', shader, objType='transporter')
# pirate = create_object('/home/vivek/CG/3D-Space-Game/assets/objects/models/pirate.obj', shader, objType='pirate')
# planet = create_object('/home/vivek/CG/3D-Space-Game/assets/objects/models/planet.obj', shader, objType='planet')
# laser = create_object('/home/vivek/CG/3D-Space-Game/assets/objects/models/laser.obj', shader, objType='laser')
# spacestation = create_object('/home/vivek/CG/3D-Space-Game/assets/objects/models/spacestation.obj', shader, objType='spacestation')

transporterVerts, transporterInds = load_obj('/home/vivek/CG/3D-Space-Game/assets/objects/models/transporter.obj')
pirateVerts, pirateInds = load_obj('/home/vivek/CG/3D-Space-Game/assets/objects/models/pirate.obj')
planetVerts, planetInds = load_obj('/home/vivek/CG/3D-Space-Game/assets/objects/models/planet.obj')
laserVerts, laserInds = load_obj('/home/vivek/CG/3D-Space-Game/assets/objects/models/laser.obj')
spacestationVerts, spacestationInds = load_obj('/home/vivek/CG/3D-Space-Game/assets/objects/models/spacestation.obj')

transporterProps = {
    'vertices': transporterVerts,
    'indices': transporterInds,
    'position': np.array([0.0, 0.0, 0.0], dtype=np.float32),
    'rotation': np.array([0.0, 0.0, 0.0], dtype=np.float32),
    'scale': np.array([1.0, 1.0, 1.0], dtype=np.float32),
    'colour': np.array([1.0, 1.0, 1.0, 1.0], dtype=np.float32)
}

pirateProps = {
    'vertices': pirateVerts,
    'indices': pirateInds,
    'position': np.array([0.0, 0.0, 0.0], dtype=np.float32),
    'rotation': np.array([0.0, 0.0, 0.0], dtype=np.float32),
    'scale': np.array([1.0, 1.0, 1.0], dtype=np.float32),
    'colour': np.array([1.0, 1.0, 1.0, 1.0], dtype=np.float32)
}

planetProps = {
    'vertices': planetVerts,
    'indices': planetInds,
    'position': np.array([0.0, 0.0, 0.0], dtype=np.float32),
    'rotation': np.array([0.0, 0.0, 0.0], dtype=np.float32),
    'scale': np.array([1.0, 1.0, 1.0], dtype=np.float32),
    'colour': np.array([1.0, 1.0, 1.0, 1.0], dtype=np.float32)
}

laserProps = {
    'vertices': laserVerts,
    'indices': laserInds,
    'position': np.array([0.0, 0.0, 0.0], dtype=np.float32),
    'rotation': np.array([0.0, 0.0, 0.0], dtype=np.float32),
    'scale': np.array([1.0, 1.0, 1.0], dtype=np.float32),
    'colour': np.array([1.0, 1.0, 1.0, 1.0], dtype=np.float32)
}

spacestationProps = {
    'vertices': spacestationVerts,
    'indices': spacestationInds,
    'position': np.array([0.0, 0.0, 0.0], dtype=np.float32),
    'rotation': np.array([0.0, 0.0, 0.0], dtype=np.float32),
    'scale': np.array([1.0, 1.0, 1.0], dtype=np.float32),
    'colour': np.array([1.0, 1.0, 1.0, 1.0], dtype=np.float32)
}