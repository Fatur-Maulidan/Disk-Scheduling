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
# track = [55, 58, 39, 18, 90, 160, 150, 38, 184]
track = []
head = 0
jumlah_track = 9
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
    os.system('cls')
    if metode == 1:
        FIFO()
    elif metode == 2:
        LIFO()
    elif metode == 3:
        SSTF()
    elif metode == 4:
        SCAN()
    elif metode == 5:
        CSCAN()
    elif metode == 6:
        print("Hasil Semua Metode")
        FIFO()
        LIFO()
        SSTF()
        SCAN()
        CSCAN()
    else:
        print(f"Metode yang dipilih tidak ada \n")
        checkMetode()

# Metode First In First Out
def FIFO():
    global track_result, head
    track_result_fifo = track_result
    traversed_track_result = []
    
    for i in range(jumlah_track):
        track_result_fifo += str(track[i]) + " -> " if i != jumlah_track - 1 else str(track[i])
        if i == 0:
            traversed_track_result.append(abs(head - track[i]))
        else :
            traversed_track_result.append(abs(track[i] - track[i-1]))
            
    printData(track_result_fifo, traversed_track_result, "FIFO")

def LIFO():
    global track_result
    track_result_lifo = track_result
    traversed_track_result = []
    
    for i in range(jumlah_track - 1, -1, -1):
        track_result_lifo += str(track[i]) + " -> " if i != 0 else str(track[i])
        if i == jumlah_track - 1:
            traversed_track_result.append(abs(head - track[i]))
        else:
            traversed_track_result.append(abs(track[i] - track[i+1]))
            
    printData(track_result_lifo, traversed_track_result, "LIFO")

def SSTF():
    global track_result, track
    track_result_sstf = track_result 
    traversed_track_result = []
    
    track_temp = sortTrackForSSTF(sorted(track), head)
    
    for i in range(jumlah_track):
        track_result_sstf += str(track_temp[i]) + " -> " if i != jumlah_track - 1 else str(track_temp[i])
        if i == 0:
            traversed_track_result.append(abs(head - track_temp[i]))
        else:
            traversed_track_result.append(abs(track_temp[i] - track_temp[i-1]))
    
    printData(track_result_sstf, traversed_track_result, "SSTF")
    
def SCAN():
    global track_result, track
    track_result_scan = track_result
    traversed_track_result = []
    
    track_temp = sortTrackForSCAN(sorted(track), head)
    
    for i in range(jumlah_track):
        track_result_scan += str(track_temp[i]) + " -> " if i != jumlah_track - 1 else str(track_temp[i])
        if i == 0:
            traversed_track_result.append(abs(head - track_temp[i]))
        else:
            traversed_track_result.append(abs(track_temp[i] - track_temp[i-1]))
        
    printData(track_result_scan, traversed_track_result, "SCAN")
    
def CSCAN():
    global track_result, track
    track_result_cscan = track_result
    traversed_track_result = []
    
    track_temp = sortTrackForCSCAN(sorted(track), head)
    
    for i in range(jumlah_track):
        track_result_cscan += str(track_temp[i]) + " -> " if i != jumlah_track - 1 else str(track_temp[i])
        if i == 0:
            traversed_track_result.append(abs(head - track_temp[i]))
        else:
            traversed_track_result.append(abs(track_temp[i] - track_temp[i-1]))

    printData(track_result_cscan, traversed_track_result, "C-SCAN")

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

def printData(track_result, traversed_result, nama_metode):
    global head, track, jumlah_track
    print(f"Metode yang digunakan: ", nama_metode)
    print(f"Posisi Head: ", head)
    print(f"Nilai Dari Track: ", track)
    print(f"Jumlah Track: ", jumlah_track)
    print(f"Track Result: ", track_result)
    print(f"Traversed Result: ", traversed_result)
    print(f"Sum Dari Traversed Result: ", sum(traversed_result))
    print(f"Average Dari Traversed Result: {sum(traversed_result) / len(traversed_result):.2f} \n")
    
main()