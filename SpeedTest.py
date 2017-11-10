import subprocess
import time
from time import gmtime, strftime

# Open a simple text file for writing the result
resultFile = open("speedtest.txt", "a+")

while True:
	# Header text & placeholders for our result
	print ("Starting Test...")
	timeStr = strftime("%Y-%m-%d %H:%M:%S", gmtime())
	downloadSpeed = ""
	uploadSpeed = ""

	# Action the process to test our speed
	# capturing it's output
	result = subprocess.run(['speedtest-cli'], stdout=subprocess.PIPE)

	# Process the output into text & split the text
	# at each new line character
	btext = result.stdout
	text = btext.decode('ascii')
	lines = text.split("\n")

	# For each line, check whether it is upload
	# or download
	for line in lines:
		# For Download, take a split against space
		# and the middle value is the speed
		if line.startswith('Download: '):
			speedParts = line.split(" ")
			if len(speedParts) == 3:
				downloadSpeed = speedParts[1]
		# Likewise for upload, the middle  value is
		# the tested speed
		elif line.startswith('Upload: '):
			speedParts = line.split(" ")
			if len(speedParts) == 3:
				uploadSpeed = speedParts[1]

	# Print our output result as a CSV
	print (timeStr + "," + downloadSpeed + "," + uploadSpeed)

	# Write the result to a file also
	resultFile.write (timeStr + "," + downloadSpeed + "," + uploadSpeed + "\r\n")
	resultFile.flush()

	# Count down until the next test time
	count = 10
	while count > 0:
		# The line is repeated, so we use the end=""
		# and a return carriage to print over and over
		print ("\rTime until next test " + str(count) + " seconds", end="")
		time.sleep(1)
		count = count - 1
	# Print a new line to stop the next text appending
	# on the time count down line
	print()
