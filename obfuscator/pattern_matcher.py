from opcodes.opcode_obj import *
from obfuscator.pattern import *
from utils.utils import object_list_to_type_list
from utils.contract import *

#identify pattern in the opcode list
#replace the pattern in the original opcode list with the obfuscated pattern
def pattern_matcher(contract):
    opcode_type_list = object_list_to_type_list(contract.opcode)
    index = 0
    for name,pattern in pattern_dict.items():
        original_pattern = pattern[0]
        replaceable = pattern[1]
        instanciated_pattern = pattern[2]
        i_p_length = len(instanciated_pattern)
        #TODO : adjust JUMP value depending on the number of opcodes added
        if set(original_pattern).issubset(opcode_type_list):
            print("Found pattern \"%s\"\n" % name)
            if replaceable : 
                replace_list(contract,opcode_type_list, original_pattern, instanciated_pattern)


        index += 1

#for JUMP or JUMPI, adjust the value depending on the number of bytes added
def adjust_jump(added_bytes,jump_index,contract):
    jump_index = 0
    print("called adjust_jump")
    #TODO : adjust push_value depending on whether or not it should
    #we suppose yet that every jump is preceded by a push
    for opcode in contract.opcode:
            if isinstance(opcode,JUMP):
                push_value = int_to_hex_string(added_bytes + 2) # because we add 2 bytes for the JUMP adjust
                adjusted_jump = [PUSH(1,push_value),ADD(), JUMP()]
                contract.update_opcode(contract.opcode[:jump_index] + adjusted_jump + contract.opcode[jump_index+1:])
                jump_index += get_bytelength(adjusted_jump) -1
                added_bytes += get_bytelength(adjusted_jump) - 1
            elif isinstance(opcode,JUMPI):
                push_value = int_to_hex_string(added_bytes + 2) # because we add 2 bytes for the JUMP adjust
                adjusted_jump = [PUSH(1,push_value),ADD(), JUMPI()]

                contract.update_opcode(contract.opcode[:jump_index] + adjusted_jump + contract.opcode[jump_index+1:])
                jump_index += get_bytelength(adjusted_jump) -1
                added_bytes += get_bytelength(adjusted_jump) - 1

            else:
                jump_index += 1




    pass


#replace subset of a list with another list
def replace_list(contract, opcode_type_list, original_pattern, instanciated_pattern):
    index = 0
    jump_dict = {}
    added_bytes = 0
    for element in opcode_type_list:
        if element == JUMP:
            jump_dict[index] = (JUMP, added_bytes)

        elif element == JUMPI:
            jump_dict[index] = (JUMPI, added_bytes)

        elif element == original_pattern[0]:
            if opcode_type_list[index:index+len(original_pattern)] == original_pattern:

                contract.update_opcode(contract.opcode[:index] + instanciated_pattern + contract.opcode[index+len(original_pattern):])

                added_bytes += get_bytelength(instanciated_pattern) # -1 because we replace one opcode by multiple opcodes
                index += added_bytes

                adjust_jump(added_bytes,index,contract)
                print("Added %s bytes" % added_bytes)

        index += 1

def int_to_hex_string(integer):
    hex_string = hex(integer)[2:]
    if len(hex_string) % 2 != 0:
        hex_string = "0"+hex_string
    return hex_string

#get bytelength from instanciated pattern
def get_bytelength(instanciated_pattern):
    bytelength = 0
    for opcode in instanciated_pattern:
        if isinstance(opcode,PUSH):
            bytelength += opcode.pc_offset + 1
        else:
            bytelength += 1
    return bytelength