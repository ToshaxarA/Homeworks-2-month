i=0; j=0
spisok = []
list1=[]
import random
while i<5001:
    spisok.append(i)
    i+=1
while j<100:
    list1.append(random.randint(1,100))
    j+=1

def binary_search(element:int, spisok:list) ->int:
    n = 5000
    result_ok = False
    first = 0
    last = n-1
    while True:
        if element not in spisok:
                    print("Элемент не найден =(")
                    break
        while result_ok == False:
            if first<last:
                middle = round((first+last)/2)
                # print(first)
                # print(middle)
                # print(last)
                # print(" ")
                
                if element == middle:
                    first = middle
                    last = first
                    result_ok = True
                    position = middle
                if element == last:
                    result_ok = True
                    position = last
                if element == first:
                    result_ok = True
                    position = first
                if element>middle:
                    first = middle+1
                elif element<middle:
                    last = middle-1
                                                      
        if result_ok == True:
            print(f"Элемент найден!, это {position}")
            break
        else:
            print("Элемент не найден =(")
            break
        
binary_search(40000,spisok)

def buble_sort(not_sorted_list:list) ->list:
    a=not_sorted_list
    print(f"Список до сортировки: \n {not_sorted_list}")
    print(" ")
    for i in range(len(a)-1):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    print(f"Список после сортировки 'пузырьком': \n {a}")
buble_sort(list1)