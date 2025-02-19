# this script is meant to be run as a github action
# it will generate the HTML files and search index based on the website_data
# folder

import os
import sys
from build_index_file import build_index_file
from build_htmls import build_html_intermediate_page, build_html_terminal_page, build_html_all_guidelines
from generate_search_index import generate_search_index


website_structure_path = '../docs/website_data/'
  
def scrape_website_data_folder_and_build():
    search_data = []
    # Read all sub-folders in the website structure path
    index_built = False
    all_guideline_root = None
    for root, dirs, files in os.walk(website_structure_path, topdown=True):
        
        # normalize path and replace backwards slashes with forward slashes
        
        root = os.path.normpath(root).replace('\\', '/')
        # DEBUG
        #print(root, dirs, files, '\n')
        # continue
        
        if index_built == False:
            build_index_file(root, dirs)
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
            build_html_intermediate_page(root, dirs)
        else:
            # this considers the case for files OR for empty dirs AND empty files
            # include search data since now you have things to search for            
            build_html_terminal_page(root, files, search_data)
    
    build_html_all_guidelines(all_guideline_root, search_data)
    generate_search_index(search_data)
    
    return

scrape_website_data_folder_and_build()

if __name__ == 'main':    
    scrape_website_data_folder_and_build()