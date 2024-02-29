class TaskState:
    def maskAsPending(self):
        pass

    def maskAsInProgress(self):
        pass

    def maskAsCompleted(self):
        pass

class PendingState(TaskState):
    def maskAsPending(self):
        print("Task is already pending")
        # return PendingState()

    def maskAsInProgress(self):
        print("Marking task as 'In Progress'")
        return InProgressState()

    def maskAsCompleted(self):
        print("Marking task as 'Completed'")
        return CompletedState()

class InProgressState(TaskState):
    def maskAsPending(self):
        print("Marking task as 'Pending'")
        return PendingState()

    def maskAsInProgress(self):
        print("Task is already in progress")
        # return InProgressState()

    def maskAsCompleted(self):
        print("Marking task as 'Completed'")
        return CompletedState()

class CompletedState(TaskState):
    def maskAsPending(self):
        print("Cannot revert 'Completed' task back to 'Pending'")
        # return CompletedState()

    def maskAsInProgress(self):
        print("Cannot modify 'Completed' task")
        # return CompletedState()

    def maskAsCompleted(self):
        print("Task is already completed")
        # return CompletedState()


class Task : 
    def __init__(self, s) -> None:
        self.state = s
        
    def changeState(self, s) :
        if s != None :
            self.state = s
        
    def maskAsPending(self):
        self.changeState(self.state.maskAsPending())
        
    def maskAsInProgress(self):
        self.changeState(self.state.maskAsInProgress())
        
    def maskAsCompleted(self):
        self.changeState(self.state.maskAsCompleted())
        
if __name__ == "__main__":
    task = Task(PendingState())
    task.maskAsPending()
    task.maskAsInProgress()
    task.maskAsCompleted()
    task.maskAsPending()
    task.maskAsInProgress()