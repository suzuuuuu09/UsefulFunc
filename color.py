from time import sleep

class Text_color:
    def __init__(self):
        pass

    def gaming_color(self, text:str, interval:float = 0.01):
        def hsv_to_rgb(h, s, v):
            h = float(h)
            s = float(s)
            v = float(v)

            hi = int(h / 60) % 6
            f = h / 60 - hi
            p = v * (1 - s)
            q = v * (1 - f * s)
            t = v * (1 - (1 - f) * s)

            if hi == 0:
                r, g, b = v, t, p
            elif hi == 1:
                r, g, b = q, v, p
            elif hi == 2:
                r, g, b = p, v, t
            elif hi == 3:
                r, g, b = p, q, v
            elif hi == 4:
                r, b, g = t, p, v
            elif hi == 5:
                r, b, g = v, p, q

            r = int(r * 255)
            g = int(g * 255)
            b = int(b * 255)

            return [r, g, b]
        
        h, s, v = 0, 0.8, 1
        while True:
            h += 1
            rgb = hsv_to_rgb(h, s, v)
            r = int(rgb[0])
            g = int(rgb[1])
            b = int(rgb[2])
            print(f"\r\033[38;2;{r};{g};{b}m{text}", flush=True, end="")
            sleep(interval)
            if(h >= 360): h = 0

color = Text_color()
color.gaming_color("Hello world!")
