class TaskState:
    def performTask(self):
        pass

    def run(self):
        pass

    def finishTask(self):
        pass
    
    def cancelTask(self):
        pass

class PendingState(TaskState):
    def performTask(self):
        print("Task is already pending")
        # return PendingState()

    def run(self):
        print("Marking task as 'In Progress'")
        return InProgressState()

    def finishTask(self):
        print("Marking task as 'Completed'")
        return CompletedState()
    
    def cancelTask(self):
        pass

class InProgressState(TaskState):
    def performTask(self):
        print("Marking task as 'Pending'")
        return PendingState()

    def run(self):
        print("Task is already in progress")
        # return InProgressState()

    def finishTask(self):
        print("Marking task as 'Completed'")
        return CompletedState()
    
    def cancelTask(self):
        pass

class CompletedState(TaskState):
    def performTask(self):
        print("Cannot revert 'Completed' task back to 'Pending'")

    def run(self):
        print("Cannot modify 'Completed' task")


    def finishTask(self):
        print("Task is already completed")
        # return CompletedState()
        
    def cancelTask(self):
        pass


class Task : 
    def __init__(self, s) -> None:
        self.state = s
        
    def changeState(self, s) :
        if s != None :
            self.state = s
        
    def performTask(self):
        self.changeState(self.state.performTask())
        
    def run(self):
        self.changeState(self.state.run())
        
    def finishTask(self):
        self.changeState(self.state.finishTask())
        
if __name__ == "__main__":
    task1 = Task(PendingState())
    task1.performTask()
    task1.run()
    task1.finishTask()
    task1.performTask()
    task1.run()
    
    print()
    task2 = Task(InProgressState())
    task2.performTask()
    task2.run()
    task2.finishTask()
    task2.performTask()
    task2.run()
    
    print()
    task3 = Task(CompletedState())
    task3.performTask()
    task3.run()
    task3.finishTask()