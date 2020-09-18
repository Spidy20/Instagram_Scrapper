from PIL import ImageTk
import PIL.Image
from tkinter import *
import tkinter as tk
import requests,webbrowser
import io
from bs4 import BeautifulSoup
from urllib.request import urlopen

windo = Tk()
windo.configure(background='white')
windo.title("Instagram Scrapper")

windo.geometry('1120x520')
windo.iconbitmap('./meta/insta.ico')
windo.resizable(0, 0)


def search():
    try:
        global im5,un
        un = str(txt2.get())
        res = requests.get('https://www.instagram.com/' + un)
        s_data = BeautifulSoup(res.text, 'html.parser')

        ## Fetch DP in system
        insta_dp = s_data.find("meta", property="og:image")
        dp_url = insta_dp.attrs['content']

        u = urlopen(dp_url)
        raw_data = u.read()
        im5 = PIL.Image.open(io.BytesIO(raw_data))
        im5 = im5.resize((150, 150), PIL.Image.ANTIALIAS)


        ## Fetch Info
        ui = s_data.find("meta", property="og:description")
        cont = ui.attrs['content'][:40]
        cont = cont.split(' ')
        follower = cont[0]
        follower = follower.replace('m', 'M')
        following = cont[2]
        # following = int(following.replace(',', ''))
        posts = cont[4]
        followers1 = str(follower)+" Followers"
        following1 = str(following)+" Following"
        posts1 = str(posts)+" Posts"
        followers_label.config(text=followers1)
        following_label.config(text=following1)
        posts_label.config(text=posts1)

        ## Show DP
        image = ImageTk.PhotoImage(im5)
        panel5 = Button(windo,image = image, command = check_link,borderwidth=0)
        panel5.image = image
        panel5.pack()
        panel5.place(x=885, y=90)

        im7 = PIL.Image.open('./meta/download.png')
        im7 = im7.resize((40, 40), PIL.Image.ANTIALIAS)
        sp_img7 = ImageTk.PhotoImage(im7)
        panel8 = Button(windo, borderwidth=0,command=download_dp, image=sp_img7, bg='white')
        panel8.image=sp_img7
        panel8.pack()
        panel8.place(x=940, y=245)


    except Exception as e:
        print(e)
        lab1 = tk.Label(windo, text="ID not found!", width=20, height=1, fg="white", bg="firebrick1",
                        font=('times', 14, ' bold '))
        lab1.place(x=400, y=250)
        windo.after(4000, destroy_widget, lab1)

def check_link():
    link = 'https://www.instagram.com/' + un
    webbrowser.open_new_tab(link)

def clear():
    txt2.delete(first=0,last=100)


def download_dp():
    im5.save(un+'.jpg')
    lab1 = tk.Label(windo, text="Picture Downloaded!", width=20, height=1, fg="black", bg="gold",
                    font=('times', 14, ' bold '))
    lab1.place(x=400, y=250)
    windo.after(4000, destroy_widget,lab1 )

def destroy_widget(widget):
    widget.destroy()

im = PIL.Image.open('./meta/ig.png')
im = im.resize((200, 200), PIL.Image.ANTIALIAS)
wp_img = ImageTk.PhotoImage(im)
panel4 = Label(windo, image=wp_img, bg='white')
panel4.pack()
panel4.place(x=50, y=70)

im1 = PIL.Image.open('./meta/search.png')
im1 = im1.resize((40, 40), PIL.Image.ANTIALIAS)
sp_img = ImageTk.PhotoImage(im1)
panel5 = Button(windo, borderwidth=0, image=sp_img,command=search, bg='white')
panel5.pack()
panel5.place(x=750, y=175)

im2 = PIL.Image.open('./meta/eraser.png')
im2 = im2.resize((40, 40), PIL.Image.ANTIALIAS)
sp_img1 = ImageTk.PhotoImage(im2)
panel6 = Button(windo, borderwidth=0,command=clear, image=sp_img1, bg='white')
panel6.pack()
panel6.place(x=810, y=175)


pred = tk.Label(windo, text="Instragram Profile Scrapper", width=30, height=2, fg="white", bg="maroon2",
                font=('times', 25, ' bold '))
pred.place(x=274, y=10)

lab = tk.Label(windo, text="Enter your ID", width=18, height=1, fg="white", bg="blue2",
               font=('times', 16, ' bold '))
lab.place(x=394, y=120)

txt2 = tk.Entry(windo, borderwidth=7, width=26, bg="white", fg="black", font=('times', 25, ' bold '))
txt2.place(x=280, y=170)

followers_label = tk.Label(windo, text='Followers', width=17, height=2, fg="white", bg="maroon2",
                           font=('times', 18, ' bold '))
followers_label.place(x=200, y=300)

following_label = tk.Label(windo, text="Following", width=17, height=2, fg="black", bg="spring green",
                           font=('times', 18, ' bold '))
following_label.place(x=470, y=300)

posts_label = tk.Label(windo, text="Posts", width=17, height=2, fg="white", bg="dark violet",
                       font=('times', 18, ' bold '))
posts_label.place(x=740, y=300)


windo.mainloop()