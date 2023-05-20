import webbrowser
import tkinter as tk

def search_website():
    query = input.get()
    query = query.replace(' ', '+')
    url = f"https://www.okazii.ro/cautare/{query}.html"
    webbrowser.open(url)


window = tk.Tk()
window.title("Website Search")
window.geometry("300x500")  


window.configure(padx=10, pady=100, bg='black')

header = tk.Label(window, text="Search")
header.pack()
header.config(font=("Courier", 20))
header.config(fg="white")
header.config(bg="black")


input = tk.Entry(window, width=30)
input.pack(pady=10)


buton = tk.Button(window, text="Submit", command=search_website,width=15)
buton.pack(pady=5)


window.mainloop()
