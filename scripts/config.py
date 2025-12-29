"""Configuration constants for Blender Text Sphere project."""

import os
from math import pi

# Project paths
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(PROJECT_DIR, "output")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "text_sphere.mp4")

# Text settings
TEXT_CHARACTERS = "[blender-text-sphere]"
TEXT_SIZE = 1.2
TEXT_EXTRUSION = 0.15
TEXT_BEVEL_DEPTH = 0.02

# Sphere settings
SPHERE_RADIUS = 3.0
SPHERE_SEGMENTS = 64
SPHERE_RINGS = 32

# Orbit settings
ORBIT_RADIUS = 8.0
ROTATION_SPEED = 360.0  # degrees per animation cycle

# Rainbow color palette (hex values from design doc)
RAINBOW_COLORS = [
    (1.0, 0.0, 0.25, 1.0),   # Red #FF0040
    (1.0, 0.5, 0.0, 1.0),    # Orange #FF8000
    (1.0, 1.0, 0.0, 1.0),    # Yellow #FFFF00
    (0.5, 1.0, 0.0, 1.0),    # Lime #80FF00
    (0.0, 1.0, 0.25, 1.0),   # Green #00FF40
    (0.0, 1.0, 1.0, 1.0),    # Cyan #00FFFF
    (0.0, 0.5, 1.0, 1.0),    # Blue #0080FF
    (0.5, 0.0, 1.0, 1.0),    # Purple #8000FF
    (1.0, 0.0, 1.0, 1.0),    # Magenta #FF00FF
]

# Sphere material properties
SPHERE_COLOR = (0.19, 0.19, 0.63, 1.0)  # Deep blue-purple #3030A0
SPHERE_METALLIC = 0.1
SPHERE_ROUGHNESS = 0.3
SPHERE_ALPHA = 1.0  # Fully opaque
SPHERE_TRANSMISSION = 0.0  # No transparency
SPHERE_EMISSION_STRENGTH = 0.1

# Text material properties
TEXT_METALLIC = 0.0
TEXT_ROUGHNESS = 0.4
TEXT_EMISSION_STRENGTH = 2.0
TEXT_SUBSURFACE = 0.1

# Background color
BACKGROUND_COLOR = (0.04, 0.04, 0.06, 1.0)  # Near black #0A0A0F

# Camera settings
CAMERA_LOCATION = (0, -20, 5)
CAMERA_ROTATION = (75 * pi / 180, 0, 0)  # 75 degrees in radians
CAMERA_FOCAL_LENGTH = 50  # mm

# Lighting settings
KEY_LIGHT = {
    "location": (10, -10, 15),
    "power": 500,
    "color": (1.0, 0.97, 0.94),  # Warm white #FFF8F0
}

FILL_LIGHT = {
    "location": (-8, -5, 8),
    "power": 200,
    "color": (0.94, 0.97, 1.0),  # Cool white #F0F8FF
}

RIM_LIGHT = {
    "location": (0, 15, 5),
    "power": 300,
    "color": (0.88, 0.91, 1.0),  # Blue-white #E0E8FF
}

AMBIENT_COLOR = (0.06, 0.06, 0.13)  # Dark blue #101020
AMBIENT_STRENGTH = 0.1

# Render settings
RESOLUTION_X = 1920
RESOLUTION_Y = 1080
FRAME_RATE = 60
DURATION_SECONDS = 30  # Slower, more stately orbit
TOTAL_FRAMES = FRAME_RATE * DURATION_SECONDS  # 1800 frames

# Eevee settings (preview mode)
EEVEE_SAMPLES = 32
EEVEE_BLOOM_THRESHOLD = 0.8
EEVEE_BLOOM_INTENSITY = 0.1

# Cycles settings (production mode)
CYCLES_SAMPLES = 128
CYCLES_MAX_BOUNCES = 8
CYCLES_DIFFUSE_BOUNCES = 4
CYCLES_GLOSSY_BOUNCES = 4
CYCLES_TRANSMISSION_BOUNCES = 8

# Compositor settings (bloom/glare)
GLARE_MIX = 0.3
GLARE_THRESHOLD = 0.8
GLARE_SIZE = 8

# Output format
OUTPUT_FORMAT = "FFMPEG"
OUTPUT_CODEC = "H264"
OUTPUT_QUALITY = "HIGH"
