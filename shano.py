from collections import Counter
from math import ceil

msg = 'AAAAAAAAABBBBBBBBCCCCCCDDDDDEEEEFF'
# print(Counter(msg))
count = dict(Counter(msg))
# print(count)

for k, v in count.items():
    print(k,  v)


evals = sorted(list(count.values()), reverse = True)
enc_code={key: None for key in count.keys()}
print(enc_code, end = '\n\n')



# SeperationIndex(evals)


def Bit_encoder(upper_grp, lower_grp):
    for k in upper_grp:
        if enc_code[k] == None:
            enc_code[k] = '0'
        else:
            enc_code[k] +=''.join('0')

    for k in lower_grp:
        if enc_code[k] == None:
            enc_code[k] = '1'
        else:
            enc_code[k] += ''.join('1')

    print(enc_code, end = '\n\n')

upper_grp = {'A':9, 'B':8}
lower_grp = {'C':6, 'D':5, 'E':4, 'F':2}
Bit_encoder(upper_grp, lower_grp)

upper_grp = {'A':9}
lower_grp = {'B':8}
Bit_encoder(upper_grp, lower_grp)

upper_grp = {'C':6, 'D':5}
lower_grp = {'E':4, 'F':2}
Bit_encoder(upper_grp, lower_grp)

upper_grp = {'C':6}
lower_grp = {'D':5}
Bit_encoder(upper_grp, lower_grp)

upper_grp = {'E':4}
lower_grp = {'F':2}
Bit_encoder(upper_grp, lower_grp)
