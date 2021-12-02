def get_pins(observed):
    pinTable = []
    for i in observed:
        if i == 0: pinTable.append([0,8])
        if i == 1: pinTable.append([1,2,4])
        if i == 2: pinTable.append([1,2,3,5])
        if i == 3: pinTable.append([2,3,6])
        if i == 4: pinTable.append([1,4,5,7])
        if i == 5: pinTable.append([2,4,5,6,8])
        if i == 6: pinTable.append([3,5,6,9])
        if i == 7: pinTable.append([4,7,8])
        if i == 8: pinTable.append([0,5,7,8,9])
        if i == 9: pinTable.append([6,8,9])
    
    possiblePins = []
    if len(pinTable) == 0:
        return possiblePins
    
    for i in pinTable[0]:
        if len(pinTable) == 1:
            possiblePins.append(i)
        else:
            for k in pinTable[1]:
                if len(pinTable) == 2:
                    possiblePins.append("".join([str(i), str(k)]))
                else:
                    for l in pinTable[2]:
                        if len(pinTable) == 3:
                            possiblePins.append("".join([str(i), str(k), str(l)]))
                        else:
                            for z in pinTable[3]:
                                if len(pinTable) == 4:
                                    possiblePins.append("".join([str(i), str(k), str(l), str(z)]))
                                else:
                                    for q in pinTable[4]:
                                        if len(pinTable) == 5:
                                            possiblePins.append("".join([str(i), str(k), str(l), str(z), str(q)]))
                                        else:
                                            for w in pinTable[5]:
                                                if len(pinTable) == 6:
                                                    possiblePins.append("".join([str(i), str(k), str(l), str(z), str(q), str(w)]))
                                                else:
                                                    for e in pinTable[6]:
                                                        if len(pinTable) == 7:
                                                            possiblePins.append("".join([str(i), str(k), str(l), str(z), str(q), str(w), str(e)]))
                                                        else:
                                                            for r in pinTable[7]:
                                                                if len(pinTable) == 8:
                                                                    possiblePins.append("".join([str(i), str(k), str(l), str(z), str(q), str(w), str(e), str(r)]))
                                                                
    return possiblePins

print(get_pins('11'))