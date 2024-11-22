# **Risk oranı verilen bir pozisyon açamak için hesaplamalar - Modüler**

```csharp

    public static (string Message, decimal? StopLoss, decimal? TakeProfit) CalculateForexLevelsFromRatio(string accountType, decimal exchangeRate, decimal accountBalance, decimal riskAmountUSD, float riskRewardRatio, string positionType)
    {
        // Hesap türüne göre lot büyüklüğünü belirle
        decimal lotSize = accountType switch
        {
            "standart" => 100_000m,
            "mini" => 10_000m,
            "mikro" => 1_000m,
            _ => throw new ArgumentException("Geçersiz hesap türü.")
        };

        // Pip başına değer
        decimal pipValue = (0.0001m / exchangeRate) * lotSize;

        // Stop Loss pip sayısını hesapla
        decimal stopLossPips = riskAmountUSD / pipValue;

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
        return new(successMessage, stopLossLevel, takeProfitLevel);
    }


    public static (string Message, decimal? StopLoss, decimal? TakeProfit) CalculateForexLevelsFromAmount(string accountType, decimal exchangeRate, decimal accountBalance, decimal riskAmountUSD, float riskRewardRatio, string positionType)
    {
        // Hesap türüne göre lot büyüklüğünü belirle
        decimal lotSize = accountType switch
        {
            "standart" => 100_000m,
            "mini" => 10_000m,
            "mikro" => 1_000m,
            _ => throw new ArgumentException("Geçersiz hesap türü.")
        };

        // Pip başına değer
        decimal pipValue = (0.0001m / exchangeRate) * lotSize;

        // Stop Loss pip sayısını hesapla
        decimal stopLossPips = riskAmountUSD / pipValue;

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
        return new(successMessage, stopLossLevel, takeProfitLevel);
    }

    public static (string Message, decimal ProfitUSD, decimal LossUSD) CalculateProfitAndLoss(string accountType, decimal exchangeRate, decimal stopLossLevel, decimal takeProfitLevel, string positionType)
    {
        // Hesap türüne göre lot büyüklüğünü belirle
        decimal lotSize = accountType switch
        {
            "standart" => 100_000m,
            "mini" => 10_000m,
            "mikro" => 1_000m,
            _ => throw new ArgumentException("Geçersiz hesap türü.")
        };

        // Pip başına değer
        decimal pipValue = (0.0001m / exchangeRate) * lotSize;

        // Pip farklarını hesapla
        decimal pipDifferenceStopLoss = 0m;
        decimal pipDifferenceTakeProfit = 0m;

        if (positionType == "long")
        {
            pipDifferenceStopLoss = (exchangeRate - stopLossLevel) / 0.0001m; // Long pozisyonda zarar
            pipDifferenceTakeProfit = (takeProfitLevel - exchangeRate) / 0.0001m; // Long pozisyonda kâr
        }
        else if (positionType == "short")
        {
            pipDifferenceStopLoss = (stopLossLevel - exchangeRate) / 0.0001m; // Short pozisyonda zarar
            pipDifferenceTakeProfit = (exchangeRate - takeProfitLevel) / 0.0001m; // Short pozisyonda kâr
        }
        else
        {
            return ("Geçersiz pozisyon türü. 'long' veya 'short' olmalı.", 0, 0);
        }

        // USD bazında kâr ve zarar hesaplamaları
        decimal lossUSD = pipDifferenceStopLoss * pipValue;
        decimal profitUSD = pipDifferenceTakeProfit * pipValue;

        // Mesaj ve sonuçlar
        string message = "Kâr ve zarar hesaplama başarılı.";
        return new(message, profitUSD, lossUSD);
    }

```

---

## **Örnek Kullanımlar:**

### **Örnek 1: CalculateForexLevelsFromRatio**

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

        var result = ForexCalculator.CalculateForexLevelsFromRatio(accountType, exchangeRate, accountBalance, riskPercentage, riskRewardRatio, positionType);

        Console.WriteLine(result.Message);

        if (result.StopLoss.HasValue && result.TakeProfit.HasValue)
        {
            Console.WriteLine($"Account Type: {accountType}");
            Console.WriteLine($"Position Type: {positionType}");
            Console.WriteLine($"Stop Loss Seviyesi: {result.StopLoss.Value:F4}");
            Console.WriteLine($"Take Profit Seviyesi: {result.TakeProfit.Value:F4}");
        }

    }
}
```

**Çıktı:**

```result
Hesaplama basarili.
Account Type: mini
Position Type: short
Stop Loss Seviyesi: 1.0403
Take Profit Seviyesi: 1.0391
```

---

### **Örnek 2: CalculateForexLevelsFromAmount**

```csharp
class Program
{
    static void Main(string[] args)
    {
        accountType = "mini";
        exchangeRate = 0.58136M;
        accountBalance = 500m;
        decimal riskAmountUSD = 25m; // USD üzerinden risk miktarı
        riskRewardRatio = 3f;
        positionType = "long";

        result = ForexCalculator.CalculateForexLevelsFromAmount(accountType, exchangeRate, accountBalance, riskAmountUSD, riskRewardRatio, positionType);

        Console.WriteLine(result.Message);

        if (result.StopLoss.HasValue && result.TakeProfit.HasValue)
        {
            Console.WriteLine($"Account Type: {accountType}");
            Console.WriteLine($"Position Type: {positionType}");
            Console.WriteLine($"Stop Loss Seviyesi: {result.StopLoss.Value:F4}");
            Console.WriteLine($"Take Profit Seviyesi: {result.TakeProfit.Value:F4}");
        }
    }
}
```

**Çıktı:**

```result
Hesaplama basarili.
Account Type: mini
Position Type: long
Stop Loss Seviyesi: 0.5799
Take Profit Seviyesi: 0.5857
```

### **Örnek 3: CalculateProfitAndLoss**

```csharp
class Program
{
    static void Main(string[] args)
    {
        accountType = "mini";
        exchangeRate = 0.58179M;
        accountBalance = 500m;
        positionType = "long";
        decimal stopLossLevel = 0.57990M;
        decimal takeProfitLevel = 0.58416M;


        var result2 = ForexCalculator.CalculateProfitAndLoss(
            accountType: accountType,
            exchangeRate: exchangeRate,
            stopLossLevel: stopLossLevel,
            takeProfitLevel: takeProfitLevel,
            positionType: positionType
        );

        Console.WriteLine($"Message: {result2.Message}");
        Console.WriteLine($"Profit (USD): {result2.ProfitUSD:F2}");
        Console.WriteLine($"Loss (USD): {result2.LossUSD:F2}");
    }
}
```

**Çıktı:**

```result
Message: Kâr ve zarar hesaplama basarili.
Profit (USD): 40.74
Loss (USD): 32.49
```
