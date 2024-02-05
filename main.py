import os
import tkinter as tk
from tkinter import filedialog, messagebox

import fitz  # PyMuPDF
from PIL import Image

# fix blurry text
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)


def convert_pdf_to_png(pdf_path, output_directory):
    doc = fitz.open(pdf_path)
    i = 0
    for page in doc:
        i += 1
        pix = page.get_pixmap(dpi=400)
        output = output_directory + "/output_" + str(i) + ".png"
        pix.save(output)
        print(f"Page {i} saved to {output}")

    doc.close()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")], title="Choose a file to open")

    save_dir = filedialog.askdirectory(initialdir=file_path.rsplit("/", 1)[0], title="Choose a directory to save")

    # make new directory
    new_dir = save_dir + "/output_" + file_path.rsplit("/", 1)[1]
    if not os.path.exists(new_dir):
        os.mkdir(new_dir)

    try:
        convert_pdf_to_png(file_path, new_dir)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
