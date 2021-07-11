import random

def Quicksort (Sequence):
    #Lists  to append to
    SmallerThanPivot = []
    LargerThanPivot = []
    EqualToPivot = []
    
    if len(Sequence) <= 1: #End case for recursion, no more values to sort
        return(Sequence) #Ends recursion
    else:
        pivot = Sequence.pop(random.randint(0,len(Sequence)-1)) #Selects pivot randomly and removes it from the list (Would be better to use median of three)

        for i in Sequence: 
            
            if i > pivot: #Uses if statements to seperate smaller than pivot/equal to pivot and larger than pivot into list
                LargerThanPivot.append(i)
            
            elif i < pivot:
                SmallerThanPivot.append(i)
            
            elif i == pivot:
                EqualToPivot.append(i)
        
        return (Quicksort(SmallerThanPivot) + [pivot] + EqualToPivot + Quicksort(LargerThanPivot)) #Uses recursion to do quicksort on the seperated lists

def BubbleSort(Sequence):
    Loop = True  # Enables the while loop to start, if in another langauge a do while loop would be used
    
    while Loop:
        Change = False  # Makes sure each loop through the list has a different NumberOfChanges counter
        for i in range(1,len(Sequence)):
            
            if Sequence[i] < Sequence[i-1]:  # Compares the index to the index before (this is why the for loop starts at 1)
                Sequence[i], Sequence[i - 1] = Sequence[i - 1], Sequence[i]  # This swaps the values around
                Change = True # Makes sure end condition does not trigger
            
            elif Change == False and i == (len(Sequence)-1): #End Case for the while loop
                Loop = False
    
    return Sequence

def InsertionSort(Sequence):
    for i in range(1,len(Sequence)): #Starts at 1 so the index can decrease by one without a index out of range error
        for b in range(i,0,-1): #Decreases index by 1 every time it loops, finishing at 1. This makes sure everything before the value of i is checked each time
            if Sequence[b] < Sequence[b - 1]:  # Compares the index to the index before (this is why the for loop starts at 1)
                Sequence[b - 1], Sequence[b] = Sequence[b], Sequence[b - 1 ]  # This swaps the values around
    
    return Sequence 

def RandomSequenceGenerator(NoLoop,MaxRandNumber):
    RandomSequence = []
    
    for i in range(0,NoLoop):
        RandomSequence.append(random.randint(0,MaxRandNumber))
    
    return RandomSequence

Sequence = RandomSequenceGenerator(100,1000)

print("Quick Sort")
print(Quicksort(Sequence))

print("Bubble Sort ")
print(BubbleSort(Sequence))

print("Insertion Sort")
print(InsertionSort(Sequence))