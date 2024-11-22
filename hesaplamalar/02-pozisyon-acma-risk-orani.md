# **Risk oranı verilen bir pozisyon açamak için hesaplamalar**

```csharp

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

public static class ForexCalculator
{
    /// <summary>
    /// %X zarar kabul edildiğinde, stoploss ve takeprofit bigileri hesaplanıp gönderilir.
    /// </summary>
    /// <param name="accountType"></param>
    /// <param name="exchangeRate"></param>
    /// <param name="accountBalance"></param>
    /// <param name="riskAmountUSD"></param>
    /// <param name="riskRewardRatio"></param>
    /// <param name="positionType"></param>
    /// <returns></returns>
    /// <exception cref="ArgumentException"></exception>
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

    /// <summary>
    /// X birim (USD TRY JPY) zarar kabul edildiğinde, stoploss ve takeprofit bilgileri hesaplanıp gönderir.
    /// </summary>
    /// <param name="accountType"></param>
    /// <param name="exchangeRate"></param>
    /// <param name="accountBalance"></param>
    /// <param name="riskAmountUSD"></param>
    /// <param name="riskRewardRatio"></param>
    /// <param name="positionType"></param>
    /// <returns></returns>
    /// <exception cref="ArgumentException"></exception>
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

    /// <summary>
    /// Stoploss ve takeprofit bilgileri verildiğinde, elde edilecek kar ve zarar tutarları hesaplanıp gönderilir.
    /// </summary>
    /// <param name="accountType"></param>
    /// <param name="exchangeRate"></param>
    /// <param name="stopLossLevel"></param>
    /// <param name="takeProfitLevel"></param>
    /// <param name="positionType"></param>
    /// <returns></returns>
    /// <exception cref="ArgumentException"></exception>
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

    /// <summary>
    /// Eğer girmek istediğim bir pozisyon varsa ve tahmin ettiğim bir stoploss pozisyonu tayin ettiysem, 
    /// bu aralıkda ne kadar zararı kabul ettiğini belirttiğinde girmen gereken lot büyüklüğünü hesaplayıp gönderir.
    /// 
    /// Örneğin EURUSD LONG pozisyon için giriş noktası ve stoploss noktasına karar verelim.
    /// Bu pozisyonda max 30 dolar zarar kabul ediyorsanız, pozisyon için girilmesi gereken lot miktarı hesaplanıp gönderilecektir.
    /// </summary>
    /// <param name="accountType"></param>
    /// <param name="exchangeRate"></param>
    /// <param name="stopLossLevel"></param>
    /// <param name="riskAmountUSD"></param>
    /// <param name="positionType"></param>
    /// <returns></returns>
    /// <exception cref="ArgumentException"></exception>
    public static (string Message, decimal LotAmount) CalculateLotAmountWithPositionType(string accountType, decimal exchangeRate, decimal stopLossLevel, decimal riskAmountUSD, string positionType)
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
        decimal pipValuePerLot = (0.0001m / exchangeRate) * lotSize;

        // Pozisyon türüne göre pip farkını hesapla
        decimal pipDifference = positionType.ToLower() switch
        {
            "long" => (exchangeRate - stopLossLevel) / 0.0001m,
            "short" => (stopLossLevel - exchangeRate) / 0.0001m,
            _ => throw new ArgumentException("Geçersiz pozisyon türü. 'long' veya 'short' olmalıdır.")
        };

        // Pip farkı negatifse hata döndür
        if (pipDifference <= 0)
        {
            return ("Stop Loss seviyesi yanlış pozisyon türüyle uyumsuz.", 0m);
        }

        // Lot miktarını hesapla
        decimal lotAmount = riskAmountUSD / (pipDifference * pipValuePerLot);

        // Sonuç döndür
        string message = lotAmount > 0
            ? "Lot miktarı hesaplama başarılı."
            : "Hata: Lot miktarı hesaplanamadı.";

        return new(message, lotAmount);
    }

}


```
