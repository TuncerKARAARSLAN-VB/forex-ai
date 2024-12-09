# EMA CROSS STRATEGY

![](./ema-cross-strategy/images/ema-cross.png)

Bu stratejide bir kaç kural yer almaktadır.

EMA20 ve EMA10 arsındaki kesişimler yakalanır.

```mql5

//+------------------------------------------------------------------+
//| Expert tick function                                            |
//+------------------------------------------------------------------+
void OnTick()
  {
   static datetime lastCheckTime = 0;
   if (TimeCurrent() - lastCheckTime >= 10) // Her 10 saniyede bir çalıştır
     {
      lastCheckTime = TimeCurrent();

      double ema10_prev = iMA(NULL, 0, 10, 0, MODE_EMA, PRICE_CLOSE, 1); // EMA10 önceki değer
      double ema20_prev = iMA(NULL, 0, 20, 0, MODE_EMA, PRICE_CLOSE, 1); // EMA20 önceki değer
      double ema10_current = iMA(NULL, 0, 10, 0, MODE_EMA, PRICE_CLOSE, 0); // EMA10 güncel değer
      double ema20_current = iMA(NULL, 0, 20, 0, MODE_EMA, PRICE_CLOSE, 0); // EMA20 güncel değer

      if (ema10_prev <= ema20_prev && ema10_current > ema20_current)
         {
          Print("Bullish Crossover: EMA10 crossed above EMA20.");
         }
      else if (ema10_prev >= ema20_prev && ema10_current < ema20_current)
         {
          Print("Bearish Crossover: EMA10 crossed below EMA20.");
         }
     }
  }

```

Açık pozisyon kontrolü

```mql5

bool CheckOpenPosition(string symbol)
  {
   for (int i = 0; i < PositionsTotal(); i++) // Açık pozisyonları kontrol et
     {
      ulong ticket = PositionGetTicket(i); // Pozisyon bileti al
      if (PositionSelectByTicket(ticket)) // Pozisyon bilgilerini al
        {
         string currentSymbol = PositionGetString(POSITION_SYMBOL); // Pozisyon sembolü al
         if (currentSymbol == symbol) // Belirtilen sembolün pozisyonu kontrolü
           {
            return true; // Açık pozisyon bulundu
           }
        }
     }
   return false; // Hiçbir açık pozisyon bulunamadı
  }

```

Pozisyonun açıldığı andan şu ana kadarki zaman içerisinde karın maximum değerinin hesaplanması

```mql5

//+------------------------------------------------------------------+
//| Pozisyonun açıldığı andaki değeri ve şu ana kadarki maksimum kar |
//+------------------------------------------------------------------+
double GetMaxProfitSinceOpen(string symbol)
  {
   double maxProfit = 0.0; // Maksimum kar değişkeni
   
   for (int i = 0; i < PositionsTotal(); i++) // Tüm açık pozisyonları kontrol et
     {
      ulong ticket = PositionGetTicket(i); // Pozisyon bileti al
      if (PositionSelectByTicket(ticket)) // Pozisyon bilgilerini yükle
        {
         string currentSymbol = PositionGetString(POSITION_SYMBOL); // Pozisyon sembolü
         if (currentSymbol == symbol) // İlgili sembol için pozisyon var mı?
           {
            double openPrice = PositionGetDouble(POSITION_PRICE_OPEN); // Pozisyon açılış fiyatı
            double lotSize = PositionGetDouble(POSITION_VOLUME); // Pozisyon hacmi
            double currentProfit = 0.0;

            // Mevcut piyasa fiyatına göre kar hesaplama
            if (PositionGetInteger(POSITION_TYPE) == POSITION_TYPE_BUY) // Eğer pozisyon BUY ise
               currentProfit = (SymbolInfoDouble(SYMBOL_BID) - openPrice) * lotSize * SymbolInfoDouble(SYMBOL_TRADE_TICK_VALUE);
            else if (PositionGetInteger(POSITION_TYPE) == POSITION_TYPE_SELL) // Eğer pozisyon SELL ise
               currentProfit = (openPrice - SymbolInfoDouble(SYMBOL_ASK)) * lotSize * SymbolInfoDouble(SYMBOL_TRADE_TICK_VALUE);

            if (currentProfit > maxProfit) // Maksimum karı güncelle
               maxProfit = currentProfit;
           }
        }
     }
   return maxProfit; // Maksimum kar değeri döndür
  }


```

Close Position

````mql5

//+------------------------------------------------------------------+
//| Pozisyon kapatma işlemi                                         |
//+------------------------------------------------------------------+
void ClosePosition(ulong ticket)
  {
   double lotSize = PositionGetDouble(POSITION_VOLUME); // Pozisyon hacmi al
   string symbol = PositionGetString(POSITION_SYMBOL); // Pozisyon sembolü
   if (OrderSend(symbol, ORDER_TYPE_SELL, lotSize, SymbolInfoDouble(SYMBOL_BID), 2, 0, 0, "Close Position", ticket))
      Print("Pozisyon kapatıldı: ", ticket);
   else
      Print("Pozisyon kapatılamadı: ", ticket, " Hata: ", GetLastError());
  }

```

Close position crossover

```mql5

void ClosePositionOnCrossover(string symbol, int emaFastPeriod, int emaSlowPeriod)
  {
   // EMA hesaplamaları
   double emaFastPrev = iMA(symbol, 0, emaFastPeriod, 0, MODE_EMA, PRICE_CLOSE, 1); // EMA Hızlı (önceki bar)
   double emaSlowPrev = iMA(symbol, 0, emaSlowPeriod, 0, MODE_EMA, PRICE_CLOSE, 1); // EMA Yavaş (önceki bar)
   double emaFastCurrent = iMA(symbol, 0, emaFastPeriod, 0, MODE_EMA, PRICE_CLOSE, 0); // EMA Hızlı (mevcut bar)
   double emaSlowCurrent = iMA(symbol, 0, emaSlowPeriod, 0, MODE_EMA, PRICE_CLOSE, 0); // EMA Yavaş (mevcut bar)

   // Açık pozisyonları kontrol et
   for (int i = 0; i < PositionsTotal(); i++)
     {
      ulong ticket = PositionGetTicket(i); // Pozisyon bileti al
      if (PositionSelectByTicket(ticket) && PositionGetString(POSITION_SYMBOL) == symbol)
        {
         int positionType = PositionGetInteger(POSITION_TYPE); // Pozisyon yönü (BUY veya SELL)

         // Yön kontrolü ve kesişim mantığı
         if (positionType == POSITION_TYPE_BUY && emaFastPrev > emaSlowPrev && emaFastCurrent < emaSlowCurrent)
           {
            // BUY pozisyon için kapanış sinyali
            ClosePosition(ticket);
           }
         else if (positionType == POSITION_TYPE_SELL && emaFastPrev < emaSlowPrev && emaFastCurrent > emaSlowCurrent)
           {
            // SELL pozisyon için kapanış sinyali
            ClosePosition(ticket);
           }
        }
     }
  }

```

Tam kod

```mql5

//+------------------------------------------------------------------+
//| EMA Kesişimine Dayalı Pozisyon Yönetimi                         |
//+------------------------------------------------------------------+
input double LotSize = 0.1;  // İşlem hacmi
input double MaxLoss = 5.0; // Maksimum izin verilen zarar ($)
input double LossThreshold = 30.0; // Maksimum karın yüzdesel düşüş eşiği

// Fonksiyon: EMA kesişimi kontrolü
int CheckEMACrossover(string symbol, int fastPeriod, int slowPeriod, ENUM_TIMEFRAMES timeframe)
  {
   double emaFastPrev = iMA(symbol, timeframe, fastPeriod, 0, MODE_EMA, PRICE_CLOSE, 1);
   double emaSlowPrev = iMA(symbol, timeframe, slowPeriod, 0, MODE_EMA, PRICE_CLOSE, 1);
   double emaFastCurrent = iMA(symbol, timeframe, fastPeriod, 0, MODE_EMA, PRICE_CLOSE, 0);
   double emaSlowCurrent = iMA(symbol, timeframe, slowPeriod, 0, MODE_EMA, PRICE_CLOSE, 0);

   if (emaFastPrev < emaSlowPrev && emaFastCurrent > emaSlowCurrent) return 1; // Yukarı yönlü kesişim
   if (emaFastPrev > emaSlowPrev && emaFastCurrent < emaSlowCurrent) return -1; // Aşağı yönlü kesişim
   return 0; // Kesişim yok
  }

// Fonksiyon: Açık pozisyon kontrolü
bool HasOpenPosition(string symbol)
  {
   for (int i = 0; i < PositionsTotal(); i++)
     {
      if (PositionSelectByIndex(i) && PositionGetString(POSITION_SYMBOL) == symbol)
         return true;
     }
   return false;
  }

// Fonksiyon: Pozisyon kapatma
bool ClosePosition(string symbol)
  {
   for (int i = 0; i < PositionsTotal(); i++)
     {
      if (PositionSelectByIndex(i) && PositionGetString(POSITION_SYMBOL) == symbol)
        {
         ulong ticket = PositionGetInteger(POSITION_TICKET);
         double lotSize = PositionGetDouble(POSITION_VOLUME);
         int positionType = PositionGetInteger(POSITION_TYPE);

         double closePrice = (positionType == POSITION_TYPE_BUY) ? SymbolInfoDouble(symbol, SYMBOL_BID) : SymbolInfoDouble(symbol, SYMBOL_ASK);
         return OrderSend(symbol, (positionType == POSITION_TYPE_BUY) ? ORDER_TYPE_SELL : ORDER_TYPE_BUY, lotSize, closePrice, 2, 0, 0, "Close", ticket);
        }
     }
   return false;
  }

// Fonksiyon: Açık pozisyonun kar/zarar kontrolü
void ManagePosition(string symbol)
  {
   for (int i = 0; i < PositionsTotal(); i++)
     {
      if (PositionSelectByIndex(i) && PositionGetString(POSITION_SYMBOL) == symbol)
        {
         ulong ticket = PositionGetInteger(POSITION_TICKET);
         int positionType = PositionGetInteger(POSITION_TYPE);
         double maxProfit = PositionGetDouble(POSITION_PROFIT); // Pozisyon kârı
         double openPrice = PositionGetDouble(POSITION_PRICE_OPEN);
         double lotSize = PositionGetDouble(POSITION_VOLUME);

         // Maksimum kar %30 düşerse kapat
         if (maxProfit > 0 && maxProfit * 0.7 > PositionGetDouble(POSITION_PROFIT))
           {
            Print("Kar %30 düştü, pozisyon kapatılıyor.");
            ClosePosition(symbol);
            return;
           }

         // Maksimum kayıp kontrolü
         if (PositionGetDouble(POSITION_PROFIT) < -MaxLoss)
           {
            Print("Maksimum zarar aşıldı, pozisyon kapatılıyor.");
            ClosePosition(symbol);
            return;
           }
        }
     }
  }

// Ana işlem fonksiyonu
void OnTick()
  {
   string symbol = "EURUSD";
   int fastPeriod = 10, slowPeriod = 20;
   ENUM_TIMEFRAMES timeframe = PERIOD_M5;

   // Kesişim kontrolü
   int crossoverSignal = CheckEMACrossover(symbol, fastPeriod, slowPeriod, timeframe);

   // Açık pozisyon yoksa ve kesişim sinyali varsa pozisyon aç
   if (!HasOpenPosition(symbol) && crossoverSignal != 0)
     {
      double price = (crossoverSignal == 1) ? SymbolInfoDouble(symbol, SYMBOL_ASK) : SymbolInfoDouble(symbol, SYMBOL_BID);
      int orderType = (crossoverSignal == 1) ? ORDER_TYPE_BUY : ORDER_TYPE_SELL;

      if (OrderSend(symbol, orderType, LotSize, price, 2, 0, 0, "EMA Crossover Signal"))
         Print("Yeni pozisyon açıldı: ", (crossoverSignal == 1) ? "BUY" : "SELL");
     }

   // Açık pozisyon varsa yönet
   if (HasOpenPosition(symbol))
      ManagePosition(symbol);

   // Yeni kesişimde pozisyon kapat
   if (crossoverSignal != 0)
      ClosePosition(symbol);
  }

```


```mql5

//+------------------------------------------------------------------+
//| Expert initialization function                                  |
//+------------------------------------------------------------------+
input double LotSize = 0.1; // İşlem hacmi
input double MaxLossUSD = 5.0; // Maksimum kabul edilebilir zarar
string Symbol = "EURUSD"; // İşlem yapılacak sembol
int FastEMA = 10; // Hızlı EMA
int SlowEMA = 20; // Yavaş EMA

double maxProfit = 0.0; // Maksimum kâr
datetime lastCheckTime = 0; // Son kontrol zamanı

//+------------------------------------------------------------------+
//| Expert tick function                                            |
//+------------------------------------------------------------------+
void OnTick()
  {
   if (TimeCurrent() - lastCheckTime >= 10) // Her 10 saniyede bir çalıştır
     {
      lastCheckTime = TimeCurrent();

      double emaFastPrev = iMA(Symbol, PERIOD_M5, FastEMA, 0, MODE_EMA, PRICE_CLOSE, 1); // EMA hızlı (önceki)
      double emaSlowPrev = iMA(Symbol, PERIOD_M5, SlowEMA, 0, MODE_EMA, PRICE_CLOSE, 1); // EMA yavaş (önceki)
      double emaFastCurrent = iMA(Symbol, PERIOD_M5, FastEMA, 0, MODE_EMA, PRICE_CLOSE, 0); // EMA hızlı (mevcut)
      double emaSlowCurrent = iMA(Symbol, PERIOD_M5, SlowEMA, 0, MODE_EMA, PRICE_CLOSE, 0); // EMA yavaş (mevcut)

      // Pozisyon kontrol
      if (!CheckOpenPosition(Symbol)) // Açık pozisyon yoksa
        {
         if (emaFastPrev <= emaSlowPrev && emaFastCurrent > emaSlowCurrent)
            OpenPosition(Symbol, POSITION_TYPE_BUY);
         else if (emaFastPrev >= emaSlowPrev && emaFastCurrent < emaSlowCurrent)
            OpenPosition(Symbol, POSITION_TYPE_SELL);
        }
      else // Açık pozisyon varsa yönetim
        {
         ManagePosition(Symbol, emaFastPrev, emaSlowPrev, emaFastCurrent, emaSlowCurrent);
        }
     }
  }

//+------------------------------------------------------------------+
//| Açık pozisyon kontrol fonksiyonu                                |
//+------------------------------------------------------------------+
bool CheckOpenPosition(string symbol)
  {
   for (int i = 0; i < PositionsTotal(); i++)
     {
      if (PositionSelectByIndex(i) && PositionGetString(POSITION_SYMBOL) == symbol)
        return true;
     }
   return false;
  }

//+------------------------------------------------------------------+
//| Pozisyon açma fonksiyonu                                        |
//+------------------------------------------------------------------+
void OpenPosition(string symbol, int positionType)
  {
   double price = positionType == POSITION_TYPE_BUY ? SymbolInfoDouble(symbol, SYMBOL_ASK) : SymbolInfoDouble(symbol, SYMBOL_BID);
   OrderSend(symbol, positionType, LotSize, price, 2, 0, 0, "EMA Cross Position");
   Print("Yeni pozisyon açıldı: ", positionType == POSITION_TYPE_BUY ? "BUY" : "SELL");
  }

//+------------------------------------------------------------------+
//| Pozisyon yönetim fonksiyonu                                     |
//+------------------------------------------------------------------+
void ManagePosition(string symbol, double emaFastPrev, double emaSlowPrev, double emaFastCurrent, double emaSlowCurrent)
  {
   for (int i = 0; i < PositionsTotal(); i++)
     {
      if (PositionSelectByIndex(i) && PositionGetString(POSITION_SYMBOL) == symbol)
        {
         ulong ticket = PositionGetTicket(i);
         double profit = PositionGetDouble(POSITION_PROFIT);
         double openPrice = PositionGetDouble(POSITION_PRICE_OPEN);
         int positionType = PositionGetInteger(POSITION_TYPE);

         // Maksimum kâr güncellemesi
         if (profit > maxProfit)
            maxProfit = profit;

         // Kar kaybı kontrolü
         if (profit < maxProfit * 0.7)
           {
            ClosePosition(ticket);
            Print("Kâr kaybı önlemek için pozisyon kapatıldı.");
            return;
           }

         // EMA kesişimi durumunda pozisyon kapatma
         if ((positionType == POSITION_TYPE_BUY && emaFastPrev > emaSlowPrev && emaFastCurrent < emaSlowCurrent) ||
             (positionType == POSITION_TYPE_SELL && emaFastPrev < emaSlowPrev && emaFastCurrent > emaSlowCurrent))
           {
            ClosePosition(ticket);
            Print("Yeni EMA kesişimi nedeniyle pozisyon kapatıldı.");
            return;
           }

         // Zarar kontrolü
         if (profit < -MaxLossUSD)
           {
            ClosePosition(ticket);
            Print("Zarar limiti aşıldı, pozisyon kapatıldı.");
            return;
           }
        }
     }
  }

//+------------------------------------------------------------------+
//| Pozisyon kapatma fonksiyonu                                     |
//+------------------------------------------------------------------+
void ClosePosition(ulong ticket)
  {
   double lotSize = PositionGetDouble(POSITION_VOLUME);
   string symbol = PositionGetString(POSITION_SYMBOL);
   int positionType = PositionGetInteger(POSITION_TYPE);
   double price = positionType == POSITION_TYPE_BUY ? SymbolInfoDouble(symbol, SYMBOL_BID) : SymbolInfoDouble(symbol, SYMBOL_ASK);

   if (OrderSend(symbol, positionType == POSITION_TYPE_BUY ? ORDER_TYPE_SELL : ORDER_TYPE_BUY, lotSize, price, 2, 0, 0, "Close Position", ticket))
      Print("Pozisyon kapatıldı: ", ticket);
   else
      Print("Pozisyon kapatılamadı: ", ticket, " Hata: ", GetLastError());
  }

```