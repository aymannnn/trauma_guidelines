import os
import csv
import json

def generate_search_index(csv_file='all_csv_search.csv', output_file='../docs/search-index.json'):
    index = []

    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) < 2:
                continue
            text, pdf_path = row
            index.append({
                'text': text,
                'url': pdf_path
            })

    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2)
    print(f'Search index generated successfully and saved to {output_file}')

if __name__ == '__main__':
    generate_search_index()
