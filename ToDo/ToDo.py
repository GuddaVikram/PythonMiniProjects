# A to-do application which helps the users to add the tasks, alter the status of the task, Delete the task etc
import json
import os
from enum import Enum

class TaskStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in progress"
    COMPLETED = "completed"


class Todo():
    def __init__(self, path = "/Users/vikramg/AIML Tutorial/Mini Python Projects/ToDo/Tasks.json") -> None:
        self.path = path
        self.is_file_exists()
    
    def is_file_exists(self):
        if not os.path.exists(self.path):
            with open(self.path,"w") as file:
                json.dump({},file)
                file.close()

    def get_tasks(self):
        with open(self.path,'r') as file:
            dic = json.load(file)
            file.close()
        return dic

    def save_task(self,tasks):
        with open(self.path,'w') as file:
            json.dump(tasks,file)
            file.close()

    def get_task_by_id(self,id):
        tasks = self.get_tasks()
        
        return tasks[str(id)]

    def add_task(self,title,status: TaskStatus,description): 
        tasks = self.get_tasks()

        max_value = max(map(int, tasks.keys()), default=0)
        
        tasks[max_value+1]  = {
                    "title": title,
                    "status": status.value,
                    "description": description 
                }
        self.save_task(tasks)

    # Delete the task based on the id
    def delete_task(self,id : int):
        tasks = self.get_tasks()
        
        try:
            tasks.pop(str(id))
            self.save_task(tasks)
        except KeyError:
            print(f'No task is present with id = {id}')
        except Exception as ex:
            print(f'Error: {ex}')

    def update_task_status(self,task_id, status: TaskStatus):
        tasks = self.get_tasks()
        
        try:
            tasks[str(task_id)]["status"] = status.value
            self.save_task(tasks)
        except KeyError:
            print(f'No task is present with id = {task_id}')
        except Exception as ex:
            print(f'Error: {ex}')
        


todo = Todo()
todo.update_task_status(1,TaskStatus.IN_PROGRESS)

        
