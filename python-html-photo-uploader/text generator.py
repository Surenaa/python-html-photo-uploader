def generate_text_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        print(f"Text file '{file_path}' successfully generated.")
    except IOError:
        print("An error occurred while generating the text file.")

# Usage example:
file_path = 'example.txt'
content = '''This is the content of the text file.
It can have multiple lines.
You can write anything you want.'''

generate_text_file(file_path, content)