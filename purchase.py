

def purchase(List):
    L = List  # assign list with variable name 'L'.
    a_name = input("Please enter your name: ")
    print("\nHello " + a_name + "! Welcome to our COFFEE SHOP.\nPlease select product as per your choice.")
    q = {}  # assign empty dictionary with variable name 'q'.
    flag = "Y"
    while flag.upper() == "Y":  # check and go if flag is 'Y' or 'y'.
        product = input("\nWhat product do you want to buy? ")
        product_name = product.upper()  # change the string value in the upper case.

        if product_name == L[0][0].upper() \
                or product_name == L[1][0].upper() \
                or product_name == L[2][0].upper() \
                or product_name == L[3][0].upper() \
                or product_name == L[4][0].upper() \
                or product_name == L[5][0].upper() \
                or product_name == L[6][0].upper() \
                or product_name == L[7][0].upper() \
                or product_name == L[8][0].upper() \
                or product_name == L[9][0].upper():  # check the user entered product name with stock of store
            p = True
            while p == True:
                try:
                    p_quantity = int(input("How many " + product + " do you want to buy: "))
                    p = False
                except:  # executes, if customer entered unexpected value.
                    print("\t\tError!!!\nPlease enter integer value!! ")
            if product_name == L[0][0].upper() and p_quantity <= int(L[0][2]):
                q[product_name] = p_quantity
            elif product_name == L[1][0].upper() and p_quantity <= int(L[1][2]):
                q[product_name] = p_quantity
            elif product_name == L[2][0].upper() and p_quantity <= int(L[2][2]):
                q[product_name] = p_quantity
            elif product_name == L[3][0].upper() and p_quantity <= int(L[3][2]):
                q[product_name] = p_quantity
            elif product_name == L[4][0].upper() and p_quantity <= int(L[4][2]):
                q[product_name] = p_quantity
            elif product_name == L[5][0].upper() and p_quantity <= int(L[5][2]):
                q[product_name] = p_quantity
            elif product_name == L[6][0].upper() and p_quantity <= int(L[6][2]):
                q[product_name] = p_quantity
            elif product_name == L[7][0].upper() and p_quantity <= int(L[7][2]):
                q[product_name] = p_quantity
            elif product_name == L[8][0].upper() and p_quantity <= int(L[8][2]):
                q[product_name] = p_quantity
            elif product_name == L[9][0].upper() and p_quantity <= int(L[9][2]):
                q[product_name] = p_quantity
            else:
                print(
                    "\nSorry!! " + a_name + "!, " + product + " is out of stock.\nWe will add stock of " + product + " later. \nLets hope, you will get this product after next shopping.\n")

            flag = (input(a_name + " do you want buy more products?(Y/N)"))
        else:
            print("sorry!! " + product + " is not available in our store.")
            print("\nChoose from following products please!")
            print("--------------------------------------------")
            print("PRODUCT\t\tPRICE\t\tQUANTITY")
            print("--------------------------------------------")
            for i in range(len(L)):
                print(L[i][0], "\t\t", L[i][1], "\t\t",
                      L[i][2])  # print, last updated product name, quantity and price.
            print("--------------------------------------------")

    print("\nYou Choosed Items and it's Quantity respectively:\n", q, "\n")
    
    f_amount = 0  # final amount
    for keys in q.keys():
        if keys == L[0][0].upper():  # executes this operation if product is 
            p_price = int(L[0][1])
            p_num = int(q[keys])
            p_amount = (p_price * p_num)
            f_amount += (p_price * p_num)
            print("\nTotal cost for COFFEE: ", p_amount)
        elif keys == L[1][0].upper():  # executes this operation if product is  entered by customer.
            l_price = int(L[1][1])
            l_num = int(q[keys])
            l_amount = (l_price * l_num)
            f_amount += (l_price * l_num)
            print("Total cost for TEA: ", l_amount)
        elif keys == L[2][0].upper():  # executes this operation if product is  entered by customer.
            c_price = int(L[2][1])
            c_num = int(q[keys])
            c_amount = (c_price * c_num)
            f_amount += (c_price * c_num)
            print("Total cost for ESPRESSO: ", c_amount)
        elif keys == L[3][0].upper():  # executes this operation if product is entered by customer.
            t_price = int(L[3][1])
            t_num = int(q[keys])
            t_amount = (t_price * t_num)
            f_amount += (t_price * t_num)
            print("Total cost for AMERICANO: ", t_amount)
        elif keys == L[4][0].upper():  # executes this operation if product is entered by customer.
            z_price = int(L[4][1])
            z_num = int(q[keys])
            z_amount = (z_price * z_num)
            f_amount += (z_price * z_num)
            print("Total cost for FLATE WHITE: ", z_amount)
        elif keys == L[5][0].upper():  # executes this operation if product is  entered by customer.
            m_price = int(L[5][1])
            m_num = int(q[keys])
            m_amount = (m_price * m_num)
            f_amount += (m_price * m_num)
            print("Total cost for ICED COFFEE: ", m_amount)
        elif keys == L[6][0].upper():  # executes this operation if product is  entered by customer.
            n_price = int(L[6][1])
            n_num = int(q[keys])
            n_amount = (n_price * n_num)
            f_amount += (n_price * n_num)
            print("Total cost for COLD BREW: ", n_amount)
        elif keys == L[7][0].upper():  # executes this operation if product is  entered by customer.
            s_price = int(L[7][1])
            s_num = int(q[keys])
            s_amount = (s_price * s_num)
            f_amount += (s_price * s_num)
            print("Total cost for TEA: ", s_amount)
        elif keys == L[8][0].upper():# executes this operation if product is  entered by customer.
            e_price = int(L[8][1])
            e_num = int(q[keys])
            e_amount = (e_price * e_num)
            f_amount += (e_price * e_num)
            print("Total cost for WATER: ", e_amount)
        elif keys == L[9][0].upper():# executes this operation if product is  entered by customer.
            g_price = int(L[9][1])
            g_num = int(q[keys])
            g_amount = (g_price * g_num)
            f_amount += (g_price * g_num)
            print("Total cost for GREEN TEA: ", g_amount)
    
    print("\nYour discountable total amount is: ", f_amount)


    '''
        In the following operation:
        1) write a each unique involve name which includes current date and time with customer name as well.
        2) write a purchase product name and details in file (invoice).
        3) write a discounted amount and final payable amount in file (invoice).
    '''

    import datetime  # import system date and time for create a unique invoive name.
    dt = str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().month) + "-" + str(
        datetime.datetime.now().day) + "-" + str(datetime.datetime.now().hour) + "-" + str(
        datetime.datetime.now().minute) + "-" + str(datetime.datetime.now().second)
    invoice = str(dt)  # unique invoice
    t = str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().month) + "-" + str(
        datetime.datetime.now().day)  # date
    d = str(t)  # date
    u = str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute) + ":" + str(
        datetime.datetime.now().second)  # time
    e = str(u)  # time

    file = open(invoice + " (" + a_name + ").txt", "w")  # generate a unique invoive name and open it in write mode.
    file.write("=============================================================")
    file.write("\nCOFFEE STORE\t\t\t\tINVOICE")
    file.write("\n\nInvoice: " + invoice + "\t\tDate: " + d + "\n\t\t\t\t\tTime: " + e + "")
    file.write("\nName of Customer: " + str(a_name) + "")
    file.write("\n=============================================================")
    file.write("\nPARTICULAR\tQUANTITY\tUNIT PRICE\tTOTAL")
    file.write("\n-------------------------------------------------------------")

    for keys in q.keys():  # In this loop, write in a file only those product which is purchase by user.
        if keys == "CAPPUCCINO":
            file.write(
                str("\n" + str(keys) + " \t\t " + str(q['CAPPUCCINO']) + " \t\t " + str(L[0][1]) + " \t\t " + str(p_amount)))
        elif keys == "LATTE":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['LATTE']) + " \t\t " + str(L[1][1]) + " \t\t " + str(l_amount)))
        elif keys == "ESPRESSO":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['ESPRESSO']) + " \t\t " + str(L[2][1]) + " \t\t " + str(c_amount)))
        elif keys == "AMERICANO":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['AMERICANO']) + " \t\t " + str(L[3][1]) + " \t\t " + str(t_amount)))
        elif keys == "FLATE WHITE":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['FLATE WHITE']) + " \t\t " + str(L[4][1]) + " \t\t " + str(z_amount)))
        elif keys == "ICED COFFEE":
            file.write(
                str("\n" + str(keys) + " \t\t " + str(q['ICED COFFEE']) + " \t\t " + str(L[5][1]) + " \t\t " + str(m_amount)))
        elif keys == "COLD BREW":
            file.write(
                str("\n" + str(keys) + " \t\t " + str(q['COLD BREW']) + " \t\t " + str(L[6][1]) + " \t\t " + str(n_amount)))
        elif keys == "TEA":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['TEA']) + " \t\t " + str(L[7][1]) + " \t\t " + str(s_amount)))
        elif keys == "WATER":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['WATER']) + " \t\t " + str(L[8][1]) + " \t\t " + str(e_amount)))       
        elif keys == "GREEN TEA":
            file.write(
                str("\n" + str(keys) + " \t\t " + str(q['GREEN TEA']) + " \t\t " + str(L[9][1]) + " \t\t " + str(g_amount)))

    file.write("\n-------------------------------------------------------------")
    file.write("\n\t\t\t Your payable amount is: " + str(f_amount))
    file.write("\n-------------------------------------------------------------")
    file.write("\n\n\tThank You " + a_name + " for your shopping.\n\t\tSee you again!")
    file.write("\n=============================================================")
    file.close()
    return q
