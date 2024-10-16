# MA, Moving Avarage, Ağırlıklı Ortalama

**Hareketli Ortalama (Moving Average) Nedir?**

Hareketli ortalama, bir finansal varlığın fiyatlarının belirli bir süre boyunca ortalamasını alarak trendleri ve yönleri belirlemek için kullanılan bir teknik analiz aracıdır. Genellikle, piyasalarda alım-satım sinyalleri oluşturmak ve fiyat dalgalanmalarını düzeltmek için kullanılır.

[MA Python Code](ma.py)
![MA](./images/ma.png)

**Hareketli Ortalama Türleri:**

1. **Basit Hareketli Ortalama (SMA):** Belirli bir dönem içerisindeki fiyatların aritmetik ortalamasını alır.
   
   Varsayalım ki son 5 günün kapanış fiyatları: 20, 22, 24, 21, 23

   $$
   \text{SMA} = \frac{20 + 22 + 24 + 21 + 23}{5} = \frac{110}{5} = 22
   $$

   Burada \(P_i\), ilgili dönemdeki fiyatları ve \(n\) ise dönem sayısını ifade eder.

2. **Ağırlıklı Hareketli Ortalama (WMA):** Daha yeni fiyatlara daha fazla ağırlık vererek hesaplanır.

   $$
   \text{WMA} = \frac{\sum_{i=1}^{n} (P_i \cdot W_i)}{\sum_{i=1}^{n} W_i}
   $$

   Burada \(W_i\), ilgili dönemdeki ağırlıkları temsil eder.

3. **Üssel Hareketli Ortalama (EMA):** En son fiyatlara daha fazla ağırlık vererek hesaplanan bir hareketli ortalamadır. EMA, SMA’ya göre daha hızlı tepki verir.

   $$
   \text{EMA}_t = \left( \frac{P_t - \text{EMA}_{t-1}}{N} \right) + \text{EMA}_{t-1}
   $$

   Burada \(N\), süreyi belirtir (genellikle 2, 5, 10, 20, 50, 100 veya 200 gün olarak seçilir).

**Adım Adım Hareketli Ortalama Hesaplama:**

1. **Veri Toplama:** İlk olarak, belirli bir zaman diliminde (örneğin, son 20 gün) varlığın kapanış fiyatlarını toplayın.

2. **Hesaplama:**
   - **SMA için:** Tüm kapanış fiyatlarını toplayın ve toplamı gün sayısına bölün.
   - **WMA için:** Her fiyat için bir ağırlık belirleyin (örneğin, en son fiyat için en yüksek ağırlık) ve formülü uygulayın.
   - **EMA için:** İlk olarak bir SMA hesaplayın ve ardından yukarıdaki EMA formülünü kullanarak her gün için güncelleyin.

3. **Grafik Üzerinde Görselleştirme:** Hesapladığınız hareketli ortalamayı fiyat grafiği üzerine çizin. Böylece, fiyat hareketleri ile hareketli ortalama arasındaki ilişkiyi görebilirsiniz.

**Piyasa Giriş ve Çıkış Yorumları:**

- **Giriş Noktaları:**
  - **Kısa Vadeli SMA/EMA:** Eğer fiyat, kısa vadeli hareketli ortalamanın üzerinde kalıyorsa, alım sinyali olarak değerlendirebilirsiniz. Örneğin, 10 günlük EMA, 50 günlük EMA'yı yukarıdan kesiyorsa bu bir alım sinyali olabilir.
  - **Destek ve Direnç:** Hareketli ortalamalar, destek ve direnç seviyeleri olarak da kullanılabilir. Fiyat, bir hareketli ortalamayı test ettiğinde, buradan geri dönebilir veya bu seviyeden devam edebilir.

- **Çıkış Noktaları:**
  - **Kısa Vadeli SMA/EMA:** Eğer fiyat, hareketli ortalamanın altında kalıyorsa, satış sinyali olarak değerlendirilebilir. Örneğin, 10 günlük EMA, 50 günlük EMA'yı aşağıdan kesiyorsa bu bir satış sinyali olabilir.
  - **Zarar Durdurma:** Hareketli ortalamayı, zarar durdurma seviyeleri belirlemek için kullanabilirsiniz. Eğer fiyat belirli bir hareketli ortalamanın altına düşerse, pozisyonunuzu kapatabilirsiniz.

**Örnek Hesaplama:**

Varsayalım ki son 5 günün kapanış fiyatları: 20, 22, 24, 21, 23

1. **SMA Hesaplama:**

   $$
   \text{SMA} = \frac{20 + 22 + 24 + 21 + 23}{5} = \frac{110}{5} = 22
   $$

2. **EMA Hesaplama:** İlk olarak, 5 günlük SMA'yı kullanarak EMA hesaplamaya başlayabilirsiniz. Ardından, gün gün devam edin.

Hareketli ortalamalar, yatırım kararlarınızı desteklemek için güçlü araçlar sunar. Ancak, tek başlarına kullanılmamalıdırlar; diğer göstergelerle ve analizlerle birleştirilmelidir.

[MA Python Code](ma.py)

![MA](./images/ma.png)

## MA Nasıl Yorumlayacağız

USD/JPY paritesinde 1 saatlik grafiklerde 30 periyotluk hareketli ortalama (Moving Average - MA), kısa vadeli eğilimleri analiz etmek ve piyasa yönü hakkında fikir sahibi olmak için önemli bir göstergedir. Bu tür bir hareketli ortalama, 30 saatlik bir zaman dilimindeki fiyat ortalamasını gösterir ve genellikle trendin gücünü veya potansiyel dönüş noktalarını analiz etmek için kullanılır.

### 1. **Trend Takibi:**
   - **Fiyat, 30 Periyotluk MA'nın Üzerinde:** 
     Eğer USD/JPY fiyatı 30 periyotluk hareketli ortalamanın üzerinde seyrediyorsa, bu piyasanın yukarı yönlü bir trend içinde olduğunu gösterir. Bu durumda, alım yönünde bir fırsat olduğunu düşünebiliriz. Bu, boğa piyasası olarak yorumlanabilir ve alım (long) pozisyonları için uygun bir sinyal olabilir.
   
   - **Fiyat, 30 Periyotluk MA'nın Altında:**
     Eğer fiyat 30 periyotluk MA'nın altına düşmüşse, bu piyasanın düşüş eğiliminde olduğunu gösterir. Bu durumda, satış (short) pozisyonları daha uygun olabilir ve alım pozisyonlarından kaçınmak mantıklı olacaktır. Yatırımcılar, bu durumda alım için daha uygun seviyeleri bekleyebilir.

### 2. **Destek ve Direnç Olarak Kullanım:**
   - 30 periyotluk hareketli ortalama, aynı zamanda fiyatın destek veya direnç seviyelerini de gösterebilir. Fiyatın hareketli ortalamanın üzerine çıkması, bu seviyenin destek olarak çalıştığını ve fiyatın tekrar yukarı yönlü bir hareket yapabileceğini gösterebilir.
   - Öte yandan, fiyat hareketli ortalamanın altında direnç buluyorsa, bu satış baskısının devam edebileceğini ve düşüş eğiliminin süreceğini gösterebilir.

### 3. **Alım Kararları:**
   - **Golden Cross (Altın Kesişim):** 
     Eğer kısa vadeli bir hareketli ortalama (örneğin 10 periyotluk) 30 periyotluk MA'yı yukarı doğru keserse, bu genellikle yükseliş sinyali olarak kabul edilir ve alım pozisyonları için iyi bir zaman olabilir. Bu, genellikle fiyatların yukarı yönlü bir hareket başlatacağı anlamına gelir.
   
   - **Fiyatın 30 Periyotluk MA Üzerinde Kalması:**
     Fiyat hareketli ortalamanın üzerinde seyretmeye devam ettiği sürece bu, trendin güçlü bir şekilde yukarı yönlü olduğunu ve alım pozisyonlarının değerlendirilebileceğini gösterir.

### 4. **Satış Kararları:**
   - **Death Cross (Ölüm Kesişimi):** 
     Eğer kısa vadeli bir hareketli ortalama 30 periyotluk MA'yı aşağı doğru keserse, bu genellikle düşüş sinyali olarak kabul edilir ve satış (short) pozisyonları açmak için bir fırsat olabilir. Bu kesişim, düşüş trendinin başlangıcını gösterebilir.
   
   - **Fiyatın 30 Periyotluk MA'nın Altına Düşmesi:**
     Eğer fiyat hareketli ortalamanın altında seyretmeye başlarsa, bu piyasanın düşüş eğiliminde olduğunu ve alım yapmanın riskli olabileceğini gösterir. Yatırımcılar satış pozisyonlarını değerlendirebilir ya da alım için trendin tekrar tersine dönmesini bekleyebilir.

### 5. **Fiyatın Hareketli Ortalama Etrafında Yatay Seyretmesi:**
   - Bazen fiyat hareketli ortalama etrafında yatay bir seyir izleyebilir. Bu durumda piyasada belirgin bir trend olmaması, kararsız bir piyasa koşulunu gösterir. Fiyatın hareketli ortalamadan net bir şekilde uzaklaştığı noktalar alım ya da satış kararı için daha güvenilir olabilir.

### 6. **Genel Yorum:**
   - **Yukarı Yönlü Trend (Bullish):** USD/JPY fiyatı 30 periyotluk hareketli ortalamanın üzerinde seyrederken, bu yukarı yönlü bir piyasa hareketini destekleyebilir. Alım pozisyonları için uygun bir zaman olabilir.
   - **Aşağı Yönlü Trend (Bearish):** Fiyat hareketli ortalamanın altına düştüğünde, bu aşağı yönlü bir eğilimi işaret eder ve alım yapmaktan kaçınıp satış fırsatlarına odaklanmak mantıklı olabilir.

### Ek Faktörler:
   - **Destek ve Direnç Düzeyleri:** Hareketli ortalama ile birlikte fiyatın kritik destek ve direnç noktalarını da göz önünde bulundurmak, daha sağlam alım-satım kararları almanıza yardımcı olabilir.
   - **Temel Faktörler:** Forex piyasasında teknik analiz önemli olsa da, USD/JPY gibi paritelerde temel faktörler (ABD ve Japonya merkez bankası kararları, faiz oranları, ticaret dengesi gibi) fiyatı etkileyebilir. Teknik göstergelerin yanı sıra bu faktörleri de göz önünde bulundurmak gerekir.

Sonuç olarak, USD/JPY için 30 periyotluk hareketli ortalama genellikle kısa vadeli trend yönünü belirlemek ve alım/satım kararlarını desteklemek için kullanılabilir. Trendin yönüne ve fiyatın hareketli ortalamaya göre konumuna dikkat ederek, piyasa giriş ve çıkış noktalarını daha sağlıklı bir şekilde belirleyebilirsiniz.

[Long pozisyon nedir?](../forex/long.md)

[Short pozisyon nedir?](../forex/short.md)
