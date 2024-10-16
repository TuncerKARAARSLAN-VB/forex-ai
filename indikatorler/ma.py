import matplotlib.pyplot as plt
import numpy as np

from datetime import datetime, timedelta

# Bugünün tarihi
bugun = datetime.now()

# Son 100 günün ve bugünün tarihlerini listeye ekleme
son_100_gun_tarihleri = [(bugun - timedelta(days=i)).strftime('%Y-%m-%d') for i in range(100, -1, -1)]

# Listeyi gösterme
print(son_100_gun_tarihleri)



# Başlangıç fiyatı 10
fiyatlar = [10]

# Rastgele artış, azalış ya da aynı kalma
degisimler = np.random.choice([-1, 0, 1], 100)  # -1 azalsın, 0 sabit kalsın, 1 artsın

# Fiyat listesini oluşturma
for degisim in degisimler:
    fiyatlar.append(fiyatlar[-1] + degisim)

# SMA (Hareketli Ortalama) Hesaplama
pencere_boyutu = 5
sma = [sum(fiyatlar[max(0, i - pencere_boyutu + 1):i + 1]) / min(pencere_boyutu, i + 1) for i in range(len(fiyatlar))]

# Grafik Oluşturma
plt.plot(son_100_gun_tarihleri, fiyatlar, marker='o', label='Kapanış Fiyatları')
plt.plot(son_100_gun_tarihleri, sma, marker='x', label='SMA (5 Gün)')
plt.title('Hareketli Ortalama Hesaplama (Random Yükselme/Azalış)')
plt.xlabel('Gün')
plt.ylabel('Fiyat')
plt.legend()
plt.grid()
plt.show()
