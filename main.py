import io
import sys
from obfuscator.pattern_matcher import pattern_matcher
from utils.utils import *
from decompiler.decompiler import *
from utils.contract import *

def main():
    
	if len(sys.argv) < 2:
		print("Usage: %s <filename>" % sys.argv[0])
		return

	#read file
	filename = sys.argv[1]
	file_content = read_file(filename)


	#bytecode string to bytecode list
	bytecode = text_to_bytecode_list(file_content)

	#isolate creation and runtime bytecode
	creation_bytecode, runtime_bytecode = isolate_creation_runtime_bytecode(bytecode)

	print("Creation bytecode: %s" % "".join(creation_bytecode))
	print("Runtime bytecode: %s" % "".join(runtime_bytecode))
	#bytecode list to opcode list
	opcode_list =  bytecode_to_opcode(runtime_bytecode)
	
	print("Successfully decompiled %s" % filename)

	#create Contract object
	contract = Contract(runtime_bytecode,creation_bytecode, opcode_list)
	print(contract)

	#find opcode pattern
	pattern_matcher(contract)

	#adjust JUMP instr to new bytecode
	print(contract)
if __name__ == "__main__":
	main()