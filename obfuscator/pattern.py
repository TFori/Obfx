from opcodes.opcode_obj import *

# schema: [original_contract_pattern , obfuscated_contract_pattern]
# TODO: think about priority order for obfuscation -> a bytecode could have a certain pattern that appear in another pattern
#       and an obfuscation could happen before another would appear next
pattern_dict = {
    "add":            ([ADD] , True, [DUP(2),PUSH(1,"00"),SUB(),SUB(),SWAP(1),POP(),NOT(),PUSH(1,"01"),ADD()] ),
    "payable check" : ([CALLVALUE,DUP,ISZERO,PUSH,JUMPI,PUSH,DUP,REVERT],False,[] ),
  # "test":           ([PUSH,PUSH] , True, [INVALID,REVERT] ),


}