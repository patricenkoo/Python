# simple search of a word in a list

def main():
    class TodoItem:
        def __init__(self, title, description, completed=False):
            self.title = self.setTitle(title)
            self.description = self.setDescription(description)
            self.completed = self.setCompleted(completed)

            def getTitle(self):
                print("title accessed")
                return self.title

            def getDescription(self):
                print("description accessed")
                return self.description

            def getCompleted(self):
                print("completed accessed")
                return self.completed
            
            def setTitle(self, title):
                print("title changed")
                if type(title) == str:
                    self.title = title
                    return self.title
                else:
                    self.title = None
                    print("invalid value")
            
            def setDescription(self, description):
                print("description changed")
                if type(description) == str:
                    self.description = description
                    return self.description
                else:
                    self.description = None
                    print("invalid value")

            def setCompleted(self, completed):
                print("completed change")
                if type(completed) == bool:
                    self.completed = completed
                    return self.completed
                else:
                    self.completed = None
                    print("invalid value")
    
    newTodoItem = TodoItem("Playe","actor of the theater")
    print(newTodoItem.setTitle())
    print(newTodoItem.setDescription())
    print(newTodoItem.getDescription())
    print(newTodoItem.getTitle())
    print(newTodoItem.setCompleted())


if __name__ == "__main__":
    main()

