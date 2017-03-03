#!/usr/bin/env python
import func


name=input("What is your name?")
print("Hello {}, have a nice day.".format(name))
print("You can list or create a new list (l), add (a) or remove(r) in existing list")
ques=input("What you want?\n")
todolist=name


if (ques=="a"):
    print('Add:')
    func.add(todolist)
elif (ques=="r"):
    print('Remove:')
    func.remove(todolist)
elif (ques=="l"):
    print('List:')
    func.tdlist(todolist)
else:
    print("I don't understand what you want")



if __name__=="__main__":
    main()

