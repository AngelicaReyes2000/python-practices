import sys

file_name = "todo_data.txt"
todos = []

#Read File
try:
    file = open(file_name, "r")
    todos = file.readlines()
    file.close()
except:
    pass

print(todos)

#Add todo
if len(sys.argv) >= 3 and sys.argv[1].lower() == "add":
    todos.append(f"{sys.argv[2]}\n")

#Remove Todo
if len(sys.argv) >= 3 and sys.argv[1].lower() == "remove":
    try:
        index_to_delete = int(sys.argv[2])
        if index_to_delete > 0:
            index_to_delete -= 1
            del(todos[index_to_delete])
        else:
            print("Wrong number!")
    except Exception as e:
        print(e)
        sys.exit(1)


print(todos)

#Save File
file = open(file_name, "w")
file.writelines(todos)
file.close()

#Print list
if len(todos) == 0:
    print("You have no todos :)")
else:
    print("\nHere's your to do list:\n")
    for x in range(len(todos)):
        print(f"{x + 1}. {todos[x]}", end ="")


# Print commands
print("\n********************************\n")
print(f"To view ToDos:\n{sys.argv[0]}")
print(f"To view ToDo:\n{sys.argv[0]} add \"Clean Room\"\n")
print(f"To remove or complete ToDo:\n{sys.argv[0]} remove 2\n")
