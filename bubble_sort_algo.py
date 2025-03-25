#Bubble sort algo pg 52 Data Sructures and Algos

def bubble_sort(list):
    unsorted_untill_index = len(list) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in  range(unsorted_untill_index):
            if list[i] > list[i + 1]:
                sorted = False
        unsorted_untill_index -= 1
    return list

print(bubble_sort([65, 45, 5, 35, 25, 15, 10, 55]))