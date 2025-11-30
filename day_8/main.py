from art import logo

print(logo)

alphabet = [chr(i) for i in range(97, 123)]


def caesar(text, shift, mode):
    result = ""
    if mode == "d":
        shift *= -1

    for ch in text:
        if ch in alphabet:
            pos = alphabet.index(ch)
            new_pos = (pos + shift) % 26
            result += alphabet[new_pos]
        else:
            result += ch

    return result


while True:
    plain_text = input("Type plain text: ").lower()
    c_type = input("Encode or decode? (e/d): ").lower() or "e"

    if c_type not in ("e", "d"):
        print("Should only encode or decode.")
        break

    salt = int(input("Salt: ") or 8)
    result = caesar(plain_text, salt, c_type)

    print(f"Result: {result}")

    again = input("Do you want to go again? (y/n): ").lower()
    if again != "y":
        break
