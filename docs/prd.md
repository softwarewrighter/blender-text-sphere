# Product Requirements Document: Blender Text Sphere

## Overview

Blender Text Sphere is a Python-scripted 3D visualization project that renders animated text orbiting around a sphere using Blender. This project is part of a series of text-sphere demos implemented across different technologies (CSS, D3, Godot, Three.js, WASM).

## Goals

1. Create a Blender-based implementation of the text sphere animation that visually matches the existing web/game engine demos
2. Generate high-quality video output suitable for comparison with other implementations
3. Provide a scriptable, reproducible pipeline for scene creation and rendering
4. Demonstrate Blender's capabilities for procedural 3D animation

## Target Output

- **Format**: MP4 video (H.264 codec)
- **Resolution**: 1920x1080 (1080p)
- **Frame Rate**: 60 FPS
- **Duration**: 10-second loop (600 frames)
- **Background**: Dark/black gradient matching web demos

## Visual Requirements

### Central Sphere
- Translucent or semi-transparent material
- Subtle gradient shading (blue-purple tones)
- Soft shadow/glow effect
- Positioned at scene origin

### Orbiting Text
- Individual 3D extruded letters spelling a configurable word/phrase
- Default text: "BLENDER TEXT SPHERE" (or similar)
- Rainbow color gradient across letters
- Emissive/glow material for each letter
- Letters arranged in circular orbit around sphere
- Continuous rotation animation (clockwise or configurable)

### Lighting & Environment
- Dark background (near-black or gradient)
- Ambient lighting for overall visibility
- Point/area lights to enhance sphere reflections
- Bloom/glow post-processing effect

### Camera
- Static camera positioned to frame entire animation
- Centered on sphere with adequate margin for orbiting text
- Optional: subtle camera movement for added depth

## Functional Requirements

### Script Structure
1. **Controller Script** (`run_blender.py`): Launches Blender with appropriate arguments
2. **Scene Script** (`scene.py`): Defines 3D objects, materials, and scene setup
3. **Animation Script** (`animation.py`): Defines keyframes and motion
4. **Render Script** (`render.py`): Configures render settings and executes render

### Configuration
- Configurable text content
- Adjustable sphere size and orbit radius
- Customizable rotation speed
- Selectable color palette
- Render quality presets (preview, production)

### Output
- Rendered video file in `output/` directory
- Optional: individual frame export for debugging
- Console progress feedback during render

## Non-Functional Requirements

- Scripts must work with Blender 4.5.1
- No external Python dependencies beyond Blender's built-in modules
- Render time under 30 minutes on modern hardware (production quality)
- Preview renders under 2 minutes

## Success Criteria

1. Generated video visually matches the aesthetic of existing text-sphere demos
2. Animation loops seamlessly (first and last frame match)
3. Scripts run without manual intervention
4. Documentation enables reproduction on other systems

## Out of Scope

- Interactive real-time viewing (batch render only)
- Web export/deployment
- Audio/sound effects
- Multiple animation variations (single canonical output)
