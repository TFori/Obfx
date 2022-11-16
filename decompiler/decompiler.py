
from opcodes.opcode_obj import *
from opcodes.opcode_dict import *
# separate text every 2 characters


def text_to_bytecode_list(bytecode):
    bytecode = bytecode.replace(' ', '')
    bytecode = bytecode.replace('0x', '')
    bytecode = bytecode.replace('\n', '')
    bytecode = bytecode.replace('\r', '')
    bytecode = bytecode.replace('\t', '')
    bytecode = bytecode.replace('\v', '')
    bytecode = bytecode.replace('\f', '')
    return [bytecode[i:i+2] for i in range(0, len(bytecode), 2)]


def print_bytecode(bytecode):
    print(' '.join(bytecode))

# translate bytecode array to opcode list


def bytecode_to_opcode(bytecode):
    opcodes_obj_list = list()
    top_stack_bytes = hex(0)
    i = 0
    while i < len(bytecode):

        # trasnform "60" to "0x60" to then match with opcodes_dict
        opcode = ("0x%0.2X" % int(bytecode[i], 16)).lower()
        if opcodes_dict[opcode][0] == PUSH:
            # (0x60 to 0x7f) #get the number of bytes next to PUSH instruction
            push_offset = int(bytecode[i], 16) - int("60", 16) + 1
            # merge the bytes next to PUSH instruction
            value = "".join(bytecode[i+1:i+push_offset+1])
            opcodes_obj_list.append(
                PUSH(push_offset, value))  # create PUSH object
            i += push_offset

        elif opcodes_dict[opcode][0] == DUP:
            # (0x80 to 0x8f) #get the number of bytes next to DUP instruction
            stack_position = int(bytecode[i], 16) - int("80", 16) + 1

            opcodes_obj_list.append(DUP(stack_position))  # create DUP object

        elif opcodes_dict[opcode][0] == SWAP:
            stack_position = int(bytecode[i], 16) - int("90", 16) + 1
            opcodes_obj_list.append(SWAP(stack_position))

        elif opcodes_dict[opcode][0] == LOG:
            log_number = int(bytecode[i], 16) - int("a0", 16)
            opcodes_obj_list.append(LOG(log_number))

        else:
            opcodes_obj_list.append(opcodes_dict[opcode][0]())

        i += 1

    return opcodes_obj_list

# transform opcode list to bytecode string without "0x"
def opcode_to_bytecode(opcode_list):
    bytecode = ""
    for opcode in opcode_list:
        if isinstance(opcode, PUSH):
            bytecode += opcode.opcode[2:] + opcode.value
        else:
            bytecode += opcode.opcode[2:]
    return bytecode
