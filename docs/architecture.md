# Architecture: Blender Text Sphere

## System Overview

```
+------------------------------------------------------------------+
|                        Entry Point                                |
|                      run_blender.sh                               |
+-----------------------------+------------------------------------+
                              |
                              v
+------------------------------------------------------------------+
|                    Blender Runtime                                |
|              /home/mike/tools/blender-4.5.1-linux-x64            |
|                                                                   |
|  +-----------------------------------------------------------+   |
|  |                   Python Scripts                          |   |
|  |                                                           |   |
|  |  +----------+   +----------+   +----------+              |   |
|  |  |  main.py |-->| scene.py |-->| render.py|              |   |
|  |  +----------+   +----------+   +----------+              |   |
|  |        |              |                                   |   |
|  |        |              v                                   |   |
|  |        |        +------------+                            |   |
|  |        +------->|animation.py|                            |   |
|  |                 +------------+                            |   |
|  |                       |                                   |   |
|  |                       v                                   |   |
|  |               +------------+                              |   |
|  |               | config.py  |                              |   |
|  |               +------------+                              |   |
|  +-----------------------------------------------------------+   |
+------------------------------------------------------------------+
                              |
                              v
+------------------------------------------------------------------+
|                      Output                                       |
|                  output/text_sphere.mp4                          |
+------------------------------------------------------------------+
```

## Directory Structure

```
blender-text-sphere/
|-- docs/
|   |-- info.txt           # Blender path and related projects
|   |-- prd.md             # Product requirements
|   |-- architecture.md    # This file
|   |-- design.md          # Visual and technical design
|   |-- planning.md        # Implementation roadmap
|   +-- status.md          # Current project status
|-- scripts/
|   |-- main.py            # Orchestrator script
|   |-- config.py          # Configuration constants
|   |-- scene.py           # Scene construction
|   |-- animation.py       # Animation keyframes
|   +-- render.py          # Render configuration
|-- output/
|   +-- text_sphere.mp4    # Rendered video output
|-- run_blender.sh         # Shell script to launch Blender
+-- README.md              # Project overview
```

## Component Details

### run_blender.sh
Shell script entry point that:
- Locates Blender executable at `/home/mike/tools/blender-4.5.1-linux-x64/blender`
- Launches Blender in background/headless mode
- Passes `scripts/main.py` as the Python script to execute
- Accepts optional arguments for render mode (preview/production)

### scripts/config.py
Centralized configuration module containing:
- **Text settings**: characters, font, extrusion depth
- **Sphere settings**: radius, material properties
- **Orbit settings**: radius, rotation speed, letter spacing
- **Color settings**: rainbow palette, emission strength
- **Render settings**: resolution, frame rate, duration
- **Output settings**: file paths, format options

### scripts/main.py
Main orchestrator that:
1. Imports configuration
2. Clears default Blender scene
3. Calls scene setup functions
4. Calls animation setup functions
5. Triggers render

### scripts/scene.py
Scene construction module containing:
- `create_sphere()`: Creates central translucent sphere
- `create_text_objects()`: Generates 3D text meshes for each letter
- `setup_materials()`: Creates rainbow emissive materials
- `setup_lighting()`: Configures ambient and point lights
- `setup_camera()`: Positions and configures camera
- `setup_world()`: Sets background and environment

### scripts/animation.py
Animation module containing:
- `animate_orbit()`: Sets keyframes for circular text rotation
- `calculate_positions()`: Computes letter positions on sphere surface
- `setup_rotation_drivers()`: Configures continuous rotation

### scripts/render.py
Render configuration module containing:
- `configure_render_engine()`: Sets Cycles/Eevee settings
- `configure_output()`: Sets format, codec, quality
- `configure_compositor()`: Adds bloom/glow effects
- `execute_render()`: Triggers animation render

## Data Flow

1. **Initialization**: `run_blender.sh` invokes Blender with `main.py`
2. **Configuration Load**: `main.py` imports settings from `config.py`
3. **Scene Build**: `scene.py` creates all 3D objects and materials
4. **Animation Setup**: `animation.py` applies keyframes to objects
5. **Render Config**: `render.py` sets quality and output settings
6. **Execution**: Blender renders frames to video file
7. **Output**: Final MP4 written to `output/` directory

## Blender API Dependencies

| Module | Blender API |
|--------|-------------|
| scene.py | `bpy.ops.mesh`, `bpy.ops.object`, `bpy.data.materials` |
| animation.py | `bpy.context.scene.frame_set`, `obj.keyframe_insert` |
| render.py | `bpy.context.scene.render`, `bpy.ops.render.render` |

## Render Engines

### Eevee (Preview)
- Real-time rasterization
- Fast iteration (seconds per frame)
- Good for development and testing

### Cycles (Production)
- Path-traced ray tracing
- Physically accurate lighting
- Required for final output quality

## External Dependencies

- **Blender 4.5.1**: Self-contained, no pip packages needed
- **FFmpeg**: Bundled with Blender for video encoding
- **Python 3.11**: Bundled with Blender

## Error Handling

- Scripts validate Blender version on startup
- Missing fonts fall back to Blender's default
- Render failures log to console with frame number
- Output directory created if missing
