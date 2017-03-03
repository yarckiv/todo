#!/usr/bin/env python
import defc


name=input("What is your name?")
print("Hello {}, have a nice day.".format(name))
print("You can list or create a new list (l), add (a) or remove(r) in existing list")
ques=input("What you want?\n")
todolist=name


if (ques=="a"):
    print('Add:')
    defc.add(todolist)
elif (ques=="r"):
    print('Remove:')
    defc.remove(todolist)
elif (ques=="l"):
    print('List:')
    defc.tdlist(todolist)
else:
    print("I don't understand what you want")





