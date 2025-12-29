"""Main orchestrator script for Blender Text Sphere.

This script is the entry point for the Blender render pipeline.
Run with: blender --background --python scripts/main.py -- [--preview|--production]
"""

import bpy
import sys
import os

# Add scripts directory to path for imports
script_dir = os.path.dirname(os.path.abspath(__file__))
if script_dir not in sys.path:
    sys.path.insert(0, script_dir)

import config
import scene
import animation
import render


def parse_args():
    """Parse command line arguments passed after '--'."""
    # Arguments after '--' are passed to the script
    argv = sys.argv
    if "--" in argv:
        args = argv[argv.index("--") + 1:]
    else:
        args = []

    mode = 'preview'  # default
    skip_render = False

    for arg in args:
        if arg in ('--production', '-p'):
            mode = 'production'
        elif arg in ('--preview', '-v'):
            mode = 'preview'
        elif arg in ('--no-render', '-n'):
            skip_render = True

    return mode, skip_render


def validate_blender_version():
    """Ensure we're running on a compatible Blender version."""
    version = bpy.app.version
    print(f"Blender version: {version[0]}.{version[1]}.{version[2]}")

    if version[0] < 4:
        print("Warning: This script was designed for Blender 4.x")
        print("Some features may not work correctly on older versions.")

    return True


def main():
    """Main entry point."""
    print("=" * 60)
    print("Blender Text Sphere - Render Pipeline")
    print("=" * 60)

    # Parse arguments
    mode, skip_render = parse_args()
    print(f"Mode: {mode}")
    print(f"Skip render: {skip_render}")

    # Validate Blender version
    validate_blender_version()

    # Step 1: Build the scene
    print("\n--- Building Scene ---")
    scene_objects = scene.build_scene()

    # Step 2: Set up animation
    print("\n--- Setting Up Animation ---")
    orbit_controller = animation.setup_animation(scene_objects["text_objects"])

    # Step 3: Verify loop
    print("\n--- Verifying Loop ---")
    animation.verify_loop()

    # Step 4: Configure render
    print("\n--- Configuring Render ---")
    render.setup_render(mode=mode)

    # Step 5: Execute render (unless skipped)
    if not skip_render:
        print("\n--- Executing Render ---")
        render.execute_render()
    else:
        print("\n--- Render Skipped ---")
        print("Scene is ready. You can render manually or save the .blend file.")

    print("\n" + "=" * 60)
    print("Pipeline complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
