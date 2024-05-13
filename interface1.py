from time import sleep
from tkinter import *
from threading import Thread
from tkinter import filedialog
import pygame 



class Timer:
    
    def __init__(self, master):
        # Master
        self.master = master
        self.interface()
    def interface(self):
        self.Frame_Principale = self.create_rounded_frame(self.master, 50, 20, 500, 750, "#8547F5")
        self.Titre = Label(self.Frame_Principale, text="TIMER 00:00", font=("bold", 20), fg="BLACK", bg="#8547F5")
        self.Titre.place(x=140, y=0, width=210, height=50)
        # Sets
        self.sets = self.create_rounded_frame(self.Frame_Principale, 20, 80, 460, 50, "#F4F4F4")

        self.sets_et = Label(self.sets, text="CYCLES", background="blue", fg="#818181", bg="#F4F4F4",font=("helvetica 24 bold", 12))
        self.sets_et.place(x=3, y=4, width=260, height=35)

        self.sets_saisie = Entry(self.sets, bg="white", font=("digital-7", 20), fg="green")
        self.sets_saisie.place(x=285, y=3, width=160, height=35)
        # Warmup
        self.Warmup = self.create_rounded_frame(self.Frame_Principale, 20, 160, 460, 50, "#F4F4F4")

        self.war_et = Label(self.Warmup, text="Echauffement (seconds)        ", fg="#818181", bg="#F4F4F4",font=("helvetica 24 bold", 14))
        self.war_et.place(x=3, y=4, width=260, height=35)

        self.Warmup_saisie = Entry(self.Warmup, bg="white", font=("digital-7", 20), fg="green")
        self.Warmup_saisie.place(x=285, y=3, width=160, height=35)
        # Work
        self.Work = self.create_rounded_frame(self.Frame_Principale, 20, 240, 460, 50, "#F4F4F4")

        self.work_et = Label(self.Work, text="Intervalle de travail (seconds)", fg="#818181", bg="#F4F4F4",font=("helvetica 24 bold", 14))
        self.work_et.place(x=3, y=4, width=260, height=35)

        self.work_saisie = Entry(self.Work, bg="white", font=("digital-7", 20), fg="green")
        self.work_saisie.place(x=285, y=3, width=160, height=35)
        # Rest
        self.Rest = self.create_rounded_frame(self.Frame_Principale, 20, 320, 460, 50, "#F4F4F4")

        self.Rest_et = Label(self.Rest, text="Intervalle de repos (seconds)", fg="#818181", bg="#F4F4F4",font=("helvetica 24 bold", 14))
        self.Rest_et.place(x=5, y=4, width=260, height=35)

        self.Rest_saisie = Entry(self.Rest, bg="white", font=("digital-7", 20), fg="green")
        self.Rest_saisie.place(x=285, y=3, width=160, height=35)
        # Total
        self.Total = self.create_rounded_frame(self.Frame_Principale, 20, 400, 460, 50, "#F4F4F4")
        self.Total_et = Label(self.Total, text="TOTAL :", bg="#F4F4F4", fg="#818181", font=("helvetica 24 bold", 14))
        self.Total_et.place(x=3, y=4, width=260, height=35)
        # RUN
        self.RUN = Button(self.Frame_Principale, text="RUN", bg="BLUE", fg="green", font=("Time", 15), command=self.run)
        self.RUN.place(x=20, y=680, width=220, height=50)

        # RESET
        self.RESET = Button(self.Frame_Principale, text="RESET", bg="BLUE", fg="green", font=("Time", 15),command= self.Restart)
        self.RESET.place(x=260, y=680, width=220, height=50)
        self.restart = False

    def play_audio(self,audio):
    # Load the selected audio file
        if audio:
            pygame.mixer.init()
            pygame.mixer.music.load(audio)
            pygame.mixer.music.play()
    def pause_timer(self):
       pass
    def Restart(self):
        self.restart = True
        self.interface()

    def create_rounded_frame(self, parent, x, y, width, height, couleur):
        frame = Frame(parent, bg=couleur, bd=5, relief="ridge")
        frame.place(x=x, y=y, width=width, height=height)
        return frame
    
    def run(self):
        self.SetS = int(self.sets_saisie.get())
        self.Work = int(self.work_saisie.get())
        self.Warmup = int(self.Warmup_saisie.get())
        self.Rest = int(self.Rest_saisie.get())
        self.total = (self.SetS * self.Work + self.Warmup + (self.SetS - 1) * self.Rest) 
        Total_saisie = Label(self.Total, bg="black", font=("digital-7", 20), fg="green")
        Total_saisie.config(text=f"{self.total}")
        Total_saisie.place(x=285, y=3, width=160, height=35)
        self.play_audio("C:\\Users\\T16\\Desktop\\Projet\\robotic-countdown-43935.mp3")
        sleep(3)
        self.thread1 = Thread(target=self.Total1)
        self.thread2 = Thread(target= self.timer_count, args=(self.SetS, self.Work, self.Warmup, self.Rest))

        self.thread1.start()
        self.thread2.start()
       
    def timer_count(self, sets, Work, Warmup, Rest):
        self.warmup(Warmup)
        self.Sets(sets, Work, Rest)    

    def Sets(self, S, W, R):
        while int(S) >= 0 and  not self.restart :
            if self.restart:
                break
            self.sets = self.create_rounded_frame(self.Frame_Principale, 20, 80, 460, 50, "#F4F4F4")
            self.sets_et = Label(self.sets, text="EXERCICE", background="blue", fg="#818181", bg="#F4F4F4",font=("helvetica 24 bold", 14))
            self.sets_et.place(x=3, y=4, width=260, height=35)
            self.sets_saisie = Label(self.sets, bg="black", font=("digital-7", 20), fg="green")
            self.sets_saisie.place(x=285, y=3, width=160, height=35)
            self.sets_saisie.config(text=f"{S}")
            self.Frame_Principale.update()
            if S == 0:
                break
            self.work(W)
            if S == 1:
                S -= 1
                continue
            self.rest(R)
            S -= 1

    def warmup(self, w):
        self.Warmup = self.create_rounded_frame(self.Frame_Principale, 20, 160, 460, 50, "#F4F4F4")
        self.war_et = Label(self.Warmup, text="Echauffement (seconds)          ", fg="#818181", bg="#F4F4F4",font=("helvetica 24 bold", 14))
        self.war_et.place(x=3, y=4, width=260, height=35)
        self.Warmup_saisie = Label(self.Warmup, bg="black", font=("digital-7", 20), fg="green")
        self.Warmup_saisie.place(x=285, y=3, width=160, height=35)
        while w > 0 and  not self.restart:
            if self.restart:
                break
            w -= 1
            self.Warmup_saisie.config(text=f"{w}")
            sleep(1)
            self.Frame_Principale.update()

    def work(self, w):
        self.Work = self.create_rounded_frame(self.Frame_Principale, 20, 240, 460, 50, "#F4F4F4")
        self.work_et = Label(self.Work, text="Intervalle de travail (seconds)", fg="#818181", bg="#F4F4F4",font=("helvetica 24 bold", 14))
        self.work_et.place(x=3, y=4, width=260, height=35)
        self.work_saisie = Label(self.Work, bg="black", font=("digital-7", 20), fg="green")
        self.work_saisie.place(x=285, y=3, width=160, height=35)
        while w > 0 and  not self.restart :
            if self.restart:
                break
            w -= 1
            self.work_saisie.config(text=f"{w}")
            sleep(1)
            self.Frame_Principale.update()

    def Total1(self):
        T = self.total
        self.Total = self.create_rounded_frame(self.Frame_Principale, 20, 400, 460, 50, "#F4F4F4")
        self.Total_et = Label(self.Total, text="TOTAL : ", fg="#818181", font=("helvetica 24 bold", 14))
        self.Total_et.place(x=3, y=4, width=260, height=35)
        self.Total_saisie = Label(self.Total, bg="black", text="Total", font=("digital-7", 20), fg="green")
        self.Total_saisie.place(x=285, y=3, width=160, height=35)
        while T > 0 and  not self.restart :
            if self.restart:
                break
            T -= 1
            self.Total_saisie.config(text=f"{T}")
            sleep(1)
            self.Frame_Principale.update()

    def rest(self, S):
        self.Rest = self.create_rounded_frame(self.Frame_Principale, 20, 320, 460, 50, "#F4F4F4")
        self.Rest_et = Label(self.Rest, text="Intervalle de repos (seconds)", fg="#818181", bg="#F4F4F4",font=("helvetica 24 bold", 14))
        self.Rest_et.place(x=5, y=4, width=260, height=35)
        self.Rest_saisie = Label(self.Rest, bg="black", font=("digital-7", 20), fg="green")
        self.Rest_saisie.place(x=285, y=3, width=160, height=35)
        while S > 0 and not self.restart :
            if self.restart:
                break
            S -= 1
            self.Rest_saisie.config(text=f"{S}")
            self.Frame_Principale.update()
            sleep(1)
        

def main():
    master = Tk()
    master.geometry("400x100")
    frame = Timer(master)
    master.mainloop()

if __name__ == "__main__":
    main()
