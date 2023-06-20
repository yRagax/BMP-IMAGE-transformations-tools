def blur(bitmap, operator):
    d = len(operator)//2
    height = len(bitmap)
    width = len(bitmap[0])
    for i in range(height):
        for j in range(width):
            B_sum = G_sum = R_sum = times = 0
            for k in range(i-d,i+d):
                for l in range(j-d,j+d):
                    if k > -1 and k < height and l > -1 and l < width:
                        B_sum += bitmap[k][l][0]*operator[k-i+d][l-j+d]
                        G_sum += bitmap[k][l][1]*operator[k-i+d][l-j+d]
                        R_sum += bitmap[k][l][2]*operator[k-i+d][l-j+d]
                        times += operator[k-i+d][l-j+d]
            if times==0:
                continue
            bitmap[i][j][0] = int(B_sum / times)
            bitmap[i][j][1] = int(G_sum / times)
            bitmap[i][j][2] = int(R_sum / times)


def pixelation(bitmap, size):
    height = len(bitmap)
    width = len(bitmap[0])
    for i in range(0,height,2*size):
        for j in range(0,width,2*size):
            B_sum = G_sum = R_sum = times = 0
            for k in range(i-size,i+size):
                for l in range(j-size,j+size):
                    if k > -1 and k < height and l > -1 and l < width:
                        B_sum += bitmap[k][l][0]
                        G_sum += bitmap[k][l][1]
                        R_sum += bitmap[k][l][2]
                        times += 1
            if times==0:
                continue
            B_sum = int(B_sum/times)
            G_sum = int(G_sum/times)
            R_sum = int(R_sum/times)
            for k in range(i-size,i+size):
                for l in range(j-size,j+size):
                    if k > -1 and k < height and l > -1 and l < width:
                        bitmap[k][l][0] = B_sum
                        bitmap[k][l][1] = G_sum
                        bitmap[k][l][2] = R_sum