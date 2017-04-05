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


def field_to_int(stream,fieldname):
	stream_output = []
	for row in stream:
		row[fieldname] = int(row[fieldname])
		stream_output.append(row)
	return stream_output

def value_mapper(stream,map):
	

for team in nfl_teams_csv:
	#convert division to text
	division_index = int(team['division']) - 1
	team['division'] = DIVISION_MAP[division_index]

	#convert team valuation to number
	team['team_valuation'] = int(team['team_valuation'])

	#convert sb wins to number
	team['super_bowl_wins'] = int(team['super_bowl_wins'])

	if(team['super_bowl_wins'] == 0 and team['team_valuation'] < 2000000000):
		nfl_potential_teams.append(team)

nfl_potential_teams = lookup_value(nfl_potential_teams,zipcode_csv,'zipcode','zipcode','avg_per_capita_income')


for team in nfl_potential_teams:
	if(int(team['avg_per_capita_income']) >= 30000):
		nfl_potential_teams.remove(team)


for team in nfl_potential_teams:
	print team



