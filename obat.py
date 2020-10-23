import string
import random

l_prefix    = []
l_sufix     = []
l_satuan    = ['Tablet', 'Botol', 'Ampul', 'Kantong', 'Vial', 'Paket']

def create_prefix_and_sufix():
    for _ in range(random.randint(10,30)):
        prefix  = random.choice(string.ascii_uppercase)
        prefix += random.choice(string.ascii_uppercase)
        if prefix not in l_prefix:
            l_prefix.append(prefix)

    for _ in range(random.randint(5,10)):
        sufix  = random.choice(string.ascii_lowercase)
        sufix += random.choice(string.ascii_lowercase)
        if sufix not in l_sufix:
            l_sufix.append(sufix)

def create_nama_obat():
    prefix  = random.choice(l_prefix)
    mid     = str(random.randint(0,9))
    mid    += str(random.randint(0,9))
    mid    += str(random.randint(0,9))
    sufix   = random.choice(l_sufix)
    return prefix+mid+sufix

def create_nomor_obat(nama_obat):
    result  = 'OB'+nama_obat
    return result

def create_stok_obat():
    result  = random.randint(10,300)
    return result

def create_satuan_obat():
    result  = random.choice(l_satuan)
    return result

def create_harga_obat():
    digit_depan = str(random.randint(1,150))
    digit_tengah= str(random.randint(0,9))
    digit_akhir = '00'
    result      = int(digit_depan+digit_tengah+digit_akhir)
    return result