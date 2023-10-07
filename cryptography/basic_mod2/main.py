import string

with open("message.txt", "r") as f:
    msg_text = f.read()

nums_list =  list(map(lambda x: int(x), msg_text.split()))

# finding modular inverse of each number
modinv41_list = list(map(lambda x: pow(x, -1, 41), nums_list))

alpha_list = list(string.ascii_uppercase)
digits_list = list(range(0, 10))
char_set = alpha_list + digits_list + ["_"]

decrypted_list = [str(char_set[idx-1]) for idx in modinv41_list]
decrypted_msg = "".join(decrypted_list)

decrypted_flag = f"picoCTF{{{decrypted_msg}}}"
print(decrypted_flag)
