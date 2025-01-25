from algoritma_metode import *

def FIFO(track, head, jumlah_track):
    track_result_fifo = [head]
    traversed_track_result = []
    
    for i in range(jumlah_track):
        track_result_fifo.append(track[i])
        if i == 0:
            traversed_track_result.append(abs(head - track[i]))
        else :
            traversed_track_result.append(abs(track[i] - track[i-1]))
            
    return track_result_fifo, traversed_track_result

def LIFO(track, head, jumlah_track):
    track_result_lifo = []
    traversed_track_result = []
    
    for i in range(jumlah_track - 1, -1, -1):
        track_result_lifo.append(track[i])
        if i == jumlah_track - 1:
            traversed_track_result.append(abs(head - track[i]))
        else:
            traversed_track_result.append(abs(track[i] - track[i+1]))

    return [head] + track_result_lifo, traversed_track_result

def SSTF(track, head, jumlah_track):
    track_result_sstf = sortTrackForSSTF(sorted(track), head)
    traversed_track_result = []
    
    for i in range(jumlah_track):
        if i == 0:
            traversed_track_result.append(abs(head - track_result_sstf[i]))
        else:
            traversed_track_result.append(abs(track_result_sstf[i] - track_result_sstf[i-1]))
            
    return [head] + track_result_sstf, traversed_track_result
    
def SCAN(track, head, jumlah_track):
    track_result_scan = sortTrackForSCAN(sorted(track), head)
    traversed_track_result = []
    
    for i in range(jumlah_track):
        if i == 0:
            traversed_track_result.append(abs(head - track_result_scan[i]))
        else:
            traversed_track_result.append(abs(track_result_scan[i] - track_result_scan[i-1]))
            
    return [head] + track_result_scan, traversed_track_result
    
    
def CSCAN(track, head, jumlah_track):
    track_result_cscan = sortTrackForCSCAN(sorted(track), head)
    traversed_track_result = []
    
    for i in range(jumlah_track):
        if i == 0:
            traversed_track_result.append(abs(head - track_result_cscan[i]))
        else:
            traversed_track_result.append(abs(track_result_cscan[i] - track_result_cscan[i-1]))
            
    return [head] + track_result_cscan, traversed_track_result