from tkinter import *
from tkinter import messagebox
import os

class ViewNotes:
    def __init__(self, root):
        self.root = root
        self.root.geometry("870x615")  
        self.root.title("View Notes")
        self.root.configure(bg="pink")

        title_lbl=Label(root,text="Your Notes", font=("Montserrat", 14, "bold"), bg="black", fg="white") 
        title_lbl.place(x=52,y=38,width=761,height=30)

        self.notes_text = Text(self.root, wrap=WORD, width=95, height=30, bg="white")
        self.notes_text.place(x=50, y=80)  
        self.load_notes()  

    def load_notes(self):
        file_path = r"C:\Users\Hp\Desktop\face_recognition_project_cse299\class_notes.txt"
        if os.path.isfile(file_path):
            with open(file_path, "r") as f:
                notes_content = f.read()
                self.notes_text.delete(1.0, END)
                self.insert_with_spacing(notes_content)
        else:
            messagebox.showerror("Error", "Class notes file not found!")

    def insert_with_spacing(self, content):
        lines = content.split('\n')
        for line in lines:
            self.notes_text.insert(END, line + '\n')
            self.notes_text.tag_add("yellow_border", f"{self.notes_text.index('end -2c')} linestart", f"{self.notes_text.index('end -2c')} lineend")

            self.notes_text.insert(END, '\n')

        self.notes_text.tag_configure("yellow_border", background="yellow", foreground="black", spacing1=5, spacing2=5)
        
if __name__ == "__main__":
    root = Tk()
    obj = ViewNotes(root)
    root.mainloop()
