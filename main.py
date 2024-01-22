import os

file_path = os.path.expanduser("/Users/ashwini/PycharmProjects/read_txt/test.txt")
output_file_path = os.path.expanduser("/Users/ashwini/PycharmProjects/read_txt/test2.txt")

try:
    with open(file_path, 'r') as dhamo:
        with open(output_file_path, 'w') as output_file:
            for line in dhamo:
                output_file.write(line)

except FileNotFoundError:
    print(f"AshwiniError: File '{file_path}' not found.")
except Exception as e:
    print(f"superexception: {e}")
