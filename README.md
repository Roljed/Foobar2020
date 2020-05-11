# Foobar2020
Google Challenges 

## Challenge 1
Decipher string, where each character of lowercase [a...z] are replaced with their counterparts:

    a --> z
    b --> y
    c --> x
 other characters remain the same.
 
 ## Challenge 2
 ### Sub-Challenge 1
 Given a list of elevator versions represented as strings, write a function solution(l) that returns the same list sorted in ascending order by major, minor, and revision number so that you can identify the current elevator version. The versions in list l will always contain major numbers, but minor and revision numbers are optional. If the version contains a revision number, then it will also have a minor number.
 For example, given the list l as ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"], the function solution(l) would return the list ["1.0", "1.0.2", "1.0.12", "1.1.2", "1.3.3"]. If two or more versions are equivalent but one version contains more numbers than the others, then these versions must be sorted ascending based on how many numbers they have, e.g ["1", "1.0", "1.0.0"].
 
 #### Example
    Input:  ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
    Output: 0.1,1.1.1,1.2,1.2.1,1.11,2,2.0,2.0.0
 
 ### Sub-Challenge 2
 You have L, a list containing some digits (0 to 9). Write a function solution(L) which finds the largest number that can be made from some or all of these digits and is divisible by 3. If it is not possible to make such a number, return 0 as the solution. L will contain anywhere from 1 to 9 digits.  The same digit may appear multiple times in the list, but each element in the list may only be used once.

#### Example
    Input:  [3, 1, 4, 1]
    Output: 4311
