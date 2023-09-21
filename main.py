import tkinter as tk
from tkinter import filedialog

from PyPDF2 import PdfMerger

import os


def open_file_dialog():
    file_paths = filedialog.askopenfilenames(filetypes=[("PDFファイル", "*.pdf")])
    if file_paths:
        global pdf_files
        global array_char
        pdf_files.append(f"{file_paths[0]}")
        array_char += "\n" + f"{file_paths[0]}"
        file_label.config(text=f"選択したファイル{array_char}")

def open_directory_dialog():
    global dir_path
    dir_path = filedialog.askdirectory()
    if dir_path:
        directory_label.config(text=f"選択したディレクトリ\n{dir_path}")

def select_cancel():
    global pdf_files
    global array_char
    if len(pdf_files) > 0:
        file_label.config(text="選択をキャンセルしました")
    elif len(pdf_files) == 0:
        file_label.config(text="選択したファイル")
    pdf_files = []
    array_char = ""
    

def run_button():
    global new_name
    new_name = new_name_entry.get()
    merge = PdfMerger()
    for i in range(len(pdf_files)):
        merge.append(f"{pdf_files[i]}")
    save_file = os.path.join(dir_path, new_name)
    save_file = f"{save_file}.pdf"
    run_text = ""
    if len(pdf_files) < 2:
        run_text += f"{len(pdf_files)}個しかファイルが選択されていません\n"
    if new_name == "":
        run_text += "保存するファイル名が入力されていません\n"
    if dir_path == "":
        run_text += "保存するディレクトリが選択されていません"
    if run_text == "":
        j = 1
        while os.path.exists(save_file):
            save_file = f"{save_file[:-4]}({j}).pdf"
            j += 1
        merge.write(save_file)
        merge.close()
        run_text = f"{save_file}で保存しました"
    run_label.config(text=run_text)



root = tk.Tk()
root.title("ファイルとディレクトリ選択")

file_button = tk.Button(root, text="結合するPDFファイルを選択", command=open_file_dialog)
file_button.pack(pady=10)

file_label = tk.Label(root, text="選択したファイル")
file_label.pack()

cancel_button = tk.Button(root, text="選択をキャンセル", command=select_cancel)
cancel_button.pack(pady=10)

dir_button = tk.Button(root, text="保存するディレクトリを選択", command=open_directory_dialog)
dir_button.pack(pady=10)

directory_label = tk.Label(root, text="選択したディレクトリ")
directory_label.pack()

new_name_label = tk.Label(root, text="保存するファイル名を入力(拡張子は不要)")
new_name_label.pack()

new_name_entry = tk.Entry(root, width=40)
new_name_entry.pack()

save_button = tk.Button(root, text="実行", command=run_button)
save_button.pack(pady=10)

run_label = tk.Label(root, text="")
run_label.pack()


pdf_files = []
array_char = ""
new_name = ""
dir_path = ""

root.mainloop()
