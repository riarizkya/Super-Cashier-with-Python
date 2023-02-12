class User():
    def __init__(self):
      self.nama = str(input('Masukkan nama Anda:'))
      while True:
        try:
          self.nomor_telepon = int(input('Masukkan nomor telepon Anda:'))
          break
        except:
          print('Maaf, informasi yang Anda masukkan salah. Silakan mengisi kembali informasi dengan angka.')
      self.alamat = str(input('Masukkan alamat Anda untuk pengiriman '))

    def user_ID(self):
      import string
      karakter_valid = string.ascii_letters + string.digits + '_.'
      while True:
        user_id = str(input('Buatlah user ID sebelum melakukan transaksi:'))
        if all(char in karakter_valid for char in user_id):
            print(user_id)
            break
        else:
          print("User ID tidak boleh mengandung karakter selain underscore (_) dan titik (.). Silakan coba lagi.")
      return str(f'Selamat datang {self.nama}, user ID Anda adalah {user_id}! Selamat berbelanja.')

class Transactions():
  def __init__(self):
    self.buat_transaksi = {}

  def tambah_barang(self, nama_barang, jumlah_barang, harga_barang):
      try:
        nama_barang = str(nama_barang)
        if nama_barang != str(nama_barang):
          print('Maaf, nama barang tidak valid.')
          return
      except TypeError:
        print('Maaf, informasi yang dimasukkan salah, silakan coba kembali.')
        return

      try:
        jumlah_barang = int(jumlah_barang)
        if jumlah_barang <= 0:
          print('Maaf, jumlah barang tidak boleh kurang dari 1.')
          return
      except ValueError:
        print('Maaf, informasi yang dimasukkan salah, silakan coba kembali.')
        return
  
      try:
        harga_barang = int(harga_barang)
        if harga_barang <= 0:
          print('Maaf, harga barang tidak boleh sama dengan Rp0,-.')
          return
      except ValueError:
        print('Maaf, informasi yang dimasukkan salah, silakan coba kembali.')
        return
      
      self.buat_transaksi[nama_barang] = (jumlah_barang, harga_barang)
      print(f'Barang Anda: "{nama_barang}", berjumlah: "{jumlah_barang}", seharga satuan: "{harga_barang}" berhasil ditambahkan.')

  def update_nama_barang(self, nama_barang, nama_barang_baru):
    if nama_barang in self.buat_transaksi:
      self.buat_transaksi[nama_barang_baru] = self.buat_transaksi.pop(nama_barang)
      print(f'Anda mengganti {nama_barang} dengan {nama_barang_baru}.')
      self.tabel_barang = []
      from tabulate import tabulate
      for nama_barang, (jumlah_barang, harga_barang) in self.buat_transaksi.items():
        self.tabel_barang.append([nama_barang, jumlah_barang, harga_barang])
        print(f'Daftar belanja Anda saat ini adalah:\n {tabulate(self.tabel_barang, headers=["Nama Barang","Jumlah Barang", "Harga Barang"])}')  
    else:
      print('Nama barang tidak ditemukan.')

  def update_jumlah_barang(self, nama_barang, jumlah_barang_baru):
    if nama_barang in self.buat_transaksi:
        self.buat_transaksi[nama_barang] = (jumlah_barang_baru, self.buat_transaksi[nama_barang][1])
        print(f'Anda mengganti jumlah {nama_barang} menjadi {jumlah_barang_baru}.')
        self.tabel_barang = []
        from tabulate import tabulate
        for nama_barang, (jumlah_barang, harga_barang) in self.buat_transaksi.items():
          self.tabel_barang.append([nama_barang, jumlah_barang, harga_barang])
          print(f'Daftar belanja Anda saat ini adalah:\n {tabulate(self.tabel_barang, headers=["Nama Barang","Jumlah Barang", "Harga Barang"])}')
    else:
      print('Jumlah barang tidak ditemukan.')

  def update_harga_barang(self, nama_barang, harga_barang_baru):
    if nama_barang in self.buat_transaksi:
        self.buat_transaksi[nama_barang] = (self.buat_transaksi[nama_barang][0], harga_barang_baru)
        print(f'Anda mengganti harga {nama_barang} menjadi {harga_barang_baru}.')
        self.tabel_barang = []
        from tabulate import tabulate
        for nama_barang, (jumlah_barang, harga_barang) in self.buat_transaksi.items():
          self.tabel_barang.append([nama_barang, jumlah_barang, harga_barang])
          print(f'Daftar belanja Anda saat ini adalah:\n {tabulate(self.tabel_barang, headers=["Nama Barang","Jumlah Barang", "Harga Barang"])}')
    else:
      print('Harga barang tidak ditemukan.')

  def hapus_barang(self, nama_barang):
    if nama_barang in self.buat_transaksi:
      self.buat_transaksi.pop(nama_barang)
      print(f'Anda menghapus {nama_barang} dari daftar belanja.')
      self.tabel_barang = []
      from tabulate import tabulate
      for nama_barang, (jumlah_barang, harga_barang) in self.buat_transaksi.items():
        self.tabel_barang.append([nama_barang, jumlah_barang, harga_barang])
      print(f'Daftar belanja Anda saat ini adalah:\n {tabulate(self.tabel_barang, headers=["Nama Barang","Jumlah Barang", "Harga Barang"])}')
    else:
      print('Nama barang yang ingin dihapus tidak ditemukan.')

  def reset_transaksi(self):
    self.buat_transaksi.clear()
    print(f'Anda menghapus semua barang dari dari daftar belanja.')
    self.tabel_barang = []
    from tabulate import tabulate
    print(f'Daftar belanja Anda saat ini adalah:\n {tabulate(self.tabel_barang, headers=["Nama Barang","Jumlah Barang", "Harga Barang"])}')
    
  def cek_pesanan(self):
    print('Silakan mengecek pesanan yang telah Anda buat: apakah pesanan sudah benar? (yes/no): ')
    cek_jawaban = input().strip()
    if cek_jawaban == 'yes':
        print('Pesanan Anda sudah benar, tidak ada perubahan.')
    elif cek_jawaban == 'no':
        print('Sepertinya Anda menemukan kesalahan pada pesanan. Silakan melakukan update pesanan sesuai keinginan Anda atau menghapus pesanan bila diperlukan:')
        print('Update pesanan?:(input "update")')
        pilihan = input('').strip()
        if pilihan == 'update':
            perubahan = input('Silakan pilih bagian yang diinginkan: (nama/ jumlah/ harga)').strip()
            if perubahan == 'nama':
                nama_barang_lama, nama_barang_baru = input('Isilah perubahan dengan format (nama barang lama, nama barang baru):').split(',')
                self.update_nama_barang(nama_barang_lama, nama_barang_baru)
        elif perubahan == 'jumlah':
          nama_barang = input('Masukkan nama barang yang ingin Anda ubah jumlahnya:')
          jumlah_barang_baru = int(input('Masukkan jumlah barang yang baru:'))
          self.update_jumlah_barang(nama_barang, jumlah_barang_baru)
        elif perubahan == 'harga':
          nama_barang = input('Masukkan nama barang yang ingin Anda ubah harganya:')
          harga_barang_baru = int(input('Masukkan harga barang yang baru:'))
          self.update_harga_barang(nama_barang, harga_barang_baru)
    for nama_barang, (jumlah_barang, harga_barang) in self.buat_transaksi.items():
      self.tabel_barang = []
      from tabulate import tabulate
      self.tabel_barang.append([nama_barang, jumlah_barang, harga_barang])
      print(f'Daftar belanja Anda saat ini adalah: \n {tabulate(self.tabel_barang, headers =["Nama Barang", "Jumlah Barang", "Harga Barang"])}')

  def menampilkan_daftar_barang(self):
    self.tabel_barang = []
    from tabulate import tabulate
    total_harga = 0
    for nama_barang, (jumlah_barang, harga_barang) in self.buat_transaksi.items():
        subtotal = jumlah_barang * harga_barang
        total_harga += subtotal
        self.tabel_barang.append([nama_barang, jumlah_barang, harga_barang, subtotal])

    diskon = 0
    if total_harga >= 200000:
      diskon = 0.05
      diskon_dalam_rupiah = total_harga * diskon
    if total_harga >= 300000:
      diskon = 0.08
      diskon_dalam_rupiah = total_harga * diskon
    if total_harga >= 500000:
      diskon = 0.1
      diskon_dalam_rupiah = total_harga * diskon
    harga_dibayar = total_harga - (total_harga * diskon)
    
    self.tabel_barang.append(["Total Harga", "", "", total_harga])
    self.tabel_barang.append(["Diskon", "", "", diskon_dalam_rupiah])
    self.tabel_barang.append(["Harga yang Harus Dibayar", "", "", harga_dibayar])
    print(f'Daftar belanja Anda saat ini adalah:\n {tabulate(self.tabel_barang, headers=["Nama Barang","Jumlah Barang", "Harga Barang", "Harga Barang Sesuai Jumlah"])}')
    
