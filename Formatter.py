file = open("input.txt", "r")
loop = True
out = ""
while loop:
    letter = file.read(1)
    if letter == ":":
        letter = ""
        print("Removed ':'")
    elif letter == "!":
        loop = False
        print("Found file end")
    else:
        print("Keeping letter '" + letter + "'")
    out += letter

outfile = open("output.txt", "w")
outfile.write(out)
outfile.close
input("\n\n Press enter to exit")
