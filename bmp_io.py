def bmp_load(filename):
    data = open('resources/'+filename+'.bmp', 'rb').read()
    start = data[10]+data[11]*(16**2)+data[12]*(16**4)+data[13]*(16**6)
    width = data[18]+data[19]*(16**2)+data[20]*(16**4)+data[21]*(16**6)
    height = data[22]+data[23]*(16**2)+data[24]*(16**4)+data[25]*(16**6)
    padding = (4-3*width%4)%4
    bitmap = list(list(data[start:][i:i+3*width]) for i in range(0,height*(3*width+padding),3*width+padding))
    bitmap = [[bitmap[i][j:j+3] for j in range(0,len(bitmap[i]),3)] for i in range(0,len(bitmap))]
    return data,bitmap,start,filename,padding,width,height


def bmp_save(data,bitmap,start,filename,padding):
    bitmap = [[element for sublist in bitmap[i] for element in sublist] for i in range(0,len(bitmap))]
    bitmap = [row+[0]*padding for row in bitmap]
    bitmap = [element for sublist in bitmap for element in sublist]
    f = open('results/'+filename+'_modified.bmp','wb')
    f.write(data[:start]+bytes(bitmap))
    f.close()