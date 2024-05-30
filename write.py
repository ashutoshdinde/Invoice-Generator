def over_write(List, Dictionary):   # an overwrite function
    L = List    # assign list with variable name 'L'
    d = Dictionary    # assign Dictionary with variable name 'd'
    """
    Update quantity of product after customer purchased some quantity of any product.
    And print remaining stock products.
    """
    for keys in d.keys():
        if keys == "CAPPUCCINO":
            L[0][2] = str(int(L[0][2])-d['CAPPUCCINO'])
        elif keys == "LATTE":
            L[1][2] = str(int(L[1][2])-d['LATTE'])
        elif keys == "ESPRESSO":
            L[2][2] = str(int(L[2][2])-d['ESPRESSO'])
        elif keys == "AMERICANO":
            L[3][2] = str(int(L[3][2])-d['AMERICANO'])
        elif keys == "FLATE WHITE":
            L[4][2] = str(int(L[4][2])-d['FLATE WHITE'])
        elif keys == "ICED COFFEE":
            L[5][2] = str(int(L[5][2])-d['ICED COFFEE'])
        elif keys == "COLD BREW":
            L[6][2] = str(int(L[6][2])-d['COLD BREW'])
        elif keys == "TEA":
            L[7][2] = str(int(L[7][2])-d['TEA'])
        elif keys == "WATER":
            L[8][2] = str(int(L[8][2])-d['WATER'])
        else:
            L[9][2] = str(int(L[9][2])-d['GREEN TEA'])
    print("\nRemaining Stock Products:\n",L)
        
    files = open("products.txt", "w")  # opens stock file (products.txt) file in write mode.
    for each in L:
        files.write(str(",".join(each)))
        files.write("\n")         
    files.close()
    return
