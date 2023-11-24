import tkinter as tk
from tkinter import scrolledtext

class HelpChatbot:
    def __init__(self, root):
        self.root = root
        self.root.title("Help Chatbot")
        self.root.configure(bg="light sky blue")
        self.root.geometry("890x615") 

        self.chat_history = []

        self.text_widget = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=100, height=30)  
        self.text_widget.grid(row=0, column=0, padx=35, pady=10, columnspan=2)

        self.user_entry = tk.Entry(root, width=100)  
        self.user_entry.grid(row=1, column=0, padx=10, pady=10)
        self.user_entry.bind('<Return>', self.process_input)

        self.send_button = tk.Button(root, text="Send Question",width=19, command=self.process_input)
        self.send_button.grid(row=1, column=1, padx=10, pady=10)

        self.add_student_button = tk.Button(root, text="How to Add Students", command=self.add_students_help)
        self.add_student_button.grid(row=2, column=0, padx=10, pady=10)

        self.take_attendance_button = tk.Button(root, text="How to Take Attendance", command=self.take_attendance_help)
        self.take_attendance_button.grid(row=2, column=1, padx=10, pady=10)

    def process_input(self, event=None):
        user_input = self.user_entry.get()
        self.user_entry.delete(0, tk.END)
        self.chat_history.append(f"You: {user_input}")
        response = self.generate_response(user_input)
        self.chat_history.append(f"Chatbot: {response}")
        self.update_chat_history()

    def generate_response(self, user_input):
        if "add students" in user_input.lower():
            return "To add students, go to the 'Add Student' section from the front page and follow the instructions."
        elif "take attendance" in user_input.lower():
            return "To take attendance, go to the 'Face Detect Attendance' section from the front page and click the 'Face Detect' button to take attendance."
        elif "help" in user_input.lower():
            return "To add students, go to the 'Add Student' section from the front page and follow the instructions.\nTo take attendance, go to the 'Face Detect Attendance' section from the front page and click the 'Face Detect' button to take attendance."
        elif "how to add students" in user_input.lower():
            return "To add students, go to the 'Add Student' section from the front page and follow the instructions."
        elif "how to take attendance" in user_input.lower():
            return "To take attendance, go to the 'Face Detect Attendance' section from the front page and click the 'Face Detect' button to take attendance."
        elif "hi" in user_input.lower():
            return "How can I help you?"
        else:
            return "Sorry, I couldn't understand your question. Please ask about adding students or taking attendance."

    def update_chat_history(self):
        self.text_widget.config(state=tk.NORMAL)
        self.text_widget.delete(1.0, tk.END)
        for item in self.chat_history:
            self.text_widget.insert(tk.END, item + "\n")
        self.text_widget.config(state=tk.DISABLED)

    def add_students_help(self):
        response = "To add students, go to the 'Add Student' section from the front page and follow the instructions."
        self.chat_history.append(f"Chatbot: {response}")
        self.update_chat_history()

    def take_attendance_help(self):
        response = "To take attendance, go to the 'Face Detect Attendance' section from the front page and click the 'Face Detect' button to take attendance."
        self.chat_history.append(f"Chatbot: {response}")
        self.update_chat_history()

if __name__ == "__main__":
    root = tk.Tk()
    chatbot = HelpChatbot(root)
    root.mainloop()
