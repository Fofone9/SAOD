from simpleInsertionSort import simpleInsertionSort
from InsertionSortIntoLinkedList import InsertionSortIntoLinkedList
from bubbleSort import bubbleSort
from quickSort import quickSort
from digitalSort import digitalSort
from piramidSort import piramidSort
from distributiveCountingSort import distributiveCountingSort
from simpleMergeSort import simpleMergeSort
from simpleMergeSortForList import simpleMergeSortForList


def vivod(name, forwCount, compCount):
    print(name)
    print('количесвто перестановок', str(forwCount))
    print('количесвто сравнений', str(compCount))


test_count = 100

for i in range(5):
    array_size = 2000 + 2000*i
    simpleInsertionSort_forwardingCount = 0
    simpleInsertionSort_comparisonCount = 0


    InsertionSortIntoLinkedList_forwardingCount = 0
    InsertionSortIntoLinkedList_comparisonCount = 0

    bubbleSort_forwardingCount = 0
    bubbleSort_comparisonCount = 0

    quickSort_forwardingCount = 0
    quickSort_comparisonCount = 0

    digitalSort_forwardingCount = 0
    digitalSort_comparisonCount = 0

    piramidSort_forwardingCount = 0
    piramidSort_comparisonCount = 0

    distributiveCountingSort_forwardingCount = 0
    distributiveCountingSort_comparisonCount = 0

    simpleMergeSort_forwardingCount = 0
    simpleMergeSort_comparisonCount = 0

    simpleMergeSortForList_forwardingCount = 0
    simpleMergeSortForList_comparisonCount = 0

    for i in range(test_count):
        simpleInsertionSortObj = simpleInsertionSort(array_size)
        simpleInsertionSortObj.sort()
        simpleInsertionSort_comparisonCount += simpleInsertionSortObj.comparisonCount
        simpleInsertionSort_forwardingCount += simpleInsertionSortObj.forwardingCount

        InsertionSortIntoLinkedListObj = InsertionSortIntoLinkedList(array_size)
        InsertionSortIntoLinkedListObj.sort()
        InsertionSortIntoLinkedList_comparisonCount += InsertionSortIntoLinkedListObj.comparisonCount
        InsertionSortIntoLinkedList_forwardingCount += InsertionSortIntoLinkedListObj.forwardingCount

        bubbleSortObj = bubbleSort(array_size)
        bubbleSortObj.sort()
        bubbleSort_comparisonCount += bubbleSortObj.comparisonCount
        bubbleSort_forwardingCount += bubbleSortObj.forwardingCount

        quickSortObj = quickSort(array_size)
        quickSortObj.sort()
        quickSort_comparisonCount += quickSortObj.comparisonCount
        quickSort_forwardingCount += quickSortObj.forwardingCount

        digitalSortObj = digitalSort(array_size)
        digitalSortObj.sort()
        digitalSort_comparisonCount += digitalSortObj.comparisonCount
        digitalSort_forwardingCount += digitalSortObj.forwardingCount

        piramidSortObj = piramidSort(array_size)
        piramidSortObj.sort()
        piramidSort_comparisonCount += piramidSortObj.comparisonCount
        piramidSort_forwardingCount += piramidSortObj.forwardingCount

        distributiveCountingSortObj = distributiveCountingSort(array_size)
        distributiveCountingSortObj.sort()
        distributiveCountingSort_comparisonCount += distributiveCountingSortObj.comparisonCount
        distributiveCountingSort_forwardingCount += distributiveCountingSortObj.forwardingCount

        simpleMergeSortObj = simpleMergeSort(array_size)
        simpleMergeSortObj.sort()
        simpleMergeSort_comparisonCount += simpleMergeSortObj.comparisonCount
        simpleMergeSort_forwardingCount += simpleMergeSortObj.forwardingCount

        simpleMergeSortForListObj = simpleMergeSortForList(array_size)
        simpleMergeSortForListObj.sort()
        simpleMergeSortForList_comparisonCount += simpleMergeSortForListObj.comparisonCount
        simpleMergeSortForList_forwardingCount += simpleMergeSortForListObj.forwardingCount
    print('Количество элементов', str(array_size))
    vivod('Простая сортировка вставками.', simpleInsertionSort_forwardingCount/100, simpleInsertionSort_comparisonCount/100)
    vivod('Сортировка вставками в связанный список.', InsertionSortIntoLinkedList_forwardingCount/100, InsertionSortIntoLinkedList_comparisonCount/100)
    vivod('Пузырьковая сортировка.', bubbleSort_forwardingCount/100, bubbleSort_comparisonCount/100)
    vivod('Быстрая сортировка.', quickSort_forwardingCount/100, quickSort_comparisonCount/100)
    vivod('Цифровая обменная сортировка.', digitalSort_forwardingCount/100, digitalSort_comparisonCount/100)
    vivod('Пирамидальная сортировка.', piramidSort_forwardingCount/100, piramidSort_comparisonCount/100)
    vivod('Сортировка распределяющим подсчетом.', distributiveCountingSort_forwardingCount/100, distributiveCountingSort_comparisonCount/100)
    vivod('Сортировка простым двухпутевым слиянием.', simpleMergeSort_forwardingCount/100, simpleMergeSort_comparisonCount/100)
    vivod('Сортировка слиянием списков для простого двухпутевого слияния.', simpleMergeSortForList_forwardingCount/100, simpleMergeSortForList_comparisonCount/100)
    print()
