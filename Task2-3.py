
dictionary = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, 
{'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

sort = sorted(dictionary, key=lambda x:x['color'])
print(sort)

