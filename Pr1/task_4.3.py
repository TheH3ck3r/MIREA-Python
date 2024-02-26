import tkinter as tk
import math

def pyshader(func, w, h):
    scr = bytearray((0, 0, 0) * w * h)
    for y in range(h):
        for x in range(w):
            p = (w * y + x) * 3
            scr[p:p + 3] = [max(min(int(c * 255), 255), 0)
                            for c in func(x / w, y / h)]
    return bytes('P6\n%d %d\n255\n' % (w, h), 'ascii') + scr

# def func(x, y):
#     packmen_center_x, packmen_center_y = 0.5, 0.5
#     packmen_radius = 0.4 
#     packmen_distance = math.sqrt((x - packmen_center_x) ** 2 + (y - packmen_center_y) ** 2)

#     packmen_eye_center_x, packmen_eye_center_y = 0.7, 0.3
#     packmen_eye_radius = 0.05

#     if packmen_distance <= packmen_radius:
#         if math.sqrt((x - packmen_eye_center_x) ** 2 + (y - packmen_eye_center_y) ** 2) <= packmen_eye_radius:
#             return (0, 0, 0)
#         else:
#             return (255, 255, 0)
#     else:
#         return (0, 0, 0

def func(x, y):
    # packmen_center_x, packmen_center_y = 0.5, 0.5
    # packmen_radius = 0.4 
    # packmen_distance = math.sqrt((x - packmen_center_x) ** 2 + (y - packmen_center_y) ** 2)

    # packmen_eye_center_x, packmen_eye_center_y = 0.7, 0.3
    # packmen_eye_radius = 0.05

    # mouth_start_angle = 0 * math.pi
    # mouth_end_angle = 0 * math.pi

    # if packmen_distance <= packmen_radius:
    #     if math.sqrt((x - packmen_eye_center_x) ** 2 + (y - packmen_eye_center_y) ** 2) <= packmen_eye_radius:
    #         return (0, 0, 0)
    #     elif (x - packmen_center_x) ** 2 + (y - packmen_center_y) ** 2 >= (packmen_radius - 0.05) ** 2:
    #         return (255, 255, 0)
    #     elif math.atan2(y - packmen_center_y, x - packmen_center_x) >= mouth_start_angle and math.atan2(y - packmen_center_y, x - packmen_center_x) <= mouth_end_angle:
    #         return (0, 0, 0)
    #     else:
    #         return (255, 255, 0)
    # else:
    #     return (0, 0, 0)

    body = ((x - 0.5) ** 2 + (y - 0.5) ** 2) < 0.1
    eye = ((x - 0.6) ** 2 + (y - 0.3) ** 2) > 0.003
    mouth = 0.6 * x + 0.2 < y or 0.6 * x + 0.2 < 1 - y
    p = int(body and eye and mouth)
    return p, p, 0


root = tk.Tk()
label = tk.Label(root)
img = tk.PhotoImage(data=pyshader(func, 256, 256)).zoom(2, 2)
label.pack()
label.config(image=img)
root.mainloop()