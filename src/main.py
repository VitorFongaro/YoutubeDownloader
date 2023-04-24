import tkinter
from tkinter import ttk, messagebox, filedialog
import youtube
import thumbnail


def verify():
    video_link = link_var.get()
    option = option_var.get()
    
    if video_link == "" or option == "":
        messagebox.showwarning("Erro", "Preencha os campos.")
    else:
        thumb_link = youtube.image(video_link)
        if thumb_link == False:
            messagebox.showwarning("Erro", "Vídeo não encontrado")
        else:
            show_video(thumb_link)
            show_download()
            

def show_video(link):
    text = youtube.title(link)
    video_title_label = tkinter.Label(title_frame, text=text, font=("Consolas", 10)).grid(row=0, column=0)
    image = thumbnail.convert(link)
    thumb_label = tkinter.Label(show_frame, image=image)
    thumb_label.image = image
    thumb_label.grid(row=0, column=0)


def show_download():
    path_label = tkinter.Label(download_frame, textvariable=path_var, width=50, bg="white").grid(row=0, column=0)
    path_btn = tkinter.Button(download_frame, text="Escolher caminho", command=choose_path, bg="red", fg="white", font=("Consolas")).grid(row=0, column=1)
    

def choose_path():
    path = filedialog.askdirectory()
    path_var.set(path)
    download_btn = tkinter.Button(btn_download_frame, text="Download", bg="red", fg="white", command=dowload, font=("Consolas")).grid(row=1, column=0, columnspan=2)
    

def dowload():
    if option_var.get() == "Vídeo":
        if youtube.video(link_var.get(), path_var.get()) == True:
            text = "Download realizado com sucesso!"
        else:
            text = "Erro ao realizar o download"
    else:
        if youtube.audio(link_var.get(), path_var.get()) == True:
            text = "Download realizado com sucesso!"
        else:
            text = "Erro ao realizar o download"
    result_label = tkinter.Label(result_frame, text=text, bg="white", fg="red" ,font=("Consolas", 18)).grid(row=0, column=0)

    
root = tkinter.Tk()
root.title("YouTube Downloader")
root.geometry("800x600")
style= ttk.Style()
style.theme_use('clam')
style.configure("TCombobox", fieldbackground= "gray90", background= "white")
title_label = tkinter.Label(root, text="YouTube Downloader", font=("Consolas", 18)).pack(pady=10)
frame = tkinter.Frame(root)
frame.pack()

# Var
option_var = tkinter.StringVar()
link_var = tkinter.StringVar()
path_var = tkinter.StringVar()

# Link
info_frame = tkinter.LabelFrame(frame, bg="white")
info_frame.grid(row= 0, column=0, pady=5)

link_label = tkinter.Label(info_frame, text="Link: ", font=("Consolas"), bg="white").grid(row=0, column=0)
link = tkinter.Entry(info_frame, textvariable=link_var,width=30, bg="gray90",).grid(row=0, column=1, padx=5)
combobox_label= tkinter.Label(info_frame, text="Selecione uma opcão: ", font=("Consolas"), bg="white").grid(row=1, column=0)
option = ttk.Combobox(info_frame, textvariable=option_var,values=["Vídeo", "Áudio"], width=27).grid(row=1, column=1)

for widget in info_frame.winfo_children():
    widget.grid_configure(pady=5)

# Submit
submit_frame = tkinter.LabelFrame(frame, bg="white")
submit_frame.grid(row=1, column=0)
submit_btn = tkinter.Button(submit_frame, text="Enviar", width=20, bg="red", fg="white", font=("Consolas"), command=verify).grid(row=0,column=0)

# Show
title_frame = tkinter.LabelFrame(frame, bg="white")
title_frame.grid(row=2, column=0, pady=10)
show_frame = tkinter.LabelFrame(frame, bg="white")
show_frame.grid(row=3, column=0)

# Download
download_frame = tkinter.LabelFrame(frame, bg="white")
download_frame.grid(row=4, column=0, pady=10)
btn_download_frame = tkinter.LabelFrame(frame, bg="white")
btn_download_frame.grid(row=5, column=0, pady=5)

# Result
result_frame = tkinter.LabelFrame(frame, bg="white")
result_frame.grid(row=6, column=0)

root.mainloop()