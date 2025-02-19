import os

def add_gitkeep(directory):
    for root, dirs, files in os.walk(directory):
        if not dirs and not files:
            gitkeep_path = os.path.join(root, '.gitkeep')
            with open(gitkeep_path, 'w') as f:
                pass
            print(f'Added .gitkeep to {root}')

if __name__ == '__main__':
    website_structure_path = '../docs/website_data/'
    add_gitkeep(website_structure_path)