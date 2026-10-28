# Local image generation

Fully offline 9:16 image generation on Apple Silicon. No UI, no server, no cloud.
Everything lives in this folder — engine, weights, LoRAs and output.

- Engine: [mflux](https://github.com/mflux-community/mflux) — MLX-native, built for Apple Silicon
- Model: Z-Image-Turbo (Tongyi Lab, 6B), quantized to 4-bit at `models/z-image-turbo-q4`
- ~90s per 720x1280 image, 4.5 GB peak memory

## Generate

Run from the repo root:

```bash
imagegen/gen.sh NAME "prompt text"
imagegen/gen.sh NAME -f rp/some_story/prompts/chapter1.txt
```

Output lands in `imagegen/out/NAME.png` plus `NAME.json` with the exact seed and
settings, so any image can be regenerated bit-for-bit.

Options: `-s SEED`, `-n STEPS`, `-r WxH`, `-N "negative prompt"`,
`-l path.safetensors:0.8` (repeatable).

## LoRAs

Drop `.safetensors` files in `imagegen/loras/` and reference them:

```bash
imagegen/gen.sh elara_vow "..." -l imagegen/loras/cinematic_skin.safetensors:0.7
```

Stack up to several; scales are independent. Z-Image LoRAs and LyCORIS LoKr are
both supported. Built-in styles are also available via
`--lora-style portrait|illustration|...` passed straight to mflux.

## Layout

| path | tracked | what |
|---|---|---|
| `gen.sh` | yes | the only entry point you need |
| `README.md` | yes | this file |
| `loras/` | yes (empty) | drop LoRA weights here |
| `out/` | **no** | all generated images |
| `models/` | **no** | 5.5 GB quantized weights |
| `.venv/` | **no** | Python env |

## Rebuilding from scratch

```bash
cd imagegen
uv venv .venv --python 3.12
uv pip install --python .venv/bin/python mflux
.venv/bin/mflux-save -m z-image-turbo -q 4 --path models/z-image-turbo-q4
```

The last command downloads 31 GB of bf16 weights to `~/.cache/huggingface`.
Once the 4-bit copy exists that cache can be deleted — the local copy is
self-contained.

Note: `.venv` holds absolute paths in its script shebangs, so it cannot be
moved. If this folder is relocated, delete `.venv` and recreate it with the two
commands above.

## Other models

`mflux-generate-<name>` entry points exist for FLUX.1-dev, Qwen-Image,
FLUX.2-Klein and others. `dev` at 4-bit gives stronger prompt adherence and
fabric detail but runs several times slower on this machine. Swap by changing
`MODEL` in `gen.sh` or calling the matching entry point directly.
