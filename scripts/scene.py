"""Scene construction module for Blender Text Sphere."""

import bpy
from math import cos, sin, radians
import config


def clear_scene():
    """Remove all default objects from the scene."""
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

    # Clear orphan data
    for block in bpy.data.meshes:
        if block.users == 0:
            bpy.data.meshes.remove(block)
    for block in bpy.data.materials:
        if block.users == 0:
            bpy.data.materials.remove(block)
    for block in bpy.data.curves:
        if block.users == 0:
            bpy.data.curves.remove(block)


def create_sphere():
    """Create the central translucent sphere."""
    bpy.ops.mesh.primitive_uv_sphere_add(
        segments=config.SPHERE_SEGMENTS,
        ring_count=config.SPHERE_RINGS,
        radius=config.SPHERE_RADIUS,
        location=(0, 0, 0)
    )
    sphere = bpy.context.active_object
    sphere.name = "CentralSphere"

    # Create and apply material
    mat = bpy.data.materials.new(name="SphereMaterial")
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links

    # Clear default nodes
    nodes.clear()

    # Create Principled BSDF
    bsdf = nodes.new('ShaderNodeBsdfPrincipled')
    bsdf.location = (0, 0)
    bsdf.inputs['Base Color'].default_value = config.SPHERE_COLOR
    bsdf.inputs['Metallic'].default_value = config.SPHERE_METALLIC
    bsdf.inputs['Roughness'].default_value = config.SPHERE_ROUGHNESS
    bsdf.inputs['Alpha'].default_value = config.SPHERE_ALPHA
    bsdf.inputs['Transmission Weight'].default_value = config.SPHERE_TRANSMISSION
    bsdf.inputs['Emission Color'].default_value = config.SPHERE_COLOR
    bsdf.inputs['Emission Strength'].default_value = config.SPHERE_EMISSION_STRENGTH

    # Create output node
    output = nodes.new('ShaderNodeOutputMaterial')
    output.location = (300, 0)
    links.new(bsdf.outputs['BSDF'], output.inputs['Surface'])

    # Opaque rendering (no transparency)
    mat.surface_render_method = 'DITHERED'

    sphere.data.materials.append(mat)

    # Smooth shading
    bpy.ops.object.shade_smooth()

    return sphere


def create_text_material(name, color):
    """Create an emissive material for text."""
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links

    nodes.clear()

    bsdf = nodes.new('ShaderNodeBsdfPrincipled')
    bsdf.location = (0, 0)
    bsdf.inputs['Base Color'].default_value = color
    bsdf.inputs['Metallic'].default_value = config.TEXT_METALLIC
    bsdf.inputs['Roughness'].default_value = config.TEXT_ROUGHNESS
    bsdf.inputs['Emission Color'].default_value = color
    bsdf.inputs['Emission Strength'].default_value = config.TEXT_EMISSION_STRENGTH
    bsdf.inputs['Subsurface Weight'].default_value = config.TEXT_SUBSURFACE

    output = nodes.new('ShaderNodeOutputMaterial')
    output.location = (300, 0)
    links.new(bsdf.outputs['BSDF'], output.inputs['Surface'])

    return mat


def create_text_objects():
    """Create 3D text objects for each letter, positioned in orbit."""
    text_objects = []
    num_letters = len(config.TEXT_CHARACTERS)
    angle_offset = 360 / num_letters

    for i, char in enumerate(config.TEXT_CHARACTERS):
        # Create text curve
        bpy.ops.object.text_add(location=(0, 0, 0))
        text_obj = bpy.context.active_object
        text_obj.name = f"Letter_{char}"

        # Set the character
        text_obj.data.body = char
        text_obj.data.size = config.TEXT_SIZE
        text_obj.data.extrude = config.TEXT_EXTRUSION
        text_obj.data.bevel_depth = config.TEXT_BEVEL_DEPTH
        text_obj.data.bevel_resolution = 2

        # Center the text origin
        text_obj.data.align_x = 'CENTER'
        text_obj.data.align_y = 'CENTER'

        # Calculate position on orbit
        angle = radians(i * angle_offset)
        x = config.ORBIT_RADIUS * cos(angle)
        y = config.ORBIT_RADIUS * sin(angle)
        text_obj.location = (x, y, 0)

        # Make text face outward from center
        text_obj.rotation_euler = (radians(90), 0, angle + radians(90))

        # Apply rainbow material
        color_index = i % len(config.RAINBOW_COLORS)
        mat = create_text_material(f"TextMat_{char}", config.RAINBOW_COLORS[color_index])
        text_obj.data.materials.append(mat)

        text_objects.append(text_obj)

    return text_objects


def setup_camera():
    """Position and configure the camera."""
    bpy.ops.object.camera_add(
        location=config.CAMERA_LOCATION,
        rotation=config.CAMERA_ROTATION
    )
    camera = bpy.context.active_object
    camera.name = "MainCamera"
    camera.data.lens = config.CAMERA_FOCAL_LENGTH

    # Set as active camera
    bpy.context.scene.camera = camera

    return camera


def setup_lighting():
    """Create the three-point lighting setup."""
    lights = []

    # Key light (Area)
    bpy.ops.object.light_add(
        type='AREA',
        location=config.KEY_LIGHT["location"]
    )
    key = bpy.context.active_object
    key.name = "KeyLight"
    key.data.energy = config.KEY_LIGHT["power"]
    key.data.color = config.KEY_LIGHT["color"]
    key.data.size = 5
    lights.append(key)

    # Fill light (Area)
    bpy.ops.object.light_add(
        type='AREA',
        location=config.FILL_LIGHT["location"]
    )
    fill = bpy.context.active_object
    fill.name = "FillLight"
    fill.data.energy = config.FILL_LIGHT["power"]
    fill.data.color = config.FILL_LIGHT["color"]
    fill.data.size = 4
    lights.append(fill)

    # Rim light (Point)
    bpy.ops.object.light_add(
        type='POINT',
        location=config.RIM_LIGHT["location"]
    )
    rim = bpy.context.active_object
    rim.name = "RimLight"
    rim.data.energy = config.RIM_LIGHT["power"]
    rim.data.color = config.RIM_LIGHT["color"]
    lights.append(rim)

    return lights


def setup_world():
    """Configure world background and environment."""
    world = bpy.context.scene.world
    if world is None:
        world = bpy.data.worlds.new("World")
        bpy.context.scene.world = world

    world.use_nodes = True
    nodes = world.node_tree.nodes
    links = world.node_tree.links

    nodes.clear()

    # Background node
    bg = nodes.new('ShaderNodeBackground')
    bg.location = (0, 0)
    bg.inputs['Color'].default_value = config.BACKGROUND_COLOR
    bg.inputs['Strength'].default_value = config.AMBIENT_STRENGTH

    # Output node
    output = nodes.new('ShaderNodeOutputWorld')
    output.location = (300, 0)
    links.new(bg.outputs['Background'], output.inputs['Surface'])

    return world


def build_scene():
    """Build the complete scene."""
    print("Clearing scene...")
    clear_scene()

    print("Creating sphere...")
    sphere = create_sphere()

    print("Creating text objects...")
    text_objects = create_text_objects()

    print("Setting up camera...")
    camera = setup_camera()

    print("Setting up lighting...")
    lights = setup_lighting()

    print("Setting up world...")
    world = setup_world()

    print("Scene construction complete!")
    return {
        "sphere": sphere,
        "text_objects": text_objects,
        "camera": camera,
        "lights": lights,
        "world": world
    }
