#!/usr/bin/env python3


def belajar_gui(dibuat_oleh="Ruben Leonardo Sigalingging."):
	from os import system
	system("clear")
	system("pip install pyfiglet")
	system("pip install tk")
	system("clear")
	import tkinter as program_gui_ruben_leonardo_sigalingging
	jendela=program_gui_ruben_leonardo_sigalingging.Tk()


	# UBAH WARNA BACKGROUND ATAU LATAR BELAKANG :
	jendela.configure(bg="black")	


	def alat_hash_sha1(dibuat_oleh="Ruben Leonardo Sigalingging"):
		ubah_ke_kode_sha1=tombol_input_user.get()
		import hashlib
		kode_sha1=hashlib.sha1()
		kode_sha1.update(ubah_ke_kode_sha1.encode("ascii"))
		hasil_hash_sha1.set(str(kode_sha1.hexdigest()))
		label_program_ke_2.config(font=("Times New Roman",15,"bold","italic","roman"),fg="darkcyan")



	jendela.title("Program GUI Ruben Leonardo Sigalingging")


	jendela.geometry("1266x768")


	label=program_gui_ruben_leonardo_sigalingging.Label(jendela,text="[!] Program GUI [!]\n[!] Ruben Leonardo Sigalingging [!]",font=("Times New Roman",25,"bold","italic","roman"),cursor="crosshair",bd=2,height=5,width=50,bg="darkcyan",fg="darkgray",justify=program_gui_ruben_leonardo_sigalingging.CENTER)
	label.pack()


	tombol_input_user=program_gui_ruben_leonardo_sigalingging.Entry(jendela,width=25,bd=5,justify=program_gui_ruben_leonardo_sigalingging.CENTER,cursor="spraycan",fg="red",bg="black")
	# BUAT TOMBOL KE TENGAH.
	tombol_input_user.pack(side="top")


	# TOMBOL INPUT KEDUA
	tombol_input_user_ke_2=program_gui_ruben_leonardo_sigalingging.Button(jendela,text="Go To SHA-1 Encryption!",cursor="pirate",command=alat_hash_sha1,font=("Times New Roman",12),fg="darkcyan")
	tombol_input_user_ke_2.pack()


	hasil_hash_sha1=program_gui_ruben_leonardo_sigalingging.StringVar()
	hasil_hash_sha1.set("SHA-1 Hash Result Code!")


	label_program_ke_2=program_gui_ruben_leonardo_sigalingging.Label(jendela,font=("Times New Roman",15,"bold","italic","roman"),fg="darkcyan",textvariable=hasil_hash_sha1)
	label_program_ke_2.pack()






	jendela.mainloop()
belajar_gui()