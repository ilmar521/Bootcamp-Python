matrix_srt = '''7i3
Tsi
h%x
i #
sM 
$a 
#t%
^r!'''

list_matrix = matrix_srt.split('\n')
final_list = []

if len(list_matrix) > 0:
    for col in range(0, len(list_matrix[0])):
        for row in list_matrix:
            if row[col].isalpha():
                final_list.append(row[col])
            else:
                if len(final_list) > 0 and final_list[-1] != ' ' and row != list_matrix[0]:
                    final_list.append(' ')

print(''.join(final_list))
