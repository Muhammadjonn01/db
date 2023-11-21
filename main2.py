from registration_login_exit import Registration
from all_work_with_tasks import TodoListManager

manager = TodoListManager()
reg = Registration()
run_1 = True
run = False
while run_1 == True:
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        username = input("Enter username: ")
        password = input("Enter password: ")
        reg.append_users(username, password)
        run = True
    elif choice == '2':
        username = input("Enter username: ")
        password = input("Enter password: ")
        while True:
            if(reg.check_user(username, password) == True):
                run =True
                break   
    elif choice == '3':
        print("Exit:")
        break
    else:
        print("Invalid choice. Please try again.")
    while run_1 == True:
            print('1. Add:')
            print('2. Remove:')
            print('3. Sort by priority:')
            print('4. Show all tasks:')
            print('5. Mark task as completed:')
            print('6. Todays tasks:')
            print('7. :Exit:')
            inp = input("Input your choice:")
            if inp == '1':
                manager.add_task()
            elif inp == '2':
                manager.remove_task()
            elif inp == '3':
                manager.sort_by_priority()
            elif inp == '4':
                manager.view_tasks()
            elif inp == '5':
                manager.mark_task_as_completed()
            elif inp == '6':
                manager.show_todays_tasks()
            elif inp == '7':
                print("Exiting....")
                break
            else:
                print("Invalid input")