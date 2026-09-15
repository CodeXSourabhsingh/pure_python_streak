import heapq
import datetime
class Task:
    def __init__(self,name,priority,deadline):
        self.name = name
        self.priority = priority
        self.deadline = deadline

    def __str__ (self):
        return f"Task {self.name} | priority {self.priority} | deadline {self.deadline}"  
    
class TaskScheduler :
    def __init__(self):
        self.heap = []
        self.counter = 0
    def add_task(self, task):
        heapq.heappush(self.heap, (task.priority, self.counter, task))
        self.counter += 1

    def execute_task(self):
        try:
            priority ,counter, task = heapq.heappop(self.heap)
            return task
        except IndexError:
            print('NO Task to execute')
            return
    def veiw_task (self):
        if not self.heap:
            print("no task.")
            return
        for priority, counter,task in sorted(self.heap):
            print(task)
            
class TaskLogger:
    def __init__(self,filepath):
        self.filepath = filepath

    def log(self, task):
        with open(self.filepath, 'a') as f:
            f.write(f"{datetime.datetime.now()} {task}\n")

if __name__ == "__main__":
    scheduler = TaskScheduler()
    logger = TaskLogger('task_log.Txt')
    while True:
        print("1. Add Task")
        print("2. Exeute Task")
        print('3. Veiw Task')
        print('4. Exit')


        try:
          choice = int(input('Enter choice: '))
        except ValueError:
            print('invalid input. Enter number')
            continue

        if choice == 1:
            name = input("Task name: ")
            priority = int(input("Priority (1=highest): "))
            deadline = input("Deadline: ")
            task = Task(name, priority, deadline)
            scheduler.add_task(task)
            print(f"Added: {task}")
        elif choice == 2:
            task = scheduler.execute_task()
            if task:
                logger.log(task)
                print(f"Executed: {task}")
        elif choice == 3:
            scheduler.veiw_task()
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
    







        

