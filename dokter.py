import random
import time

def create_nid(tanggal_lahir):
    awalan          = str(random.randint(10,45))
    tanggal_lahir   = format_tanggal(tanggal_lahir)
    akhiran         = '0'+str(random.randint(0,9))
    return awalan+tanggal_lahir+akhiran

def create_nama(kelamin):
    nama_laki_awalan        = ['Rizki ','Ahmad ','Tri ','Catur ','Rafles ','Muhammad ','Putra ','Made ','Dwi ','','Putu ','','']
    nama_laki_tengah        = ['Mamat','Salman','Albert','Antony','Andri','Junet','Panjul','Saepudin','Kevin','Alvin','Hendra','Bagus','Agus','Eko','Rozan']
    nama_laki_akhiran       = [' Ali','','','','',' Wiguna',' Liusdy',' Setiawan','',' Budiman',' Oktavianus','',' Suardi',' Nurcahyo']
    nama_perempuan_awalan   = ['Putri ','Cinta ','Sarah ','Lina ','Nada ','','','','','','Cintia ','Monika ','Zara ','Wardah ']
    nama_perempuan_tengah   = ['Dwi','Roman','Reyna','Joana','Sesilia','Andra','Hana','Ulfa','Ema','Renata','Farah','Minah']
    nama_perempuan_akhiran  = [' Lestari','','',' Ayu',' Fitriani',' Puan',' Lami','','','',' Maharani',' Natasya',' Susanti']
    if kelamin == 'Laki-laki':
        awalan  = random.choice(nama_laki_awalan)
        tengah  = random.choice(nama_laki_tengah)
        akhiran = random.choice(nama_laki_akhiran)
    else:
        awalan  = random.choice(nama_perempuan_awalan)
        tengah  = random.choice(nama_perempuan_tengah)
        akhiran = random.choice(nama_perempuan_akhiran)
    return awalan+tengah+akhiran

def create_nomor_telpon():
    nomor = "08"
    for _ in range (10):
        nomor += str(random.randint(0,9))
    return nomor

def create_tempat_lahir():
    kota = ['Jakarta Pusat','Jakarta Barat','Jakarta Timur','Jakarta Selatan','Jakarta Utara',
    'Tangerang','Tangerang Selatan','Kabupaten Tangerang','Depok','Bogor','Bekasi']
    return random.choice(kota)

def create_alamat():
    awalan  = ['Jl.','Perum. ']
    tengah  = ['Mangga','Pisang','Kiwi','Sirsak','Jambu','Pepaya','Kedondong','Anggrek','Mawar','Melati','Tulip','Manggis','Buaya','Lele','Ayam','Bebek','Sapi']
    akhiran = [' 1',' 2',' 3',' 4',' 5']
    
    awalan  = random.choice(awalan)
    tengah  = random.choice(tengah)
    akhiran = random.choice(akhiran)
    return awalan+tengah+akhiran

def create_jenis_kelamin():
    jenis_kelamin = ['Laki-laki','Perempuan']
    return random.choice(jenis_kelamin)

def format_tanggal(tanggal):
    bulan, hari, tahun  = tanggal.split('/')
    return bulan+hari+tahun[2:]

def str_time_prop(start, end, format, prop):
    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))

def random_date(start, end, prop):
    return str_time_prop(start, end, '%m/%d/%Y', prop)

nama_depan    = ['fakhri','michael','kevin','kevin','imanuel','muhammad','rizki','rizqi','ryan','hazel','rozan','wahyu']
nama_tengah   = [' ',' deo ',' ',' dwitama ',' alvin ',' mahdy ',' maulana ',' eko ',' ',' ',' naufal ',' aji ']
nama_belakang = ['albari','barli','saputra','putra','santosa','satria','akbar','parwanto','widjayana','israeli','zafran','pambudi']

g_nama = []

while len(g_nama) <= 10:

    depan   = random.choice(nama_depan)
    tengah  = random.choice(nama_tengah)
    belakang= random.choice(nama_belakang)

    nama    = depan+tengah+belakang

    if nama not in g_nama:
        print(nama.upper())
        g_nama.append(nama)