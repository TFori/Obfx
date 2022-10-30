from opcodes.opcode_obj import *

# schema: [original_contract_pattern , obfuscated_contract_pattern]
pattern_dict = {
    "add": ([ADD] , True, [DUP(2),PUSH(1,"00"),SUB(),SUB(),SWAP(1),POP(),NOT(),PUSH(1,"01"),ADD()] ),
    "payable check" : ( [CALLVALUE,DUP,ISZERO,PUSH,JUMPI,PUSH,DUP,REVERT],False,[] )

}