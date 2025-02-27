######################################################
# Write other shaders for minimap and crosshair (Since they need orthographic projection)

# Following is the standard perspective projection shader with uniform colour to all vertices. Can modify as required
standard_shader = {
    "vertex_shader" : '''
        
        #version 330 core
        layout(location = 0) in vec3 vertexPosition;

        uniform mat4 modelMatrix;
        uniform mat4 viewMatrix;
        uniform mat4 projectionMatrix;
        uniform float focalLength;

        void main() {
            vec4 camCoordPos = viewMatrix * modelMatrix * vec4(vertexPosition, 1.0);
            gl_Position = projectionMatrix * vec4(focalLength * (camCoordPos[0] / abs(camCoordPos[2])), focalLength * (camCoordPos[1] / abs(camCoordPos[2])), camCoordPos[2], 1.0);
        }

        ''',

        "fragment_shader" : '''

        #version 330 core

        out vec4 outputColour;

        uniform vec4 objectColour;
        uniform vec3 camPosition;

        void main() {
            vec3 camPos = camPosition;
            outputColour = objectColour;
        }

        '''

}

# standard_shader = {
#     "vertex_shader" : '''
        
#         #version 330 core

#         layout(location = 0) in vec3 aPos; // Position attribute
#         layout(location = 1) in vec3 aNormal; // Normal attribute

#         uniform mat4 modelMatrix;
#         uniform mat4 viewMatrix;
#         uniform mat4 projectionMatrix;

#         out vec3 FragPos; // Position of the fragment in world space
#         out vec3 Normal; // Normal of the fragment in world space

#         void main()
#         {
#             FragPos = vec3(modelMatrix * vec4(aPos, 1.0));
#             Normal = mat3(transpose(inverse(modelMatrix))) * aNormal; // Transform normal to world space

#             gl_Position = projectionMatrix * viewMatrix * vec4(FragPos, 1.0);
#         }

#         ''',

#         "fragment_shader" : '''

#         #version 330 core

#         in vec3 FragPos; // Position of the fragment in world space
#         in vec3 Normal; // Normal of the fragment in world space

#         uniform vec3 objectColour;
#         uniform vec3 lightColour;
#         uniform vec3 lightPos;
#         uniform vec3 viewPos;

#         out vec4 FragColor;

#         void main()
#         {
#             // Ambient lighting
#             float ambientStrength = 0.1;
#             vec3 ambient = ambientStrength * lightColour;

#             // Diffuse lighting
#             vec3 norm = normalize(Normal);
#             vec3 lightDir = normalize(lightPos - FragPos);
#             float diff = max(dot(norm, lightDir), 0.0);
#             vec3 diffuse = diff * lightColour;

#             // Specular lighting
#             float specularStrength = 0.5;
#             vec3 viewDir = normalize(viewPos - FragPos);
#             vec3 reflectDir = reflect(-lightDir, norm);
#             float spec = pow(max(dot(viewDir, reflectDir), 0.0), 32);
#             vec3 specular = specularStrength * spec * lightColour;

#             vec3 result = (ambient + diffuse + specular) * objectColour;
#             FragColor = vec4(result, 1.0);
#         }

#         '''

# }
######################################################