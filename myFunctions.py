import pandas as pd
echonest=pd.read_csv("data/echonest.csv")
tracks=pd.read_csv("data/tracks.csv")
features=pd.read_csv("data/features.csv")

def printPivotTableLiveness(diz):
    col = ["Variables", "Cluster #1", "Cluster #2", "Cluster #3", "Cluster #4", "Cluster #5", "Cluster #6",
           "Cluster #7", "Cluster #8", "Cluster #9", "Cluster #10", "Cluster #11", "Cluster #12", "Cluster #13", "Cluster #14"]
    col = col[:len(diz)+1]

    df = pd.DataFrame(columns=col, index=None)

    df["Variables"] = ["25%", "< 50%", "< 75%", "75%> ", "TOT"]
    for name in col[1:]:
        n_cluster = int(name.split("#")[1])
        l = [0, 0, 0, 0, 0]
        for key in diz[n_cluster - 1]:
            row = echonest[echonest["track_id"] == key]
            x = row.audio_features_liveness.values
            if x <= 0.25:
                l[0] += 1
            elif 0.25 < x <= 0.50:
                l[1] += 1
            elif 0.50 < x <= 0.75:
                l[2] += 1
            elif 0.75 < x <= 1:
                l[3] += 1

        l = [round(100 * x / len(diz[n_cluster - 1]), 2) for x in l]
        s = sum(l)
        l[4] = s
        l = ['{:.2f}'.format(x) + "%" for x in l]
        df[name] = l

    return df

def printPivotTableSpeechiness(diz):
    col = ["Variables", "Cluster #1", "Cluster #2", "Cluster #3", "Cluster #4", "Cluster #5", "Cluster #6",
           "Cluster #7", "Cluster #8", "Cluster #9", "Cluster #10", "Cluster #11", "Cluster #12", "Cluster #13",
           "Cluster #14"]
    col = col[:len(diz) + 1]
    df = pd.DataFrame(columns=col, index=None)

    df["Variables"] = ["25%", "< 50%", "< 75%", "75%> ", "TOT"]
    for name in col[1:]:
        n_cluster = int(name.split("#")[1])
        l = [0, 0, 0, 0, 0]
        for key in diz[n_cluster - 1]:
            row = echonest[echonest["track_id"] == key]
            x = row.audio_features_speechiness.values
            if x <= 0.25:
                l[0] += 1
            elif 0.25 < x <= 0.50:
                l[1] += 1
            elif 0.50 < x <= 0.75:
                l[2] += 1
            elif 0.75 < x <= 1:
                l[3] += 1

        l = [round(100 * x / len(diz[n_cluster - 1]), 2) for x in l]
        s = sum(l)
        l[4] = s
        l = ['{:.2f}'.format(x) + "%" for x in l]
        df[name] = l

    return df

def printPivotTableInstrumentalness(diz):
    col = ["Variables", "Cluster #1", "Cluster #2", "Cluster #3", "Cluster #4", "Cluster #5", "Cluster #6",
           "Cluster #7", "Cluster #8", "Cluster #9", "Cluster #10", "Cluster #11", "Cluster #12", "Cluster #13",
           "Cluster #14"]
    col = col[:len(diz) + 1]
    df = pd.DataFrame(columns=col, index=None)

    df["Variables"] = ["25%", "< 50%", "< 75%", "75%> ", "TOT"]
    for name in col[1:]:
        n_cluster = int(name.split("#")[1])
        l = [0, 0, 0, 0, 0]
        for key in diz[n_cluster - 1]:
            row = echonest[echonest["track_id"] == key]
            x = row.audio_features_instrumentalness.values
            if x <= 0.25:
                l[0] += 1
            elif 0.25 < x <= 0.50:
                l[1] += 1
            elif 0.50 < x <= 0.75:
                l[2] += 1
            elif 0.75 < x <= 1:
                l[3] += 1

        l = [round(100 * x / len(diz[n_cluster - 1]), 2) for x in l]
        s = sum(l)
        l[4] = s
        l = ['{:.2f}'.format(x) + "%" for x in l]
        df[name] = l

    return df

def printPivotTableDuration(diz):
    col = ["Variables", "Cluster #1", "Cluster #2", "Cluster #3", "Cluster #4", "Cluster #5", "Cluster #6",
           "Cluster #7", "Cluster #8", "Cluster #9", "Cluster #10", "Cluster #11", "Cluster #12", "Cluster #13",
           "Cluster #14"]
    col = col[:len(diz) + 1]
    df = pd.DataFrame(columns=col, index=None)

    df["Variables"] = ["0-120s", "120-480s", "480-720s", "720>", "TOT"]

    for name in col[1:]:
        cont = 0
        n_cluster = int(name.split("#")[1])
        l = [0, 0, 0, 0, 0]
        for key in diz[n_cluster - 1]:
            row = tracks[tracks["track_id"] == key]
            x = row.track_duration.values
            if x <= 120:
                cont += 1
                l[0] += 1
            elif 120 < x <= 480:
                cont += 1
                l[1] += 1
            elif 480 < x <= 720:
                cont += 1
                l[2] += 1
            elif x > 720:
                cont += 1
                l[3] += 1
        l = [round(100 * x / cont, 2) for x in l]
        s = sum(l)
        l[4] = s
        l = ['{:.2f}'.format(x) + "%" for x in l]
        df[name] = l

    return df

def printPivotTableDanceability(diz):
    col = ["Variables", "Cluster #1", "Cluster #2", "Cluster #3", "Cluster #4", "Cluster #5", "Cluster #6",
           "Cluster #7", "Cluster #8", "Cluster #9", "Cluster #10", "Cluster #11", "Cluster #12", "Cluster #13",
           "Cluster #14"]
    col = col[:len(diz) + 1]
    df = pd.DataFrame(columns=col, index=None)

    df["Variables"] = ["25%", "< 50%", "< 75%", "75%> ", "TOT"]
    for name in col[1:]:
        n_cluster = int(name.split("#")[1])
        l = [0, 0, 0, 0, 0]
        for key in diz[n_cluster - 1]:
            row = echonest[echonest["track_id"] == key]
            x = row.audio_features_danceability.values
            if x <= 0.25:
                l[0] += 1
            elif 0.25 < x <= 0.50:
                l[1] += 1
            elif 0.50 < x <= 0.75:
                l[2] += 1
            elif 0.75 < x <= 1:
                l[3] += 1

        l = [round(100 * x / len(diz[n_cluster - 1]), 2) for x in l]
        s = sum(l)
        l[4] = s
        l = ['{:.2f}'.format(x) + "%" for x in l]
        df[name] = l

    return df

def printPivotTableBit(diz):
    col = ["Variables", "Cluster #1", "Cluster #2", "Cluster #3", "Cluster #4", "Cluster #5", "Cluster #6",
           "Cluster #7", "Cluster #8", "Cluster #9", "Cluster #10", "Cluster #11", "Cluster #12", "Cluster #13",
           "Cluster #14"]
    col = col[:len(diz) + 1]
    df  = pd.DataFrame(columns=col, index=None)

    df["Variables"] = ["bit < 80"," 80 < bit < 130","130 < bit < 180", "bit > 180", "TOT"]
    for name in col[1:]:
        n_cluster = int(name.split("#")[1])
        l = [0,0,0,0,0]
        for key in diz[n_cluster-1]:
            row = echonest[echonest["track_id"]==key]
            x = row.audio_features_tempo.values
            if x <= 80:
                l[0] += 1
            elif 80 < x <= 130:
                l[1] += 1
            elif 130 < x <= 180:
                l[2] += 1
            elif 180 < x:
                l[3] += 1

        l = [round(100*x/len(diz[n_cluster-1]),2) for x in l]
        s = sum(l)
        l[4] = s
        l = ['{:.2f}'.format(x)+"%" for x in l]
        df[name] = l

    return df

def printPivotTableZero(diz):
    col = ["Variables", "Cluster #1", "Cluster #2", "Cluster #3", "Cluster #4", "Cluster #5", "Cluster #6",
           "Cluster #7", "Cluster #8", "Cluster #9", "Cluster #10", "Cluster #11", "Cluster #12", "Cluster #13",
           "Cluster #14"]
    col = col[:len(diz) + 1]
    df  = pd.DataFrame(columns=col, index=None)

    df["Variables"] = [" zcr < 0.02"," 0.02 < zcr < 0.04","0.04 < zcr < 0.06", "zcr > 0.06", "TOT"]
    for name in col[1:]:
        n_cluster = int(name.split("#")[1])
        l = [0,0,0,0,0]
        for key in diz[n_cluster-1]:
            row = features[features["track_id"]==key]
            x = row.zcr_mean_01.values
            if x <= 0.02:
                l[0] += 1
            elif 0.02 < x <= 0.04:
                l[1] += 1
            elif 0.04 < x <= 0.06:
                l[2] += 1
            elif 0.06 < x:
                l[3] += 1

        l = [round(100*x/len(diz[n_cluster-1]),2) for x in l]
        s = sum(l)
        l[4] = s
        l = ['{:.2f}'.format(x)+"%" for x in l]
        df[name] = l

    return df

def printPivotTableSpectral(diz):
    col = ["Variables", "Cluster #1", "Cluster #2", "Cluster #3", "Cluster #4", "Cluster #5", "Cluster #6",
           "Cluster #7", "Cluster #8", "Cluster #9", "Cluster #10", "Cluster #11", "Cluster #12", "Cluster #13",
           "Cluster #14"]
    col = col[:len(diz) + 1]
    df  = pd.DataFrame(columns=col, index=None)

    df["Variables"] = ["bandwidth < 500"," 500 < bandwidth < 1000","1000 < bandwidth < 1800", "bandwidth > 1800", "TOT"]
    for name in col[1:]:
        n_cluster = int(name.split("#")[1])
        l = [0,0,0,0,0]
        for key in diz[n_cluster-1]:
            row = features[features["track_id"]==key]
            x = row.spectral_bandwidth_mean_01.values
            if x <= 500:
                l[0] += 1
            elif 500 < x <= 1000:
                l[1] += 1
            elif 1000 < x <= 1800:
                l[2] += 1
            elif 1800 < x:
                l[3] += 1

        l = [round(100*x/len(diz[n_cluster-1]),2) for x in l]
        s = sum(l)
        l[4] = s
        l = ['{:.2f}'.format(x)+"%" for x in l]
        df[name] = l

    return df

def printPivotTableRMSEEmean(diz):
    col = ["Variables", "Cluster #1", "Cluster #2", "Cluster #3", "Cluster #4", "Cluster #5", "Cluster #6",
           "Cluster #7", "Cluster #8", "Cluster #9", "Cluster #10", "Cluster #11", "Cluster #12", "Cluster #13",
           "Cluster #14"]
    col = col[:len(diz) + 1]
    df  = pd.DataFrame(columns=col, index=None)

    df["Variables"] = ["RMSEE < 1.25"," 1.25 < RMSEE < 2.5","2.5 < RMSEE < 3.75", "RMSEE > 3.75", "TOT"]
    for name in col[1:]:
        n_cluster = int(name.split("#")[1])
        l = [0,0,0,0,0]
        for key in diz[n_cluster-1]:
            row = features[features["track_id"]==key]
            x = row.rmse_mean_01.values
            if x <= 1.25:
                l[0] += 1
            elif 1.25 < x <= 2.5:
                l[1] += 1
            elif 2.5 < x <= 3.75:
                l[2] += 1
            elif 3.75 < x:
                l[3] += 1

        l = [round(100*x/len(diz[n_cluster-1]),2) for x in l]
        s = sum(l)
        l[4] = s
        l = ['{:.2f}'.format(x)+"%" for x in l]
        df[name] = l

    return df

def printPivotTableRMSEEmax(diz):
    col = ["Variables", "Cluster #1", "Cluster #2", "Cluster #3", "Cluster #4", "Cluster #5", "Cluster #6",
           "Cluster #7", "Cluster #8", "Cluster #9", "Cluster #10", "Cluster #11", "Cluster #12", "Cluster #13",
           "Cluster #14"]
    col = col[:len(diz) + 1]
    df  = pd.DataFrame(columns=col, index=None)

    df["Variables"] = ["RMSEE < 5"," 5 < RMSEE < 10","10 < RMSEE < 20", "RMSEE > 20", "TOT"]
    for name in col[1:]:
        n_cluster = int(name.split("#")[1])
        l = [0,0,0,0,0]
        for key in diz[n_cluster-1]:
            row = features[features["track_id"]==key]
            x = row.rmse_max_01.values
            if x <= 5:
                l[0] += 1
            elif 5 < x <= 10:
                l[1] += 1
            elif 10 < x <= 20:
                l[2] += 1
            elif 20 < x:
                l[3] += 1

        l = [round(100*x/len(diz[n_cluster-1]),2) for x in l]
        s = sum(l)
        l[4] = s
        l = ['{:.2f}'.format(x)+"%" for x in l]
        df[name] = l

    return df

def printPivotTableGenres(diz):
    col = ["Variables", "Cluster #1", "Cluster #2", "Cluster #3", "Cluster #4", "Cluster #5", "Cluster #6",
           "Cluster #7", "Cluster #8", "Cluster #9", "Cluster #10", "Cluster #11"]
    df  = pd.DataFrame(columns=col, index=None)
    
    df["Variables"] = ["Hip-Hop", "Pop", "Rock", "Experimental","Folk","Jazz","Electronic","International",
                       "Blues","Classical","Old-Time Historic", "Instrumental","TOT"]
                        
    for name in col[1:]:
        cont=0
        n_cluster = int(name.split("#")[1])
        l = [0,0,0,0,0,0,0,0,0,0,0,0,0]
        for key in diz[n_cluster-1]:      
            row = tracks[tracks["track_id"]==key]
            x = row.track_genre_top.values
            if x == "Hip-Hop":
                cont+=1
                l[0] += 1
            elif  x == "Pop":
                cont+=1
                l[1] += 1
            elif x == "Rock":
                cont+=1
                l[2] += 1
            elif x == "Experimental":
                cont+=1
                l[3] += 1
            elif  x == "Folk":
                cont+=1
                l[4] += 1
            elif x == "Jazz":
                cont+=1
                l[5] += 1
            elif x == "Electronic":
                cont+=1
                l[6] += 1
            elif  x == "International":
                cont+=1
                l[7] += 1
            elif x == "Blues":
                cont+=1
                l[8] += 1
            elif x =="Classical":
                cont+=1
                l[9] += 1
            elif  x == "Old-Time / Historic":
                cont+=1
                l[10] += 1
            elif x == "Instrumental":
                cont+=1
                l[11] += 1
        l = [round(100*x/cont,2) for x in l]
        s = sum(l)
        l[12] = s
        l = ['{:.2f}'.format(x)+"%" for x in l]
        df[name] = l 
            
    return df 