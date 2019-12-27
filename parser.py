import sys
import csv

with open('progressionChart.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    excercises = []
    line_count = 0
    for row in csv_reader:
        filename = 'level_' + str(line_count) + '.md'
        f = open(filename, 'w')
        sys.stdout = f
        if line_count == 0:
            excercises = row
            line_count += 1
        else:
            for i in range(len(excercises)):
                print('* ' + excercises[i] + ": " + row[i])
            line_count += 1
        f.close()

