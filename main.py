# pip install trilio
from twilio.rest import Client
from tkinter import *


# function for message sending
def Se_nd(contact,text):
    
    client=Client(acc_sid,token)
    print(contact.get())
# SENDING MESSAGE
    message = client.messages.create(body=text.get(),from_="whatsapp:+14155238886",to=f"whatsapp:{contact.get()}")  
# CONFORMING MESSAGE
    print("Sent")
  



window = Tk();
window.geometry("400x300")

# important 
token="a67fb68c8f4f2e4a84c5e2bafee7d058"
acc_sid="ACbdacbfeff55f0f6b5a15429dd1df787a"


# MAKING GUI

question1=Label(window,text="To whom would you like to send message? (Add country code too) : \n",font=("times",10,"bold"))
question1.grid(row=0,column=0)
contact=StringVar()
answer=Entry(window,textvariable=contact)
answer.grid(row=2,column=0)

question2=Label(window,text="What do u want to send? : \n",font=("times",10,"bold"))
question2.grid(row=6,column=0)
    
text=StringVar();
answer2=Entry(window,textvariable=text);
answer2.grid(row=8,column=0)



b1=Button(window,fg="grey",text="Submit",command=lambda:Se_nd(contact,text))
b1.grid(row=10,column=0)
window.mainloop()