# MQL5'te Mevcut Program Türleri  

MQL5'te dört ana program türü bulunmaktadır:  

1. **Göstergeler (Indicators):**  
   Belirli bir formüle dayalı olarak hesaplanan veri dizilerini grafiksel olarak gösteren programlardır. Genellikle fiyat serilerine dayanır.  

2. **Uzman Danışmanlar (Expert Advisors):**  
   Ticaret işlemlerini tamamen veya kısmen otomatikleştiren programlardır.  

3. **Skriptler (Scripts):**  
   Tek seferde bir işlem gerçekleştirmek için tasarlanmış programlardır.  

4. **Servisler (Services):**  
   Arka planda sürekli çalışan programlardır ve grafiklere bağlı olmadan çalışabilirler.  

Bu türlerin her birinin amacı ve özel özellikleri ilerleyen bölümlerde ayrıntılı olarak ele alınacaktır. Şu anda önemli olan, bu programların hepsinin **MQL5 diliyle** yazıldığını ve birçok ortak özelliğe sahip olduğunu bilmek. Bu nedenle, öncelikle ortak özelliklerle başlayıp, her bir türün kendine has yönlerini kademeli olarak öğreneceğiz.  

---

## MetaTrader 5'te Teknik Özellikler  

MetaTrader 5'in temel teknik özelliği, tüm kontrolün **istemci terminalinde** yapılmasıdır. Terminalde başlatılan komutlar sunucuya iletilir.  

- MQL5 tabanlı uygulamalar yalnızca istemci terminalinde çalışır.  
- Çoğu program, düzgün çalışmak için canlı bir sunucu bağlantısına ihtiyaç duyar.  
- Hiçbir uygulama sunucuya yüklenmez. Sunucu yalnızca istemci terminalinden alınan emirleri işler ve ticaret ortamındaki değişiklikleri döner. Bu değişiklikler MQL5 programlarına da erişilebilir hale gelir.  

---

## Programların Grafik Bağlamında Çalışması  

Çoğu MQL5 programı, **grafik bağlamında** çalışır. Yani bir programı başlatmak için, onu istenilen grafiğe "sürükleyip bırakmanız" gerekir.  
Bunun tek istisnası, arka planda çalışan ve grafiklere bağlı olmayan **servis türü programlardır**.  

---

## Dosya Yapısı ve Çalışma Klasörleri  

Tüm MQL5 programları, MetaTrader 5 çalışma klasörünün içindeki **/MQL5/<tür>** klasörlerinde saklanır. Buradaki `<tür>`, program türünü ifade eder:  

- **Indicators** (Göstergeler)  
- **Experts** (Uzman Danışmanlar)  
- **Scripts** (Skriptler)  
- **Services** (Servisler)  

MetaTrader 5'in kurulum şekline bağlı olarak, çalışma klasörünün yolu farklılık gösterebilir. Örneğin:  

- **C:/Program Files/MetaTrader 5/**  
- **C:/Users/<kullanıcı_adı>/AppData/Roaming/MetaQuotes/Terminal/<instance_id>/**  

**Dosya -> Veri Kataloğunu Aç (File -> Open data catalog)** komutunu çalıştırarak bu klasörün tam konumu öğrenilebilir. Bu komut hem terminalde hem de düzenleyicide mevcuttur.  

---

## Yeni Program Oluşturma  

Yeni bir program oluştururken doğru klasörü aramakla uğraşmanıza gerek yoktur. **MetaEditor'de yerleşik olarak bulunan MQL Sihirbazı** (MQL Wizard), bu işlemi kolaylaştırır.  

- **Dosya -> Yeni (File -> New)** komutuyla MQL Sihirbazı açılır.  
- İlgili program türü seçildikten sonra gerekli kaynak kod şablonunu içeren bir metin dosyası otomatik olarak oluşturulur ve düzenleme için açılır.  

---

## MQL5 Klasör Yapısındaki Diğer Alt Klasörler  

**MQL5 klasöründe**, yukarıda bahsedilen türlerin yanında başka alt klasörler de bulunur. Bunlar da MQL5 programlamasıyla doğrudan ilgilidir, ancak detaylarına ilerleyen bölümlerde değinilecektir.  
