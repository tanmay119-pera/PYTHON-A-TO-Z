'''                             PYTHON-MINI-PROJECT-4 "TO-DO LIST"                               '''

import os

# This list will store our tasks as small dictionaries
todo_list = []

def clear_screen():
    # Clears the terminal screen for a cleaner UI
    os.system('cls' if os.name == 'nt' else 'clear')

    # It's shows the task list after clearing the screen
def show_tasks():
    clear_screen()
    print("=" * 35)
    print("      📝 MY AWESOME TO-DO LIST")
    print("=" * 35)
    
    if not todo_list:
        print("  📭 Your list is completely empty!")
        print("  Time to chill, or add a task.")
    else:
        for index, item in enumerate(todo_list, start=1):
            # Choose the right emoji based on completion status
            status_icon = "✅" if item['completed'] else "⏳"
            
            # Strike-through effect for completed tasks
            task_name = item['task']
            if item['completed']:
                task_name = f"~{task_name}~ (Done)"
                
            print(f"  {index}. {status_icon}  {task_name}")
    print("=" * 35)

# Adding a main function to encapsulate the program logic
def main():
    while True:
        show_tasks()
        
        print("\nWhat would you like to do?")
        print("1. ➕ Add a Task")
        print("2. ✔️  Mark Task as Done")
        print("3. ❌ Delete a Task")
        print("4. 🚪 Exit")
        
        choice = input("\nEnter your choice (1-4): ")

        # Validate user input
        if choice == '1':
            new_task = input("\n✏️  Enter the new task: ")
            if new_task.strip():
                todo_list.append({"task": new_task, "completed": False})
                
        elif choice == '2':
            try:
                task_num = int(input("\n✔️  Enter task number to mark as done: "))
                if 1 <= task_num <= len(todo_list):
                    todo_list[task_num - 1]['completed'] = True
                else:
                    input("Invalid number! Press Enter to try again...")
            except ValueError:
                input("Please enter a valid number! Press Enter to try again...")
                
        elif choice == '3':
            try:
                task_num = int(input("\n❌ Enter task number to delete: "))
                if 1 <= task_num <= len(todo_list):
                    removed = todo_list.pop(task_num - 1)
                    input(f"Deleted '{removed['task']}'. Press Enter to continue...")
                else:
                    input("Invalid number! Press Enter to try again...")
            except ValueError:
                input("Please enter a valid number! Press Enter to try again...")
                
        elif choice == '4':
            print("\n👋 Goodbye! Have a productive and soulful day!")
            break
            
        else:
            input("Invalid choice! Press Enter to try again...")

if __name__ == "__main__":
    main()