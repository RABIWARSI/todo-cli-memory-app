class TodoApp:
    def __init__(self):
        self.todos = []

    def add_task(self, title, desc):
        self.todos.append({"title": title, "desc": desc, "done": False})
        print(f"Added: {title}")

    def view_tasks(self):
        if not self.todos:
            print("\nNo tasks in list.")
            return
        print("\n--- Current Tasks ---")
        for i, t in enumerate(self.todos):
            status = "✅" if t['done'] else "❌"
            print(f"{i+1}. {t['title']} - {t['desc']} [{status}]")

    def update_task(self, idx, title):
        if 0 <= idx < len(self.todos):
            self.todos[idx]['title'] = title
            print("Updated!")

    def delete_task(self, idx):
        if 0 <= idx < len(self.todos):
            removed = self.todos.pop(idx)
            print(f"Deleted: {removed['title']}")

    def mark_complete(self, idx):
        if 0 <= idx < len(self.todos):
            self.todos[idx]['done'] = True
            print("Marked as complete!")

def main():
    app = TodoApp()
    while True:
        print("\nOptions: 1.Add 2.View 3.Update 4.Delete 5.Complete 6.Exit")
        choice = input("Select an option: ")
        try:
            if choice == '1':
                app.add_task(input("Title: "), input("Desc: "))
            elif choice == '2':
                app.view_tasks()
            elif choice == '3':
                app.update_task(int(input("Task Number: "))-1, input("New Title: "))
            elif choice == '4':
                app.delete_task(int(input("Task Number: "))-1)
            elif choice == '5':
                app.mark_complete(int(input("Task Number: "))-1)
            elif choice == '6':
                print("Goodbye!")
                break
        except Exception as e:
            print(f"Error: Invalid input. Please try again.")

if __name__ == "__main__":
    main()
