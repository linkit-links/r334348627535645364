#!/usr/bin/env bash
# Run after: hf auth login  (with a WRITE token)
set -euo pipefail
REPO_ROOT="/Users/adamcohn/Projects/Cursor projects/MLX Local Lora Create"
STAGE="/Users/adamcohn/hf-lilien-lora"
HF="$REPO_ROOT/.venv/bin/hf"

cp "$REPO_ROOT/docs/huggingface/lilien-jugendstil-z-image-turbo/README.md" "$STAGE/README.md"
cp ~/loras/lilien_z_image_turbo_v1/lilien_z_image_turbo_v1.safetensors "$STAGE/" 2>/dev/null || true

# Ink calibration grids from latest test run
RUN=$(ls -td "$REPO_ROOT"/test_runs/lilien_z_image_turbo_v1__calibration__* 2>/dev/null | head -1)
if [[ -n "$RUN" && -d "$RUN/grids" ]]; then
  rm -rf "$STAGE/samples/grids" "$STAGE/samples/grids_color"
  mkdir -p "$STAGE/samples/grids" "$STAGE/samples/grids_color"
  cp "$RUN/grids/"*.png "$STAGE/samples/grids/"
fi

# Color calibration grids (no black ink on cream paper in prompts)
COLOR_RUN=$(ls -td "$REPO_ROOT"/test_runs/lilien_z_image_turbo_v1_color__calibration__* 2>/dev/null | head -1)
if [[ -n "$COLOR_RUN" && -d "$COLOR_RUN/grids" ]]; then
  mkdir -p "$STAGE/samples/grids_color"
  cp "$COLOR_RUN/grids/"*.png "$STAGE/samples/grids_color/"
fi

"$HF" repos create lilien-jugendstil-z-image-turbo --type model 2>/dev/null || true
"$HF" upload AdamSCohn/lilien-jugendstil-z-image-turbo "$STAGE" . \
  --commit-message "Update Lilien LoRA model card and calibration grids"

echo "Done: https://huggingface.co/AdamSCohn/lilien-jugendstil-z-image-turbo"
