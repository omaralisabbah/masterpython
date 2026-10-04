#------------------------------------------------------
# Sets Methods Part 1
#--------------------
# clear() - Removes all elements from the set.
# discard() - Removes a specified element from the set. If the element is not present, it does nothing.
# remove() - Removes a specified element from the set. If the element is not present, it raises a KeyError.
# pop() - Removes and returns an arbitrary element from the set. Raises KeyError if the set is empty.
# union() - Returns a new set containing all unique elements from both sets.
# add() - Adds a specified element to the set.
# copy() - Returns a shallow copy of the set.
# update() - Updates the set with elements from another set or iterable.
#------------------------------------------------------


# clear() - Removes all elements from the set
setA = {1, 2, 3, 4, 5}
print("Set A before clear():", setA)
setA.clear()
print("Set A after clear():", setA)  # Output: Set A after clear(): set()


print("------------------------------------------------------")


# discard() - Removes a specified element from the set. If the element is not present, it does nothing.
setB = {1, 2, 3, 4, 5}
print("Set B before discard(3):", setB)
setB.discard(3)
print("Set B after discard(3):", setB)  # Output: Set B after discard(3): {1, 2, 4, 5}


print("------------------------------------------------------")


# remove() - Removes a specified element from the set. If the element is not present, it raises a KeyError.
setC = {1, 2, 3, 4, 5}
print("Set C before remove(3):", setC)
setC.remove(3)
print("Set C after remove(3):", setC)  # Output: Set C after remove(3): {1, 2, 4, 5}


print("------------------------------------------------------")


# pop() - Removes and returns an arbitrary element from the set. Raises KeyError if the set is empty.
setD = {1, 2, 3, 4, 5}
print("Set D before pop():", setD)
element = setD.pop()
print("Element removed:", element)
print("Set D after pop():", setD)  # Output: Set D after pop(): {1, 2, 4, 5}


print("------------------------------------------------------")


# union() - Returns a new set containing all unique elements from both sets.
setE = {1, 2, 3} 
setF = {3, 4, 5}
setG = setE.union(setF)
print("Set G (union of E and F):", setG)  # Output: Set G (union of E and F): {1, 2, 3, 4, 5} 
print("Set E | Set F:", setE | setF)  # Output: {1, 2, 3, 4, 5} (using the | operator for union)


print("------------------------------------------------------")


# add() - Adds a specified element to the set. If the element is already present, it does nothing.
setH = {1, 2, 3}
print("Set H before add(4):", setH)
setH.add(4)
print("Set H after add(4):", setH)  # Output: Set H after add(4): {1, 2, 3, 4}
setH.add(2)  # Adding an existing element
print("Set H after add(2):", setH)  # Output: Set H after add(2): {1, 2, 3, 4} (no change)


print("------------------------------------------------------")


# copy() - Returns a shallow copy of the set.
setI = {1, 2, 3}
setJ = setI.copy()
print("Set I:", setI)  # Output: Set I: {1, 2, 3}
print("Set J (copy of I):", setJ)  # Output: Set J (copy of I): {1, 2, 3}


print("------------------------------------------------------")


# update() - Updates the set with elements from another set or iterable.
setK = {1, 2, 3}
setL = {3, 4, 5}
print("Set K before update():", setK)
setK.update(setL)
print("Set K after update():", setK)  # Output: Set K after update(): {1, 2, 3, 4, 5}