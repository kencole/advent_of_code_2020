from collections import Counter

def read_input(filename):
    with open(filename) as file:
        content = file.readlines()
    content = [line.rstrip() for line in content]
    return content

filename = 'day06p1.txt'

lines = read_input(filename)


surveys = [[]]
responses = [0]
for line in lines:
    tokens = line.split()
    if len(tokens) > 0:
        surveys[-1].extend(tokens)
        responses[-1] += 1
    else:
        surveys.append([])
        responses.append(0)

        
surveys = [''.join(survey) for survey in surveys]
surveys = [list(survey) for survey in surveys]
survey_counters = [Counter(survey) for survey in surveys]

all_yesses = 0

for yes_counts, response_count in zip(survey_counters, responses):
    for question in yes_counts.keys():
        if yes_counts[question] == response_count:
            all_yesses += 1

print(all_yesses)

