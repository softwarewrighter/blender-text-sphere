"""Render configuration module for Blender Text Sphere."""

import bpy
import os
import config


def configure_eevee():
    """Configure Eevee render engine for preview mode."""
    scene = bpy.context.scene
    scene.render.engine = 'BLENDER_EEVEE_NEXT'

    eevee = scene.eevee

    # Sampling (Blender 4.x uses different attribute names)
    try:
        eevee.taa_render_samples = config.EEVEE_SAMPLES
    except AttributeError:
        pass  # Attribute may not exist in all versions

    # Bloom is now handled via compositor in Blender 4.x EEVEE Next
    # We'll use the compositor glare node instead

    # Other effects - try/except for version compatibility
    try:
        eevee.use_gtao = True  # Ambient Occlusion
    except AttributeError:
        pass

    try:
        eevee.use_ssr = True   # Screen Space Reflections
    except AttributeError:
        pass

    print("Eevee render engine configured")


def configure_cycles():
    """Configure Cycles render engine for production mode."""
    scene = bpy.context.scene
    scene.render.engine = 'CYCLES'

    cycles = scene.cycles

    # Try to use GPU if available
    cycles.device = 'GPU'

    # Sampling
    cycles.samples = config.CYCLES_SAMPLES
    cycles.use_denoising = True

    # Light paths
    cycles.max_bounces = config.CYCLES_MAX_BOUNCES
    cycles.diffuse_bounces = config.CYCLES_DIFFUSE_BOUNCES
    cycles.glossy_bounces = config.CYCLES_GLOSSY_BOUNCES
    cycles.transmission_bounces = config.CYCLES_TRANSMISSION_BOUNCES

    # Try to set up GPU compute
    try:
        prefs = bpy.context.preferences.addons['cycles'].preferences
        # Try CUDA, then OptiX, then HIP, then ONEAPI
        for compute_type in ['OPTIX', 'CUDA', 'HIP', 'ONEAPI']:
            try:
                prefs.compute_device_type = compute_type
                prefs.get_devices()
                for device in prefs.devices:
                    device.use = True
                print(f"Cycles using {compute_type} GPU acceleration")
                break
            except:
                continue
    except Exception as e:
        print(f"Could not enable GPU, using CPU: {e}")
        cycles.device = 'CPU'

    print("Cycles render engine configured")


def setup_compositor():
    """Set up compositor nodes for bloom/glow effect."""
    scene = bpy.context.scene
    scene.use_nodes = True

    tree = scene.node_tree
    nodes = tree.nodes
    links = tree.links

    # Clear existing nodes
    nodes.clear()

    # Create render layers node
    render_layers = nodes.new('CompositorNodeRLayers')
    render_layers.location = (0, 0)

    # Create glare node for bloom
    glare = nodes.new('CompositorNodeGlare')
    glare.location = (300, 0)
    glare.glare_type = 'FOG_GLOW'
    glare.quality = 'HIGH'
    glare.mix = config.GLARE_MIX
    glare.threshold = config.GLARE_THRESHOLD
    glare.size = config.GLARE_SIZE

    # Create composite output
    composite = nodes.new('CompositorNodeComposite')
    composite.location = (600, 0)

    # Link nodes
    links.new(render_layers.outputs['Image'], glare.inputs['Image'])
    links.new(glare.outputs['Image'], composite.inputs['Image'])

    print("Compositor nodes configured")


def configure_output():
    """Configure output format and file settings."""
    scene = bpy.context.scene
    render = scene.render

    # Resolution
    render.resolution_x = config.RESOLUTION_X
    render.resolution_y = config.RESOLUTION_Y
    render.resolution_percentage = 100

    # Frame rate
    render.fps = config.FRAME_RATE

    # Frame range
    scene.frame_start = 1
    scene.frame_end = config.TOTAL_FRAMES

    # Output format - FFMPEG for video
    render.image_settings.file_format = 'FFMPEG'
    render.ffmpeg.format = 'MPEG4'
    render.ffmpeg.codec = 'H264'
    render.ffmpeg.constant_rate_factor = 'HIGH'
    render.ffmpeg.ffmpeg_preset = 'GOOD'

    # Output path
    os.makedirs(config.OUTPUT_DIR, exist_ok=True)
    render.filepath = config.OUTPUT_FILE

    print(f"Output configured: {config.OUTPUT_FILE}")


def execute_render():
    """Execute the animation render."""
    print(f"Starting render: {config.TOTAL_FRAMES} frames at {config.FRAME_RATE}fps")
    print(f"Output: {config.OUTPUT_FILE}")

    # Render animation
    bpy.ops.render.render(animation=True)

    print("Render complete!")


def setup_render(mode='preview'):
    """Set up rendering based on mode."""
    print(f"Setting up render in {mode} mode...")

    if mode == 'production':
        configure_cycles()
    else:
        configure_eevee()

    setup_compositor()
    configure_output()

    print("Render setup complete!")
