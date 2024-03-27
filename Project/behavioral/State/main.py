class TaskState:
    def performPending(self):
        pass

    def startInProgress(self):
        pass

    def finishTask(self):
        pass

class PendingState(TaskState):
    def performPending(self):
        print("Task is already pending")
        # return PendingState()

    def startInProgress(self):
        print("Marking task as 'In Progress'")
        return InProgressState()

    def finishTask(self):
        print("Marking task as 'Completed'")
        return CompletedState()

class InProgressState(TaskState):
    def performPending(self):
        print("Marking task as 'Pending'")
        return PendingState()

    def startInProgress(self):
        print("Task is already in progress")
        # return InProgressState()

    def finishTask(self):
        print("Marking task as 'Completed'")
        return CompletedState()

class CompletedState(TaskState):
    def performPending(self):
        print("Cannot revert 'Completed' task back to 'Pending'")
        # return CompletedState()

    def startInProgress(self):
        print("Cannot modify 'Completed' task")
        # return CompletedState()

    def finishTask(self):
        print("Task is already completed")
        # return CompletedState()


class Task : 
    def __init__(self, s) -> None:
        self.state = s
        
    def changeState(self, s) :
        if s != None :
            self.state = s
        
    def performPending(self):
        self.changeState(self.state.performPending())
        
    def startInProgress(self):
        self.changeState(self.state.startInProgress())
        
    def finishTask(self):
        self.changeState(self.state.finishTask())
        
if __name__ == "__main__":
    task1 = Task(PendingState())
    task1.performPending()
    task1.startInProgress()
    task1.finishTask()
    task1.performPending()
    task1.startInProgress()
    
    print()
    task2 = Task(InProgressState())
    task2.performPending()
    task2.startInProgress()
    task2.finishTask()
    task2.performPending()
    task2.startInProgress()
    
    print()
    task3 = Task(CompletedState())
    task3.performPending()
    task3.startInProgress()
    task3.finishTask()