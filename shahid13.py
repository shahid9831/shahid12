class StreamlineApp:
    def __init__(self):
        self.tasks = []

    def run(self):
        print("Welcome to Streamline!")
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.complete_task()
            elif choice == "3":
                self.view_tasks()
            elif choice == "4":
                print("Thank you for using Streamline!")
                break
            else:
                print("Invalid choice. Please try again.")

    def display_menu(self):
        print("\n1. Add a task")
        print("2. Complete a task")
        print("3. View tasks")
        print("4. Exit")

    def add_task(self):
        task_name = input("Enter task name: ")
        self.tasks.append(task_name)
        print("Task added successfully!")

    def complete_task(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks):
                print(f"{i + 1}. {task}")
            task_index = int(input("Enter the task number to complete: ")) - 1
            if 0 <= task_index < len(self.tasks):
                completed_task = self.tasks.pop(task_index)
                print(f"Task '{completed_task}' marked as completed!")
            else:
                print("Invalid task number.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks):
                print(f"{i + 1}. {task}")


# Entry point of the app
if __name__ == "__main__":
    app = StreamlineApp()
    app.run()
