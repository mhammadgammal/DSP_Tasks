import math
from sklearn import preprocessing
# from QuanTest1 import QuantizationTest1
# from QuanTest2 import QuantizationTest2
import tkinter as tk
from tkinter import ttk
def getdatafile(path):
    with open(path) as f:
        data = f.readlines()
    x_values = []
    y_values = []
    for item in data:
        item = item.strip()
        if ' ' in item:
            x_v, y_v = item.split(' ')
            x_values.append((float(x_v)))
            y_values.append((float(y_v)))
    return x_values, y_values
def task1():
    window1=tk.Tk()
    window1.geometry("300x300")
    l1=tk.Label(window1,text="enter number of bits")
    l1.pack()
    ph = tk.Text(window1, height=1, width=30)
    ph.pack()
    num=0
    def takeinput():
        num=float(ph.get("1.0", "end-1c"))
        x = []
        y = []
        x, y = getdatafile("Quan1_input (1).txt")
        #first
        #clac min
        numb=pow(2,num)
        Min=min(y)
        Max=max(y)
        delta=(Max- Min) / numb
        q=[]
        ra =[]
        tem = Min
        mmm=[]
        nnn=[]
        b=int(num)
        n=int(numb)
        for i in range(int(numb)):
            temp=round(float(tem+delta),4)
            mid=round((temp+tem)/2,4)
            q.append(mid)
            nnn.append(tem)
            tem=temp
            mmm.append(temp)
        for i in range(len(y)):
            for x in range(n):
                if y[i]>=nnn[x] and y[i]<=mmm[x] :
                    ra.append(x)
                    break
        result=[]
        for i in range(len(ra)):
            result.append(q[ra[i]])
        encod=[]
        print(result)
        bin3 = lambda x: ''.join(reversed([str((x >> i) & 1) for i in range(b)]))
        for i in range(len(ra)):
            encod.append(bin3(ra[i]))
        print(encod)
        # QuantizationTest1("Quan1_Out.txt",encod,result)
    b1 = tk.Button(window1, command=takeinput, text="task 1")

    b1.pack()
def task2():
    window1=tk.Tk()
    window1.geometry("300x300")
    l1=tk.Label(window1,text="enter number of Levels")
    l1.pack()
    ph = tk.Text(window1, height=1, width=30)
    ph.pack()
    num=0
    def takeinput():
        num=float(ph.get("1.0", "end-1c"))
        x = []
        y = []
        x, y =getdatafile("Quan2_input.txt")
        #first
        #clac min
        numb=math.log(num,2)
        Min=min(y)
        Max=max(y)
        delta=(Max- Min) / num
        delta=round(delta,3)
        q=[]
        ra =[]
        tem = Min
        mmm=[]
        nnn=[]
        n=int(numb)
        for i in range(len(y)):
            temp=round(float(tem+delta),3)
            mid=round((temp+tem)/2,3)
            q.append(mid)
            nnn.append(tem)
            tem=temp
            mmm.append(temp)

        for i in range(len(y)):
            for x in range(len(y)):
                if y[i]<=mmm[x] and y[i]>=nnn[x]:
                    ra.append(x)
                    break
        result=[]
        for i in range(len(ra)):
            result.append(q[ra[i]])
        encod=[]
        bin3 = lambda x: ''.join(reversed([str((x >> i) & 1) for i in range(n)]))
        for i in range(len(ra)):
            encod.append(bin3(ra[i]))
        er=[]
        for i in range(len(ra)):
            a=float(result[i]-y[i])
            a=round(a,3)
            er.append(a)
        for i in range(len(ra)):
            ra[i]=ra[i]+1
        print(ra)
        print(encod)
        print(result)
        print(er)
        # QuantizationTest2("Quan2_Out.txt",ra,encod,result,er)
    b1 = tk.Button(window1, command=takeinput, text="task 2")
    b1.pack()
def home():
    home=tk.Tk()
    home.geometry("300x100")
    home.title("Welcome to DSP Tasks")
    l1=tk.Label(home,text="do you want task 1 or 2")
    l1.pack()
    b1=tk.Button(home,command=task1,text="task 1")
    b1.pack()
    b2 = tk.Button(home, command=task2, text="task 2")
    b2.pack()
    home.mainloop()
home()