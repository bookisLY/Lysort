********************************************************************************************************
There have Six sorts functions to sort list , and provide a func to make a random list or iterable object

you can use like these way:
*********************************************************************************************************
#make a range(0,10000) 30000 random data and return a list
list = Rand_Iter(0, 100000, 30000).get_list()  

#sort_way:

bubble_sort(list)
 
selection_sort(list)
 
insert_sort(list)
 
Sort.merge_sort(list)

quick_sort(0, len(list)-1, list)

heap_sort(list, len(list)-1)

#input a iterable and return a list 
Rand_Iter().get_list(iterable)   

#input a iterable and return a list 
Rand_Iter().get_tupe(list)  #return a tuple 

#return a interable container
Rand_Iter(start,stop,num).get_iter()

Have a good day , enjoy it!
