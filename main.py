# read the file

with open('new_example.txt', 'w') as file_object:
    content = 'new exmaple'
    file_object.write(content)