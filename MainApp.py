import tkinter as tk
from tkinter import ttk
import mysql.connector
from PIL import Image, ImageTk   
from tkcalendar import Calendar
import customtkinter as ct
import random
from PIL import ImageFont
from datetime import datetime


countries_dict = {
    'Baku': 'Баку',
    'Moscow': 'Москва',
    'Istanbul': 'Стамбул',
    'Tbilisi': 'Тбилиси',
    'Kyiv': 'Киев',
    'Minsk': 'Минск',
    'Almaty': 'Алматы',
    'Tokyo': 'Токио',
    'Paris': 'Париж',
    'London': 'Лондон',
    'Berlin': 'Берлин',
    'Rome': 'Рим',
    'Madrid': 'Мадрид',
    'Vienna': 'Вена',
    'Budapest': 'Будапешт',
    'Athens': 'Афины',
    'Amsterdam': 'Амстердам',
    'Brussels': 'Брюссель',
    'Warsaw': 'Варшава',
    'Prague': 'Прага',
    'Copenhagen': 'Копенгаген',
    'Stockholm': 'Стокгольм',
    'Oslo': 'Осло',
    'Lisbon': 'Лиссабон',
    'Helsinki': 'Хельсинки',
    'Kazan': 'Казань',
    'Samara': 'Самара',
    'Ankara': 'Анкара',
    'Antalya': 'Анталья',
    'Batumi': 'Батуми',
    'Kutaisi': 'Кутаиси',
    'Lviv': 'Львов',
    'Odesa': 'Одесса',
    'Dnipro': 'Днепр',
    'Gomel': 'Гомель',
    'Vitebsk': 'Витебск',
    'Brest': 'Брест',
    'Grodno': 'Гродно',
    'Astana': 'Астана',
    'Shymkent': 'Шымкент',
    'Karaganda': 'Караганда',
    'Aktobe': 'Актобе',
    'Seoul': 'Сеул',
    'Beijing': 'Пекин',
    'Shanghai': 'Шанхай',
    'Munich': 'Мюнхен',
    'Frankfurt': 'Франкфурт',
    'Zurich': 'Цюрих',
    'Amsterdam': 'Амстердам',
    'Brussels': 'Брюссель',
    'Warsaw': 'Варшава',
    'Prague': 'Прага',
    'Copenhagen': 'Копенгаген',
    'Stockholm': 'Стокгольм',
    'Oslo': 'Осло',
    'Lisbon': 'Лиссабон',
    'Helsinki': 'Хельсинки'
}

app = ct.CTk()
# TICKERS
avia_ti = {}
hotel_ti = {}
apart_ti ={}
car_ti = {}

app.geometry("1300x800")

avia_pressed= False
bpr = False
go_sck = 0
self_idi = 0
selected_date = 0
canvas = tk.Canvas(app, width=1300, height=750, borderwidth=0, highlightthickness=0, bd=0)

# Рисуем два прямоугольника на Canvas
# Левая часть (первые 300 пикселей по ширине)
left_rectangle = canvas.create_rectangle(0, 0, 1300, 950, fill="#ffffff")
# Правая часть (оставшиеся 300 пикселей по ширине)
right_rectangle = canvas.create_rectangle(0, 0, 1300, 575, fill="#3371f5")

# Размещаем Canvas в окне
canvas.pack(fill=tk.BOTH, expand=True)
# font_path = os.path.join("Fonts", "open-sans-v15-latin_cyrillic-regular.ttf")
# font_path2 = os.path.join("Fonts", "Bitter-VariableFont_wght.ttf")
# app.tk.call('font', 'create', 'customFont', '-family', 'YourFontName', '-size', 16)
# app.tk.call('font', 'create', 'customFont2', '-family', 'YourFontName2', '-size', 16)
# custom_font_2 = ct.CTkFont(family="YourFontName2", size=13)
# custom_font = ct.CTkFont(family="YourFontName", size=12)

font_path = "Fonts/open-sans-v15-latin_cyrillic-regular.ttf"
# Путь к файлу шрифта

# Регистрация шрифта
# Загрузка шрифта с помощью Pillow
# pil_font = ImageFont.truetype(font_path, size=12)
#
# # Создание объекта шрифта tkinter
# font_family_name = pil_font.getname()[0]
# app.tk.call('tk', 'font', 'create', 'CustomFont', '-family', font_family_name)
# custom_font = tkfont.Font(name='CustomFont', exists=True)
pil_font = ImageFont.truetype(font_path, size=12)

# Создаем объект шрифта tkinter
custom_font = ct.CTkFont(family=pil_font.getname()[0], size=14)

# Регистрация шрифта в tkinter
app.tk.call('font', 'create', 'CustomFont', '-family', pil_font.getname()[0], '-size', 12)



avia_frames = {}
avia_frames_counter = 1

avia_tickets_frames = {}
avia_tickets_frames_counter = 1


hotel_frames = {}
hotel_frames_counter = 1
hotel_tickets_frames = {}
hotel_tickets_frames_counter = 1



apart_frames = {}
apart_frames_counter = 1
apart_tickets_frames = {}
apart_tickets_frames_counter = 1

car_frames = {}
car_frames_counter =1

# Генератор корзины
bag_cont = {}
bag_cont_counter = 1



# Стилизация Entry
style = ttk.Style()
style.theme_use('clam')  # выбираем тему
style.configure('Custom.TEntry', background='#008000', borderwidth=0, fieldbackground='#FFFFFF',
                foreground='gray', relief='flat', width=5,height=8, padding=(5, 5))

new_style = ttk.Style()
new_style.configure('CustomRed.TEntry',bordercolor='#E97d41', background='#E97d41',highlightthickness=0, borderwidth=0, fieldbackground='#FFFFFF',
                foreground='black', relief='flat', padding=(5, 5))



def open_calendar(label1):
    top = tk.Toplevel(app)
    top.title("Календарь")

    cal = Calendar(top, selectmode='day', year=2024, month=5, day=12)
    cal.pack(padx=10, pady=10)

    def on_date_select(label):
        global selected_date
        selected_date = cal.get_date()
        label.configure(text="Выбранная дата: " + selected_date)
        top.destroy()

    button_select = ct.CTkButton(top, text="Выбрать", hover_color="#Ff5c00", fg_color="#Da560a"
                                  , border_spacing=8, text_color='white', corner_radius=15
                                  , height=15, font=('Verdana', 20), command=lambda label = label1: on_date_select(label=label1))
    button_select.pack(pady=10)

def open_calendar_2(event, label2):
    top = tk.Toplevel(app)
    top.title("Календарь")

    cal = Calendar(top, selectmode='day', year=2024, month=5, day=12)
    cal.pack(padx=10, pady=10)

    def on_date_select(label):
        selected_date = cal.get_date()
        label.configure(text="Выбранная дата: " + selected_date)
        top.destroy()

    button_select = ttk.Button(top, text="Выбрать", command=lambda label=label2: on_date_select(label=label2))
    button_select.pack(pady=10)


def sql_conn(querry):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="09070500",
        database="travelDB"
    )

    mycursor = mydb.cursor()

    # выбирает дату из базы
    mycursor.execute(querry)
    abc = mycursor.fetchall()
    mydb.commit()
    mydb.close()
    return abc
def avia_butt():
    global avia_frames, avia_frames_counter
    if not avia_frames.get(avia_frames_counter) and not hotel_frames.get(hotel_frames_counter) and not car_frames.get(car_frames_counter) and not apart_frames.get(apart_frames_counter):
        pass
    elif car_frames.get(car_frames_counter):
        if not car_ti.get(0):
            pass
        else:
            car_ti[0].pack_forget()
            del car_ti[0]
        canvas.itemconfig(right_rectangle, fill="#3371f5")
        frame.configure(fg_color="#3371f5", bg_color="#3371f5")
        und_frame.configure(fg_color="#3371f5", bg_color="#3371f5")
        button2.configure(fg_color="#2f67de",hover_color="#3e71dc")
        button3.configure(fg_color="#2f67de",hover_color="#3e71dc")
        button4.configure(fg_color="#2f67de", bg_color="#3371f5",hover_color="#3e71dc")
        button5.configure(fg_color="#2f67de", bg_color="#3371f5",hover_color="#3e71dc")
        main_l.configure(fg_color="#3371f5", text="Авиабилеты по самым выгодным ценам! ")
        main_l2.configure(fg_color="#3371f5", text="скидки до 60%")
        button4.configure(fg_color="#2f67de", hover_color="#3e71dc", image=wicon_image2, text_color="#C5d5f5")
        car_frames[car_frames_counter - 1].pack_forget()
        car_frames[car_frames_counter].pack_forget()
        del car_frames[car_frames_counter - 1]
        del car_frames[car_frames_counter]


    elif apart_frames.get(apart_frames_counter):

        if not apart_ti.get(0):

            pass

        else:

            apart_ti[0].pack_forget()

            del apart_ti[0]

        button3.configure(fg_color="#2f67de", hover_color="#3e71dc", image=wicon_image4, text_color="#C5d5f5")

        apart_frames[apart_frames_counter - 1].pack_forget()

        apart_frames[apart_frames_counter].pack_forget()

        del apart_frames[apart_frames_counter - 1]

        del apart_frames[apart_frames_counter]

    elif hotel_frames.get(hotel_frames_counter):
        if not hotel_ti.get(0):
            pass
        else:
            hotel_ti[0].pack_forget()
            del hotel_ti[0]
        button2.configure(fg_color="#2f67de", hover_color="#3e71dc", image=wicon_image1, text_color="#C5d5f5")
        hotel_frames[hotel_frames_counter - 1].pack_forget()
        hotel_frames[hotel_frames_counter].pack_forget()
        del hotel_frames[hotel_frames_counter - 1]
        del hotel_frames[hotel_frames_counter]

    else:
        avia_frames[avia_frames_counter - 1].pack_forget()
        avia_frames[avia_frames_counter].pack_forget()
        del avia_frames[avia_frames_counter - 1]
        del avia_frames[avia_frames_counter]
    def act_button():
        #cчетчик
        if not avia_ti.get(0):
            pass
        else:
            avia_ti[0].pack_forget()
            del avia_ti[0]
        t2 = avia_to_entry.get()
        new_date = str(0) + selected_date
        date_str = new_date
        date_obj = datetime.strptime(date_str, '%m/%d/%y')
        formatted_date_str = date_obj.strftime('%Y-%m-%d')
        print(formatted_date_str, t2)
        querry = f"select * from aviatickets where to_country = '{t2}' and Date(travel_date) LIKE '{formatted_date_str}';"
        def creating_new_frame():

            global avia_tickets_frames, avia_tickets_frames_counter, avia_ti
            main_l.pack_forget()
            main_l2.pack_forget()
            avia_ticket_inner_frame = ct.CTkFrame(canvas, fg_color="#e6f7ff", width=1050, height=300)
            avia_ticket_inner_frame.pack_propagate(False)
            avia_ti[0] = avia_ticket_inner_frame
            main_label = ct.CTkLabel(avia_ticket_inner_frame, text="Самые дешёвые билеты", font=("Helvetica", 30),
                                     text_color="black")
            if not avia_to_entry.get():
                querry2 = "SELECT * FROM aviatickets WHERE travel_date >= DATE_SUB(CURDATE(), INTERVAL 2 DAY) AND travel_date < CURDATE() + INTERVAL 1 DAY;"
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="09070500",
                    database="travelDB")
                mycursor = mydb.cursor()

                # выбирает дату из базы
                mycursor.execute(querry2)
                rows = mycursor.fetchall()
                for row in rows:
                    abc = row[3].hour

                    print(row)
                    avia_ticket_frame = ct.CTkFrame(avia_ticket_inner_frame, width=300, height=300, corner_radius=18,
                                                    bg_color="#e6f7ff", fg_color="white")
                    avia_ticket_frame.pack_propagate()
                    price_label = ct.CTkLabel(avia_ticket_frame, text=f"{random.randint(450, 850)} ₼",
                                              text_color="black",
                                              font=("Helvetica-bold", 22))
                    inner_grid_frame = ct.CTkFrame(avia_ticket_frame, fg_color="white", bg_color="white")
                    # azal_logo = ct.CTkButton(avia_ticket_frame, width=50, height=50, text="", image=ImageTk.PhotoImage(Image.open("icons/azal_logo.png").resize((50, 50), Image.LANCZOS))
                    #                       , fg_color='white',
                    #                       hover_color='white')

                    cal_butt = ct.CTkButton(inner_grid_frame, width=32, height=32, text="", image=ImageTk.PhotoImage(
                        Image.open(f"Calendar_icons/mycollection/png/{row[3].day}.png"))
                                            , fg_color='white',
                                            hover_color='white')
                    country_code = ct.CTkFrame(inner_grid_frame, fg_color="white", bg_color="white")
                    time_rand = random.randint(5, 9)
                    time_text = ct.CTkLabel(country_code, text=f"{row[3].hour}:00 - {row[3].hour + time_rand}:55",
                                            font=("Helvetica", 14), text_color="black")
                    gyd = ct.CTkLabel(country_code, text=f"GYD    {row[5]}", text_color="#a0a9b6", font=("Helvetica", 14))

                    text_to_fly = ct.CTkFrame(inner_grid_frame, fg_color="white", bg_color="white")
                    time_to_text = ct.CTkLabel(text_to_fly, text=f"{time_rand}ч в пути в {row[2]}/ 1 пересадка",
                                               font=("Helvetica", 14),
                                               text_color="black")
                    time_to_text_2 = ct.CTkLabel(text_to_fly, text=f"{round(time_rand / 2)}ч в {row[4]}",
                                                 text_color="#a0a9b6",
                                                 font=("Helvetica", 14))

                    avia_ticket_inner_frame.pack()
                    main_label.pack(anchor="w", padx=(15, 0), pady=15)
                    avia_ticket_frame.pack(side=tk.LEFT, padx=15, pady=30)
                    price_label.grid(row=0, column=0, padx=15, pady=5, sticky="w")
                    inner_grid_frame.grid(row=1, column=0, pady=15)
                    inner_grid_frame.columnconfigure(0, pad=10)  # Отступ между столбцом 0 и столбцом 1
                    inner_grid_frame.columnconfigure(1, pad=10)
                    inner_grid_frame.columnconfigure(2, pad=10)

                    cal_butt.grid(row=0, column=0)
                    country_code.grid(row=0, column=1)
                    text_to_fly.grid(row=0, column=2)
                    time_to_text.grid(row=0, column=0)
                    time_to_text_2.grid(row=1, column=0)
                    time_text.grid(row=0, column=0)
                    gyd.grid(row=1, column=0)

                mydb.commit()
                mydb.close()
            else:
                abc = sql_conn(querry)
                time_from = (abc[0][3]).hour
                avia_ticket_frame = ct.CTkFrame(avia_ticket_inner_frame, width=300, height=300, corner_radius=18,
                                                bg_color="#e6f7ff", fg_color="white")
                avia_ticket_frame.pack_propagate()
                price_label = ct.CTkLabel(avia_ticket_frame, text=f"{random.randint(450, 850)} ₼", text_color="black",
                                          font=("Helvetica-bold", 22))
                inner_grid_frame = ct.CTkFrame(avia_ticket_frame, fg_color="white", bg_color="white")
                # azal_logo = ct.CTkButton(avia_ticket_frame, width=50, height=50, text="", image=ImageTk.PhotoImage(Image.open("icons/azal_logo.png").resize((50, 50), Image.LANCZOS))
                #                       , fg_color='white',
                #                       hover_color='white')

                cal_butt = ct.CTkButton(inner_grid_frame, width=32, height=32, text="", image=ImageTk.PhotoImage(
                    Image.open(f"Calendar_icons/mycollection/png/{abc[0][3].day}.png"))
                                        , fg_color='white',
                                        hover_color='white')
                country_code = ct.CTkFrame(inner_grid_frame, fg_color="white", bg_color="white")
                time_rand = random.randint(5, 9)
                time_text = ct.CTkLabel(country_code, text=f"{time_from}:00 - {time_from + time_rand}:55",
                                        font=("Helvetica", 14), text_color="black")
                gyd = ct.CTkLabel(country_code, text=f"GYD    {abc[0][5]}", text_color="#a0a9b6", font=("Helvetica", 14))

                text_to_fly = ct.CTkFrame(inner_grid_frame, fg_color="white", bg_color="white")
                time_to_text = ct.CTkLabel(text_to_fly, text=f"{time_rand}ч в пути в {abc[0][2]}/ 1 пересадка",
                                           font=("Helvetica", 14),
                                           text_color="black")
                time_to_text_2 = ct.CTkLabel(text_to_fly, text=f"{round(time_rand / 2)}ч в {abc[0][4]}", text_color="#a0a9b6",
                                             font=("Helvetica", 14))
                avia_ticket_inner_frame.pack()
                main_label.pack(anchor="w", padx=(15, 0), pady=5)
                avia_ticket_frame.pack(anchor="w", padx=15, pady=30)
                price_label.grid(row=0, column=0, padx=15, pady=5, sticky="w")
                # azal_logo.grid(row=0,column=0, sticky="e")
                inner_grid_frame.grid(row=1, column=0, pady=15)
                inner_grid_frame.columnconfigure(0, pad=10)  # Отступ между столбцом 0 и столбцом 1
                inner_grid_frame.columnconfigure(1, pad=10)
                inner_grid_frame.columnconfigure(2, pad=10)

                cal_butt.grid(row=0, column=0)
                country_code.grid(row=0, column=1)
                text_to_fly.grid(row=0, column=2)
                time_to_text.grid(row=0, column=0)
                time_to_text_2.grid(row=1, column=0)
                time_text.grid(row=0, column=0)
                gyd.grid(row=1, column=0)
            # avia_tickets_frames[avia_tickets_frames_counter] += avia_ticket_inner_frame
            # avia_tickets_frames_counter+=1

        creating_new_frame()



    button1.configure(fg_color="#ffffff", hover_color="#ffffff", image=icon_image, text_color="black")
    avia_frame = ct.CTkFrame(master=canvas, fg_color="#FFFFFF", corner_radius=5)
    avia_from_entry = ct.CTkEntry(avia_frame,placeholder_text="Баку", corner_radius=5,border_width=0,fg_color="#ffffff",text_color="black",  font=('Helvetica', 16))
    avia_to_entry = ct.CTkEntry(avia_frame, placeholder_text="Куда?",border_width=0,fg_color="#ffffff",text_color="black", font=('Helvetica', 16))

    frame_time = ct.CTkFrame(avia_frame, width=800, height=100, fg_color='white')

    # Создаем метку (Label)
    label_time1 = ct.CTkLabel(frame_time, text="Когда", fg_color='white', text_color='gray', font=('Helvetica', 16))
    # label2.grid(row=0, column=0, pady=10,padx=(20,0), sticky="w")  # "sticky" выравнивает метку по левому краю
    label_time1.pack(side="left", padx=(10, 80))

    # Создаем кнопку (Button)
    button = ct.CTkButton(frame_time, width=15, height=15, text="", image=icon_image_cal, fg_color='white',
                          hover_color='white', command=lambda label1=label_time1: open_calendar(label1=label_time1))
    # button.grid(row=0, column=5, pady=10, padx=(0, 20), sticky="e")
    button.pack(side='right', padx=(80, 0))

    frame_time_back = ct.CTkFrame(avia_frame, width=800, height=100, fg_color='white')

    # Создаем метку (Label)
    label_time2 = ct.CTkLabel(frame_time_back, text="Обратно", fg_color='white', text_color='gray',
                              font=('Helvetica', 16))
    # label2.grid(row=0, column=0, pady=10,padx=(20,0), sticky="w")  # "sticky" выравнивает метку по левому краю
    label_time2.pack(side="left", padx=(60, 120))



    avia_from_entry.grid(row=0, column=0, ipadx=23, ipady=17)
    avia_to_entry.grid(row=0, column=1, ipadx=23, ipady=17)
    # avia_time_entry.grid(row=0, column=2, ipadx=23, ipady=17)
    # outer_button.grid(row=0, column=2,padx=20, pady=10, ipadx=23, ipady=17)
    frame_time.grid(row=0, column=2)
    frame_time_back.grid(row=0, column=3)
    avia_frame.pack()

    frame_time_back.bind("<Button-1>", lambda event, label2=label_time2: open_calendar_2(event, label2=label_time2))
    label_time2.bind("<Button-1>", lambda event, label2=label_time2: open_calendar_2(event, label2=label_time2))

    confirm_button = ct.CTkButton(canvas, text="Найти билеты", hover_color="#Ff5c00",bg_color="#3371f5", fg_color="#Da560a"
                                  , border_spacing=15, text_color='white', corner_radius=15
                                  , height=55, font=('Verdana', 20), command= act_button)
    confirm_button.pack(pady=55, ipadx=25, ipady=8)

    # ad_frame.place(relx=0.5, rely=1, anchor=tk.S)

    avia_frames[avia_frames_counter - 1] = avia_frame
    avia_frames[avia_frames_counter] = confirm_button

avia_frames_counter+=2

def hotel_butt():
    global hotel_frames, hotel_frames_counter
    if not hotel_frames.get(hotel_frames_counter) and not avia_frames.get(avia_frames_counter) and not apart_frames.get(apart_frames_counter) and not car_frames.get(car_frames_counter):
        pass
    elif car_frames.get(car_frames_counter):
        if not car_ti.get(0):
            pass
        else:
            car_ti[0].pack_forget()
            del car_ti[0]
        canvas.itemconfig(right_rectangle, fill="#3371f5")
        frame.configure(fg_color="#3371f5", bg_color="#3371f5")
        und_frame.configure(fg_color="#3371f5", bg_color="#3371f5")
        button1.configure(fg_color="#2f67de", hover_color="#3e71dc")
        button3.configure(fg_color="#2f67de", hover_color="#3e71dc")
        button4.configure(fg_color="#2f67de", bg_color="#3371f5", hover_color="#3e71dc")
        button5.configure(fg_color="#2f67de", bg_color="#3371f5", hover_color="#3e71dc")
        main_l.configure(fg_color="#3371f5", text="Отели в любой точке мира")
        main_l2.configure(fg_color="#3371f5", text="P.S (паспорт не требуется)")
        button4.configure(fg_color="#2f67de", hover_color="#3e71dc", image=wicon_image2, text_color="#C5d5f5")
        car_frames[car_frames_counter - 1].pack_forget()
        car_frames[car_frames_counter].pack_forget()
        del car_frames[car_frames_counter - 1]
        del car_frames[car_frames_counter]

    elif avia_frames.get(avia_frames_counter):
        if not avia_ti.get(0):
            pass
        else:
            avia_ti[0].pack_forget()
            del avia_ti[0]
        main_l.configure(fg_color="#3371f5", text="Отели в любой точке мира")
        main_l2.configure(fg_color="#3371f5", text="P.S (паспорт не требуется)")
        button1.configure(fg_color="#2f67de", hover_color="#3e71dc", image=wicon_image, text_color="#C5d5f5")
        avia_frames[avia_frames_counter - 1].pack_forget()
        avia_frames[avia_frames_counter].pack_forget()
        del avia_frames[avia_frames_counter - 1]
        del avia_frames[avia_frames_counter]
    elif apart_frames.get(apart_frames_counter):
        if not apart_ti.get(0):
            pass
        else:
            apart_ti[0].pack_forget()
            del apart_ti[0]
        main_l.configure(fg_color="#3371f5", text="Отели в любой точке мира")
        main_l2.configure(fg_color="#3371f5", text="P.S (паспорт не требуется)")
        button3.configure(fg_color="#2f67de", hover_color="#3e71dc", image=wicon_image4, text_color="#C5d5f5")
        apart_frames[apart_frames_counter - 1].pack_forget()
        apart_frames[apart_frames_counter].pack_forget()
        del apart_frames[apart_frames_counter - 1]
        del apart_frames[apart_frames_counter]

    else:
        hotel_frames[hotel_frames_counter - 1].pack_forget()
        hotel_frames[hotel_frames_counter].pack_forget()
        del hotel_frames[hotel_frames_counter - 1]
        del hotel_frames[hotel_frames_counter]

    def act_button():
        # cчетчик
        if not hotel_ti.get(0):
            pass
        else:
            hotel_ti[0].pack_forget()
            del hotel_ti[0]
        t2 = country_hotel_entry.get()
        new_date = str(0) + selected_date
        date_str = new_date
        date_obj = datetime.strptime(date_str, '%m/%d/%y')
        formatted_date_str = date_obj.strftime('%Y-%m-%d')
        print(formatted_date_str, t2)
        querry = f"select * from hotels where country = '{t2}' and Date(stay_date) LIKE '{formatted_date_str}';"

        def creating_new_frame():
            global  hotel_ti
            main_l.pack_forget()
            main_l2.pack_forget()
            hotel_ticket_inner_frame = ct.CTkFrame(canvas, fg_color="#e6f7ff", width=1250, height=500)
            hotel_ticket_inner_frame.pack_propagate(False)
            hotel_ti[0] = hotel_ticket_inner_frame
            main_label = ct.CTkLabel(hotel_ticket_inner_frame, text="Топ отели по вкусным ценам!", font=("Helvetica", 30),
                                     text_color="black")
            if not country_hotel_entry.get():
                querry2 = "SELECT * FROM hotels WHERE stay_date >= DATE_SUB(CURDATE(), INTERVAL 4 DAY) AND stay_date < CURDATE() + INTERVAL 3 DAY;"
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="09070500",
                    database="travelDB")
                mycursor = mydb.cursor()

                # выбирает дату из базы
                mycursor.execute(querry2)
                rows = mycursor.fetchall()
                for row in rows:
                    abc = row[3].hour
                    price_calc = random.randint(450, 850)
                    n = 5
                    print(row)
                    hotel_ticket_frame = ct.CTkFrame(hotel_ticket_inner_frame, width=340, height=450, corner_radius=18,
                                                    bg_color="#e6f7ff", fg_color="white")
                    hotel_ticket_frame.pack_propagate()

                    # Загрузка изображения
                    icon_image12 = ImageTk.PhotoImage(
                    Image.open(f"Hotels_pics/{row[0]}.png").resize((340, 260), Image.LANCZOS))

                    # Фрейм для изображения и текста
                    image_frame = ct.CTkFrame(hotel_ticket_frame, width=icon_image.width(),bg_color="#e6f7ff", height=icon_image.height())

                    button121 = ct.CTkButton(image_frame, image=icon_image12, text="",bg_color="white",hover_color="white", fg_color="white")
                    inner_grid_frame = ct.CTkFrame(hotel_ticket_frame, fg_color="white", bg_color="white")
                    price_label1 = ct.CTkLabel(inner_grid_frame, text=f"{price_calc} ₼", text_color="black", font=("Helvetica", 18))
                    hotel_info = ct.CTkLabel(inner_grid_frame, text=f' {row[2]}  {row[4]*"★"}{(5-row[4])*"☆"}', text_color="black", font=("Helvetica", 18))


                    hotel_ticket_inner_frame.pack()
                    hotel_ticket_frame.pack(side=tk.LEFT, padx=15, pady=30, ipady=10)
                    image_frame.pack(side=tk.TOP)
                    button121.pack()
                    inner_grid_frame.pack(side=tk.BOTTOM)
                    inner_grid_frame.rowconfigure(0, pad=10)  # Отступ между столбцом 0 и столбцом 1
                    inner_grid_frame.rowconfigure(1, pad=10)
                    price_label1.grid(row=0, column=0, sticky="w")
                    hotel_info.grid(row=1,column=0)

                    # img_frame.pack()

                mydb.commit()
                mydb.close()
            else:
                abc = sql_conn(querry)
                print(abc)


                hotel_ticket_frame = ct.CTkFrame(hotel_ticket_inner_frame, width=340, height=450, corner_radius=18,
                                                 bg_color="#e6f7ff", fg_color="white")
                hotel_ticket_frame.pack_propagate()

                # Загрузка изображения
                icon_image12 = ImageTk.PhotoImage(
                    Image.open(f"Hotels_pics/1.png").resize((340, 260), Image.LANCZOS))

                # Фрейм для изображения и текста
                image_frame = tk.Frame(hotel_ticket_frame, width=icon_image.width(), height=icon_image.height())

                button121 = ct.CTkButton(image_frame, image=icon_image12, text="", hover_color="white",
                                         fg_color="white")
                inner_grid_frame = ct.CTkFrame(hotel_ticket_frame, fg_color="white", bg_color="white")
                price_calc = random.randint(450, 850)
                n = 5
                price_label1 = ct.CTkLabel(inner_grid_frame, text=f"{price_calc} ₼", text_color="black",
                                           font=("Helvetica", 18))
                hotel_info = ct.CTkLabel(inner_grid_frame, text=f' {abc[0][2]}  {abc[0][4] * "★"}{(5 - abc[0][4]) * "☆"}',
                                         text_color="black", font=("Helvetica", 18))

                hotel_ticket_inner_frame.pack()
                hotel_ticket_frame.pack(side=tk.LEFT, padx=15, pady=30, ipady=10)
                image_frame.pack(side=tk.TOP)
                button121.pack()
                inner_grid_frame.pack(side=tk.BOTTOM)
                inner_grid_frame.rowconfigure(0, pad=10)  # Отступ между столбцом 0 и столбцом 1
                inner_grid_frame.rowconfigure(1, pad=10)
                price_label1.grid(row=0, column=0, sticky="w")
                hotel_info.grid(row=1, column=0)
            # avia_tickets_frames[avia_tickets_frames_counter] += avia_ticket_inner_frame
            # avia_tickets_frames_counter+=1

        creating_new_frame()
    button2.configure(fg_color="#ffffff", hover_color="#ffffff", image=icon_image1, text_color="black")
    hotel_frame = ct.CTkFrame(master=canvas, fg_color="#FFFFFF",bg_color="#3371f5")
    country_hotel_entry = ct.CTkEntry(hotel_frame,placeholder_text="Город или Отель", corner_radius=5,border_width=0,fg_color="#ffffff",text_color="black", font=('Helvetica', 16))
    frame_time_hotel = ct.CTkFrame(hotel_frame, width=800, height=100, fg_color='white')

    label_time1_hotel = ct.CTkLabel(frame_time_hotel, text="Дата Заезда", fg_color='white', text_color='gray',
                                    font=('Helvetica', 16))
    label_time1_hotel.pack(side="left", padx=(10, 80))

    # Создаем кнопку (Button)
    button_hotel = ct.CTkButton(frame_time_hotel, width=15, height=15, text="", image=icon_image_cal,
                                fg_color='white',
                                hover_color='white', command=lambda label1=label_time1_hotel: open_calendar(label1))
    # button.grid(row=0, column=5, pady=10, padx=(0, 20), sticky="e")
    button_hotel.pack(side='right', padx=(80, 0))

    frame_time_back_hotel = ct.CTkFrame(hotel_frame, width=800, height=100, fg_color='white')

    label_time2_hotel = ct.CTkLabel(frame_time_back_hotel, text="Дата выезда", fg_color='white', text_color='gray',
                                    font=('Helvetica', 16))
    label_time2_hotel.pack(side="left", padx=(60, 120))



    country_hotel_entry.grid(row=0, column=0, ipadx=23, ipady=17)
    frame_time_hotel.grid(row=0, column=1, ipadx=23, ipady=17)
    frame_time_back_hotel.grid(row=0, column=2)
    hotel_frame.pack()

    frame_time_back_hotel.bind("<Button-1>", lambda event, label2=label_time2_hotel: open_calendar_2(event, label2))
    label_time2_hotel.bind("<Button-1>", lambda event, label2=label_time2_hotel: open_calendar_2(event, label2))

    confirm_button_hotel = ct.CTkButton(canvas, text="Найти отели", hover_color="#Ff5c00",bg_color="#3371f5", fg_color="#Da560a"
                                        , border_spacing=15, text_color='white', corner_radius=15
                                        , height=55, font=('Verdana', 20), command=act_button)
    confirm_button_hotel.pack(pady=55, ipadx=25, ipady=8)

    hotel_frames[hotel_frames_counter - 1] = hotel_frame
    hotel_frames[hotel_frames_counter] = confirm_button_hotel


hotel_frames_counter +=2

def apart_butt():
    global apart_frames, apart_frames_counter, car_ti
    if not apart_frames.get(apart_frames_counter) and not hotel_frames.get(hotel_frames_counter) and not avia_frames.get(avia_frames_counter) and not car_frames.get(car_frames_counter):
        pass
    elif car_frames.get(car_frames_counter):
        if not car_ti.get(0):
            pass
        else:
            car_ti[0].pack_forget()
            del car_ti[0]
        canvas.itemconfig(right_rectangle, fill="#3371f5")
        frame.configure(fg_color="#3371f5", bg_color="#3371f5")
        und_frame.configure(fg_color="#3371f5", bg_color="#3371f5")
        button2.configure(fg_color="#2f67de", hover_color="#3e71dc")
        button1.configure(fg_color="#2f67de", hover_color="#3e71dc")
        button4.configure(fg_color="#2f67de", bg_color="#3371f5", hover_color="#3e71dc")
        button5.configure(fg_color="#2f67de", bg_color="#3371f5", hover_color="#3e71dc")
        main_l.configure(fg_color="#3371f5", text="Апартаменты на любой вкус и цвет")
        main_l2.configure(fg_color="#3371f5", text="даже вилла Янаковича")
        button4.configure(fg_color="#2f67de", hover_color="#3e71dc", image=wicon_image2, text_color="#C5d5f5")
        car_frames[car_frames_counter - 1].pack_forget()
        car_frames[car_frames_counter].pack_forget()
        del car_frames[car_frames_counter - 1]
        del car_frames[car_frames_counter]
    elif hotel_frames.get(hotel_frames_counter):
        if not hotel_ti.get(0):
            pass
        else:
            hotel_ti[0].pack_forget()
            del hotel_ti[0]
        main_l.configure(fg_color="#3371f5", text="Апартаменты на любой вкус и цвет")
        main_l2.configure(fg_color="#3371f5", text="даже вилла Янаковича")
        button2.configure(fg_color="#2f67de", hover_color="#3e71dc", image=wicon_image1, text_color="#C5d5f5")
        hotel_frames[hotel_frames_counter - 1].pack_forget()
        hotel_frames[hotel_frames_counter].pack_forget()
        del hotel_frames[hotel_frames_counter - 1]
        del hotel_frames[hotel_frames_counter]
    elif avia_frames.get(avia_frames_counter):
        if not avia_ti.get(0):
            pass
        else:
            avia_ti[0].pack_forget()
            del avia_ti[0]
        main_l.configure(fg_color="#3371f5", text="Апартаменты на любой вкус и цвет")
        main_l2.configure(fg_color="#3371f5", text="даже вилла Янаковича")
        button1.configure(fg_color="#2f67de", hover_color="#3e71dc", image=wicon_image, text_color="#C5d5f5")
        avia_frames[avia_frames_counter - 1].pack_forget()
        avia_frames[avia_frames_counter].pack_forget()
        del avia_frames[avia_frames_counter - 1]
        del avia_frames[avia_frames_counter]

    else:
        apart_frames[apart_frames_counter-1].pack_forget()
        apart_frames[apart_frames_counter].pack_forget()
        del apart_frames[apart_frames_counter-1]
        del apart_frames[apart_frames_counter]

    def act_button():
        if not apart_ti.get(0):
            pass
        else:
            apart_ti[0].pack_forget()
            del apart_ti[0]
        # cчетчик
        t2 = country_hotel_entry.get()
        new_date = str(0) + selected_date
        date_str = new_date
        date_obj = datetime.strptime(date_str, '%m/%d/%y')
        formatted_date_str = date_obj.strftime('%Y-%m-%d')
        print(formatted_date_str, t2)
        querry = f"select * from hotels where country = '{t2}' and Date(stay_date) LIKE '{formatted_date_str}';"

        def creating_new_frame():
            global  apart_ti
            main_l.pack_forget()
            main_l2.pack_forget()
            hotel_ticket_inner_frame = ct.CTkFrame(canvas, fg_color="#e6f7ff", width=1250, height=500)
            hotel_ticket_inner_frame.pack_propagate(False)
            apart_ti[0] = hotel_ticket_inner_frame
            main_label = ct.CTkLabel(hotel_ticket_inner_frame, text="Топ отели по вкусным ценам!", font=("Helvetica", 30),
                                     text_color="black")
            if not country_hotel_entry.get():
                querry2 = "SELECT * FROM hotels WHERE stay_date >= DATE_SUB(CURDATE(), INTERVAL 4 DAY) AND stay_date < CURDATE() + INTERVAL 3 DAY;"
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="09070500",
                    database="travelDB")
                mycursor = mydb.cursor()

                # выбирает дату из базы
                mycursor.execute(querry2)
                rows = mycursor.fetchall()
                for row in rows:
                    abc = row[3].hour
                    price_calc = random.randint(450, 850)
                    n = 5
                    print(row)
                    hotel_ticket_frame = ct.CTkFrame(hotel_ticket_inner_frame, width=340, height=450, corner_radius=18,
                                                    bg_color="#e6f7ff", fg_color="white")
                    hotel_ticket_frame.pack_propagate()

                    # Загрузка изображения
                    icon_image12 = ImageTk.PhotoImage(
                    Image.open(f"Hotels_pics/{row[0]}.png").resize((340, 260), Image.LANCZOS))

                    # Фрейм для изображения и текста
                    image_frame = ct.CTkFrame(hotel_ticket_frame, width=icon_image.width(),bg_color="#e6f7ff", height=icon_image.height())

                    button121 = ct.CTkButton(image_frame, image=icon_image12, text="",bg_color="white",hover_color="white", fg_color="white")
                    inner_grid_frame = ct.CTkFrame(hotel_ticket_frame, fg_color="white", bg_color="white")
                    price_label1 = ct.CTkLabel(inner_grid_frame, text=f"{price_calc} ₼", text_color="black", font=("Helvetica", 18))
                    hotel_info = ct.CTkLabel(inner_grid_frame, text=f' {row[2]}  {row[4]*"★"}{(5-row[4])*"☆"}', text_color="black", font=("Helvetica", 18))


                    hotel_ticket_inner_frame.pack()
                    hotel_ticket_frame.pack(side=tk.LEFT, padx=15, pady=30, ipady=10)
                    image_frame.pack(side=tk.TOP)
                    button121.pack()
                    inner_grid_frame.pack(side=tk.BOTTOM)
                    inner_grid_frame.rowconfigure(0, pad=10)  # Отступ между столбцом 0 и столбцом 1
                    inner_grid_frame.rowconfigure(1, pad=10)
                    price_label1.grid(row=0, column=0, sticky="w")
                    hotel_info.grid(row=1,column=0)

                    # img_frame.pack()

                mydb.commit()
                mydb.close()
            else:
                abc = sql_conn(querry)
                print(abc)


                hotel_ticket_frame = ct.CTkFrame(hotel_ticket_inner_frame, width=340, height=450, corner_radius=18,
                                                 bg_color="#e6f7ff", fg_color="white")
                hotel_ticket_frame.pack_propagate()

                # Загрузка изображения
                icon_image12 = ImageTk.PhotoImage(
                    Image.open(f"Hotels_pics/1.png").resize((340, 260), Image.LANCZOS))

                # Фрейм для изображения и текста
                image_frame = tk.Frame(hotel_ticket_frame, width=icon_image.width(), height=icon_image.height())

                button121 = ct.CTkButton(image_frame, image=icon_image12, text="", hover_color="white",
                                         fg_color="white")
                inner_grid_frame = ct.CTkFrame(hotel_ticket_frame, fg_color="white", bg_color="white")
                price_calc = random.randint(450, 850)
                n = 5
                price_label1 = ct.CTkLabel(inner_grid_frame, text=f"{price_calc} ₼", text_color="black",
                                           font=("Helvetica", 18))
                hotel_info = ct.CTkLabel(inner_grid_frame, text=f' {abc[0][2]}  {abc[0][4] * "★"}{(5 - abc[0][4]) * "☆"}',
                                         text_color="black", font=("Helvetica", 18))

                hotel_ticket_inner_frame.pack()
                hotel_ticket_frame.pack(side=tk.LEFT, padx=15, pady=30, ipady=10)
                image_frame.pack(side=tk.TOP)
                button121.pack()
                inner_grid_frame.pack(side=tk.BOTTOM)
                inner_grid_frame.rowconfigure(0, pad=10)  # Отступ между столбцом 0 и столбцом 1
                inner_grid_frame.rowconfigure(1, pad=10)
                price_label1.grid(row=0, column=0, sticky="w")
                hotel_info.grid(row=1, column=0)

        creating_new_frame()

    button3.configure(fg_color="#ffffff", hover_color="#ffffff", image=icon_image4, text_color="black")
    apart_frame = ct.CTkFrame(master=canvas, fg_color="#FFFFFF")
    country_hotel_entry = ct.CTkEntry(apart_frame,placeholder_text="Город или Апартаменты", corner_radius=5,border_width=0,fg_color="#ffffff",text_color="black", font=('Helvetica', 16))
    frame_time_hotel = ct.CTkFrame(apart_frame, width=800, height=100, fg_color='white')

    label_time1_hotel = ct.CTkLabel(frame_time_hotel, text="Дата Заезда", fg_color='white', text_color='gray',
                                    font=('Helvetica', 16))
    label_time1_hotel.pack(side="left", padx=(10, 80))

    # Создаем кнопку (Button)
    button_hotel = ct.CTkButton(frame_time_hotel, width=15, height=15, text="", image=icon_image_cal,
                                fg_color='white',
                                hover_color='white', command=lambda label1=label_time1_hotel: open_calendar(label1))
    # button.grid(row=0, column=5, pady=10, padx=(0, 20), sticky="e")
    button_hotel.pack(side='right', padx=(80, 0))

    frame_time_back_hotel = ct.CTkFrame(apart_frame, width=800, height=100, fg_color='white')

    label_time2_hotel = ct.CTkLabel(frame_time_back_hotel, text="Дата выезда", fg_color='white', text_color='gray',
                                    font=('Helvetica', 16))
    label_time2_hotel.pack(side="left", padx=(60, 120))


    country_hotel_entry.grid(row=0, column=0, ipadx=23, ipady=17)
    frame_time_hotel.grid(row=0, column=1, ipadx=23, ipady=17)
    frame_time_back_hotel.grid(row=0, column=2)
    apart_frame.pack()

    frame_time_back_hotel.bind("<Button-1>", lambda event, label2=label_time2_hotel: open_calendar_2(event, label2))
    label_time2_hotel.bind("<Button-1>", lambda event, label2=label_time2_hotel: open_calendar_2(event, label2))

    confirm_button_appart = ct.CTkButton(canvas, text="Найти апартаменты", hover_color="#Ff5c00",bg_color="#3371f5", fg_color="#Da560a"
                                        , border_spacing=15, text_color='white', corner_radius=15
                                        , height=55, font=('Verdana', 20), command = act_button)
    confirm_button_appart.pack(pady=55, ipadx=25, ipady=8)

    apart_frames[apart_frames_counter - 1] = apart_frame
    apart_frames[apart_frames_counter] = confirm_button_appart

apart_frames_counter += 2


def car_butt():
    global car_ti
    if not apart_frames.get(apart_frames_counter) and not hotel_frames.get(
            hotel_frames_counter) and not avia_frames.get(avia_frames_counter) and not car_frames.get(car_frames_counter):
        pass

    elif hotel_frames.get(hotel_frames_counter):
        if not hotel_ti.get(0):
            pass
        else:
            hotel_ti[0].pack_forget()
            del hotel_ti[0]
        button2.configure(fg_color="#2f67de", hover_color="#3e71dc", image=wicon_image1, text_color="#C5d5f5")
        hotel_frames[hotel_frames_counter - 1].pack_forget()
        hotel_frames[hotel_frames_counter].pack_forget()
        del hotel_frames[hotel_frames_counter - 1]
        del hotel_frames[hotel_frames_counter]
    elif avia_frames.get(avia_frames_counter):
        if not avia_ti.get(0):
            pass
        else:
            avia_ti[0].pack_forget()
            del avia_ti[0]
        button1.configure(fg_color="#2f67de", hover_color="#3e71dc", image=wicon_image, text_color="#C5d5f5")
        avia_frames[avia_frames_counter - 1].pack_forget()
        avia_frames[avia_frames_counter].pack_forget()
        del avia_frames[avia_frames_counter - 1]
        del avia_frames[avia_frames_counter]
    elif apart_frames.get(apart_frames_counter):
        if not apart_ti.get(0):
            pass
        else:
            apart_ti[0].pack_forget()
            del apart_ti[0]
        button3.configure(fg_color="#2f67de", hover_color="#3e71dc", image=wicon_image4, text_color="#C5d5f5")
        apart_frames[apart_frames_counter - 1].pack_forget()
        apart_frames[apart_frames_counter].pack_forget()
        del apart_frames[apart_frames_counter - 1]
        del apart_frames[apart_frames_counter]
    else:
        if not car_ti.get(0):
            pass
        else:
            car_ti[0].pack_forget()
            del car_ti[0]
        car_frames[car_frames_counter - 1].pack_forget()
        car_frames[car_frames_counter].pack_forget()
        del car_frames[car_frames_counter - 1]
        del car_frames[car_frames_counter]
    def act_button():
        # cчетчик
        t2 = car_entry.get()
        querry = f"select * from carsharing where car_model = '{t2}';"
        classes_dict = {"Эконом": "economy", "Комфорт": "standard", "Представительский": "premium"}
        def creating_new_frame():
            global  car_ti
            if not car_ti.get(0):
                pass
            else:
                car_ti[0].pack_forget()
                del car_ti[0]
            main_l.pack_forget()
            main_l2.pack_forget()
            car_ticket_inner_frame = ct.CTkFrame(canvas, fg_color="#e6f7ff", width=1300, height=500)
            car_ticket_inner_frame.pack_propagate(False)
            car_ti[0] = car_ticket_inner_frame
            main_label = ct.CTkLabel(car_ticket_inner_frame, text="Топ отели по вкусным ценам!", font=("Helvetica", 30),
                                     text_color="black")
            if not car_entry.get():
                querry2 = f"SELECT * FROM carsharing WHERE car_class = '{classes_dict[dropdown.get()]}'"
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="09070500",
                    database="travelDB")
                mycursor = mydb.cursor()

                # выбирает дату из базы
                mycursor.execute(querry2)
                rows = mycursor.fetchall()
                for row in rows:
                    print(row)
                    car_ticket_frame = ct.CTkFrame(car_ticket_inner_frame, width=340, height=450, corner_radius=18,
                                                    bg_color="#e6f7ff", fg_color="white")
                    car_ticket_frame.pack_propagate()

                    # Фрейм для изображения и текста
                    image_frame = ct.CTkFrame(car_ticket_frame, width=icon_image.width(),bg_color="#e6f7ff", height=icon_image.height())
                    image = Image.open(f"Cars/{row[0]}.png").resize((360, 215), Image.LANCZOS)
                    image_ctk = ct.CTkImage(image, size=(360, 215))
                    button121 = ct.CTkButton(image_frame, image=image_ctk, text="",bg_color="white",hover_color="white", fg_color="white")
                    inner_grid_frame = ct.CTkFrame(car_ticket_frame, fg_color="white", bg_color="white")
                    price_label1 = ct.CTkLabel(inner_grid_frame, text=f"за {row[7]}₼ в час {row[1]}", text_color="black", font=("Helvetica", 18))
                    hotel_info = ct.CTkLabel(inner_grid_frame, text=f' Гос.номер: {row[2]}   Класс: {dropdown.get()}', text_color="black", font=("Helvetica", 17))
                    hotel_info2 = ct.CTkLabel(inner_grid_frame,
                                             text=f'Расположение: {row[3]}   Статус: {row[9]}',
                                             text_color="black", font=("Helvetica", 17))

                    car_ticket_inner_frame.pack()
                    car_ticket_frame.pack(side=tk.LEFT, padx=15, pady=30, ipady=10)
                    image_frame.pack(side=tk.TOP)
                    button121.pack()
                    inner_grid_frame.pack(side=tk.BOTTOM)
                    inner_grid_frame.rowconfigure(0, pad=10)  # Отступ между столбцом 0 и столбцом 1
                    inner_grid_frame.rowconfigure(1, pad=10)
                    price_label1.grid(row=0, column=0, sticky="w")
                    hotel_info.grid(row=2,column=0, sticky="w")
                    hotel_info2.grid(row=1,column=0, sticky="w")
                    # img_frame.pack()

                mydb.commit()
                mydb.close()
            else:
                abc = sql_conn(querry)
                print(abc)
                car_ticket_frame = ct.CTkFrame(car_ticket_inner_frame, width=340, height=450, corner_radius=18,
                                               bg_color="#e6f7ff", fg_color="white")
                car_ticket_frame.pack_propagate()

                # Фрейм для изображения и текста
                image_frame = ct.CTkFrame(car_ticket_frame, width=icon_image.width(), bg_color="#e6f7ff",
                                          height=icon_image.height())
                image = Image.open(f"Cars/{abc[0][0]}.png").resize((360, 215), Image.LANCZOS)
                image_ctk = ct.CTkImage(image, size=(360, 215))
                button121 = ct.CTkButton(image_frame, image=image_ctk, text="", bg_color="white", hover_color="white",
                                         fg_color="white")
                inner_grid_frame = ct.CTkFrame(car_ticket_frame, fg_color="white", bg_color="white")
                price_label1 = ct.CTkLabel(inner_grid_frame, text=f"За {abc[0][7]}₼ в час {abc[0][1]}", text_color="black",
                                           font=("Helvetica", 18))
                hotel_info = ct.CTkLabel(inner_grid_frame, text=f' Гос.номер: {abc[0][2]}   Класс: {dropdown.get()}',
                                         text_color="black", font=("Helvetica", 16))
                hotel_info2 = ct.CTkLabel(inner_grid_frame,
                                          text=f'Расположение: {abc[0][3]}   Статус: {abc[0][9]}',
                                          text_color="black", font=("Helvetica", 16))

                car_ticket_inner_frame.pack()
                car_ticket_frame.pack(side=tk.LEFT, padx=15, pady=30, ipady=10)
                image_frame.pack(side=tk.TOP)
                button121.pack()
                inner_grid_frame.pack(side=tk.BOTTOM)
                inner_grid_frame.rowconfigure(0, pad=10)  # Отступ между столбцом 0 и столбцом 1
                inner_grid_frame.rowconfigure(1, pad=10)
                price_label1.grid(row=0, column=0, sticky="w")
                hotel_info.grid(row=2, column=0, sticky="w")
                hotel_info2.grid(row=1, column=0, sticky="w")

        creating_new_frame()
    button4.configure(fg_color="#ffffff", hover_color="#ffffff", image=icon_image2, text_color="black")
    canvas.itemconfig(right_rectangle, fill="#6dba6a")
    frame.configure(fg_color="#6dba6a", bg_color="#6dba6a")
    und_frame.configure(fg_color="#5AAB5D", bg_color="#5AAB5D")
    button1.configure(fg_color="#5AAB5D", hover_color="#45ca49")
    button2.configure(fg_color="#5AAB5D", hover_color="#45ca49")
    button3.configure(fg_color="#5AAB5D", hover_color="#45ca49")
    button4.configure(fg_color="#ffffff", bg_color="#5AAB5D", hover_color="#ffffff")
    button5.configure(fg_color="#5AAB5D", bg_color="#6dba6a", hover_color="#45ca49")
    main_l.configure(fg_color="#6dba6a", text="Теперь и аренда машин ")
    main_l2.configure(fg_color="#6dba6a", text="(попробуй скорее!) ")


    car_frame = ct.CTkFrame(master=canvas, fg_color="#FFFFFF", corner_radius=8, bg_color="#6dba6a")
    car_entry = ct.CTkEntry(car_frame, placeholder_text="Марка машины",placeholder_text_color="black", corner_radius=8,
                                      border_width=0, fg_color="#ffffff", text_color="black", font=('Helvetica', 16))
    selected_option = ct.StringVar(value="Выберите класс машины")  # Установка начального значения

    # Список вариантов
    options = ["Эконом", "Комфорт", "Представительский"]

    # Создание выпадающего меню
    dropdown = ct.CTkOptionMenu(car_frame, values=options, variable=selected_option, font=("Helvetica",16), fg_color="white", text_color="black"
                                , button_color="white", button_hover_color="#3C7E3F"
                                ,bg_color="white", dropdown_hover_color="white")


    car_entry.grid(row=0, column=0, padx=10, ipadx=23, ipady=17)
    dropdown.grid(row=0, column=1, padx=(25,25))
    car_frame.pack(ipadx=5)
    confirm_button_car = ct.CTkButton(canvas, text="Найти машину", hover_color="#Ff5c00", bg_color="#6dba6a",
                                         fg_color="#Da560a"
                                         , border_spacing=15, text_color='white', corner_radius=15
                                         , height=55, font=('Verdana', 20),command=act_button )
    confirm_button_car.pack(pady=55, ipadx=25, ipady=8)

    car_frames[car_frames_counter - 1] = car_frame
    car_frames[car_frames_counter] = confirm_button_car


car_frames_counter += 2

def bag_butt():
    button5.configure(fg_color="#437cf6", hover_color="#4c82f6", image=wicon_image5, text_color="white")
    top = tk.Toplevel(app)
    top.title("Корзина")
    top.geometry('300x500')
    top.configure(fg_color = "green")

    main_frame = ct.CTkFrame(top, fg_color="white")
    label = ct.CTkLabel(top,  fg_color="white", text="")
    main_label = ct.CTkLabel(main_frame, text = "Корзина пока пуста,ну ка заполните ее! ")
    main_frame.pack()
    label.pack()
    main_label.grid(row=0,column=0)






## Черные иконки
icon_image = ImageTk.PhotoImage(Image.open("icons/plane.png").resize((30, 30), Image.LANCZOS))
icon_image1 = ImageTk.PhotoImage(Image.open("icons/bed.png").resize((25, 25), Image.LANCZOS))
icon_image2 = ImageTk.PhotoImage(Image.open("icons/car.png").resize((25, 25), Image.LANCZOS))
icon_image4 = ImageTk.PhotoImage(Image.open("icons/key.png").resize((25, 25), Image.LANCZOS))
icon_image5 = ImageTk.PhotoImage(Image.open("icons/bag.png").resize((25, 25), Image.LANCZOS))
icon_image_cal=ImageTk.PhotoImage(Image.open("icons/calendar.png").resize((25, 25), Image.LANCZOS))

## Белые иконки
wicon_image = ImageTk.PhotoImage(Image.open("icons/wplane.png").resize((25, 25), Image.LANCZOS))
wicon_image1 = ImageTk.PhotoImage(Image.open("icons/wbed.png").resize((25, 25), Image.LANCZOS))
wicon_image2 = ImageTk.PhotoImage(Image.open("icons/wcar.png").resize((25, 25), Image.LANCZOS))
wicon_image4 = ImageTk.PhotoImage(Image.open("icons/wkey.png").resize((25, 25), Image.LANCZOS))
wicon_image5 = ImageTk.PhotoImage(Image.open("icons/wbag.png").resize((25, 25), Image.LANCZOS))


app.configure(fg_color="#3371f5")
cal = Calendar(app, selectmode="day", year=2020, month=5, day=22)
text_az = "Ucuz aviabiletlərin axtarışı"
main_l = ct.CTkLabel(canvas, text="Поиск дешёвых авиабилетов",text_color="white",fg_color="#3371f5", font=("Helvetica bold", 36))
main_l2 = ct.CTkLabel(canvas, text="16 лет помогаем вам экономить",text_color="white",fg_color="#3371f5", font=("Helvetica", 20))

frame = ct.CTkFrame(master=canvas, width=200, height=200, corner_radius=45, bg_color="#3371f5", fg_color="#3371f5")
und_frame = ct.CTkFrame(frame,fg_color="#2f67de")
button1 = ct.CTkButton(und_frame, text="Авиабилет",fg_color="#2f67de",font=custom_font,hover_color="#3e71dc",border_color="#2f67de",corner_radius=10, image=wicon_image, compound=tk.TOP, command=avia_butt)
button2 = ct.CTkButton(und_frame, text="Отель",fg_color="#2f67de",font=custom_font,hover_color="#3e71dc", image=wicon_image1, compound=tk.TOP, command=hotel_butt)
button3 = ct.CTkButton(und_frame, text="Апартаменты",fg_color="#2f67de",font=custom_font,hover_color="#3e71dc", image=wicon_image4, compound=tk.TOP, command=apart_butt)
button4 = ct.CTkButton(und_frame, text="Аренда Машин",fg_color="#2f67de",font=custom_font,hover_color="#3e71dc", image=wicon_image2, compound=tk.TOP, command=car_butt)
button5 = ct.CTkButton(frame,width=102, text="Корзина",fg_color="#437cf6",font=custom_font,text_color="#C5d5f5",hover_color="#4c82f6",corner_radius=13, image=wicon_image5, compound=tk.TOP, command=bag_butt)



main_l.pack(pady=15)
main_l2.pack()
frame.pack( pady=25)
und_frame.grid_rowconfigure(0, weight=1)
und_frame.grid_columnconfigure(0, weight=1)
und_frame.grid(row=0,column=0, padx=(0,15))
button1.grid(row=0, column=0,ipady=3 )
button2.grid(row=0, column=1, ipady=3)
button3.grid(row=0, column=2, ipady=3)
button4.grid(row=0, column=3, ipady=3)
button5.grid(row=0, column=1, ipady=3)

# ad_frame = ct.CTkFrame(app, corner_radius=22, fg_color="white", height=390, width=390)
# bg_image = ImageTk.PhotoImage(Image.open("bakcground_img/ad_bg_final.png").resize((390, 390), Image.LANCZOS))
# label11 = ct.CTkLabel(ad_frame, text='', image = bg_image)
# label11.place(x = 10, y = 10)

# ad_frame.place(relx=0.5, rely=1, anchor=tk.S)
# ad_frame.pack(pady=50)
avia_butt()
app.mainloop()

