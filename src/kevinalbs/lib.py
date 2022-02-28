# This file currently has no theme.

def bin2hex (bin):
    """
    print binary as hex
    """
    if type(bin) != bytes:
        raise Exception("Expected bytes")
    for byte in bin:
        print ("{:02x}".format(byte), end="")
    print ()
