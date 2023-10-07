import string

with open("message.txt", "r") as f:
    text_msg = f.read()

nums_list = list(map(lambda x: int(x), text_msg.split()))

mod37_list = list(map(lambda x: x%37, nums_list))
print(mod37_list)

alpha_list = list(string.ascii_uppercase)
int_list = list(range(0,10))
char_set = alpha_list + int_list + ['_']
print(char_set)

decrypted_msg = "".join([str(char_set[idx]) for idx in mod37_list])
print(decrypted_msg)
    
decrypted_flag = f"picoCTF{{{decrypted_msg}}}"
print(decrypted_flag)