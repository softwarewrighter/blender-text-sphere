"""Animation module for Blender Text Sphere."""

import bpy
from math import cos, sin, radians, atan2
import config


def create_orbit_empty():
    """Create an empty object at origin to serve as orbit parent."""
    bpy.ops.object.empty_add(type='PLAIN_AXES', location=(0, 0, 0))
    orbit_empty = bpy.context.active_object
    orbit_empty.name = "OrbitController"
    return orbit_empty


def parent_letters_to_orbit(text_objects, orbit_empty):
    """Parent all letter objects to the orbit controller."""
    for text_obj in text_objects:
        text_obj.parent = orbit_empty
        # Keep current world transform
        text_obj.matrix_parent_inverse = orbit_empty.matrix_world.inverted()


def animate_orbit(orbit_empty):
    """Animate the orbit controller rotation for seamless loop."""
    scene = bpy.context.scene
    scene.frame_start = 1
    scene.frame_end = config.TOTAL_FRAMES

    # Set keyframes for rotation
    # Frame 1: starting position (0 degrees)
    scene.frame_set(1)
    orbit_empty.rotation_euler = (0, 0, 0)
    orbit_empty.keyframe_insert(data_path="rotation_euler", frame=1)

    # Frame TOTAL_FRAMES: full rotation (-360 degrees for clockwise)
    # For seamless loop, we rotate to -360 degrees (clockwise when viewed from above)
    scene.frame_set(config.TOTAL_FRAMES)
    orbit_empty.rotation_euler = (0, 0, radians(-360))
    orbit_empty.keyframe_insert(data_path="rotation_euler", frame=config.TOTAL_FRAMES)

    # Set linear interpolation for constant speed
    if orbit_empty.animation_data and orbit_empty.animation_data.action:
        for fcurve in orbit_empty.animation_data.action.fcurves:
            for keyframe in fcurve.keyframe_points:
                keyframe.interpolation = 'LINEAR'

    # Reset to frame 1
    scene.frame_set(1)


def setup_animation(text_objects):
    """Set up the complete animation system."""
    print("Creating orbit controller...")
    orbit_empty = create_orbit_empty()

    print("Parenting letters to orbit...")
    parent_letters_to_orbit(text_objects, orbit_empty)

    print("Animating orbit rotation...")
    animate_orbit(orbit_empty)

    print("Animation setup complete!")
    return orbit_empty


def verify_loop():
    """Verify that the animation loops seamlessly."""
    scene = bpy.context.scene

    # Check frame 1 positions
    scene.frame_set(1)
    frame1_positions = {}
    for obj in bpy.data.objects:
        if obj.name.startswith("Letter_"):
            frame1_positions[obj.name] = obj.matrix_world.translation.copy()

    # Check frame TOTAL_FRAMES positions (should match frame 1)
    scene.frame_set(config.TOTAL_FRAMES)
    frame_end_positions = {}
    for obj in bpy.data.objects:
        if obj.name.startswith("Letter_"):
            frame_end_positions[obj.name] = obj.matrix_world.translation.copy()

    # Compare positions
    all_match = True
    for name in frame1_positions:
        diff = (frame1_positions[name] - frame_end_positions[name]).length
        if diff > 0.001:  # Allow small floating point error
            print(f"Warning: {name} position mismatch: {diff}")
            all_match = False

    if all_match:
        print("Loop verification: PASSED - Animation loops seamlessly")
    else:
        print("Loop verification: WARNING - Some positions don't match")

    scene.frame_set(1)
    return all_match
