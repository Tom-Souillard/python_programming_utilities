import os
import argparse


def preview_rename(directory, old_pattern, new_pattern):
    """Preview the file renaming operation.

    Parameters:
        directory (str): The directory containing the files to rename.
        old_pattern (str): The old naming pattern.
        new_pattern (str): The new naming pattern.
    """
    for filename in os.listdir(directory):
        if old_pattern in filename:
            new_filename = filename.replace(old_pattern, new_pattern)
            print(f'{filename} -> {new_filename}')


def apply_rename(directory, old_pattern, new_pattern):
    """Apply the file renaming operation.

    Parameters:
        directory (str): The directory containing the files to rename.
        old_pattern (str): The old naming pattern.
        new_pattern (str): The new naming pattern.
    """
    for filename in os.listdir(directory):
        if old_pattern in filename:
            new_filename = filename.replace(old_pattern, new_pattern)
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Batch file renamer')
    parser.add_argument('-d', '--directory', required=True, help='Directory containing the files to rename')
    parser.add_argument('-o', '--old-pattern', required=True, help='Old naming pattern')
    parser.add_argument('-n', '--new-pattern', required=True, help='New naming pattern')
    parser.add_argument('-p', '--preview', action='store_true', help='Preview changes without applying them')

    args = parser.parse_args()

    if args.preview:
        preview_rename(args.directory, args.old_pattern, args.new_pattern)
    else:
        apply_rename(args.directory, args.old_pattern, args.new_pattern)