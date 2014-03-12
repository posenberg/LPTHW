from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

#we could do these two on one line too, how?
#in_file = open(from_file)
#indata = in_file.read()

indata = open(from_file).read()

print "This file is %d bytes long" % len(indata)

#we import exists function returns Boolean True or False if the file exists or not
print "Does the output file really exist? %r" % exists(to_file)
print "Ready hit return to continue, CTRL-C to abort."

raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
#in_file.close()
# ^ dont need to close in_file since it's not required to open