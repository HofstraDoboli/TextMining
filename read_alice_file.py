def read_line_by_line():
    # read the alice file line by line
    f = open('alice.txt', 'r')
    for line in f:      ## iterates over the lines of the file
        print(line, end = '')    ## trailing , so print does not add an end-of-line char
                   ## since 'line' already includes the end-of line.
    f.close()

# or read all lines
def read_all_lines():
    f = open('alice.txt', 'r')
    all_lines = ' '.join(f.readlines())  # joins the lines together
    print(all_lines)
    f.close()