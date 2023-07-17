

# 1. Define a function odd_positions(xs:list)->list that returns a list with all elements of xs
# in odd positions.
li = [0, 1, 2, 3, 4, 5, 6]
def odd_positions(xs: list) -> list:
    """
    Returns a list of elements located at odd positions in the provided list 'xs'.

    Args:
        xs: List of elements.

    Returns:
        A list of elements at odd positions.
    """
    list1 = [x for x in xs if xs.index(x) % 2 != 0]
    return list1
# odd_positions(li)


# 2. Define a function even_positions(xs:list)->list that returns a list with all elements of
# xs in even positions.
def even_positions(xs: list) -> list:
    """
    Returns a list of elements located at even positions in the provided list 'xs'.

    Args:
        xs: List of elements.

    Returns:
        A list of elements at even positions.
    """
    list1 = [x for x in xs if xs.index(x) % 2 == 0]
    return list1
# even_positions(li)


# 3. Define a function reverse(xs:list)->list that returns a list with all elements of xs in
# reverse order without using the the built-in function reversed or method list.reverse.
def reverse(xs: list) -> list:
    """
    Returns a list containing all elements from 'xs', but in the reversed order.

    Args:
        xs: List of elements.

    Returns:
        A list of elements in the reverse order.
    """
    return xs[::-1]
# print(reverse(li))


# 4. Define a function runs(pattern:list,length:int)->list that returns a list of the given
# length filled with runs of elements of xs. For instance, runs([0, 1, 2], 0) returns [] and
# runs([0, 1, 2], 4) returns [0, 1, 2, 0].
def runs(pattern: list, length: int) -> list:
    """
    Returns a list of the specified 'length', filled with the elements from 'pattern'.

    Args:
        pattern: List of elements.
        length: The length of the desired list.

    Returns:
        A list filled with runs of elements of 'pattern'.
    """
    if len(pattern) == length:
        return pattern
    elif len(pattern) == 0:
        return []
    elif len(pattern) > length:
        return pattern[0:length]
    elif len(pattern) < length:
        li = length - len(pattern)
        list1 = pattern + pattern[0:li]
        return list1
# runs(li, 2)


# 5. Define a function doubles(xs:List[float])->List[float] that returns a list with all
# elements of xs multiplied by 2.
def doubles(xs: list) -> list:
    """
    Returns a list where each element is twice the corresponding element in the provided list 'xs'.

    Args:
        xs: List of numbers.

    Returns:
        A list where each element is twice of the corresponding element in 'xs'.
    """
    list2 = [x*2 for x in xs]
    return list2
# doubles(li)


# 6. Define a function squares(xs:List[float])->List[float] that returns a list with all
# elements of xs raised to the power of 2.
def squares(xs: list) -> list:
    """
    Returns a list where each element is the square of the corresponding element in the provided list 'xs'.

    Args:
        xs: List of numbers.

    Returns:
        A list where each element is the square of the corresponding element in 'xs'.
    """

    list2 = [x ** 2 for x in xs]
    return list2


# 7. Define a function smaller_than_filter(xs:List[int],cutoff:int)->List[int] that returns
# a list with all elements of xs smaller than the given cut-off value.
def smaller_than_filter(xs: list, cutoff: int) -> list:
    """
    Returns a list containing the elements from 'xs' that are less than the provided 'cutoff' value.

    Args:
        xs: List of numbers.
        cutoff: A cutoff value.

    Returns:
        A list of elements from 'xs' that are less than 'cutoff'.
    """
    list2 = [x for x in xs if x < cutoff]
    return list2
# smaller_than_filter(li, 3)


# 9. Define a function remove_all(xs:List[int],v:int)->List[int] that returns a list with
# all elements of xs that are not equal v without using list.remove or del.
def remove_all(xs: list, v: int) -> list:
    """
    Returns a list containing all elements from 'xs' that are not equal to 'v'.

    Args:
        xs: List of elements.
        v: A value to remove from the list.

    Returns:
        A list of elements from 'xs' that are not equal to 'v'.
    """
    list2 = [x for x in xs if x != v]
    return list2
# remove_all(li, 2)

# 10. Define a function count(xs:List[int],v:int)->int that returns the number of elements
# of xs equal to v without using list.count or list.index.
def count(xs, v):
    """
    Returns the count of how many times 'v' appears in 'xs'.

    Args:
        xs: List of elements.
        v: A value to count.

    Returns:
        The count of 'v' in 'xs'.
    """
    list2 = [x for x in xs if x == v]
    return print(len(list2))
# count(li, 2)

li = [0,1,2,3,4,5,6]
bi = [2,3,4,5,6]

# 11. Define a function count_any(xs:List[int],vs:List[int])->int that returns the number
# of elements of xs that are equal to any element of vs without using list.count or list.index.
def count_any(xs, vs):
    """
    Returns the count of how many elements in 'xs' are present in 'vs'.

    Args:
        xs: List of elements.
        vs: List of elements to compare with 'xs'.

    Returns:
        The count of elements in 'xs' that are present in 'vs'.
    """
    list2 = [x for x in xs if x in vs]
    return print(len(list2))
# count_any(li, bi)

# 12. Define a function has_any(xs:List[int],vs:List[int])->bool that checks if xs has at
# least one element equal to any element of vs without using list.count or list.index.
def has_any(xs, vs)-> bool:
    """
    Returns a boolean indicating whether any element of 'vs' is present in 'xs'.

    Args:
        xs: List of elements.
        vs: List of elements to check in 'xs'.

    Returns:
        True if any element of 'vs' is present in 'xs', False otherwise.
    """
    list2 = [x for x in xs if x in vs]
    if len(list2) > 0:
        return True
# has_any(li, bi)

# 13. Define a function has_none(xs:List[int],vs:List[int])->int that checks if xs has no
# element equal to any element of vs without using list.count or list.index.
def has_none(xs, vs):
    """
    Returns a boolean indicating whether none of the elements in 'vs' are present in 'xs'.

    Args:
        xs: List of elements.
        vs: List of elements to check in 'xs'.

    Returns:
        True if none of the elements in 'vs' are present in 'xs', False otherwise.
    """
    list2 = [x for x in xs if x in vs]
    if len(list2) == 0:
        return print("It has none",0)
    else:
        print(len(list2))

# 14. Define a function has_all(xs:List[int],vs:List[int])->int that checks if for every element of vs there is an
# element in xs equal to it without using list.count or list.index.
def has_all(xs, vs):
    """
    Returns a boolean indicating whether all elements of 'vs' are present in 'xs'.

    Args:
        xs: List of elements.
        vs: List of elements to check in 'xs'.

    Returns:
        The number of elements of 'vs' which are present in 'xs'.
    """
    list2 = [x for x in vs if x in xs]
    if len(list2) == len(vs):
        return print("All", len(list2))
    else:
        print(len(list2))
# has_all(li, bi)

# 15. Define a function unique_filter(xs:List[int])->List[int] that returns a list with all
# elements of xs that are unique in xs, i.e., those elements that are not equal to any other element
# of xs without using list.count or list.index.


li = [0,1,2,3,3,4,4,5,5]


def unique_filter(xs:list):
    """
    Returns a list of elements from 'xs' that appear only once in 'xs'.

    Args:
        xs: List of elements.

    Returns:
        A list of elements from 'xs' that are unique.
    """
    list1 = []
    for i in range(len(xs)):
        inde = i
        val = xs[inde]
        xs.pop(inde)
        if val in xs:
            pass
        else:
            list1.append(val)
        xs.insert(inde, val)
    return list1
# print(unique_filter(li))


# 16. Define a function repeated_filter(xs:List[int])->List[int] that returns a list with all
# elements of xs that are not unique in xs, i.e., those elements that are equal to some other
# element of xs without using list.count or list.index.
def repeated_filter(xs):
    """
    Returns a list of elements from 'xs' that are not unique in 'xs'.

    Args:
        xs: List of integers.

    Returns:
        A list of elements from 'xs' that are not unique.
    """
    list1 = []
    for i in range(len(xs)):
        inde = i
        val = xs[inde]
        xs.pop(inde)
        if val in xs:
            list1.append(val)
        else:
            pass
        xs.insert(inde, val)
    return list1


def repeated_filter(xs):
    """
       Returns a list of elements from 'xs' that are not unique in 'xs'.

       Args:
           xs: List of integers.

       Returns:
           A list of elements from 'xs' that are not unique.
       """
    list1 = []
    list2 = [x for x in xs if (list1.append(x) or x in list1[:-1])]
    return list2


# 17. Define a function replace(xs:List[int],a:int,b:int)->List[int] that returns a new
# list with the elements of xs except for those equal to a which are replaced with b.
def replace(xs:list,a:int,b:int):
    """
    Returns a new list with the elements of 'xs' except for those equal to 'a' which are replaced with 'b'.

    Args:
        xs: List of integers.
        a: The integer to be replaced.
        b: The integer to replace 'a'.

    Returns:
        A list where all occurrences of 'a' in 'xs' are replaced with 'b'.
    """
    list2 = [b if x == a else x for x in xs]
    print(list2)
# replace(li, 3, 0)

#18. Define a function lowpass(xs:List[float],cutoff:float)->List[float] that returns a
#list with all elements of xs replacing those larger than the cutoff value with it.
def lowpass(xs, cutoff):
    """
    Returns a list with all elements of 'xs', replacing those larger than the 'cutoff' value with it.

    Args:
        xs: List of floats.
        cutoff: The cutoff float value.

    Returns:
        A list where elements larger than 'cutoff' are replaced with 'cutoff'.
    """
    list2 = [cutoff if x > cutoff else x for x in xs]
    print(list2)

# 19. Define a function odd_in_odd(xs:List[int])->List[int] that returns a list with all odd
# elements that occur in odd positions in xs.
li = [0,1,2,3,3,4,4,5,5]
def odd_in_odd(xs):
    """
    Returns a list with all odd elements that occur in odd positions in 'xs'.

    Args:
        xs: List of integers.

    Returns:
        A list of odd elements that occur at odd positions in 'xs'.
    """
    list2 = [xs[x] for x in range(1, len(xs), 2) if xs[x] % 2 != 0]
    return list2
# odd_in_odd(li)


# 20. Define a recursive function sequence(n:int)->List[int] that returns a list containing a
# sequence of consecutive integers from 0 to n (included) without using range.
def sequence(n:int):
    """
    Returns a list containing a sequence of consecutive integers from 0 to 'n' (inclusive).

    Args:
        n: The last number in the sequence.

    Returns:
        A list of consecutive integers from 0 to 'n'.
    """
    list1 = []
    value = 0
    def add(value):
        list1.append(value)
        if len(list1) < (n+1):
            value += 1
            add(value)
        else:
            return print(list1)
    add(0)
# sequence(3)

# 21. Define a recursive function anti_sequence(n:int)->List[int] that returns a list containing a decreasing sequence
# of consecutive integers from n to 0 (included) without using range or list.reverse.
def anti_sequence(n:int):
    """
    Returns a list containing a decreasing sequence of consecutive integers from 'n' to 0 (inclusive).

    Args:
        n: The start of the sequence.

    Returns:
        A list of consecutive integers from 'n' to 0 in decreasing order.
    """
    list1 = []
    value = n
    def add(value):
        list1.append(value)
        if len(list1) < (n+1):
            value -= 1
            add(value)
        else:
            return print(list1)
    add(value)
# anti_sequence(3)

# 22. Define a recursive function int_range(start:int,stop:int)->List[int] that returns a list containing a sequence of
# consecutive integers from start (inclusive) to stop (inclusive) without using range.
def int_range(start, stop):
    """
    Returns a list containing a sequence of consecutive integers from 'start' (inclusive) to 'stop' (inclusive).

    Args:
        start: The start of the sequence.
        stop: The end of the sequence.

    Returns:
        A list of consecutive integers from 'start' to 'stop'.
    """
    list1 = []
    value = start
    dif = stop - start+1
    def add(value):
        list1.append(value)
        if len(list1) < dif:
            value += 1
            add(value)
        else:
            return print(list1)
    add(value)
# int_range(3, 7)

# 23. Define a recursive function int_range(start:int,stop:int,step:int=1)->List[int] that returns a list containing a
# sequence of integers from start (inclusive) to stop (inclusive) by step without using range.
def int_range(start:int,stop:int,step:int=1):
    """
    Returns a list containing a sequence of integers from 'start' (inclusive) to 'stop' (inclusive) with a step of 'step'.

    Args:
        start: The start of the sequence.
        stop: The end of the sequence.
        step: The step size.

    Returns:
        A list of integers from 'start' to 'stop' with a step of 'step'.
    """
    list1 = []
    value = start
    step = step
    dif = stop - start + 1
    def add(value):
        list1.append(value)
        if len(list1) < (dif/step):
            value += step
            add(value)
        else:
            return print(list1)
    add(value)
# int_range(2, 9, 2)

# 24. Define a recursive function squares_sequence(n:int)->List[int] that returns a list of numbers from 0 to n
# (included) squared.
def squares_sequence(n:int)->list:
    """
    Returns a list of numbers from 0 to 'n' (inclusive) squared.

    Args:
        n: The last number in the sequence.

    Returns:
        A list of squares of numbers from 0 to 'n'.
    """
    list1 = []

    def add(value):
        list1.append(value ** 2)
        if value < n:
            add(value + 1)

    add(0)
    return list1
# squares_sequence(4)

# 26. Define a recursive function factorials_sequence(n:int)->List[int] that returns a list
# of the factorial of the numbers from 0 to n included. (Hint: you can avoid computing each
# factorial from scratch by reusing information in the list you are building.)
def factorials_sequence(n:int):
    """
    Returns a list of the factorial of the numbers from 0 to 'n' included.

    Args:
        n: The last number in the sequence.

    Returns:
        A list of factorials of numbers from 0 to 'n'.
    """
    result = [1]
    def add(value):
        if value <= n:
            result.append(result[-1] * value)
            add(value + 1)
    add(1)
    return result
# factorials_sequence(4)

