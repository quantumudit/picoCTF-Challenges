import tarfile
import os
import codecs

tarfile_path = "leak.tar"
extract_dir = "userdata"

if not os.path.exists(extract_dir):
    with tarfile.open(tarfile_path, "r") as tar:
        tar.extractall(path=extract_dir)

    print(f"Successfully extracted {tarfile_path} to {extract_dir}")
else:
    # Initialize an empty list to store extracted files
    extracted_files_list = []

    # Walk through the directory and its subdirectories
    for root, _, files in os.walk(extract_dir):
        for file in files:
            file_path = os.path.join(root, file)
            extracted_files_list.append(file_path)
    
    extracted_files = ", ".join(extracted_files_list)

    print(f"The data files avaialbe are: {extracted_files}")

username_data = "./userdata/leak/usernames.txt"
password_data = "./userdata/leak/passwords.txt"

with open(username_data) as f:
    usernames = [text.strip() for text in f.readlines()]

with open(password_data) as f:
    passwords = [text.strip() for text in f.readlines()]

user_dict = {username: password for username, password in zip(usernames, passwords)}

target_user = "cultiris"
target_password = user_dict[target_user]

print(f"\nThe target user's encoded password: {target_password}")

# ROT13 / Ceaser Cipher is used to encode the password and we can decode it as follows:
decoded_password = codecs.decode(target_password, "rot_13")

print(f"The target user's decoded password: {decoded_password}")
