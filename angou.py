import re

target_char = input()
pattern = r'((.)(\d+))'
results = re.findall(pattern, target_char)
char_list = [chr((ord(result[1]) - 97 + (int(result[2]) if int(result[2])%2==0 else int(result[2])*(-1)))%26 + 97) for result in results]
result_chr = "".join(char_list)

print(result_chr)