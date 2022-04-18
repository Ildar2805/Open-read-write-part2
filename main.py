#Задание 3
import glob
glob.glob('./*.txt')
text = {}
for file in glob.glob("*.txt"):
    with open(file, encoding='utf-8') as document:
        text[file] = [len(document.readlines())]
    with open(file, encoding='utf-8') as document:
         text[file].append(document.read())
sorted_tuple = sorted(text.items(), key=lambda x: x[1])
sorted_text = dict(sorted_tuple)
for key, value in sorted_text.items():
    print(value[1])

            