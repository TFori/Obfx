
# https://stackoverflow.com/questions/32362148/typeerror-type-object-is-not-iterable-iterating-over-object-instances
class OPCODE(type):
    name = "OPCODE"

    def __iter__(cls):
        return iter(cls.name)


class STOP(metaclass=OPCODE):
    opcode = "0x00"
    name = "STOP"
    ins = 0
    outs = 0
    gas = 0


class ADD(metaclass=OPCODE):
    opcode = "0x01"
    name = "ADD"
    ins = 2
    outs = 1
    gas = 3


class MUL(metaclass=OPCODE):
    opcode = "0x02"
    name = "MUL"
    ins = 2
    outs = 1
    gas = 5


class SUB(metaclass=OPCODE):
    opcode = "0x03"
    name = "SUB"
    ins = 2
    outs = 1
    gas = 3


class DIV(metaclass=OPCODE):
    opcode = "0x04"
    name = "DIV"
    ins = 2
    outs = 1
    gas = 5


class SDIV(metaclass=OPCODE):
    opcode = "0x05"
    name = "SDIV"
    ins = 2
    outs = 1
    gas = 5


class MOD(metaclass=OPCODE):
    opcode = "0x06"
    name = "MOD"
    ins = 2
    outs = 1
    gas = 5


class SMOD(metaclass=OPCODE):
    opcode = "0x07"
    name = "SMOD"
    ins = 2
    outs = 1
    gas = 5


class ADDMOD(metaclass=OPCODE):
    opcode = "0x08"
    name = "ADDMOD"
    ins = 3
    outs = 1
    gas = 8


class MULMOD(metaclass=OPCODE):
    opcode = "0x09"
    name = "MULMOD"
    ins = 3
    outs = 1
    gas = 8


class EXP(metaclass=OPCODE):
    opcode = "0x0a"
    name = "EXP"
    ins = 2
    outs = 1
    gas = 10


class SIGNEXTEND(metaclass=OPCODE):
    opcode = "0x0b"
    name = "SIGNEXTEND"
    ins = 2
    outs = 1
    gas = 5


class LT(metaclass=OPCODE):
    opcode = "0x10"
    name = "LT"
    ins = 2
    outs = 1
    gas = 3


class GT(metaclass=OPCODE):
    opcode = "0x11"
    name = "GT"
    ins = 2
    outs = 1
    gas = 3


class SLT(metaclass=OPCODE):
    opcode = "0x12"
    name = "SLT"
    ins = 2
    outs = 1
    gas = 3


class SGT(metaclass=OPCODE):
    opcode = "0x13"
    name = "SGT"
    ins = 2
    outs = 1
    gas = 3


class EQ(metaclass=OPCODE):
    opcode = "0x14"
    name = "EQ"
    ins = 2
    outs = 1
    gas = 3


class ISZERO(metaclass=OPCODE):
    opcode = "0x15"
    name = "ISZERO"
    ins = 1
    outs = 1
    gas = 3


class AND(metaclass=OPCODE):
    opcode = "0x16"
    name = "AND"
    ins = 2
    outs = 1
    gas = 3


class OR(metaclass=OPCODE):
    opcode = "0x17"
    name = "OR"
    ins = 2
    outs = 1
    gas = 3


class XOR(metaclass=OPCODE):
    opcode = "0x18"
    name = "XOR"
    ins = 2
    outs = 1
    gas = 3


class NOT(metaclass=OPCODE):
    opcode = "0x19"
    name = "NOT"
    ins = 1
    outs = 1
    gas = 3


class BYTE(metaclass=OPCODE):
    opcode = "0x1a"
    name = "BYTE"
    ins = 2
    outs = 1
    gas = 3


class SHL(metaclass=OPCODE):
    opcode = "0x1b"
    name = "SHL"
    ins = 2
    outs = 1
    gas = 3


class SHR(metaclass=OPCODE):
    opcode = "0x1c"
    name = "SHR"
    ins = 2
    outs = 1
    gas = 3


class SAR(metaclass=OPCODE):
    opcode = "0x1d"
    name = "SAR"
    ins = 2
    outs = 1
    gas = 3


class KECCAK256(metaclass=OPCODE):
    opcode = "0x20"
    name = "KECCAK256"
    ins = 2
    outs = 1
    gas = 30


class SHA3(metaclass=OPCODE):
    opcode = "0x20"
    name = "SHA3"
    ins = 2
    outs = 1
    gas = 30


class ADDRESS(metaclass=OPCODE):
    opcode = "0x30"
    name = "ADDRESS"
    ins = 0
    outs = 1
    gas = 2


class BALANCE(metaclass=OPCODE):
    opcode = "0x31"
    name = "BALANCE"
    ins = 1
    outs = 1
    gas = 20


class ORIGIN(metaclass=OPCODE):
    opcode = "0x32"
    name = "ORIGIN"
    ins = 0
    outs = 1
    gas = 2


class CALLER(metaclass=OPCODE):
    opcode = "0x33"
    name = "CALLER"
    ins = 0
    outs = 1
    gas = 2


class CALLVALUE(metaclass=OPCODE):
    opcode = "0x34"
    name = "CALLVALUE"
    ins = 0
    outs = 1
    gas = 2


class CALLDATALOAD(metaclass=OPCODE):
    opcode = "0x35"
    name = "CALLDATALOAD"
    ins = 1
    outs = 1
    gas = 3


class CALLDATASIZE(metaclass=OPCODE):
    opcode = "0x36"
    name = "CALLDATASIZE"
    ins = 0
    outs = 1
    gas = 2


class CALLDATACOPY(metaclass=OPCODE):
    opcode = "0x37"
    name = "CALLDATACOPY"
    ins = 3
    outs = 0
    gas = 3


class CODESIZE(metaclass=OPCODE):
    opcode = "0x38"
    name = "CODESIZE"
    ins = 0
    outs = 1
    gas = 2


class CODECOPY(metaclass=OPCODE):
    opcode = "0x39"
    name = "CODECOPY"
    ins = 3
    outs = 0
    gas = 3


class GASPRICE(metaclass=OPCODE):
    opcode = "0x3a"
    name = "GASPRICE"
    ins = 0
    outs = 1
    gas = 2


class EXTCODESIZE(metaclass=OPCODE):
    opcode = "0x3b"
    name = "EXTCODESIZE"
    ins = 1
    outs = 1
    gas = 20


class EXTCODECOPY(metaclass=OPCODE):
    opcode = "0x3c"
    name = "EXTCODECOPY"
    ins = 4
    outs = 0
    gas = 20


class RETURNDATASIZE(metaclass=OPCODE):
    opcode = "0x3d"
    name = "RETURNDATASIZE"
    ins = 0
    outs = 1
    gas = 2


class RETURNDATACOPY(metaclass=OPCODE):
    opcode = "0x3e"
    name = "RETURNDATACOPY"
    ins = 3
    outs = 0
    gas = 3


class EXTCODEHASH(metaclass=OPCODE):
    opcode = "0x3f"
    name = "EXTCODEHASH"
    ins = 1
    outs = 1
    gas = 400


class BLOCKHASH(metaclass=OPCODE):
    opcode = "0x40"
    name = "BLOCKHASH"
    ins = 1
    outs = 1
    gas = 20


class COINBASE(metaclass=OPCODE):
    opcode = "0x41"
    name = "COINBASE"
    ins = 0
    outs = 1
    gas = 2


class TIMESTAMP(metaclass=OPCODE):
    opcode = "0x42"
    name = "TIMESTAMP"
    ins = 0
    outs = 1
    gas = 2


class NUMBER(metaclass=OPCODE):
    opcode = "0x43"
    name = "NUMBER"
    ins = 0
    outs = 1
    gas = 2


class DIFFICULTY(metaclass=OPCODE):
    opcode = "0x44"
    name = "DIFFICULTY"
    ins = 0
    outs = 1
    gas = 2


class GASLIMIT(metaclass=OPCODE):
    opcode = "0x45"
    name = "GASLIMIT"
    ins = 0
    outs = 1
    gas = 2


class CHAINID(metaclass=OPCODE):
    opcode = "0x46"
    name = "CHAINID"
    ins = 0
    outs = 1
    gas = 2


class SELFBALANCE(metaclass=OPCODE):
    opcode = "0x47"
    name = "SELFBALANCE"
    ins = 0
    outs = 1
    gas = 5


class BASEFEE(metaclass=OPCODE):
    opcode = "0x48"
    name = "BASEFEE"
    ins = 0
    outs = 1
    gas = 2


class POP(metaclass=OPCODE):
    opcode = "0x50"
    name = "POP"
    ins = 1
    outs = 0
    gas = 2


class MLOAD(metaclass=OPCODE):
    opcode = "0x51"
    name = "MLOAD"
    ins = 1
    outs = 1
    gas = 3


class MSTORE(metaclass=OPCODE):
    opcode = "0x52"
    name = "MSTORE"
    ins = 2
    outs = 0
    gas = 3


class MSTORE8(metaclass=OPCODE):
    opcode = "0x53"
    name = "MSTORE8"
    ins = 2
    outs = 0
    gas = 3


class SLOAD(metaclass=OPCODE):
    opcode = "0x54"
    name = "SLOAD"
    ins = 1
    outs = 1
    gas = 50


class SSTORE(metaclass=OPCODE):
    opcode = "0x55"
    name = "SSTORE"
    ins = 2
    outs = 0
    gas = 0


class JUMP(metaclass=OPCODE):
    opcode = "0x56"
    name = "JUMP"
    ins = 1
    outs = 0
    gas = 8


class JUMPI(metaclass=OPCODE):
    opcode = "0x57"
    name = "JUMPI"
    ins = 2
    outs = 0
    gas = 10


class PC(metaclass=OPCODE):
    opcode = "0x58"
    name = "PC"
    ins = 0
    outs = 1
    gas = 2


class MSIZE(metaclass=OPCODE):
    opcode = "0x59"
    name = "MSIZE"
    ins = 0
    outs = 1
    gas = 2


class GAS(metaclass=OPCODE):
    opcode = "0x5a"
    name = "GAS"
    ins = 0
    outs = 1
    gas = 2


class JUMPDEST(metaclass=OPCODE):
    opcode = "0x5b"
    name = "JUMPDEST"
    ins = 0
    outs = 0
    gas = 1


class PUSH(metaclass=OPCODE):
    name = "PUSH"
    ins = 0
    outs = 1
    gas = 3
    # init PUSH obj, 1<byte_amount<32, value as a string ("0x6541")

    def __init__(self, byte_amount, value):
        self.opcode = hex(int("60", 16) + byte_amount - 1)  # (0x60 to 0x7f)
        self.name = "PUSH%s %s" % (byte_amount, value)
        self.value = (value)
        self.pc_offset = byte_amount

        if byte_amount > 32 | byte_amount < 1:
            raise Exception('Wrong amount of byte for PUSH')
        else:
            byte_amount = byte_amount

        if len(str(value)) != byte_amount*2:
            raise ValueError("Invalid value (%s) for PUSH with byte_amount = %s" % (value,byte_amount))
        else:
            value = value


class DUP(metaclass=OPCODE):
    name = "DUP"
    gas = 3

    def __init__(self, stack_position):
        self.opcode = hex(int("80", 16) + stack_position - 1)  # (0x80 to 0x8f)
        self.name = "DUP{}".format(stack_position)
        self.ins = stack_position
        self.outs = stack_position + 1
        self.gas = 3

        if stack_position > 16 | stack_position < 1:
            raise Exception('Wrong stack position for DUP')
        else:
            stack_position = stack_position


class SWAP:
    name = "SWAP"
    gas = 3

    def __init__(self, stack_position):
        self.opcode = hex(int("90", 16) + stack_position - 1)  # (0x90 to 0x9f)
        self.name = "SWAP{}".format(stack_position)
        self.ins = stack_position + 1
        self.outs = stack_position + 1

        if stack_position > 16 | stack_position < 1:
            raise Exception('Wrong stack position for SWAP')
        else:
            stack_position = stack_position


class LOG(metaclass=OPCODE):
    name = "LOG"
    outs = 0
    gas = 375

    def __init__(self, log_number):
        self.opcode = hex(int("a0", 16) + log_number - 1)  # (0xa0 to 0xa4)
        self.name = "LOG{}".format(log_number)
        self.ins = log_number + 2

        if log_number > 4 | log_number < 1:
            raise Exception('Wrong log number for LOG')
        else:
            log_number = log_number


class CREATE(metaclass=OPCODE):
    opcode = "0xf0"
    name = "CREATE"
    ins = 3
    outs = 1
    gas = 32000


class CALL(metaclass=OPCODE):
    opcode = "0xf1"
    name = "CALL"
    ins = 7
    outs = 1
    gas = 40


class CALLCODE(metaclass=OPCODE):
    opcode = "0xf2"
    name = "CALLCODE"
    ins = 7
    outs = 1
    gas = 40


class RETURN(metaclass=OPCODE):
    opcode = "0xf3"
    name = "RETURN"
    ins = 2
    outs = 0
    gas = 0


class DELEGATECALL(metaclass=OPCODE):
    opcode = "0xf4"
    name = "DELEGATECALL"
    ins = 6
    outs = 1
    gas = 40


class CREATE2(metaclass=OPCODE):
    opcode = "0xf5"
    name = "CREATE2"
    ins = 4
    outs = 1
    gas = 32000


class STATICCALL(metaclass=OPCODE):
    opcode = "0xfa"
    name = "STATICCALL"
    ins = 6
    outs = 1
    gas = 40


class REVERT(metaclass=OPCODE):
    opcode = "0xfd"
    name = "REVERT"
    ins = 2
    outs = 0
    gas = 0


class INVALID(metaclass=OPCODE):
    opcode = "0xfe"
    name = "INVALID"
    ins = 0
    outs = 0
    gas = 0


class SELFDESTRUCT(metaclass=OPCODE):
    opcode = "0xff"
    name = "SELFDESTRUCT"
    ins = 1
    outs = 0
    gas = 0
