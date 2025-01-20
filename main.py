import os

# Biodata Pembuat:
# M. Fatur Maulidan Azzahra - 10124907
# Mata Kuliah Sistem Operasi Mengenai Disk Scheduling
"""
    Disk Scheduling proses menentukan urutan akses ke disk untuk melayani permintaan baca/tulis pada disk. 
    Disk scheduling sangat penting untuk memaksimalkan efisiensi akses disk, terutama karena waktu pencarian (seek time) 
    untuk memindahkan kepala baca/tulis merupakan faktor utama dalam performa disk.
"""

# track = [98, 183, 37, 122, 14, 124, 65, 67, 80, 120]
track = []
head = 0
jumlah_track = 10
track_result = ""
nama_metode = ""

def main():
    global head, track, jumlah_track, track_result
    
    jumlah_track = int(input("Masukkan jumlah track: "))
    head = int(input("Masukkan posisi head: "))
    track_result += str(head) + " -> "

    for i in range(jumlah_track):
        track_new = int(input(f"Masukkan track ke-{i+1} : "))
        track.append(track_new)
        
    checkMetode(menu())
    
def menu():
    print(f"Pilih 1 - 4 Metode apa yang akan digunakan")
    print(f"1. Metode FIFO (First In First Out)")
    print(f"2. Metode LIFO (Last In First Out)")
    print(f"3. Metode SSTF (Shortest Service Time First)")
    print(f"4. Metode SCAN")
    print(f"5. Metode C-SCAN")
    print(f"6. Print Semua Hasil")
    pilihan = int(input("Pilih Metode: "))
    return pilihan

def checkMetode(metode):
    global nama_metode
    os.system('cls')
    if metode == 1:
        nama_metode = "FIFO (First In First Out)"
        FIFO()
    elif metode == 2:
        nama_metode = "LIFO (Last In First Out)"
        LIFO()
    elif metode == 3:
        nama_metode = "SSTF (Shortest Seek Time First)"
        SSTF()
    elif metode == 4:
        nama_metode = "SCAN"
        SCAN()
    elif metode == 5:
        nama_metode = "C-SCAN"
        CSCAN()
    elif metode == 6:
        print("Hasil Semua Metode")
        print(f"Metode FIFO: ", FIFO())
        print(f"Metode LIFO: ", LIFO())
        print(f"Metode SSTF: ", SSTF())
        print(f"Metode SCAN: ", SCAN())
        print(f"Metode C-SCAN: ", CSCAN())
    else:
        print(f"Metode yang dipilih tidak ada \n")
        checkMetode()

# Metode First In First Out
def FIFO():
    global track_result
    track_result_fifo = track_result
    for i in range(jumlah_track):
        track_result_fifo += str(track[i]) + " -> " if i != jumlah_track - 1 else str(track[i])
        
    return track_result_fifo

def LIFO():
    global track_result
    track_result_lifo = track_result
    for i in range(jumlah_track - 1, -1, -1):
        track_result_lifo += str(track[i]) + " -> " if i != 0 else str(track[i])

    return track_result_lifo

def SSTF():
    global track_result, track
    track_result_sstf = track_result 
    
    track_temp = sortTrackForSSTF(sorted(track), head)
    
    for i in range(jumlah_track):
        track_result_sstf += str(track_temp[i]) + " -> " if i != jumlah_track - 1 else str(track_temp[i])
        
    return track_result_sstf
    
def SCAN():
    global track_result, track
    track_result_scan = track_result
    
    track_temp = sortTrackForSCAN(sorted(track), head)
    
    for i in range(jumlah_track):
        track_result_scan += str(track_temp[i]) + " -> " if i != jumlah_track - 1 else str(track_temp[i])
    
    return track_result_scan
    
def CSCAN():
    global track_result, track
    track_result_cscan = track_result
    
    track_temp = sortTrackForCSCAN(sorted(track), head)
    
    for i in range(jumlah_track):
        track_result_cscan += str(track_temp[i]) + " -> " if i != jumlah_track - 1 else str(track_temp[i])

    return track_result_cscan

def sortTrackForSSTF(track, head):
    track_temp = []
    for i in range(len(track)):
        if(head > track[i]):
            track_temp.append(track[i])
    
    track_temp = sorted(track_temp, reverse=True)
    
    for i in range(len(track)):
        if(head <= track[i]):
            track_temp.append(track[i])
    
    return track_temp
    
def sortTrackForSCAN(track, head):
    track_temp = []
    track_temp_2 = []
    
    for i in range(len(track)):
        if (head < track[i]):
            track_temp.append(track[i])
    
    for i in range(len(track)):
        if(head > track[i]):
            track_temp_2.append(track[i])
            
    track_temp_2 = sorted(track_temp_2, reverse=True)

    track_temp.extend(track_temp_2)
    
    return track_temp

def sortTrackForCSCAN(track, head):
    track_temp = []
    
    for i in range(len(track)):
        if(head < track[i]):
            track_temp.append(track[i])
            
    for i in range(len(track)):
        if(head > track[i]):
            track_temp.append(track[i])
            
    return track_temp
    
    
main()
print("Posisi Head: ", head)
print("Nilai Dari Track: ", track)
print("Jumlah Track: ", jumlah_track)
print("Metode yang digunakan: ", nama_metode)
print("Track Result: ", track_result)