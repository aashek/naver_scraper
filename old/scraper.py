import regex

lines = open('lolo', encoding='utf8').read().splitlines()
n = len(lines)

f = open("bobby.tsv", 'wb', encoding='utf8')

ans = ['' for i in range(11)]


ans[0] = "잡히지"
write_index = 1

i = 1
while i < n - 1:
    if regex.search(r'\p{IsHangul}', lines[i]) and not regex.search(r'\p{IsHangul}', lines[i+1]):
        if write_index > 10: break
        ans[write_index] = lines[i]
        ans[write_index+1] = '\"' + lines[i+1] + '\"'
        write_index += 2
    i += 1

f.write(",".join(ans))
f.close()
