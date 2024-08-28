from tkinter import *
import datetime

st=Tk()
st.config(bg='Yellow')
st.title('          *****Digital Clock*****'          )
st.geometry('1000x500')


def date_time():
    time=datetime.datetime.now()
    hr=time.strftime('%H')
    min=time.strftime('%M')
    sec=time.strftime('%S')
    am=time.strftime('%p')
            
    date=time.strftime('%d')
    month=time.strftime('%m')
    year=time.strftime('%y')
    day=time.strftime('%a')

    label_date.config(text=date)
    labal_Mon.config(text=month)
    labal_year.config(text= year)
    labal_day.config(text=day)
    
    label_hr.config(text=hr)
    labal_Min.config(text=min)
    labal_Sec.config(text=sec)
    labal_AM.config(text=am)
    label_hr.after(200,date_time)


# Time code
label_hr=Label(st,text='00',font=('Time New Roman',30,'bold'),bg='red',fg='white')
label_hr.place(x=120,y=50,width=100,height=110)

Label_hr_text=Label(st,text='Hour',font=('Time New Roman',20,'bold'),bg='red',fg='white')
Label_hr_text.place(x=120,y=190,width=100,height=30)


labal_Min=Label(st,text='00',font=('Time New Roman',30,'bold'),bg='red',fg='white')
labal_Min.place(x=320,y=50,width=100,height=110)

Label_min_text=Label(st,text='Min',font=('Time New Roman',20,'bold'),bg='red',fg='white')
Label_min_text.place(x=320,y=190,width=100,height=30)

labal_Sec=Label(st,text='00',font=('Time New Roman',30,'bold'),bg='red',fg='white')
labal_Sec.place(x=520,y=50,width=100,height=110)

Label_Sec_text=Label(st,text='Sec',font=('Time New Roman',20,'bold'),bg='red',fg='white')
Label_Sec_text.place(x=520,y=190,width=100,height=30)


labal_AM=Label(st,text='00',font=('Time New Roman',30,'bold'),bg='red',fg='white')
labal_AM.place(x=720,y=50,width=100,height=110)

Label_am_text=Label(st,text='AM/PM',font=('Time New Roman',20,'bold'),bg='red',fg='white')
Label_am_text.place(x=720,y=190,width=100,height=30)

#Date code
label_date=Label(st,text='00',font=('Time New Roman',30,'bold'),bg='red',fg='white')
label_date.place(x=120,y=270,width=100,height=110)

Label_date_text=Label(st,text='Date',font=('Time New Roman',20,'bold'),bg='red',fg='white')
Label_date_text.place(x=120,y=410,width=100,height=30)

labal_Mon=Label(st,text='00',font=('Time New Roman',30,'bold'),bg='red',fg='white')
labal_Mon.place(x=320,y=270,width=100,height=110)

Label_mon_text=Label(st,text='Month',font=('Time New Roman',20,'bold'),bg='red',fg='white')
Label_mon_text.place(x=320,y=410,width=100,height=30)

labal_year=Label(st,text='00',font=('Time New Roman',30,'bold'),bg='red',fg='white')
labal_year.place(x=520,y=270,width=100,height=110)

Label_year_text=Label(st,text='Year',font=('Time New Roman',20,'bold'),bg='red',fg='white')
Label_year_text.place(x=520,y=410,width=100,height=30)

labal_day=Label(st,text='00',font=('Time New Roman',30,'bold'),bg='red',fg='white')
labal_day.place(x=720,y=270,width=100,height=110)

Label_day_text=Label(st,text='Day',font=('Time New Roman',20,'bold'),bg='red',fg='white')
Label_day_text.place(x=720,y=410,width=100,height=30)





date_time()
st.mainloop()