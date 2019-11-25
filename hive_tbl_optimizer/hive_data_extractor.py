# python3 /home/cloudera/Desktop/projects/hive_data_extractor.py
import subprocess
import shlex
import re
import os

def get_results(cmd):	
	'''
	Function to run a query and return its results
	'''
	response = subprocess.Popen(['hive', '-e', cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	s_output, s_err = response.communicate()
	s_output = s_output.decode('utf-8')
	s_err = s_err.decode('utf-8')
	status = response.returncode
	#print(status)
	#except:
	if status != 0:
		print("There was an error running the command! Please see details below...")
		print(s_output)	
		print(s_err)
		return None
	else:
		if 'ParseException' in s_output or 'ParseException' in s_err:
			print('A SYNTAX ERROR HAS PROBABLY OCCURRED. PLEASE GO THROUGH THE ERROR MESSAGE IN DETAIL!')		
			print(s_err)
			print(s_output)
			return None
		else:
			print(s_output)
			return s_output

def check_partitions_buckets(db_name, tbl_name):
	'''
	Function to check for names of partitions and buckets in existing tables by applying regex on the result of "describe extended db_name.table_name" command
	'''
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

def get_query_run_history():
	'''
	Function to get run history of all tables and extract the information of the tables of interest
	'''
	log_file_names = os.listdir('/tmp/cloudera/')
	for log in log_file_names:
		cmd = "cat /tmp/cloudera/{l} | grep 'Compiling command'".format(l=log)
		res = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		res_out, res_err = res.communicate()
		print(res_out.decode())


def main():
	first_input = input('Welcome to Hive Tuning Utilities! What do you want to do? \
				\n 1. Enter a Hive command and see it\'s output. \
				\n 2. Check out the partitions/buckets for a particular table. \
				\n 3. See query run history. \
				\n Choose from the options above: ')
	if first_input == '1':
		cmd = input('Enter a valid Hive command: ')
		get_results(cmd)
	elif first_input == '2':
		db_name = input('Enter the name of database which contains the table: ')
		tbl_name = input('Enter the table name whose partition and bucket information you want to see: ')
		check_partitions_buckets(db_name, tbl_name)
	else:
		get_query_run_history()

if __name__ == '__main__':
	main()
		

