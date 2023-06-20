import math
import copy


def f(x, t, w, d):
    return (w/2)-((w/2)-x)*math.cos(t)-(((1/2)*(((w/2)-x)**2)*math.sin(2*t))/(d-((w/2)-x)*math.sin(t)))


def g(x, y, t, w, d, h):
    return (h/2)+(d*(y-(h/2)))/(d+(x-w/2)*math.sin(t))


def transform_3d(bitmap, t, d):
    output_bitmap = copy.deepcopy(bitmap)
    height = len(bitmap)
    width = len(bitmap[0])

    for i in range(height):
        transformed = []
        for j in range(width):
            transformed.append(f(j,t,width,d))
        for j in range(math.floor(transformed[0])):
            output_bitmap[i][j][0] = 0
            output_bitmap[i][j][1] = 0
            output_bitmap[i][j][2] = 0

        values = [[0,0,0]]
        weights = [transformed[0]-math.floor(transformed[0])]
        canvas_id = math.floor(transformed[0])
        previous_stop = transformed[0]
        transformed_id = 1
        while(canvas_id<width):
            while(transformed_id<len(transformed) and transformed[transformed_id]<canvas_id+1):
                values.append(bitmap[i][transformed_id-1])
                weights.append(transformed[transformed_id]-previous_stop)
                transformed_id += 1
                previous_stop = transformed[transformed_id-1]
            if(transformed_id<len(transformed)):
                values.append(bitmap[i][transformed_id])
                weights.append(canvas_id+1-previous_stop)
            avg_blues = avg_greens = avg_reds = 0
            for value,weight in zip(values,weights):
                avg_blues += value[0]*weight
                avg_greens += value[1]*weight
                avg_reds += value[2]*weight
            output_bitmap[i][canvas_id][0] = int(avg_blues)
            output_bitmap[i][canvas_id][1] = int(avg_greens)
            output_bitmap[i][canvas_id][2] = int(avg_reds)

            canvas_id += 1
            previous_stop = canvas_id
            values.clear()
            weights.clear()

    output_bitmap_2 = copy.deepcopy(output_bitmap)
    for j in range(width):
        transformed = []
        for i in range(height):
            transformed.append(g(j,i,t,width,d,height))
        for i in range(math.floor(transformed[0])):
            output_bitmap_2[i][j][0] = 0
            output_bitmap_2[i][j][1] = 0
            output_bitmap_2[i][j][2] = 0
        
        values = [[0,0,0]]
        weights = [transformed[0]-math.floor(transformed[0])]
        canvas_id = math.floor(transformed[0])
        previous_stop = transformed[0]
        transformed_id = 1
        while(canvas_id<height):
            while(transformed_id<len(transformed) and transformed[transformed_id]<canvas_id+1):
                values.append(output_bitmap[transformed_id-1][j])
                weights.append(transformed[transformed_id]-previous_stop)
                transformed_id += 1
                previous_stop = transformed[transformed_id-1]
            if(transformed_id<len(transformed)):
                values.append(output_bitmap[transformed_id][j])
                weights.append(canvas_id+1-previous_stop)
            avg_blues = avg_greens = avg_reds = 0
            for value,weight in zip(values,weights):
                avg_blues += value[0]*weight
                avg_greens += value[1]*weight
                avg_reds += value[2]*weight
            output_bitmap_2[canvas_id][j][0] = int(avg_blues)
            output_bitmap_2[canvas_id][j][1] = int(avg_greens)
            output_bitmap_2[canvas_id][j][2] = int(avg_reds)

            canvas_id += 1
            previous_stop = canvas_id
            values.clear()
            weights.clear()

    for i in range(height):
        for j in range(width):
            bitmap[i][j][0] = output_bitmap_2[i][j][0]
            bitmap[i][j][1] = output_bitmap_2[i][j][1]
            bitmap[i][j][2] = output_bitmap_2[i][j][2]