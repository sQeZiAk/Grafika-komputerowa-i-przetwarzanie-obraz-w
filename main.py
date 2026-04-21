import cv2
import numpy as np
import matplotlib.pyplot as plt
import urllib.request

# Obraz
url = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Lemon.jpg/250px-Lemon.jpg"

# Dodanie nagłówka User-Agent, aby uniknąć błędu 403 Forbidden
req = urllib.request.Request(
    url,
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)
resp = urllib.request.urlopen(req)
image_array = np.asarray(bytearray(resp.read()), dtype=np.uint8)
img = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Wyświetlanie obrazu 
plt.imshow(img_rgb)
plt.title("Oryginalny obraz")
plt.axis("off")
plt.show()

# zmiana rozdzielczości 
width = int(img.shape[1] * 0.5)
height = int(img.shape[0] * 0.5)
resized = cv2.resize(img, (width, height))

# zmiana koloru
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

# obrót
rotated = cv2.rotate(gray, cv2.ROTATE_90_CLOCKWISE)

# obraz konc
plt.imshow(rotated, cmap='gray')
plt.title("Po przetwarzaniu")
plt.axis("off")
plt.show()

# macierz
print("Macierz obrazu:")
print(rotated)