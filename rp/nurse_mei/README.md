# Nurse Mei — localized story packs

| File | Language |
|------|----------|
| `en.json` | English (source of truth) |
| `id.json` | Indonesian |
| `pt.json` | Portuguese (Brazil) |
| `ru.json` | Russian |
| `hi.json` | Hinglish (Roman script) |

Media (`*.mkv`, `*.webp`) is shared across locales. Do **not** translate `videoUrl` / `imageUrl`.

## Android loading

```text
base = …/rp/nurse_mei/
preferred = device language → en | id | pt | ru | hi
load base + preferred + ".json"
on 404 / parse fail → base + "en.json"
```

| Device locale | File |
|---------------|------|
| `in` / `id` | `id.json` |
| `pt` / `pt-BR` | `pt.json` |
| `ru` | `ru.json` |
| `hi` | `hi.json` |
| else | `en.json` |

Catalog entry: `rp/rp_lists.json` → `"file": "nurse_mei/en.json"`, `"locales": ["en","id","pt","ru","hi"]`, plus optional `i18n` listing copy.

Backward-compatible stub: `rp/nurse_mei.json` (same as `en.json`) for older builds that hardcode the top-level path.

## Validate

```bash
python3 tools/validate_rp_locale.py rp/nurse_mei/en.json --all
```

See `STYLE.md` and `GLOSSARY.md` before editing dialogue.
