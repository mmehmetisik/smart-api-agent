"""
parser.py - LLM Çıktı Parser'ı
==============================
Görev: GAMZE
Branch: feature/tools-registry-parser
Durum: YAPILACAK

Bu dosya LLM'in çıktısını parse eder (ayrıştırır).
Agent'ın düşünce sürecini yapılandırılmış veriye çevirir.

LLM ÇIKTI FORMATI:
LLM şu formatta cevap verir:
    [THOUGHT] Düşünce buraya
    [ACTION] tool_name(param1="value1", param2="value2")
    [ANSWER] Final cevap buraya

PARSER NE YAPIYOR?
Bu metni alıp şöyle bir dictionary'ye çeviriyor:
    {"type": "action", "tool": "get_weather", "params": {"city": "Istanbul"}}
    veya
    {"type": "answer", "content": "İstanbul'da hava güzel."}

YAPILACAKLAR:
1. parse_llm_response() fonksiyonunu tamamla
2. [ACTION] satırını parse et - araç adı ve parametreleri çıkar
3. [ANSWER] satırını parse et - cevabı çıkar
4. [THOUGHT] satırını parse et - düşünceyi çıkar
5. Hata yönetimi ekle (format bozuksa ne olacak?)

İPUÇLARI:
- Regex kullanabilirsin (import re)
- String metodları da işe yarar (split, strip, find)
- Birden fazla [THOUGHT] olabilir, en sonuncuyu al
- [ACTION] formatı: tool_name(param1="value1", param2="value2")
"""

import re


def parse_llm_response(response: str) -> dict:
    """
    LLM'in cevabını parse ederek yapılandırılmış veri döndürür.
    
    Bu fonksiyon Agent'ın düşünce döngüsünde kritik rol oynar.
    LLM'in metin çıktısını Python dictionary'sine çevirir.
    
    Args:
        response: LLM'den gelen ham metin cevabı
        
        Örnek input:
            "[THOUGHT] Kullanıcı hava durumu soruyor
             [ACTION] get_weather(city=\"Istanbul\")"
    
    Returns:
        dict: Parse edilmiş sonuç
        
        Eğer ACTION varsa:
            {
                "type": "action",
                "thought": "Kullanıcı hava durumu soruyor",
                "tool": "get_weather",
                "params": {"city": "Istanbul"}
            }
        
        Eğer ANSWER varsa:
            {
                "type": "answer",
                "thought": "Tüm bilgileri aldım",
                "content": "İstanbul'da hava 18°C ve güneşli."
            }
        
        Eğer parse edilemezse:
            {
                "type": "error",
                "content": "Parse hatası: ...",
                "raw": "<orijinal response>"
            }
    
    Örnek:
        >>> response = '[THOUGHT] Hava durumu lazım\\n[ACTION] get_weather(city="Ankara")'
        >>> result = parse_llm_response(response)
        >>> print(result)
        {"type": "action", "thought": "Hava durumu lazım", "tool": "get_weather", "params": {"city": "Ankara"}}
    """
    
    # TODO: Response'u temizle (baştaki/sondaki boşluklar)
    # response = response.strip()
    
    # TODO: [THOUGHT] satırını bul ve çıkar
    # thought = None
    # thought_match = re.search(r'\[THOUGHT\]\s*(.+?)(?=\[ACTION\]|\[ANSWER\]|$)', response, re.DOTALL)
    # if thought_match:
    #     thought = thought_match.group(1).strip()
    
    # TODO: [ANSWER] varsa, cevap döndür
    # if "[ANSWER]" in response:
    #     answer_match = re.search(r'\[ANSWER\]\s*(.+?)$', response, re.DOTALL)
    #     if answer_match:
    #         return {
    #             "type": "answer",
    #             "thought": thought,
    #             "content": answer_match.group(1).strip()
    #         }
    
    # TODO: [ACTION] varsa, action parse et
    # if "[ACTION]" in response:
    #     action_match = re.search(r'\[ACTION\]\s*(\w+)\((.+?)\)', response)
    #     if action_match:
    #         tool_name = action_match.group(1)
    #         params_str = action_match.group(2)
    #         params = _parse_parameters(params_str)
    #         return {
    #             "type": "action",
    #             "thought": thought,
    #             "tool": tool_name,
    #             "params": params
    #         }
    
    # TODO: Hiçbiri yoksa hata döndür
    # return {
    #     "type": "error",
    #     "content": "Geçerli bir format bulunamadı",
    #     "raw": response
    # }
    
    pass  # Bu satırı sil ve fonksiyonu tamamla


def _parse_parameters(params_str: str) -> dict:
    """
    Parametre string'ini dictionary'ye çevirir.
    
    Args:
        params_str: Parametre string'i
                   Örnek: 'city="Istanbul", country="Turkey"'
    
    Returns:
        dict: Parametreler
              Örnek: {"city": "Istanbul", "country": "Turkey"}
    """
    # TODO: Parametreleri parse et
    # Bu biraz karmaşık olabilir, regex veya basit string işleme kullan
    #
    # Basit yaklaşım:
    # params = {}
    # pairs = params_str.split(',')
    # for pair in pairs:
    #     if '=' in pair:
    #         key, value = pair.split('=', 1)
    #         key = key.strip()
    #         value = value.strip().strip('"\'')
    #         params[key] = value
    # return params
    
    pass  # Bu satırı sil ve fonksiyonu tamamla


def extract_thought(response: str) -> str | None:
    """
    Response'dan [THOUGHT] kısmını çıkarır.
    
    Bu fonksiyon UI'da düşünce sürecini göstermek için kullanılır.
    
    Args:
        response: LLM'den gelen cevap
    
    Returns:
        str | None: Düşünce metni veya None
    """
    # TODO: Düşünceyi çıkar
    # match = re.search(r'\[THOUGHT\]\s*(.+?)(?=\[ACTION\]|\[ANSWER\]|$)', response, re.DOTALL)
    # return match.group(1).strip() if match else None
    
    pass  # Bu satırı sil ve fonksiyonu tamamla


# =============================================================================
# TEST KODU
# =============================================================================

if __name__ == "__main__":
    print("=== Parser Test ===\n")
    
    # Test 1: Action parse
    test1 = """[THOUGHT] Kullanıcı İstanbul'un hava durumunu soruyor.
[ACTION] get_weather(city="Istanbul")"""
    
    print("Test 1: Action Parse")
    print(f"Input: {test1}")
    print(f"Output: {parse_llm_response(test1)}")
    print()
    
    # Test 2: Answer parse
    test2 = """[THOUGHT] Tüm bilgileri topladım, şimdi cevap verebilirim.
[ANSWER] İstanbul'da hava 18°C ve parçalı bulutlu. 100 dolar şu an 3,245 TL."""
    
    print("Test 2: Answer Parse")
    print(f"Input: {test2}")
    print(f"Output: {parse_llm_response(test2)}")
    print()
    
    # Test 3: Çoklu parametre
    test3 = """[THOUGHT] Döviz çevirisi gerekiyor.
[ACTION] get_exchange_rate(from_currency="USD", to_currency="TRY", amount=100)"""
    
    print("Test 3: Çoklu Parametre")
    print(f"Input: {test3}")
    print(f"Output: {parse_llm_response(test3)}")
    print()
    
    # Test 4: Hatalı format
    test4 = "Bu düz bir metin, format yok"
    
    print("Test 4: Hatalı Format")
    print(f"Input: {test4}")
    print(f"Output: {parse_llm_response(test4)}")
