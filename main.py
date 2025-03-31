import os
import sys
import time
import traceback

def get_args():
	args = input("Enter a problem number: ")
	if args.lower() in ["quit", "exit", "qqq"]:
		raise KeyboardInterrupt()
	args = args.split(" ")
	files = sorted(f for f in os.listdir(".") if f.endswith(".py"))
	matched = False
	if args[0] == "":
		# get most recently changed file
		args[0] = sorted(files, key=lambda f: os.path.getmtime(f), reverse=True)[0]
		matched = True
	else:
		# get first file that matches prefix
		args[0] = args[0].zfill(3)
		for file in files:
			if file.startswith(args[0]):
				args[0] = file
				matched = True
				break
	if not matched:
		args[0] = None
	return args

def run(args):
	file = args[0]
	if file is None:
		print("File not found.")
		return True
	args = " ".join(args[1:])
	print()
	print(time.strftime("%I:%M:%S %p"))
	print(file)
	print("-" * len(file))
	print(flush=True)
	start = time.monotonic()
	try:
		success = False
		success = os.system(f"python {file} {args}") == 0
	except KeyboardInterrupt:
		pass
	stop = time.monotonic()
	elapsed = time.strftime("%H:%M:%S", time.gmtime(stop - start))
	print()
	print("-" * len(file))
	print(f"Completion time: {elapsed}")
	print()
	return success

def main():
	while True:
		args = get_args()
		while not run(args):
			if input("Retry? [Y/n]").lower() == "n":
				break

if __name__ == "__main__":
	try:
		try:
			script_path = __file__
		except NameError:
			script_path = sys.argv[0]
		os.chdir(os.path.join(os.path.dirname(script_path), "solutions"))
		main()
	except KeyboardInterrupt:
		print("Cancelled by user.")
	except:
		traceback.print_exc()
	finally:
		print()
		print("Press ENTER to exit.", end="")
		input()
