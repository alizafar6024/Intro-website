import sys
import json
import os
import smtplib
from email.message import EmailMessage
from datetime import datetime
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget, QLineEdit, QLabel, QMessageBox, QDateEdit, QComboBox

class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.tasks = self.load_from_file()
        self.update_task_list()

    def init_ui(self):
        self.setWindowTitle("To-Do List App")
        self.setGeometry(100, 100, 500, 500)
        
        layout = QVBoxLayout()
        
        self.task_input = QLineEdit(self)
        self.task_input.setPlaceholderText("Enter a new task")
        layout.addWidget(self.task_input)
        
        self.due_date = QDateEdit(self)
        self.due_date.setCalendarPopup(True)
        self.due_date.setDate(datetime.today().date())
        layout.addWidget(self.due_date)
        
        self.reminder_type = QComboBox(self)
        self.reminder_type.addItems(["None", "Email", "Telegram", "Both"])
        layout.addWidget(self.reminder_type)
        
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
                tasks = json.load(file)
            # Ensure every task has a due_date field
                for task in tasks:
                    if "due_date" not in task:
                        task["due_date"] = "No Due Date"
                return tasks
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    
    def save_to_file(self, filename="tasks.json"):
        with open(filename, "w") as file:
            json.dump(self.tasks, file, indent=4)
    
    def update_task_list(self):
        self.task_list.clear()
        for task in self.tasks:
            status = "✔" if task["completed"] else "✘"
            self.task_list.addItem(f"{task['task']} - Due: {task['due_date']} [{status}]")
    
    def add_task(self):
        task_text = self.task_input.text().strip()
        due_date = self.due_date.date().toString("yyyy-MM-dd")
        reminder_type = self.reminder_type.currentText()
        
        if task_text:
            self.tasks.append({"task": task_text, "completed": False, "due_date": due_date, "reminder": reminder_type})
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
    
    def send_email_reminder(self, recipient_email, subject, body):
        sender_email = "your_email@gmail.com"
        app_password = "your_app_password"
        
        msg = EmailMessage()
        msg.set_content(body)
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = recipient_email
        
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(sender_email, app_password)
                server.send_message(msg)
            print("Email reminder sent successfully!")
        except Exception as e:
            print("Failed to send email reminder:", e)
    
    def check_and_send_reminders(self):
        today = datetime.today().strftime("%Y-%m-%d")
        for task in self.tasks:
            if not task["completed"] and task["due_date"] == today:
                if task["reminder"] in ["Email", "Both"]:
                    self.send_email_reminder("recipient@gmail.com", "Task Reminder", f"Reminder: {task['task']} is due today!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec())
