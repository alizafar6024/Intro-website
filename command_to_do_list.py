tasks = []
# load task from a file

def load_from_file(filename="tasks.json"):
    if not os.path.exists(filename):
        with open(filename, "w") as file:
            json.dump([], file)
            return []
    try:
        with open(filename, "r") as file:
            data = file.read().strip()
            return json.loads(data) if data else []
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Add task
def add_task(task_list, task):
    task_list.append({"task": task, "completed": False})
    save_to_file(task_list)
    print(f'task "{task}" added successfully!')

# View task
def view_tasks(task_list):
    if not task_list:
        print("no task available")
    else:
        for index, task in enumerate(task_list, start=1):
            status = "✔" if task["completed"] else "x"
            print(f"{index}. {task['task']} [{status}]")

# Mark a task as complete

def mark_completed(task_list, task_index):
    if 0 <= task_index < len(task_list):
        task_list[task_index]["completed"]= True
        save_to_file(task_list)
        print(f'task "{task_list[task_index]["task"]}" marked as completed!')
    else:
        print("invalid task number.")
    
# Delete a task

def delete_task(task_list, task_index):
    if 0 <= task_index < len(task_list):
        removed_task = task_list.pop(task_index)
        save_to_file(task_list)
        print(f'task "{removed_task["task"]}" deleted!')
    else:
        print("invalid task number.")

# Save tasks to a file

import json
import os

def save_to_file(task_list, filename="tasks.json"):
    try:
        with open(filename, "w") as file:
            json.dump(task_list, file, indent=4)
            print("Task successfully saved to file!")
    except Exception as e:
        print(f"Error saving tasks: {e}")

    
#  User interaction (CLI menu)

def main():
    tasks = load_from_file()

    while True:
        print("\nTo-Do List App")
        print("1. Add task")
        print("2. View tasks")
        print("3. mark task as completed")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(tasks, task)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            view_tasks(tasks)
            try:
                task_index = int(input("Enter task number to mark as completed: ")) -1
                delete_task(tasks, task_index)
            except ValueError:
                print("Invalid input.")
        elif choice == "5":
            save_to_file(tasks)
            print("Tasks saved. Exiting...")
        else:
            print("Invalid choice. Try again...")
        
if __name__ == "__main__":
    main(  )