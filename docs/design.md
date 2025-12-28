# Design Document: Blender Text Sphere

## Visual Design

### Color Palette

The design uses a rainbow spectrum to match the CSS and Three.js implementations:

| Element | Color(s) | Hex Values |
|---------|----------|------------|
| Letter 1 | Red | `#FF0040` |
| Letter 2 | Orange | `#FF8000` |
| Letter 3 | Yellow | `#FFFF00` |
| Letter 4 | Lime | `#80FF00` |
| Letter 5 | Green | `#00FF40` |
| Letter 6 | Cyan | `#00FFFF` |
| Letter 7 | Blue | `#0080FF` |
| Letter 8 | Purple | `#8000FF` |
| Letter 9 | Magenta | `#FF00FF` |
| ... | Repeat cycle | ... |
| Background | Near Black | `#0A0A0F` |
| Sphere | Blue-Purple Gradient | `#2040A0` to `#6020A0` |

### Typography

- **Font**: Blender's built-in "Bfont" (default) or system sans-serif
- **Style**: Bold weight for visibility
- **Extrusion**: 0.15 units depth for 3D appearance
- **Bevel**: Slight edge bevel (0.02 units) for soft edges

### Sphere Appearance

```
Material Properties:
|-- Base Color: Deep blue-purple (#3030A0)
|-- Metallic: 0.1 (slight sheen)
|-- Roughness: 0.3 (soft reflections)
|-- Alpha: 0.7 (semi-transparent)
|-- Transmission: 0.3 (glass-like)
+-- Emission: 0.1 (subtle inner glow)
```

### Text Material (Per Letter)

```
Material Properties:
|-- Base Color: Rainbow (per letter)
|-- Metallic: 0.0
|-- Roughness: 0.4
|-- Emission Color: Same as base
|-- Emission Strength: 2.0 (glow effect)
+-- Subsurface: 0.1 (soft light transmission)
```

## Scene Layout

### Coordinate System

```
Top View (Z-up):
                    +Y
                     |
                     |    Letter positions
        +------------+------------+
        |    L3      |      L1    |
        |            |            |
   -X --+-------[SPHERE]----------+-- +X
        |            |            |
        |    L5      |      L7    |
        +------------+------------+
                     |
                    -Y

Side View:
                    +Z
                     |
        Letters orbit in XY plane
                     |
   -X -----------[SPHERE]------------- +X
                     |
                    -Z
```

### Dimensions

| Element | Value |
|---------|-------|
| Sphere radius | 3.0 units |
| Orbit radius | 8.0 units |
| Letter height | 1.2 units |
| Letter extrusion | 0.15 units |
| Scene bounds | 20 x 20 x 10 units |

### Camera Setup

```
Camera Properties:
|-- Type: Perspective
|-- Focal Length: 50mm
|-- Position: (0, -20, 5)
|-- Rotation: (75deg, 0deg, 0deg)
|-- Target: Scene origin (0, 0, 0)
+-- Depth of Field: Disabled (sharp focus)
```

### Lighting Setup

```
Light Rig:
|-- Key Light (Area)
|   |-- Position: (10, -10, 15)
|   |-- Power: 500W
|   +-- Color: Warm white (#FFF8F0)
|-- Fill Light (Area)
|   |-- Position: (-8, -5, 8)
|   |-- Power: 200W
|   +-- Color: Cool white (#F0F8FF)
|-- Rim Light (Point)
|   |-- Position: (0, 15, 5)
|   |-- Power: 300W
|   +-- Color: Blue-white (#E0E8FF)
+-- Ambient (World)
    |-- Color: Dark blue (#101020)
    +-- Strength: 0.1
```

## Animation Design

### Motion Characteristics

```
Orbit Animation:
|-- Type: Circular orbit in XY plane
|-- Direction: Counter-clockwise (top view)
|-- Speed: 360deg per 10 seconds (full rotation)
|-- Easing: Linear (constant speed)
+-- Loop: Seamless (frame 1 = frame 601)
```

### Letter Distribution

Letters are evenly distributed around the orbit:

```python
# For N letters, each letter offset:
angle_offset = 360 / N  # degrees

# Letter positions at time t:
for i, letter in enumerate(letters):
    base_angle = i * angle_offset
    current_angle = base_angle + (t * rotation_speed)
    x = orbit_radius * cos(radians(current_angle))
    y = orbit_radius * sin(radians(current_angle))
    z = 0  # Orbit in XY plane
```

### Keyframe Strategy

```
Frame Timeline (600 frames @ 60fps = 10 seconds):
|-- Frame 1: All letters at starting positions
|-- Frame 300: Letters at 180deg rotation (halfway)
|-- Frame 600: Letters at 360deg (back to start)
+-- Interpolation: Linear
```

## Post-Processing

### Compositor Nodes

```
Render Layers --> Glare (Bloom) --> Color Balance --> Output

Glare Settings:
|-- Type: Fog Glow
|-- Quality: High
|-- Mix: 0.3
|-- Threshold: 0.8
+-- Size: 8
```

### Color Grading

```
Color Balance:
|-- Shadows: Slight blue shift (+0.02 B)
|-- Midtones: Neutral
+-- Highlights: Slight warm shift (+0.01 R)

Contrast:
|-- Lift: 0.0
|-- Gamma: 1.0
+-- Gain: 1.05 (slight brightness boost)
```

## Render Settings

### Preview Mode (Eevee)

```
Eevee Settings:
|-- Samples: 32
|-- Bloom: Enabled
|   |-- Threshold: 0.8
|   +-- Intensity: 0.1
|-- Ambient Occlusion: Enabled
|-- Screen Space Reflections: Enabled
+-- Motion Blur: Disabled
```

### Production Mode (Cycles)

```
Cycles Settings:
|-- Device: GPU (if available)
|-- Samples: 128
|-- Denoising: OptiX/OIDN
|-- Light Paths:
|   |-- Max Bounces: 8
|   |-- Diffuse: 4
|   |-- Glossy: 4
|   +-- Transmission: 8
+-- Motion Blur: Disabled (clean frames)
```

### Output Format

```
Format:
|-- Container: MPEG-4
|-- Codec: H.264
|-- Quality: High (CRF 18)
|-- Resolution: 1920 x 1080
|-- Frame Rate: 60 fps
+-- Color Space: sRGB
```

## Accessibility Considerations

- High contrast between text and background
- Large, readable text characters
- Smooth motion (no rapid flashing)
- Color palette visible to most color vision types
