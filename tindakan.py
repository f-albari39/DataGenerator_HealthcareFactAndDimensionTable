import random

l_id_tindakan     = ["TA100","TA200","TA300"]
l_nama_tindakan   = ["Check Up Luar","Check Up Dalam","Operasi Ringan"]
l_biaya_tindakan  = []

def create_tindakan(x):
    create_harga()
    result  = l_id_tindakan[x]
    result += "-"+l_nama_tindakan[x]+"-"
    result += str(l_biaya_tindakan[x])
    return result

def create_harga():
    nominal = random.randint(5,20)
    for _ in range(len(l_id_tindakan)):
        l_biaya_tindakan.append(nominal*1000)
        persentase = random.randint(150,300)
        nominal = (nominal*persentase)//100