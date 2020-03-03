#Imports
import configparser
import time

def Configure_From_File(config_file_path):
	# asserting configuration file has the correct extension
	path = config_file_path.split('.')
	assert(path[len(path)-1] == 'ini')

	config = configparser.ConfigParser()
	config.read(config_file_path)
	return config


def End_Test(Bot):
	#Countdown
	input("Press [ENTER] to end session.")
	time.sleep(.5)
	Bot.Driver.quit()
	time.sleep(.5)
	print("\nSession ended.")
	quit()
