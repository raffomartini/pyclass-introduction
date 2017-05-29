import json
import urllib

with open('notes/show_int_brief.json') as f:
	raw_data = json.load(f)

if __name__ == '__main__':
	pass
	records = raw_data['ins_api']['outputs']['output']['body']['TABLE_interface'][
		'ROW_interface']
	record = records[0]

	# to encode things as an URL
	print urllib.urlencode(record)
	# to do that manually
	print '&'.join('{}={}'.format(k, v) for k, v in record.items())
