import json
from jinja2 import Template
from seedsigner.models.settings import SettingsDefinition



print("Generating static index.html")

# Extract the SettingsDefinition from the SeedSigner source
settings_definition_dict = SettingsDefinition.to_dict()

# Load the Jinja2 template
with open("index.jinja", 'r') as template_file:
    template = Template(template_file.read())

template_data = {
    "settings_entries": [],
}

for entry in settings_definition_dict.get("settings_entries"):
    print(entry["attr_name"])
    if entry["visibility"] == "hidden":
        print(f"""Skipping hidden setting '{entry["attr_name"]}'""")
        continue
    if entry.get("abbreviated_name"):
        entry["attr_name"] = entry["abbreviated_name"]
    template_data["settings_entries"].append(entry)

# Render the final static index.html
final_html = template.render(template_data)
with open("index.html", 'w') as html_file:
    html_file.write(final_html)
