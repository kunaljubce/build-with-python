import subprocess
import shlex
import re

def get_results(cmd):
	#cmd = 'show create table movies.genre;'	
	try:
		response = subprocess.Popen(['hive', '-e', cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		s_output, s_err = response.communicate()
		s_output = s_output.decode('utf-8')
		s_err = s_err.decode('utf-8')
	except:
		print("There was an error running the command! Please see details below...")
		print(s_output)	
		print(s_err)
		return None
	else:
		if 'ParseException' in s_output or 'ParseException' in s_err:
			print('A SYNTAX ERROR HAS PROBABLY OCCURRED. PLEASE GO THROUGH THE ERROR MESSAGE IN DETAIL!')		
			print(s_err)
			return None
		else:
			print(s_output)
			return s_output

def check_partitions_buckets(db_name, tbl_name):
	print('Fetching info about partitions and buckets...')
	cmd = 'describe extended {db}.{tbl};'.format(db=db_name, tbl=tbl_name)
	output = get_results(cmd)
	if output is not None:
		pattern = re.compile(r'bucketCols:\[[a-zA-Z0-9_, ]*\]|(partitionKeys:\[[a-zA-Z0-9_, ]*\])')
		match = pattern.finditer(output)
		buckets_and_partitions_list = {}
		for m in match:
			key = m.group(0).split(':')[0]
			buckets_and_partitions_list[key] = m.group(0).split(':')[1]
		print('Names of bucketed columns in the table are: {}'.format(buckets_and_partitions_list['bucketCols']))
		print('Names of partitioned columns in the table are: {}'.format(buckets_and_partitions_list['partitionKeys']))


def main():
	first_input = input('Welcome to Hive Tuning Utilities! What do you want to do? \n 1. Enter a Hive command and see it\'s output. \n 2. Check out the partitions/buckets for a particular table. \n Choose from the options above: ')
	if first_input == '1':
		cmd = input('Enter a valid Hive command: ')
		get_results(cmd)
	else:
		db_name = input('Enter the name of database which contains the table: ')
		tbl_name = input('Enter the table name whose partition and bucket information you want to see: ')
		check_partitions_buckets(db_name, tbl_name)

if __name__ == '__main__':
	main()
		

