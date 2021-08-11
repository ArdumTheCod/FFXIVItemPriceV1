import requests
import re
import operator
import tkinter as tk
import time

Height = 300
Width = 500
pld_item = [31830, 31813]
chest_items = [31868, 31832, 31862, 31850, 31856, 31844, 31838]
feet_items = [31853, 31859, 31847, 31835, 31841, 31871, 31865]
hands_items = [31851, 31857, 31845, 31833, 31839, 31869, 31863]
head_items = [31831, 31861, 31837, 31867, 31849, 31855, 31843]
leg_items = [31852, 31858, 31846, 31870, 31834, 31864, 31840]
waist_items = [31872, 31836, 31866, 31842, 31854, 31860, 31848]
acc_items = [31885, 31887, 31883, 31886, 31884,
             31875, 31877, 31873, 31876, 31874,
             31880, 31882, 31878, 31881, 31879,
             31890, 31892, 31888, 31891, 31889]
weap_items = [31823, 31817, 31825, 31821,
              31829,31819, 31828, 31816,
              31820, 31815,31814, 31827,
              31818, 31826, 31824,31822]
item_list = {
}
search = False

def api_grab(item_num):
    api_url = ("https://universalis.app/api/Aether/" + str(item_num))
    page = requests.get(api_url)
    page_data = page.json()
    refine1 = {key: page_data[key] for key in page_data.keys()
           & {"listings"}}

    for pro in refine1:
        new_dict = refine1[pro][4]
        refine2 = {key: new_dict[key] for key in new_dict.keys()
                & {"pricePerUnit"}}
    new1_entry = str(refine2)
    new2_entry = list(map(int, re.findall(r'\d+', new1_entry)))
    new3_entry = new2_entry[0]
    return new3_entry

def search_best():
    i = 0
    while i < len(pld_item):
        item_num = (pld_item[i])
        world_price = api_grab(item_num)
        item_list[int(item_num)] = int(world_price / 21)
        i = i + 1
    i = 0

    while i < len(chest_items):
        item_num = (chest_items[i])
        world_price = api_grab(item_num)
        item_list[int(item_num)] = int(world_price / 42)
        i = i + 1
    i = 0

    while i < len(feet_items):
        item_num = (feet_items[i])
        world_price = api_grab(item_num)
        item_list[int(item_num)] = int(world_price / 33)
        i = i + 1
    i = 0

    while i < len(hands_items):
        item_num = (hands_items[i])
        world_price = api_grab(item_num)
        item_list[int(item_num)] = int(world_price / 33)
        i = i + 1
    i = 0

    while i < len(head_items):
        item_num = (head_items[i])
        world_price = api_grab(item_num)
        item_list[int(item_num)] = int(world_price / 33)
        i = i + 1
    i = 0

    while i < len(leg_items):
        item_num = (leg_items[i])
        world_price = api_grab(item_num)
        item_list[int(item_num)] = int(world_price / 42)
        i = i + 1
    i = 0

    while i < len(waist_items):
        item_num = (waist_items[i])
        world_price = api_grab(item_num)
        item_list[int(item_num)] = int(world_price / 21)
        i = i + 1
    i = 0

    while i < len(acc_items):
        item_num = (acc_items[i])
        world_price = api_grab(item_num)
        item_list[int(item_num)] = int(world_price / 21)
        i = i + 1
    i = 0

    while i < len(weap_items):
        item_num = (weap_items[i])
        world_price = api_grab(item_num)
        item_list[int(item_num)] = int(world_price / 21)
        i = i + 1


    sorted_d = dict( sorted(item_list.items(), key=operator.itemgetter(1)))
    best_prices = list(sorted_d.items())[:15]
    T.insert(tk.END, ("\nThe Cheapest items in order"))

    T.insert(tk.END, ("\nuniversalis.app/market/" + str(best_prices[0]).replace('(', '').replace(')', '').replace(',', '').replace(' ', '  PricePerToken: ')) + \
            ("\nuniversalis.app/market/" + str(best_prices[1]).replace('(', '').replace(')', '').replace(',', '').replace(' ', '  PricePerToken: ')) + \
            ("\nuniversalis.app/market/" + str(best_prices[2]).replace('(', '').replace(')', '').replace(',', '').replace(' ', '  PricePerToken: ')) + \
            ("\nuniversalis.app/market/" + str(best_prices[3]).replace('(', '').replace(')', '').replace(',', '').replace(' ', '  PricePerToken: ')) + \
            ("\nuniversalis.app/market/" + str(best_prices[4]).replace('(', '').replace(')', '').replace(',', '').replace(' ', '  PricePerToken: '))+ \
            ("\nuniversalis.app/market/" + str(best_prices[5]).replace('(', '').replace(')', '').replace(',', '').replace(' ', '  PricePerToken: '))+ \
            ("\nuniversalis.app/market/" + str(best_prices[6]).replace('(', '').replace(')', '').replace(',', '').replace(' ', '  PricePerToken: '))+ \
            ("\nuniversalis.app/market/" + str(best_prices[7]).replace('(', '').replace(')', '').replace(',', '').replace(' ', '  PricePerToken: '))+ \
            ("\nuniversalis.app/market/" + str(best_prices[8]).replace('(', '').replace(')', '').replace(',', '').replace(' ', '  PricePerToken: '))+ \
            ("\nuniversalis.app/market/" + str(best_prices[9]).replace('(', '').replace(')', '').replace(',', '').replace(' ', '  PricePerToken: '))+ \
            ("\nuniversalis.app/market/" + str(best_prices[10]).replace('(', '').replace(')', '').replace(',', '').replace(' ', '  PricePerToken: '))+ \
            ("\nuniversalis.app/market/" + str(best_prices[11]).replace('(', '').replace(')', '').replace(',', '').replace(' ', '  PricePerToken: '))+ \
            ("\nuniversalis.app/market/" + str(best_prices[12]).replace('(', '').replace(')', '').replace(',', '').replace(' ', '  PricePerToken: '))+ \
            ("\nuniversalis.app/market/" + str(best_prices[13]).replace('(', '').replace(')', '').replace(',', '').replace(' ', '  PricePerToken: '))+ \
            ("\nuniversalis.app/market/" + str(best_prices[14]).replace('(', '').replace(')', '').replace(',', '').replace(' ', '  PricePerToken: '))
             )


root = tk.Tk()

canvas = tk.Canvas(root, height=Height, width=Width)
canvas.pack()

frame = tk.Frame(root)
frame.place(relx=0.4, rely=0.05, relwidth=0.2, relheight=0.1)

box = tk.Text(root, bg="white")
box.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.7)

S = tk.Scrollbar(root)
T = tk.Text(root, height=10, width=50)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
T.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.7)
S.place(relx=0.9, rely=0.2, relwidth=0.05, relheight=0.7)

T.insert(tk.END, "After clicking the button, please be patient\nit may take some time to search all exarchic gear:")

button = tk.Button(frame, text="Show Best", command=search_best)
button.pack(expand=True, fill="both")

root.mainloop()
