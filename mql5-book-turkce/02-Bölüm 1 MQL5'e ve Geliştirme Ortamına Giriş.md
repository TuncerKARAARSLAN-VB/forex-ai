# Bölüm 1: MQL5'e ve Geliştirme Ortamına Giriş  

MetaTrader 5’te MQL5'in yeniden canlandırılmasında en önemli değişikliklerden biri, **nesne yönelimli programlama (OOP)** kavramını desteklemesidir. MQL4 (MetaTrader 4'ün dili) çıktığı dönemde genellikle C programlama diliyle kıyaslanırken, MQL5'i C++ ile karşılaştırmak daha doğru bir yaklaşımdır. Adil olmak gerekirse, başlangıçta yalnızca MQL5'te bulunan tüm OOP araçlarının bugün MQL4'e de aktarıldığını belirtmek gerekir. Ancak, programlama bilgisi az olan kullanıcılar hala OOP'yi çok karmaşık bir konsept olarak algılamaktadır.  

Bu kitap, karmaşık şeyleri basitleştirmeyi amaçlamaktadır. MQL5 terminali ile birlikte sunulan ve mql5.com web sitesinde de mevcut olan **MQL5 Dil Referansı**nın yerini almak yerine, ona ek olarak kullanılması hedeflenmiştir.  

Bu kitapta, **MQL5 programlamanın tüm bileşenlerini ve tekniklerini** adım adım açıklayacağız. Böylece her aşama net olacak ve OOP teknolojisi, güçlü bir araç olarak düzgün ve mantıklı bir şekilde kullanıldığında potansiyelini kademeli olarak açığa çıkaracaktır. Bunun sonucunda, MQL programlarının geliştiricileri, belirli bir göreve uygun bir programlama stilini seçebileceklerdir. Yani sadece nesne yönelimli değil, aynı zamanda "eski" prosedürel yöntemi de tercih edebilir ve bunların çeşitli kombinasyonlarını kullanabilirler.  

---

## Kullanıcı Profilleri: Programcılar ve Programcı Olmayanlar  

Ticaret terminali kullanıcıları iki gruba ayrılabilir:  

1. **Programcılar**: En az bir dilde programlama deneyimi olan kişiler.  
2. **Programcı Olmayanlar**: Terminalin MQL5 kullanarak özelleştirilmesiyle ilgilenen "saf" traderlar.  

Programcılar, kitabın ilk iki bölümünü atlayarak doğrudan MetaTrader 5'e yerleştirilmiş **API'lere (Uygulama Programlama Arayüzleri)** geçebilir. Programcı olmayanlar için kitabı kademeli bir şekilde okumaları önerilir.  

C++ bilen programcılar, MQL5 ile çalışmaya başlarken önemli bir avantaja sahiptir. Bununla birlikte, bu avantajın bir dezavantajı da vardır: MQL5, C++ ile tamamen uyumlu değildir (özellikle son standartlarla kıyaslandığında). Bu nedenle, alışkanlıkla "C++ gibi" bir yapı yazmaya çalışmak, genellikle beklenmeyen derleyici hatalarıyla sonuçlanabilir. Bu kitapta, dilin belirli unsurlarını ele alırken bu farklılıklara dikkat çekmeye çalışacağız.  

---

## MQL5 Programlarının Fonksiyonları ve Tipleri  

MQL5, kullanıcı arayüzü üzerinden veya yerleşik yazılım araçları aracılığıyla teknik analiz yapma, ticaret emirlerini yürütme veya harici veri kaynaklarıyla entegrasyon gibi birçok işlevi destekler.  

MQL5 programlarının farklı işlevleri yerine getirmesi gerektiğinden, MetaTrader 5’te bazı **özel program türleri** desteklenmektedir. Bu, birçok yazılım sisteminde standart bir tekniktir. Örneğin, Windows'ta, genellikle pencere tabanlı programların yanı sıra komut satırıyla çalışan programlar ve hizmetler de bulunur.  

MetaTrader 5'te de benzer bir yaklaşım benimsenmiştir. Bu yapı, her bir program türünün belirli görevler için optimize edilmesini sağlar ve platformun esnekliğini artırır.
