from tkinter import *
from tkinter import messagebox
import phonenumbers as pn 
from phonenumbers import geocoder, carrier, timezone
from PIL import ImageTk,Image

Root = Tk()
Root.geometry("670x1150") 
Root.title("Phone Number tracker")
Root.config(bg="#fff")
H = Root.winfo_screenheight()
W = Root.winfo_screenwidth()
w = W-50
h = H-82
Root.maxsize(w, h)
Root.minsize(w, h)


def get():
	# phon number 
	n = Inp.get()
	ln = len(n)
	#print(ln)
	if(ln<10 or ln>10):
		messagebox.showwarning("Phone Number Tracker", "Invalid number")
		

	a = "+91"
	gnum = a+n
	r = pn.parse(gnum)
	
	F = Frame(Root, width=620, height=250, bg="#fff")
	F.place(x=20, y=430)
	
	rl = Label(F, text=r, font="Arial 6 bold", fg="#111542", bg="#fff")
	rl.place(x=20, y=20)
	
	# geocoder 
	G = geocoder.description_for_number(r, "en")
	gl = Label(F, text="Location : "+G, font="Arial 6 bold", fg="#111542", bg="#fff")
	gl.place(x=20, y=80)
	
	# Carrier
	C = carrier.name_for_number(r, "en")
	cl = Label(F, text="Network : "+C, font="Arial 6 bold", fg="#111542", bg="#fff")
	cl.place(x=20, y=120)
	
	# timezone 
	T = timeZone = timezone.time_zones_for_number(r)
	t = Label(F, text="Timezone : ", font="Arial 6 bold", fg="#111542", bg="#fff")
	t.place(x=20, y=160)
	tl = Label(F, text=T, font="Arial 6 bold", fg="#111542", bg="#fff")
	tl.place(x=160, y=160)
	
	Inp.delete(0, "end")

	

canvas = Canvas(Root, width = 670, height = 1150)
canvas.place(x=0, y=0)

N = Label(text="Phone Number Tracker", fg="#111542", font="Arial 12 bold", bg="#fff")
N.place(x=50, y=50)

number = Label(text="Mobile Number :", bg="#fff")
number.grid(row=0, column=0, pady=200, padx=10)

Inp = Entry(width=18)
Inp.grid(row=0, column=1, pady=200)

btn = Button(text="TRACK", bg="blue", fg="#fff", font="Arial 12 bold", command=get)
btn.place(x=50, y=300)

	# Exit
exit = Button(text="EXIT", bg="red", fg="#fff", width=6, font="Arial 12 bold", command=quit)
exit.place(x=345, y=300)

img = (Image.open("/storage/emulated/0/Download/t.png"))

resized_image= img.resize((w,h), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)

#Add image to the Canvas Items
canvas.create_image(0,0, anchor=NW, image=new_image)
 


Root.mainloop() ;
