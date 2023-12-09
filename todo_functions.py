import csv

def add_todo(file_name):
    print("Add todo")
    # Ask the title of the todo
    todo_name = input("Enter a todo: ")
    # Open file - list.csv
    with open(file_name, "a") as f:
        writer = csv.writer(f)
        # Insert values - title = user entered
                      # - completed = False
        writer.writerow([todo_name, "False"])

def remove_todo(file_name):
    print("Remove to do")

def mark_todo(file_name):
    print("Mark to do")

def view_todo(file_name):
    print("view to do list")
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        reader.__next__()
        for row in reader: # to loop through all the rows in reader
            if (row[1] == "True"):
            # row = ["Todo 1", "False"]
                print(f"Todo {row[0]} is completed")
            else:
                print(f"Todo {row[0]} is not complete")