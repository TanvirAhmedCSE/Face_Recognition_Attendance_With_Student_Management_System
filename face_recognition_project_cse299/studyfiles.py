import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import fitz

class Lectures:
    def __init__(self, root):
        self.root = root
        self.root.title("Class Lectures")
        root.geometry("1920x1080")
        self.root.configure(bg="skyblue")

        self.file_data = []
        self.pdf_document = None
        self.current_page = 0

        self.create_widgets()
        self.load_file_data()

    def create_widgets(self):
        self.listbox = tk.Listbox(self.root,width=50)
        self.listbox.pack()

        self.open_button = tk.Button(self.root, text="Upload Lectures", command=self.open_file_dialog)
        self.open_button.pack()

        self.listbox.bind("<<ListboxSelect>>", self.on_file_select)

        self.img_label = tk.Label(self.root)
        self.img_label.pack()

        self.page_number_label = tk.Label(self.root)
        self.page_number_label.pack()

        self.prev_button = tk.Button(self.root, text="Previous Page", command=self.prev_page)
        self.prev_button.pack()

        self.next_button = tk.Button(self.root, text="Next Page", command=self.next_page)
        self.next_button.pack()

    def open_file_dialog(self):
        file_types = [("PDF files", "*.pdf")]
        file = filedialog.askopenfilename(filetypes=file_types)
        if file:
            self.file_data.append((file, os.path.basename(file)))
            self.listbox.insert(tk.END, os.path.basename(file))
            self.save_file_data()
            self.open_pdf(file)

    def save_file_data(self):
        with open("file_data.txt", "w") as file:
            for file_path, file_name in self.file_data:
                file.write(f"{file_path}\n")

    def load_file_data(self):
        if os.path.exists("file_data.txt"):
            with open("file_data.txt", "r") as file:
                for line in file:
                    file_path = line.strip()
                    self.file_data.append((file_path, os.path.basename(file_path)))
                    self.listbox.insert(tk.END, os.path.basename(file_path))

    def open_pdf(self, pdf_file):
        self.pdf_document = fitz.open(pdf_file)
        self.show_page()

    def show_page(self):
        if self.pdf_document:
            num_pages = len(self.pdf_document)
            if 0 <= self.current_page < num_pages:
                page = self.pdf_document.load_page(self.current_page)
                image = page.get_pixmap(matrix=fitz.Matrix(2, 2))
                image.save("temp_image.jpg")
                img = Image.open("temp_image.jpg")
                img.thumbnail((600, 600))
                img = ImageTk.PhotoImage(img)
                self.img_label.config(image=img)
                self.img_label.image = img
                self.page_number_label.config(text=f"Page {self.current_page + 1} of {num_pages}")

    def next_page(self):
        if self.pdf_document:
            self.current_page = (self.current_page + 1) % len(self.pdf_document)
            self.show_page()

    def prev_page(self):
        if self.pdf_document:
            self.current_page = (self.current_page - 1) % len(self.pdf_document)
            self.show_page()

    def on_file_select(self, event):
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            self.current_page = 0
            self.open_pdf(self.file_data[selected_index][0])

if __name__ == "__main__":
    root = tk.Tk()
    pdf_viewer = Lectures(root)
    root.mainloop()
