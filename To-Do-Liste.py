def add_task(todo_list, task):
    todo_list.append({"task": task, "completed": False})

def remove_task(todo_list, task):
    for item in todo_list:
        if item in todo_list:
            if item["task"] == task:
                todo_list.remove(item)
                return
    print("Aufgabe nicht gefunden")

def show_tasks(todo_list):
    if not todo_list:
        print("Keine Aufgaben in der Liste")
    else:
        for item in todo_list:
            status = "Erledigt" if item["completed"] else "Nicht erledigt"

def mark_as_done(todo_list, task):
    for item in todo_list:
        if item["task"] == task:
            item["completed"] = True
            return
    print("Aufgabe nicht gefunden!")

# Hauptprogramm
todo_list = []
add_task(todo_list, "Einkaufen")
add_task(todo_list, "Hausaufgaben machen")
add_task(todo_list, "Python lernen")

show_tasks(todo_list)
remove_task(todo_list, "Hausaufgaben machen")
show_tasks(todo_list)
