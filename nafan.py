from time import sleep
nama = "Nafan Nur Alim"
kelas = "XI PPLG 1"
sekolah = "SMKN 8 Semarang"
NIS = "10066"
alamat = "Jl. Tumpang 1 no. 104"
agama = "Islam"
tanggal = "Semarang, 31 Oktober 2005"
umur = "17 Tahun"
print("Wait a second\n")
sleep(1)
print("\n---------------------------------------------------\n")
sleep(1)
print("||||||[LOADING]||||||")
sleep(2)
print("[1/10  #---------][ 10%]")
sleep(0.7)
print("[2/10  ##--------][ 20%]")
sleep(0.5)
print("[3/10  ###-------][ 30%]")
sleep(0.2)
print("[4/10  ####------][ 40%]")
sleep(0.7)
print("[5/10  #####-----][ 50%]")
sleep(0.1)
print("[6/10  ######----][ 60%]")
sleep(0.1)
print("[7/10  #######---][ 70%]")
sleep(1)
print("[8/10  ########--][ 80%]")
sleep(0.5)
print("[9/10  #########-][ 90%]")
sleep(0.2)
print("[10/10 ##########][100%]")
sleep(1)
print("|||||[SUCCESFULL]|||||")
print("\n---------------------------------------------------\n")
print("Apakah Anda Ingin Melihat Biodata?\n[ya]  [tidak]")
sleep(0.5)
x = input("Pilihan Anda : ")

if x == "ya" :
	print("\n---------------------------------------------------\nNama                 = ", nama)
	sleep(0.5)
	print("Kelas                = ", kelas)
	sleep(0.5)
	print("Sekolah              = ", sekolah)
	sleep(0.5)
	print("NIS                  = ", NIS)
	sleep(0.5)
	print("Alamat               = ", alamat)
	sleep(0.5)
	print("Agama                = ", agama)
	sleep(0.5)
	print("Tempat Tanggal Lahir = ", tanggal)
	sleep(0.5)
	print("Umur                 = ", umur)
	sleep(0.5)
	print("---------------------------------------------------\n")
	print(quit)

if x == "tidak":
    print("Selamat Tinggal")
    sleep(1)
    print("^^ Semoga Harimu Menyenangkan ^^")