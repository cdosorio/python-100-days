import tkinter as tk
from tkinter import END, Entry, filedialog
from PIL import Image, ImageDraw, ImageFont

def upload_file():
    
    watermark = input_watermark.get()
    f_types = [('Jpg Files', '*.jpg')]
    image_filename = filedialog.askopenfilename(filetypes=f_types)       
    image = Image.open(image_filename)
    
    # Image is converted into editable form using
    # Draw function and assigned to draw
    draw = ImageDraw.Draw(image)  

    # Determine a font size based on image size
    fontsize = 1  # starting font size
    # portion of image width you want text width to be
    img_fraction = 0.50
    font = ImageFont.truetype("arial.ttf", fontsize)
    while font.getsize(watermark)[0] < img_fraction*image.size[0]:
        # iterate until the text size is just larger than the criteria
        fontsize += 1
        font = ImageFont.truetype("arial.ttf", fontsize)

    # optionally de-increment to be sure it is less than criteria
    fontsize -= 1
    font = ImageFont.truetype("arial.ttf", fontsize)
    print('final font size',fontsize)

    font = ImageFont.truetype("arial.ttf", fontsize, encoding="unic")
    draw.text((0, 0), watermark, fill = (255, 255, 255), font=font)
    image.show()


window = tk.Tk()
window.geometry("400x200")  # Size of the window 
window.title('Watermark')
my_font1=('times', 16, 'bold')

button_upload = tk.Button(window, text='Upload Image', 
   width=20,command = lambda:upload_file())
button_upload.grid(row=2, column=0, columnspan=2) 

label_watermark = tk.Label(window,text='Watermark:', font=my_font1)  
label_watermark.grid(row=3,column=0)

input_watermark = Entry(width=35)
input_watermark.grid( row=3, column=1)
input_watermark.insert(END , "Your watermark")


window.mainloop()