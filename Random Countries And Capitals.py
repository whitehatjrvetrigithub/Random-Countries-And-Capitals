from tkinter import*
import random
root=Tk()
root.title ("Random Country and Capital")
root.geometry("500x500")
root.configure (background="snow")

country_names=Entry(root)
country_names.place (relx=0.5, rely=0.1, anchor=CENTER)
capital_names=Entry(root)
capital_names.place (relx=0.5, rely=0.2, anchor=CENTER)
country_list=Label(root)
capital_list=Label(root)
random_country_list=Label(root)
random_capital_list=Label(root)

country=[]
capital=[]  

def ccname():
    added_country_name=country_names.get()
    country.append(added_country_name)
    country_list["text"]="Country Name: "+str(country)
    added_capital_name=capital_names.get()
    capital.append (added_capital_name)
    capital_list["text"]="City Name: "+str(capital)


def random_number():
    length1=len(country)
    random_no1=random.randint(0,length1-1)
    random_country=country[random_no1]
    random_country_list["text"]="Random Country is:"+str(random_country)
    length2=len(capital)
    random_no2=random.randint(0,length2-1)
    random_capital=capital[random_no2]
    random_capital_list["text"]="Random Capital is: "+str(random_capital)

btn=Button(root,text="Display Country and City Name", command=ccname,bg="Lightblue",fg="white")
btn.place(relx=0.5,rely=0.3,anchor=CENTER)
country_list.place(relx=0.5,rely=0.4, anchor=CENTER)
capital_list.place(relx=0.5,rely=0.5, anchor=CENTER)
btn1=Button(root, text="Display Country and City Name Randomly", command=random_number,bg="Lightblue",fg="white",)
btn1.place(relx=0.5,rely=0.6, anchor=CENTER)
random_country_list.place(relx=0.5,rely=0.7, anchor=CENTER)
random_capital_list.place(relx=0.5, rely=0.8,anchor=CENTER)




root.mainloop()