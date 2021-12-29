import re


file_path = 'MOCK_DATA.txt'
result_file_path = 'results.txt'

file_reader = open(file_path, mode='r', encoding='Latin-1')
final_results = open(result_file_path, mode='w', encoding='Latin-1')

class_text = file_reader.read()

searcher = r'@\S+\w+.[a-z]+'
results_all = re.findall(searcher, class_text)

for item in results_all:
    print(item)
    final_results.write(item +'\n')
print(f'Total: {str(len(results_all))}')


file_path = 'MOCK_DATA.txt'
result_file_name = 'results_name.txt'

file_reader = open(file_path, mode='r', encoding='Latin-1')
final_results = open(result_file_name, mode='w', encoding='Latin-1')

class_text = file_reader.read()

searcher = r'[A-Z]+[a-z]+\s'
results_all = re.findall(searcher, class_text)

for item in results_all:
    print(item)
    final_results.write(item +'\n')
print(f'Total: {str(len(results_all))}')


file_path = 'MOCK_DATA.txt'
result_file_file = 'results_file.txt'

file_reader = open(file_path, mode='r', encoding='Latin-1')
final_results = open(result_file_file, mode='w', encoding='Latin-1')

class_text = file_reader.read()

searcher = r'[A-Z]+[a-z]+[.][a-z]+'
results_all = re.findall(searcher, class_text)

for item in results_all:
    print(item)
    final_results.write(item + '\n')
print(f'Total: {str(len(results_all))}')


file_path = 'MOCK_DATA.txt'
result_file_color = 'results_color.txt'

file_reader = open(file_path, mode='r', encoding='Latin-1')
final_results = open(result_file_color, mode='w', encoding='Latin-1')

class_text = file_reader.read()

searcher = r'#\S+\w+.'
results_all = re.findall(searcher, class_text)

for item in results_all:
    print(item)
    final_results.write(item + '\n')
print(f'Total: {str(len(results_all))}')