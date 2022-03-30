#/usr/bin/Python3
#/usr/bin/env Python3
#Author: Ar1sto (https://github.com/Ar1sto) | Discord: Omniscius#6583

from random import choice as polyfunction
polycode = ("one()", "two()", "three()")

class polymorphiccode():

# Funktion 1: Normaler String

    def one():
        codeone = """
from subprocess import run
print ("Polymorphic-Code Example: 1")
i = "Omniscius"
example_one = f'''
                ╔═════════════════════╗
                ║█████████████████████║
                ║█████████████████████║
                ║█████████████████████║
                ║█████████████████████║
                ║█████████████████████║
                ║█████████████████████║
                ║█████████████████████║
                ║█████████████████████║
                ╚═════════════════════╝
                       {i}
               '''
run(["lolcat"], input=example_one, text=True)

                  """
        exec(codeone)
        
# Funktion 2: Hexadezimal zu String
        
    def two():
        codetwo = """
from subprocess import run
print ("Polymorphic-Code Example: 2")
i = "4f6d6e6973636975730a"
convert = bytes.fromhex(f'{i}').decode('utf-8')
convert = convert.replace(r'''"\n"''', "")
example_two = f'''
                ╔═════════════════════╗
                ║█████████████████████║
                ║█████████████████████║
                ║█████████████████████║
                ║█████████████████████║
                ║█████████████████████║
                ║█████████████████████║
                ║█████████████████████║
                ║█████████████████████║
                ╚═════════════════════╝
                       {convert}
               '''
run(["lolcat"], input=example_two, text=True)
                  """
        exec(codetwo)
        
# Funktion 3: String-Funktion reverse-String zu Base85 und zurück dekodiert dann wieder reverse

    def three():
        codethree = """
from subprocess import run
import string, base64
print ("Polymorphic-Code Example: 3")
name = list(string.ascii_lowercase+string.ascii_uppercase)
i = name[40]+name[12]+name[13]+name[8]+name[18]+name[2]+name[8]+name[20]+name[18]
i = i[::-1]
i_bytes = i.encode("ascii")
i_base_bytes = base64.a85encode(i_bytes)
i_bcoded = i_base_bytes.decode("ascii")
i_bcoded_bytes = i_bcoded.encode("ascii")
i_bcoded_decoder = base64.a85decode(i_bcoded_bytes)
i_decoded = i_bcoded_decoder.decode("ascii")
i_reverse_decoded = i_decoded[::-1]
example_three = f'''
                ╔═════════════════════╗
                ║█████████████████████║
                ║█████████████████████║
                ║█████████████████████║
                ║█████████████████████║
                ║█████████████████████║
                ║█████████████████████║
                ║█████████████████████║
                ║█████████████████████║
                ╚═════════════════════╝
                       {i_reverse_decoded}
               '''
run(["lolcat"], input=example_three, text=True)
                  """
        exec(codethree)
execution = polyfunction(polycode)
exec(f"polymorphiccode.{execution}")
