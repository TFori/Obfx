import string
from opcodes.opcode_obj import *
from obfuscator.pattern import *
from utils.utils import object_list_to_type_list, replace_sublist_in_list, get_bytelength_without_push_value, get_bytelength, int_to_hex_string, hex_string_to_int
from utils.contract import *

# identify pattern in the opcode list
# replace the pattern in the original opcode list with the obfuscated pattern
def pattern_matcher(contract: Contract):
    opcode_type_list = object_list_to_type_list(contract.opcode)
    index = 0
    for name, pattern in pattern_dict.items():
        original_pattern = pattern[0]
        replaceable = pattern[1]
        instanciated_pattern = pattern[2]
        if set(original_pattern).issubset(opcode_type_list):
            print("Found pattern \"%s\"" % name)
            if replaceable:
                replace_sublist_in_list(contract,opcode_type_list,original_pattern, instanciated_pattern)
                adjust_jump_2( contract)
            else:
                print("Pattern \"%s\"is not replaceable\n" % name)
                pass

        index += 1


# for JUMP or JUMPI, adjust the value depending on the number of bytes added
def adjust_jump(added_bytes: int, contract: Contract):

    jump_index = 0
    # TODO : adjust push_value depending on whether or not it should
    # we suppose yet that every jump is preceded by a push
    for opcode in contract.opcode:
        if isinstance(opcode, JUMP):
            # because we add 2 bytes for the JUMP adjust
            push_value = int_to_hex_string(added_bytes + 2)
            adjusted_jump = [PUSH(1, push_value), ADD(), JUMP()]
            contract.update_opcode(
                contract.opcode[:jump_index] + adjusted_jump + contract.opcode[jump_index+1:])
            jump_index += get_bytelength(adjusted_jump) - 1
            added_bytes += get_bytelength(adjusted_jump) - 1

        elif isinstance(opcode, JUMPI):
            # because we add 2 bytes for the JUMP adjust
            push_value = int_to_hex_string(added_bytes + 2)
            adjusted_jump = [PUSH(1, push_value), ADD(), JUMPI()]

            contract.update_opcode(
                contract.opcode[:jump_index] + adjusted_jump + contract.opcode[jump_index+1:])
            jump_index += get_bytelength(adjusted_jump) - 1
            added_bytes += get_bytelength(adjusted_jump) - 1

        else:
            jump_index += 1

    pass



def adjust_jump_2(contract: Contract):
    contract_opcode = contract.opcode
    i = 0
    previous_opcode = INVALID()

    for i in range(len(contract_opcode)):
        for flag,added_bytes in contract.obfuscation_flags.items():
            previous_opcode = contract_opcode[i-1]
            current_opcode = contract_opcode[i]

            if isinstance(current_opcode, JUMP) or isinstance(current_opcode, JUMPI):
                    if isinstance(previous_opcode, PUSH):                                           
                            print("previous %s and added %s bytes" % (previous_opcode.name, added_bytes))       
                            new_push_value = hex(int(previous_opcode.value,16) + added_bytes -1)[2:]  #TODO: idk why -1 is necessary
                            new_push_value = hex_string_to_int(new_push_value)
                            new_byte_amount = len(new_push_value) // 2    
                            contract_opcode[i-1] = PUSH(new_byte_amount,new_push_value)
                            contract.update_opcode(contract_opcode)
                            print("new walue is %s" %(contract_opcode[i-1].name))                                                   # type: ignore")



