def decrypt_rail_fence(text: str, rails: int):
    rail = [["" for _ in range(len(text))] for _ in range(rails)]
    text_len = len(text)

    row, col = 0, 0
    direction = "down"


    # Mark places to fill with characters
    for char in text:
        if row == 0:
            direction = "down"
        
        if row == rails - 1:
            direction = "up"

        rail[row][col] = "*"

        col += 1
        if direction == "down":
            row += 1
        else:
            row -= 1

    # Fill the marked places
    idx = 0
    for i in range(rails):
        for j in range(text_len):
            if (rail[i][j] == "*") and (idx < text_len):
                rail[i][j] = text[idx]
                idx += 1

    # Read matrix in a zig-zag manner
    decrypted_list = []
    row, col = 0, 0

    for char in text:
        if row == 0:
            direction = "down"
        
        if row == rails - 1:
            direction = "up"

        if rail[row][col] != "*":
            decrypted_list.append(rail[row][col])

        col += 1
        if direction == "down":
            row += 1
        else:
            row -= 1

    return "".join(decrypted_list)


if __name__ == "__main__":
    with open("message.txt") as f:
        msg_txt = f.read()

    decrypted_text = decrypt_rail_fence(text=msg_txt, rails=4).split(":")[1].strip()
    flag = f"picoCTF{{{decrypted_text}}}"
    print(flag)