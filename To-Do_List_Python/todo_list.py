user_input ='random'
todo_list =[]
while user_input !='4':
    print('1)Add a task\n2)Mark as done\n3)View to-do list\n4)Exit')
    user_input=input('Enter Option: ')

    if user_input == '1':
        task=input('Task: ')
        todo_list.append(task)
        print('Task created -> ',task)
    elif user_input == '2':
        task=input('Task to mark: ')
        if task in todo_list:
            print('Task Completed: ',task)
            todo_list.remove(task)
        else:
            print("Task doesn't exist")
    elif user_input == '3':
        print('Todo list:')
        for task in todo_list:
            print(task)
    elif user_input == '4':
        print('Goodbye!')
    else:
        print('Please select a valid input!')