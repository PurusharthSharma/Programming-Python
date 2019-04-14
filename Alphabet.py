from tkinter import *

root = Tk()
root.title("Alphabet_App")
root.configure(background='white')

strl = StringVar()
strl.set("Welcome to Alphabet App")
ABC = Frame(root,bg="white")
ABC.grid()


Cont = Canvas(ABC, width=160, height=120,bg="white")
Cont.grid(row=3,column=3)

txtDisplay = Entry(ABC, textvariable = strl,font=('arial',44,'bold'), bg="Honeydew", bd=34, width=39,
                   justify=CENTER)
txtDisplay.grid(row=0, column=0, columnspan=7, pady=1)


def Clear():
    strl.set("Welcome to Alphabet App")


def Alphabet_A():
    strl.set("A is for Apple")
    tts = gTTS(text = "A is for Apple", lang ='en')
    tts.save("Alphabet_A.mp3")
    os.system("start Alphabet_A.mp3")



def Alphabet_B():
    strl.set("B is for Apple")
    tts = gTTS(text = "B is for Apple", lang ='en')
    tts.save("Alphabet_B.mp3")
    os.system("start Alphabet_B.mp3")



def Alphabet_C():
    strl.set("C is for Cheery")
    tts = gTTS(text = "C is for Apple", lang ='en')
    tts.save("Alphabet_C.mp3")
    os.system("start Alphabet_C.mp3")



def Alphabet_D():
    strl.set("A is for Apple")
    tts = gTTS(text = "D is for Apple", lang ='en')
    tts.save("Alphabet_D.mp3")
    os.system("start Alphabet_D.mp3")



def Alphabet_E():
    strl.set("E is for Apple")
    tts = gTTS(text = "E is for Apple", lang ='en')
    tts.save("Alphabet_E.mp3")
    os.system("start Alphabet_E.mp3")



def Alphabet_F():
    strl.set("F is for Apple")
    tts = gTTS(text = "F is for Apple", lang ='en')
    tts.save("Alphabet_F.mp3")
    os.system("start Alphabet_F.mp3")



def Alphabet_G():
    strl.set("G is for Apple")
    tts = gTTS(text = "G is for Apple", lang ='en')
    tts.save("Alphabet_G.mp3")
    os.system("start Alphabet_G.mp3")




def Alphabet_H():
    strl.set("H is for Apple")
    tts = gTTS(text = "H is for Apple", lang ='en')
    tts.save("Alphabet_H.mp3")
    os.system("start Alphabet_H.mp3")



def Alphabet_I():
    strl.set("I is for Apple")
    tts = gTTS(text = "I is for Apple", lang ='en')
    tts.save("Alphabet_I.mp3")
    os.system("start Alphabet_I.mp3")



def Alphabet_J():
    strl.set("J is for Apple")
    tts = gTTS(text = "J is for Apple", lang ='en')
    tts.save("Alphabet_J.mp3")
    os.system("start Alphabet_J.mp3")



def Alphabet_K():
    strl.set("K is for Apple")
    tts = gTTS(text = "K is for Apple", lang ='en')
    tts.save("Alphabet_K.mp3")
    os.system("start Alphabet_K.mp3")



def Alphabet_L():
    strl.set("L is for Apple")
    tts = gTTS(text = "L is for Apple", lang ='en')
    tts.save("Alphabet_L.mp3")
    os.system("start Alphabet_L.mp3")



def Alphabet_M():
    strl.set("M is for Apple")
    tts = gTTS(text = "M is for Apple", lang ='en')
    tts.save("Alphabet_M.mp3")
    os.system("start Alphabet_M.mp3")



def Alphabet_N():
    strl.set("N is for Apple")
    tts = gTTS(text = "N is for Apple", lang ='en')
    tts.save("Alphabet_N.mp3")
    os.system("start Alphabet_N.mp3")



def Alphabet_O():
    strl.set("O is for Apple")
    tts = gTTS(text = "O is for Apple", lang ='en')
    tts.save("Alphabet_O.mp3")
    os.system("start Alphabet_O.mp3")



def Alphabet_P():
    strl.set("P is for Apple")
    tts = gTTS(text = "P is for Apple", lang ='en')
    tts.save("Alphabet_P.mp3")
    os.system("start Alphabet_P.mp3")



def Alphabet_Q():
    strl.set("Q is for Apple")
    tts = gTTS(text = "Q is for Apple", lang ='en')
    tts.save("Alphabet_Q.mp3")
    os.system("start Alphabet_Q.mp3")



def Alphabet_R():
    strl.set("R is for Apple")
    tts = gTTS(text = "R is for Apple", lang ='en')
    tts.save("Alphabet_R.mp3")
    os.system("start Alphabet_R.mp3")



def Alphabet_S():
    strl.set("S is for Apple")
    tts = gTTS(text = "S is for Apple", lang ='en')
    tts.save("Alphabet_S.mp3")
    os.system("start Alphabet_S.mp3")



def Alphabet_T():
    strl.set("T is for Apple")
    tts = gTTS(text = "T is for Apple", lang ='en')
    tts.save("Alphabet_T.mp3")
    os.system("start Alphabet_T.mp3")



def Alphabet_U():
    strl.set("U is for Apple")
    tts = gTTS(text = "U is for Apple", lang ='en')
    tts.save("Alphabet_U.mp3")
    os.system("start Alphabet_U.mp3")



def Alphabet_V():
    strl.set("V is for Apple")
    tts = gTTS(text = "V is for Apple", lang ='en')
    tts.save("Alphabet_V.mp3")
    os.system("start Alphabet_V.mp3")



def Alphabet_W():
    strl.set("W is for Apple")
    tts = gTTS(text = "W is for Apple", lang ='en')
    tts.save("Alphabet_W.mp3")
    os.system("start Alphabet_W.mp3")



def Alphabet_X():
    strl.set("X is for Apple")
    tts = gTTS(text = "X is for Apple", lang ='en')
    tts.save("Alphabet_X.mp3")
    os.system("start Alphabet_X.mp3")



def Alphabet_Y():
    strl.set("Y is for Apple")
    tts = gTTS(text = "Y is for Apple", lang ='en')
    tts.save("Alphabet_Y.mp3")
    os.system("start Alphabet_Y.mp3")



def Alphabet_Z():
    strl.set("Z is for Apple")
    tts = gTTS(text = "Z is for Apple", lang ='en')
    tts.save("Alphabet_Z.mp3")
    os.system("start Alphabet_Z.mp3")




btnA = Button(ABC, pady=1, bd=4, font=('arial',21,'bold'), width=10, height=3,
              text="A", bg="Honeydew").grid(row=1, column=0)

btnB = Button(ABC, pady=1, bd=4, font=('arial',21,'bold'), width=10, height=3,
              text="B", bg="powder blue").grid(row=1, column=1)

btnC = Button(ABC, pady=1, bd=4, font=('arial',21,'bold'), width=10, height=3,
              text="C", bg="Cornsilk").grid(row=1, column=2)

btnD = Button(ABC, pady=1, bd=4, font=('arial',21,'bold'), width=10, height=3,
              text="D", bg="powder blue").grid(row=1, column=3)

btnE = Button(ABC, pady=1, bd=4, font=('arial',21,'bold'), width=10, height=3,
              text="E", bg="Cornsilk").grid(row=1, column=4)

btnF = Button(ABC, pady=1, bd=4, font=('arial',21,'bold'), width=10, height=3,
              text="F", bg="powder blue").grid(row=1, column=5)

btnG = Button(ABC, pady=1, bd=4, font=('arial',21,'bold'), width=10, height=3,
              text="G", bg="Cornsilk").grid(row=1, column=6)


#=======

btnH = Button(ABC, pady=1, bd=4, font=('arial',21,'bold'), width=10, height=3,
              text="H", bg="powder blue").grid(row=2, column=0)

btnI = Button(ABC, pady=1, bd=4, font=('arial',21,'bold'), width=10, height=3,
              text="I", bg="Honeydew").grid(row=2, column=1)

btnJ = Button(ABC, pady=1, bd=4, font=('arial',21,'bold'), width=10, height=3,
              text="J", bg="powder blue").grid(row=2, column=2)

btnK = Button(ABC, pady=1, bd=4, font=('arial',21,'bold'), width=10, height=3,
              text="K", bg="Honeydew").grid(row=2, column=3)

btnL = Button(ABC, pady=1, bd=4, font=('arial',21,'bold'), width=10, height=3,
              text="L", bg="powder blue").grid(row=2, column=4)

btnM = Button(ABC, pady=1, bd=4, font=('arial',21,'bold'), width=10, height=3,
              text="M", bg="Honeydew").grid(row=2, column=5)

btnN = Button(ABC, pady=1, bd=4, font=('arial',21,'bold'), width=10, height=3,
              text="N", bg="powder blue").grid(row=2, column=6)


#=======


btnO = Button(ABC, pady=1, bd=4, font=('arial',21,'bold'), width=10, height=3,
              text="O", bg="Cornsilk").grid(row=3, column=0)

btnP = Button(ABC, pady=1, bd=4, font=('arial',21,'bold'), width=10, height=3,
              text="P", bg="powder blue").grid(row=3, column=1)

btnQ = Button(ABC, pady=1, bd=4, font=('arial',21,'bold'), width=10, height=3,
              text="Q", bg="Cornsilk").grid(row=3, column=2)

btnR = Button(ABC, pady=1, bd=4, font=('arial',21,'bold'), width=10, height=3,
              text="R", bg="powder blue").grid(row=3, column=3)

btnS = Button(ABC, pady=1, bd=4, font=('arial',21,'bold'), width=10, height=3,
              text="S", bg="Cornsilk").grid(row=3, column=4)

btnT = Button(ABC, pady=1, bd=4, font=('arial',21,'bold'), width=10, height=3,
              text="T", bg="powder blue").grid(row=3, column=5)

btnU = Button(ABC, pady=1, bd=4, font=('arial',21,'bold'), width=10, height=3,
              text="U", bg="Cornsilk").grid(row=3, column=6)

#==========

              

btnV = Button(ABC, pady=1, bd=4, font=('arial',21,'bold'), width=10, height=3,
              text="V", bg="powder blue").grid(row=4, column=0)

btnW = Button(ABC, pady=1, bd=4, font=('arial',21,'bold'), width=10, height=3,
              text="W", bg="Honeydew").grid(row=4, column=1)

btnX = Button(ABC, pady=1, bd=4, font=('arial',21,'bold'), width=10, height=3,
              text="X", bg="powder blue").grid(row=4, column=2)

btnY = Button(ABC, pady=1, bd=4, font=('arial',21,'bold'), width=10, height=3,
              text="Y", bg="Honeydew").grid(row=4, column=3)

btnZ = Button(ABC, pady=1, bd=4, font=('arial',21,'bold'), width=10, height=3,
              text="Z", bg="powder blue").grid(row=4, column=4)



root.mainloop()
