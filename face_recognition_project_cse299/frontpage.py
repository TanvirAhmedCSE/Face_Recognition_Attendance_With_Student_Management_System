from tkinter import*
import tkinter as tk
from tkinter import Button
from PIL import Image, ImageTk
from addstudent import AddStudent
import os
from train import Train
from face_recognition import Face_Recognition
from developers import Developerss
from classnotes import ClassNotes
from countattendance import CountAttendance
from studyfiles import Lectures
from helpchatbot import HelpChatbot
import tkinter
from datetime import datetime
import webbrowser
    
class FrontPage:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition Attendance System")

        # Load animated GIF and extract frames
        self.animated_gif = Image.open(r"C:\Users\Hp\Desktop\face_recognition_project_cse299\images\tech.gif")
        self.frames = [ImageTk.PhotoImage(frame.resize((1920, 1080))) for frame in self.get_frames(self.animated_gif)]

        # Create canvas to display the frames
        self.canvas = tk.Canvas(self.root, width=1920, height=1080)
        self.canvas.pack()

        # Start animation loop
        self.animate(0)



        #1 Load the student button image
        img1 = Image.open(r"C:\Users\Hp\Desktop\face_recognition_project_cse299\images\students.png")
        img1 = img1.resize((220, 220), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        # Create the student button
        b1 = Button(self.root, image=self.photoimg1, cursor="hand2",command=self.add_student)
        b1.place(x=100, y=100, width=220, height=220)

        b1_1 = Button(self.root, text="Add Student", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white", command=self.add_student)
        b1_1.place(x=100, y=300, width=220, height=40)
        
        
        #2 Load the face detector button image
        img2 = Image.open(r"C:\Users\Hp\Desktop\face_recognition_project_cse299\images\face_detect.jpg")
        img2 = img2.resize((220, 220), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        # Create the face detector button
        b1 = Button(self.root, image=self.photoimg2, cursor="hand2", command=self.face_data)
        b1.place(x=380, y=100, width=220, height=220)

        b1_1 = Button(self.root, text="Face Detect Attendance", cursor="hand2",command=self.face_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=380, y=300, width=220, height=40)

        #3 Create View Attendance button
        img3 = Image.open(r"C:\Users\Hp\Desktop\face_recognition_project_cse299\images\view_attendances.jpg")
        img3 = img3.resize((220, 220), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b1 = Button(self.root, image=self.photoimg3, cursor="hand2",command=self.view_attendance)
        b1.place(x=660, y=100, width=220, height=220)

        b1_1 = Button(self.root, text="View Attendance", cursor="hand2", command=self.view_attendance, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=660, y=300, width=220, height=40)


        #4 Load the Count Attendance button image
        img4 = Image.open(r"C:\Users\Hp\Desktop\face_recognition_project_cse299\images\counts.png")
        img4 = img4.resize((220, 220), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        # Create the Count Attendance button
        b1 = Button(self.root, image=self.photoimg4, cursor="hand2", command=self.count_atten)
        b1.place(x=940, y=100, width=220, height=220)

        b1_1 = Button(self.root, text="Count Attendances", cursor="hand2",command=self.count_atten, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=940, y=300, width=220, height=40)


        #5 Load the Study Lectures button image
        img45 = Image.open(r"C:\Users\Hp\Desktop\face_recognition_project_cse299\images\study.png")
        img45 = img45.resize((220, 220), Image.LANCZOS)
        self.photoimg45 = ImageTk.PhotoImage(img45)

        # Create the Study Lectures button
        b1 = Button(self.root, image=self.photoimg45, cursor="hand2", command=self.study_files)
        b1.place(x=1220, y=100, width=220, height=220)

        b1_1 = Button(self.root, text="Study Lectures", cursor="hand2", command=self.study_files, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=1220, y=300, width=220, height=40)




        #6 Load the train data button image
        img5 = Image.open(r"C:\Users\Hp\Desktop\face_recognition_project_cse299\images\train.png")
        img5 = img5.resize((220, 220), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        # Create the train data button
        b1 = Button(self.root, image=self.photoimg5, cursor="hand2", command=self.train_data)
        b1.place(x=100, y=420, width=220, height=220)

        b1_1 = Button(self.root, text="Train Data", command=self.train_data, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=100, y=620, width=220, height=40)


        #7 Load the photos image
        img6 = Image.open(r"C:\Users\Hp\Desktop\face_recognition_project_cse299\images\photos.png")
        img6 = img6.resize((220, 220), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        # Create the photos button
        b1 = Button(self.root, image=self.photoimg6, cursor="hand2",command=self.open_img)
        b1.place(x=380, y=420, width=220, height=220)

        b1_1 = Button(self.root, text="Students Photos", cursor="hand2",command=self.open_img, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=380, y=620, width=220, height=40)



        #8 Load the classnotes image
        img7 = Image.open(r"C:\Users\Hp\Desktop\face_recognition_project_cse299\images\classnotespic.jpeg")
        img7 = img7.resize((220, 220), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        # Create the classnotes button
        b1 = Button(self.root, image=self.photoimg7, cursor="hand2",command=self.class_notes)
        b1.place(x=660, y=420, width=220, height=220)

        b1_1 = Button(self.root, text="Write Class Notes", cursor="hand2",command=self.class_notes, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=660, y=620, width=220, height=40)

        #9 Create the Developer button
        img8 = Image.open(r"C:\Users\Hp\Desktop\face_recognition_project_cse299\images\developer.png")
        img8 = img8.resize((220, 220), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(self.root, image=self.photoimg8, cursor="hand2", command=self.developers_details)
        b1.place(x=940, y=420, width=220, height=220)

        b1_1 = Button(self.root, text="Developers", cursor="hand2",command=self.developers_details, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=940, y=620, width=220, height=40)


        #10 Create the Help Chatbot button
        img9 = Image.open(r"C:\Users\Hp\Desktop\face_recognition_project_cse299\images\help.png")
        img9 = img9.resize((220, 220), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(self.root, image=self.photoimg9, cursor="hand2", command=self.help_chatbot)
        b1.place(x=1220, y=420, width=220, height=220)

        b1_1 = Button(self.root, text="Help Chatbot", cursor="hand2", command=self.help_chatbot, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=1220, y=620, width=220, height=40)


        # Create Exit button
        b1_1 = Button(self.root, text="Exit", cursor="hand2",command=self.exit_btn, font=("times new roman", 15, "bold"), bg="red", fg="white")
        b1_1.place(x=20, y=20, width=100, height=30)

        # Create a label to display the time
        self.time_label = tk.Label(self.root, text="", font=("times new roman", 15, "bold"), bg="green", fg="white")
        self.time_label.place(x=660, y=15, width=200, height=30)

        # Create a label to display the date
        self.date_label = tk.Label(self.root, text="", font=("times new roman", 15, "bold"), bg="green", fg="white")
        self.date_label.place(x=660, y=40, width=200, height=30)

        # Update the time and date labels
        self.update_clock()
        

        # Google Icon Button
        img10 = Image.open(r"C:\Users\Hp\Desktop\face_recognition_project_cse299\images\google.png")
        img10 = img10.resize((35, 35), Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        b1 = Button(self.root, image=self.photoimg10, cursor="hand2", command=self.open_google)
        b1.place(x=700, y=700, width=35, height=35)

        # YouTube Icon Button
        img11 = Image.open(r"C:\Users\Hp\Desktop\face_recognition_project_cse299\images\youtube.png")
        img11 = img11.resize((35, 35), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)
        b2 = Button(self.root, image=self.photoimg11, cursor="hand2", command=self.open_youtube)
        b2.place(x=760, y=700, width=35, height=35)

        # Gmail Icon Button
        img12 = Image.open(r"C:\Users\Hp\Desktop\face_recognition_project_cse299\images\gmail.png")
        img12 = img12.resize((35, 35), Image.LANCZOS)
        self.photoimg12 = ImageTk.PhotoImage(img12)
        b2 = Button(self.root, image=self.photoimg12, cursor="hand2", command=self.open_gmail)
        b2.place(x=820, y=700, width=35, height=35)


    def open_img(self):
        os.startfile("data")

    def add_student(self):
        self.new_window=Toplevel(self.root) 
        self.app=AddStudent(self.new_window)  

    def train_data(self):
        self.new_window=Toplevel(self.root) 
        self.app=Train(self.new_window)  

    def developers_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Developerss(self.new_window)  

    def face_data(self):
        self.new_window=Toplevel(self.root) 
        self.app=Face_Recognition(self.new_window)   
    
    def class_notes(self):
        self.new_window=Toplevel(self.root) 
        self.app=ClassNotes(self.new_window)
    
    def count_atten(self):
        self.new_window=Toplevel(self.root) 
        self.app=CountAttendance(self.new_window)

    def study_files(self):
        self.new_window=Toplevel(self.root) 
        self.app=Lectures(self.new_window)
    
    def help_chatbot(self):
        self.new_window=Toplevel(self.root) 
        self.app=HelpChatbot(self.new_window)


    def view_attendance(self):
        os.startfile(r"C:\Users\Hp\Desktop\face_recognition_project_cse299\attendancehere.csv")
    
    def update_clock(self):
        current_time = datetime.now().strftime("%I:%M:%S %p")  # 12-hour format with AM/PM
        current_date = datetime.now().strftime("%d-%m-%Y")
        self.time_label.config(text="Time: " + current_time)
        self.date_label.config(text="Date: " + current_date)
        self.root.after(1000, self.update_clock)
    
    def open_google(self):
        webbrowser.open("https://www.google.com")
    
    def open_youtube(self):
        webbrowser.open("https://www.youtube.com")

    def open_gmail(self):
        webbrowser.open("https://www.gmail.com")
    
    def exit_btn(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition", "Are you sure exit this project", parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return
        
    def get_frames(self, image):
        try:
            while True:
                yield image.copy()
                image.seek(image.tell() + 1)
        except EOFError:
            pass

    def animate(self, index):
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.frames[index])
        index = (index + 1) % len(self.frames)
        self.root.after(100, self.animate, index)

# Create the main window
root = tk.Tk()
app = FrontPage(root)

# Start the main loop
root.mainloop()
