def solution(genres, plays):
    answer = []
    index = []
    for i in range(0, len(genres), 1):
        index.append(i)
    playlist = list(zip(genres,plays,index))
    
    genre = {}
    song = {}
    
    for i in playlist:
        if i[0] in genre:
            genre[i[0]] += i[1]
            song[i[0]][i[2]] = i[1]            
        else:
            genre[i[0]] = i[1]
            song[i[0]] = {}
            song[i[0]][i[2]] = i[1]
    
    sorted_genre = dict(sorted(genre.items(), reverse=True, key=(lambda x:x[1])))
    for i in list(sorted_genre.keys()):
        count = 0
        for i, j in sorted(song[i].items(), reverse=True, key=lambda x:(x[1], -x[0])):
            count += 1
            answer.append(i)
            if count == 2:
                break
    
    
    return answer
