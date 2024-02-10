from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
class Developerss:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x420")
        self.root.title("Developers Details")

        left_frame = Frame(self.root, bg="lightgray")
        left_frame.pack(side=LEFT, padx=10, pady=10, fill="both", expand=True)

        right_frame = Frame(self.root, bg="lightblue")
        right_frame.pack(side=RIGHT, padx=10, pady=10, fill="both", expand=True)

        # Developer 1 Details
        developer1_label = Label(left_frame, text="Developer 1", font=("times new roman", 20, "bold"), bg="lightgray")
        developer1_label.pack(pady=10)

        developer1_image = Image.open(r"C:\Users\Hp\Desktop\face_recognition_project_cse299\images\tanvirpic.jpg")  
        developer1_image = developer1_image.resize((200, 200), Image.LANCZOS)
        developer1_photo = ImageTk.PhotoImage(developer1_image)

        developer1_image_label = Label(left_frame, image=developer1_photo, bg="lightgray")
        developer1_image_label.photo = developer1_photo
        developer1_image_label.pack()

        developer1_info = Label(left_frame, text="Name: Mr X\nID: 124356\nDepartment: Computer Science\nEmail: mrx12@gmail.com\nPthon Developer", font=("times new roman", 14), bg="lightgray")
        developer1_info.pack(pady=10)

        # Developer 2 Details
        developer2_label = Label(right_frame, text="Developer 2", font=("times new roman", 20, "bold"), bg="lightblue")
        developer2_label.pack(pady=10)

        developer2_image = Image.open(r"C:\Users\Hp\Desktop\face_recognition_project_cse299\images\fahminpic.jpg")  
        developer2_image = developer2_image.resize((200, 200), Image.LANCZOS)
        developer2_photo = ImageTk.PhotoImage(developer2_image)

        developer2_image_label = Label(right_frame, image=developer2_photo, bg="lightblue")
        developer2_image_label.photo = developer2_photo
        developer2_image_label.pack()

        developer2_info = Label(right_frame, text="Name: Mr Y\nID: 678905\nDepartment: Computer Science\nEmail: mry12@gmail.com\nPthon Developer", font=("times new roman", 14), bg="lightblue")
        developer2_info.pack(pady=10)

# Create the main window
root = tk.Tk()
app = Developerss(root)

# Start the main loop
root.mainloop()
