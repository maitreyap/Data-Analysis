#Script to Calculate Time Difference between two sample points
#Takes a input csv file calculates the time difference and outputs data to a csv file

#Usage - run on commandline - python timediff.py inputfilename outputfilename

import argparse
import csv
import datetime

def ImportCsvData(inputcsvfilename, outputcsvfile):
    time = []
    timediff = []
    with open(inputcsvfilename, 'r') as csvfile:
        csv_read = csv.reader(csvfile)
        next(csv_read)
        for line in csv_read:
            time.append(line[0])
    with open(outputcsvfile, 'w') as newcsvfile:
        csv_write = csv.writer(newcsvfile)

        csv_write.writerow(['Time', 'Time Diff'])
        for x in range(1, time.__len__()):
            date_object_curr = datetime.datetime.strptime(time[x-1], '%Y-%m-%d %H:%M:%S %Z')
            date_object_next = datetime.datetime.strptime(time[x], '%Y-%m-%d %H:%M:%S %Z')
            date_object_diff = date_object_next - date_object_curr
            timediff.append(date_object_diff)
            csv_write.writerow([date_object_curr, date_object_diff])
            print(time[x])
            print(date_object_diff)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("InputFile", help='Name of Input file to process')
    parser.add_argument("OutputFile", help='Name of File to output processed data')
    args = parser.parse_args()
    inputfilename = args.InputFile
    outputfilename = args.OutputFile
    print(args.InputFile)
    print(args.OutputFile)

    ImportCsvData(inputfilename, outputfilename)
    input("press enter to exit")