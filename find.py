from pathlib import Path
import json, base64, zlib

for path in (Path('.') / 'Mod' / 'assets' / 'game' / 'worldgen' / 'schematics').rglob('*.json'):
    with path.open('r') as fp:
        data = json.load(fp = fp)
    
    block_codes = data.get('BlockCodes')
    if not block_codes:
        continue

    indices = data.get('Indices')
    if not indices:
        continue

    block_ids = data.get('BlockIds')
    if not indices:
        continue

    block_entities = data.get('BlockEntities')
    if not block_entities:
        continue

    block_codes_lut = dict()
    for block_id, block_name in block_codes.items():
        if block_name.startswith('game:tapestry'):
            block_codes_lut[block_id] = block_name

    if not len(block_codes_lut):
        continue

    found = False
    for index_val, block_id in zip(indices, block_ids):
        block_name = block_codes_lut.get(str(block_id))
        if not block_name:
            continue
        block_entity_encoded = block_entities.get(str(index_val))
        if not block_entity_encoded:
            continue
        found = True
    if found:
        print(f"Found: {path}")