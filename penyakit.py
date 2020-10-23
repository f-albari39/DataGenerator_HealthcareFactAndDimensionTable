import icd10
from googletrans import Translator
import random
import string

translator  = Translator()

def generate_code():
    prefix  = random.choice(string.ascii_uppercase)
    mid     = str(random.randint(0,9))
    end     = str(random.randint(0,9))
    code    = prefix+mid+end
    return code

def find(code):
    if icd10.exists(code):
        code            = icd10.find(code)
        try:
            jenis_penyakit  = code.block_description
        except:
            return False
        if jenis_penyakit != None:
            return True
    return False

def create_data_penyakit(code):
    code            = icd10.find(code)
    jenis_penyakit  = code.block_description

    jenis_penyakit  = translator.translate(jenis_penyakit, dest='id')
    jenis_penyakit  = jenis_penyakit.text
    
    no_penyakit_pre = str(random.randint(10,99))
    no_penyakit_pas = str(random.randint(10,99))
    no_penyakit     = no_penyakit_pre+str(code)+no_penyakit_pas

    result          = no_penyakit+"_"+str(code)+"_"+jenis_penyakit

    return result

# Testing Purpose
# g_idc = []

# while(len(g_idc) <= 10):

#     icd_x           = generate_code()
#     test            = icd_x in g_idc

#     if test == False:
#         if find(icd_x):
#             detail_penyakit                 = create_data_penyakit(icd_x)
#             icd_x, jenis_penyakit, no_penyakit= detail_penyakit.split('_')
            
#             print(no_penyakit+" - "+icd_x+" - "+jenis_penyakit)
#             g_idc.append(icd_x)