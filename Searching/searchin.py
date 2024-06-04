import sys, os
sys.path.append(os.path.join(sys.path[0], 'searchin/'))

import pandas       as pd
import tkinter      as tk
import funckie      as fc

mus = pd.read_csv('artists.csv')

wiget = tk.Tk()
a=500
b=int(0.618*a)
wiget.title('Enter request')
wiget.geometry(f'{a}x{b}')
wiget.resizable(width=False, height=False)
wiget['bg'] = 'grey9'

def ret(event):
    fc.seek_for_machine(message.get(), out, mus, 'artist')


tk.Label(wiget,
         bg = 'CadetBlue1', 
         text='Enter Name').pack()

message = tk.StringVar()

entry = tk.Entry(wiget,
                 textvariable=message)

entry.focus_set()

btn = tk.Button(wiget, 
                relief='groove', 
                text='Search', 
                bg = 'darkseagreen1',
                command=lambda: fc.seek_for_machine(message.get(), out, mus, 'artist'))

out = tk.Text(wiget,
              width=55,
              height=10,
              bg='black', 
              fg='lime', 
              relief='groove',
              highlightthickness=0)

entry.pack()
btn.pack()
out.pack()

wiget.bind('<Escape>', lambda event: wiget.destroy())
wiget.bind('<Return>', ret)

tk.mainloop()


# USED FUNCTION
def seek_for_machine(piece, disp, dframe, col):     # MODIFIED 'SEEK' SOR SEARCHING_MACHINE
    name_list = dframe[col].dropna().drop_duplicates().reset_index(drop=True).tolist()
    try:
        disp.delete(1.0, 'end')
        for i in name_list:
            if i != None and i.lower().find(piece.lower()) >= 0:
                disp.insert(1.0, f'{name_list.index(i)+1} {i} \n')
    except:
        disp.insert(1.0, 'find an error in code')
        tk.mainloop()