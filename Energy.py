gpekpe = input("Press [1] for G.P.E, Press [2] for K.P.E.: ")
if gpekpe == "1":
    m = input("Enter mass: ")
    while m == "":
        m = input("Enter mass: ")
    w = input("Enter weight: ")
    while w == "":
        w = input("Enter weight: ")
    g = input("Enter gravity: ")
    while g == "":
        g = input("Enter gravity: ")
    gpe = float(m)*float(w)*float(g)
    print("G.P.E. = " + str(gpe) + " jules")
if gpekpe == "2":
    m = input("Enter mass: ")
    while m == "":
        m = input("Enter mass: ")
    v = input("Enter velocity: ")
    while v == "":
        v = input("Enter velocity: ")
    kpe = 0.5*float(m)*(float(v)**2)
    print("K.P.E. = " + str(kpe) + " grams")

#I am done. -Tanish