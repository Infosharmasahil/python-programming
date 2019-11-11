destinations = ['Cozumel', 'Cancun', 'Montego Bay', 'Bora Bora', 'Maui', 'Phuket',
'Mykonos', 'Palawan', 'Vieques', 'Negril']

countries = ['Mexico', 'Mexico', 'Jamaica', 'Tahita', 'USA', 'Thaialnd', 'Greece', 'Philippines', 'Puerto Rica', 'Jamaica']

for idx in range(len(destinations)):
    destinations[idx] += ' - ' + countries[idx]  

print(destinations)