from tkinter import *
from tkinter import messagebox
import os
from viewnotes import ViewNotes

class ClassNotes:
    def __init__(self, root):
        self.root = root
        self.root.geometry("920x600")
        self.root.title("Class Notes")
        self.root.configure(bg="skyblue")

        self.notes_text = Text(self.root, wrap=WORD, width=95, height=30, bg="white", fg="black")
        self.notes_text.pack(pady=10)
        self.notes_text.insert(END, "Write your class notes here...")

        save_button = Button(self.root, text="Save Notes", command=self.save_notes, bg="green", fg="white")
        save_button.pack()
        
        view_button = Button(self.root, text="View Notes", command=self.view_notes, bg="green", fg="white")
        view_button.pack()

    def save_notes(self):
        notes = self.notes_text.get("1.0", "end-1c") 
        if notes.strip():
            with open("class_notes.txt", "a") as f:
                f.write(notes + "\n")
            messagebox.showinfo("Success", "Class notes saved successfully!")
        else:
            messagebox.showerror("Error", "Please write some notes before saving.")

    def view_notes(self):
        self.new_window=Toplevel(self.root) 
        self.app=ViewNotes(self.new_window)

if __name__ == "__main__":
    root = Tk()
    obj = ClassNotes(root)
    root.mainloop()
