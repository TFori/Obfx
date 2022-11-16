from opcodes.opcode_obj import *
# schema": [opcode, ins, outs, gas]
opcodes_dict = {
    "0x00": [STOP, 0, 0, 0],
    "0x01": [ADD, 2, 1, 3],
    "0x02": [MUL, 2, 1, 5],
    "0x03": [SUB, 2, 1, 3],
    "0x04": [DIV, 2, 1, 5],
    "0x05": [SDIV, 2, 1, 5],
    "0x06": [MOD, 2, 1, 5],
    "0x07": [SMOD, 2, 1, 5],
    "0x08": [ADDMOD, 3, 1, 8],
    "0x09": [MULMOD, 3, 1, 8],
    "0x0a": [EXP, 2, 1, 10],
    "0x0b": [SIGNEXTEND, 2, 1, 5],
    "0x10": [LT, 2, 1, 3],
    "0x11": [GT, 2, 1, 3],
    "0x12": [SLT, 2, 1, 3],
    "0x13": [SGT, 2, 1, 3],
    "0x14": [EQ, 2, 1, 3],
    "0x15": [ISZERO, 1, 1, 3],
    "0x16": [AND, 2, 1, 3],
    "0x17": [OR, 2, 1, 3],
    "0x18": [XOR, 2, 1, 3],
    "0x19": [NOT, 1, 1, 3],
    "0x1a": [BYTE, 2, 1, 3],
    "0x1b": [SHL, 2, 1, 3],
    "0x1c": [SHR, 2, 1, 3],
    "0x1d": [SAR, 2, 1, 3],
    "0x20": [KECCAK256, 2, 1, 30],
    "0x30": [ADDRESS, 0, 1, 2],
    "0x31": [BALANCE, 1, 1, 20],  # now 400
    "0x32": [ORIGIN, 0, 1, 2],
    "0x33": [CALLER, 0, 1, 2],
    "0x34": [CALLVALUE, 0, 1, 2],
    "0x35": [CALLDATALOAD, 1, 1, 3],
    "0x36": [CALLDATASIZE, 0, 1, 2],
    "0x37": [CALLDATACOPY, 3, 0, 3],
    "0x38": [CODESIZE, 0, 1, 2],
    "0x39": [CODECOPY, 3, 0, 3],
    "0x3a": [GASPRICE, 0, 1, 2],
    "0x3b": [EXTCODESIZE, 1, 1, 20], # now 700
    "0x3c": [EXTCODECOPY, 4, 0, 20], # now 700
    "0x3d": [RETURNDATASIZE, 0, 1, 2],
    "0x3e": [RETURNDATACOPY, 3, 0, 3],
    "0x3f": [EXTCODEHASH, 1, 1, 3],
    "0x40": [BLOCKHASH, 1, 1, 20],
    "0x41": [COINBASE, 0, 1, 2],
    "0x42": [TIMESTAMP, 0, 1, 2],
    "0x43": [NUMBER, 0, 1, 2],
    "0x44": [DIFFICULTY, 0, 1, 2],
    "0x45": [GASLIMIT, 0, 1, 2],
    "0x46": [CHAINID, 0, 1, 2],
    "0x47": [SELFBALANCE, 0, 1, 5],
    "0x48": [BASEFEE, 0, 1, 2],
    "0x50": [POP, 1, 0, 2],
    "0x51": [MLOAD, 1, 1, 3],
    "0x52": [MSTORE, 2, 0, 3],
    "0x53": [MSTORE8, 2, 0, 3],
    "0x54": [SLOAD, 1, 1, 50],  # 200 now
    # actual cost 5000-20000 depending on circumstance
    "0x55": [SSTORE, 2, 0, 0],
    "0x56": [JUMP, 1, 0, 8],
    "0x57": [JUMPI, 2, 0, 10],
    "0x58": [PC, 0, 1, 2],
    "0x59": [MSIZE, 0, 1, 2],
    "0x5a": [GAS, 0, 1, 2],
    "0x5b": [JUMPDEST,0,0,1],
    "0x60": [PUSH,0,1,3],
    "0x61": [PUSH,0,1,3],
    "0x62": [PUSH,0,1,3],
    "0x63": [PUSH,0,1,3],
    "0x64": [PUSH,0,1,3],
    "0x65": [PUSH,0,1,3],
    "0x66": [PUSH,0,1,3],
    "0x67": [PUSH,0,1,3],
    "0x68": [PUSH,0,1,3],
    "0x69": [PUSH,0,1,3],
    "0x6a": [PUSH,0,1,3],
    "0x6b": [PUSH,0,1,3],
    "0x6c": [PUSH,0,1,3],
    "0x6d": [PUSH,0,1,3],
    "0x6e": [PUSH,0,1,3],
    "0x6f": [PUSH,0,1,3],
    "0x70": [PUSH,0,1,3],
    "0x71": [PUSH,0,1,3],
    "0x72": [PUSH,0,1,3],
    "0x73": [PUSH,0,1,3],
    "0x74": [PUSH,0,1,3],
    "0x75": [PUSH,0,1,3],
    "0x76": [PUSH,0,1,3],
    "0x77": [PUSH,0,1,3],
    "0x77": [PUSH,0,1,3],
    "0x79": [PUSH,0,1,3],
    "0x7a": [PUSH,0,1,3],
    "0x7b": [PUSH,0,1,3],
    "0x7c": [PUSH,0,1,3],
    "0x7d": [PUSH,0,1,3],
    "0x7e": [PUSH,0,1,3],
    "0x7f": [PUSH,0,1,3],
    "0x80": [DUP,1,2,3],
    "0x81": [DUP,2,3,3],
    "0x82": [DUP,3,4,3],
    "0x83": [DUP,4,5,3],
    "0x84": [DUP,5,6,3],
    "0x85": [DUP,6,7,3],
    "0x86": [DUP,7,8,3],
    "0x87": [DUP,8,9,3],
    "0x88": [DUP,9,10,3],
    "0x89": [DUP,10,11,3],
    "0x8a": [DUP,11,12,3],
    "0x8b": [DUP,12,13,3],
    "0x8c": [DUP,13,14,3],
    "0x8d": [DUP,14,15,3],
    "0x8e": [DUP,15,16,3],
    "0x8f": [DUP,16,17,3],
    "0x90": [SWAP,2,2,3],
    "0x91": [SWAP,3,3,3],
    "0x92": [SWAP,4,4,3],
    "0x93": [SWAP,5,5,3],
    "0x94": [SWAP,6,6,3],
    "0x95": [SWAP,7,7,3],
    "0x96": [SWAP,8,8,3],
    "0x97": [SWAP,9,9,3],
    "0x98": [SWAP,10,10,3],
    "0x99": [SWAP,11,11,3],
    "0x9a": [SWAP,12,12,3],
    "0x9b": [SWAP,13,13,3],
    "0x9c": [SWAP,14,14,3],
    "0x9d": [SWAP,15,15,3],
    "0x9e": [SWAP,16,16,3],
    "0x9f": [SWAP,17,17,3],  
    "0xa0": [LOG, 2, 0, 375],
    "0xa1": [LOG, 3, 0, 750],
    "0xa2": [LOG, 4, 0, 1125],
    "0xa3": [LOG, 5, 0, 1500],
    "0xa4": [LOG, 6, 0, 1875],
    # "0xe1": [SLOADBYTES, 3, 0, 50], # to be discontinued
    # "0xe2": [SSTOREBYTES, 3, 0, 0], # to be discontinued
    # "0xe3": [SSIZE, 1, 1, 50], # to be discontinued
    "0xf0": [CREATE, 3, 1, 32000],
    "0xf1": [CALL, 7, 1, 40],  # 700 now
    "0xf2": [CALLCODE, 7, 1, 40],  # 700 now
    "0xf3": [RETURN, 2, 0, 0],
    "0xf4": [DELEGATECALL, 6, 1, 40],  # 700 now
    "0xf5": [CREATE2, 7, 1, 40],
    "0xfa": [STATICCALL, 6, 1, 40],
    "0xfd": [REVERT, 2, 0, 0],
    "0xfe":[INVALID,0,0,0],
    "0xff": [SELFDESTRUCT, 1, 0, 0],  # 5000 now
}

#add invalid value to dict
#add 0x01 to make the range from go from (a) to (b) and not (a) to (b-1)
for i in range(0x0c,0x0f + 0x01):
    opcodes_dict["0x0"+hex(i)[2:]]=[INVALID,0,0,0] #add "0" to "0x" to make it 0x0c or its "0xc"

for i in range(0x1e,0x1f + 0x01):
    opcodes_dict["0x"+hex(i)[2:]]=[INVALID,0,0,0]

for i in range(0x21,0x2F + 0x01):
    opcodes_dict["0x"+hex(i)[2:]]=[INVALID,0,0,0]

for i in range(0x49,0x4f + 0x01):
    opcodes_dict["0x"+hex(i)[2:]]=[INVALID,0,0,0]

for i in range(0x5c,0x5f + 0x01):
    opcodes_dict["0x"+hex(i)[2:]]=[INVALID,0,0,0]

for i in range(0xa5,0xef + 0x01):
    opcodes_dict["0x"+hex(i)[2:]]=[INVALID,0,0,0]

for i in range(0xf6,0xf9 + 0x01):
    opcodes_dict["0x"+hex(i)[2:]]=[INVALID,0,0,0]

for i in range(0xfb,0xfc + 0x01):
    opcodes_dict["0x"+hex(i)[2:]]=[INVALID,0,0,0]