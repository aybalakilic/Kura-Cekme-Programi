from tkinter import * #tkinter kütüphanesinin tüm alt fonksiyonları ithal ettim
import random         #random kütüphanesini çağırdım

arayuz = Tk()  #başa eklenir muhakkak

arayuz.title("Kura Çekme Programı") #Arayüzün başlığı
arayuz.resizable(False,False)   #Ortadaki simge ve ekran oranı imlecini iptal eder

canva =Canvas( arayuz , height=500 , width=800)    #canvas nesnesi üzerinde nesne oluşturu
canva.pack()    #ekrana gönderir

top_frame = Frame(arayuz , height=100 , width=780 , bg ="#f0a1d3")
top_frame.place(x=10 , y=10)

top_frame_yazisi = Label(top_frame , text="Kura Çekme Programına Hoşgeldiniz" , font=("Times-20",28,"bold") , fg="white" , bg="#f0a1d3")
top_frame_yazisi.place(x=45, y=30)

big_frame = Frame(arayuz, height=370, width=780, bg="#f2d8e8")
big_frame.place(x=10, y=120)



def isim_alma_fonk():
    
    names = entry.get()
    dizi =names.split()

    kazanan= dizi[random.randint(0,len(dizi)-1)]
    print(dizi)
    print(kazanan)
    
    asil_sonuc_label.config(text=f"Kazanan İsim: {kazanan}")




entry = Entry(big_frame,font=("Times-20",18))
entry.place(x=250,y=90)

uzun_frame = Frame(big_frame, height=50 , width = 550, bg="#f0a1d3")
uzun_frame.place(x=100,y=20)

entry_ustu_yazi =Label(big_frame, text ="Adayların isimlerini boşluk bırakarak aşağıya yazınız...", font=("Times-20",15,"bold"), fg="black")
entry_ustu_yazi.place(x=120 ,y=30)


random_button =Button(big_frame, text ="Kura Çek",font=("Times-20",20,"bold"), bg="#b39fab",fg="white", command=isim_alma_fonk)
random_button.place(x=300 , y=140 )  


sonuc_frame =Frame(big_frame,height=150,width=550,bg="#f0a1d3")
sonuc_frame.place(x=100,y=205)

asil_sonuc_label=Label(sonuc_frame, font=("Times-20",25,"bold"),bg="#f0a1d3", fg="black")
asil_sonuc_label.place(x=100, y=55)





















arayuz.mainloop() #sonuna bu yazılıp döndürülür