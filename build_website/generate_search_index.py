import os
import json

# TODO: change to search-index not test_search-index

def generate_search_index(
    guideline_data, 
    output_file='../docs/search-index.json'):
    index = []
    for data in guideline_data:
        pdf_title = data[0]
        pdf_path = data[1]
        index.append({
            'text': pdf_title,
            'url': pdf_path
        })
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2)
    return