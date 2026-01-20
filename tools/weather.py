"""
weather.py - Hava Durumu Aracı
==============================
Görev: GÖZDE
Branch: feature/tools-weather
Durum: YAPILACAK

Bu dosya OpenWeatherMap API'den hava durumu bilgisi çeker.
Agent "İstanbul'da hava nasıl?" gibi sorularda bu aracı kullanır.

API BİLGİLERİ:
- Kayıt: https://openweathermap.org/api (ücretsiz hesap aç)
- Endpoint: https://api.openweathermap.org/data/2.5/weather
- Dokümantasyon: https://openweathermap.org/current

YAPILACAKLAR:
1. get_weather() fonksiyonunu tamamla
2. API çağrısını yaz
3. Hata yönetimini ekle (şehir bulunamazsa, API hatası vs.)
4. Sonucu güzel formatla

TEST:
    python -c "from tools.weather import get_weather; print(get_weather('Istanbul'))"

İPUÇLARI:
- API key'i config.py'dan al, buraya yazma!
- Sıcaklık Kelvin olarak gelir, Celsius'a çevir
- Türkçe şehir isimleri çalışmayabilir, İngilizce dene
"""

import requests
from config import OPENWEATHER_API_KEY, OPENWEATHER_BASE_URL


def get_weather(city: str) -> dict:
    """
    Belirtilen şehir için hava durumu bilgisi getirir.
    
    Bu fonksiyon OpenWeatherMap API'yi kullanarak anlık hava
    durumu bilgisini çeker ve kullanıcı dostu bir formatta döndürür.
    
    Args:
        city: Şehir adı (örn: "Istanbul", "Ankara", "London")
              Türkçe karakterler sorun çıkarabilir, İngilizce tercih edin.
    
    Returns:
        dict: Hava durumu bilgisi içeren sözlük
            {
                "success": True/False,
                "city": "Istanbul",
                "temperature": 18,
                "description": "parçalı bulutlu",
                "humidity": 65,
                "wind_speed": 3.5,
                "error": None  # Hata varsa mesaj içerir
            }
    
    Örnek:
        >>> result = get_weather("Istanbul")
        >>> print(result)
        {"success": True, "city": "Istanbul", "temperature": 18, ...}
        
        >>> result = get_weather("XYZCity")
        >>> print(result)
        {"success": False, "error": "Şehir bulunamadı: XYZCity"}
    """
    
    # TODO: API parametrelerini hazırla
    params = {
        "q": city,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric",  
        "lang": "tr"        
    }
    
    # TODO: API çağrısı yap
    try:
        response = requests.get(OPENWEATHER_BASE_URL, params=params)
        
        # TODO: Hata durumlarını ele al (404 ve 401)
        if response.status_code == 404:
            return {"success": False, "error": f"Şehir bulunamadı: {city}"}
        
        if response.status_code == 401:
            return {"success": False, "error": "API key geçersiz."}
            
        response.raise_for_status() 
        data = response.json()

        # TODO: Başarılı cevabı formatla
        return {
            "success": True,
            "city": data["name"],
            "temperature": round(data["main"]["temp"]),
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "error": None
        }
    
    # TODO: Hata durumlarını ele al (Bağlantı ve Diğer hatalar)
    except requests.exceptions.RequestException as e:
        return {"success": False, "error": f"API bağlantı hatası: {str(e)}"}


# =============================================================================
# TEST KODU
# =============================================================================
# Bu kısım dosya direkt çalıştırıldığında test yapar
# Kullanım: python tools/weather.py

if __name__ == "__main__":
    # Test 1: Geçerli şehir
    print("Test 1: Istanbul")
    result = get_weather("Istanbul")
    print(f"Sonuç: {result}")
    print()
    
    # Test 2: Başka bir şehir
    print("Test 2: Ankara")
    result = get_weather("Ankara")
    print(f"Sonuç: {result}")
    print()
    
    # Test 3: Geçersiz şehir
    print("Test 3: Geçersiz şehir")
    result = get_weather("BuSehirYok12345")
    print(f"Sonuç: {result}")
