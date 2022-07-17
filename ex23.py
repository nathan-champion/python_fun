from sys import argv
import sys
script, input_encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()
    if  line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)   
    print(raw_bytes, "<====>", cooked_string)



def write_file(language_file, encoding, errors, outfile):
    line = language_file.readline()
    if line:
        write_line(line, encoding, errors, outfile)
        return write_file(language_file, encoding, errors, outfile)

def write_line(line, encoding, errors, outfile):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    outfile.write(raw_bytes)



def rev_main(bytes_file, encoding, errors):
    line = bytes_file.readline()
    if line:
        rev_print_line(line, encoding, errors)
        #return rev_main(bytes_file, encoding, errors)

def rev_print_line(line, encoding, errors):
    next_byte_lang = line.strip()
    next_byte_lang = next_byte_lang.decode(encoding)
    print(next_byte_lang)


#REVERSING
languages = open("lang_bytes_utf-8.txt", encoding=input_encoding)
rev_main(languages, input_encoding, error)


#MAKING THE BYTES FILE
#languages = open("languages.txt", encoding=input_encoding)
#outfile = open(f"lang_bytes_{input_encoding}.bytes", mode='wb')
#write_file(languages, input_encoding, error, outfile)
#outfile.close()






#ORIGINAL CODE
#main(languages, input_encoding, error)

