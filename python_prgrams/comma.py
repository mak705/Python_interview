with open ("m.txt", "r") as mak:
    output = []
    for col in mak:
        output.append(col.strip())
    print ','.join(output)
