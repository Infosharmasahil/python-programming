import json

#person = {'name': 'Alice', 'job': 'Engineer', 'city': 'Toronto'}

#print(type(person))

#properly formatted json
#keys and all strings enclosed in double quotations
#enclosed with curly braces, square brackets can be used

with open('cohort_4.json', 'r') as cohort_file:
    cohort = json.load(cohort_file) #converts json file to python dictionary/list

print(type(cohort))
print(json.dumps(cohort, indent=2))
#print(cohort)