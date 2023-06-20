from bmp_io import *
from bmp_func import *
from bmp_colmods import *
from bmp_func3d import *


for i in range(30):
    data,bitmap,start,filename,padding,width,height = bmp_load('marbles')


    #gray scale
    """
    for i in range(height):
        for j in range(width):
            val = int(math.sqrt(bitmap[i][j][0]**2+bitmap[i][j][1]**2+bitmap[i][j][2]**2)/math.sqrt(3))
            bitmap[i][j][0] = val
            bitmap[i][j][1] = val
            bitmap[i][j][2] = val
    """


    #gray scale 2
    """
    for i in range(height):
        for j in range(width):
            val = max(bitmap[i][j][0],bitmap[i][j][1],bitmap[i][j][2])
            bitmap[i][j][0] = val
            bitmap[i][j][1] = val
            bitmap[i][j][2] = val
    """


    #gaussian blur
    """
    operator = [[1,2,3,4,3,2,1],[2,3,4,5,4,3,2],[3,4,5,6,5,4,3],
    [4,5,6,7,6,5,4],[3,4,5,6,5,4,3],[2,3,4,5,4,3,2],[1,2,3,4,3,2,1]]
    blur(bitmap,operator)
    """


    #linear blur
    """
    operator = [[1]*7]*7
    blur(bitmap,operator)
    """


    #pixelation
    """
    pixelation(bitmap,10)
    """


    # RGB to HSV testing
    """
    print(RGB_to_HSV(255,0,0))
    print(RGB_to_HSV(0,255,0))
    print(RGB_to_HSV(0,0,255))
    """


    #3D stuff
    transform_3d(bitmap,(i/10)-1.5,width)


    bmp_save(data,bitmap,start,filename+str(i),padding)