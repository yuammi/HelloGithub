class TodoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)
        print(f"添加任务: {task}")
    
    def view_tasks(self):
        if self.tasks:
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")
        else:
            print("暂无待办事项")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"删除任务: {task}")
        else:
            print(f"任务 '{task}' 不存在")

    def mark_task_completed(self, task):
        if task in self.tasks:
            index = self.tasks.index(task)
            self.tasks[index] = f"{task} (已完成)"
            print(f"标记任务为已完成: {task}")
        else:
            print(f"任务 '{task}' 不存在")

if __name__ == "__main__":
    todo_list = TodoList()
    
    while True:
        print("\n1. 添加任务")
        print("2. 查看任务")
        print("3. 删除任务")
        print("4. 标记任务为已完成")
        print("5. 退出")
        
        choice = input("选择一个操作: ")
        
        if choice == '1':
            task = input("输入任务: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task = input("输入要删除的任务: ")
            todo_list.remove_task(task)
        elif choice == '4':
            task = input("输入要标记为已完成的任务: ")
            todo_list.mark_task_completed(task)
        elif choice == '5':
            break
        else:
            print("无效的选择，请重试。")
