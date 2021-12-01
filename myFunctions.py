import pandas as pd
echonest=pd.read_csv("data/echonest.csv")
tracks=pd.read_csv("data/tracks.csv")

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