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

## Log File Format and Limitations
The script expects each log entry to be in the format `key=value` or `key="value"`. However, the current implementation does not support escape sequences within the log file. Therefore, please be aware of the following limitations:
- **Double Quotes (")**: The script does not support escaped double quotes within values. Values should not contain unescaped double quotes as they may lead to parsing errors.
- **Commas (,)**: If a value contains commas, it should be enclosed in double quotes. However, the script does not support commas within values that are not enclosed in double quotes.
- **Equals Sign (=)**: The script uses the equals sign to separate keys from values. Keys or values containing equals signs may be incorrectly parsed.

Users should ensure that their log files conform to these format requirements for proper parsing and conversion into CSV format.

## Error Handling
The script includes basic error handling for file not found and I/O errors.
