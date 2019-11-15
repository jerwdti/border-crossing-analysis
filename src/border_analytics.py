__author__ = "Chengtian Deng"

import math
import csv
import argparse


# post condition: filename successfully parsed
def analysis(input_f, output_f):
    # reading the input file
    with open(input_f, "r") as f:
        table = csv.reader(f)
        # skipping the header
        next(table, None)
        # sort tabel by border, date, type
        sorted_tabel = sorted(table, key=lambda x: x[3:5])

        # sum value based on measure(border, date and type)
        temp_tabel_by_measure = []
        for row in sorted_tabel:
            if row[3:6] in temp_tabel_by_measure:
                temp_tabel_by_measure[temp_tabel_by_measure.index(row[3:6]) + 1] \
                    = int(temp_tabel_by_measure[temp_tabel_by_measure.index(row[3:6]) + 1]) + int(row[6])
            else:
                temp_tabel_by_measure.append(row[3:6])
                temp_tabel_by_measure.append(row[6])

        # calculate the average of previous monthly based on border and type
        tabel_by_measure = []
        temp = []
        total = 0
        count = 0
        index = 0
        averages = [0] * len(temp_tabel_by_measure)
        # combining value and the measurement into one list
        for n in range(0, len(temp_tabel_by_measure), 2):
            newItem = temp_tabel_by_measure[n]
            newItem.append(temp_tabel_by_measure[n + 1])
            tabel_by_measure.append(newItem)

        # for each record, increments the counter and total to calculate previous monthly average
        for row in tabel_by_measure:
            if [row[0], row[2]] in temp:
                average = total / count
                # rounding
                if average - math.floor(average) < 0.5:
                    averages[index] = math.floor(total / count)
                else:
                    averages[index] = math.ceil(total / count)
                total = total + int(row[3])
                count = count + 1
            else:
                temp.append([row[0], row[2]])
                total = int(row[3])
                count = 1
            index = index + 1

        # adding the calculated average value into the list
        for n in range(0, len(tabel_by_measure)):
            tabel_by_measure[n].append(averages[n])

        # sort by data, value, type, border
        tabel_by_measure.sort(key=lambda x: (x[1], int(x[3]), x[2], x[0]), reverse=True)

        # outputting the file into the directory
        with open(output_f, "w") as f_out:
            output_file = csv.writer(f_out)
            output_file.writerow(['Border', 'Date', 'Measure', 'Value', 'Average'])

            for row in tabel_by_measure:
                output_file.writerow(row)


def main():
    # parsing arguments into the system using arparser
    parser = argparse.ArgumentParser(description='Border Crossing Statistics directory')
    parser.add_argument("input", help="input csv file directory ", type=str)
    parser.add_argument("output", help="output csv file directory ", type=str)
    args = parser.parse_args()

    analysis(args.input, args.output)


if __name__ == "__main__":
    main()
