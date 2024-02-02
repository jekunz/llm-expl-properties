import json

with open("/Users/kunje68/Downloads/expl_out.json", "r") as handle:
    parsed = json.load(handle)

to_json = []
questions = ['Does the output contain an explanation for the prediction?', 
'Would you give an explanation/justify your reasoning if you were asked this question by a friend?',
'If there is an explanation: Does the explanation refer to commonsense concepts that are taken as given?',
'If there is an explanation: Does the explanation list contributing factors?',
'If there is an explanation: Does the explanation include subjective or biased criteria?',
'If there is an explanation: Does the explanation include illustrative elements (e.g. examples)?',
'If there is an explanation: Is the explanation misleading (e.g. arguing for a label that is wrong)?']

cnt = 0
for line in parsed: 
    for q in questions: 
        line_dup = line.copy()
        s = '*****INSTRUCTION:***** ' + line['instruction'] + '\n' + line['input'] + '\n*****OUTPUT:***** ' + line['output'] + '\n*****QUESTION:***** ' + q
        assert isinstance(s, str)
        line_dup['all_data'] = s
        line_dup['index'] = cnt
        to_json.append(line_dup)
        cnt += 1

#print(to_json)

with open("/Users/kunje68/Downloads/expl_aio2.json", "w") as outfile:
    json.dump(to_json, outfile)