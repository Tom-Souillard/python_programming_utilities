# Log Parser

import re
import json
from collections import Counter


def parse_log(file_path, pattern):
    """Parse a log file and extract information based on a regular expression pattern.

    Parameters:
        file_path (str): The path to the log file.
        pattern (str): The regular expression pattern to match.

    Returns:
        list: A list of dictionaries containing the parsed log data.
    """
    parsed_data = []
    with open(file_path, 'r') as f:
        for line in f:
            match = re.search(pattern, line)
            if match:
                parsed_data.append(match.groupdict())
    return parsed_data


def generate_statistics(parsed_data, key):
    """Generate statistics based on the parsed log data.

    Parameters:
        parsed_data (list): The parsed log data.
        key (str): The key to use for generating statistics.

    Returns:
        dict: A dictionary containing the statistics.
    """
    counter = Counter(item[key] for item in parsed_data)
    return counter


if __name__ == '__main__':
    # Define the log file path and the regular expression pattern
    log_file_path = 'example.log'
    log_pattern = r'(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(?P<date>.*?)\] "(?P<request>.*?)"'

    # Parse the log file
    parsed_data = parse_log(log_file_path, log_pattern)

    # Generate statistics
    ip_statistics = generate_statistics(parsed_data, 'ip')

    # Output the statistics
    print('IP Address Statistics:')
    print(json.dumps(ip_statistics, indent=4))