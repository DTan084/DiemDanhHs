# đn ok
from PIL import Image, ImageTk,ImageDraw
from tkinter import *
from tkinter import ttk
import PIL.Image ,PIL.ImageDraw
import mysql.connector
from tkinter import messagebox
from main import Face_Recognition_System
from main import new_print

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Đăng nhập")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")

        self.var_email = StringVar()
        self.var_password = StringVar()

        self.bg_image = PIL.Image.open(r"ImageFaceDetect\b2.jpg")
        self.bg_image = self.bg_image.resize((1350, 700), PIL.Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        bg_lbl = Label(self.root, image=self.bg_photo)
        bg_lbl.place(x=0, y=0, width=1350, height=700)

        #Frame
        login_frame=Frame(self.root,bg="white")
        login_frame.place(x=275,y=150,width=800,height=400)
        #style_ttk.tentry
        self.estyle = ttk.Style()
        self.estyle.configure("EntryStyle.TEntry", background='black')

        title=Label(login_frame,text="Đăng nhập ",font=("times new roman",24,"bold"),bg="white",fg="black").place(x=350,y=50)

        email = Label(login_frame, text="Email", font=("times new roman", 18, "bold"), bg="white",
                      fg="black").place(x=250, y=130)
        self.txtuser=ttk.Entry(login_frame,textvariable=self.var_email, font=("times new roman", 16))
        self.txtuser.place(x=250, y=160,height=35,width=300)

        pass_word = Label(login_frame, text="Mật khẩu", font=("times new roman", 18, "bold"), bg="white",
                      fg="black").place(x=250, y=200)
        self.txtpass = ttk.Entry(login_frame, textvariable=self.var_password,font=("times new roman", 16), background="black" ,show="*")
        self.txtpass.place(x=250, y=230,height=35,width=300)

        #check_button
        self.varcheck = IntVar()
        checkbtn = Checkbutton(login_frame, variable=self.varcheck, text="Đăng nhập bằng tài khoản Admin",
                               font=("times new roman", 12), onvalue=1, offvalue=0)
        checkbtn.place(x=250, y=270)

        btn_login = Button(login_frame, text="Đăng nhập", command=self.login,font=("times new roman", 18,"bold"), fg="white", bd=0,
                            bg="#B00857",cursor="hand2").place(x=300, y=310,width=220,height=40)

    def reset(self):
        self.var_email.set("")
        self.var_password.set("")
        self.varcheck.set(0)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Lỗi !!","Vui lòng nhập đầy đủ thông tin")
        elif(self.varcheck.get()==1) :
            conn = mysql.connector.connect(host='localhost', user='root', password='', database='face_recognizer',
                                           port='3306')
            my_cursor = conn.cursor()
            my_cursor.execute("select * from admin where Account=%s and Password=%s", (
                self.var_email.get(),
                self.var_password.get()
            ))
            row = my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Lỗi", "Sai tên đăng nhập, mật khẩu hoặc quyền đăng nhập")
            else:
                new_print(str(0))
                self.reset()
                messagebox.showinfo("Thông báo","Bạn đã đăng nhập thành công với quyền Admin")
                self.new_window = Toplevel(self.root)
                self.app = Face_Recognition_System(self.new_window)
            conn.commit()
            conn.close()
        else:
            conn = mysql.connector.connect(host='localhost', user='root', password='', database='face_recognizer',
                                           port='3306')
            my_cursor = conn.cursor()
            my_cursor.execute("select Teacher_id from teacher where Email=%s and Password=%s",(
                                    self.var_email.get(),
                                    self.var_password.get()
            ))
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Lỗi", "Sai tên đăng nhập hoặc mật khẩu")
            else:
                new_print(str(row[0]))
                self.reset()
                self.new_window = Toplevel(self.root)
                self.app = Face_Recognition_System(self.new_window)
            conn.commit()
            conn.close()
if __name__=="__main__":
    root=Tk()
    obj=Login_Window(root)
    root.mainloop()