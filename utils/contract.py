from opcodes.opcode_dict import *
from opcodes.opcode_obj import *
from decompiler.decompiler import *

class Contract:
    def __init__(self, creation_bytecode, runtime_bytecode, opcode_list):
        self.bytecode = runtime_bytecode
        self.opcode = opcode_list
        self.creation_bytecode = creation_bytecode
        #2-tuple of (added_bytes,index)
        self.obfuscation_flags = dict()

    def update_bytecode(self,new_bytecode):
        self.bytecode = new_bytecode
        self.opcode = bytecode_to_opcode(self.bytecode) #update opcode when updating bytecode

    def update_opcode(self, new_opcode_list):
        self.opcode = new_opcode_list
        self.bytecode = opcode_to_bytecode(self.opcode) #update bytecode when updating opcode

    def __str__(self) -> str:
        #if runtime bytecode is a list, join to string
        if isinstance(self.bytecode, list):
            print("Runtime bytecode: %s" % "".join(self.bytecode))
        else:
            print("Runtime bytecode: %s" % self.bytecode)
        pc_bytecode = pc_bytecode_dict(self.opcode)
        string_result = ""
        for k, v in pc_bytecode.items():
            string_result += ("%s : %s \n" % (hex(k), v.name ))
        return string_result

    def add_obfuscation_flag(self, index, added_bytes):
        self.obfuscation_flags[index] = added_bytes
        print("Added Obf Flag at opcode n°%s with %s bytes added" % (index, added_bytes))

#return a dict with pc as key and bytecode as value
def pc_bytecode_dict(opcodes_obj_list):
    pc = int("0",base=16)   
    pc_bytecode_dict = {}
    iter_opcode = iter(opcodes_obj_list)

    for opcode in iter_opcode:
        if isinstance(opcode, PUSH): #if opcode is a PUSH, increment pc by the number of bytes next to PUSH
            pc_bytecode_dict[pc] = opcode
            pc += opcode.pc_offset + 1
        else:    
            pc_bytecode_dict[pc] = opcode
            pc += 1

    return pc_bytecode_dict
