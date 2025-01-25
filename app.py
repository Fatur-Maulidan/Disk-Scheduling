# Biodata Pembuat:
# M. Fatur Maulidan Azzahra - 10124907
# Mata Kuliah Sistem Operasi Mengenai Disk Scheduling
"""
    Disk Scheduling proses menentukan urutan akses ke disk untuk melayani permintaan baca/tulis pada disk. 
    Disk scheduling sangat penting untuk memaksimalkan efisiensi akses disk, terutama karena waktu pencarian (seek time) 
    untuk memindahkan kepala baca/tulis merupakan faktor utama dalam performa disk.
"""

import streamlit as st

from metode import *
from helper import *

track = []
track_result = ""
head = 0
jumlah_track = 0

st.write("Biodata Pembuat")
st.write("Nama: M. Fatur Maulidan Azzahra")
st.write("NIM: 10124907")
st.write("Mata Kuliah: Sistem Operasi")

st.header("Disk Scheduling")

head = st.number_input(
    "Masukkan Nilai Head",
    placeholder="1 - 200",
    min_value=1,
    max_value=200,
    format="%d",
)

if head:
    if not handleRangeInput(head):
        st.warning("Masukkan angka antara 0 - 200")
        show_warning = True
else:
    show_warning = False 
    
jumlah_track = st.number_input(
    "Masukkan Jumlah Track",
    placeholder="Masukkan Jumlah Track minimal 1 dan maksimal 100",
    min_value=1,
    max_value=100,
    value=None,
    format="%d",
)

if jumlah_track is not None:
    for i in range(jumlah_track):
        track_new = st.number_input(
            f"Masukkan Track ke-{i+1}",
            min_value=0,
            max_value=200,
            value=0,  # Default value harus valid
            format="%d",  # Format angka bulat
        )
        track.append(track_new)  # Tambahkan nilai ke daftar track
else:
    st.stop()

if 0 not in track:
    track_result = str(head) + str(" -> ")
    for i in range(jumlah_track):
        track_result += str(track[i]) + " -> " if i != jumlah_track - 1 else str(track[i])
    
st.write(f"Track: {track_result}")

metode = st.selectbox(
    "Pilih Metode",
    ("FIFO", "LIFO", "SSTF", "SCAN", "C-SCAN")
)

if (metode == "FIFO") and (0 not in track and head is not None):
    track_result_fifo, traversed_track_result = FIFO(track, head, jumlah_track)
    st.write(f"Track: {track_result_fifo}")
    st.write(f"Traversed Track: {traversed_track_result}")
    
    resultAtPyPlot(track_result_fifo, traversed_track_result, metode, st)
    resultTraversedTrackResultTable(track_result_fifo, traversed_track_result, st)
    
elif(metode == "LIFO") and (0 not in track and head is not None):
    track_result_lifo, traversed_track_result = LIFO(track, head, jumlah_track)
    st.write(f"Track: {track_result_lifo}")
    st.write(f"Traversed Track: {traversed_track_result}")
    
    resultAtPyPlot(track_result_lifo, traversed_track_result, metode, st)
    resultTraversedTrackResultTable(track_result_lifo, traversed_track_result, st)

elif(metode == "SSTF") and (0 not in track and head is not None):
    track_result_sstf, traversed_track_result = SSTF(track, head, jumlah_track)
    st.write(f"Track: {track_result_sstf}")
    st.write(f"Traversed Track: {traversed_track_result}")
    
    resultAtPyPlot(track_result_sstf, traversed_track_result, metode, st)
    resultTraversedTrackResultTable(track_result_sstf, traversed_track_result, st)
    
elif(metode == "SCAN") and (0 not in track and head is not None):
    track_result_scan, traversed_track_result = SCAN(track, head, jumlah_track)
    st.write(f"Track: {track_result_scan}")
    st.write(f"Traversed Track: {traversed_track_result}")
    
    resultAtPyPlot(track_result_scan, traversed_track_result, metode, st)
    resultTraversedTrackResultTable(track_result_scan, traversed_track_result, st)
    
elif(metode == "C-SCAN") and (0 not in track and head is not None):
    track_result_cscan, traversed_track_result = CSCAN(track, head, jumlah_track)
    st.write(f"Track: {track_result_cscan}")
    st.write(f"Traversed Track: {traversed_track_result}")
    
    resultAtPyPlot(track_result_cscan, traversed_track_result, metode, st)
    resultTraversedTrackResultTable(track_result_cscan, traversed_track_result, st)



# column = [col1, col2, col3] = st.columns(3)

# split_number = split_number_into_parts(jumlah_track, parts=3)
# print(split_number)

# # Iterasi melalui kolom dan input nilai
# for i in range(len(column)):
#     with column[i]:  # Setiap kolom memiliki input masing-masing
#         for j in range(split_number[i]):
#             track_new = st.number_input(
#                 f"Masukkan Track ke-{j+1} (Kolom {i+1})",
#                 min_value=0,
#                 max_value=200,
#                 value=0,  # Default value harus valid
#                 format="%d",  # Format angka bulat
#             )
#             track.append(track_new)  # Tambahkan nilai ke daftar track

