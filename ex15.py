from sys import argv
#script and filenames are argument variables. script refers to the python files and filename variable refers to the text file we will use
script, filename = argv
#the variable text uses the open() command to return the file object which are the texts within the document
#open function is built in module
text = open(filename)
#print output uses the formatter %r for the raw data.
#print uses text variable and uses .read() method/function to read the parameter "filename"
print "Here's our file: %r:" % filename
print text.read()
text = text.close()
#Takes input from the use about what's the file name and assigns it to file_again variable

#NOTE:When you’re done with a file, call f.close() to close it and free up any system resources taken up by the open file.

#if you omit these codes below, you just have the text printed once.
print "Type the filename again:"
file_again = raw_input("> ")
#Takes variable assigned from user and uses the function open() with file_again as the argument
txt_again = open(file_again)
#prints all the texts txt_again variable, but needs to be included with the .read() method 
print txt_again.read()
txt_again = txt_again.close()

# "Ex 15 -Reading Files"
