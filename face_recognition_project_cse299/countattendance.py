import tkinter as tk
import csv
from collections import defaultdict

class CountAttendance:
    def __init__(self, root):
        self.root = root
        root.title("Student Attendance Count")
        self.root.configure(bg="skyblue")
        self.root.geometry("400x250") 

        self.count_button = tk.Button(root, text="Count Attendance", command=self.count_attendance)
        self.count_button.pack()

        self.result_text = tk.Text(root, height=10, width=30)
        self.result_text.config(state='disabled')
        self.result_text.pack()

    def count_attendance(self):
        attendance_counts = defaultdict(int)
        file_path = r'C:\Users\Hp\Desktop\face_recognition_project_cse299\attendancehere.csv'
        with open(file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                student_name = row[4]
                attendance_counts[student_name] += 1

        #Display attendance counts
        self.result_text.config(state='normal')
        self.result_text.delete(1.0, tk.END)
        for student, count in attendance_counts.items():
            self.result_text.insert(tk.END, f"{student}: {count} attendances)\n")
        self.result_text.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    app = CountAttendance(root)
    root.mainloop()
