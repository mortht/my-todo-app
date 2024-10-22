import os

DEFAULT_FILE_PATH = 'todos.txt'


def init_todos(filepath=DEFAULT_FILE_PATH):
    if not os.path.exists(filepath):
        with open(filepath, 'w'):
            pass


def get_todos(filepath=DEFAULT_FILE_PATH):
    """ Read a text file and return the list of to-do items. """
    with open(filepath, 'r') as file:
        return file.readlines()


def save_todos(todos_arg, filepath=DEFAULT_FILE_PATH):
    """ Write the to-do items list in a text file. """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())
