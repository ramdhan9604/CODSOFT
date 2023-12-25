import json 
from datetime import datetime

class ToDoListCLI:
    def __init__(self,filename='todolist_cli.json'):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename,'r') as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            pass

    def save_tasks(self):
        with open(self.filename,'w') as file:
            json.dump(self.tasks,file,indent=2)

    def show_tasks(self):
        if not self.tasks:
            print("No tasks found")
        else:
            for idx,task in enumerate(self.tasks,start=1):
                status = "Completed" if task['completed'] else "Pending"
                print(f"{idx}.{task['title']}-{task['due_date']} ({status})")
            
    def add_task(self,title,due_date):
        new_task = {'title':title,'due_date':due_date,'completed':False}
        self.tasks.append(new_task)
        self.save_tasks()
        print("Task added Successfully.")

    def edit_task(self,task_index,new_title,new_due_data):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks[task_index-1]
            task['title'] = new_title
            task['due_date'] = new_due_data
            self.save_tasks()
            print("Task updated successfully")
        else:
            print("Invalid task index")

    def mark_completed(self,task_index):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks[task_index-1]
            task['completed']=True
            self.save_tasks()
            print("Task marked as completed")
        else:
            print("Invalid task index")

    def remove_task(self,task_index):
        if 1<= task_index <= len(self.tasks):
            removed_task= self.tasks.pop(task_index-1)
            self.save_tasks()
            print(f"Task'{removed_task['title']}' removed successfully.")
        else:
            print("Invalid task index")

def cli_application():
    todo_list = ToDoListCLI()

    while True:
        print("\n ------- TO-DO-LIST Menu--------")
        print("1.Show Tasks")
        print("2. Add task")
        print("3. Update task")
        print("4. Mark Task as Completed")
        print("5. Remove Task")
        print("6. Exit")

        choice = input("Enter your choice")

        if choice =='1':
            todo_list.show_tasks()
        elif choice=='2':
            title = input("Enter task title:")
            due_date = input("Enter due date(YYYY-MM-DD):")
            todo_list.add_task(title,due_date)
        elif choice=='3':
            todo_list.show_tasks()
            task_index = int(input("Enter the task index to edit:"))
            new_title = input("Enter new task title:")
            new_due_data = input("Enter new due date(YYYY-MM-DD):")
            todo_list.edit_task(task_index,new_title,new_due_data)
        elif choice == '4':
            todo_list.show_tasks()
            task_index = int(input("Enter the task index to mark as completed:"))
            todo_list.mark_completed(task_index)
        elif choice== '5':
            todo_list.show_tasks()
            task_index = int(input("Enter the task index to want to remove:"))
            todo_list.remove_task(task_index)
        elif choice=='6' :
            print("Exiting the TO-DO-LIST application.")
            break
        else:
            print("Invalid choice please try again.") 

if __name__ =='__main__':
    cli_application()


        