import os
import sys
import time

os.system('clear')
time.sleep(1)
os.system(' figlet Tools-Setan Termux')
print "=================================================="
print " AUTHOR : TH4UF4N"
print " LOKASI : Di Memori Internal"
print " Github : https://github.com/G3B0K-ID"
print " Warning: Membuat Tak Semudah Memakai"
print "=================================================="
print
time.sleep(2)
print "[+] Menu Pilihan [+]"
print "[1] Bahan Termux"
print "[2] Torjan"
print "[3] grabcam"
print "[4] dark fb"
print "[5] exit to tools"
pilih = raw_input('[?] pilih : ')
if pilih == "1":
        os.system('pkg update && pkg upgrade')
        os.system('pkg install python')
        os.system('pkg install python2')
        os.system('pkg install pip')
        os.system('pkg install mechanize')
        os.system('pip2 install requests')
        print "[+] Penginstallan Selesai"
elif pilih == "2":
        os.system('git clone https://github.com/RI33F/Trojans')
        print "[+] Penginstallan Selesai"
        print "[+] Selanjutnya Ketik $ cd Trojans"
        print "[+] Lalu Ketil $ python2 trojans.py"
elif pilih == "3":
        os.system('git clone https://github.com/noob-hackers/grabcam/')
        print "[+] Penginstallan Selesai"
        print "[+] Selanjutnya Ketik $ cd grabcam"
        print "[+] Lalu Ketil $ bash grabcam.sh"
elif pilih == "4":
        print "[+] git clone https://github.com/B4N954N2-ID/Dark"
        print "[+] Penginstallan Selesai"
        print "[+] Selanjutnya Ketik $ cd Dark"
        print "[+] Lalu Ketil $ python2 Darkfb.py"
elif pilih == "5":
        os.system("exit")
