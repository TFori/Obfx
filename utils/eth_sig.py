import sha3

def get_function_signature(function_name):
    encoded_function_name = function_name.encode('utf-8')
    k = sha3.keccak_256()
    k.update(encoded_function_name)
    signature = "0x" + k.hexdigest()[:8]

    print ("Sig of %s is %s" % (encoded_function_name, signature))
    return signature

if __name__ == "__main__":
    function_name = input("Enter function name: ")
    get_function_signature("inc()")