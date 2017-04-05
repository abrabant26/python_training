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


def write_dict_to_csv(filepath, data, fields=None):
	if not fields:
			fields = data[0].keys()
	with open(filepath, 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=fields)
		writer.writeheader()
		writer.writerows(data)


def get_low_value_teams(teams):
	low_value_teams = []
	for team in teams:
		if int(team.get('super_bowl_wins')) == 0 and int(team.get('team_valuation')) < 2000000000 \
		and int(team.get('avg_per_capita_income')) < 30000:
			low_value_teams.append(team)
	return low_value_teams


def per_capita_income_by_zipcode():
	fp = 'zipcode_data.csv'
	data = read_csv(fp)
	per_capita_lookup = {row['zipcode']: row['avg_per_capita_income'] for row in data}
	return per_capita_lookup


def merge_teams_and_cities(low_value_teams, cities):
	merged = []
	for team in low_value_teams:
		merged.append({'team_name': team['team_name'], 'target_city': '', 'avg_per_capita_income': team['avg_per_capita_income']})
	for city in cities:
		merged.append({'team_name': '', 'target_city': city['target_city'], 'avg_per_capita_income': city['avg_per_capita_income']})
	return merged


def main():
	nfl_teams = read_csv('nfl_teams.csv')
	per_capita_data = per_capita_income_by_zipcode()
	for team in nfl_teams:
		team['division'] = DIVISION_LOOKUP[int(team['division'])]
		team['avg_per_capita_income'] = per_capita_data[team['zipcode']]
	low_value_teams = get_low_value_teams(nfl_teams)
	
	cities = read_csv('target_cities.csv')
	cities_and_teams = merge_teams_and_cities(low_value_teams, cities)
	sorted_cities_and_teams = sorted(cities_and_teams, key=lambda k: k['avg_per_capita_income'])
	write_dict_to_csv('low_value_teams_and_some_cities.csv', sorted_cities_and_teams)


if __name__ == "__main__":
	main()