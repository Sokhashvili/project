import json
import threading

def parse_and_print_json(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
        print(f"Contents of {file_name}:")
        print(json.dumps(data, indent=4))
        print()


json_files = ['file1.json', 'file2.json', 'file3.json']


threads = []
for file_name in json_files:
    thread = threading.Thread(target=parse_and_print_json, args=(file_name,))
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()