import matplotlib.pyplot as plt
import string

ciphertext ="lrvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi jx qmbm wi bpr xjvni mkd ymibrut jx irhx wi bpr riirkvr jx ymbinlmtmipw utn qmumbr dj w ipmhh but bj rhnvwdmbr bpr yjeryrkbi jx bpr qmbm mvvjudwko bj yt wkbrusurbmbwjk lmird jk xjubt trmui jx ibndt wb wi kjb mk rmit bmiq bj rashmwk rmvp yjeryrkb mkd wbi iwokwxwvmkvr mkd ijyr ynib urymwk nkrashmwkrd bj ower m vjyshrbr rashmkmbwjk jkr cjnhd pmer bj lr fnmhwxwrd mkd wkiswurd bj invp mk rabrkb bpmb pr vjnhd urmvp bpr ibmbr jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii ijnkd mkd ipmsrhrii ipmsr w dj kjb drry ytirhx bpr xwkmh mnbpjuwbt lnb yt rasruwrkvr cwbp qmbm pmi hrxb kj djnlb bpmb bpr xjhhjcwko wi bpr sujsru msshwvmbwjk mkd wkbrusurbmbwjk w jxxru yt bprjuwri wk bpr pjsr bpmb bpr riirkvr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb"

plaintext = "because the practice of the basic movements of kata is the focus and mastery of self is the essence of matsubayashi ryu karate do i shall try to elucidate the movements of the kata according to my interpretation based on forty years of study it is not an easy task to explain each movement and its significance and some must remain unexplained to give a complete explanation one would have to be jualified and inspired to such an extent that he could reach the state of enlightened mind capable of recognizing soundless sound and shapeless shape i do not deem myself the final authority but my experience with kata has left no doubt that the follow ing is the proper application and interpretation i offer my theories in the hope that the essence of okinawan karate will remain intact"

common_letters = ["e", "a", "r", "i", "o", "t", "n","s",
                  "l","c","u","d","p","m","h","g","b","f","y","w","k","v","x","z","j","q"]
common_letters = common_letters[::-1]

def collect_frequency(alphabet):
    # Collect the frequency of each letter in the cipherciphertext
    freq = {x:0 for x in alphabet}
    for letter in ciphertext:
        if letter != " ":
            freq[letter] += 1

    return freq

def gen_alpha():
    # Generate a list of all letters in the alphabet in-order
    alphabet = list(string.ascii_lowercase)
    return alphabet

def sort_freq(freq):
    # Sort the dictionary of letters and frequency by the frequency
    freq = {k: v for k, v in sorted(freq.items(), key=lambda item: item[1])}
    return freq

def swap_corresponding_common_letter(freq_sorted):
    # Swap the letter with the corresponding most common letter
    for index, item in enumerate(freq_sorted):
        freq_sorted[item] = common_letters[index]
    return freq_sorted

def plot(freq):
    plt.bar(freq.keys(), freq.values())
    plt.show()

def freq_anal(freq):
    # Perform the frequency analysis workflow
    print("Performing frequency analysis...")
    alphabet = gen_alpha()
    freq = collect_frequency(alphabet)
    freq_sorted = sort_freq(freq)
    do_graph = input("Would you like to view a graph of the letter frequency? Y/n: ")
    print()
    if do_graph.lower() == "y":
        plot(freq_sorted)
    swap_corresponding_common_letter(freq)
    print("Finished frequency analysis and swap")

def decipher(alphabet):
    print(alphabet)
    result = []
    for letter in ciphertext:
        if letter == " ":
            result.append(letter)
        else:
            result.append(alphabet[letter])
    return "".join(result)

def manual_mode(letter_map):
    alphabet = gen_alpha()
    if not letter_map:
        letter_map= {letter: letter for letter in alphabet}
    while True:
        print("Current decryption guess:")
        guess = decipher(letter_map)
        print(guess)
        current = input("Enter current letter: ")
        desired = input("Enter letter to swap: ")
        print()
        # Example
        # Change 't' to ''i'
        # Swap where 't' is to where 'i' is in freq
        for key, value in letter_map.items():
            if value == current:
                letter_map[key] = desired
            elif value == desired:
                letter_map[key] = current

def game():
    print("Encrypted ciphertext:")
    print(ciphertext)
    print()
    do_freq = input("Would you like to perform frequency analysis? Y/n: ")
    print()
    letter_map = False
    if do_freq.lower() == "y":
        letter_map = freq_anal()
    manual_mode(letter_map)

game()
