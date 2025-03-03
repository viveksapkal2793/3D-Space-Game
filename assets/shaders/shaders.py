# Enhanced Shaders.py
# Upgraded with minimap, crosshair, and additional utilities for gaming applications

# Standard Perspective Shader (Upgraded with Lighting and Texture Support)
standard_shader = {
 "vertex_shader": '''
 #version 330 core
 layout(location = 0) in vec3 vertexPosition; // Vertex position
 layout(location = 1) in vec3 vertexNormal; // Vertex normal
 layout(location = 2) in vec2 vertexUV; // Texture coordinates

 uniform mat4 modelMatrix;
 uniform mat4 viewMatrix;
 uniform mat4 projectionMatrix;
 uniform float focalLength;

 out vec3 FragPos; // World-space fragment position
 out vec3 Normal; // World-space normal
 out vec2 UV; // Texture UV coordinates

 void main() {
 FragPos = vec3(modelMatrix * vec4(vertexPosition, 1.0));
 Normal = mat3(transpose(inverse(modelMatrix))) * vertexNormal;
 UV = vertexUV;
 vec4 camCoordPos = viewMatrix * vec4(FragPos, 1.0);
 gl_Position = projectionMatrix * vec4(focalLength * (camCoordPos.xy / abs(camCoordPos.z)), camCoordPos.z, 1.0);
 }
 ''',

 "fragment_shader": '''
 #version 330 core
 in vec3 FragPos;
 in vec3 Normal;
 in vec2 UV;

 uniform vec4 objectColour; // Base object color
 uniform vec3 lightPos; // Light position
 uniform vec3 lightColour; // Light color
 uniform vec3 viewPos; // Camera position
 uniform sampler2D textureSampler; // Texture sampler
 uniform float textureBlend; // Blend factor for texture vs color (0.0 = full color, 1.0 = full texture)

 out vec4 outputColour;

 void main() {
 // Ambient
 float ambientStrength = 0.2;
 vec3 ambient = ambientStrength * lightColour;

 // Diffuse
 vec3 norm = normalize(Normal);
 vec3 lightDir = normalize(lightPos - FragPos);
 float diff = max(dot(norm, lightDir), 0.0);
 vec3 diffuse = diff * lightColour;

 // Specular
 float specularStrength = 0.5;
 vec3 viewDir = normalize(viewPos - FragPos);
 vec3 reflectDir = reflect(-lightDir, norm);
 float spec = pow(max(dot(viewDir, reflectDir), 0.0), 32);
 vec3 specular = specularStrength * spec * lightColour;

 // Combine lighting with texture and base color
 vec4 baseColor = mix(objectColour, texture2D(textureSampler, UV), textureBlend);
 vec3 result = (ambient + diffuse + specular) * baseColor.rgb;
 outputColour = vec4(result, baseColor.a);
 }
 '''
}

# Edge Shader (Upgraded with Outline Width and Color Variation)
edge_shader = {
 "vertex_shader": '''
 #version 330 core
 layout(location = 0) in vec3 vertexPosition;
 layout(location = 1) in vec3 vertexNormal;

 uniform mat4 modelMatrix;
 uniform mat4 viewMatrix;
 uniform mat4 projectionMatrix;
 uniform float outlineWidth; // Width of the outline

 void main() {
 vec3 offset = vertexNormal * outlineWidth; // Offset by normal for edge effect
 vec4 pos = modelMatrix * vec4(vertexPosition + offset, 1.0);
 gl_Position = projectionMatrix * viewMatrix * pos;
 }
 ''',

 "fragment_shader": '''
 #version 330 core
 out vec4 outputColour;
 uniform vec3 edgeColour; // Customizable edge color

 void main() {
 outputColour = vec4(edgeColour, 1.0); // Dynamic edge color
 }
 '''
}

# HUD Shader (Upgraded with Scaling and Alpha Blending)
hud_shader = {
 "vertex_shader": '''
 #version 330 core
 layout(location = 0) in vec3 vertexPosition;
 layout(location = 1) in vec3 vertexColor;

 uniform vec2 screenPosition; // Position in screen space
 uniform float rotation; // Rotation angle in radians
 uniform vec2 scale; // Scale factor for HUD element
 uniform vec2 screenSize; // Screen resolution

 out vec3 fragColor;

 void main() {
 float cosAngle = cos(-rotation);
 float sinAngle = sin(-rotation);
 vec2 rotatedPos = vec2(
 vertexPosition.x * cosAngle - vertexPosition.y * sinAngle,
 vertexPosition.x * sinAngle + vertexPosition.y * cosAngle
 );
 vec2 scaledPos = rotatedPos * scale;
 vec2 finalPos = (screenPosition + scaledPos) / (screenSize * 0.5) - 1.0; // Normalize to [-1, 1]
 gl_Position = vec4(finalPos, 0.0, 1.0);
 fragColor = vertexColor;
 }
 ''',

 "fragment_shader": '''
 #version 330 core
 in vec3 fragColor;
 uniform float alpha; // Transparency control
 out vec4 outputColour;

 void main() {
 outputColour = vec4(fragColor, alpha);
 }
 '''
}

# Minimap Shader (Orthographic Projection with Texture and Fog of War)
minimap_shader = {
 "vertex_shader": '''
 #version 330 core
 layout(location = 0) in vec3 vertexPosition;
 layout(location = 1) in vec2 vertexUV;

 uniform mat4 orthoMatrix; // Orthographic projection matrix
 uniform vec2 mapOffset; // Minimap offset in world space
 uniform float mapScale; // Minimap scale factor

 out vec2 UV;

 void main() {
 vec2 scaledPos = vertexPosition.xy * mapScale + mapOffset;
 gl_Position = orthoMatrix * vec4(scaledPos, 0.0, 1.0);
 UV = vertexUV;
 }
 ''',

 "fragment_shader": '''
 #version 330 core
 in vec2 UV;
 uniform sampler2D mapTexture; // Minimap texture
 uniform vec2 playerPos; // Player position for fog of war
 uniform float fogRadius; // Radius of fog visibility

 out vec4 outputColour;

 void main() {
 vec4 texColor = texture2D(mapTexture, UV);
 float dist = length(UV - playerPos); // Distance from player
 float fogFactor = smoothstep(fogRadius, fogRadius * 1.5, dist); // Smooth fog transition
 outputColour = mix(texColor, vec4(0.1, 0.1, 0.1, 1.0), fogFactor); // Darken beyond radius
 }
 '''
}

# Crosshair Shader (Orthographic Projection with Dynamic Shape)
crosshair_shader = {
 "vertex_shader": '''
 #version 330 core
 layout(location = 0) in vec3 vertexPosition;

 uniform mat4 orthoMatrix; // Orthographic projection matrix
 uniform vec2 screenPos; // Screen position of crosshair
 uniform float scale; // Scale of crosshair
 uniform float rotation; // Rotation angle

 void main() {
 float cosAngle = cos(rotation);
 float sinAngle = sin(rotation);
 vec2 rotatedPos = vec2(
 vertexPosition.x * cosAngle - vertexPosition.y * sinAngle,
 vertexPosition.x * sinAngle + vertexPosition.y * cosAngle
 );
 vec2 finalPos = screenPos + rotatedPos * scale;
 gl_Position = orthoMatrix * vec4(finalPos, 0.0, 1.0);
 }
 ''',

 "fragment_shader": '''
 #version 330 core
 uniform vec3 color; // Crosshair color
 uniform float thickness; // Thickness of crosshair lines

 out vec4 outputColour;

 void main() {
 vec2 uv = gl_FragCoord.xy - vec2(0.5); // Center UV
 float dist = min(abs(uv.x), abs(uv.y)); // Distance to nearest edge
 float alpha = smoothstep(thickness, thickness * 0.5, dist); // Anti-aliased edge
 outputColour = vec4(color, 1.0 - alpha);
 }
 '''
}

# Glow Effect Shader (Bonus Utility for Visual Enhancement)
glow_shader = {
 "vertex_shader": '''
 #version 330 core
 layout(location = 0) in vec3 vertexPosition;

 uniform mat4 modelMatrix;
 uniform mat4 viewMatrix;
 uniform mat4 projectionMatrix;

 void main() {
 gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(vertexPosition, 1.0);
 }
 ''',

 "fragment_shader": '''
 #version 330 core
 uniform vec2 resolution; // Screen resolution
 uniform vec3 glowColor; // Glow color
 uniform float glowIntensity;// Glow strength
 uniform sampler2D texture; // Base texture

 out vec4 outputColour;

 void main() {
 vec2 uv = gl_FragCoord.xy / resolution;
 vec4 baseColor = texture2D(texture, uv);
 float glow = 0.0;
 for (float i = -2.0; i <= 2.0; i += 1.0) {
 for (float j = -2.0; j <= 2.0; j += 1.0) {
 vec2 offset = vec2(i, j) * 0.005;
 glow += texture2D(texture, uv + offset).a;
 }
 }
 glow = glow * glowIntensity / 25.0; // Normalize and scale
 outputColour = vec4(baseColor.rgb + glowColor * glow, baseColor.a);
 }
 '''
}
