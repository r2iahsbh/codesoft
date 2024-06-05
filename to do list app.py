task = []
def addTask():
   task = input(" Please enter a task:")
   task.append(task)
   print("Task '{task}' added to list.")
    
def listTasks():
   if not task:
     print("there are no tasks currently.")
   else: 
     print("Current Tasks.")
     for Index,task in enumerate(task):
       print(f"Task #{Index}.{task} ")
    
     

   def deleteTask():
    listTasks()
    try:   
       tasktoDelete = int(input("Enter the # to delete:"))
       if tasktoDelete >=0 and tasktoDelete<len(task):
        task.pop(tasktoDelete)
        print("Task {tasktodDelete} has been removed.")
    except:
      print("Invalid input.")

if __name__ == "__main__":
### create a loop to run the app

  print("Welcome to the to do list app:")
while  True:
  print("\n")
  print("Please select one of the following options")
  print("-----------------------------------------")
  print("1. Add new task")
  print("2.Delete a task")
  print("3.List tasks")
  print("4.Quit")

  choice = input("Enter your choice:")
  if(choice == "1"):
    addTask()
  elif(choice == "2"):
    deleteTask()
  elif (choice == "3"):
    listtask
  elif (choice == "4"):
    break

else:
  print("Invalid input.please try again")


  