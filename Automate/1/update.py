from subprocess import call

def run_me(arr):
	for element in arr:
		parameter = element.split()
		call(parameter) 

instructions = [
  'npm outdated -depth=0 -g',
  "npm update -g"
]

run_me(instructions)