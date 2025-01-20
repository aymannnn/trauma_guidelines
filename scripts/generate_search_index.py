import os
import json
from bs4 import BeautifulSoup

def generate_search_index(base_dir='../docs/pages', output_file='../docs/search-index.json'):
    index = []

    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    soup = BeautifulSoup(content, 'html.parser')
                    
                    title = soup.title.string if soup.title else 'No title'
                    bullet_points = []
                    for li in soup.find_all('li'):
                        # Remove any links within the bullet points
                        for a in li.find_all('a'):
                            a.decompose()
                        bullet_points.append(li.get_text(separator=' ', strip=True))
                    bullet_points_text = ' '.join(bullet_points)
                    
                    # Extract button text and links
                    buttons = []
                    for button in soup.find_all('button'):
                        button_text = button.get_text(strip=True)
                        button_link = button.get('onclick', '').replace("location.href='", "").replace("'", "")
                        buttons.append(f'{button_text}: {button_link}')
                    buttons_text = ' '.join(buttons)
                    
                    index.append({
                        'url': os.path.relpath(file_path, base_dir),
                        'title': title,
                        'content': bullet_points_text,
                        'buttons': buttons_text
                    })

    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2)
    print(f'Search index generated successfully and saved to {output_file}')

if __name__ == '__main__':
    generate_search_index()
