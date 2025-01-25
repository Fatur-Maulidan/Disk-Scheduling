import matplotlib.pyplot as plt
import pandas as pd

def handleRangeInput(input):
    if 0 <= input <= 200:
        return input
    return False

def split_number_into_parts(num, parts):
    max_part = (num + 2) // parts
    parts = []
    while num > 0:
        part = min(max_part, (num + len(parts)) // (len(parts) + 1))
        parts.append(part)
        num -= part
    return parts

def resultAtPyPlot(track_result, traversed_track_result, metode, st):
    traversed_track_result = [0]
    for i in range(1, len(track_result)):
        traversed_track_result.append(traversed_track_result[-1] + abs(track_result[i] - track_result[i-1]))  # Tambahkan selisih absolut
        
    print(traversed_track_result)
    
    plt.figure(figsize=(20, 10))  # Ukuran gambar (panjang, lebar)
    plt.plot(traversed_track_result, track_result, marker='o', markersize=5, color='blue')
    plt.title(f"{metode} Disk Scheduling")
    
    plt.xlim(0)
    plt.ylim(200,0)
    plt.ylabel("Track Number")
    plt.xlabel(f" Time --> ")
    
    for i, txt in enumerate(track_result):
        plt.annotate(txt, (traversed_track_result[i], track_result[i]))
    
    plt.subplots_adjust(left=0.1, right=0.95, top=0.9, bottom=0.1)
    
    st.pyplot(plt)
    
def resultTraversedTrackResultTable(track_result, traversed_track_result, st):
    df = pd.DataFrame({
        "Next Track Accessed": track_result,
        "Number of Track Traversed": [''] + traversed_track_result
    })
    
    st.table(df)
    st.write(f"Total Track Traversed = {" + ".join(map(str, traversed_track_result))} = {sum(traversed_track_result)}")
    st.write(f"Average Track Traversed = {sum(traversed_track_result)} / {len(traversed_track_result)} = {sum(traversed_track_result) / len(traversed_track_result):.2f}")
    