file = open("input.txt", "r")
loop = True
out = ""
while loop:
    letter = file.read(1)
    if letter == ":" or letter == "\n" or letter == " ":
        print("Removed '" + letter + "'")
        letter = ""
    elif letter == "!":
        loop = False
        print("Found file end")
    else:
        print("Keeping letter '" + letter + "'")
    out += letter
outfile = open("output.txt", "w")
outfile.write(out)
outfile.close
input("Press enter to exit")
