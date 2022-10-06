from collections import Counter



a='RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE. AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE.'

b=Counter(a)



del b [',']
del b ['.']
del b [' ']
del b ['0']
del b ['1']
del b ['2']
del b ['3']
del b ['4']
del b ['5']
del b ['6']
del b ['7']
del b ['8']
del b ['9']
print(b)
c=list(b.items())
d=sorted(c,key=lambda letra:letra[1],reverse=True)


letrak=['e','a','r','o','i','n','l','d','c','u','t','s','m','p','b','f','q','j','y','v','g','h','x','z','k','ñ','w']



for x in range(0,len(d)):
    a=a.replace(d[x][0],letrak[x])

#beste modu bat
'''char_to_replace = {d[0][0]: 'E',
                   d[1][0]: 'A',
                   d[2][0]: 'R',
                   d[3][0]: 'O',
                   d[4][0]: 'I',
                   d[5][0]: 'N',
                   d[6][0]: 'L',
                   d[7][0]: 'D',
                   d[8][0]: 'C',
                   d[9][0]: 'U',
                   d[10][0]: 'T',
                   d[11][0]: 'S',
                   d[12][0]: 'M',
                   d[13][0]: 'P',
                   d[14][0]: 'B',
                   d[15][0]: 'F',
                   d[16][0]: 'Y',
                   d[17][0]: 'Q',
                   d[18][0]: 'J',
                   d[19][0]: 'G',
                   d[20][0]: 'H',
                   d[21][0]: 'X',
                   d[22][0]: 'Z',
                   #d[23][0]: '',
                   #d[24][0]: '',
                   #d[25][0]: '',
                   #d[26][0]: ''
                   }

a = a.translate(str.maketrans(char_to_replace)) 

'''



print(a)


