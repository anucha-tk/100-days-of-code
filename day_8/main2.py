from art import logo

print(logo)

while True:
    plain_text = input("Type plain text: ").lower()
    c_type = input("What e or d: ").lower()
    if c_type not in ["e", "d"]:
        print("Should only encode or decode type")
        break
    salt = int(input("Salt: "))

    result_text = ""
    for idx, w in enumerate(plain_text):
        if c_type == "e":
            encode_code = ord(w) + salt
            if encode_code > 122:
                encode_code = (encode_code - 122) + 97
            chipher_text = chr(encode_code)
            result_text += chipher_text
        else:
            decode_code = ord(w) - salt
            print(w, "decode_code", decode_code)
            if decode_code < 97:
                decode_code = 123 - (97 - decode_code)
            chipher_text = chr(decode_code)
            result_text += chipher_text

    print(f"encode: {result_text}")
    break
