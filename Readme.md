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
The script expects each log entry to be in the format `key=value` or `key="value"`. Please be aware of the following constraints regarding the log file format:
- **Double Quotes (")**: If a value contains double quotes, they should be escaped. Unescaped double quotes might be interpreted as the end of a value.
- **Commas (,)**: Since commas are used as field separators in CSV files, any commas within a value should be enclosed in double quotes to ensure correct parsing.
- **Equals Sign (=)**: The equals sign is used to separate keys from values. If a key or value contains an equals sign, the script might incorrectly parse the entry.

## Error Handling
The script includes basic error handling for file not found and I/O errors.
