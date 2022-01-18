from datetime import *
from prettytable import PrettyTable
now = datetime.now()
hari_ini = now.strftime("%A")
tanggal = date.today()


class main:
	def __init__(self, jadwal):
		senin = """Sejarah Indonesia
		PPKN
		Kimia"""
		
		selasa = """Biologi
		Prakarya & KWU
		Matematika
		PJOK"""
		
		rabu = """Matematika
		B. Indonesia
		Fisika
		Seni Budaya"""
		
		kamis = """Matematika
		Sosiologi
		Biologi
		Bahasa Jawa"""
		
		jumat = """PAI
		B. Indonesia
		B. Inggris"""
		
		if jadwal == "Monday":
			jadwal = senin
			hari = "Senin"
		elif jadwal == "Tuesday":
			jadwal = selasa
			hari = "Selasa"
		elif jadwal == "Wednesday":
			jadwal = rabu
			hari = "Rabu"
		elif jadwal == "Thursday":
			jadwal = kamis
			hari = "Kamis"
		elif jadwal == "Friday":
			jadwal = jumat
			hari = "Jum'at"
		elif jadwal == "Saturday":
			jadwal = sabtu
			hari = "Sabtu"
		elif jadwal == "Sunday":
			jadwal = minggu
			hari = "Minggu"
		
		self.jadwal = jadwal
		self.hari = hari
	
	def tampilkan(self):
		hasil = {}
		hasil['hari'] = self.hari
		hasil['jadwal'] = self.jadwal
		return hasil

def home():
	h = "\033[92m"
	p = "\033[0m"
	print(h + "\n\t\t\t\tJadwal Pelajaran XII MIPA 1\n"+ p)
	daftarjadwal = PrettyTable(["Senin", "Selasa", "Rabu", "Kamis", "Jum'at"])
	daftarjadwal.add_row(["Sejarah Indonesia", "Biologi", "Matematika", "Matematika", "PAI"])
	daftarjadwal.add_row(["PPKN", "Prakarya & KWU", "B. Indonesia", "Sosiologi", "B. Indonesia"])
	daftarjadwal.add_row(["Kimia", "Matematika", "Fisika", "Biologi", " B. Inggris"])
	daftarjadwal.add_row(["", "PJOK", "Seni Budaya", "B. Jawa", ""])
	print(daftarjadwal)
	a = main(str(hari_ini))
	b = a.tampilkan()
	print("Tanggal: " + h + str(tanggal) + p)
	print("Hari: " + h + b['hari'] + p)
	print("\nJadwal Pelajaran:")
	for s in b['jadwal'].replace('\t', '').splitlines():
		print("- " + s)
home()