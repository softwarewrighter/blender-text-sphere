# Planning Document: Blender Text Sphere

## Implementation Phases

### Phase 1: Project Setup
- [x] Create project directory structure
- [x] Document Blender installation path
- [x] Create PRD, architecture, and design documents
- [x] Create planning and status documents
- [ ] Create README with project overview

### Phase 2: Core Scripts
- [ ] Create `scripts/config.py` with all configuration constants
- [ ] Create `scripts/main.py` orchestrator
- [ ] Create `run_blender.sh` launcher script
- [ ] Verify Blender can execute scripts headlessly

### Phase 3: Scene Construction
- [ ] Implement `scripts/scene.py`
  - [ ] `clear_scene()` - Remove default objects
  - [ ] `create_sphere()` - Central translucent sphere
  - [ ] `create_text_objects()` - 3D text for each letter
  - [ ] `setup_materials()` - Rainbow emissive materials
  - [ ] `setup_lighting()` - Three-point light rig
  - [ ] `setup_camera()` - Camera positioning
  - [ ] `setup_world()` - Background and environment

### Phase 4: Animation
- [ ] Implement `scripts/animation.py`
  - [ ] `calculate_orbit_positions()` - Letter placement math
  - [ ] `animate_rotation()` - Keyframe insertion
  - [ ] `verify_loop()` - Ensure seamless loop

### Phase 5: Rendering
- [ ] Implement `scripts/render.py`
  - [ ] `configure_eevee()` - Preview render settings
  - [ ] `configure_cycles()` - Production render settings
  - [ ] `setup_compositor()` - Bloom/glow effects
  - [ ] `configure_output()` - Video format settings
  - [ ] `execute_render()` - Trigger render

### Phase 6: Testing & Polish
- [ ] Test preview render (Eevee)
- [ ] Verify visual match with web demos
- [ ] Test production render (Cycles)
- [ ] Optimize render times if needed
- [ ] Verify seamless loop playback

### Phase 7: Documentation & Cleanup
- [ ] Update README with usage instructions
- [ ] Document any system-specific configurations
- [ ] Add sample output or screenshots
- [ ] Final code review and cleanup

## Task Breakdown

### config.py Tasks
| Task | Priority | Complexity |
|------|----------|------------|
| Define text characters | High | Low |
| Set sphere parameters | High | Low |
| Set orbit parameters | High | Low |
| Define color palette | High | Low |
| Set render resolution | High | Low |
| Set frame count/duration | High | Low |
| Define file paths | Medium | Low |

### scene.py Tasks
| Task | Priority | Complexity |
|------|----------|------------|
| Clear default scene | High | Low |
| Create UV sphere mesh | High | Low |
| Apply sphere material | High | Medium |
| Create text objects | High | Medium |
| Position text in orbit | High | Medium |
| Apply text materials | High | Medium |
| Add key light | High | Low |
| Add fill light | Medium | Low |
| Add rim light | Medium | Low |
| Position camera | High | Low |
| Set world background | High | Low |

### animation.py Tasks
| Task | Priority | Complexity |
|------|----------|------------|
| Calculate letter angles | High | Medium |
| Set initial positions | High | Medium |
| Insert rotation keyframes | High | Medium |
| Set linear interpolation | High | Low |
| Verify frame 1 = frame N+1 | High | Low |

### render.py Tasks
| Task | Priority | Complexity |
|------|----------|------------|
| Configure Eevee settings | High | Low |
| Configure Cycles settings | High | Medium |
| Enable bloom compositor | Medium | Medium |
| Set output format | High | Low |
| Execute render command | High | Low |

## Dependencies

```
Phase 1 ──► Phase 2 ──► Phase 3 ──► Phase 4 ──► Phase 5 ──► Phase 6 ──► Phase 7
                │                      │           │
                └──────────────────────┴───────────┘
                    (config.py shared by all)
```

## Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Blender API changes | Low | High | Pin to Blender 4.5.1 |
| Slow render times | Medium | Medium | Use Eevee for previews |
| Font not available | Low | Low | Use Blender's built-in font |
| GPU not detected | Medium | Low | Fall back to CPU rendering |
| Memory issues | Low | Medium | Reduce samples if needed |

## Testing Strategy

### Unit Testing
- Each scene.py function creates expected object
- Animation produces correct number of keyframes
- Config values are within valid ranges

### Integration Testing
- Full pipeline runs without errors
- Output file is valid MP4
- Video plays in standard players

### Visual Testing
- Compare against CSS text sphere screenshot
- Verify colors match palette
- Confirm smooth animation at 60fps
- Check seamless loop point

## Definition of Done

A task is complete when:
1. Code is written and saved
2. Script runs without errors
3. Output matches expected result
4. Related documentation updated
