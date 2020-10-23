import random

l_penggunaan = []

def create_fakta_1():
    l_penggunaan.clear()
    min_penggunaan  = random.randint(0,15)
    max_penggunaan  = random.randint(60,150)

    for _ in range(30):
        l_penggunaan.append(random.randint(min_penggunaan,max_penggunaan))

    jumlah_penggunaan   = sum(l_penggunaan)
    rata_penggunaan     = jumlah_penggunaan//len(l_penggunaan)
    penggunaan_terbanyak= max(l_penggunaan)
    penggunaan_tersedikit= min(l_penggunaan)

    persentase      = random.randint(0,1000)//10
    obat_penyakit   = (persentase*jumlah_penggunaan)//1000
    obat_tindakan   = jumlah_penggunaan - obat_penyakit
    result          = [jumlah_penggunaan,rata_penggunaan,penggunaan_terbanyak,penggunaan_tersedikit,obat_penyakit,obat_tindakan,persentase,min_penggunaan,max_penggunaan]
    return result

def create_fakta_n(persentase, min_penggunaan, max_penggunaan):
    l_penggunaan.clear()
    if min_penggunaan == 0:
        min_penggunaan = random.randint(0,11)
    else:
        while True:
            default = min_penggunaan
            min_penggunaan += random.randint(-7,11)
            if min_penggunaan >= 0:
                break
            else:
                min_penggunaan = default
    
    if max_penggunaan == min_penggunaan:
        max_penggunaan = random.randint(11,29)
    else:
        while True:
            default = max_penggunaan
            max_penggunaan += random.randint(-11,29)
            if max_penggunaan > min_penggunaan:
                break
            else:
                max_penggunaan = default

    for _ in range(30):
        l_penggunaan.append(random.randint(min_penggunaan,max_penggunaan))

    jumlah_penggunaan   = sum(l_penggunaan)
    rata_penggunaan     = jumlah_penggunaan//len(l_penggunaan)
    penggunaan_terbanyak= max(l_penggunaan)
    penggunaan_tersedikit= min(l_penggunaan)

    persentase  = random.randint(0,1000)//10

    if persentase == 0:
        persentase = random.randint(0,100)
    elif persentase == 1000:
        persentase = random.randint(900,1000)
    else:
        while True:
            default = persentase
            persentase += random.randint(-700,700)
            if persentase <= 1000 and persentase >= 0:
                break
            else:
                persentase = default

    obat_penyakit   = (persentase*jumlah_penggunaan)//1000
    obat_tindakan   = jumlah_penggunaan - obat_penyakit
    result      = [jumlah_penggunaan,rata_penggunaan,penggunaan_terbanyak,penggunaan_tersedikit,obat_penyakit,obat_tindakan,persentase,min_penggunaan,max_penggunaan]

    return result

p = [1,2,3]
