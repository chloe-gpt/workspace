def divide_str():
    string = input("Enter string. > ")
    divisor = int(input("Enter a divisor. > "))
    l = []
    piece_length, leftovers = divmod(len(string), divisor)
    print("Piece Length:", piece_length, "|", "Leftovers:", leftovers)
    for i in range(divisor):
        start = ((i) * piece_length)
        end = ((i+1) * piece_length)
        l.append(string[start:end])
    if leftovers == 1:
        l.append(string[-1])
    elif leftovers > 1:
        l.append(string[(-1 * leftovers):-1])
        l[-1] = l[-1] + string[-1]
    print(l)