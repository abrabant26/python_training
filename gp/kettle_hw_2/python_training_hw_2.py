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


'''Function takes input stream, lookup stream, key, lookup key, and lookup value
Adds matching lookup value to rows where keys matching
Returns: stream with lookup values appended'''
def lookup_value(stream, lookup_stream, key, lookup_key, lookup_value):
	stream_output = []
	for row in stream:
		for lookup_row in lookup_stream:
			if(row[key] == lookup_row[lookup_key]):
				row[lookup_value] = lookup_row[lookup_value]
		
		stream_output.append(row)
	
	return stream_output


'''Function takes an input stream, single or array of columns, operator as a string,
single or array of values, and a desired result (bool)
Returns: new stream that matches filter and desired_result'''
def filter_stream(stream, column, operator, value, desired_result):
	criteria_true = []
	criteria_false = []

	for row in stream:
		if operator == "=":
			if(row[column] == value):
				criteria_true.append(row)
			else:
				criteria_false.append(row)
		if operator == "<":
			if(row[column] < value):
				criteria_true.append(row)
			else:
				criteria_false.append(row)
		if operator == "= and <":
			if (row[column[0]] == value[0] and row[column[1]] < value[1]):
				criteria_true.append(row)
			else:
				criteria_false.append(row)
	
	if(desired_result == True):
		return criteria_true
	if(desired_result == False):
		return criteria_false


'''Function takes a stream and fieldname as input
Converts specified field to an int
Returns: modified stream'''
def field_to_int(stream,fieldname):
	stream_output = []
	for row in stream:
		row[fieldname] = int(row[fieldname])
		stream_output.append(row)
	return list(stream_output)


'''Input: Array of streams
Returns: stream where each row has all keys, null for no values'''
def stream_schema_merge(streams):
	keys = []
	full_stream = []
	output_stream = []

	for stream in streams:
		keys = keys + list(stream[0].keys())
		full_stream = full_stream + stream

	for row in full_stream:
		new_row = dict.fromkeys(keys)
		new_row.update(row)
		output_stream.append(new_row)

	return output_stream


'''Input: data stream, row to sort on'''
'''Returns: stream sorted on specified row'''
def rows_merge_sort(stream, sort_column):
	stream_copy = stream
	sort_split(stream, stream_copy, 0, len(stream), sort_column)

def sort_split(stream, stream_copy, ibegin, iend, sort_column):
	imiddle = int((iend + ibegin) / 2)


	if iend - ibegin <= 1:
		# print stream_copy[ibegin:iend]
		# print "------------"
		return None

	sort_split(stream, stream_copy, ibegin, imiddle, sort_column)
	sort_split(stream, stream_copy, imiddle, iend, sort_column)

	sort_merge(stream, stream_copy, ibegin, imiddle, iend, sort_column)

def sort_merge(stream, stream_copy, ibegin, imiddle, iend, sort_column):

	i = ibegin
	j = imiddle
	while(i < iend):
		print stream[i][sort_column]
		print stream[j][sort_column]

	if (i < imiddle and (j <= iend or ))

		i += 1

#Map division code to text
for team in nfl_teams_csv:
	division_index = int(team['division']) - 1
	team['division'] = DIVISION_MAP[division_index]
	nfl_potential_teams.append(team)


nfl_potential_teams = field_to_int(nfl_potential_teams, "team_valuation") #convert 'team_valuation' to int
nfl_potential_teams = field_to_int(nfl_potential_teams, "super_bowl_wins") #convert 'super_bowl_wins' to int
zipcode_data = field_to_int(zipcode_csv, 'avg_per_capita_income') #convert 'avg_per_capita_income' to int

#filter out high-value teams
nfl_potential_teams = filter_stream(nfl_potential_teams, ['super_bowl_wins', 'team_valuation'], '= and <', [0, 2000000000], True)

#lookup zipcode data
nfl_potential_teams = lookup_value(nfl_potential_teams,zipcode_data,'zipcode','zipcode','avg_per_capita_income')

#filter out high-income cities
nfl_potential_teams = filter_stream(nfl_potential_teams, 'avg_per_capita_income', '<', 30000, True)

#merge teams and cities
merged_data = stream_schema_merge([nfl_potential_teams, target_cities_csv])

rows_merge_sort(merged_data, 'avg_per_capita_income')

# for row in merged_data:
# 	print row




