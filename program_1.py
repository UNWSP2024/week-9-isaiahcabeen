def count_file_lines():
    try:
        with open('names.txt', 'r') as file:
            lines = file.readlines()
            lines = [line.strip() for line in lines if line.strip()]
            print(f'Total number of names in the file: {len(lines)}')
    except FileNotFoundError:
        print('Error: The file "names.txt" was not found.')
    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == '__main__':
    count_file_lines()
