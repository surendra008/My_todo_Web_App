

def get_todos(filename='todos.txt'):
    with open(filename, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_args,filename='todos.txt'):
    with open(filename, "w") as file:
        file.writelines(todos_args)

if __name__ == "__main__":
    print("hello")
    print(get_todos())
