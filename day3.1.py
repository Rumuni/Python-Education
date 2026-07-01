import math
print(math.pi)

def calculate_cylinder(radius, height):
    S = 2 * math.pi * radius ** 2 +2 * math.pi * radius * height
    V = math.pi * radius ** 2 * height
    return S, V

r = 3.0
h = 5.0

print(f"半径：{r}, 高さ：{h} の円柱の計算結果")
s, v =calculate_cylinder(r, h)
print(f"表面積：{s}, 体積：{v}")