from sys import argv

script, input_file = argv
#define your functions below

def print_all(f):
	#.read()  reads the whole file
	print f.read()

''' .seek(...) moves to new file position.
    method takes an  argument offset is a byte count. ie .seek(0)
    or .seek(1) or .seek(2)  
    Optional argument whence defaults to 0 (offset from start of file, 
    offset should be >= 0); other values are 1 (move relative to current 
    position, positive or negative), and 2 (move  relative to end of file, 
    usually negative, although many platforms allow seeking beyond the 
    end of a file).  If the file is opened in text mode, only offsets returned
    by tell() are legal.  Use of other offsets causes undefined behavior.                                                                                                     
	Note that not all file objects are seekable. '''

def rewind(f):
	# seek() at the 0 position means you're at the start of the file
	f.seek(0)
	# works in values of BYTES
	# f.seek(1) would move over to the next position of the line.
	# f.seek(10) moves ten spaces over -- you get the idea

def print_a_line(line_count, f):
	# readline() reads the line line from the file.
	print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now's let's rewind, kind of like a tape.\n"

rewind(current_file) #this just moves the position to the beginning of current file

print "Let's print three lines: "

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

# I added the extra ones below. Each 
current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

