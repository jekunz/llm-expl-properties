import json, random

file = "/Users/kunje68/Downloads/alpaca_gpt4_data.json"

with open(file, 'r') as handle:
    parsed = json.load(handle)
random.seed(42)
random.shuffle(parsed)

include = []

for line in parsed:
    print('')
    print(parsed.index(line))
    print('Instruction: ', line['instruction'])
    print('Input: ', line['input'])

    if input() == 'y':
        include.append(line)

    if len(include) == 200:
        break

with open("/Users/kunje68/Downloads/expl_out.json", "w") as outfile:
    json.dump(include, outfile)