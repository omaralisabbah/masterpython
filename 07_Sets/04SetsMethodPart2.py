#------------------------------------------------------
# Sets Methods Part 2
#--------------------
# difference() - Returns a new set containing elements that are in the first set but not in the second set.
# difference_update() - Removes elements from the first set that are also in the second set.
# symmetric_difference() - Returns a new set containing elements that are in either of the sets but not in both.
# symmetric_difference_update() - Updates the first set with elements that are in either of the sets but not in both.
# intersection() - Returns a new set containing elements that are common to both sets.
# intersection_update() - Updates the first set with elements that are common to both sets.
#------------------------------------------------------


# difference() - Returns a new set containing elements that are in the first set but not in the second set.
setH = {1, 2, 3, 4, 5}
setI = {4, 5, 6, 7, 8}
setJ = setH.difference(setI)  
print("Set J (difference of H and I):", setJ)  # Output: Set J (difference of H and I): {1, 2, 3}
print("Set H - Set I:", setH - setI)  # Output: {1, 2, 3} (using the - operator for difference)


print("------------------------------------------------------")


# difference_update() - Removes elements from the first set that are also in the second set.
setK = {1, 2, 3, 4, 5}
setL = {4, 5, 6, 7, 8}
print("Set K before difference_update(I):", setK)
setK.difference_update(setL)
print("Set K after difference_update(I):", setK)  # Output: Set K after difference_update(I): {1, 2, 3}


print("------------------------------------------------------")


# symmetric_difference() - Returns a new set containing elements that are in either of the sets but not in both.
setM = {1, 2, 3, 4, 5}
setN = {4, 5, 6, 7, 8}
setO = setM.symmetric_difference(setN)
print("Set O (symmetric difference of M and N):", setO)  # Output: Set O (symmetric difference of M and N): {1, 2, 3, 6, 7, 8}
print("Set M ^ Set N:", setM ^ setN)  # Output: {1, 2, 3, 6, 7, 8} (using the ^ operator for symmetric difference)


print("------------------------------------------------------")


# symmetric_difference_update() - Updates the first set with elements that are in either of the sets but not in both.
setP = {1, 2, 3, 4, 5}
setQ = {4, 5, 6, 7, 8}
print("Set P before symmetric_difference_update(Q):", setP)
setP.symmetric_difference_update(setQ)
print("Set P after symmetric_difference_update(Q):", setP)  # Output: Set P after symmetric_difference_update(Q): {1, 2, 3, 6, 7, 8}


print("------------------------------------------------------")


# intersection() - Returns a new set containing elements that are common to both sets.
setR = {1, 2, 3, 4, 5}
setS = {4, 5, 6, 7, 8}
setT = setR.intersection(setS)
print("Set R (intersection of R and S):", setR)  # Output: Set R (intersection of R and S): {4, 5}
print("Set R & Set S:", setR & setS)  # Output: {4, 5} (using the & operator for intersection)


print("------------------------------------------------------")


# intersection_update() - Updates the first set with elements that are common to both sets.
setU = {1, 2, 3, 4, 5}
setV = {4, 5, 6, 7, 8}
print("Set U before intersection_update(V):", setU)
setU.intersection_update(setV)
print("Set U after intersection_update(V):", setU)  # Output: Set U after intersection_update(V): {4, 5}

