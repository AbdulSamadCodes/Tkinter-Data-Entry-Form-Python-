import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

window = tkinter.Tk()
window.title("Data Entry Form")

#--------THE MAIN FRAME--------

frame = tkinter.Frame(window)
frame.pack()


# ---- SHOWING USER INFO LABEL FRAME-----------

user_info_frame = tkinter.LabelFrame(frame,text="User information",padx=20,pady=40)
user_info_frame.grid(row=0,column=0)

first_name_label = tkinter.Label(user_info_frame,text="First Name")
first_name_label.grid(row=0 , column=0)

last_name_label = tkinter.Label(user_info_frame,text="Last Name")
last_name_label.grid(row=0 , column=1)

first_name_input = tkinter.Entry(user_info_frame)
last_name_input = tkinter.Entry(user_info_frame)

first_name_input.grid(row = 1 , column=0)
last_name_input.grid(row = 1 , column=1)

gender = tkinter.Label(user_info_frame,text="Gender")
gender.grid(row=0,column=2)

gender_combo = ttk.Combobox(user_info_frame,values=['Male','Female'])
gender_combo.grid(row=1,column=2)

age_label = tkinter.Label(user_info_frame, text="Age") 
age_label.grid(row=2,column=0)

age_spinbox = tkinter.Spinbox(user_info_frame, from_ = 18 , to=110)
age_spinbox.grid(row=3,column=0)

nationality_label = tkinter.Label(user_info_frame,text="Nationality")
nationality_label.grid(row=2,column=1)

nationality_combobox = ttk.Combobox(user_info_frame,values=["Pakistan","India","Australia","England"])
nationality_combobox.grid(row=3,column=1)

#------A loop to give padding in all the parent's childrens widgets

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=5)


#  SAVING COURSE INFO LABEL FRAME-------
    
courses_frame = tkinter.LabelFrame(frame,text="Courses")
courses_frame.grid(row=1,column=0,sticky="news")

courses_registration_label = tkinter.Label(courses_frame,text=" Registration Status")
courses_registration_label.grid(row=0,column=0)


var1 = IntVar()
cr_check = tkinter.Checkbutton(courses_frame,text="Currently Registered",variable=var1, onvalue=1)
cr_check.grid(row=1,column=0)


c_courses = tkinter.Label(courses_frame,text="Completed Courses")
c_courses.grid(row = 0 , column=1)
c_course_spinbox = ttk.Spinbox(courses_frame , from_="0" , to="infinity")
c_course_spinbox.grid(row=1,column=1) 

semesters_label = tkinter.Label(courses_frame,text=" 8 Semesters")
semesters_label.grid(row = 0 , column=2)
semester_spinbox = ttk.Spinbox(courses_frame , from_="1"  , to="8")
semester_spinbox.grid(row=1,column=2) 

#------A loop to give padding in all the parent's childrens widgets

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)


#------------Accept Terms Label Frame
    
terms_frame = tkinter.LabelFrame(frame,text="Terms and conditions")
terms_frame.grid(row=2,column=0 , sticky="news",pady=5)

var2 = IntVar()
terms_check = tkinter.Checkbutton(terms_frame,text="I agree to terms and conditions", variable=var2 , onvalue=2 )
terms_check.grid(row=0,column=0)


#------A loop to give padding in all the parent's childrens widgets

for widget in terms_frame.winfo_children():
    widget.grid_configure(padx=5,pady=8)


#* Method to store data in the file
        
def Storedata():
    if (var2.get() == 2):
     with open("data.txt","a") as file:
        print("---------STUDENT--------")
        file.write("Name: " + first_name_input.get() + " " +  last_name_input.get() + "\n")
        file.write("Gender : " + gender_combo.get() + "\n")
        file.write("Age : " + age_spinbox.get() + "\n" )
        if (var1.get() == 1):
            file.write("Regitered : Currently Registered" + "\n")
        else:
           messagebox.showinfo("You have to be registered first")    
        file.write("Courses completed : " + c_course_spinbox.get() + "\n")
        file.write("Semesters completed " + semester_spinbox.get() + "\n")
        file.write("Nationality : " + nationality_combobox.get() + "\n")
    else:
       messagebox.showinfo("You have to agree with the agreement")    
    print("\n\n")


#------Store Data Button-------
    
store_button = tkinter.Button(window,text="Store data",font=("Sans-Serif",14),command=Storedata)
store_button.pack(anchor="center", pady=1 )  



































window.mainloop()