import os

### >> github.com/Akbaroke << ##

## BUG 1 (Jika Salah memasukan Nomor dan Mencoba memasukan no baru, Maka Program selalu memberikan ERROR karena pada awal input nomor Salah ( jadi agar program berjalan lagi harus kita restart ulang / jalankan ulang) )
## BUG 2 (Belum adanya Error handling pada Tf pulsa apa bila Pulsa tidak cukup)

def profil(username,sandi,no_tlp,umur,pulsa):
    os.system('cls')
    s = len(sandi)-2
    sensor = '*'*s
    print('Selamat Datang Di menu Profil \n')
    print('Username\t:', username)
    print('Sandi\t\t:', sandi[0:2]+sensor)
    print('No.Tlpn\t\t:', no_tlp)
    print('Umur\t\t:', umur)
    print('Pulsa\t\t: Rp', pulsa)

    # Menu Transaksi
    print('\n>> Menu Transaksi <<')
    print('1. Isi Pulsa\n2. Transfer Pulsa\n3. Keluar\n')
    tr = input('Masukan Kode Transaksi di atas : ')
    if tr == '1':
        # pass #isipulsa()
        os.system('cls')
        print('>> Menu Isi Pulsa <<\n')
        isipulsa = input('Jumlah Pulsa : Rp ')
        with open('database.txt', 'r') as f:
            lines = f.readlines()
        with open('database.txt', 'w') as f:
            for line in lines:
                if line.strip('') != username+','+sandi+','+no_tlp+','+umur+','+pulsa:
                    f.write(line)
            f.close()
        pulsa = int(pulsa) + int(isipulsa)
        file_akun = open('database.txt', 'a')
        write = username+','+sandi+','+no_tlp+','+umur+','+str(pulsa)
        write_newline = '\n'
        file_akun.write(write_newline)
        file_akun.write(write)
        file_akun.close()

        os.system('cls')
        print('\n>> PULSA BERHASIL TERISI (TRANSAKSI SUKSES !!!) <<')
        input('\nPress ENTER untuk kembali ke Menu Profil ... ')
        profil(username,sandi,no_tlp,umur,pulsa)

    elif tr == '2':
        os.system('cls')
        print('>> Menu Transfer Pulsa <<\n')
        no_tujuan = input('No.tlpn Tujuan\t: ')
        tfpulsa = input('Jumlah Pulsa\t: Rp ')
        file_p = open('database.txt', 'r')
        for p in file_p:
            list_p = []
            a = p.split(',')
            list_p.extend(a)
            no_p = list_p[2]
            if no_tujuan == no_p:
                with open('database.txt', 'r') as f:
                    lines = f.readlines()
                with open('database.txt', 'w') as f:
                    for line in lines:
                        if line.strip('') != username+','+sandi+','+no_tlp+','+umur+','+pulsa:
                            f.write(line)
                    f.close()
                pulsa = int(pulsa) - int(tfpulsa)
                file_akun = open('database.txt', 'a')
                write = username+','+sandi+','+no_tlp+','+umur+','+str(pulsa)
                write_newline = '\n'
                file_akun.write(write_newline)
                file_akun.write(write)
                file_akun.close()
                file_p.close()
                del list_p[0:]
                # tf_tujuan(no_tujuan,tfpulsa)
                file = open('database.txt', 'r')
                for i in file:
                    list = []
                    a = i.split(',')
                    list.extend(a)
                    username_tujuan = list[0]
                    sandi_tujuan = list[1]
                    no_tlp_tujuan = list[2]
                    umur_tujuan = list[3]
                    pulsa_tujuan = list[4]
                    if no_tujuan == no_tlp_tujuan:
                        with open('database.txt', 'r') as f:
                            lines = f.readlines()
                        with open('database.txt', 'w') as f:
                            for line in lines:
                                if line.strip('') != username_tujuan+','+sandi_tujuan+','+no_tlp_tujuan+','+umur_tujuan+','+pulsa_tujuan:
                                    f.write(line)
                            f.close()
                        pulsa_tujuan = int(pulsa_tujuan) + int(tfpulsa)
                        file_akun = open('database.txt', 'a')
                        write = username_tujuan+','+sandi_tujuan+','+no_tlp_tujuan+','+umur_tujuan+','+str(pulsa_tujuan)
                        write_newline = '\n'
                        file_akun.write(write_newline)
                        file_akun.write(write)
                        file_akun.close()
                        print('\n>> Transfer BERHASIL (TRANSAKSI SUKSES !!!) <<')
                        input('\nPress ENTER untuk kembali ke Menu Profil ... ')
                        profil(username,sandi,no_tlp,umur,pulsa)
                    del list[0:]
            else:
                print('\n>> Transfer GAGAL !!! (No Tujuan TIDAK terdaftar) <<')
                input('\nPress ENTER untuk Kembali Ke menu Transaksi ...')
                profil(username,sandi,no_tlp,umur,pulsa)

    elif tr == '3':
        os.system('cls')
        def err():
            os.system('cls')
            print('(Kata yang anda Ketik Salah !!!)\n')
            print('Selamat datang Di Program By.Bot')
            head = input('\nMasuk / Daftar ? ')
            if head.lower() in 'daftar':
                daftar()
            elif head.lower() in 'masuk':
                masuk()
            else:
                err()
        
        def menuCover():
            print('Selamat datang Di Program By.Bot')
            head = input('\nMasuk / Daftar ? ')
            if head.lower() in 'daftar':
                daftar()
            elif head.lower() in 'masuk':
                masuk()
            else:
                err()
        menuCover()

    else:
        print('\n(Kode Transaksi SALAH !!!)')
        input('Press ENTER untuk Mengulang ...')
        profil(username,sandi,no_tlp,umur,pulsa)


def daftar():
    os.system('cls')
    dataUser = []
    print('Selamat datang Di Menu Daftar\n')
    username = input('Username\t: ')
    sandi = input('Sandi\t\t: ')
    no_tlp = input('No.Tlpn\t\t: ')
    umur = input('Umur\t\t: ')
    pulsa = '0'
    input('\tTekan ENTER Untuk Melanjutkan ... ')

    dataUser.append(username)
    dataUser.append(sandi)
    dataUser.append(no_tlp)
    dataUser.append(umur)
    dataUser.append(pulsa)

    file = open('database.txt', 'r')
    y = len(file.readlines())
    if y < 1: # jika file kosong
        file_akun = open('database.txt', 'a')
        write = dataUser[0]+','+dataUser[1]+','+dataUser[2]+','+dataUser[3]+','+dataUser[4]
        write_newline = ''
        file_akun.write(write_newline)
        file_akun.write(write)
        file_akun.close()
        file.close()
        del dataUser[0:]

    elif y > 0: # jika file sudah terisi
        file_akun = open('database.txt', 'a')
        write = dataUser[0]+','+dataUser[1]+','+dataUser[2]+','+dataUser[3]+','+dataUser[4]
        write_newline = '\n'
        file_akun.write(write_newline)
        file_akun.write(write)
        file_akun.close()
        file.close()
        del dataUser[0:]
    
    s = len(sandi)-3
    sensor = '*'*s
    print('Selamat !!! Data Anda Berhasil Tersimpan...\n')
    print('Username\t:', username)
    print('Sandi\t\t:', sandi[0:3]+sensor)
    print('No.Tlpn\t\t:', no_tlp)
    print('Umur\t\t:', umur)
    print('Pulsa\t\t: Rp', pulsa)
        
    input('\nTekan ENTER untuk Melanjutkan Ke Menu Profil ...')
    profil(username,sandi,no_tlp,umur,pulsa)


def masuk():
    def err():
        os.system('cls')
        print('Username dan Sandi TIDAK TERDAFTAR !!!')

        def error():
            os.system('cls')
            print('(Kata yang anda Ketik Salah !!!)\n')
            head = input('\nMasuk / Daftar ? ')
            if head.lower() in 'daftar':
                daftar()
            elif head.lower() in 'masuk':
                masuk()
            else:
                error()

        def menuCover():
            head = input('\nMasuk / Daftar ? ')
            if head.lower() in 'daftar':
                daftar()
            elif head.lower() in 'masuk':
                masuk()
            else:
                error()
        menuCover()

    def menumasuk():
        os.system('cls')
        print('Selamat datang Di Menu Masuk\n')
        username1 = input('Username\t: ')
        sandi1 = input('Sandi\t\t: ')
        file = open('database.txt', 'r')
        for i in file:
            list = []
            a = i.split(',')
            list.extend(a)
            username = list[0]
            sandi = list[1]
            no_tlp = list[2]
            umur = list[3]
            pulsa = list[4]
            if username1 == username and sandi1 == sandi:
                profil(username,sandi,no_tlp,umur,pulsa)
                break
            del list[0:]
        else:
            err()
    menumasuk()

# Cover
def cover():
    os.system('cls')
    def err():
        os.system('cls')
        print('(Kata yang anda Ketik Salah !!!)\n')
        print('Selamat datang Di Program By.Bot')
        head = input('\nMasuk / Daftar ? ')
        if head.lower() in 'daftar':
            daftar()
        elif head.lower() in 'masuk':
            masuk()
        else:
            err()
    
    def menuCover():
        print('Selamat datang Di Program TRANSAKSI PULSA')
        head = input('\nMasuk / Daftar ? ')
        if head.lower() in 'daftar':
            daftar()
        elif head.lower() in 'masuk':
            masuk()
        else:
            err()
    
    menuCover()

cover()