states = {
	'Karnataka' : 'KA',
	'Maharastra' : 'MH',
	'West Bengal' : 'WB',
	'Tamil Nadu' : 'TN'
}

cities = {
	'KA' : 'Bangalore',
	'MH' : 'Mumbai',
	'WB' : 'Kolkata',
	'TN' : 'Chennai'
}

print '-' * 10
print "KA state has: ", cities['KA']
print "WB state has: ", cities['WB']

print '-' * 10
print "Maharastra abbreviation is", states['Maharastra']
print "Tamil Nadu abbreviation is", states['Tamil Nadu']

print '-' * 10
print "Karnataka has: ", cities[states['Karnataka']]
print "West Bengal has: ", cities[states['West Bengal']]

print '-' * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)

print '-' * 10
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)

print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])
	
print '-' * 10
state = states.get('Andhra', None)
if not state:
    print "Sorry, no Andhra."
