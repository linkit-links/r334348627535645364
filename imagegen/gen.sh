#!/usr/bin/env bash
# Local 9:16 image generation via mflux + Z-Image-Turbo (4-bit, Apple Silicon).
#
# Usage:
#   imagegen/gen.sh NAME "prompt text"          generate imagegen/out/NAME.png
#   imagegen/gen.sh NAME -f path/prompt.txt     read prompt from a file
#
# Options (after the prompt):
#   -s SEED      seed (default: random)
#   -n STEPS     steps (default: 9, Z-Image-Turbo's sweet spot)
#   -r WxH       resolution (default: 720x1280, exact 9:16)
#   -l PATH[:SCALE]  add a LoRA, repeatable. e.g. -l imagegen/loras/foo.safetensors:0.8
#   -N "text"    negative prompt
#
# Every run also writes imagegen/out/NAME.json with the full invocation, so any
# image can be reproduced exactly.

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MFLUX="$ROOT/.venv/bin/mflux-generate-z-image-turbo"
MODEL="$ROOT/models/z-image-turbo-q4"
OUT="$ROOT/out"

[[ -x "$MFLUX" ]] || { echo "mflux not installed. See imagegen/README.md" >&2; exit 1; }
[[ -d "$MODEL" ]] || { echo "quantized model missing at $MODEL" >&2; exit 1; }

(( $# >= 2 )) || { sed -n '2,20p' "${BASH_SOURCE[0]}" | sed 's/^# \?//'; exit 1; }

NAME="$1"; shift

if [[ "$1" == "-f" ]]; then
  [[ -f "$2" ]] || { echo "prompt file not found: $2" >&2; exit 1; }
  PROMPT="$(cat "$2")"
  shift 2
else
  PROMPT="$1"; shift
fi

SEED="$RANDOM"
STEPS=9
RES="720x1280"
NEG=""
LORA_ARGS=()

while (( $# )); do
  case "$1" in
    -s) SEED="$2"; shift 2 ;;
    -n) STEPS="$2"; shift 2 ;;
    -r) RES="$2"; shift 2 ;;
    -N) NEG="$2"; shift 2 ;;
    -l)
      # accept path or path:scale
      LPATH="${2%:*}"; LSCALE="${2##*:}"
      if [[ "$LPATH" == "$2" ]]; then LSCALE="1.0"; fi
      [[ -f "$LPATH" ]] || { echo "lora not found: $LPATH" >&2; exit 1; }
      LORA_ARGS+=(--lora "$LPATH" "$LSCALE")
      shift 2 ;;
    *) echo "unknown option: $1" >&2; exit 1 ;;
  esac
done

W="${RES%x*}"; H="${RES#*x}"
mkdir -p "$OUT"

ARGS=(
  -m "$MODEL"
  --prompt "$PROMPT"
  --width "$W" --height "$H"
  --steps "$STEPS"
  --seed "$SEED"
  --vae-tiling
  --output "$OUT/$NAME.png"
)
[[ -n "$NEG" ]] && ARGS+=(--negative-prompt "$NEG")
(( ${#LORA_ARGS[@]} )) && ARGS+=("${LORA_ARGS[@]}")

echo "→ $NAME  ${W}x${H}  steps=$STEPS  seed=$SEED"
"$MFLUX" "${ARGS[@]}" 2>&1 | grep -viE "^\s*$|redirects are currently not supported"

# reproducibility sidecar
python3 - "$OUT/$NAME.json" "$NAME" "$PROMPT" "$NEG" "$W" "$H" "$STEPS" "$SEED" \
  "${LORA_ARGS[@]+"${LORA_ARGS[@]}"}" <<'PY'
import json, sys
dst, name, prompt, neg, w, h, steps, seed, *lora = sys.argv[1:]
loras = []
for i in range(0, len(lora), 3):          # --lora PATH SCALE triples
    loras.append({"path": lora[i+1], "scale": float(lora[i+2])})
json.dump({
    "name": name, "model": "z-image-turbo-q4", "prompt": prompt,
    "negative_prompt": neg or None, "width": int(w), "height": int(h),
    "steps": int(steps), "seed": int(seed), "loras": loras,
}, open(dst, "w"), indent=2)
PY

echo "✓ out/$NAME.png"
