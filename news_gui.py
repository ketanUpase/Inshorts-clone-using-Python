import io
import webbrowser

import requests
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk, Image
class NewsApp:
    def __init__(self):
        # fetch data
        self.data = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=3401fcb1b4cd4dc0abc9ec8cf57937b0').json()
        # initial GUI load
        self.load_gui()
        # load the 1 st news item
        self.load_news_item(0)


    def load_gui(self):
        self.root = Tk()
        self.root.geometry('350x600')
        self.root.resizable(False, False)
        self.root.title('Mera News App')
        self.root.configure(background='black')

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def load_news_item(self, index):
        #clear the screen for the news item
        self.clear()

        # image
        try:
            image_url = self.data['articles'][index]['urlToImage']
            raw_data = urlopen(image_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
            photo = ImageTk.PhotoImage(im)
        except:
            image_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Image_not_available.png/640px-Image_not_available.png'
            raw_data = urlopen(image_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
            photo = ImageTk.PhotoImage(im)


        label = Label(self.root, image=photo)
        label.pack()
        heading = Label(self.root, text=self.data['articles'][index]['title'], bg='black', fg='white', wraplength=350, justify='center')
        heading.pack(pady=(10, 20))
        heading.config(font=('verdana', 15))

        details = Label(self.root, text=self.data['articles'][index]['description'], bg='black', fg='white', wraplength=350, justify='center')
        details.pack(pady=(2, 20))
        details.config(font=('verdana', 10))

        frame = Frame(self.root, bg='black')
        frame.pack(expand=True, fill=BOTH)

        if index !=0:
            prev = Button(frame, text='prev', width=16, height=3, command=lambda :self.load_news_item(index-1))
            prev.pack(side=LEFT)

        read = Button(frame, text='read more', width=16, height=3, command=lambda :self.open_link(self.data['articles'][index]['description']))
        read.pack(side=LEFT)

        if index != len(self.data['articles'])-1:
            next = Button(frame, text='next', width=16, height=3,command=lambda :self.load_news_item(index+1))
            next.pack(side=LEFT)

        self.root.mainloop()

    def open_link(self,url):
        webbrowser.open(url)
        # load 1st news item
        # when ever i start app these three task will be perform
obj = NewsApp()
