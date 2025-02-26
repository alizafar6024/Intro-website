import sys
import json
import os
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget, QLineEdit, QLabel, QMessageBox

class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.tasks = self.load_from_file()
        self.update_task_list()

    def init_ui(self):
        self.setWindowTitle("To-Do List App")
        self.setGeometry(100, 100, 400, 400)
        
        layout = QVBoxLayout()
        
        self.task_input = QLineEdit(self)
        self.task_input.setPlaceholderText("Enter a new task")
        layout.addWidget(self.task_input)
        
        self.add_button = QPushButton("Add Task", self)
        self.add_button.clicked.connect(self.add_task)
        layout.addWidget(self.add_button)
        
        self.task_list = QListWidget(self)
        layout.addWidget(self.task_list)
        
        self.complete_button = QPushButton("Mark as Completed", self)
        self.complete_button.clicked.connect(self.mark_completed)
        layout.addWidget(self.complete_button)
        
        self.delete_button = QPushButton("Delete Task", self)
        self.delete_button.clicked.connect(self.delete_task)
        layout.addWidget(self.delete_button)
        
        self.setLayout(layout)
    
    def load_from_file(self, filename="tasks.json"):
        if not os.path.exists(filename):
            return []
        try:
            with open(filename, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def save_to_file(self, filename="tasks.json"):
        with open(filename, "w") as file:
            json.dump(self.tasks, file, indent=4)
    
    def update_task_list(self):
        self.task_list.clear()
        for task in self.tasks:
            status = "✔" if task["completed"] else "✘"
            self.task_list.addItem(f"{task['task']} [{status}]")
    
    def add_task(self):
        task_text = self.task_input.text().strip()
        if task_text:
            self.tasks.append({"task": task_text, "completed": False})
            self.save_to_file()
            self.update_task_list()
            self.task_input.clear()
        else:
            QMessageBox.warning(self, "Warning", "Task cannot be empty!")
    
    def mark_completed(self):
        selected_item = self.task_list.currentRow()
        if selected_item >= 0:
            self.tasks[selected_item]["completed"] = True
            self.save_to_file()
            self.update_task_list()
        else:
            QMessageBox.warning(self, "Warning", "No task selected!")
    
    def delete_task(self):
        selected_item = self.task_list.currentRow()
        if selected_item >= 0:
            del self.tasks[selected_item]
            self.save_to_file()
            self.update_task_list()
        else:
            QMessageBox.warning(self, "Warning", "No task selected!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec())