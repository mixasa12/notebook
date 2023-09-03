import configMod as cm
from configMod import set_public_key
from configMod import get_public_key
import encryption as en
from encryption import cipher
import error
from error import er_of_key
path="main.ini"
def codeText(s,m_k):
    PK=cm.get_public_key(path)
    text_mess="[main]keyopen="+str(PK)+'\n'
    text_mess+=en.cipher(s,int(m_k))
    return text_mess

def uncodeText(s,m_k):
    index = s.find('[main]keyopen=')
    if index!=0:
        error.er_of_key()
        return ''
    index = s.find('\n')
    if index==(-1):
        error.er_of_key()
        return ''
    PK=s[14:index]
    if PK.isnumeric()==False:
        error.er_of_key()
        return ''
    PK=int(PK)
    stri=s[s.find('\n')+1:len(s)]
    ss = ""
    SK=int(PK/m_k)
    return en.cipher(stri,SK)
