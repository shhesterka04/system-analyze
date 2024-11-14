import csv
import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: python task.py <path_to_csv> <row_number> <column_number>")
        return

    path_to_csv = sys.argv[1]
    row_number = int(sys.argv[2])
    column_number = int(sys.argv[3])

    try:
        with open(path_to_csv, mode='r') as file:
            reader = csv.reader(file)
            rows = list(reader)
            if row_number < 0 or row_number >= len(rows):
                print("Row number out of range")
                return
            if column_number < 0 or column_number >= len(rows[row_number]):
                print("Column number out of range")
                return
            print(rows[row_number][column_number])
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()