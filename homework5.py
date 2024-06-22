str_1="программирование"
str_2='13'
number_int=7
number_float=1.3
boolean1=True
immutable_var=[str_1,str_2,number_int,number_float,boolean1]
print(immutable_var)
#___________________________________________________________________-
number_int=float(number_int) # можно преобразовать целое число в число с плавающей точкой
number_float=int(number_float) # и наоборот
str_2=int(str_2) # можно строку преобразовать в число только если она содержит чис
number_float=str(number_int) # можно число преобразовать в строку
boolean1=(int(boolean1)) # можно логический тип преобразовать в число (1,0 в зависимости от типа
#____________________________________________________________________
immutable_list=['наименование',"единица измерения","количество","себестоимость","наценка","продажа"]
print("Заданный список: ",immutable_list)
immutable_list.append("НДС")
immutable_list.remove("наценка")
print("Измененный список: ",immutable_list)
