matrix_srt = '''7i3
Tsi
h%x
i #
sM 
$a 
#t%
^r!'''

list_matrix = matrix_srt.split('\n')
final_srt = ''

if len(list_matrix) > 0:
    for col in range(0, len(list_matrix[0])):
        for row in list_matrix:
            if row[col].isalpha():
                final_srt += row[col]
            else:
                if len(final_srt) > 0 and final_srt[-1] != ' ':
                    final_srt += ' '

print(final_srt)
