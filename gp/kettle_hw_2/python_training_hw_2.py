import csv

#import files
nfl_teams_file = open("nfl_teams.csv", "r")
nfl_teams_csv = list(csv.DictReader(nfl_teams_file))

zipcode_file = open("zipcode_data.csv", "r")
zipcode_csv = list(csv.DictReader(zipcode_file))

target_cities_file = open("target_cities.csv", "r")
target_cities_csv = list(csv.DictReader(target_cities_file))

nfl_potential_teams = []

DIVISION_MAP = ["NFC North", "NFC South", "NFC East", "NFC West", "AFC North", "AFC South", "AFC East", "AFC West"]


#function to perform lookups
def lookup_value(stream, lookup_stream, key, lookup_key, lookup_value):
	stream_output = []
	for row in stream:
		for lookup_row in lookup_stream:
			if(row[key] == lookup_row[lookup_key]):
				row[lookup_value] = lookup_row[lookup_value]
		
		stream_output.append(row)
	
	return stream_output

def filter_stream(stream, column, operator, value, desired_result):
	criteria_true = []
	criteria_false = []

	for row in stream:
		if(row[column] + operator + value):
			criteria_true.append(row)
		else:
			criteria_false.append(row)
	
	if(desired_result == True):
		return criteria_true
	if(desired_result == False):
		return criteria_false


def field_to_int(stream,fieldname):
	stream_output = []
	for row in stream:
		row[fieldname] = int(row[fieldname])
		stream_output.append(row)
	return list(stream_output)


# zipcode_data = convert_to_list(zipcode_csv)

# for row in zipcode_data:
# 	print "zip: " + row

for team in nfl_teams_csv:
	#convert division to text
	division_index = int(team['division']) - 1
	team['division'] = DIVISION_MAP[division_index]

	# if(team['super_bowl_wins'] == 0 and team['team_valuation'] < 2000000000):
	# 	nfl_potential_teams.append(team)
	nfl_potential_teams.append(team)



nfl_potential_teams = field_to_int(nfl_potential_teams,"team_valuation")
nfl_potential_teams = field_to_int(nfl_potential_teams,"super_bowl_wins")

zipcode_data = field_to_int(zipcode_csv, 'avg_per_capita_income')

nfl_potential_teams = lookup_value(nfl_potential_teams,zipcode_data,'zipcode','zipcode','avg_per_capita_income')

# for team in nfl_potential_teams:
# 	if(int(team['avg_per_capita_income']) >= 30000):
# 		nfl_potential_teams.remove(team)


for team in nfl_potential_teams:
	print team



