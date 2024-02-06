import json
import re

# Load project names
with open('projects.json') as file:
    projects = json.load(file)

# Generate Markdown content
markdown_content = "\n".join([
    f"""<a href="https://github.com/haroonj/{project}#gh-dark-mode-only" target="_blank">
  <img align="center" src="https://github-readme-stats.vercel.app/api/pin/?username=haroonj&repo={project}&theme=nightowl&show_owner=true#gh-dark-mode-only"/>
</a>
<a href="https://github.com/haroonj/{project}#gh-light-mode-only" target="_blank">
  <img align="center" src="https://github-readme-stats.vercel.app/api/pin/?username=haroonj&repo={project}&theme=vue&show_owner=true#gh-light-mode-only"/>
</a>\n""" for project in projects
])

# Read current README
with open('README.md', 'r') as file:
    readme_contents = file.read()

# Define the start and end markers for the projects section
start_marker = '<!-- projects-start -->'
end_marker = '<!-- projects-end -->'

# Replace the old projects section with the new content
new_readme_contents = re.sub(f"{start_marker}.*?{end_marker}",
                             f"{start_marker}\n{markdown_content}\n{end_marker}",
                             readme_contents, flags=re.DOTALL)

# Write the updated README back to the file
with open('README.md', 'w') as file:
    file.write(new_readme_contents)
