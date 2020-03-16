import random as rd

def create_tab(size,start,stop):
    tab=[]
    for i in range(int(size)):
        nb=rd.randint(start,stop)
        tab.append(nb)
    return tab

def insert_sort(tab):
    for i in range(1,len(tab)):
        nb = tab[i]
        j = i - 1
        while j >= 0 and tab[j] > nb:
            tab[j+1] = tab[j]
            j = j - 1
        tab[j+1] = nb
    return tab