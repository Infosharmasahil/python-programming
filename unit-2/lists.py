'''
cohort_4 = ['Daniela', 'Kayle', 'Emma', 'Julien', 'Chizea', 'Sahil', 'Shilaj', 'Lizhi', 'Christina', 'Allaina'] 

print(len(cohort_4))

#access items in list using position (index)

print(cohort_4[0]) #prints first item in list



#add items to the list, use append 

#print(type(cohort_4))


cohort_4.append('Romeo')


cohort_4.remove('Julien') 
print(cohort_4)

cohort_4.remove('Julien') 

'''
values = [2.3, 45, 11, -5, 3.5, 7.9, 11.7, 40, 85.6, 77.1]

float_list =  []

for n in values:
    if type(n) is float:
        float_list.append(n)

print(float_list)




