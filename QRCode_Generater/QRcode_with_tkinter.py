from tkinter import *
import qrcode

window = Tk()
window.title("QRCode Generation")
window.minsize(width=500, height=600)
window.maxsize(width=800, height=800)

l1 = Label(window, text = 'Enter url link for which you want to create a QRCode')
l1.place(x= 5,y=7)
#link = input("Enter url link for which you want to create a QRCode")
e1 = Entry(window,width = 20, bd=1)
e1.place(x=5,y=25)

b1 = Button(window, text="Submit")
b1.place(x=150, y=80)

features = qrcode.QRCode(version=1, box_size=40, border=2)
features.add_data(e1)
features.make(fit=True)
generate_image1 = features.make_image(fill_color="red", back_color='white')
generate_image1.save('link1.png')

generate_image2 = qrcode.make("sample sample")
generate_image2.save('sample.png')

window.mainloop()