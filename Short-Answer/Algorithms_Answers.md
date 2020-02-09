#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) => Testing was completed within the Algorithm_Question.md document. For every n increase, the loop increase one more time. 

b) O(n log n) => The for loop is O(n). The while loop is kind of interesting because at first sight it seems it grows proporcional as n grows making it an O
(n) complexity but it is not. I tested this script with several n values and it kinds of grow at the same rate except on some values. "sum" is not really important but j grows j * 2 on each while loop 

c) This one is O(n). There is a constant of 2 that we can eliminate but the algorithm calculation grows proporcional as the input grows 

## Exercise II

Ok, well I will use binary search to devide f floors and ask if below that floor the egg breaks, if it doesn't then I will use the upper half of the half and ask again until I get a positive response. The complexity of binary search is O(log n) 


