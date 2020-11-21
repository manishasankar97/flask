#Dictionaries are unordered mappings for storing objects. 
#Lists store objects in an ordered sequence, dictionaries use a key-value pairing

salaries = {'john' : 20, 'sally' : 40, 'tommy' : 300}
print(salaries['john'])

salaries["john"] = salaries['john'] + 60
print(salaries['john'])

#list in dictionaries
people = {'john': [1,2,3], 'sally':[40,10,30]}
print(people['sally'][0]) 

#nested dictionaries
people1 = {'john' : {'salary' :10, 'age': 30}}
print('age:',people1["john"]["age"])


d = {'k1' :10, 'k2': 20, 'k3':30}
print(d.keys())
print(d.values())
print(d.items())