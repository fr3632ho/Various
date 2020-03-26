import math
import time



t0 = time.time()
tuple_list = list()





bool = False
for x in range(0,500):
    if bool:
        break
    for y in range(0,500):
        if bool:
            break
        for z in range(0,500):
            if x*y*z % 60 == 0 and (x < y and y < z) and (math.pow(x,2) + math.pow(y,2) == math.pow(z,2)) and (x + y + z == 1000):
                tuple_list.append((x,y,z))
                print(x,y,z)
                bool = True
                break


print(len(tuple_list))

t1 = time.time() - t0
print(t1)
