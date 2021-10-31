from tkinter import *
import pygame
from tkinter import filedialog

root = Tk()
root.title("MP3 PLAYER")
root.geometry("500x300")

pygame.mixer.init()
is_paused = False


def add_song():
    song = filedialog.askopenfilename(
        title="Bir şarkı seç", filetypes=(("mp3 Files", "*.mp3"),))
    music_list.insert(END, song)


def play():
    global is_paused
    if is_paused:
        pygame.mixer.music.unpause()
        pause = False
        return
    song = music_list.get(ACTIVE)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()


def stop():
    global is_paused
    pygame.mixer.music.stop()
    is_paused = False


def pause():
    global is_paused
    pygame.mixer.music.pause()
    is_paused = True


music_list = Listbox(root, bg="black", fg="green", width=60)
music_list.pack(pady=20)

pause_img = PhotoImage(file="pause50.png")
play_img = PhotoImage(file="play50.png")
stop_img = PhotoImage(file="stop50.png")

controls = Frame(root)
controls.pack()

pause_button = Button(controls, image=pause_img, borderwidth=0, command=pause)
play_button = Button(controls, image=play_img, borderwidth=0, command=play)
stop_button = Button(controls, image=stop_img, borderwidth=0, command=stop)

pause_button.grid(row=0, column=1, padx=10)
play_button.grid(row=0, column=2, padx=10)
stop_button.grid(row=0, column=4, padx=10)

menu = Menu(root)
root.config(menu=menu)

add_songs_menu = Menu(menu)
menu.add_cascade(label="Şarkı Ekle", menu=add_songs_menu)
add_songs_menu.add_command(label="Listeye Şarkı Ekle", command=add_song)

root.mainloop()
