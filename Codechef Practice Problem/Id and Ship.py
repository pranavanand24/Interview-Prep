for _ in range(int(input())):
    ID  = input()
    if ID == "B" or ID == "b":
        print("BattleShip")
    elif ID == "C" or ID == "c":
        print("Cruiser")
    elif ID == "D" or ID == "d":
        print("Destroyer")
    elif ID == "F" or ID == "f":
        print("Frigate")