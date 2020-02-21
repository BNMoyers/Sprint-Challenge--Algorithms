#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)
    The time complexity of this problem increases linearly in direct relation to the size of n.


b)O(nlogn)
The complexity of i is O(n), while the complexity of j is O(logn), because j is doubling every iteration (thus halving the time to reach n). Put together, that makes O(nlogn).


c)O(n)
    The complexity of this algorithm also increases linearly, in proportion with 'bunnies'.

## Exercise II


This problem requires a classic 'divide and conquer' strategy. 

The ground floor of the building is our lowest floor. The top floor is our highest floor. We find the difference, and then go to the middlemost floor.

Once on the middle floor, we drop an egg to test whether it breaks. 

Does it break? If so, then this floor becomes our new highest floor.
Does it stay unbroken? If so, this is our new bottom floor.

Now we just repeat the process until we narrow down to a single floor!

The runtime complexity of this algorithm is O(logn), because each iteration divides the remainder in half.