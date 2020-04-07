#!/usr/bin/env python3
def find_item(list, item):
    #Returns True if the item is in the list, False if not.
    if len(list) == 0:
        return False

    #Is the item in the center of the list?
    middle = len(list)//2
    lists = list.sort()
    if lists[middle] == item:
        return True
     
    #Is the item in the first half of the list? 
    if item < lists[middle]:
        #Call the function with the first half of the list
        return find_item(lists[:middle], item)
    else:
        #Call the function with the second half of the list
        return find_item(lists[middle+1:], item)

    return False

#Do not edit below this line - This code helps check your work!
list_of_names = ["Parker", "Drew", "Cameron", "Logan", "Alex", "Chris", "Terry", "Jamie", "Jordan", "Taylor"]

print(find_item(list_of_names, "Alex")) # True
print(find_item(list_of_names, "Andrew")) # False
print(find_item(list_of_names, "Drew")) # True
print(find_item(list_of_names, "Jared")) # False