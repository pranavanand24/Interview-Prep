def makeArrayConsecutive2(statues):
    count = 0
    minvalue = min(statues)
    maxvalue = max(statues)
    
    for item in range(minvalue, maxvalue+1):
        if item not in statues:
            count += 1
    return count