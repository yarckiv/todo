import os


def add(todolist):
    with open(todolist, 'a+') as f:
        string = input("What you want to add (after ','): \n")
        f.write (string + '\n')
    with open (todolist) as f:
        print("Your list: \n" + f.read())


def remove(todolist):
    with open(todolist) as f:
        st=f.read()
        print("Your list \n", st)
        rem=input("What you want delete? \n")
        st = st.replace(rem, '')
        print("New list: \n", st)
    with open(todolist, 'w') as f:
        f.write(st)


def tdlist(todolist):
    if os.path.isfile(todolist):
        with open(todolist) as f:
            print("Your list \n",f.read())
    else:
        with open(todolist, 'w') as f:
            print("You create a new list "+f.name)
            string=input("What you want to add (after ','): \n")
            f.write(string + '\n')
        with open(todolist) as f:
            print("Your list: \n"+f.read())
