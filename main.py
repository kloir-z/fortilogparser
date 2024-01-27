import argparse
import csv
import re
from collections import defaultdict
import os

def parse_log(log_file_path):
    # Check if the log file exists
    if not os.path.exists(log_file_path):
        raise FileNotFoundError(f"Log file not found: {log_file_path}")

    base, ext = os.path.splitext(log_file_path)
    csv_file_path = base + '.csv' if ext != '.csv' else base + '_converted.csv'  # Avoid duplicate .csv extension

    column_order = {}  # Dictionary to maintain the order of appearance of each key
    log_entries = []
    pattern = re.compile(r'(\S+)=("[^"]+"|\S+)')

    try:
        with open(log_file_path, 'r') as log_file:
            for line_num, line in enumerate(log_file, start=1):
                log_entries.append(line)
                for key, _ in pattern.findall(line):
                    if key not in column_order:
                        column_order[key] = line_num

        ordered_columns = sorted(column_order, key=lambda k: column_order[k])

        with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=ordered_columns)
            writer.writeheader()

            for line in log_entries:
                row_data = defaultdict(str)
                for key, value in pattern.findall(line):
                    row_data[key] = value.strip('"')
                writer.writerow(row_data)

        print(f'CSV file created: {csv_file_path}')
    except IOError as e:
        print(f"An error occurred while processing the file: {e}")

def main():
    parser = argparse.ArgumentParser(description='Parse log file into CSV format.')
    parser.add_argument('log_file', help='Path to the log file to be parsed.')
    args = parser.parse_args()

    try:
        parse_log(args.log_file)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
