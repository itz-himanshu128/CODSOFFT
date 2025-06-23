import json
import os
from datetime import datetime

class TodoList:
    def __init__(self):
        self.tasks = []
        self.filename = "tasks.json"
        self.load_tasks()
    
    def load_tasks(self):
        """Load tasks from file if it exists"""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as file:
                    self.tasks = json.load(file)
        except:
            self.tasks = []
    
    def save_tasks(self):
        """Save tasks to file"""
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.tasks, file, indent=2)
        except:
            print("Error saving tasks!")
    
    def add_task(self):
        """Add a new task"""
        task_name = input("Enter task description: ").strip()
        if task_name:
            task = {
                'id': len(self.tasks) + 1,
                'description': task_name,
                'completed': False,
                'created_date': datetime.now().strftime("%Y-%m-%d %H:%M")
            }
            self.tasks.append(task)
            self.save_tasks()
            print(f"✓ Task '{task_name}' added successfully!")
        else:
            print("Task description cannot be empty!")
    
    def view_tasks(self):
        """Display all tasks"""
        if not self.tasks:
            print("No tasks found! Your to-do list is empty.")
            return
        
        print("\n" + "="*50)
        print("YOUR TO-DO LIST")
        print("="*50)
        
        pending_tasks = [task for task in self.tasks if not task['completed']]
        completed_tasks = [task for task in self.tasks if task['completed']]
        
        if pending_tasks:
            print("\n📋 PENDING TASKS:")
            for task in pending_tasks:
                print(f"  {task['id']}. [ ] {task['description']}")
                print(f"      Created: {task['created_date']}")
        
        if completed_tasks:
            print("\n✅ COMPLETED TASKS:")
            for task in completed_tasks:
                print(f"  {task['id']}. [✓] {task['description']}")
                print(f"      Created: {task['created_date']}")
        
        print(f"\nTotal Tasks: {len(self.tasks)} | Pending: {len(pending_tasks)} | Completed: {len(completed_tasks)}")
    
    def mark_completed(self):
        """Mark a task as completed"""
        if not self.tasks:
            print("No tasks to mark as completed!")
            return
        
        self.view_tasks()
        try:
            task_id = int(input("\nEnter task ID to mark as completed: "))
            task_found = False
            
            for task in self.tasks:
                if task['id'] == task_id:
                    if task['completed']:
                        print("Task is already completed!")
                    else:
                        task['completed'] = True
                        task['completed_date'] = datetime.now().strftime("%Y-%m-%d %H:%M")
                        self.save_tasks()
                        print(f"✓ Task '{task['description']}' marked as completed!")
                    task_found = True
                    break
            
            if not task_found:
                print("Task ID not found!")
        
        except ValueError:
            print("Please enter a valid task ID number!")
    
    def update_task(self):
        """Update a task description"""
        if not self.tasks:
            print("No tasks to update!")
            return
        
        self.view_tasks()
        try:
            task_id = int(input("\nEnter task ID to update: "))
            task_found = False
            
            for task in self.tasks:
                if task['id'] == task_id:
                    old_description = task['description']
                    new_description = input(f"Enter new description (current: '{old_description}'): ").strip()
                    
                    if new_description:
                        task['description'] = new_description
                        task['updated_date'] = datetime.now().strftime("%Y-%m-%d %H:%M")
                        self.save_tasks()
                        print(f"✓ Task updated successfully!")
                    else:
                        print("Task description cannot be empty!")
                    task_found = True
                    break
            
            if not task_found:
                print("Task ID not found!")
        
        except ValueError:
            print("Please enter a valid task ID number!")
    
    def delete_task(self):
        """Delete a task"""
        if not self.tasks:
            print("No tasks to delete!")
            return
        
        self.view_tasks()
        try:
            task_id = int(input("\nEnter task ID to delete: "))
            task_found = False
            
            for i, task in enumerate(self.tasks):
                if task['id'] == task_id:
                    confirm = input(f"Are you sure you want to delete '{task['description']}'? (y/n): ")
                    if confirm.lower() == 'y':
                        deleted_task = self.tasks.pop(i)
                        # Reassign IDs to maintain order
                        for j, remaining_task in enumerate(self.tasks):
                            remaining_task['id'] = j + 1
                        self.save_tasks()
                        print(f"✓ Task '{deleted_task['description']}' deleted successfully!")
                    else:
                        print("Task deletion cancelled.")
                    task_found = True
                    break
            
            if not task_found:
                print("Task ID not found!")
        
        except ValueError:
            print("Please enter a valid task ID number!")
    
    def clear_completed(self):
        """Remove all completed tasks"""
        completed_tasks = [task for task in self.tasks if task['completed']]
        
        if not completed_tasks:
            print("No completed tasks to clear!")
            return
        
        confirm = input(f"Are you sure you want to delete all {len(completed_tasks)} completed tasks? (y/n): ")
        if confirm.lower() == 'y':
            self.tasks = [task for task in self.tasks if not task['completed']]
            # Reassign IDs
            for i, task in enumerate(self.tasks):
                task['id'] = i + 1
            self.save_tasks()
            print(f"✓ {len(completed_tasks)} completed tasks cleared!")
        else:
            print("Operation cancelled.")
    
    def show_statistics(self):
        """Show task statistics"""
        if not self.tasks:
            print("No tasks to show statistics for!")
            return
        
        total = len(self.tasks)
        completed = len([task for task in self.tasks if task['completed']])
        pending = total - completed
        completion_rate = (completed / total) * 100 if total > 0 else 0
        
        print("\n" + "="*30)
        print("TASK STATISTICS")
        print("="*30)
        print(f"Total Tasks: {total}")
        print(f"Completed: {completed}")
        print(f"Pending: {pending}")
        print(f"Completion Rate: {completion_rate:.1f}%")
        
        if self.tasks:
            oldest_task = min(self.tasks, key=lambda x: x['created_date'])
            print(f"Oldest Task: {oldest_task['description']}")

def show_menu():
    """Display the main menu"""
    print("\n" + "="*40)
    print("TO-DO LIST APPLICATION")
    print("="*40)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Update Task")
    print("5. Delete Task")
    print("6. Clear Completed Tasks")
    print("7. Show Statistics")
    print("8. Exit")
    print("-"*40)

def main():
    """Main function to run the application"""
    todo = TodoList()
    
    print("Welcome to Your To-Do List Manager!")
    
    while True:
        show_menu()
        choice = input("Choose an option (1-8): ").strip()
        
        if choice == '1':
            todo.add_task()
        elif choice == '2':
            todo.view_tasks()
        elif choice == '3':
            todo.mark_completed()
        elif choice == '4':
            todo.update_task()
        elif choice == '5':
            todo.delete_task()
        elif choice == '6':
            todo.clear_completed()
        elif choice == '7':
            todo.show_statistics()
        elif choice == '8':
            print("Thank you for using To-Do List Manager! Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1-8.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()