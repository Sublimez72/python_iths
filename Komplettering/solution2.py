import csv


path = "Komplettering/puzzle-file-2.csv"


def main():
    csv_file = open(path, newline="")
    reader = csv.reader(csv_file, delimiter=",")
    checksum = 0
    for row in reader:
        row = list(map(int, row))
        row.sort()
        checksum += row[-1] - row[0]
    csv_file.close()
    print(checksum)


if __name__ == "__main__":
    main()
