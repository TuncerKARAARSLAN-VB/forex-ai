# **Risk oranı verilen bir pozisyon açamak için hesaplamalar - Modüler**

```csharp
using System;

class ForexCalculator
{
    // Custom struct dönemi - Hesaplama sonuçları ve mesajlar için
    public struct ForexCalculationResult
    {
        public string Message { get; set; }
        public decimal? StopLoss { get; set; }
        public decimal? TakeProfit { get; set; }

        public ForexCalculationResult(string message, decimal? stopLoss, decimal? takeProfit)
        {
            Message = message;
            StopLoss = stopLoss;
            TakeProfit = takeProfit;
        }
    }

    // Forex hesaplama fonksiyonu
    public static ForexCalculationResult 
    CalculateForexLevels(string accountType, decimal exchangeRate, decimal accountBalance, 
                         decimal riskPercentage, float riskRewardRatio, string positionType)
    {
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

                string message = $"Seçtiğiniz lot büyüklüğü için risk tutarınız çok düşük.\n" +
                                 $"Mevcut lot büyüklüğü ({accountType}) için minimum risk yüzdesi: {minRiskPercentage:F2}%.\n" +
                                 $"Alternatif olarak, {lowerLotType} lot kullanarak minimum risk yüzdesi: {lowerMinRiskPercentage:F2}% ile işlem açabilirsiniz.";

                return new ForexCalculationResult(message, null, null);
            }
            else
            {
                string message = $"Seçtiğiniz lot büyüklüğü için risk tutarınız çok düşük.\n" +
                                 $"Mevcut lot büyüklüğü ({accountType}) için minimum risk yüzdesi: {minRiskPercentage:F2}%.\n" +
                                 $"Mevcut bakiyenizle işlem yapmak için daha yüksek bir bakiye veya risk yüzdesi gereklidir.";

                return new ForexCalculationResult(message, null, null);
            }
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

        string successMessage = "Hesaplama başarılı.";
        return new ForexCalculationResult(successMessage, stopLossLevel, takeProfitLevel);
    }
}
```

---

## **Örnek Kullanımlar:**

### **Örnek 1:**

```csharp
class Program
{
    static void Main(string[] args)
    {
        string accountType = "mini";
        decimal exchangeRate = 1.04m;
        decimal accountBalance = 100m;
        decimal riskPercentage = 3m;
        float riskRewardRatio = 3f;
        string positionType = "long";

        var result = ForexCalculator.CalculateForexLevels(accountType, exchangeRate, accountBalance, riskPercentage, riskRewardRatio, positionType);

        Console.WriteLine(result.Message);
        if (result.StopLoss.HasValue && result.TakeProfit.HasValue)
        {
            Console.WriteLine($"Stop Loss Seviyesi: {result.StopLoss.Value:F4}");
            Console.WriteLine($"Take Profit Seviyesi: {result.TakeProfit.Value:F4}");
        }
    }
}
```

**Çıktı:**

```result
Hesaplama basarili.
Stop Loss Seviyesi: 1.0397
Take Profit Seviyesi: 1.0409
```

---

### **Örnek 2: Yetersiz Risk**

```csharp
class Program
{
    static void Main(string[] args)
    {
        string accountType = "standart";
        decimal exchangeRate = 1.04m;
        decimal accountBalance = 100m;
        decimal riskPercentage = 3m;
        float riskRewardRatio = 3f;
        string positionType = "short";

        var result = ForexCalculator.CalculateForexLevels(accountType, exchangeRate, accountBalance, riskPercentage, riskRewardRatio, positionType);

        Console.WriteLine(result.Message);
    }
}
```

**Çıktı:**

```result
Seçtiginiz lot büyüklügü için risk tutariniz çok düsük.
Mevcut lot büyüklügü (standart) için minimum risk yüzdesi: 9.62%.
Alternatif olarak, mini lot kullanarak minimum risk yüzdesi: 0.96% ile islem açabilirsiniz.
```

### **Örnek 3:**

```csharp
class Program
{
    static void Main(string[] args)
    {
        string accountType = "mini";
        decimal exchangeRate = 1.04m;
        decimal accountBalance = 100m;
        decimal riskPercentage = 3m;
        float riskRewardRatio = 3f;
        string positionType = "short";

        var result = ForexCalculator.CalculateForexLevels(accountType, exchangeRate, accountBalance, riskPercentage, riskRewardRatio, positionType);

        Console.WriteLine(result.Message);
    }
}
```

**Çıktı:**

```result
Hesaplama basarili.
Stop Loss Seviyesi: 1.0403
Take Profit Seviyesi: 1.0391
```

## **Main** bloğundaki değerlere göre adım adım yapılan hesaplama

### 1. **Hesap Türüne Göre Lot Büyüklüğü Belirleme**

Verilen değerler:

- `accountType = "mini"`: Hesap türü **mini**.

Bu durumda, **mini** hesap türü için lot büyüklüğü:

- `lotSize = 10,000` birim (yani 10,000 birimlik işlem büyüklüğü seçilir).

### 2. **Risk Tutarı Hesaplama**

Verilen değerler:

- `accountBalance = 100m`: Hesap bakiyesi **100 USD**.
- `riskPercentage = 3m`: Risk yüzdesi **%3**.

**Risk tutarı**, hesap bakiyesi ve risk yüzdesi ile hesaplanır:

\[
\text{Risk Amount} = \left(\frac{\text{riskPercentage}}{100}\right) \times \text{accountBalance}
\]
\[
\text{Risk Amount} = \left(\frac{3}{100}\right) \times 100 = 3 \, \text{USD}
\]

Yani, işlem başına riske edilecek miktar **3 USD**.

## 3. **Pip Değeri Hesaplama**

Verilen değerler:

- `exchangeRate = 1.04`: Döviz kuru **1.04**.

**Pip değeri**, lot büyüklüğü ve döviz kuru kullanılarak hesaplanır. Forex piyasasında pip değeri genellikle şu formülle hesaplanır:
\[
\text{Pip Value} = \left(\frac{0.0001}{\text{exchangeRate}}\right) \times \text{lotSize}
\]
\[
\text{Pip Value} = \left(\frac{0.0001}{1.04}\right) \times 10,000 = 0.009615 \, \text{USD}
\]
Bu, **1 pip** değerinin **0.0096 USD** olduğu anlamına gelir.

### 4. **Risk Tutarı ile Pip Değerini Karşılaştırma**

- Eğer **riskAmount** (3 USD) **pipValue** (0.0096 USD) değerine bölünürse, kaç pip risk alınacağını hesaplayabiliriz:
\[
\text{Stop Loss Pips} = \frac{\text{Risk Amount}}{\text{Pip Value}} = \frac{3}{0.009615} = 312.5 \, \text{pips}
\]
Bu durumda, **stop loss** için alınacak risk **312.5 pip**.

### 5. **Take Profit Hesaplama**

Verilen değer:

- `riskRewardRatio = 3f`: Risk-ödül oranı **3**.

**Take Profit** pip sayısı, **stop loss** pip sayısının risk-ödül oranı ile çarpılmasıyla hesaplanır:
\[
\text{Take Profit Pips} = \text{Stop Loss Pips} \times \text{Risk Reward Ratio}
\]
\[
\text{Take Profit Pips} = 312.5 \times 3 = 937.5 \, \text{pips}
\]
Bu durumda, **take profit** seviyesi için hedeflenen pip sayısı **937.5 pip**.

### 6. **Stop Loss ve Take Profit Seviyelerinin Hesaplanması**

**Short pozisyon** için:

- **Stop Loss**: Giriş fiyatının üzerine doğru bir hareketle, **312.5 pip**'lik bir kaybı kabul edeceğiz.
- **Take Profit**: Giriş fiyatının altına doğru bir hareketle, **937.5 pip**'lik bir karı hedefleyeceğiz.

**Stop Loss Seviyesi**:
\[
\text{Stop Loss Level} = \text{Exchange Rate} + (312.5 \times 0.0001) = 1.04 + 0.03125 = 1.07125
\]

**Take Profit Seviyesi**:
\[
\text{Take Profit Level} = \text{Exchange Rate} - (937.5 \times 0.0001) = 1.04 - 0.09375 = 0.94625
\]

## Sonuçlar

**Hesaplama başarılı** mesajı ile birlikte hesaplanan seviyeler:
- **Stop Loss Seviyesi**: 1.0713
- **Take Profit Seviyesi**: 0.9463

Bu sonuçlar, **mini** hesap türü ve **short pozisyon** için belirlenen risk yüzdesi, döviz kuru, ve risk-ödül oranına göre hesaplanan **stop loss** ve **take profit** seviyeleridir.