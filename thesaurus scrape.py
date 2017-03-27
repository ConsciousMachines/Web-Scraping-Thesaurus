from tkinter import *
import time
import urllib.request
from bs4 import BeautifulSoup
import turtle 
root = Tk()


page = Label(master=None)
page.place(x=0, y=0, relwidth=1, relheight=1)
def callback(event):
    print( ("clicked at", event.x, event.y))

frame = Frame(root, width=100, height=100)
frame.bind("<Button-1>", callback)
frame.pack()

b = Button(master=None, text="Click me", compound=CENTER)

# FONT SIZES
size1 = 40
size2 = 20
size3 = 10
arg = "superb"




def do():
    canv_width = 1000
    canv_height =720
    canv = Canvas(root,width=canv_width,height=canv_height)#highlightthickness=0
    canv.pack(fill='both', expand=True)
    y_d = int((1/40)*canv_height)
    x_d = int(canv_width/2)
    canv.create_text((x_d,y_d),text=arg,font=("ESSTIXFifteen "+str(size1)))
    # MAIN DEF 
    total = 0
    for i in range(len(main_syns)):
        total += len(main_syns[i])
    y_desc = int((1/10)*canv_height)
    x_desc = int( canv_width/(len(desc)+1))
    twerk = range(len(desc))
    for i in twerk:
        # sev slope gen
        canv.create_text(((i+1)*x_desc, y_desc),text=desc[i],font=("Harrington "+str(size2)) )
        for j in range(len(main_syns[i])):
            canv.create_text(((i+1)*x_desc, 10+(j+1)*20+y_desc),text=main_syns[i][j],font=("Ubuntu "+str(size3)))
    canv.update()
            
        

    ball = canv.create_oval(0, 20, 20, 40, outline='black', fill='gray40', tags=('ball'))

    delta_x = delta_y = 3
    new_x, new_y = delta_x, -delta_y
    while True:
        time.sleep(0.005)
        if canv.find_overlapping(canv.coords(ball)[0], canv.coords(ball)[1], canv.coords(ball)[2], canv.coords(ball)[3])[0] == 1:
            new_x, new_y = delta_x, -delta_y
            canv.move(ball, new_x, new_y)
            print( 'fitst if', new_x, new_y)
        if canv.find_overlapping(canv.coords(ball)[0], canv.coords(ball)[1], canv.coords(ball)[2], canv.coords(ball)[3])[0] == 2:
            new_x, new_y = delta_x, delta_y
            canv.move(ball, new_x, new_y)
            print( '2nd if', new_x, new_y)
        if canv.find_overlapping(canv.coords(ball)[0], canv.coords(ball)[1], canv.coords(ball)[2], canv.coords(ball)[3])[0] == 3:
            new_x, new_y = -delta_x, delta_y
            canv.move(ball, new_x, new_y)
        if canv.find_overlapping(canv.coords(ball)[0], canv.coords(ball)[1], canv.coords(ball)[2], canv.coords(ball)[3])[0] == 4:
            new_x, new_y = delta_x, -delta_y
            canv.move(ball, new_x, new_y)
        print( new_x, new_y)
        canv.move(ball, new_y, new_y)
        canv.update()

def move_right(event):
        canv.move(rect, 7, 0)




















def vs(word,which):
    # SET UP PAGE
    pagu = "http://www.thesaurus.com/browse/"+word
    pagu2 = urllib.request.urlopen(pagu)
    soup = BeautifulSoup(pagu2,"html.parser")

    # MAIN HEADER AND DEFINITIONS
    definitions = []
    elements = soup.find_all("div", class_="synonym-description".split())
    for el in elements:
        yoyo = el.get_text()
        definitions.append(yoyo.strip())
    # MAIN CONTENT
    elements = soup.find_all("div", class_="synonyms")
    num_maj_syns = len(elements)
    maj_syns_indices = []
    all_words = []
    for i in range(num_maj_syns):   
        maj_syns_indices.append("synonyms-"+str(i))
    for i in range(num_maj_syns):
        elements = soup.find_all("div",id=maj_syns_indices[i])
        soup2_0 = BeautifulSoup(str(elements),"html.parser")
        soup2 = soup2_0.find_all("span", class_="text")
        wurdz = []
        for j in soup2:
            yoyo = j.get_text()
            wurdz.append(yoyo)
        all_words.append(wurdz)
    print("DONE ZONE")
                 
    # SYN OF SYNS CONTENT
    elements = soup.find_all("div", class_="box syn_of_syns oneClick-area")
    num_syn_of_syn_sets = len(elements)
    syn_of_syns_indices = []
    for i in range(num_syn_of_syn_sets):
        syn_of_syns_indices.append("synonym_of_synonyms_"+str(i))
    syn_of_syns_names = []
    syn_of_syns_descriptions = []
    syn_of_syns_content = []
    for i in range(num_syn_of_syn_sets): 
        elements = soup.find_all("div", id=syn_of_syns_indices[i])
        shitt = []
        for el in elements:
            soup2_0 = BeautifulSoup(str(el),"html.parser")
            soup2_1 = soup2_0.find_all("div", {'data-linkid':"nn1ov4"})
            soup2 = BeautifulSoup(str(soup2_1),"html.parser")
            name = soup2.find("div", class_="subtitle")
            name = name.a.get_text()
            syn_of_syns_names.append(name)
            #print(name)
            desc = soup2.find("div",class_="def").get_text()
            syn_of_syns_descriptions.append(desc)
            #print(desc)
            syns = soup2.find_all(class_="syn_of_syns")
            for i in syns:
                shit = i.get_text()
                shitt.append(shit)
        syn_of_syns_content.append(shitt)
    #print(syn_of_syns_content)
    if which == 0:
        return definitions
    if which == 1:
        return all_words
    if which == 2:
        return [syn_of_syns_names,syn_of_syns_descriptions]
    if which == 3:
        return syn_of_syns_content


desc = vs(arg,0)
main_syns = vs(arg,1)
sos = vs(arg,2)
sofs = vs(arg,3)



do()



turtle.setx(int(canv_width/2))
turtle.sety(int((1/20)*canv_height))
turtle.forward(15)
turtle.right(45)
turtle.forward(10)


