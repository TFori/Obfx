def int_to_hex_string(integer: int) -> str:
    hex_string = hex(integer)[2:]
    if len(hex_string) % 2 != 0:
        hex_string = "0"+hex_string
    return hex_string

#if string uneven, add a 0 at the beginning
def add_0_to_hex(hex_string: str) -> str:
    if len(hex_string) % 2 != 0:
        hex_string = "0"+hex_string
    return hex_string