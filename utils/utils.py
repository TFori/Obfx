import sha3
from utils.contract import *
from opcodes.opcode_dict import *
from opcodes.opcode_obj import *
def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()

#transform list of object to list of type
def object_list_to_type_list(object_list):
    type_list = []
    for object in object_list:
        type_list.append(type(object))
    return type_list



def isolate_creation_runtime_bytecode(bytecode):
    index = 0
    runtime_bytecode = bytecode
    creation_bytecode = []
    for byte in bytecode:
        if byte == "f3" and bytecode[index+1] == "fe":
            runtime_bytecode = bytecode[index+2:]   #+2 to include/exclude 0xf3 & 0xfe
            creation_bytecode = bytecode[:index+2]
        index += 1
    return creation_bytecode, runtime_bytecode

#replace every occurence of a sublist in a list
def replace_sublist_in_list(contract:Contract, opcode_type_list, original_pattern, instanciated_pattern):
    current_opcode = contract.opcode
    added_bytes = 0
    obf_i = 0

    for i in range(len(opcode_type_list)):
        if opcode_type_list[i:i+len(original_pattern)] == original_pattern:

            current_opcode[obf_i:obf_i+len(original_pattern)] = instanciated_pattern

            obf_i+=len(instanciated_pattern)-1 #TODO: the (-1) might be a bug source when multiple obf from a single pattern)
            added_bytes += get_bytelength(instanciated_pattern)
            print(i)
            contract.add_obfuscation_flag(get_bytelength(current_opcode[0:i]),added_bytes)

        obf_i += 1
    contract.update_opcode(current_opcode)
    return added_bytes

# get bytelength from instanciated pattern
def get_bytelength(instanciated_pattern: list) -> int:
    bytelength = 0
    for opcode in instanciated_pattern:
        if isinstance(opcode, PUSH):
            bytelength += opcode.pc_offset + 1
        else:
            bytelength += 1
    return bytelength

def get_bytelength_without_push_value(instanciated_pattern:list) -> int:
    bytelength = 0
    for opcode in instanciated_pattern:
        bytelength += 1
    return bytelength


def int_to_hex_string(integer: int) -> str:
    hex_string = hex(integer)[2:]
    if len(hex_string) % 2 != 0:
        hex_string = "0"+hex_string
    return hex_string

#if string uneven, add a 0 at the beginning
def hex_string_to_int(hex_string: str) -> str:
    if len(hex_string) % 2 != 0:
        hex_string = "0"+hex_string
    return hex_string

# #replace a list by another list in a list
# def replace_list_in_list(contract: Contract, instanciated_pattern: list, opcode_types: list, original_pattern: list,):
#     index = 0
#     for element in opcode_types:
#         if element == original_pattern[0]:
#             if opcode_types[index:index+len(original_pattern)] == original_pattern:
#                 new_opcode = contract.opcode[0:index] + instanciated_pattern + contract.opcode[index+len(original_pattern):]
#                 contract.update_opcode(new_opcode)
#         index += 1

# #find how many pattern times pattern appear in list
# def count_pattern_in_list(list: list, pattern: list) -> int:
#     count = 0
#     for i in range(len(list)):
#         if list[i:i+len(pattern)] == pattern:
#             count += 1
#     return count

