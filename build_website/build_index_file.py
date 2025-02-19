from html_templates import template_button, index_template

def build_index_file(docs_path, dirs):
    # this is just the first index file that will be built with all of the
    # folders in the first
    t_content = ''
    for d in dirs:
        # fixed the indent
        t_content += f'\n        ' + template_button.format(
            path='pages/' + d + '.html', 
            text=d)
    fpath = docs_path + '/index.html'
    with open(fpath, 'w') as file:
        file.write(
            index_template.safe_substitute(content=t_content))
    return