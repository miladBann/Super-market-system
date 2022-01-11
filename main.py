from tkinter import *
from tkinter import messagebox
import tkinter
import json
import datetime
import time
import eel
from threading import Thread

import items
from twilio.rest import Client
from num2words import num2words


BLACK = "#562c2c"
ORANGE = "#f2542d"
WHITE = "#f5dfbb"
LIGHT_BLUE = "#0e9594"
DARK_BLUE = "#127475"
Yellow = "#fff44f"
payment_num = 0
payment_num2 = 0
item_lista = []
item_regular_price_lista = []
item_end_price_lista = []


auth_key = "36a9c902b942e22b60e5589432b8cc95"
acc_sid = "AC65bad8d2579e711ed04969b7e99f976a"


name = None
kopa_num = None
calc = ""
new_list = []
first_value = 0
second_value = 0
num = 1
cost = 0
item_count = 0
mass = 0
paid = None
worker_index = None


def display():
    global name, calc

    name_entry.destroy()
    id_entry.destroy()
    log_in_btn.destroy()
    kopa_entry.destroy()

    window.attributes('-fullscreen', True)
    window.config(padx=0, pady=0, background=WHITE)

    def close():
        window.destroy()

    close_btn = Button(window, text="❌", font=(
        "Arial", 18, "bold"), command=close)
    close_btn.place(x=1480, y=0)

    ################left hand side################################################
    price_label = Label(text="Price          ", font=(
        "Arial", 22, "bold"), height=2, bg=WHITE)
    price_label.place(x=0, y=810)

    items_Count_label = Label(text="items count", font=(
        "Arial", 22, "bold"), borderwidth=3, relief="solid", height=2, bg=WHITE)
    items_Count_label.place(x=160, y=810)

    product_label = Entry(text="product description", font=(
        "Arial", 40, "bold"), borderwidth=3, relief="solid", width=14, bg=WHITE)
    product_label.place(x=0, y=0)

    mass_label = Label(text="Mass", font=("Arial", 22, "bold"),
                       borderwidth=3, relief="solid", height=2, width=5, bg=WHITE)
    mass_label.place(x=401, y=0)

    status_label = Label(text="status", font=(
        "Arial", 22, "bold"), borderwidth=3, relief="solid", height=2, bg=WHITE)
    status_label.place(x=490, y=0)

    #############################right hand side#########################################
    name_label = Label(text="Name:    ", font=(
        "Arial", 22, "bold"),  bg=WHITE)
    name_label.place(x=600, y=0)

    date_label = Label(text="Date:      ", font=("Arial", 22, "bold"),
                       bg=WHITE)
    date_label.place(x=600, y=50)

    time_label = Label(text="Time:      ", font=(
        "Arial", 22, "bold"),  bg=WHITE)
    time_label.place(x=600, y=100)

    real_name = Label(text=name, font=("Arial", 22, "bold"),
                      bg=WHITE)
    real_name.place(x=1200, y=0)

    now = datetime.datetime.now().date()
    real_date = Label(text=now, font=("Arial", 22, "bold"), bg=WHITE)
    real_date.place(x=1200, y=50)

    def getTime():
        string = time.strftime('%H:%M:%S %p')
        real_time.config(text=string)
        real_time.after(1000, getTime)

    real_time = Label(text="time", font=("Arial", 22, "bold"), bg=WHITE)
    real_time.place(x=1200, y=100)

    getTime()

    kopa_in_use = Label(text=f"{kopa_num}", font=(
        "Arial", 66, "bold"), bg=WHITE)
    kopa_in_use.place(x=950, y=20)

    ######################Down right side 1#################################################
    space = Label(text="____________________________________________________________________________________", font=(
        "Arial", 20, "bold"), background=WHITE)
    space.place(x=500, y=145)

    ###########################################################################################################################################

    def add():
        messagebox.showinfo(
            title="Insert user info", message="make sure to add the user id before adding items")

        def add_more():
            item_mass_entry.delete(0, END)
            item_code_entry.delete(0, END)
            item_name_entry.delete(0, END)
            item_specific_price_entry.delete(0, END)
            item_general_price_entry.delete(0, END)

        def add_item():
            global cost, item_count, item_lista, item_regular_price_lista, item_end_price_lista

            name = item_name_entry.get()
            code = item_code_entry.get()
            general_price = item_general_price_entry.get()
            price = item_specific_price_entry.get()
            mass = item_mass_entry.get()

            # spacing system

            name_space = 20 - len(name)
            final_str = name + (" " * name_space)

            mass_space = 16 - len(mass)
            final_mass = mass + (" " * mass_space)

            general_price_space = 14 - len(general_price)
            final_general_price = general_price + (" " * general_price_space)

            # spacing system
            new_str = f"{final_str}{final_mass}{final_general_price}{price}"

            item_lista.append(name)
            item_regular_price_lista.append(general_price)
            item_end_price_lista.append(price)

            lista.insert(END, new_str)
            lista.insert(
                END, "___________________________________________________________________")

            item_count += 1
            items_Count_label.config(text=item_count)

            cost += round(float(price), 2)
            price_label.config(text=cost)

            mass_label.config(text=mass)

            status_label.config(text="✅")

        window2 = tkinter.Toplevel(window)
        window2.title("Add Items")
        window2.minsize(width=700, height=600)
        window2.config(padx=20, pady=20, bg=DARK_BLUE)

        title = Label(window2, text="Add items to the list", font=(
            "Arial", 22, "bold"), bg=DARK_BLUE)
        title.place(x=180, y=0)

        # labels
        item_name_label = Label(window2, text="item:", font=(
            "Arial", 22, "bold"), bg=DARK_BLUE)
        item_name_label.place(x=0, y=80)

        item_mass_label = Label(window2, text="mass:", font=(
            "Arial", 22, "bold"), bg=DARK_BLUE)
        item_mass_label.place(x=0, y=160)

        item_general_price_label = Label(window2, text="price/kg:", font=(
            "Arial", 22, "bold"), bg=DARK_BLUE)
        item_general_price_label.place(x=0, y=240)

        item_code_label = Label(window2, text="code:", font=(
            "Arial", 22, "bold"), bg=DARK_BLUE)
        item_code_label.place(x=0, y=320)

        item_specific_price_label = Label(
            window2, text="price:", font=("Arial", 22, "bold"), bg=DARK_BLUE)
        item_specific_price_label.place(x=0, y=400)

        # entries
        item_name_entry = Entry(window2, font=("Arial", 22, "bold"), width=24)
        item_name_entry.place(x=150, y=80)

        item_mass_entry = Entry(window2, font=("Arial", 22, "bold"), width=24)
        item_mass_entry.place(x=150, y=160)

        item_general_price_entry = Entry(
            window2, font=("Arial", 22, "bold"), width=24)
        item_general_price_entry.place(x=150, y=240)

        item_code_entry = Entry(window2, font=("Arial", 22, "bold"), width=24)
        item_code_entry.place(x=150, y=320)

        item_specific_price_entry = Entry(
            window2, font=("Arial", 22, "bold"), width=24)
        item_specific_price_entry.place(x=150, y=400)

        # buttons
        add_item_btn = Button(window2, text="Add Item", font=(
            "Arial", 22, "bold"), width=12, command=add_item)
        add_item_btn.place(x=100, y=470)

        add_more_btn = Button(window2, text="Add new", font=(
            "Arial", 22, "bold"), width=12, command=add_more)
        add_more_btn.place(x=360, y=470)

        window.mainloop()

    add_items = Button(text="Add Items", font=("Arial", 22, "bold"),
                       height=4, width=12, borderwidth=3, relief="solid", bg=LIGHT_BLUE, command=add)
    add_items.place(x=600, y=180)

    ###########################################################################################################################################
    def info():
        window2 = tkinter.Toplevel(window)
        window2.title("Item Information")
        window2.minsize(width=900, height=500)
        window2.config(padx=20, pady=20, bg=WHITE)

        title = Label(window2, text="Item Info",
                      font=("Arial", 22, "bold"), bg=WHITE)
        title.place(x=0, y=0)

        line_break = Label(window2, text="______________________________________________________", font=(
            "Arial", 22, "bold"), bg=WHITE)
        line_break.place(x=0, y=40)

        item_name_label = Label(window2, text="Item Name:", font=(
            "Arial", 22, "bold"), bg=WHITE)
        item_name_label.place(x=0, y=120)

        item_price_per_kg_label = Label(window2,
                                        text="Price/kg or piece:", font=("Arial", 22, "bold"), bg=WHITE)
        item_price_per_kg_label.place(x=0, y=220)

        item_code_label = Label(window2, text="Item Code:", font=(
            "Arial", 22, "bold"), bg=WHITE)
        item_code_label.place(x=0, y=320)

        item_sale_label = Label(window2, text="Sales:",
                                font=("Arial", 22, "bold"), bg=WHITE)
        item_sale_label.place(x=0, y=420)

        search_code_entry = Entry(
            window2, font=("Arial", 22, "bold"), width=15)
        search_code_entry.place(x=570, y=160)

        search_info_by_name_entry = Entry(
            window2, font=("Arial", 22, "bold"), width=15)
        search_info_by_name_entry.place(x=570, y=260)

        item_name = Label(window2, text="......", font=(
            "Arial", 22, "bold"), bg=WHITE)
        item_name.place(x=190, y=120)

        item_price = Label(window2, text="......",
                           font=("Arial", 22, "bold"), bg=WHITE)
        item_price.place(x=270, y=220)

        item_code = Label(window2, text="......", font=(
            "Arial", 22, "bold"), bg=WHITE)
        item_code.place(x=180, y=320)

        item_sale = Label(window2, text="......", font=(
            "Arial", 22, "bold"), bg=WHITE)
        item_sale.place(x=110, y=420)

        ########################################

        def search_by_code():
            item = int(search_code_entry.get())

            item_code_result = items.items[item]["code"]
            item_name_result = items.items[item]["name"]
            item_price_result = items.items[item]["price/kg"]
            item_sale_result = items.items[item]["sale"]

            item_code.config(text=item_code_result)
            item_name.config(text=item_name_result)
            item_sale.config(text=item_sale_result)
            item_price.config(text=item_price_result)

        def search_by_name():
            item_name_value = search_info_by_name_entry.get()

            for item in items.items:
                if items.items[item]["name"] == item_name_value:
                    item_code_result = items.items[item]["code"]
                    item_name_result = items.items[item]["name"]
                    item_price_result = items.items[item]["price/kg"]
                    item_sale_result = items.items[item]["sale"]

                    item_code.config(text=item_code_result)
                    item_name.config(text=item_name_result)
                    item_sale.config(text=item_sale_result)
                    item_price.config(text=item_price_result)

        def add_item_to_list():
            code_value = int(search_code_entry.get())
            name_value = search_info_by_name_entry.get()

            if code_value:
                item_name_to_add = items.items[code_value]["name"]
                item_code_to_add = items.items[code_value]["code"]
                item_general_price_to_add = items.items[code_value]["price/kg"]

                window3 = tkinter.Toplevel(window2)
                window3.title("Enter Mass")
                window3.config(padx=20, pady=20, bg=WHITE)
                window3.minsize(width=300, height=170)

                title_win = Label(window3, text="Enter Mass",
                                  font=("Arial", 22, "bold"), bg=WHITE)
                title_win.place(x=0, y=0)

                entry_mass = Entry(window3, font=("Arial", 18, "bold"))
                entry_mass.place(x=0, y=50)

                def get_mass():
                    global mass, item_count, cost
                    mass = entry_mass.get()

                    # spacing system

                    name_space = 20 - len(item_name_to_add)
                    final_str = item_name_to_add + (" " * name_space)

                    mass_space = 16 - len(str(mass))
                    final_mass = str(mass) + (" " * mass_space)

                    general_price_space = 14 - \
                        len(str(item_general_price_to_add))
                    final_general_price = str(item_general_price_to_add) + \
                        (" " * general_price_space)

                    price = float(item_general_price_to_add) * \
                        float(mass)
                    # spacing system

                    new_str2 = f"{final_str}{final_mass}{final_general_price}{price}"

                    lista.insert(END, new_str2)
                    lista.insert(
                        END, "___________________________________________________________________")

                    item_count += 1
                    items_Count_label.config(text=item_count)

                    cost += float(round(price))
                    price_label.config(text=cost)

                    mass_label.config(text=mass)

                    status_label.config(text="✅")
                    product_label.delete(0, END)

                    window3.destroy()
                    window2.destroy()

                submit_btn = Button(window3, text="Submit",
                                    font=("Arial", 18, "bold"), command=get_mass)
                submit_btn.place(x=80, y=100)

                window3.mainloop()

            elif name_value:
                for item in items.items:
                    if items.items[item]["name"] == name_value:
                        item_code_to_add = items.items[item]["code"]
                        item_name_to_add = items.items[item]["name"]
                        item_general_price_to_add = items.items[item]["price/kg"]

                        window3 = tkinter.Toplevel(window2)
                        window3.title("Enter Mass")
                        window3.config(padx=20, pady=20, bg=WHITE)
                        window3.minsize(width=300, height=170)

                        title_win = Label(window3, text="Enter Mass",
                                          font=("Arial", 22, "bold"), bg=WHITE)
                        title_win.place(x=0, y=0)

                        entry_mass = Entry(window3, font=("Arial", 18, "bold"))
                        entry_mass.place(x=0, y=50)

                        def get_mass():
                            global mass, item_count, cost
                            mass = entry_mass.get()

                            # spacing system

                            name_space = 20 - len(item_name_to_add)
                            final_str = item_name_to_add + (" " * name_space)

                            mass_space = 16 - len(str(mass))
                            final_mass = str(mass) + (" " * mass_space)

                            general_price_space = 14 - \
                                len(str(item_general_price_to_add))
                            final_general_price = str(item_general_price_to_add) + \
                                (" " * general_price_space)

                            price = float(
                                item_general_price_to_add) * float(mass)
                            # spacing system

                            new_str2 = f"{final_str}{final_mass}{final_general_price}{price}"

                            lista.insert(END, new_str2)
                            lista.insert(
                                END, "___________________________________________________________________")

                            item_count += 1
                            items_Count_label.config(text=item_count)

                            cost += float(round(price, 2))
                            price_label.config(text=cost)

                            mass_label.config(text=mass)

                            status_label.config(text="✅")
                            product_label.delete(0, END)

                            window3.destroy()
                            window2.destroy()

                        submit_btn = Button(window3, text="Submit",
                                            font=("Arial", 18, "bold"), command=get_mass)
                        submit_btn.place(x=80, y=100)

                        window3.mainloop()

        search_code_btn = Button(window2, text="Search info by code",
                                 font=("Arial", 16, "bold"), width=18, command=search_by_code)
        search_code_btn.place(x=570, y=200)

        search_info_by_name_btn = Button(window2,
                                         text="Search info by name", font=("Arial", 16, "bold"), width=18, command=search_by_name)
        search_info_by_name_btn.place(x=570, y=300)

        add_to_list_btn = Button(
            window2, text="Add to list", font=("Arial", 16, "bold"), width=18, command=add_item_to_list)
        add_to_list_btn.place(x=570, y=400)

        ########################################
        item = int(product_label.get())

        item_code_result = items.items[item]["code"]
        item_name_result = items.items[item]["name"]
        item_price_result = items.items[item]["price/kg"]
        item_sale_result = items.items[item]["sale"]

        item_code.config(text=item_code_result)
        item_name.config(text=item_name_result)
        item_sale.config(text=item_sale_result)
        item_price.config(text=item_price_result)

        window2.mainloop()

    item_info = Button(text="Item Info", font=("Arial", 22, "bold"),
                       height=4, width=12, borderwidth=3, relief="solid", bg=LIGHT_BLUE, command=info)
    item_info.place(x=830, y=180)

    ##########################################################################################################################################
    ##########################################################################################################################################
    def reciept_window():
        window2 = tkinter.Toplevel(window)
        window2.title("Reciepts Operations")
        window2.minsize(width=550, height=200)
        window2.config(padx=20, pady=20, bg=WHITE)

        title = Label(window2, text="All you can do with Reciepts",
                      font=("Arial", 22, "bold"), bg=WHITE)
        title.place(x=60, y=0)

        def normal_rc():
            global item_lista, item_regular_price_lista, item_end_price_lista, worker_index

            eel.init("web")

            @eel.expose
            def send_data():
                global item_lista, item_regular_price_lista, item_end_price_lista
                eel.recieve2(item_lista, item_regular_price_lista,
                             item_end_price_lista)

            @eel.expose
            def get_time():
                return datetime.datetime.now().strftime("%H:%M:%S")

            @eel.expose
            def send_info():
                global cost
                with open("data.json", mode="r") as datafile:
                    data = json.load(datafile)
                    name = data[worker_index]["name"]
                    kopa = data[worker_index]["kopa"]
                    total = cost

                return name, kopa, total

            eel.start("index.html")

        def start():
            new_thread = Thread(target=normal_rc)
            new_thread.start()

        normal_rc_btn = Button(window2, text="Print Reciept",
                               font=("Arial", 22, "bold"), command=start)
        normal_rc_btn.place(x=0, y=100)

        copy_reciept_btn = Button(
            window2, text="Copy Reciept", font=("Arial", 22, "bold"))
        copy_reciept_btn.place(x=300, y=100)

        window.mainloop()

    print_reciept = Button(text="Reciept", font=(
        "Arial", 22, "bold"), borderwidth=3, relief="solid", height=4, width=12, bg=LIGHT_BLUE, command=reciept_window)
    print_reciept.place(x=1060, y=180)

    ##########################################################################################################################################
    ##########################################################################################################################################
    def pay_func():
        window2 = tkinter.Toplevel(window)
        window2.title("Paying Methods 💵💰")
        window2.minsize(width=300, height=500)
        window2.config(padx=40, pady=40, bg=WHITE)

        title = Label(window2, text="Payments:", font=(
            "Arial", 22, "bold"), bg=WHITE)
        title.place(x=0, y=0)

        def pass_credit_card():
            global cost

            new_window = tkinter.Toplevel(window2)
            new_window.config(padx=20, pady=20, bg=WHITE)
            new_window.title("Enter cridit card info")
            new_window.minsize(width=670, height=550)

            title = Label(new_window, text="Enter Card Information",
                          font=("Arial", 22, "bold"), bg=WHITE)
            title.place(x=0, y=0)

            amount_to_pay_lbl = Label(
                new_window, text="Amount:", font=("Arial", 22, "bold"), bg=WHITE)
            amount_to_pay_lbl.place(x=0, y=60)

            real_amount_to_pay = Label(new_window,
                                       text=f"{cost}₪", font=("Arial", 22, "bold"), bg=WHITE)
            real_amount_to_pay.place(x=140, y=60)

            different_amount_label = Label(
                new_window, text="Other amounts:", font=("Arial", 22, "bold"), bg=WHITE)
            different_amount_label.place(x=280, y=60)

            different_amount_entry = Entry(
                new_window, font=("Arial", 22, "bold"), width=7)
            different_amount_entry.place(x=510, y=60)

            card_number_label = Label(new_window,
                                      text="Card Num:", font=("Arial", 22, "bold"), bg=WHITE)
            card_number_label.place(x=0, y=120)

            card_date_label = Label(new_window, text="Card Date:", font=(
                "Arial", 22, "bold"), bg=WHITE)
            card_date_label.place(x=0, y=280)

            card_cvv_label = Label(new_window, text="Card CVV:", font=(
                "Arial", 22, 'bold'), bg=WHITE)
            card_cvv_label.place(x=0, y=360)

            card_holder_id_label = Label(
                new_window, text="Holder ID:", font=("Arial", 22, "bold"), bg=WHITE)
            card_holder_id_label.place(x=0, y=200)

            card_holder_id_entry = Entry(
                new_window, font=("Arial", 22, "bold"), width=18)
            card_holder_id_entry.place(x=160, y=200)

            card_number_entry = Entry(
                new_window, font=("Arial", 22, "bold"), width=22)
            card_number_entry.place(x=160, y=120)

            card_date_entry = Entry(new_window, font=(
                "Arial", 22, "bold"), width=13)
            card_date_entry.place(x=160, y=280)

            card_cvv_entry = Entry(new_window, font=(
                "Arial", 22, "bold"), width=8)
            card_cvv_entry.place(x=160, y=360)

            def submit():
                global cost, paid

                card_num = card_number_entry.get()
                card_date = card_date_entry.get()
                card_cvv = card_cvv_entry.get()
                card_holder_id = card_holder_id_entry.get()
                part_of_payment = different_amount_entry.get()

                if part_of_payment == "":
                    paid = cost
                else:
                    paid = float(part_of_payment)

                new_data = {
                    card_holder_id: {
                        "card_num": card_num,
                        "card_date": card_date,
                        "card_cvv": card_cvv,
                        "paid_amount": paid,
                    }
                }

                try:
                    with open("credit_cards_data.json", mode="r") as datafile:
                        data = json.load(datafile)

                except FileNotFoundError:
                    with open("credit_cards_data.json", mode="w") as datafile:
                        json.dump(new_data, datafile, indent=4)

                else:
                    data.update(new_data)
                    with open("credit_cards_data.json", mode="w") as datafile:
                        json.dump(data, datafile, indent=4)

                finally:
                    new_window.destroy()
                    window2.destroy()

                # at this point the app should ask for a phone number to call so it can closethe recipt

                window3 = tkinter.Toplevel()
                window3.title("Insert phone number")
                window3.minsize(width=300, height=200)
                window3.config(bg=WHITE, padx=20, pady=20)

                title = Label(window3, text="Phone Num",
                              font=("Arial", 22, "bold"), bg=WHITE)
                title.place(x=0, y=0)

                num_entry = Entry(window3, font=(
                    "Arial", 20, "bold"), width=15)
                num_entry.place(x=0, y=50)

                def call_client():
                    global cost

                    if num_entry.get() != "":
                        number = num_entry.get()[1:]
                        full_number = f"+972{number}"
                        print(full_number)

                        client = Client(acc_sid, auth_key)

                        call = client.calls.create(
                            to=full_number, from_="+97293762128", url="http://demo.twilio.com/docs/voice.xml")
                        print(call.sid)

                        left_to_pay = cost - paid
                        cost = left_to_pay

                        price_label.config(text=left_to_pay)

                        lista.insert(
                            END, f"Paid by credit card:           {paid}₪")
                        lista.insert(
                            END, "___________________________________________________________________")

                        window3.destroy()

                    else:
                        print("didnt make a call")

                submite_btn = Button(window3, text="Submit",
                                     font=("Arial", 18, "bold"), command=call_client)
                submite_btn.place(x=0, y=100)

                window3.mainloop()

            btn_submit = Button(new_window, text="Submit",
                                font=("Arial", 22, "bold"), command=submit)
            btn_submit.place(x=200, y=430)

        credit_card_btn = Button(
            window2, text="Credit Card", font=("Arial", 22, "bold"), width=12, command=pass_credit_card)
        credit_card_btn.place(x=0, y=70)

        def pay_cash():
            global cost

            window3 = tkinter.Toplevel(window)
            window3.title("Pay Cash 💲")
            window3.minsize(width=500, height=200)
            window3.config(padx=20, pady=20, bg=WHITE)

            title2 = Label(window3, text="Pay the desired amount of cash", font=(
                "Arial", 22, "bold"), bg=WHITE)
            title2.place(x=0, y=0)

            amount_label = Label(window3, text="total:", font=(
                "Arial", 22, "bold"), bg=WHITE)
            amount_label.place(x=0, y=50)

            if cost == 0:
                crr_cost = "0000.00"
            else:
                crr_cost = cost

            amount_to_pay = Label(window3, text=crr_cost, font=(
                "Arial", 22, "bold"), bg=WHITE)
            amount_to_pay.place(x=80, y=50)

            other_amount_label = Label(window3, text="other:", font=(
                "Arial", 22, "bold"), bg=WHITE)
            other_amount_label.place(x=260, y=50)

            other_amount = Entry(window3, font=("Arial", 22, "bold"), width=7)
            other_amount.place(x=350, y=50)

            def submit_pay():
                global payment_num, cost
                if crr_cost == "0000.00":
                    messagebox.showerror(
                        title="Payment Error", message=f"the total is {crr_cost}, there is nothing to be payed")
                else:
                    if other_amount.get() == "":
                        pay_amount = crr_cost

                        new_data = {
                            payment_num: {
                                "amount": pay_amount
                            }
                        }
                        payment_num += 1

                        try:
                            with open("cash_data.json", mode="r") as datafile:
                                data = json.load(datafile)

                        except FileNotFoundError:
                            with open("cash_data.json", mode="w") as datafile:
                                json.dump(new_data, datafile, indent=4)

                        else:
                            data.update(new_data)
                            with open("cash_data.json", mode="w") as datafile:
                                json.dump(data, datafile, indent=4)

                        left_to_pay = cost - pay_amount

                        cost = left_to_pay

                        price_label.config(text=cost)

                        lista.insert(
                            END, f"Paid in cash:                         {pay_amount}₪")
                        lista.insert(
                            END, "___________________________________________________________________")

                        window3.destroy()
                        window2.destroy()

                    else:
                        pay_amount = float(other_amount.get())

                        new_data = {
                            payment_num: {
                                "amount": pay_amount
                            }
                        }
                        payment_num += 1

                        try:
                            with open("cash_data.json", mode="r") as datafile:
                                data = json.load(datafile)

                        except FileNotFoundError:
                            with open("cash_data.json", mode="w") as datafile:
                                json.dump(new_data, datafile, indent=4)

                        else:
                            data.update(new_data)
                            with open("cash_data.json", mode="w") as datafile:
                                json.dump(data, datafile, indent=4)

                        left_to_pay = cost - pay_amount

                        cost = left_to_pay

                        price_label.config(text=cost)

                        lista.insert(
                            END, f"Paid in cash:                         {pay_amount}₪")
                        lista.insert(
                            END, "___________________________________________________________________")

                        window3.destroy()
                        window2.destroy()

            pay_btn = Button(window3, text="Pay", font=(
                "Arial", 22, "bold"), width=7, command=submit_pay)
            pay_btn.place(x=160, y=100)

            window3.mainloop()

        cash_btn = Button(window2, text="Cash", font=(
            "Arial", 22, "bold"), width=12, command=pay_cash)
        cash_btn.place(x=0, y=170)

        def pay_zikoy():
            window4 = tkinter.Toplevel(window)
            window4.title("Pass a returned value 🧾🔁")
            window4.minsize(width=500, height=200)
            window4.config(padx=20, pady=20, bg=WHITE)

            title2 = Label(window4, text="Returned value of:", font=(
                "Arial", 22, "bold"), bg=WHITE)
            title2.place(x=0, y=20)

            value_entry = Entry(window4, font=("Arial", 22, "bold"), width=9)
            value_entry.place(x=270, y=20)

            shakel_label = Label(window4, text="₪", font=(
                "Arial", 22, "bold"), bg=WHITE)
            shakel_label.place(x=405, y=20)

            def approve():
                global cost, payment_num2

                value = float(value_entry.get())

                new_data = {
                    payment_num2: {
                        "amount": value
                    }
                }
                payment_num2 += 1

                try:
                    with open("zikoy_data.json", mode="r") as datafile:
                        data = json.load(datafile)

                except FileNotFoundError:
                    with open("zikoy_data.json", mode="w") as datafile:
                        json.dump(new_data, datafile, indent=4)

                else:
                    data.update(new_data)
                    with open("zikoy_data.json", mode="w") as datafile:
                        json.dump(data, datafile, indent=4)

                left_to_pay = cost - value

                cost = left_to_pay
                price_label.config(text=cost)

                lista.insert(
                    END, f"Returened value:                         {value}₪")
                lista.insert(
                    END, "___________________________________________________________________")

                window4.destroy()
                window2.destroy()

            approve_btn = Button(window4, text="Approve", font=(
                "Arial", 22, "bold"), width=7, command=approve)
            approve_btn.place(x=160, y=90)

            window4.mainloop()

        zikoy_btn = Button(window2, text="Reterned value",
                           font=("Arial", 22, "bold"), width=12, command=pay_zikoy)
        zikoy_btn.place(x=0, y=270)

        ##########################################################################################################################
        ##########################################################################################################################
        def pay_check():
            global cost

            window5 = tkinter.Toplevel(window)
            window5.title("Pay with a Check 💶")
            window5.config(padx=20, pady=20, bg=WHITE)
            window5.minsize(width=800, height=300)

            name_entry = Entry(window5, font=(
                "Times New Roman", 22, "bold"), width=13)
            name_entry.insert(END, "full name")
            name_entry.place(x=0, y=0)

            id_entry = Entry(window5, font=(
                "Times New Roman", 22, "bold"), width=13)
            id_entry.insert(END, "id number")
            id_entry.place(x=0, y=40)

            date_label = Label(window5, font=(
                "Times New Roman", 22, "bold"), text="date:", bg=WHITE)
            date_label.place(x=500, y=0)

            date_entry = Entry(window5, font=(
                "Times New Roman", 22, "bold"), width=12)
            date_entry.insert(END, "")
            date_entry.place(x=570, y=0)

            pay_to_the = Label(window5, text="Pay to the",
                               font=("Times New Roman", 20, "bold"), bg=WHITE)
            pay_to_the.place(x=0, y=90)

            order_of = Label(window5, text="Order of:", font=(
                "Times New Roman", 18, "bold"), bg=WHITE)
            order_of.place(x=0, y=123)

            line = Label(window5, font=("Times New Roman", 22, "bold"), bg=WHITE,
                         text="________________________________|_________")
            line.place(x=105, y=123)

            to_entry = Entry(window5, font=(
                "Times New Roman", 22, "bold"), width=32)
            to_entry.place(x=105, y=120)

            amount_num = Entry(window5, font=(
                "Times New Roman", 20, "bold"), width=10)
            amount_num.insert(END, cost)
            amount_num.place(x=595, y=120)

            shekel_label = Label(window5, text="₪", font=(
                "Times New Roman", 20, "bold"), bg=WHITE)
            shekel_label.place(x=745, y=119)

            amount_of = Label(window5, text="Amount of:", font=(
                "Times New Roman", 18, "bold"), bg=WHITE)
            amount_of.place(x=0, y=180)

            line2 = Label(window5, font=("Times New Roman", 22, "bold"), bg=WHITE,
                          text="________________________________________")
            line2.place(x=120, y=180)

            amount_words = Entry(window5, font=(
                "Times New Roman", 22, "bold"), width=42)
            amount_words.place(x=120, y=175)

            written_amount = num2words(cost, lang="en")
            shekels = written_amount.split("point")[0]
            agorot = written_amount.split("point")[1]

            final_text = f"{shekels}shakels and{agorot} cents"

            amount_words.insert(END, final_text)

            def approved():
                global cost

                client_name = name_entry.get()
                client_id = id_entry.get()
                issuing_date = date_entry.get()
                check_reciever = to_entry.get()
                check_value = amount_num.get()
                check_written_value = amount_words.get()

                new_data = {
                    client_id: {
                        "name": client_name,
                        "date": issuing_date,
                        "to": check_reciever,
                        "value": check_value,
                        "written_value": check_written_value
                    }
                }

                try:
                    with open("check_data.json", mode="r") as datafile:
                        data = json.load(datafile)

                except FileNotFoundError:
                    with open("check_data.json", mode="w") as datafile:
                        json.dump(new_data, datafile, indent=4)

                else:
                    data.update(new_data)
                    with open("check_data.json", mode="w") as datafile:
                        json.dump(data, datafile, indent=4)

                left_to_pay = cost - float(check_value)

                cost = left_to_pay
                price_label.config(text=cost)

                lista.insert(
                    END, f"Paid with a check:                        {check_value}₪")
                lista.insert(
                    END, "___________________________________________________________________")

                window5.destroy()
                window2.destroy()

            approve_btn = Button(window5, text="Approve",
                                 font=("Times New Roman", 22, "bold"), command=approved)
            approve_btn.place(x=620, y=220)

            window5.mainloop()

        check_btn = Button(window2, text="Checks",
                           font=("Arial", 22, "bold"), width=12, command=pay_check)
        check_btn.place(x=0, y=370)

        window2.mainloop()

    pay = Button(text="Pay", font=("Arial", 22, 'bold'),
                 borderwidth=3, relief="solid", height=4, width=12, bg=LIGHT_BLUE, command=pay_func)
    pay.place(x=1290, y=180)

    ######################Down right side 2#################################################

    def delete_item():
        global item_count, cost, item_lista, item_regular_price_lista, item_end_price_lista

        msg = messagebox.askyesno(
            title="Delete Item", message="Do you have the permision to delete the item")
        if msg == True:

            if item_count == 0:
                pass
            else:
                item_count -= 1
                items_Count_label.config(text=item_count)

            current_price_to_remove = lista.get(ACTIVE)[50:]
            cost -= float(current_price_to_remove)
            price_label.config(text=cost)

            status_label.config(text="❌")

            current_item_name = lista.get(ACTIVE)[:20]

            item_lista.append(f"removed: {current_item_name}")
            item_regular_price_lista.append(" ")
            item_end_price_lista.append(f"-{current_price_to_remove}")

            lista.insert(
                END, f"deleted: {current_item_name}, -{current_price_to_remove} shekels")

            lista.insert(
                END, "___________________________________________________________________")

            lista.delete(ANCHOR)

        else:
            pass

    cancle_item = Button(text="Cancle Item", font=(
        "Arial", 22, "bold"), borderwidth=3, relief="solid", height=4, width=25, bg=ORANGE, command=delete_item)
    cancle_item.place(x=600, y=350)

    def cancle_reciept():
        global item_lista, item_regular_price_lista, item_end_price_lista

        msg = messagebox.askokcancel(
            title="Cancle Reciept", message="this will cancle all the purchas process and all the products shall be returned")
        if msg == True:
            lista.delete(0, END)
            price_label.config(text='Price')
            mass_label.config(text='mass')
            items_Count_label.config(text="items count")
            status_label.config(text="status")

            item_lista = []
            item_regular_price_lista = []
            item_end_price_lista = []

            lista.insert(
                END, f"Name          count        price/kg         price")
            lista.insert(
                END, "___________________________________________________________________")
        else:
            pass

    cancle_reciepte = Button(text="Cancle Reciept", font=(
        "Arial", 22, "bold"), borderwidth=3, relief="solid", height=4, width=25, bg=ORANGE, command=cancle_reciept)
    cancle_reciepte.place(x=1060, y=350)
    ################################product list############################################
    my_frame = Frame(window)
    my_frame.place(x=0, y=70)

    lista = Listbox(my_frame, font=("Arial", 22, "bold"), width=36, height=21,
                    highlightthickness=0, selectbackground=LIGHT_BLUE, activestyle=None, borderwidth=3, relief="solid")
    lista.pack(side="left", fill="both")

    lista.insert(END, f"Name          count        price/kg         price")
    lista.insert(
        END, "___________________________________________________________________")

    my_scrollbar = Scrollbar(my_frame)
    my_scrollbar.pack(side="right", fill="both")

    lista.config(yscrollcommand=my_scrollbar.set)
    my_scrollbar.config(command=lista.yview)

    ################################calculator##########################################
    def print1():
        product_label.focus_set()
        product_label.insert(END, 1)

    b1 = Button(text=1, font=("Arial", 22, "bold"),
                borderwidth=3, relief="solid", height=2, width=6, command=print1, bg=Yellow)
    b1.place(x=600, y=520)

    def print2():
        product_label.focus_set()
        product_label.insert(END, 2)
    b2 = Button(text="2", font=("Arial", 22, "bold"),
                borderwidth=3, relief="solid", height=2, width=6, command=print2, bg=Yellow)
    b2.place(x=730, y=520)

    def print3():
        product_label.focus_set()
        product_label.insert(END, 3)
    b3 = Button(text="3", font=("Arial", 22, "bold"),
                borderwidth=3, relief="solid", height=2, width=6, command=print3, bg=Yellow)
    b3.place(x=860, y=520)

    def print4():
        product_label.focus_set()
        product_label.insert(END, 4)
    b4 = Button(text="4", font=("Arial", 22, "bold"),
                borderwidth=3, relief="solid", height=2, width=6, command=print4, bg=Yellow)
    b4.place(x=600, y=620)

    def print5():
        product_label.focus_set()
        product_label.insert(END, 5)
    b5 = Button(text="5", font=("Arial", 22, "bold"),
                borderwidth=3, relief="solid", height=2, width=6, command=print5, bg=Yellow)
    b5.place(x=730, y=620)

    def print6():
        product_label.focus_set()
        product_label.insert(END, 6)
    b6 = Button(text="6", font=("Arial", 22, "bold"),
                borderwidth=3, relief="solid", height=2, width=6, command=print6, bg=Yellow)
    b6.place(x=860, y=620)

    def print7():
        product_label.focus_set()
        product_label.insert(END, 7)
    b7 = Button(text="7", font=("Arial", 22, "bold"),
                borderwidth=3, relief="solid", height=2, width=6, command=print7, bg=Yellow)
    b7.place(x=600, y=720)

    def print8():
        product_label.focus_set()
        product_label.insert(END, 8)
    b8 = Button(text="8", font=("Arial", 22, "bold"),
                borderwidth=3, relief="solid", height=2, width=6, command=print8, bg=Yellow)
    b8.place(x=730, y=720)

    def print9():
        product_label.focus_set()
        product_label.insert(END, 9)
    b9 = Button(text="9", font=("Arial", 22, "bold"),
                borderwidth=3, relief="solid", height=2, width=6, command=print9, bg=Yellow)
    b9.place(x=860, y=720)

    def print0():
        product_label.focus_set()
        product_label.insert(END, 0)
    b0 = Button(text="0", font=("Arial", 22, "bold"),
                borderwidth=3, relief="solid", height=2, width=9, command=print0, bg=Yellow)
    b0.place(x=990, y=520)

    #######################################################################
    def find_product():
        global mass, item_count, cost

        product_label.focus_set()
        product_key = int(product_label.get())

        product_name = items.items[product_key]["name"]
        product_price_per_kg = items.items[product_key]["price/kg"]

        window3 = tkinter.Toplevel(window)
        window3.minsize(width=300, height=350)
        window3.config(padx=20, pady=20)

        title = Label(window3, text="Insert a mass or an ammount",
                      font=("Arial", 22, "bold"))
        title.pack()

        entry_mass = Entry(window3, font=("Arial", 22, "bold"))
        entry_mass.place(x=40, y=120)

        def get_mass():
            global mass, item_count, cost, item_lista, item_regular_price_lista, item_end_price_lista
            mass = entry_mass.get()

            # spacing system

            name_space = 20 - len(product_name)
            final_str = product_name + (" " * name_space)

            mass_space = 16 - len(str(mass))
            final_mass = str(mass) + (" " * mass_space)

            general_price_space = 14 - len(str(product_price_per_kg))
            final_general_price = str(product_price_per_kg) + \
                (" " * general_price_space)

            price = float(product_price_per_kg) * float(mass)
            # spacing system

            new_str2 = f"{final_str}{final_mass}{final_general_price}{price}"

            item_lista.append(product_name)
            item_regular_price_lista.append(product_price_per_kg)
            item_end_price_lista.append(price)

            lista.insert(END, new_str2)
            lista.insert(
                END, "___________________________________________________________________")

            item_count += 1
            items_Count_label.config(text=item_count)

            cost += float(round(price, 2))
            price_label.config(text=cost)

            mass_label.config(text=mass)

            status_label.config(text="✅")
            product_label.delete(0, END)

            window3.destroy()

        submit = Button(window3, text="Submit", font=(
            "Arial", 22, "bold"), command=get_mass)
        submit.place(x=130, y=200)
        window3.mainloop()

    bsearch = Button(text="Search", font=("Arial", 22, "bold"),
                     borderwidth=3, relief="solid", height=2, width=9, bg=Yellow, command=find_product)
    bsearch.place(x=1350, y=720)
    ######################################################################

    def equals():
        global first_value, second_value

        current_value = product_label.get()

        if "+" in current_value:
            second_value = product_label.get().split("+")[1]
            result = float(first_value) + float(second_value)
            product_label.delete(0, END)
            product_label.insert(END, result)

        elif "-" in current_value:
            second_value = product_label.get().split("-")[1]
            result = float(first_value) - float(second_value)
            product_label.delete(0, END)
            product_label.insert(END, result)

        elif "x" in current_value:
            second_value = product_label.get().split("x")[1]
            result = float(first_value) * float(second_value)
            product_label.delete(0, END)
            product_label.insert(END, result)

        elif "÷" in current_value:
            second_value = product_label.get().split("÷")[1]
            result = float(first_value) / float(second_value)
            product_label.delete(0, END)
            product_label.insert(END, result)

    bequals = Button(text="=", font=("Arial", 22, "bold"),
                     borderwidth=3, relief="solid", height=2, width=9, command=equals, bg=Yellow)
    bequals.place(x=990, y=620)

    def add():
        global first_value, second_value

        first_value = product_label.get()
        product_label.delete(0, END)
        product_label.insert(END, "+")

    bplus = Button(text="+", font=("Arial", 22, "bold"),
                   borderwidth=3, relief="solid", height=2, width=9, command=add, bg=Yellow)
    bplus.place(x=1170, y=520)

    def subtract():
        global first_value, second_value

        first_value = product_label.get()
        product_label.delete(0, END)
        product_label.insert(END, "-")

    bminus = Button(text="-", font=("Arial", 22, "bold"),
                    borderwidth=3, relief="solid", height=2, width=9, command=subtract, bg=Yellow)
    bminus.place(x=1350, y=520)

    def multiply():
        global first_value, second_value

        first_value = product_label.get()
        product_label.delete(0, END)
        product_label.insert(END, "x")

    bmult = Button(text="X", font=("Arial", 22, "bold"),
                   borderwidth=3, relief="solid", height=2, width=9, command=multiply, bg=Yellow)
    bmult.place(x=1170, y=620)

    def devide():
        global first_value, second_value

        first_value = product_label.get()
        product_label.delete(0, END)
        product_label.insert(END, "÷")

    bdiv = Button(text="÷", font=("Arial", 22, "bold"),
                  borderwidth=3, relief="solid", height=2, width=9, command=devide, bg=Yellow)
    bdiv.place(x=1350, y=620)

    def clear():
        product_label.delete(0, END)

    clear_all = Button(text="Clear", font=("Arial", 22, "bold"),
                       borderwidth=3, relief="solid", height=2, width=9, command=clear, bg=Yellow)
    clear_all.place(x=1170, y=720)

    def add_decimal_point():
        product_label.insert(END, ".")

    bdecimal = Button(text=".", font=("Arial", 22, "bold"),
                      borderwidth=3, relief="solid", height=2, width=9, command=add_decimal_point, bg=Yellow)
    bdecimal.place(x=990, y=720)
###################################Start payment process########################################

    def start_payment():
        window1 = tkinter.Toplevel(window)
        window1.title("Start the Purchesing Process")
        window1.minsize(width=1000, height=500)
        window1.config(padx=20, pady=20, bg=WHITE)

        def go_back():
            window1.destroy()

        def pass_id():
            new_window = tkinter.Toplevel(window1)
            new_window.config(padx=20, pady=20, bg=WHITE)
            new_window.title("Pass the ID number")
            new_window.minsize(width=600, height=500)

            title_2 = Label(new_window, text="Please pass the ID number",
                            font=("Arial", 22, "bold"), bg=WHITE)
            title_2.place(x=80, y=0)

            entry = Entry(new_window, width=22, font=("Arial", 22, "bold"))
            entry.place(x=100, y=200)

            entry.focus_set()

            def save_info():
                global num
                id_num = entry.get()

                new_data = {
                    id_num: {
                        "customer": f"{num}"
                    }
                }

                try:
                    with open("saved.json", mode="r") as datafile:
                        data = json.load(datafile)

                except FileNotFoundError:
                    with open("saved.json", mode="w") as datafile:
                        json.dump(new_data, datafile, indent=4)

                else:
                    data.update(new_data)
                    with open("saved.json", mode="w") as datafile:
                        json.dump(data, datafile, indent=4)

                finally:
                    num += 1
                    new_window.destroy()
                    window1.destroy()

            submite_btn = Button(new_window, text="Submit", font=(
                "Arial", 22, "bold"), command=save_info)
            submite_btn.place(x=200, y=260)

        def pass_credit_card():

            new_window = tkinter.Toplevel(window1)
            new_window.config(padx=20, pady=20, bg=WHITE)
            new_window.title("Enter cridit card info")
            new_window.minsize(width=600, height=500)

            title = Label(new_window, text="Enter Card Information",
                          font=("Arial", 22, "bold"), bg=WHITE)
            title.place(x=0, y=0)

            card_number_label = Label(new_window,
                                      text="Card Num:", font=("Arial", 22, "bold"), bg=WHITE)
            card_number_label.place(x=0, y=80)

            card_date_label = Label(new_window, text="Card Date:", font=(
                "Arial", 22, "bold"), bg=WHITE)
            card_date_label.place(x=0, y=240)

            card_cvv_label = Label(new_window, text="Card CVV:", font=(
                "Arial", 22, 'bold'), bg=WHITE)
            card_cvv_label.place(x=0, y=320)

            card_holder_id_label = Label(
                new_window, text="Holder ID:", font=("Arial", 22, "bold"), bg=WHITE)
            card_holder_id_label.place(x=0, y=160)

            card_holder_id_entry = Entry(
                new_window, font=("Arial", 22, "bold"), width=18)
            card_holder_id_entry.place(x=160, y=160)

            card_number_entry = Entry(
                new_window, font=("Arial", 22, "bold"), width=22)
            card_number_entry.place(x=160, y=80)

            card_date_entry = Entry(new_window, font=(
                "Arial", 22, "bold"), width=13)
            card_date_entry.place(x=160, y=240)

            card_cvv_entry = Entry(new_window, font=(
                "Arial", 22, "bold"), width=8)
            card_cvv_entry.place(x=160, y=320)

            def submit():
                card_num = card_number_entry.get()
                card_date = card_date_entry.get()
                card_cvv = card_cvv_entry.get()
                card_holder_id = card_holder_id_entry.get()

                new_data = {
                    card_holder_id: {
                        "card_num": card_num,
                        "card_date": card_date,
                        "card_cvv": card_cvv
                    }
                }

                try:
                    with open("saved.json", mode="r") as datafile:
                        data = json.load(datafile)

                except FileNotFoundError:
                    with open("saved.json", mode="w") as datafile:
                        json.dump(new_data, datafile, indent=4)

                else:
                    data.update(new_data)
                    with open("saved.json", mode="w") as datafile:
                        json.dump(data, datafile, indent=4)

                finally:
                    new_window.destroy()
                    window1.destroy()

            btn_submit = Button(new_window, text="Submit",
                                font=("Arial", 22, "bold"), command=submit)
            btn_submit.place(x=200, y=390)

            new_window.mainloop()

        def new_client():
            global item_lista, item_regular_price_lista, item_end_price_lista

            lista.delete(0, END)
            price_label.config(text='Price')
            mass_label.config(text='mass')
            items_Count_label.config(text="items count")
            status_label.config(text="status")

            item_lista = []
            item_regular_price_lista = []
            item_end_price_lista = []

            lista.insert(
                END, f"Name          count        price/kg         price")
            lista.insert(
                END, "___________________________________________________________________")
            window1.destroy()

        title = Label(window1, text="Pass your special credit card or the ID number connected with it", font=(
            "Arial", 22, "bold"), bg=WHITE)
        title.place(x=0, y=0)

        credit_card_btn = Button(window1, text="Credit Card", font=(
            "Arial", 22, "bold"), command=pass_credit_card)
        credit_card_btn.place(x=40, y=380)

        id_btn = Button(window1, text="Pass ID", font=(
            "Arial", 22, "bold"), command=pass_id)
        id_btn.place(x=250, y=380)

        new_client_btn = Button(window1, text="New Client", font=(
            "Arial", 22, "bold"), command=new_client)
        new_client_btn.place(x=400, y=380)

        close_btn = Button(window1, text="Back", font=(
            "Arial", 22, "bold"), command=go_back)
        close_btn.place(x=800, y=380)

        window1.mainloop()

    start_btn = Button(text="Start", font=(
        "Arial", 22, "bold"), borderwidth=3, relief="solid", command=start_payment, bg=WHITE)
    start_btn.place(x=335, y=810)

    def features_list():

        window2 = tkinter.Toplevel()
        window2.title("Feature List")
        window2.minsize(width=700, height=500)
        window2.config(padx=20, pady=20, bg=WHITE)

        window2.mainloop()

    features_btn = Button(text="Features", font=(
        "Arial", 22, "bold"), borderwidth=3, relief="solid", command=features_list, bg=WHITE)
    features_btn.place(x=432, y=810)

    window.mainloop()
##################################################################################################


def log_in():
    global name, kopa_num, worker_index
    name = name_entry.get()
    id = id_entry.get()
    kopa_num = kopa_entry.get()

    worker_index = id

    new_data = {
        id: {
            "name": name,
            "kopa": kopa_num
        }
    }

    try:
        with open("data.json", mode="r") as datafile:
            data = json.load(datafile)

    except FileNotFoundError:
        with open("data.json", mode="w") as datafile:
            json.dump(new_data, datafile, indent=4)

    else:
        data.update(new_data)
        with open("data.json", mode="w") as datafile:
            json.dump(data, datafile, indent=4)

    finally:
        name_entry.delete(0, END)
        id_entry.delete(0, END)
        display()


def auto_fill():
    name_entry.insert(END, "milad bannourah")
    kopa_entry.insert(END, "9")
    id_entry.insert(END, "115079")


window = Tk()
window.minsize(width=1000, height=600)
window.config(padx=25, pady=25, background=WHITE)
window.title("Kopa Log In")

header_label = Label(text="Welcome to Kopa app",
                     font=("Arial", 22, "bold"), bg=WHITE)
header_label.place(x=0, y=0)

footer_label = Label(
    text="Done by full-stack dev Milad Bannourah", font=("Arial", 22, "bold"), bg=WHITE)
footer_label.place(x=0, y=520)

name_label = Label(text="Name", font=("Arial", 22, "bold"), bg=WHITE)
name_label.place(x=180, y=180)

worker_id_label = Label(text="W-ID", font=("Arial", 22, "bold"), bg=WHITE)
worker_id_label.place(x=180, y=250)

name_entry = Entry(width=30, font=("Arial", 22, "bold"))
name_entry.place(x=280, y=180)

id_entry = Entry(width=30, font=("Arial", 22, "bold"))
id_entry.place(x=280, y=250)

log_in_btn = Button(text="Log In", font=(
    "Arial", 22, "bold"), width=15, command=log_in)
log_in_btn.place(x=360, y=390)

kopa_entry = Entry(width=30, font=("Arial", 22, "bold"))
kopa_entry.place(x=280, y=320)

kopa_number = Label(text="Kopa ", font=(
    "Arial", 22, "bold"), bg=WHITE)
kopa_number.place(x=180, y=320)

test_button = Button(text="Auto fill", font=(
    "Arial", 22, "bold"), command=auto_fill)
test_button.place(x=420, y=90)

window.mainloop()
