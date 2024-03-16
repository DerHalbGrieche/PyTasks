import argparse
from src.task import Task
import os
import json

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.__load_tasks()

    def __load_tasks(self):
        if os.path.exists('tasks.json'):
            with open('tasks.json', 'r') as file:
                tasks = json.load(file)
                self.tasks = [Task(task['name'], task['completed']) for task in tasks]

    def __save_tasks(self):
        with open('tasks.json', 'w') as file:
            tasks = [{'name': task.name, 'completed': task.completed} for task in self.tasks]
            json.dump(tasks, file)

    def add_task(self, name):
        task = Task(name)
        self.tasks.append(task)
        self.__save_tasks()
    
    def remove_task(self, name):
        for task in self.tasks:
            if task.name == name:
                self.tasks.remove(task)
                self.__save_tasks()

    def complete_task(self, name):
        for task in self.tasks:
            if task.name == name:
                task.complete()
                self.__save_tasks()

    def list_tasks(self):
        return [task.name for task in self.tasks]

    def list_completed_tasks(self):
        return [task.name for task in self.tasks if task.completed]

    def list_incomplete_tasks(self):
        return [task.name for task in self.tasks if not task.completed]
    
def main():
    parser = argparse.ArgumentParser(description='Task Manager')
    parser.add_argument('command', choices=['add', 'remove', 'complete', 'list', 'list_completed', 'list_incomplete'])
    parser.add_argument('task', nargs='?')
    args = parser.parse_args()

    task_manager = TaskManager()
    if args.command == 'add':
        task_manager.add_task(args.task)
    elif args.command == 'remove':
        task_manager.remove_task(args.task)
    elif args.command == 'complete':
        task_manager.complete_task(args.task)
    elif args.command == 'list':
        print(task_manager.list_tasks())
    elif args.command == 'list_completed':
        print(task_manager.list_completed_tasks())
    elif args.command == 'list_incomplete':
        print(task_manager.list_incomplete_tasks())

if __name__ == '__main__':
    main()