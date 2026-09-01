#!/usr/bin/env python3
import json

# Load both files
with open('rp/same_room_weekend/en.json', 'r', encoding='utf-8') as f:
    en_data = json.load(f)

with open('rp/same_room_weekend/id.json', 'r', encoding='utf-8') as f:
    id_data = json.load(f)

# Get existing IDs
existing_ids = {node['id'] for node in id_data['nodes']}

print(f"English nodes: {len(en_data['nodes'])}")
print(f"Indonesian nodes: {len(id_data['nodes'])}")
print(f"Remaining: {len(en_data['nodes']) - len(id_data['nodes'])}")

# Find the last translated node
last_id = id_data['nodes'][-1]['id']
print(f"\nLast translated node: {last_id}")

# Find index in English
last_index = next(i for i, node in enumerate(en_data['nodes']) if node['id'] == last_id)
print(f"Index in English file: {last_index}")
print(f"\nNext nodes to translate:")
for i in range(last_index + 1, min(last_index + 11, len(en_data['nodes']))):
    node = en_data['nodes'][i]
    print(f"  {node['id']}: {node.get('chapterTitle', 'continuation')}")
