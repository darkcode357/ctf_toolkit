import os,itertools,errno
def int_especial():
    try:
        os.makedirs("../../files/wordlist/int_especial/")
        print("[criando pasta wordlist/int_especial][OK]")
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
        pass
    word_list_name = input("[+]nome da wordlist=>")
    min = input("minimo de caractere=>[" + "]")
    max = input("maximo de caractere=>[" + "]")
    chrs = '1234567890~@#$%^&*()_+=-][}{\|""/?.><,,'
    with open("../../files/wordlist/int_especial/" + word_list_name, "w") as fl:
        min_length, max_length = int(min), int(max)
        for n in range(min_length, max_length + 1):
            for xs in itertools.product(chrs, repeat=n):
                dsa = fl.write(''.join(xs) + "\n")
