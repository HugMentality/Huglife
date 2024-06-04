import pandas as    pd
import funckie as   fc

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
# pd.set_option('display.width', None)

mus = pd.read_csv('artists.csv')

print(fc.alphabeth(mus, 'genre'))


# USED FUNCTION
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