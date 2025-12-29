#!/bin/bash
#
# Blender Text Sphere - Launcher Script
#
# Usage:
#   ./run_blender.sh              # Preview mode (Eevee, fast)
#   ./run_blender.sh --preview    # Preview mode (explicit)
#   ./run_blender.sh --production # Production mode (Cycles, slow)
#   ./run_blender.sh --no-render  # Build scene only, no render
#

set -e

# Blender executable path
BLENDER_PATH="/home/mike/tools/blender-4.5.1-linux-x64/blender"

# Script directory (where this script lives)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Main Python script
MAIN_SCRIPT="${SCRIPT_DIR}/scripts/main.py"

# Check if Blender exists
if [ ! -x "$BLENDER_PATH" ]; then
    echo "Error: Blender not found at $BLENDER_PATH"
    echo "Please update BLENDER_PATH in this script."
    exit 1
fi

# Check if main script exists
if [ ! -f "$MAIN_SCRIPT" ]; then
    echo "Error: Main script not found at $MAIN_SCRIPT"
    exit 1
fi

# Print banner
echo "========================================"
echo "  Blender Text Sphere Renderer"
echo "========================================"
echo "Blender: $BLENDER_PATH"
echo "Script:  $MAIN_SCRIPT"
echo "Args:    $@"
echo "========================================"
echo ""

# Run Blender in background mode with the Python script
# Pass any command line arguments after '--'
"$BLENDER_PATH" --background --python "$MAIN_SCRIPT" -- "$@"

echo ""
echo "Done!"
