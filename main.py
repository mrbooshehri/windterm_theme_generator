from jinja2 import Environment, FileSystemLoader
import yaml, os

# Create output directory
if not os.path.exists("output"):
    os.mkdir("output")

# loading color files
colors = yaml.full_load(open('colors.yml'))
# loading jija2 template
env = Environment(loader=FileSystemLoader("templates"), trim_blocks=True, lstrip_blocks=True)
for template_file in os.listdir("templates"):
    template = env.get_template(os.path.join("./", template_file))
    output_name = f"{template_file}".replace('.j2', '')
    # render template
    with open(f"output/{output_name}", 'w') as output_file:
        output_file.write(template.render(colors))

