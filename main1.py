from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Face_Recognition_System:
      def __init__(self,root):
            self.root=root
            self.root.geometry("1530x790+0+0")
            self.root.title("Face Recognition System")

            #first image
            img=Image.open(r"C:\Users\user\OneDrive\Desktop\Face_Recognition_System\college images/10450447.webp") 
            img=img.resize((500,130))
            self.photoimg=ImageTk.PhotoImage(img)

            f_lbl=Label(self.root,image=self.photoimg)
            f_lbl.place(x=0,y=0,width=500,height=130)
            #second image
            img1=Image.open(r"C:\Users\user\OneDrive\Desktop\Face_Recognition_System\college images/OIP.jpeg") 
            img1=img1.resize((500,130))
            self.photoimg1=ImageTk.PhotoImage(img1)

            f_lbl=Label(self.root,image=self.photoimg1)
            f_lbl.place(x=500,y=0,width=500,height=130)
      
            #third image
            img2=Image.open(r"C:\Users\user\OneDrive\Desktop\Face_Recognition_System\college images/10450447.webp") 
            img2=img2.resize((500,130))
            self.photoimg2=ImageTk.PhotoImage(img)

            f_lbl=Label(self.root,image=self.photoimg)
            f_lbl.place(x=1000,y=0,width=500,height=130)

            #background image
            img3=Image.open(r"C:\Users\user\OneDrive\Desktop\Face_Recognition_System\college images/OIP (1).jpeg") 
            img3=img3.resize((1530,710))
            self.photoimg3=ImageTk.PhotoImage(img3)

            bg_img=Label(self.root,image=self.photoimg3)
            bg_img.place(x=0,y=130,width=1530,height=710)


            title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE",font=("time new romen",35,"bold"),bg="white",fg="black")
            title_lbl.place(x=0,y=0,width=1530,height=45)


           #student button
            img4=Image.open(r"C:\Users\user\OneDrive\Desktop\Face_Recognition_System\college images/istockphoto-1461630610-612x612.jpg") 
            img4=img4.resize((220,220))
            self.photoimg4=ImageTk.PhotoImage(img4)

            b1=Button(bg_img,image=self.photoimg4,cursor="hand2")
            b1.place(x=200,y=100,width=220,height=220)

            b1_1=Button(bg_img,text="Student Details",cursor="hand2",font=("time new romen",15,"bold"),bg="darkblue",fg="white")
            b1_1.place(x=200,y=300,width=220,height=40)

            #Detect Face Button

            img5=Image.open(r"C:\Users\user\OneDrive\Desktop\Face_Recognition_System\college images/face.jpg") 
            img5=img5.resize((220,220))
            self.photoimg5=ImageTk.PhotoImage(img5)

            b1=Button(bg_img,image=self.photoimg5,cursor="hand2")
            b1.place(x=500,y=100,width=220,height=220)

            b1_1=Button(bg_img,text="Face Detector",cursor="hand2",font=("time new romen",15,"bold"),bg="darkblue",fg="white")
            b1_1.place(x=500,y=300,width=220,height=40)

            #Attendence face System
            img6=Image.open(r"C:\Users\user\OneDrive\Desktop\Face_Recognition_System\college images/Telpo-TPS980-face-recognition-machine.jpg") 
            img6=img6.resize((220,220))
            self.photoimg6=ImageTk.PhotoImage(img6)

            b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
            b1.place(x=800,y=100,width=220,height=220)

            b1_1=Button(bg_img,text="Attendence",cursor="hand2",font=("time new romen",15,"bold"),bg="darkblue",fg="white")
            b1_1.place(x=800,y=300,width=220,height=40)

            #Help face button
            img7=Image.open(r"C:\Users\user\OneDrive\Desktop\Face_Recognition_System\college images/OIP (4).jpeg") 
            img7=img7.resize((220,220))
            self.photoimg7=ImageTk.PhotoImage(img7)

            b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
            b1.place(x=1100,y=100,width=220,height=220)

            b1_1=Button(bg_img,text="Help",cursor="hand2",font=("time new romen",15,"bold"),bg="darkblue",fg="white")
            b1_1.place(x=1100,y=300,width=220,height=40)

            #Train face button
            img8=Image.open(r"C:\Users\user\OneDrive\Desktop\Face_Recognition_System\college images/OIP (2).jpeg") 
            img8=img8.resize((220,220))
            self.photoimg8=ImageTk.PhotoImage(img8)

            b1=Button(bg_img,image=self.photoimg8,cursor="hand2")
            b1.place(x=200,y=380,width=220,height=220)

            b1_1=Button(bg_img,text="Train",cursor="hand2",font=("time new romen",15,"bold"),bg="darkblue",fg="white")
            b1_1.place(x=200,y=580,width=220,height=40)

            #Photos face system

            img9=Image.open(r"C:\Users\user\OneDrive\Desktop\Face_Recognition_System\college images/group-of-business-people-during-break-from-the-work-taking-selfie-picture-while-enjoying-free-time-in-relaxation-area-at-modern-open-plan-startup-office-selective-focus-.jpg") 
            img9=img9.resize((220,220))
            self.photoimg9=ImageTk.PhotoImage(img9)

            b1=Button(bg_img,image=self.photoimg9,cursor="hand2")
            b1.place(x=500,y=380,width=220,height=220)

            b1_1=Button(bg_img,text="Photos",cursor="hand2",font=("time new romen",15,"bold"),bg="darkblue",fg="white")
            b1_1.place(x=500,y=580,width=220,height=40)

            #Developer face system

            img10=Image.open(r"C:\Users\user\OneDrive\Desktop\Face_Recognition_System\college images/developer2_ai_open_file_dribbble-01_4x.webp") 
            img10=img10.resize((220,220))
            self.photoimg10=ImageTk.PhotoImage(img10)

            b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
            b1.place(x=800,y=380,width=220,height=220)

            b1_1=Button(bg_img,text="Developer",cursor="hand2",font=("time new romen",15,"bold"),bg="darkblue",fg="white")
            b1_1.place(x=800,y=580,width=220,height=40)


            #Exit face sysytem
            img11=Image.open(r"C:\Users\user\OneDrive\Desktop\Face_Recognition_System\college images/OIP (3).jpeg") 
            img11=img11.resize((220,220))
            self.photoimg11=ImageTk.PhotoImage(img11)

            b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
            b1.place(x=1100,y=380,width=220,height=220)

            b1_1=Button(bg_img,text="Exit",cursor="hand2",font=("time new romen",15,"bold"),bg="darkblue",fg="white")
            b1_1.place(x=1100,y=580,width=220,height=40)










if __name__=="__main__":
      root=Tk()
      obj=Face_Recognition_System(root)
      root.mainloop()