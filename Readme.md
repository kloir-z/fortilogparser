# Format Forti Log to CSV

## Description
This script parses a specified log file and converts it into a CSV file. It dynamically generates the CSV column headers based on the keys present in the log file.

## Requirements
- Python 3
- No external libraries required

## Usage
Run the script with the path to the log file as an argument: 
```
python main.py path/to/logfile
```

## Output
The script generates a CSV file in the same directory as the log file with the same base name.

## Log File Format Constraints
The script processes log entries in the format `key=value` or `key="value"`. However, it is essential to note the following limitations regarding characters in keys and values:
- **Keys and Values**: Both keys and values should not contain spaces or special characters like commas (`,`), double quotes (`"`), or equals signs (`=`). These characters may cause incorrect parsing or formatting issues in the CSV output.
- **Double Quotes (") in Values**: Values containing double quotes should avoid as they might be misinterpreted.
- **Commas (,) in Values**: Given that commas are used as separators in CSV files, values containing commas can disrupt the formatting. Therefore, it's recommended to avoid using commas within values.

Ensure that your log files adhere to these constraints for accurate parsing and CSV conversion.

## Error Handling
The script includes basic error handling for file not found and I/O errors.
