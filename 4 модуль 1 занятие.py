#N=4, M=5, ИТОГО: 20 повторений
#Сложность: 0(N*M)
def strcounter(stroka):
    for sym in set(stroka): #4 значения - значит - 4 повторения(итерации)
        counter=0
        for sub_sym in stroka: #5 значений в stroka - 5 повт.
            if sym==sub_sym:
                counter+=1
        print(sym, counter)
#Переделаем в Сложность: O(N)
def strcounter_new(stroka):
    syms_counter={}
    for symb in stroka:
        syms_counter[symb]=syms_counter.get(symb, 0)+1
    print(syms_counter)
stroka='aabbcd'
print(set(stroka))
strcounter(stroka)
strcounter_new(stroka)