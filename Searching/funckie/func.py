import pandas       as pd

import tkinter      as tk


def deep_dict(list_of_dicts):           # DEEPCOPY OF DICTIONARY
    new_dict = []
    for row in list_of_dicts:
        main = {}
        for key in row:
            main[key] = row.get(key)
        new_dict.append(main)
    return new_dict


def deep_list(list_of_lists):           # DEEPCOPY OF LIST OF LISTS
    new_list = []
    for row in list_of_lists:
        main = []
        for col in row:
            main.append(col)
        new_list.append(main)
    return new_list


def seek(pieces_list, what_list):             # SEARCHIN' OBJECTS FROM LIST BY PIECE
    matches = []
    for i in what_list:
        for a in pieces_list:
            if i != None and i.find(a) >= 0:
                matches.append(i)
    return matches               


def factorial(digit):                   # FACTORIAL
    x = digit
    for i in range(1, x):
            x *= i
    return x

def alphabeth(df, col_name):            #DISPLAY UNIQUE WORDS SORTED BY ALPHABETH IN COLUMNS
    unq_sort = df[col_name].sort_values(ascending=True).unique()
    # сортируем уникальные по жанру

    def alpha(search_list):
        a = []
        for i in search_list:
            if i[0] not in a:
                a.append(i[0])
        return a

    alpha_col = alpha(unq_sort)
    # через рукотворную функцию возвращаем первые буквы списка уникумов

    alpha_col = pd.Series(alpha_col)
    unq_sort = pd.Series(unq_sort)
    # Переводим списки алфавита и уникумов в Series для след. функции
    # (иначе алгоритм не "ест" или выводит белиберду потом разберусь почему так)

    def alpha_table(col, base):    
        frame = {}
        for i in range(len(col)):         
            insight = base[base.str.match(col[i])]
            frame[col[i]] = insight.tolist()
            # data.insert(i, col[i], frame)
        data = pd.DataFrame.from_dict(frame, orient='index')
        data = data.fillna('o').T
        return data
    return alpha_table(alpha_col, unq_sort)
    # через рукотворную функцию возвращаем таблицу жанров
    #               распределённых по первой букве по столбцам.

    
def categorizer(dictionary, x):         # CATEGORISE MEANINGS IN COL OF DF AND WRIGHTS NAMES OF
    key = list(dictionary.keys())       # CATEGORYS IN NEW COL. USE IT WITH `DICT = {MEANING: INT_CRITERIA}`, `APPLY` AND `LABDA`:
                                        # df['NEW_COL'] = df['CATEGORISED_COL'].apply(lambda x: definer(DICT, x))
    if x in range(dictionary.get(key[0]),
                  dictionary.get(key[len(key)-1])):
        
        for i in range(len(key)-1):

            if x in range(dictionary.get(key[i]),
                          dictionary.get(key[i+1])):
                return key[i]
    else: return key[len(key)-1]



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