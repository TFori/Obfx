import string
from opcodes.opcode_obj import *
from obfuscator.pattern import *
from utils.utils import object_list_to_type_list, obfuscate_pattern, get_bytelength_without_push_value, get_bytelength,concatenate_dict_values
from utils.math import *
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
        added_bytes = pattern[3]
        if set(original_pattern).issubset(opcode_type_list):
            print("Found pattern \"%s\"" % name)
            if replaceable:
                total_added_bytes = obfuscate_pattern(contract,opcode_type_list,original_pattern, instanciated_pattern, added_bytes)
                adjust_jump_3(contract)
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
        for flag,added_bytes in contract.obfuscation_flags.items(): #TODO: adjust multiple times by each flagzsz
            previous_opcode = contract_opcode[i-1]
            current_opcode = contract_opcode[i]

            if isinstance(current_opcode, JUMP) or isinstance(current_opcode, JUMPI):
                    if isinstance(previous_opcode, PUSH):                                           
                            print("previous %s and added %s bytes" % (previous_opcode.name, added_bytes))       
                            new_push_value = hex(int(previous_opcode.value,16) + added_bytes )[2:]
                            new_push_value = add_0_to_hex(new_push_value)
                            new_byte_amount = len(new_push_value) // 2    
                            contract_opcode[i-1] = PUSH(new_byte_amount,new_push_value)
                            contract.update_opcode(contract_opcode)
                            print("new walue is %s" %(contract_opcode[i-1].name))                                                   # type: ignore")



def adjust_jump_3(contract : Contract):
    contract_opcode = contract.opcode
    pc_opcode = pc_opcode_dict(contract.opcode)

    for i in range(len(pc_opcode)):   #TODO: adjust jump depending on flag, calculate amount of flag after the current jump so we know total added bytes
            current_opcode = list(pc_opcode.items())[i][1]
            previous_opcode = list(pc_opcode.items())[i-1][1]

            if ( isinstance(current_opcode, JUMP) or isinstance(current_opcode, JUMPI) ) and isinstance(previous_opcode, PUSH):
                pc_push_elt = list(pc_opcode.items())[i-1]
                push_value = previous_opcode.value
                jump_target = push_value
    
                total_added_bytes = get_bytes_added(contract, jump_target)

                pc_push_elt[1].value = add_0_to_hex(hex(int(pc_push_elt[1].value,16) + total_added_bytes)[2:])          # type: ignore
                print("              ==> %s" % pc_push_elt[1].name)
                pc_opcode[pc_push_elt[0]] = pc_push_elt[1]
    
            
    string_result = ""
    for k, v in pc_opcode.items():
        string_result += ("%s : %s \n" % (hex(k), v.name ))                                    # type: ignore

    contract.update_opcode(list(pc_opcode.values()))

#amout of bytes added between jump and jumpdest
def get_bytes_added(contract : Contract, aim_flag):
    total_added_bytes = 0
    for flag,added_bytes in contract.obfuscation_flags.items():
        if flag < int(aim_flag,16):
            total_added_bytes += added_bytes

    return total_added_bytes




#add hex number with integer
def hex_add(hex_number, integer):
    return hex(int(hex_number,16) + integer)