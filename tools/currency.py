"""
currency.py - Döviz Kuru Aracı
==============================
Görev: İREM
Branch: feature/tools-currency
Durum: YAPILACAK

Bu dosya ExchangeRate API'den döviz kuru bilgisi çeker ve çevirir.
Agent "100 dolar kaç TL?" gibi sorularda bu aracı kullanır.

API BİLGİLERİ:
- API: https://www.exchangerate-api.com/ (ücretsiz, key gerektirmez)
- Endpoint: https://api.exchangerate-api.com/v4/latest/{CURRENCY}
- Örnek: https://api.exchangerate-api.com/v4/latest/USD

YAPILACAKLAR:
1. get_exchange_rate() fonksiyonunu tamamla
2. API çağrısını yaz
3. Para birimi çevirisini hesapla
4. Hata yönetimini ekle

TEST:
    python -c "from tools.currency import get_exchange_rate; print(get_exchange_rate('USD', 'TRY', 100))"

İPUÇLARI:
- Para birimi kodları: USD, EUR, TRY, GBP vs. (3 harfli ISO kodları)
- API key gerekmez, direkt çağrılabilir
- Sonucu 2 ondalık basamağa yuvarla
"""

import requests
from config import EXCHANGERATE_BASE_URL


def get_exchange_rate(from_currency: str, to_currency: str, amount: float) -> dict:
    """
    Bir para birimini diğerine çevirir.
    
    Bu fonksiyon ExchangeRate API'yi kullanarak güncel döviz
    kurunu çeker ve belirtilen miktarı çevirir.
    
    Args:
        from_currency: Kaynak para birimi kodu (örn: "USD", "EUR")
        to_currency: Hedef para birimi kodu (örn: "TRY", "GBP")
        amount: Çevrilecek miktar (örn: 100)
    
    Returns:
        dict: Çevirim sonucu içeren sözlük
            {
                "success": True/False,
                "from_currency": "USD",
                "to_currency": "TRY",
                "amount": 100,
                "rate": 32.45,
                "result": 3245.00,
                "error": None
            }
    
    Örnek:
        >>> result = get_exchange_rate("USD", "TRY", 100)
        >>> print(result)
        {"success": True, "from_currency": "USD", "to_currency": "TRY", 
         "amount": 100, "rate": 32.45, "result": 3245.00, "error": None}
        
        >>> result = get_exchange_rate("XYZ", "TRY", 100)
        >>> print(result)
        {"success": False, "error": "Geçersiz para birimi: XYZ"}
    """
    
    # TODO: Para birimi kodlarını büyük harfe çevir (api büyük harf bekler)
    # from_currency = from_currency.upper()
    # to_currency = to_currency.upper()
    
    # TODO: API URL'ini oluştur
    # url = f"{EXCHANGERATE_BASE_URL}/{from_currency}"
    
    # TODO: API çağrısı yap
    # try:
    #     response = requests.get(url)
    #     response.raise_for_status()
    #     data = response.json()
    # except requests.exceptions.RequestException as e:
    #     return {"success": False, "error": f"API hatası: {str(e)}"}
    
    # TODO: Hedef para biriminin kurunu bul
    # if to_currency not in data["rates"]:
    #     return {"success": False, "error": f"Geçersiz para birimi: {to_currency}"}
    
    # rate = data["rates"][to_currency]
    
    # TODO: Çevirimi hesapla
    # result = amount * rate
    
    # TODO: Sonucu döndür
    # return {
    #     "success": True,
    #     "from_currency": from_currency,
    #     "to_currency": to_currency,
    #     "amount": amount,
    #     "rate": round(rate, 4),
    #     "result": round(result, 2),
    #     "error": None
    # }
    
    pass  # Bu satırı sil ve fonksiyonu tamamla


# =============================================================================
# TEST KODU
# =============================================================================
# Bu kısım dosya direkt çalıştırıldığında test yapar
# Kullanım: python tools/currency.py

if __name__ == "__main__":
    # Test 1: USD -> TRY
    print("Test 1: 100 USD -> TRY")
    result = get_exchange_rate("USD", "TRY", 100)
    print(f"Sonuç: {result}")
    print()
    
    # Test 2: EUR -> TRY
    print("Test 2: 50 EUR -> TRY")
    result = get_exchange_rate("EUR", "TRY", 50)
    print(f"Sonuç: {result}")
    print()
    
    # Test 3: Küçük harf testi
    print("Test 3: 100 usd -> try (küçük harf)")
    result = get_exchange_rate("usd", "try", 100)
    print(f"Sonuç: {result}")
    print()
    
    # Test 4: Geçersiz para birimi
    print("Test 4: Geçersiz para birimi")
    result = get_exchange_rate("XYZ", "TRY", 100)
    print(f"Sonuç: {result}")
