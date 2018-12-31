import glob
import csv
import os


# Open result file
interesting_files = glob.glob("*/*.csv")
interesting_files = sorted( interesting_files, key = lambda file: os.path.getctime(file))
with open('output.csv','w') as fout:
    h = True
    for filename in interesting_files: 
        print('Processing %s\n' % filename)
        # Open and process file
        with open(filename,'r') as fin:
            if h:
                h = False
            else:
                try:
                    next(fin)
                except:
                    pass
            for line in fin:
                if line != '\n':
                    fout.write(line)
