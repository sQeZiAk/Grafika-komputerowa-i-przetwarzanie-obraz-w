import cv2
import numpy as np
import matplotlib.pyplot as plt
import urllib.request


url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/Fronalpstock_big.jpg"


req = urllib.request.Request(
    url,
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
)

resp = urllib.request.urlopen(req)
image = np.asarray(bytearray(resp.read()), dtype=np.uint8)

img = cv2.imdecode(image, cv2.IMREAD_COLOR)


img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)



plt.figure(figsize=(10, 6))
plt.imshow(img_rgb)
plt.title("Zdjęcie")
plt.axis("off")
plt.show()



gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

hist_gray = cv2.calcHist([gray], [0], None, [256], [0, 256])

plt.figure(figsize=(10, 5))
plt.plot(hist_gray, color='black')
plt.title("Histogram całego zdjęcia")
plt.xlabel("Jasność pikseli")
plt.ylabel("Liczba pikseli")
plt.show()


colors = ('red', 'green', 'blue')

plt.figure(figsize=(10, 5))

for i, color in enumerate(colors):
    hist = cv2.calcHist([img_rgb], [i], None, [256], [0, 256])
    plt.plot(hist, color=color)

plt.title("Histogram RGB")
plt.xlabel("Jasność pikseli")
plt.ylabel("Liczba pikseli")
plt.show()


brightness = np.mean(gray)


contrast = np.std(gray)


bright_pixels = np.sum(gray > 240) / gray.size * 100


dark_pixels = np.sum(gray < 15) / gray.size * 100

print("=== ANALIZA ZDJĘCIA ===")
print(f"Średnia jasność: {brightness:.2f}")
print(f"Kontrast: {contrast:.2f}")
print(f"Prześwietlone piksele: {bright_pixels:.2f}%")
print(f"Ciemne piksele: {dark_pixels:.2f}%")



if contrast < 30:
    print("Zdjęcie ma niski kontrast.")
else:
    print("Kontrast zdjęcia jest dobry.")

if bright_pixels > 20:
    print("Zdjęcie może być prześwietlone.")

if dark_pixels > 20:
    print("Zdjęcie może być niedoświetlone.")

if 80 < brightness < 180:
    print("Ekspozycja zdjęcia jest prawidłowa.")
else:
    print("Ekspozycja zdjęcia może być niepoprawna.")