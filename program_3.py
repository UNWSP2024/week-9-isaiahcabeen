def sum_numbers_from_file():
    try:
        with open('numbers.txt', 'r') as file:
            total = 0
            for line in file:
                try:
                    total += int(line.strip())
                except ValueError:
                    print(f"Skipping invalid value: {line.strip()}")
            print(f"Total sum of numbers: {total}")

    except IOError:
        print("An error occurred while trying to read the file.")
