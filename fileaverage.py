def fileaverage():
    fname = input("File name: ")
    fname += ".txt"
    with open(fname, "r+") as f:
        lines = f.readlines()
        lines = [int(l) for l in lines]
    average = round((sum(lines) / len(lines)))
    print(average)