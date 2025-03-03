import csv
from html_templates import *

# Template for the category pages

def build_html_intermediate_page(root, dirs, pages_directory_path):
    # OK this is the easiest by far so we start here
    # will use the template intermediate
    # the os.walk will send the root and the directory list
    # example: ../website_data/Adult Trauma Surgery ['Head', 'Neck', 'Chest', 'Abdomen', 'Pelvis', 'Spine', 'Extremities', 'Other Adult Trauma'] [] 

    t_title = root.split('/')[-1]
    t_lastpage = root.split('/')[-2]
    t_lastpage_path = ''
    use_lastpage = True
    
    if t_lastpage == 'website_data':
        use_lastpage = False
    else:
        use_lastpage = True
        t_lastpage_path = 'pages/' + t_lastpage + '.html'
    
    t_content = '<div class="button-container">'
    
    dirs.sort() # sort alphabetically
    
    for d in dirs:
        t_content += f'\n    ' + template_button.format(path='pages/' + d + '.html', text=d)
    t_content += "\n</div>"
    
    if use_lastpage:
        with open(pages_directory_path + t_title + '.html', 'w') as file:
            file.write(template_intermediate.format(title=t_title, lastpage=t_lastpage, lastpage_path=t_lastpage_path, content=t_content))
    else:
        with open(pages_directory_path + t_title + '.html', 'w') as file:
            file.write(template_intermediate_home_is_lastpage.format(title=t_title, content=t_content))
    return

def generate_content_from_data_csv(filepath):
    # csv is in the format "text, url"
    t_content = '<div class ="button-container">'
    with open(filepath, newline = '') as file:
        file_data = csv.reader(file)
        file_data = list(file_data)
        file_data.sort(key=lambda row :row[0 ])
        for row in file_data:
            text, url = row
            t_content += f'\n    ' + template_button.format(path=url, text=text)
        t_content += "\n</div>"
    return t_content

def generate_content_from_pdfs(root, 
                               file,
                               all_guideline_data,
                               pages_directory_path,
                               templates_path,
                               t_lastpage,
                               t_lastpage_path,): 
    
    root_modified = root.split('/docs/')[1] # get all AFTER docs
    root_modified += '/' # they end without a forward slash from the os walk
    # pdfs is a list of pdfs
    
    t_content = "<div>"
    file.sort() # sort alphabetically
    
    if t_lastpage == 'website_data':
        templates_path = templates_path + 'pdf_template_home_index.html'
    else:
        templates_path = templates_path + 'pdf_template.html'
    
    for pdf in file:
        pdf_name = '.'.join(pdf.split('.')[:-1]) # get everything before the .pdf and re-join it together
        pdf_path = root_modified + pdf
        # modifying PDF path to actually be to the HTML file    
        # generate HTML file for the PDF
        
        pdf_viewer_path = 'pages/' + f'{pdf_name}.html'
        pdf_view_full_path = pages_directory_path + pdf_name + '.html'
    
        # give the VIEWER data to the all guidelines so it points to the VIEWER
        # instead of pointing to the raw PDF
        
        all_guideline_data.append(pdf_name)
        
        with open(templates_path, 'r') as template_file:
            template_content = template_file.read()
        if t_lastpage == 'website_data':
            template_content = template_content.replace('$title', pdf_name).replace('$pdf_url', pdf_path)
        else:
            template_content = template_content.replace('$title', pdf_name).replace('$pdf_url', pdf_viewer_path).replace('$lastpage', t_lastpage).replace('$lastpath', t_lastpage_path)
        with open(pdf_view_full_path, 'w') as pdf_viewer_file:
            pdf_viewer_file.write(template_content)
        
        t_content += f'\n    <div><h3><a href="{pdf_name}.html" target="_blank">{pdf_name}</a></h3></div>\n'
        #t_content += f'\n    <div><a href="{pdf_path}">{pdf_name}</a></div>\n'
    t_content += "\n</div>"
    
    return t_content
    
def build_html_terminal_page(root, 
                             file, 
                             search_data, 
                             pages_directory_path,
                             templates_path):
    # check if file is empty, a CSV, or PDFs
    t_content = None
    t_title = root.split('/')[-1]
    t_lastpage = root.split('/')[-2]
    t_lastpage_path = ''
    use_lastpage = True
    
    if t_lastpage == 'website_data':
        use_lastpage = False
    else:
        use_lastpage = True
        t_lastpage_path = 'pages/' + t_lastpage + '.html'
    
    if file == []:
        # empty case
        t_content = ''
    elif file[0] == 'data.csv':
        t_content = generate_content_from_data_csv(root + '/' + file[0])
    else:
        # now file is a list that contains PDFs
        # we want to strip the .pdf from the end of the file for the name
        t_content = generate_content_from_pdfs(root, 
                                               file, 
                                               search_data,
                                               pages_directory_path,
                                               templates_path,
                                               t_lastpage,
                                               t_lastpage_path)

    if use_lastpage:
        with open(pages_directory_path + t_title + '.html', 'w') as file:
            file.write(
                template_terminal.format(
                    title=t_title, 
                    lastpage=t_lastpage, 
                    lastpage_path=t_lastpage_path, 
                    content=t_content))        
    else:
        with open(pages_directory_path + t_title + '.html', 'w') as file:
            file.write(
                template_terminal_home_is_lastpage.format(
                    title=t_title, content=t_content))

    return search_data
  
def build_html_all_guidelines(root, all_guidelines_data, pages_directory_path):
    
    t_title = root.split('/')[-1]
    t_content = '<div>'
    
    all_guidelines_data.sort()

    for pdf_name in all_guidelines_data:
        pdf_path = 'pages/' + pdf_name + '.html'
        t_content += f'\n    <div><h3><a href="{pdf_path}" target="_blank">{pdf_name}</a></h3></div>\n'
    t_content += "\n</div>"
    
    pages_directory_path = pages_directory_path + t_title + '.html'
    
    with open(pages_directory_path, 'w') as file:
        file.write(
            template_terminal_home_is_lastpage.format(
                title=t_title,  
                content=t_content))
    
    return