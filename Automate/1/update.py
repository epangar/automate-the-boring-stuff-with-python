from subprocess import call
import platform

def run_me(arr):
	if platform.system().startswith('linux'):
		for element in arr:
			parameter = element.split()
			call(parameter) 
#Add Windows methods

instructions = [
  'npm outdated -depth=0 -g',
  "npm update -g"
]

run_me(instructions)