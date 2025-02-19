import os

script_dir = os.path.dirname(os.path.abspath(__file__))
docs_path = script_dir + '../docs/'
website_structure_path = docs_path + 'website_data/'

def add_gitkeep(directory):
    for root, dirs, files in os.walk(directory):
        if not dirs and not files:
            gitkeep_path = os.path.join(root, '.gitkeep')
            with open(gitkeep_path, 'w') as f:
                pass
            print(f'Added .gitkeep to {root}')

if __name__ == '__main__':
    add_gitkeep(website_structure_path)