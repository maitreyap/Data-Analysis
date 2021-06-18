#Script to Calculate Time Difference between two sample points
#Takes a input csv file calculates the time difference and outputs data to a csv file

#Usage - run on commandline - python timediff.py inputfilename outputfilename test

import argparse
import csv
import datetime
from pytz import timezone
import pytz

def ImportCsvData(inputcsvfilename, outputcsvfile):
    time = []
    entry_id = []
    temperature = []
    humidity = []
    SoilMoisture = []
    timediff = []

    with open(inputcsvfilename, 'r') as csvfile:
        csv_read = csv.reader(csvfile)
        next(csv_read)
        for line in csv_read:
            time.append(line[0])
            entry_id.append(line[1])
            temperature.append(line[2])
            humidity.append(line[3])
            SoilMoisture.append(line[4])

    with open(outputcsvfile, 'w') as newcsvfile:
        csv_write = csv.writer(newcsvfile)

        csv_write.writerow(['Time', 'Time Diff', 'Entry ID', 'Temperature', 'Humidity', 'SoilMoisture'])
        for x in range(1, time.__len__()):
            date_object_curr = datetime.datetime.strptime(time[x-1], '%Y-%m-%d %H:%M:%S %Z')
            date_object_next = datetime.datetime.strptime(time[x], '%Y-%m-%d %H:%M:%S %Z')

            date_object_diff = date_object_next - date_object_curr
            timediff.append(date_object_diff)

            csv_write.writerow([date_object_curr, date_object_diff, entry_id[x-1],
                                temperature[x-1], humidity[x-1], SoilMoisture[x-1]])
            print(time[x])
            #print(date_object_PST_curr)
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