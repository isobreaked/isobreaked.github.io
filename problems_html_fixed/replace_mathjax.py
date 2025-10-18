import os
import shutil

# Strings to replace
old = '\mathbb'
new = '\mathbf'

# Loop through all files in current folder
for filename in os.listdir('.'):
    if filename.endswith('.html'):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        if old in content:
            # Make backup
            # shutil.copy(filename, filename + '.bak')

            # Replace
            content = content.replace(old, new)

            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)

            print(f'Updated: {filename}')
        else:
            print(f'No change: {filename}')
