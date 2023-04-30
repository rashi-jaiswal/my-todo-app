FP = "tasks.txt"


def get_tasks(x=FP):
    """ Read a text file and return the list of to-do items."""
    with open(x, 'r') as store_local:
        tasks_local = store_local.readlines()
    return tasks_local

def write_tasks(tasks_arg, y=FP):
    """ Write the to-do items list in the text file."""
    with open(y,'w') as store:
        store.writelines(tasks_arg)


print(__name__)
if __name__ == "__main__":
    print("Hello")
    print(get_tasks())

