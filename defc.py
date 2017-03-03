import shelve
import os


def tdlist (todolist):
    if os.path.isfile(todolist+'.bak'):
        with shelve.open(todolist) as f:
            for k,v in f.items():
                print(v)
    else:
        with shelve.open(todolist) as f:
            print("You create a new list (after ',') ", todolist)
            g = input("What your want to add in your list? : \n")
            for i in g.split(','):
                print(i)
                f[i] = i

def remove(todolist):
    if os.path.isfile(todolist+'.bak'):
        v = []
        with shelve.open(todolist) as f:
            print("Your list:")
            for key, values in f.items():
                print(values)
                v.append(values)
        d = input("what you want delete: \n")
        v.remove(d)
        with shelve.open(todolist, 'n') as f:
            print("Your updated list:")
            for i in v:
                print(i)
                f[i] = i
    else:
        print("You haven't any list")


def add(todolist):
    if os.path.isfile(todolist+'.bak'):
        with shelve.open(todolist) as f:
            g = input("What your want to add in your list (after ',') ? : \n")
            for i in g.split(','):
                f[i] = i
        with shelve.open(todolist) as f:
            print("Your updated list:")
            for k,v in f.items():
                print(v)
    else:
        print("You haven't any list")