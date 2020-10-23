import dokter,random,waktu,xlsxwriter,time,penyakit,obat,layanan,tindakan,fakta

nama_file = "DataRumahSakit.xlsx"
workbook    = xlsxwriter.Workbook(nama_file)

# variabel global (primary key setiap dimension)
g_nid           = []
g_id_waktu      = []
g_idc           = []
g_no_penyakit   = []
g_no_obat       = []
g_kd_layanan    = []
g_id_tindakan   = []

def create_worksheet_dokter(x):
    worksheet   = workbook.add_worksheet('Dokter')
    row         = 0
    col         = 0
    header      = ['NID','NAMA_DOKTER','TEMPAT_LAHIR_DOKTER','TANGGAL_LAHIR_DOKTER','JENIS_KELAMIN_DOKTER','ALAMAT_DOKTER','NOMOR_TELEPON_DOKTER']

    # create header
    for data_header in header:
        worksheet.write(row, col, data_header)
        col += 1
    row += 1

    # generate data
    for _ in range(x):
        col             = 0
        tanggal_lahir   = dokter.random_date("1/1/1975", "12/12/1990", random.random())
        nid             = dokter.create_nid(tanggal_lahir)
        nomor_telpon    = dokter.create_nomor_telpon()
        kelamin         = dokter.create_jenis_kelamin()
        alamat          = dokter.create_alamat()
        tempat_lahir    = dokter.create_tempat_lahir()
        nama            = dokter.create_nama(kelamin)
        
        data            = [nid,nama,tempat_lahir,tanggal_lahir,kelamin,alamat,nomor_telpon]
        
        for data_dokter in data:
            worksheet.write(row,col,data_dokter)
            col += 1
        row += 1

        # add ke variabel global
        g_nid.append(nid)
    
    print("Worksheet Dokter Created.")

def create_worksheet_waktu(bulanAwal, tahunAwal, bulanAkhir, tahunAkhir):
    worksheet   = workbook.add_worksheet('Waktu')
    row         = 0
    col         = 0
    bulan       = int(bulanAwal)
    tahun       = int(tahunAwal)
    header      = ['ID_WAKTU','TAHUN','BULAN','TANGGAL']

    # create header
    for data_header in header:
        worksheet.write(row, col, data_header)
        col += 1
    row += 1

    while tahun <= int(tahunAkhir):
        tanggal = waktu.create_date(tahun,bulan)
        id_waktu, Tahun, Bulan, Tanggal = tanggal.split('-')
        col             = 0
        id_waktu        = id_waktu.upper()
        data            = [id_waktu, Tahun, Bulan, Tanggal]

        for data_waktu in data:
            worksheet.write(row,col,data_waktu)
            col += 1
        row += 1

        if tahun == tahunAkhir:
            if bulan > bulanAkhir:
                tahun += 1
            else:
                bulan +=1
        else:
            if bulan == 12:
                bulan   = 1
                tahun  += 1
            else:
                bulan +=1
    
        g_id_waktu.append(id_waktu)

    print("Worksheet Waktu Created")

def create_worksheet_penyakit(n):
    worksheet   = workbook.add_worksheet('Penyakit')
    row         = 0
    col         = 0
    header      = ['NO_PENYAKIT','ICD-X','JENIS_PENYAKIT']

    for x in header:
        worksheet.write(row,col, x)
        col +=1
    row +=1

    while len(g_idc) <= n:
        col = 0
        
        icd_x = penyakit.generate_code()
        if penyakit.find(icd_x):
            data_penyakit = penyakit.create_data_penyakit(icd_x).split("_")

            for data in data_penyakit:
                worksheet.write(row,col,data)
                col+=1
            row+=1

            g_idc.append(data_penyakit[1])
            g_no_penyakit.append(data_penyakit[0])
    
    print("Worksheet Penyakit Created")

def create_worksheet_obat(n):
    worksheet   = workbook.add_worksheet('Obat')
    row         = 0
    col         = 0
    header      = ['NO_OBAT','NAMA_OBAT','STOK_OBAT','SATUAN_OBAT','HARGA_OBAT']

    for i in header:
        worksheet.write(row, col, i)
        col+=1
    row+=1

    obat.create_prefix_and_sufix()

    for _ in range(n):
        col = 0
        nama_obat   = obat.create_nama_obat()
        no_obat     = obat.create_nomor_obat(nama_obat)
        stok_obat   = obat.create_stok_obat()
        satuan_obat = obat.create_satuan_obat()
        harga_obat  = obat.create_harga_obat()
        data        = [no_obat,nama_obat,stok_obat,satuan_obat,harga_obat]

        for data_obat in data:
            worksheet.write(row,col,data_obat)
            col+=1
        row+=1

        g_no_obat.append(no_obat)
    
    print("Worksheet Obat Created")

def create_worksheet_layanan():
    # Butuh Revisi
    worksheet   = workbook.add_worksheet('Pelayanan')
    row         = 0
    col         = 0
    header      = ['KD_LAYANAN', 'JENIS_LAYANAN', 'NAMA_LAYANAN']

    for i in header:
        worksheet.write(row,col,i)
        col+=1
    row+=1

    create_layanan = layanan.create_layanan()
    kd_layanan, jenis_layanan, nama_layanan = create_layanan.split('-')
    data        = [kd_layanan,jenis_layanan,nama_layanan]

    col = 0
    for data_layanan in data:
        worksheet.write(row,col,data_layanan)
        col+=1
    row+=1

    g_kd_layanan.append(kd_layanan)

    print("Worksheet Layanan Created")

def create_worksheet_tindakan():
    worksheet   = workbook.add_worksheet('Tindakan')
    row         = 0
    col         = 0
    header      = ['ID_TINDAKAN', 'NAMA_TINDAKAN', 'BIAYA_TINDAKAN']

    for i in header:
        worksheet.write(row,col,i)
        col+=1
    row+=1

    # range(3) karena cuma ada 3 isi list di class tindakan
    for i in range(3):
        data = tindakan.create_tindakan(i)
        id_tindakan, nama_tindakan, biaya_tindakan = data.split('-')
        data = [id_tindakan, nama_tindakan, int(biaya_tindakan)]
        col = 0

        for data_tindakan in data:
            worksheet.write(row,col,data_tindakan)
            col+=1
        row+=1

        g_id_tindakan.append(id_tindakan)

    print("Worksheet Tindakan Created")

def create_worksheet_fakta_permintaan_obat():
    count       = 0
    worksheet   = workbook.add_worksheet('Fakta Permintaan Obat')
    row         = 0
    col         = 0
    header      = ['NO_OBAT','NO_PENYAKIT','ID_WAKTU','KD_LAYANAN','NID','ID_TINDAKAN',
                    'JUMLAH_PENGGUNAAN','RATA_RATA_PENGGUNAAN','PENGGUNAAN_TERBANYAK','PENGGUNAAN_PALING_SEDIKIT','JUMLAH_OBAT_PENYAKIT','JUMLAH_OBAT_TINDAKAN']
    
    for i in header:
        worksheet.write(row,col,i)
        col+=1
    row+=1

    # obat
    for no_obat in g_no_obat:

        for no_penyakit in g_no_penyakit:
            n_fakta = 0
            data = []
            persentase = 0
            min_penggunaan = 0
            max_penggunaan = 0

            for id_waktu in g_id_waktu:
                col = 0
                nid = random.choice(g_nid)
                kd_layanan = random.choice(g_kd_layanan)
                id_tindakan = random.choice(g_id_tindakan)

                if n_fakta == 0:
                    data = fakta.create_fakta_1()
                else:
                    data = fakta.create_fakta_n(persentase,min_penggunaan, max_penggunaan)
                
                data_main = data[:6]
                persentase = data[6]
                min_penggunaan = data[7]
                max_penggunaan = data[8]

                worksheet.write(row,col,no_obat)
                col+=1
                worksheet.write(row,col,no_penyakit)
                col+=1
                worksheet.write(row,col,id_waktu)
                col+=1
                worksheet.write(row,col,kd_layanan)
                col+=1
                worksheet.write(row,col,nid)
                col+=1
                worksheet.write(row,col,id_tindakan)
                col+=1

                for data_fakta in data_main:
                    worksheet.write(row,col,data_fakta)
                    col+=1

                row+=1
                count+=1
                n_fakta +=1
    
    print('Worksheet Fakta Created : '+str(count))
    
n_dokter        = random.randint(5,15)
n_waktu         = '1-2018-12-2019'
n_penyakit      = random.randint(15,30)
n_obat          = random.randint(10,20)

bulanAwal, tahunAwal, bulanAkhir, tahunAkhir = n_waktu.split('-')

create_worksheet_waktu(bulanAwal,tahunAwal,bulanAkhir,tahunAkhir)
create_worksheet_dokter(n_dokter)
create_worksheet_penyakit(n_penyakit)
create_worksheet_obat(n_obat)
create_worksheet_layanan()
create_worksheet_tindakan()
create_worksheet_fakta_permintaan_obat()
workbook.close()