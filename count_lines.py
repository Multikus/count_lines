import os


def count_lines(filename):
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith('#'):
                count += 1
    return count


def count_lines_in_directory(directory):
    total_count = 0
    for root, dirs, files in os.walk(directory):
        # Исключаем папку "enviroments"
        if 'environments' in dirs:
            dirs.remove('environments')
        for file in files:
            if file.endswith('.py'):
                filename = os.path.join(root, file)
                count = count_lines(filename)
                total_count += count
    return total_count


if __name__ == '__main__':
    current_directory = os.getcwd()
    total_lines = count_lines_in_directory(current_directory)
    print(f'Total lines: {total_lines}')
