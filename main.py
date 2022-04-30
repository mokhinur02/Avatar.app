import tkinter as tk

class SampleApp(tk.Tk):
    def __init__(self,*arg,**kwargs):
        tk.Tk.__init__(self,*arg,**kwargs)
        container=tk.Frame(self)
        container.pack(side='top',fill='both',expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        self.frames={}
        for F in(MainPage,SecondPage,ResultPagea,ResultPageb,ResultPagec,PrisePagea):
            page_name=F.__name__
            frame=F(parent=container,controller=self)
            self.frames[page_name]=frame
            frame.grid(row=0,column=0,sticky='nsew')
            self.show_frame('MainPage')
    def show_frame(self, page_name):
        frame=self.frames[page_name]
        frame.tkraise()

class MainPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg="deepSkyBlue")
        self.controller=controller
        self.controller.title('AVATAR APP')
        self.controller.state('zoomed')

        self.controller.iconphoto(False,tk.PhotoImage
                (file='ava/girl1.png'))
        big_label=tk.Label(self,text='AVATAR APP',font=('Script MT Bold',50,'bold'),fg='black',bg='violet')
        big_label.pack(pady=30)

        login_label=tk.Label(self,text='ENTER YOUR NAME:',font=('Baskerville Old Face',15,'bold'),bg='violet',fg='black')
        login_label.pack(pady=30)
        my_login=tk.StringVar()
        login_entry=tk.Entry(self,textvariable=my_login,font=('Baskerville Old Face',15,'bold'),bg='cyan',fg='black')
        login_entry.pack(pady=30)

        pin_label=tk.Label(self,text='ENTER YOUR PIN',font=('Baskerville Old Face',15,'bold'),bg='violet',fg='black')
        pin_label.pack(pady=30)
        my_pin=tk.StringVar()
        pin_entry=tk.Entry(self,textvariable=my_pin,font=('Baskerville Old Face',15,'bold'),bg='cyan',fg='black')
        pin_entry.pack(pady=30)

        def check_pin():
            if my_login.get()=='haha' and my_pin.get() =='0000':
                controller.show_frame('SecondPage')
            else:
                right_label['text'] ='WRONG LOGIN OR PIN'
        pin_button=tk.Button(self,text='CHECK YOUR PIN',command=check_pin,font=('Baskerville Old Face',15,'bold')
                             ,bg='violet',fg='black',activeforeground='black',activebackground='deepSkyBlue')
        pin_button.pack()
        right_label=tk.Label(self,font=('Baskerville Old Face',15,'bold'),bg='cyan',fg='fireBrick')
        right_label.pack(pady=30)

class SecondPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent,bg='deepSkyBlue')
        self.controller=controller
        big_label=tk.Label(self,text='CHOOSE ONE OF THESE:',font=('Baskerville Old Face',50,'bold')
                           ,fg='white',bg='violet',)
        big_label.pack(pady=50)
        big_label.place(x=280, y=10)

        def get_male():
            controller.show_frame('ResultPagea')
        male_button = tk.Button(self, text='male', command=get_male, font=('Baskerville Old Face', 20, 'bold'),
                                bg='cornFlowerBlue', fg='black', width=15, activebackground='deepSkyBlue',
                                activeforeground='black')
        male_button.pack(pady=50)
        male_button.place(x=150, y=150)

        def get_female():
            controller.show_frame('ResultPagec')
        female_button=tk.Button(self,text='female',command=(get_female),font=('Baskerville Old Face',20,'bold'),
                fg='black',bg='hotPink',width=15,activebackground='deepSkyBlue',activeforeground='black')
        female_button.pack(pady=50)
        female_button.place(x=950,y=150)

        def get_old():
            controller.show_frame('ResultPageb')
        old_button=tk.Button(self,text='old:+60',command=(get_old),font=('Baskerville Old Face',20,'bold'),
                fg='black',bg='goldenrod',width=15,activebackground='deepSkyBlue',activeforeground='black')
        old_button.pack(pady=50)
        old_button.place(x=550,y=150)

        def return_page():
            controller.show_frame('MainPage')
        return_button=tk.Button(self,text='bake<--',command=return_page,font=('Baskerville Old Face',15,'bold'),
                                  bg='hotPink',fg='black',activebackground='deepSkyBlue',activeforeground='black')
        return_button.pack(pady=50)
        return_button.place(x=650, y=500)
class ResultPagea(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg='black')
        self.controller = controller
        self.backGroundImage = tk.PhotoImage(file=r"ava/boys1.png")
        self.backGroundImageLabel = tk.Label(self, image=self.backGroundImage)
        self.backGroundImageLabel.place(x=100, y=120)
        self.backGroundImage2 = tk.PhotoImage(file=r"ava/boys2.png")
        self.backGroundImageLabel2 = tk.Label(self, image=self.backGroundImage2)
        self.backGroundImageLabel2.place(x=800, y=120)
        big_label=tk.Label(self,text='YOUR RESULT IS....?',font=('Baskerville Old Face',50,'bold'),
                             bg='salmon',fg='black')
        big_label.pack(pady=30)
        def return_page():
            controller.show_frame('SecondPage')

        return_button=tk.Button(self,text='back to first page',command=return_page,font=('Baskerville Old Face',20,'bold'),
                    bg='salmon',fg='black',activebackground='cyan',activeforeground='black')
        return_button.pack(pady=50)
        return_button.place(x=590,y=630)
        def return_page():
            controller.show_frame('MainPage')

        return_button=tk.Button(self,text='back to main page',command=return_page,font=('Baskerville Old Face',20,'bold'),
                   bg='salmon',fg='black',activebackground='cyan',activeforeground='black')
        return_button.pack(pady=50)
        return_button.place(x=590,y=700)
class ResultPageb(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg='white')
        self.controller = controller
        self.backGroundImage = tk.PhotoImage(file=r"ava/old.png")
        self.backGroundImageLabel = tk.Label(self, image=self.backGroundImage)
        self.backGroundImageLabel.place(x=500, y=200)

        big_label=tk.Label(self,text='YOUR RESULT IS...?',font=('Baskerville Old Face',50,'bold'),
                             bg='salmon',fg='black')
        big_label.pack(pady=30)
        def return_page():
            controller.show_frame('SecondPage')

        return_button=tk.Button(self,text='back to first page',command=return_page,font=('Baskerville Old Face',20,'bold'),
                    bg='salmon',fg='black',activebackground='cyan',activeforeground='black')
        return_button.pack(pady=50)
        return_button.place(x=100,y=500)
        def return_page():
            controller.show_frame('MainPage')

        return_button=tk.Button(self,text='back to main page',command=return_page,font=('Baskerville Old Face',20,'bold'),
                   bg='salmon',fg='black',activebackground='cyan',activeforeground='black')
        return_button.pack(pady=50)
        return_button.place(x=100,y=580)
class ResultPagec(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg='pink')
        self.controller=controller

        self.backGroundImage=tk.PhotoImage(file=r"ava/girl1.png")
        self.backGroundImageLabel=tk.Label(self,image=self.backGroundImage)
        self.backGroundImageLabel.place(x=130,y=120)

        def backGroundImage_page():
            controller.show_frame('PrisePagea')
        backGroundImage_button=tk.Button(self,command=backGroundImage_page,text='this one',
         font=('Baskerville Old Face',20,'bold'),bg='salmon',fg='black',activebackground='pink',activeforeground='black')
        backGroundImage_button.pack(pady=50)
        backGroundImage_button.place(x=175,y=325)

        self.backGroundImage2 = tk.PhotoImage(file=r"ava/girl2.png")
        self.backGroundImageLabel2 = tk.Label(self, image=self.backGroundImage2)
        self.backGroundImageLabel2.place(x=430, y=120)
        def backGroundImage_page():
            controller.show_frame('PrisePageb')
        backGroundImage_button=tk.Button(self,text='this one',command=backGroundImage_page,
        font=('Baskerville Old Face',20,'bold'),bg='salmon',fg='black',activebackground='pink',activeforeground='black')
        backGroundImage_button.pack(pady=50)
        backGroundImage_button.place(x=475,y=325)


        self.backGroundImage3 = tk.PhotoImage(file=r"ava/girl3.png")
        self.backGroundImageLabel3 = tk.Label(self, image=self.backGroundImage3)
        self.backGroundImageLabel3.place(x=730, y=120)
        def backGroundImage_page():
            controller.show_frame('PrisePagec')
        backGroundImage_button=tk.Button(self,text='this one',command=backGroundImage_page,
        font=('Baskerville Old Face',20,'bold'),bg='salmon',fg='black',activebackground='pink',activeforeground='black')
        backGroundImage_button.pack(pady=50)
        backGroundImage_button.place(x=775,y=325)


        self.backGroundImage4 = tk.PhotoImage(file=r"ava/girl4.png")
        self.backGroundImageLabel4= tk.Label(self, image=self.backGroundImage4)
        self.backGroundImageLabel4.place(x=1030, y=120)
        def backGroundImage_page():
            controller.show_frame('PrisePaged')
        backGroundImage_button=tk.Button(self,text='this one',command=backGroundImage_page,
        font=('Baskerville Old Face',20,'bold'),bg='salmon',fg='black',activebackground='pink',activeforeground='black')
        backGroundImage_button.pack(pady=50)
        backGroundImage_button.place(x=1075,y=325)

        big_label=tk.Label(self,text='YOUR RESULT IS....?',font=('Baskerville Old Face',50,'bold'),
                             bg='salmon',fg='black')
        big_label.pack(pady=30)
        def return_page():
            controller.show_frame('SecondPage')

        return_button=tk.Button(self,text='back to first page',command=return_page,font=('Baskerville Old Face',20,'bold'),
                    bg='salmon',fg='black',activebackground='cyan',activeforeground='black')
        return_button.pack(pady=50)
        return_button.place(x=565,y=420)
        def return_page():
            controller.show_frame('MainPage')

        return_button=tk.Button(self,text='back to main page',command=return_page,font=('Baskerville Old Face',20,'bold'),
                   bg='salmon',fg='black',activebackground='cyan',activeforeground='black')
        return_button.pack(pady=50)
        return_button.place(x=565,y=550)


class PrisePagea(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg='pink')
        self.controller = controller
        self.backGroundImage = tk.PhotoImage(file=r"ava/girl1.png")
        self.backGroundImageLabel = tk.Label(self, image=self.backGroundImage)
        self.backGroundImageLabel.place(x=130, y=120)
        idlabel = tk.Label(self, text='1) This is a girl with two different eyes',
                           font=('Baskerville Old Face', 20, 'bold'),
                           bg='salmon', fg='black')
        idlabel.place(x=500, y=50)
        idlabel = tk.Label(self, text='2) Black hair and white skin', font=('Baskerville Old Face', 20, 'bold'),
                           bg='salmon', fg='black')
        idlabel.place(x=500, y=100)
        idlabel = tk.Label(self, text='3) She looks like an Asian people', font=('Baskerville Old Face', 20, 'bold'),
                           bg='salmon', fg='black')
        idlabel.place(x=500, y=150)
        def prise_page():
            prise_label['text'] = 'This avatar costs 1$'
        prise_label = tk.Label(self, font=('Baskerville Old Face', 20, 'bold'), bg='salmon', fg='green')
        prise_label.place(x=120, y=400)
        prise_button = tk.Button(self, text='prise', command=prise_page, font=('Baskerville Old Face', 20, 'bold'),
                                 bg='salmon', fg='black', activebackground='pink', activeforeground='black')
        prise_button.pack(pady=50)
        prise_button.place(x=175, y=325)
        def return_page():
            controller.show_frame('ResultPagec')
        return_button = tk.Button(self, text='back to result page', command=return_page,
                                  font=('Baskerville Old Face', 20, 'bold'),
                                  bg='salmon', fg='black', activebackground='pink', activeforeground='black')
        return_button.place(x=565, y=400)
        def return_page():
            controller.show_frame('SecondPage')
        return_button = tk.Button(self, text='back to first page', command=return_page,
                                  font=('Baskerville Old Face', 20, 'bold'),
                                  bg='salmon', fg='black', activebackground='pink', activeforeground='black')
        return_button.place(x=565, y=500)
        def return_page():
            controller.show_frame('MainPage')
        return_button = tk.Button(self,text='back to main page', command=return_page,
                                  font=('Baskerville Old Face', 20, 'bold'),
                                  bg='salmon', fg='black', activebackground='pink', activeforeground='black')
        return_button.place(x=565, y=600)
if __name__ == '__main__':
    app=SampleApp()
    app.mainloop()
    app.mainloop()
