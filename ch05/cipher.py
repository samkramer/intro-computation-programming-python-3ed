# 5.8 Dictionary Comprehension

def read_book(filename):
    with open(filename, encoding="utf8") as file:
        contents = file.read().rsplit()
    return " ".join(contents)

def test_gen_code_keys(plain_text):
    gen_code_keys = (lambda book,
                     plain_text:({c: str(book.find(c)) for c in plain_text}))
    print(gen_code_keys(book, plain_text))
    
def gen_code_keys(book, plain_text):
    return {c: str(book.find(c)) for c in plain_text}

def test_encrypt(code_keys, plain_text):
    encoder = (lambda code_keys, plain_text:
               ''.join(['*' + code_keys[c] for c in plain_text])[1:])
    encrypted_text = encoder(code_keys, plain_text)
    print(f"encrypted_text: {encrypted_text}")
    
def encrypt(code_keys, plain_text):
    return ''.join(['*' + code_keys[c] for c in plain_text])[1:]


def test_decrypt(book, cipher_text):
    gen_decode_keys = (lambda book, cipher_text:
                       {s: book[int(s)] for s in cipher_text.split('*')})
    decode_keys = gen_decode_keys(book, cipher_text)
    print(f"decode_keys: {decode_keys}")

def decrypt(book, cipher_text):
    return {s: book[int(s)] for s in cipher_text.split('*')}

def decode_message(cipher_text, decode_keys):
    cipher_keys = cipher_text.split('*')
    message = ''
    for ck in cipher_keys:
        message += decode_keys[ck]
    return message

if __name__ == "__main__":    
    filename = 'donquixote_short.txt'
    book = read_book(filename)
    # print(book)
               
    plain_text = "no is no"
    # test_gen_code_keys(plain_text)
    code_keys = gen_code_keys(book, plain_text)
    print(f"code_keys: {code_keys}")
    
    print()
    
    # test_encrypt(code_keys, plain_text)
    cipher_text = encrypt(code_keys, plain_text)
    print(f"cipher_text: {cipher_text}")
    
    print()
    
    # test_decrypt(book, cipher_text)
    decode_keys = decrypt(book, cipher_text)
    print(f"decode_keys: {decode_keys}")
    
    message = decode_message(cipher_text, decode_keys)
    print(f"message: {message}")
    
    print()
    
    # Finger exercise: decrypt the following message:
    exercise_cipher_text = ('22*13*33*137*59*11*23*11*1*57*6*13*1*2*6*57*2*6' +
        '*1*22*13*33*137*59*11*23*11*1*57*6*173*7*11')
    exercise_decode_keys = decrypt(book, exercise_cipher_text)
    exercise_message = decode_message(exercise_cipher_text, exercise_decode_keys)
    print(f"exercise_message: {exercise_message}")
