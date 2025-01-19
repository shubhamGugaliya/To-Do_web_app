def get_todos(filepath='todos.txt'):
    """Read the text file and return
    the list of to-do"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg,filepath='todos.txt'):
    """Write a to-do items list in the text file"""
    with open('todos.txt', 'w') as file:
        todos = file.writelines(todos_arg)

