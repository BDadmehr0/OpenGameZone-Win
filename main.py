import json
import customtkinter as ctk
import tkinter as tk; from tkinter import simpledialog , filedialog
import os
# import random
import sys
import logging

from PIL import Image, ImageTk

# heding class
class Heding:
    h1 = 65
    h2 = 35
    h3 = 25
    p = 15

    li = '• '
    one = '➊ '
    two = '➋ '
    three = '➌ '
    four = '➍ '
    five = '➎ '
    six = '➏ '
    seven = '➐ '
    eight = '➑ '
    nine = '➒ '

# Polet Color

class color:
    yellow = '#FFBB5C'
    dark_yellow = '#FF9B50'
    red = '#E25E3E'
    dark_red = '#C63D2F'

# Pages

class about_p(ctk.CTkFrame):

    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        self.new_frame_status = False


        # OBJ

        # Menu Top Frame
        self.menu_top_frame = ctk.CTkFrame(self, corner_radius=0)
        self.menu_top_frame.pack(side='top', fill='x', expand=False)

        # Menu Top Frame OBJs

        # APP Logo
        self.image = Image.open("./assets/logo/favicon/opengmaezone-website-favicon-color.png")
        self.image = self.image.resize((64, 64))
        self.photo = ImageTk.PhotoImage(self.image)
        self.logo = ctk.CTkLabel(self.menu_top_frame, image=self.photo, text='', corner_radius=0)
        self.logo.pack(side='left', fill='x', expand=False, padx=5)


        ## about main frame
        
        # scrollable_frame
        self.scrollable_frame = ctk.CTkScrollableFrame(master=self, width=200, height=200, corner_radius=0, fg_color="transparent", label_anchor='w')
        self.scrollable_frame.pack(padx=12, pady=10, expand=True, side='top', fill='both')

        self.lb1A = ctk.CTkLabel(self.scrollable_frame, text='OpenGameZone', font=('bold', Heding.h1))
        self.lb1A.pack(padx=12, pady=20, anchor='n')

        self.image1 = Image.open("./assets/logo/favicon/opengmaezone-website-favicon-color.png")
        self.image1 = self.image.resize((128, 128))
        self.photo1 = ImageTk.PhotoImage(self.image1)
        self.logo1 = ctk.CTkLabel(self.scrollable_frame, image=self.photo1, text='', corner_radius=0)
        self.logo1.pack(padx=12, pady=20, anchor='n')

        # labels README.md
        self.lb1A = ctk.CTkLabel(self.scrollable_frame, text='This project is a Python application built using customtkinter and tkinter libraries, creating a graphical user interface for Linux.', font=('bold', Heding.p))
        self.lb1A.pack(padx=12, anchor='w')

        self.lb1_2A = ctk.CTkLabel(self.scrollable_frame, text='The main goal of this application is to establish a game shop, providing users with the ability to download, install, and play games.', font=('bold', Heding.p))
        self.lb1_2A.pack(padx=12, anchor='w')

        self.lb2A = ctk.CTkLabel(self.scrollable_frame, text='Key Highlights of the Project', font=('bold', Heding.h2))
        self.lb2A.pack(padx=12, pady=20, anchor='w')

        self.lb3A = ctk.CTkLabel(self.scrollable_frame, text=Heding.one+'Open Source', font=('bold', Heding.p))
        self.lb3A.pack(padx=12, anchor='w')
        
        self.lb4A = ctk.CTkLabel(self.scrollable_frame, text=Heding.two+'Graphical Interface', font=('bold', Heding.p))
        self.lb4A.pack(padx=12, anchor='w')

        self.lb5A = ctk.CTkLabel(self.scrollable_frame, text=Heding.three+'Game Centralization', font=('bold', Heding.p))
        self.lb5A.pack(padx=12, anchor='w')

        self.lb6A = ctk.CTkLabel(self.scrollable_frame, text=Heding.four+'Community Support', font=('bold', Heding.p))
        self.lb6A.pack(padx=12, anchor='w')

        self.lb7A = ctk.CTkLabel(self.scrollable_frame, text='Installion & Run', font=('bold', Heding.h2))
        self.lb7A.pack(padx=12,pady=20, anchor='w')

        self.lb8A = ctk.CTkLabel(self.scrollable_frame, text=Heding.one+'[Clone this repository](from https://github.com/BDadmehr0/OpenGameZone-Win)', font=('bold', Heding.p))
        self.lb8A.pack(padx=12, anchor='w')

        self.lb9A = ctk.CTkLabel(self.scrollable_frame, text=Heding.two+'Install required dependencies using "pip install -r requirements.txt"', font=('bold', Heding.p))
        self.lb9A.pack(padx=12, anchor='w')
        
        self.lb10A = ctk.CTkLabel(self.scrollable_frame, text=Heding.three+'Run the application with "python3 main.py"', font=('bold', Heding.p))
        self.lb10A.pack(padx=12, anchor='w')

        self.lb11A = ctk.CTkLabel(self.scrollable_frame, text='License', font=('bold', Heding.h2))
        self.lb11A.pack(padx=12,pady=20, anchor='w')

        self.lb12A = ctk.CTkLabel(self.scrollable_frame, text='This project is licensed under the MIT License - see the [LICENSE](/https://github.com/BDadmehr0/OpenGameZone-Win/blob/main/LICENSE) file for details.', font=('bold', Heding.p))
        self.lb12A.pack(padx=12, anchor='w')

        self.lb13A = ctk.CTkLabel(self.scrollable_frame, text='Made by Dadmehr Emami from Bahlouli School 2', font=('bold', Heding.p))
        self.lb13A.pack(padx=12, anchor='w')
        ## Menu Top Buttons

        self.main_p_btn = ctk.CTkButton(self.menu_top_frame, text='Main', font=('Times New Roman', 35), command=lambda: controller.show_frame(main_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.main_p_btn.pack(side='left', fill='y', expand=False)

        self.library_p_btn = ctk.CTkButton(self.menu_top_frame, text='Library', font=('Times New Roman', 35), command=lambda: controller.show_frame(library_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.library_p_btn.pack(side='left', fill='y', expand=False)

        self.profile_p_btn = ctk.CTkButton(self.menu_top_frame, text='Profile', font=('Times New Roman', 35), command=lambda: controller.show_frame(profile_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.profile_p_btn.pack(side='left', fill='y', expand=False)

        self.about_p_btn = ctk.CTkButton(self.menu_top_frame, text='About', font=('Times New Roman', 35), command=lambda: controller.show_frame(about_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.about_p_btn.pack(side='left', fill='y', expand=False)

        self.exit_btn = ctk.CTkButton(self.menu_top_frame, text='Exit', font=('Times New Roman', 35), command=self.exitf, corner_radius=0, fg_color=color.yellow, hover_color=color.dark_yellow)
        self.exit_btn.pack(side='right', fill='y', expand=False)

        # about main frame

    def exitf(self):
        exit()



## profile
class profile_p_friends(ctk.CTkFrame):

    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        self.new_frame_status = False


        # OBJ

        # Menu Top Frame
        self.menu_top_frame = ctk.CTkFrame(self, corner_radius=0)
        self.menu_top_frame.pack(side='top', fill='x', expand=False)

        # Menu Top Frame OBJs

        # APP Logo
        self.image = Image.open("./assets/logo/favicon/opengmaezone-website-favicon-color.png")
        self.image = self.image.resize((64, 64))
        self.photo = ImageTk.PhotoImage(self.image)
        self.logo = ctk.CTkLabel(self.menu_top_frame, image=self.photo, text='', corner_radius=0)
        self.logo.pack(side='left', fill='x', expand=False, padx=5)

        # Menu Top Buttons

        self.main_p_btn = ctk.CTkButton(self.menu_top_frame, text='Main', font=('Times New Roman', 35), command=lambda: controller.show_frame(main_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.main_p_btn.pack(side='left', fill='y', expand=False)

        self.library_p_btn = ctk.CTkButton(self.menu_top_frame, text='Library', font=('Times New Roman', 35), command=lambda: controller.show_frame(library_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.library_p_btn.pack(side='left', fill='y', expand=False)

        self.profile_p_btn = ctk.CTkButton(self.menu_top_frame, text='Profile', font=('Times New Roman', 35), command=lambda: controller.show_frame(profile_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.profile_p_btn.pack(side='left', fill='y', expand=False)

        self.about_p_btn = ctk.CTkButton(self.menu_top_frame, text='About', font=('Times New Roman', 35), command=lambda: controller.show_frame(about_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.about_p_btn.pack(side='left', fill='y', expand=False)

        self.exit_btn = ctk.CTkButton(self.menu_top_frame, text='Exit', font=('Times New Roman', 35), command=self.exitf, corner_radius=0, fg_color=color.yellow, hover_color=color.dark_yellow)
        self.exit_btn.pack(side='right', fill='y', expand=False)

        # Profile setting menu
        self.menu_left_frame = ctk.CTkFrame(self, corner_radius=0)
        self.menu_left_frame.pack(padx=12, pady=10, side='left', fill='y', expand=False)

        # Profile setting menu OBJs       
        self.button_setting_profile = ctk.CTkButton(self.menu_left_frame, text='Profile', font=('Times New Roman',20), command=lambda: controller.show_frame(profile_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.button_setting_profile.pack(fill='x')

        self.button_setting_firends = ctk.CTkButton(self.menu_left_frame, text='Friends', font=('Times New Roman',20), corner_radius=0, command=lambda: controller.show_frame(profile_p_friends), fg_color=color.red, hover_color=color.dark_red)
        self.button_setting_firends.pack(fill='x')

        self.menu_detials_frame = ctk.CTkScrollableFrame(self, corner_radius=0)
        self.menu_detials_frame.pack(padx=12, pady=10, side='bottom', fill='both', expand=True)



    def exitf(self):
        exit()



class profile_p(ctk.CTkFrame):

    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        self.new_frame_status = False


        # OBJ

        # Menu Top Frame
        self.menu_top_frame = ctk.CTkFrame(self, corner_radius=0)
        self.menu_top_frame.pack(side='top', fill='x', expand=False)

        # Menu Top Frame OBJs

        # APP Logo
        self.image = Image.open("./assets/logo/favicon/opengmaezone-website-favicon-color.png")
        self.image = self.image.resize((64, 64))
        self.photo = ImageTk.PhotoImage(self.image)
        self.logo = ctk.CTkLabel(self.menu_top_frame, image=self.photo, text='', corner_radius=0)
        self.logo.pack(side='left', fill='x', expand=False, padx=5)

        # Menu Top Buttons

        self.main_p_btn = ctk.CTkButton(self.menu_top_frame, text='Main', font=('Times New Roman', 35), command=lambda: controller.show_frame(main_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.main_p_btn.pack(side='left', fill='y', expand=False)

        self.library_p_btn = ctk.CTkButton(self.menu_top_frame, text='Library', font=('Times New Roman', 35), command=lambda: controller.show_frame(library_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.library_p_btn.pack(side='left', fill='y', expand=False)


        self.profile_p_btn = ctk.CTkButton(self.menu_top_frame, text='Profile', font=('Times New Roman', 35), command=lambda: controller.show_frame(profile_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.profile_p_btn.pack(side='left', fill='y', expand=False)

        self.about_p_btn = ctk.CTkButton(self.menu_top_frame, text='About', font=('Times New Roman', 35), command=lambda: controller.show_frame(about_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.about_p_btn.pack(side='left', fill='y', expand=False)

        self.exit_btn = ctk.CTkButton(self.menu_top_frame, text='Exit', font=('Times New Roman', 35), command=self.exitf, corner_radius=0, fg_color=color.yellow, hover_color=color.dark_yellow)
        self.exit_btn.pack(side='right', fill='y', expand=False)

        # Profile setting menu
        self.menu_left_frame = ctk.CTkFrame(self, corner_radius=0)
        self.menu_left_frame.pack(padx=12, pady=10, side='left', fill='y', expand=False)

        # Profile setting menu OBJs
        
        self.button_setting_profile = ctk.CTkButton(self.menu_left_frame, text='Profile', font=('Times New Roman',20), command=lambda: controller.show_frame(profile_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.button_setting_profile.pack(fill='x')


        self.button_setting_firends = ctk.CTkButton(self.menu_left_frame, text='Friends', font=('Times New Roman',20), corner_radius=0, command=lambda: controller.show_frame(profile_p_friends), fg_color=color.red, hover_color=color.dark_red)
        self.button_setting_firends.pack(fill='x')


        # Profile Menu Detials

        self.menu_detials_frame = ctk.CTkFrame(self, corner_radius=0)
        self.menu_detials_frame.pack(padx=12, pady=10, side='bottom', fill='both', expand=True)

        # Profile image
        self.image = Image.open("./assets/profile/user.png")
        self.image = self.image.resize((256, 256))
        self.photo = ImageTk.PhotoImage(self.image)

        self.label = ctk.CTkLabel(self.menu_detials_frame, image=self.photo, text='')
        self.label.place(x=130, y=130)

        # چک کنید آیا فایل JSON وجود دارد یا خیر
        json_file_path = "./data/acc1.json"
        try:
            with open(json_file_path, "r") as json_file:
                profile_data = json.load(json_file)
        except FileNotFoundError:
            profile_data = {
                "username": "Unknown",
                "email": "Unknown",
                "region": "Unknown"
            }

            # اگر فایل وجود نداشته باشد، اطلاعات پروفایل را به فایل JSON اضافه کنید
            with open(json_file_path, "w") as json_file:
                json.dump(profile_data, json_file, indent=4)

        # اضافه کردن دکمه Change
        self.change_btn = ctk.CTkButton(self.menu_detials_frame, text='Change Information', font=('Roboto', 17), command=self.change_profile)
        self.change_btn.place(x=600, y=400)

        self.change_btn_profile = ctk.CTkButton(self.menu_detials_frame, text='Change Profile Image', font=('Roboto', 17), command=self.select_image)
        self.change_btn_profile.place(x=400, y=400)

        # Profile Detail lb
        self.username_lb = ctk.CTkLabel(self.menu_detials_frame, text='Username', font=('Times New Roman', 35))
        self.username_lb.place(x=450, y=130)

        self.username_lb_d = ctk.CTkLabel(self.menu_detials_frame, text='Unknown', font=('Roboto', 17))
        self.username_lb_d.place(x=480, y=180)

        self.mail_lb = ctk.CTkLabel(self.menu_detials_frame, text='Mail', font=('Times New Roman', 35))
        self.mail_lb.place(x=450, y=220)

        self.mail_lb_d = ctk.CTkLabel(self.menu_detials_frame, text='Unknown', font=('Roboto', 17))
        self.mail_lb_d.place(x=480, y=270)

        self.regoin_lb = ctk.CTkLabel(self.menu_detials_frame, text='Regoin', font=('Times New Roman', 35))
        self.regoin_lb.place(x=450, y=310)

        self.regoin_lb_d = ctk.CTkLabel(self.menu_detials_frame, text='Unknown', font=('Roboto', 17))
        self.regoin_lb_d.place(x=480, y=360)

        # اطلاعات از فایل JSON خوانده شده را در label ها نشان دهید
        self.username_lb_d.configure(text=profile_data["username"])
        self.mail_lb_d.configure(text=profile_data["email"])
        self.regoin_lb_d.configure(text=profile_data["region"])

    def select_image(self):
        self.file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
        self.image = Image.open(self.file_path)
        self.image = self.image.resize((256, 256))
        self.photo = ImageTk.PhotoImage(self.image)

        if self.file_path:
            self.label.configure(image=self.photo, text='')
    
    def change_profile(self):
        # نمایش صفحه popup برای گرفتن اطلاعات جدید
        new_username = simpledialog.askstring("Change Username", "Enter new username:")
        new_region = simpledialog.askstring("Change Region", "Enter new region:")
        new_email = simpledialog.askstring("Change Email", "Enter new email:")

        if new_username is not None and new_region is not None and new_email is not None:
            # تغییر اطلاعات در label ها
            self.username_lb_d.configure(text=new_username)
            self.regoin_lb_d.configure(text=new_region)
            self.mail_lb_d.configure(text=new_email)

            # ذخیره اطلاعات جدید در فایل JSON
            json_file_path = "./data/acc1.json"
            try:
                with open(json_file_path, "r") as json_file:
                    profile_data = json.load(json_file)
            except FileNotFoundError:
                profile_data = {
                    "username": "Unknown",
                    "email": "Unknown",
                    "region": "Unknown"
                }

            # تغییر اطلاعات
            profile_data["username"] = new_username
            profile_data["region"] = new_region
            profile_data["email"] = new_email

            # ذخیره اطلاعات در فایل JSON
            with open(json_file_path, "w") as json_file:
                json.dump(profile_data, json_file, indent=4)

        

    def exitf(self):
        exit()


## library
class library_p(ctk.CTkFrame):

    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        self.new_frame_status = False

        # OBJ

        # Menu Top Frame
        self.menu_top_frame = ctk.CTkFrame(self, corner_radius=0)
        self.menu_top_frame.pack(side='top', fill='x', expand=False)

        # Menu Top Frame OBJs

        # APP Logo
        self.image = Image.open("./assets/logo/favicon/opengmaezone-website-favicon-color.png")
        self.image = self.image.resize((64, 64))
        self.photo = ImageTk.PhotoImage(self.image)
        self.logo = ctk.CTkLabel(self.menu_top_frame, image=self.photo, text='', corner_radius=0)
        self.logo.pack(side='left', fill='x', expand=False, padx=5)

        # Menu Top Buttons

        self.main_p_btn = ctk.CTkButton(self.menu_top_frame, text='Main', font=('Times New Roman', 35), command=lambda: controller.show_frame(main_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.main_p_btn.pack(side='left', fill='y', expand=False)

        self.library_p_btn = ctk.CTkButton(self.menu_top_frame, text='Library', font=('Times New Roman', 35), command=lambda: controller.show_frame(library_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.library_p_btn.pack(side='left', fill='y', expand=False)

        self.profile_p_btn = ctk.CTkButton(self.menu_top_frame, text='Profile', font=('Times New Roman', 35), command=lambda: controller.show_frame(profile_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.profile_p_btn.pack(side='left', fill='y', expand=False)

        self.about_p_btn = ctk.CTkButton(self.menu_top_frame, text='About', font=('Times New Roman', 35), command=lambda: controller.show_frame(about_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.about_p_btn.pack(side='left', fill='y', expand=False)

        self.exit_btn = ctk.CTkButton(self.menu_top_frame, text='Exit', font=('Times New Roman', 35), command=self.exitf, corner_radius=0, fg_color=color.yellow, hover_color=color.dark_yellow)
        self.exit_btn.pack(side='right', fill='y', expand=False)

    def exitf(self):
        exit()


## main
class main_p(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        self.new_frame_status = False

        # OBJ

        # Menu Top Frame
        self.menu_top_frame = ctk.CTkFrame(self, corner_radius=0)
        self.menu_top_frame.pack(side='top', fill='x', expand=False)

        # Menu Top Frame OBJs

        # APP Logo
        self.image = Image.open("./assets/logo/favicon/opengmaezone-website-favicon-color.png")
        self.image = self.image.resize((64, 64))
        self.photo = ImageTk.PhotoImage(self.image)
        self.logo = ctk.CTkLabel(self.menu_top_frame, image=self.photo, text='', corner_radius=0)
        self.logo.pack(side='left', fill='x', expand=False, padx=5)

        # Menu Top Buttons

        self.main_p_btn = ctk.CTkButton(self.menu_top_frame, text='Main', font=('Times New Roman', 35), command=lambda: controller.show_frame(main_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.main_p_btn.pack(side='left', fill='y', expand=False)

        self.library_p_btn = ctk.CTkButton(self.menu_top_frame, text='Library', font=('Times New Roman', 35), command=lambda: controller.show_frame(library_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.library_p_btn.pack(side='left', fill='y', expand=False)


        self.profile_p_btn = ctk.CTkButton(self.menu_top_frame, text='Profile', font=('Times New Roman', 35), command=lambda: controller.show_frame(profile_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.profile_p_btn.pack(side='left', fill='y', expand=False)

        self.about_p_btn = ctk.CTkButton(self.menu_top_frame, text='About', font=('Times New Roman', 35), command=lambda: controller.show_frame(about_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.about_p_btn.pack(side='left', fill='y', expand=False)

        self.exit_btn = ctk.CTkButton(self.menu_top_frame, text='Exit', font=('Times New Roman', 35), command=self.exitf, corner_radius=0, fg_color=color.yellow, hover_color=color.dark_yellow)
        self.exit_btn.pack(side='right', fill='y', expand=False)

    def exitf(self):
        exit()

## WelcomePage
class WelcomePage(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Welcome')
        self.geometry('400x300')
        self.resizable(width=False, height=False)

        p1 = tk.PhotoImage(file="./assets/logo/favicon/opengmaezone-website-favicon-color.png")
        self.iconphoto(False, p1)

        self.image = Image.open("./assets/logo/favicon/opengmaezone-website-favicon-color.png")

        self.image = self.image.resize((128, 128))
        self.photo = ImageTk.PhotoImage(self.image)

        self.label = ctk.CTkLabel(self, image=self.photo, text='')
        self.label.pack(pady=20)

        self.welcome_label = ctk.CTkLabel(self, text='Welcome\nOpenGameZone', font=('roboto', 25))
        self.welcome_label.pack()

        self.after(5000, self.close_welcome)

    def close_welcome(self):
        self.destroy()
        self.open_main_app()

    def open_main_app(self):
        app = Frame_ch()
        app.mainloop()

# Frame Changer
class Frame_ch(ctk.CTk):
    def __init__(self):
        ctk.CTk.__init__(self)
        container = ctk.CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.title('OpenGameZone')

        scrollbar = ctk.CTkScrollbar(self)
        value_1, value_2 = scrollbar.get()
        scrollbar.set(value_1, value_2)

        # icon
        p1 = tk.PhotoImage(file="./assets/logo/favicon/opengmaezone-website-favicon-color.png")
        self.iconphoto(False, p1)

        self.frames = {}

        for F in (main_p, library_p, profile_p,
                   profile_p_friends, about_p):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(main_p)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

if __name__ == "__main__":
    # log
    logging.basicConfig(filename='log.log', filemode='w', level=logging.INFO)
    log_file_path = 'log.log'
    log_file = open(log_file_path, 'w')
    sys.stdout = log_file
    sys.stderr = log_file

    # thme
    ctk.set_appearance_mode('dark')

    
    welcome_page = WelcomePage()
    welcome_page.mainloop()
    
    app = Frame_ch()
    app.mainloop()

    log_file.close()
