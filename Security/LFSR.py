
def setup(bits):
    register = []
    for bit in bits:
        register.append(bit)

    return register

def xor(bit1, bit2):
    result = int(bool(int(bit1)) ^ bool(int(bit2)))
    print(f"XORing {bit1} and {bit2} giving {result}")
    return result

def cycle(register):

    # Define how your LFSR looks here
    
    # Example one from lecture
    
    result1 = xor(register[2], register[4])
    result2 =xor(register[1], result1)

    register.insert(0, result2)
        
    output = register[-1]
    register.pop()

    return register, output

def run(starting_bits):
    regiser = setup(starting_bits)
    while True:
        register, output = cycle(regiser)
        print(register)
        print(output)
        input("Enter to cycle again...")
    


bits = input("Select starting bits: ")
run(bits)
