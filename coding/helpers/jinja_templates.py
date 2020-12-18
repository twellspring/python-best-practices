import glob
import jinaj2

def process_jinja(template_glob, jinja_vars):
    '''
    Process jinja templates and create a new file for each, removing the .j2 suffix
    Jinja2 templates should use this syntax for variables {{vars["var_name"]}} 
    '''

    for jinja_file in glob.glob(template_glob):
        with open(jinja_file) as infile:
            template = jinaj2.Template(infile.read())
        rendered_file = template.render(vars=jinja_vars)
        rendered_name = re.sub(f'.j2$', '', str(jinja_file))
        with open(rendered_name, 'w') as outfile:
            outfile.write(rendered_file)
