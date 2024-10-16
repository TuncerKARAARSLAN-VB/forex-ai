# Forex AI

Bu çalışmadaki amaç, piyasaya giriş ve çıkış anlarının analizini yapacak bir araç geliştirmektir.

Çalışmalar major para birimleri üzerinde yapılacak, spreadleri düşük likiditesi yüksek para birimleri üzerinde çalışmalar yapılacaktır.

Forex piyasasında en çok işlem gören ve likiditesi en yüksek olan **Major Para Çiftleri** (Major Currency Pairs) şunlardır:

1. **EUR/USD** – Euro / ABD Doları
2. **GBP/USD** – İngiliz Sterlini / ABD Doları
3. **USD/JPY** – ABD Doları / Japon Yeni
4. **USD/CHF** – ABD Doları / İsviçre Frangı
5. **AUD/USD** – Avustralya Doları / ABD Doları
6. **NZD/USD** – Yeni Zelanda Doları / ABD Doları
7. **USD/CAD** – ABD Doları / Kanada Doları

Bu major çiftler, dünya ekonomisindeki en büyük para birimlerini içerdiğinden yüksek hacimli işlemlerle öne çıkar. Spreadler genellikle düşüktür ve volatilite daha tahmin edilebilir olabilir.

## Karar Destek Yaklaşımları - Robot Tipleri ve Yaklaşımları

Forex piyasasına giriş çıkıiı destekleyecek analizlerimizde yaklaşımlar şunlar olabilir.

1. **Trend Takip**: Belirli indikatörler (ör. Moving Averages) ile trendi izleyen bir strateji mi?
2. **Destek ve Direnç Seviyeleri**: Fiyatın belirli seviyelere ulaştığında pozisyon açması veya kapatması mı?
3. **Scalping**: Kısa vadeli fiyat dalgalanmalarından küçük kazançlar elde etmeyi mi hedefliyoruz?
4. **Portföy Yönetimi**: Çoklu indikatör verileri ve portföy dağılımına göre mi kararlar alacağız?

## Piyasalardaki Yaygın İndikatörler

İşte Forex piyasasında alım-satım stratejileri için yaygın olarak kullanılan indikatörler ve açıklamaları ile birlikte bir tablo:

| **İndikatör**             | **Kullanım Alanı**                                                                                     | **Açıklama**                                                                                                                             |
|---------------------------|--------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| **Moving Average (MA)**    | Trend yönünü belirlemek                                                                                | Fiyatların zaman içindeki ortalamasını hesaplar. Yükselen veya düşen trendleri belirlemekte kullanılır.                                 |
| **Relative Strength Index (RSI)** | Aşırı alım/satım bölgelerini tespit etmek                                                        | Fiyatın aşırı alım veya aşırı satım bölgesinde olup olmadığını gösterir. 0-100 arasında bir değer alır, genellikle 30 altı aşırı satım, 70 üstü aşırı alım olarak kabul edilir. |
| **Moving Average Convergence Divergence (MACD)** | Trend yönü ve momentum ölçmek                                                                      | İki hareketli ortalama arasındaki farkı kullanarak momentum ve trend değişimlerini tespit eder.                                         |
| **Bollinger Bands**        | Volatilite ve fiyat hareketlerinin aşırılıklarını değerlendirmek                                       | Fiyatın bir hareketli ortalamanın etrafındaki belirli bir standart sapma aralığında hareket edip etmediğini gösterir. Volatiliteye duyarlıdır. |
| **Stochastic Oscillator**  | Aşırı alım/satım bölgelerini belirlemek                                                                | Fiyatın kapanış değerinin belirli bir süre içindeki fiyat aralığına kıyasla nerede olduğunu gösterir. Genellikle 80 üzeri aşırı alım, 20 altı aşırı satım olarak kabul edilir. |
| **Average True Range (ATR)** | Piyasanın volatilitesini ölçmek                                                                        | Belirli bir dönem boyunca ortalama fiyat hareketini ölçer. Daha yüksek değerler daha yüksek volatiliteye işaret eder.                    |
| **Parabolic SAR**          | Trend yönünü ve dönüş noktalarını tespit etmek                                                         | Fiyatların yön değiştirdiği potansiyel dönüş noktalarını belirlemek için kullanılır. Genellikle trend takibi ve çıkış noktası olarak kullanılır. |
| **Fibonacci Retracement**  | Fiyat düzeltmelerini ve destek/direnç seviyelerini belirlemek                                          | Fiyatın belirli bir trendin ne kadarını geri çektiğini belirlemek için kullanılır. Özellikle destek ve direnç seviyelerini bulmada faydalıdır. |
| **Ichimoku Kinko Hyo**     | Trend yönünü, momentum ve destek/direnç seviyelerini bir arada değerlendirmek                           | Birden fazla bileşeni olan bu indikatör, trend yönü, momentum, destek ve direnç seviyeleri hakkında geniş kapsamlı bilgi sağlar.         |
| **Commodity Channel Index (CCI)** | Aşırı alım/satım bölgelerini tespit etmek                                                         | Fiyatın ortalamaya göre ne kadar sapma gösterdiğini ölçer. Pozitif veya negatif aşırılıkları tespit ederek trend dönüşlerini tahmin etmeye çalışır. |

### İndikatör Kullanımı ve Stratejiler:

- **Trend Takip İndikatörleri**: Moving Average, MACD, Parabolic SAR gibi indikatörler trend yönünü ve dönüş noktalarını anlamak için kullanılır.
- **Momentum İndikatörleri**: RSI, Stochastic, CCI gibi indikatörler piyasanın momentumunu ve aşırı alım/satım bölgelerini tespit etmeye yarar.
- **Volatilite İndikatörleri**: Bollinger Bands ve ATR gibi indikatörler piyasanın ne kadar hareketli olduğunu ve potansiyel fiyat kırılmalarını öngörmeye çalışır.
- **Destek/Direnç İndikatörleri**: Fibonacci Retracement ve Ichimoku gibi indikatörler fiyatın potansiyel geri çekilme ve sıçrama noktalarını bulmak için kullanılır.

Bu indikatörler, Forex piyasasında çeşitli stratejiler geliştirmek için kullanılabilir ve bir araya getirilerek daha güçlü bir analiz elde edilebilir.

## Yöntem

Bu çalışmada amaç yapay zeka ile yapılacak analizler ve çalışmalarda elde edilecek en doğru indikatör gruplarının birbirleri ile koordinali çalışmaları ve bizi istenmeyen piyas harekerlerinden kurtarmaları. Bu nedenle tek indikatör kullanmak yerine, farklı karar destek yaklaşımlarına göre indikatör gruplarının verimliliği üzerine odaklanılacak.
