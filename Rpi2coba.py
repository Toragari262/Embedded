import socket
##import RPi.GPIO as GPIO
from tkinter import *
import time
import threading

##GPIO.setmode(GPIO.BCM)
##GPIO.setwarnings(False)

root = Tk()
root.geometry('1100x510+50+100')
root.title('embeden UAS 20-05,20-09,20-17')
root.resizable(width=False, height=False)
root.configure(bg='black')
root.grid()

#frame  ==================================================================

fr1 = Frame(root, width=840, height=50, bg='grey')
fr1.grid(row=0, column=0, pady=0, padx=0)
fr1.grid_propagate(0)

fr2 = Frame(root, width=840, height=450, bg='grey')
fr2.grid(row=1, column=0, pady=5, padx=0)
fr2.grid_propagate(0)

fr3 = Frame(root, width=110, height=450, bg='grey')
fr3.grid(row=1, column=1, pady=5, padx=5)
fr3.grid_propagate(0)

fr4 = Frame(root, width=110, height=450, bg='grey')
fr4.grid(row=1, column=2, pady=5, padx=5)
fr4.grid_propagate(0)

fr10 = Frame(root, width=230, height=50, bg='grey')
fr10.grid(row=0, column=1, columnspan=2, pady=0, padx=0)
fr10.grid_propagate(0)

#text box  ==================================================================

from tkinter.scrolledtext import ScrolledText
txt_box1 = ScrolledText(fr3, width=11, height=20, bg='light grey')
txt_box1.grid(row=2, column=1,pady=2,padx=2)
txt_box2 = ScrolledText(fr1, width=15, height=2, bg='light grey')
txt_box2.grid(row=0, column=7,pady=2,padx=2)
txt_box3 = ScrolledText(fr4, width=11, height=20, bg='light grey')
txt_box3.grid(row=2, column=1,pady=2,padx=2)

#LED =======================================================================

cl1 = Canvas(fr1, width=50, height=50, bg='ivory')
cl1.grid(row=0, column=2, pady=2, padx=2)
cl2 = Canvas(fr1, width=50, height=50, bg='ivory')
cl2.grid(row=0, column=3, pady=2, padx=2)
cl3 = Canvas(fr1, width=50, height=50, bg='ivory')
cl3.grid(row=0, column=4, pady=2, padx=2)
cl4 = Canvas(fr1, width=50, height=50, bg='ivory')
cl4.grid(row=0, column=5, pady=2, padx=2)

#button  ==================================================================

btt= Button(fr1, width=15)
btt.grid(row=0, column=0, padx=5, pady=5, sticky=W+E)

ld1=cl1.create_rectangle(5,5, 45,45, fill='white', outline='black', width=2)
ld2=cl2.create_rectangle(5,5, 45,45, fill='white', outline='black', width=2)
ld3=cl3.create_rectangle(5,5, 45,45, fill='white', outline='black', width=2)
ld4=cl4.create_rectangle(5,5, 45,45, fill='white', outline='black', width=2)

#canvas  ==================================================================

cv1 = Canvas(fr2, width=70, height=380, bg='white')
cv1.grid(row=0, column=0, pady=2, padx=2)
cv2 = Canvas(fr2, width=374, height=380, bg='white')
cv2.grid(row=0, column=1, pady=2, padx=0)
cv3 = Canvas(fr2, width=374, height=380, bg='white')
cv3.grid(row=0, column=2, pady=2, padx=0)
cv4 = Canvas(fr2, width=70, height=70, bg='white')
cv4.grid(row=1, column=0, pady=0, padx=2)
cv5 = Canvas(fr2, width=374, height=70, bg='white')
cv5.grid(row=1, column=1, pady=0, padx=0)
cv6 = Canvas(fr2, width=374, height=70, bg='white')
cv6.grid(row=1, column=2, pady=0, padx=0)

#label  ==================================================================

lb2 = Label (fr2, width=5, height=3, text='lb2', bg='white')
lb2.grid(row=1, column=0, padx=2, pady=2, sticky=W+E)
lb3= Label (fr3, width=10, height=3, text='Data 1')
lb3.grid(row=0, column=1, padx=2, pady=2 )
lb4 = Label (fr1, width=10, height=3, text='Counter')
lb4.grid(row=0, column=6, padx=(20,2), pady=2 )
lb5 = Label (fr4, width=10, height=3, text='Data 2')
lb5.grid(row=1, column=1, padx=2, pady=2 )
lb6 = Label (fr10, width=18, height=2, text='RASPI 2', font=("Calibri",15))
lb6.grid(row=1, column=1, padx=2, pady=2, sticky=W+E+S+N)

def fs_ms1(event):
    a=event.x 
    b=event.y
    af=str('{:.2f}'.format(a))
    bf=str('{:.2f}'.format(b))
    lb2.configure(text=str(a)+','+str(b))
cv2.bind('<Motion>', fs_ms1)
cv3.bind('<Motion>', fs_ms1)

cv2.create_text( 20, 15,  text='Data1', font=('calibri',12))
cv3.create_text( 20, 15,  text='Data2', font=('calibri',12))

for i in range (11):
    cv1.create_text(35,380-40*i, text=i*40)
    cv5.create_text(i*40+4,35, text=i)
    cv6.create_text(i*40+4,35, text=i) 
    cv2.create_line(i*40,0,i*40,380,fill='Red',width=2)
    cv2.create_line(0,i*38,380,i*38,fill='Red',width=2)
    cv3.create_line(i*40,0,i*40,380,fill='blue',width=2)
    cv3.create_line(0,i*38,380,i*38,fill='blue',width=2)
    # cv2.create_line(i * 20 + 2, 380, i * 20 + 2, 380 - 40, fill='green', width=5)

#============================================================================
btn = [24,18]  
led = [19,16,26,20]
led2 = [[19,16],[26,20]]

# Mengatur GPIO sebagai input
##GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
##GPIO.setup(led, GPIO.OUT)

counter = 0

# Fungsi callback saat push button ditekan
##def button_callback(channel):
##    global counter
##    counter += 1
##    txt_box2.insert(END,"counter:" +str(counter)+"\n")
##    lb4.config(text= "Counter"+ "\n"+ "(+)")
##    GPIO.output(led2[0], GPIO.HIGH)
##    GPIO.output(led2[1], GPIO.LOW)
##    cl1.itemconfig(ld1,fill="red")
##    cl2.itemconfig(ld2,fill="red")
##    cl3.itemconfig(ld3,fill="white")
##    cl4.itemconfig(ld4,fill="white")
##    txt_box2.yview(END)
##    
##def button_callback2(channel):
##    global counter
##    counter -= 1  
##    txt_box2.insert(END,"counter:" +str(counter)+"\n")
##    lb4.config(text= "Counter"+ "\n"+ "(-)")
##    GPIO.output(led2[1], GPIO.HIGH)
##    GPIO.output(led2[0], GPIO.LOW)
##    cl1.itemconfig(ld1,fill="white")
##    cl2.itemconfig(ld2,fill="white")
##    cl3.itemconfig(ld3,fill="red")
##    cl4.itemconfig(ld4,fill="red")
##
##GPIO.add_event_detect(btn[0], GPIO.FALLING, callback=button_callback, bouncetime=200)
##GPIO.add_event_detect(btn[1], GPIO.FALLING, callback=button_callback2, bouncetime=200)

pendengar = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
alamat1=('192.168.1.64',8000)

pengirim = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
alamat2=('192.168.1.67',8080)
pengirim.bind(alamat1)

loop_active = True
grs = [0] * 20
s = 0

def toggle_loop():
    global loop_active
    if not loop_active:
        loop_active = True
        thread = threading.Thread(target=loop)
        thread.start()
        btt.config(text="Nonaktifkan Loop")
    else:
        loop_active = False
        btt.config(text="Aktifkan Loop")

def loop():
    global s
    global z
    while loop_active:
        try:
            pesan = pengirim.recvfrom(1024)
            z = pesan[0].decode().split(",")
            txt_box1.insert(END, z[0]+"\n")
            txt_box3.insert(END, z[1]+"\n")
            b = int(z[0])
            c = int(z[1])
            if s == 0:
                for line in grs:
                    if line != 0:
                        cv2.delete(line)
                        cv3.delete(line)
            grs[s] = cv2.create_line(s * 20 + 2, 380, s * 20 + 2, 380 - b, fill='green', width=5)
            grs[s] = cv3.create_line(s * 20 + 2, 380, s * 20 + 2, 380 - c, fill='green', width=5)
            txt_box1.yview(END)
            txt_box3.yview(END)
            s = (s + 1) % 20
        except socket.timeout:
            pass

toggle_loop()
btt.config(command=toggle_loop)

root.after(1000, loop)
root.mainloop()