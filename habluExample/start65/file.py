readFile = open("text.text", "r")  # kono ekta file read korar jonno ei method use kora hoy
print(readFile.read())


# create file
wr = open("python.html", "w")  # kono file create korte hole ei method use korbo. seta j kono file hote pare...
wr.write("<p>Here is file creating function in Python</p>\n")

# create file
wr = open("python.html", "a")  # kono file create korte hole ei method use korbo. seta j kono file hote pare...
wr.write("<p>Here is file creating function 2</p>\n")
wr.write("<p>Here is file creating function 2</p>\n")
wr.write("<p>Here is file creating function 2</p>\n")