#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(1): assuming n is an integer, this snippet will only run twice.  

At n = 2, 0 < 6, a = 0 + 4
         4 < 6, a = 4 + 4
         8 !< 6

At n = 5000, 0 < 15000, a = 0 + 10000
             10000 < 15000, a = 10000 + 10000
             20000 !< 15000

Running only twice, the run time is constant.

b) O(n^2): for this snippet, we have nested loops.  As n increases, the range for the first loop increases and so does the incrimentation of j.


c) O(n): in this recursive function, the number of recursive calls will be equal to the number of bunnies passed to the function.  The number of recursive calls is directly proportional to the number of bunnies, making the runtime linear.

## Exercise II

Solution 1 - Fewest Broken Eggs:
Drop an egg from every floor starting with the first floor counting up.  Stop when the first egg breaks assuming all floors above will also result in a broken egg
Runtime: O(n)
Broken Eggs: 1

Solution 2 - Fewest Drops:
Drop an egg from the middle floor of the building.  If it breaks, eliminate floors above this floor from your "search".  Drop an egg from the middle of your remaining range.  If it DOESN'T break, eliminate the floors below from your range and drop again from the middle of your remaining range.  Continue this process until only one value remains.  This is your lowest safe value.
Runtime: O(log n)
Broken Eggs: Variable, but likely more than 1
