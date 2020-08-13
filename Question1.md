This function could be made more clear with better variable names and making the code more pythonic. 
The 'r' variable is acting as a stack data structure and should be labeled as such so its intentions are clear. 
There wouldn't be a need to loop through the string to create this stack since in python you can use the syntax:
```
    stack = s[::-1]
```
for loops are best described by using enumerate over range when possible. 

There isn't a need to create a variable to hold a boolean value if it's only purpose is to be returned. You can just return the boolean data type. The final function would like: 

```
def is_palindrome(s):
stack = s[::-1]

for idx, ele in enumerate(s):
    if s[idx] != stack[idx]:
        return False
    return True
```


You could have a more condensed version with: 

```
def is_palindrome(s):
    return s == s[::-1]
```

Where here there are no variables to hold the any state. This function is much cleaner

Another option with O(n) runtime would be:

```
def is_palindrome(s):
    start = 0
    end = len(s) - 1

    while end > start:
        if s[start] != s[end]:
            return False
        else:
            end -= 1
            start += 1
    return True
```
In this scenario you create 2 pointer variables starting from either side of the string, whenever there isn't a match the function exits. 

