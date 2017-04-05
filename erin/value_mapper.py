import csv

DIVISION_LOOKUP = {1: 'NFC North', 2: 'NFC South', 3: 'NFC East', 4: 'NFC West', 5: 'AFC North', 
				   6: 'AFC South', 7: 'AFC East', 8: 'AFC West'}


def read_csv(filepath):
	data = []
	with open(filepath, 'r') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			data.append(row)
	return data


nfl_teams = read_csv('nfl_teams.csv')
for team in nfl_teams:
	print DIVISION_LOOKUP[int(team.get('division'))]