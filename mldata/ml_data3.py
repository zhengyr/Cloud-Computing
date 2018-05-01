import csv
from random import *
with open('ccMlData.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for k in range(100):
        libId = randint(0, 1)
        if(libId==1):
            if(random()<0.9):
                filewriter.writerow(["YES", 1])
            else:
                filewriter.writerow(["NO", 0])

        else:
            if(random()<0.9):
                filewriter.writerow(["NO", 0])
            else:
                filewriter.writerow(["NO", 1])