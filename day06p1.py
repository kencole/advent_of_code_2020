def read_input(filename):
    with open(filename) as file:
        content = file.readlines()
    content = [line.rstrip() for line in content]
    return content

filename = 'day06p1.txt'

lines = read_input(filename)


surveys = [[]]
for line in lines:
    tokens = line.split()
    if len(tokens) > 0:
        surveys[-1].extend(tokens)
    else:
        surveys.append([])

        
surveys = [''.join(survey) for survey in surveys]
surveys = [list(survey) for survey in surveys]
surveys = [set(survey) for survey in surveys]
survey_counts = [len(survey) for survey in surveys]
print(sum(survey_counts))
