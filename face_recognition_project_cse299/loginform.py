from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from frontpage import FrontPage
import random

class LoginForm:
    def __init__(self, root):
        self.root = root
        root.title("Login")
        root.geometry("925x500+300+200")
        root.configure(bg="#fff")
        root.resizable(False, False)

        try:
            img = Image.open("C:/Users/Hp/Desktop/face_recognition_project_cse299/images/loginimg.png")
            img = ImageTk.PhotoImage(img)
            self.image_label = Label(root, image=img, bg="white")
            self.image_label.image = img
            self.image_label.place(x=50, y=10)
        except Exception as e:
            messagebox.showerror("Image Error", f"Error loading image: {str(e)}")

        title_lbl=Label(root, text="Face Recognition Attendance System", font=("Montserrat", 14, "bold"), bg="white", fg="#57a1f8") 
        title_lbl.place(x=35, y=335, width=480, height=30)

        frame = Frame(root, width=350, height=350, bg="white")
        frame.place(x=480, y=70)

        heading = Label(frame, text="Admin Login", fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
        heading.place(x=55, y=5)

        user = Entry(frame, width=25, fg="grey", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
        user.place(x=30, y=80)
        user.insert(0, "Username")
        user.bind('<FocusIn>', lambda e: self.on_entry_click(user))
        user.bind('<FocusOut>', lambda e: self.on_leave_user(user))

        Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)

        passw = Entry(frame, width=25, fg="grey", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
        passw.place(x=30, y=150)
        passw.insert(0, "Password")
        passw.bind('<FocusIn>', lambda e: self.on_entry_click_passw(passw))
        passw.bind('<FocusOut>', lambda e: self.on_leave_passw(passw))

        Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

        # Label for displaying the captcha
        self.captcha_label = Label(frame, text="", fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light", 11))
        self.captcha_label.place(x=30, y=185)

        # Input captcha
        self.captcha_entry = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
        self.captcha_entry.place(x=30, y=210)
        self.captcha_entry.insert(0, "Enter Captcha")
        self.captcha_entry.bind('<FocusIn>', lambda e: self.on_entry_click_captcha())
        self.captcha_entry.bind('<FocusOut>', lambda e: self.on_leave_captcha())

        # Refresh captcha
        Button(frame, width=12, pady=2, text="Refresh Captcha", bg="#57a1f8", fg="white", border=0, command=self.refresh_captcha).place(x=222, y=210)

        Button(frame, width=39, pady=7, text="Log In", bg="#57a1f8", fg="white", border=0, command=lambda: self.signin(user.get(), passw.get())).place(x=35, y=255)

    def generate_captcha(self):
        # Generate a random 4-digit number as captcha
        return str(random.randint(1000, 9999))

    def refresh_captcha(self):
        # Refresh the captcha code and update the label
        self.captcha_code = self.generate_captcha()
        self.captcha_label.config(text=self.captcha_code)

    def on_entry_click_captcha(self):
        if self.captcha_entry.get() == "Enter Captcha":
            self.captcha_entry.delete(0, "end")
            self.captcha_entry.config(fg="black")

    def on_leave_captcha(self):
        if self.captcha_entry.get() == "":
            self.captcha_entry.insert(0, "Enter Captcha")
            self.captcha_entry.config(fg="grey")

    def on_entry_click(self, entry):
        if entry.get() == "Username":
            entry.delete(0, "end")
            entry.config(fg="black")

    def on_leave_user(self, entry):
        if entry.get() == "":
            entry.insert(0, "Username")
            entry.config(fg="grey")

    def on_entry_click_passw(self, entry):
        if entry.get() == "Password":
            entry.delete(0, "end")
            entry.config(show="*")
            entry.config(fg="black")

    def on_leave_passw(self, entry):
        if entry.get() == "":
            entry.insert(0, "Password")
            entry.config(show="")
            entry.config(fg="grey")

    def signin(self, username, password):
        entered_captcha = self.captcha_entry.get()

        
        if username == 'admin' and password == '1234' and entered_captcha == self.captcha_code:  # Check if username, password and captcha are correct
            messagebox.showinfo("Login Successful", "Welcome, Admin!")
            self.root.destroy()
            self.open_front_page()
        else:
            messagebox.showerror("Login Failed", "Invalid username, password, or captcha")

    def open_front_page(self):
        front_page_window = Tk()
        front_page = FrontPage(front_page_window)
        front_page_window.mainloop()


if __name__ == "__main__":
    root = Tk()
    app = LoginForm(root)
    root.mainloop()
