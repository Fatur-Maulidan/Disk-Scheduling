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