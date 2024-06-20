class Note():
    def __init__(self, content: str) -> None:
        self.__content = content
        self.__tasklets = [] # list of all subdivided tasks

    @property
    def content(self):
        return self.__content
    
    @property
    def tasks(self):
        return self.__tasklets
    
    @content.setter
    def content(self, value: str):
        self.__content = value
    
    def addTasks(self, task_to_add: str):
        self.__tasklets.append(task_to_add)

