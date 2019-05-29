aa_sequence = 'KCAHTVSKSMSMSVGERVTLTCKASENVVTYVSWYQQKPEQSPKLLIYGASNRYTGVPDRFTGSGSATDFTLTISSVQAEDLADYHCGQGYSYPYTFGGGTKLEIKRADAAPTVSIFPPSSEQLTSGGASVVCFLNNFYPKDINVKWKIDGSERQNGVLNSWTDQDSKDSTYSMSSTLTLTKDEYERHNSYTCEATHKTSTSPIVKSFNRNEC'

def cd1(aa_quence):
    
def cd2(aa_sequence):
    return(aa_sequence[49:55])

class is_CDR_L1:
    def __init__(self, sequence):
        self.sequence= sequence
    def start_position(self):
        start_pos = 24-1
        return start_pos

    def end_position(self):
        for i in range(23+10, 23+17):
            if(self[i] == 'W' ):
                last_position = i
                return(last_position)
    def return_CDR_L1(self):

        last_postion = is_CDR_L1.end_position(self)
        seq_start = is_CDR_L1.start_position(self)
        CDR_L1 = self[seq_start:last_postion]
        return CDR_L1



class is_CDR_L2:
    def __init__(self, sequence):
        self.sequence= sequence
    def start_position(self):
        start_pos = is_CDR_L1.end_position(self)+17
        return start_pos
    def end_position(self):
        end_pos = is_CDR_L2.start_position(self) + 7
        return end_pos
    def return_CDR_L2(self):
        CDR_L2 = self[is_CDR_L2.start_position(self):is_CDR_L2.end_position(self)]
        return CDR_L2


class is_CDR_L3:
    def __init__(self, sequence):
        self.sequence= sequence
    def start_position(self):
        return is_CDR_L2.end_position(self)+33
    def end_position(self):
        for i in range(int(is_CDR_L3.start_position(self))+7, int(is_CDR_L3.start_position(self))+11):
            if ( self[i-1]=='G' and self[i-2] =='F'):
                end_pos = i
                return end_pos
    def return_CDR_L3(self):
        return self[is_CDR_L3.start_position(self):is_CDR_L2.end_position(self)]

print(is_CDR_L2.return_CDR_L2(aa_sequence))
print(cd2(aa_sequence))







