# datetime tuple

# from datetime import date
# ## Create the instance
# today = date(2019, 5, 12)
# print("Date:", today)
# time_tuple = today.timetuple()
# # print time_tupe 
# print("\n date object's tuple:\n", time_tuple)
# # printing elements as tuple
# print("\nSpecific elements of this tuple can also be accessed: ")
# attributes = ['tm_year', 'tm_mon','tm_mday', 'tm_hour',
#                 'tm_min', 'tm_sec', 'tm_wday', 'tm_yday',
#                 'tm_isdst']
# i= 0
# for t in time_tuple:
#     print(attributes[i], "=",t)
#     i+=1


# tk horloge

from tkinter import *
from time import strftime
root = Tk()
root.geometry("500x500")
root.resizable(0,0)
root.title('Python Clock')
# Label(root,text = 'Test', font ='arial 20 bold').pack(side=BOTTOM)
def time():
    string = strftime('%H:%M:%S %p')
    mark.config(text = string)
    mark.after(1000, time)
mark = Label(root, 
            font = ('calibri', 40, 'bold'),
            pady=150,
            foreground = 'black')
mark.pack(anchor = 'center')
time()

mainloop()