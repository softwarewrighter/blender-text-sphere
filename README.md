# Blender Text Sphere

A Python-scripted Blender project that renders 3D text orbiting around a sphere, producing video output that matches the visual style of the related web UI demos.

![Blender Text Sphere Screenshot](images/screenshot.png?ts=1735433189311)

## Overview

This project generates a 60fps 1080p video animation featuring rainbow-colored 3D text letters continuously orbiting around a translucent central sphere. The animation is created entirely through Python scripts that control Blender's scene construction, animation, and rendering pipeline.

## Related Projects

This is part of a series of text-sphere demos across different technologies:

- [css-text-sphere](https://github.com/softwarewrighter/css-text-sphere) - Pure CSS3 implementation
- [d3-text-sphere](https://github.com/softwarewrighter/d3-text-sphere) - D3.js implementation
- [godot-text-sphere](https://github.com/softwarewrighter/godot-text-sphere) - Godot 4 implementation
- [three-text-sphere](https://github.com/softwarewrighter/three-text-sphere) - Three.js/Rust/WASM implementation
- [wasm-text-sphere](https://github.com/softwarewrighter/wasm-text-sphere) - WebAssembly implementation

## Requirements

- Blender 4.5.1 (path: `/home/mike/tools/blender-4.5.1-linux-x64`)
- No additional Python packages required (uses Blender's built-in Python)

## Usage

```bash
# Run the render script
./run_blender.sh

# Preview mode (fast, lower quality)
./run_blender.sh --preview

# Production mode (slow, high quality)
./run_blender.sh --production
```

Output will be saved to `output/text_sphere.mp4`.

## Project Structure

```
blender-text-sphere/
|-- docs/               # Documentation
|-- scripts/            # Python scripts for Blender
|-- output/             # Rendered video output
|-- run_blender.sh      # Launch script
+-- README.md           # This file
```

## Documentation

- [Product Requirements](docs/prd.md) - Goals, requirements, and success criteria
- [Architecture](docs/architecture.md) - System design and component overview
- [Design](docs/design.md) - Visual design, colors, and render settings
- [Planning](docs/planning.md) - Implementation phases and task breakdown
- [Status](docs/status.md) - Current project progress

## Output Specifications

| Property | Value |
|----------|-------|
| Resolution | 1920x1080 |
| Frame Rate | 60 fps |
| Duration | 10 seconds |
| Format | MP4 (H.264) |
| Loop | Seamless |

## License

MIT
