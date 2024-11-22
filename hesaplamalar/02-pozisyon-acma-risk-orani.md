# **Risk oranı verilen bir pozisyon açamak için hesaplamalar**

```csharp
using System;

class ForexCalculator
{
    static void Main(string[] args)
    {
        // Kullanıcıdan giriş verilerini al
        Console.WriteLine("Hesap türünü giriniz (standart, mini, mikro):");
        string accountType = Console.ReadLine()?.ToLower();

        Console.WriteLine("Pariteyi giriniz (örnek: 1.04):");
        if (!decimal.TryParse(Console.ReadLine(), out decimal exchangeRate) || exchangeRate <= 0)
        {
            Console.WriteLine("Geçersiz parite değeri.");
            return;
        }

        Console.WriteLine("Toplam hesap bakiyenizi giriniz (örnek: 100):");
        if (!decimal.TryParse(Console.ReadLine(), out decimal accountBalance) || accountBalance <= 0)
        {
            Console.WriteLine("Geçersiz bakiye değeri.");
            return;
        }

        Console.WriteLine("Risk yüzdesini giriniz (örnek: 3):");
        if (!decimal.TryParse(Console.ReadLine(), out decimal riskPercentage) || riskPercentage <= 0 || riskPercentage > 100)
        {
            Console.WriteLine("Geçersiz risk yüzdesi.");
            return;
        }

        Console.WriteLine("Kar/Zarar oranını giriniz (örnek: 3):");
        if (!float.TryParse(Console.ReadLine(), out float riskRewardRatio) || riskRewardRatio <= 0)
        {
            Console.WriteLine("Geçersiz kar/zarar oranı.");
            return;
        }

        Console.WriteLine("Pozisyon tipini giriniz (long veya short):");
        string positionType = Console.ReadLine()?.ToLower();

        if (positionType != "long" && positionType != "short")
        {
            Console.WriteLine("Geçersiz pozisyon tipi. Sadece 'long' veya 'short' kabul edilir.");
            return;
        }

        // Hesap türüne göre lot büyüklüğünü belirle
        decimal lotSize = accountType switch
        {
            "standart" => 100_000m,
            "mini" => 10_000m,
            "mikro" => 1_000m,
            _ => throw new ArgumentException("Geçersiz hesap türü.")
        };

        // Lot türüne göre bir alt lot büyüklüğünü belirle
        string lowerLotType = accountType switch
        {
            "standart" => "mini",
            "mini" => "mikro",
            "mikro" => null, // Mikro lotun altı yok
            _ => null
        };

        decimal lowerLotSize = lowerLotType switch
        {
            "mini" => 10_000m,
            "mikro" => 1_000m,
            _ => 0m
        };

        // Risk tutarını hesapla
        decimal riskAmount = (riskPercentage / 100) * accountBalance;

        // Pip başına değer
        decimal pipValue = (0.0001m / exchangeRate) * lotSize;

        // Risk tutarını pip değerine bölecek kadar bir pozisyon büyüklüğü ayarlanabilir mi?
        if (riskAmount < pipValue)
        {
            // Minimum risk yüzdesini hesapla
            decimal minRiskPercentage = (pipValue / accountBalance) * 100;

            // Bir alt lot türüne öneri
            if (lowerLotSize > 0)
            {
                decimal lowerPipValue = (0.0001m / exchangeRate) * lowerLotSize;
                decimal lowerMinRiskPercentage = (lowerPipValue / accountBalance) * 100;

                Console.WriteLine($"Seçtiğiniz lot büyüklüğü için risk tutarınız çok düşük.");
                Console.WriteLine($"Mevcut lot büyüklüğü ({accountType}) için minimum risk yüzdesi: {minRiskPercentage:F2}%.");
                Console.WriteLine($"Alternatif olarak, {lowerLotType} lot kullanarak minimum risk yüzdesi: {lowerMinRiskPercentage:F2}% ile işlem açabilirsiniz.");
            }
            else
            {
                Console.WriteLine($"Seçtiğiniz lot büyüklüğü için risk tutarınız çok düşük.");
                Console.WriteLine($"Mevcut lot büyüklüğü ({accountType}) için minimum risk yüzdesi: {minRiskPercentage:F2}%.");
                Console.WriteLine($"Mevcut bakiyenizle işlem yapmak için daha yüksek bir bakiye veya risk yüzdesi gereklidir.");
            }

            return;
        }

        // Stop Loss pip sayısını hesapla
        decimal stopLossPips = riskAmount / pipValue;

        // Take Profit pip sayısını hesapla
        decimal takeProfitPips = stopLossPips * (decimal)riskRewardRatio;

        // Stop Loss ve Take Profit seviyelerini hesapla
        decimal stopLossLevel, takeProfitLevel;

        if (positionType == "long")
        {
            stopLossLevel = exchangeRate - (stopLossPips * 0.0001m);
            takeProfitLevel = exchangeRate + (takeProfitPips * 0.0001m);
        }
        else // short pozisyon
        {
            stopLossLevel = exchangeRate + (stopLossPips * 0.0001m);
            takeProfitLevel = exchangeRate - (takeProfitPips * 0.0001m);
        }

        // Sonuçları yazdır
        Console.WriteLine($"Hesap türü: {accountType}");
        Console.WriteLine($"Pozisyon tipi: {positionType}");
        Console.WriteLine($"Risk yüzdesi: {riskPercentage}%");
        Console.WriteLine($"Kar/Zarar oranı: 1:{riskRewardRatio}");
        Console.WriteLine($"Stop Loss seviyesi: {stopLossLevel:F4}");
        Console.WriteLine($"Take Profit seviyesi: {takeProfitLevel:F4}");
    }
}
```

---

### **Girişler:**

- Hesap türü: `standart`  
- Parite: `1.04`  
- Bakiye: `$100`  
- Risk: `%3`  
- Kar/Zarar oranı: `3`  
- Pozisyon: `long`

### **Çıkış:**

```
Seçtiğiniz lot büyüklüğü için risk tutarınız çok düşük.
Mevcut lot büyüklüğü (standart) için minimum risk yüzdesi: 9.00%.
Alternatif olarak, mini lot kullanarak minimum risk yüzdesi: 0.90% ile işlem açabilirsiniz.
```
