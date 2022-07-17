import sys
script, from_file, to_file = sys.argv

infile = open(from_file)
outfile = open(to_file, 'w')
outfile.write(infile.read())
infile.close()
outfile.close()