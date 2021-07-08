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

def RandomSequenceGenerator(NoLoop,MaxRandNumber):
    RandomSequence = []
    
    for i in range(0,NoLoop):
        RandomSequence.append(random.randint(0,MaxRandNumber))
    
    return RandomSequence
