# this script is meant to be run as a github action
# it will generate the HTML files and search index based on the website_data
# folder

import os
import sys
from build_index_file import build_index_file
from build_htmls import build_html_intermediate_page, build_html_terminal_page, build_html_all_guidelines
from generate_search_index import generate_search_index

# path is relative to trauma_guidelines since that's where this script is run
# Get the directory of the script

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct paths relative to the script's location, going one directory back
docs_path = os.path.abspath(os.path.join(script_dir, '../docs/'))
website_structure_path = os.path.join(docs_path, 'website_data/')
pages_directory_path = os.path.join(docs_path, 'pages/')
  
def scrape_website_data_folder_and_build():
    search_data = []
    # Read all sub-folders in the website structure path
    index_built = False
    all_guideline_root = None
    debug_root_dirs_files = []
    
    print(script_dir, docs_path, website_structure_path, pages_directory_path)
    
    # Ensure the /pages/ directory exists
    os.makedirs(pages_directory_path, exist_ok=True)
    
    
    for root, dirs, files in os.walk(website_structure_path, topdown=True):
        
        debug_root_dirs_files.append([root, dirs, files])
        
        # remove .gitkeep from files
        
        if '.gitkeep' in files:
            files.remove('.gitkeep')
        
        # normalize path and replace backwards slashes with forward slashes
        
        root = os.path.normpath(root).replace('\\', '/')
        # DEBUG
        #print(root, dirs, files, '\n')
        # continue
        
        if index_built == False:
            build_index_file(docs_path, dirs)
            index_built = True
            continue
        
        if root.split('/')[-1] == 'All Guidelines':
            all_guideline_root = root
            # build all guidelines at the end
            continue
        
        if dirs and files:
            print('Error, if there are directories, there should not be files, and vice versa. Files should only exist in terminal web pages')
            sys.exit(1)
        
        if dirs:
            # not a terminal node
            # do not need to send search data since nothing to search            
            build_html_intermediate_page(root, dirs, pages_directory_path)
        else:
            # this considers the case for files OR for empty dirs AND empty files
            # include search data since now you have things to search for            
            build_html_terminal_page(root, files, search_data, pages_directory_path)
            
    print('Web pages built successfully')    
    
    print(all_guideline_root)
    
    if all_guideline_root:
        build_html_all_guidelines(all_guideline_root, search_data, pages_directory_path)
    else:
        print("Error: 'All Guidelines' directory not found.")
        print(debug_root_dirs_files)
        sys.exit(1)
    print('All guidelines built successfully')
    generate_search_index(search_data, docs_path)
    print('Search index built successfully')
    return

if __name__ == '__main__':
    scrape_website_data_folder_and_build()