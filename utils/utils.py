import sha3
def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()

#transform list of object to list of type
def object_list_to_type_list(object_list):
    type_list = []
    for object in object_list:
        type_list.append(type(object))
    return type_list

def get_function_signature(function_name):
    encoded_function_name = function_name.encode('utf-8')
    k = sha3.keccak_256()
    k.update(encoded_function_name)
    signature = "0x" + k.hexdigest()[:8]

    print ("Sig of %s is %s" % (encoded_function_name, signature))
    return signature

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

if __name__ == "__main__":
    function_name = input("Enter function name: ")
    get_function_signature("inc()")