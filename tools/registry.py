"""
registry.py - Araç Kayıt ve Yönetim Sistemi
===========================================
Görev: GAMZE
Branch: feature/tools-registry-parser
Durum: YAPILACAK

Bu dosya araçları kayıt altına alır ve yönetir.
Agent hangi araçların mevcut olduğunu buradan öğrenir.

NEDEN GEREKLİ?
Agent'ın hangi araçların mevcut olduğunu bilmesi lazım.
Bu sınıf:
1. Araçları kayıt altına alır
2. LLM'e araç listesini tanımlar
3. İsme göre araç çalıştırır

YAPILACAKLAR:
1. ToolRegistry sınıfını tamamla
2. register() metodunu yaz - yeni araç kaydet
3. get_tools_description() metodunu yaz - LLM için araç listesi
4. execute() metodunu yaz - aracı çalıştır

BAĞIMLILIKLAR:
- tools/weather.py (Gözde'nin görevi)
- tools/currency.py (İrem'in görevi)

İPUÇLARI:
- Araçları bir dictionary'de tut
- Her araç için: fonksiyon, açıklama, parametreler
- Hata yönetimi önemli (araç bulunamazsa ne olacak?)
"""


class ToolRegistry:
    """
    Araç Kayıt ve Yönetim Sistemi
    
    Bu sınıf Agent'ın kullanabileceği araçları yönetir.
    Yeni araç eklemek, listelemek ve çalıştırmak için kullanılır.
    
    Kullanım:
        registry = ToolRegistry()
        registry.register(
            name="get_weather",
            func=get_weather,
            description="Hava durumu bilgisi getirir",
            parameters={"city": "Şehir adı (örn: Istanbul)"}
        )
        
        # LLM için araç listesi al
        tools_prompt = registry.get_tools_description()
        
        # Araç çalıştır
        result = registry.execute("get_weather", city="Istanbul")
    """
    
    def __init__(self):
        """
        Boş bir araç kaydı oluşturur.
        """
        # Araçları saklayacak dictionary
        # Format: {"tool_name": {"func": function, "description": str, "parameters": dict}}
        self._tools = {}
    
    def register(self, name: str, func: callable, description: str, parameters: dict) -> None:
        """
        Yeni bir araç kaydet.
        
        Args:
            name: Aracın adı (örn: "get_weather")
                  LLM bu isimle aracı çağıracak
            func: Çalıştırılacak fonksiyon
            description: Aracın ne yaptığının açıklaması
                        LLM buna bakarak hangi aracı kullanacağına karar verir
            parameters: Parametrelerin açıklaması
                       {"param_name": "param açıklaması"}
        
        Örnek:
            registry.register(
                name="get_weather",
                func=get_weather,
                description="Belirtilen şehir için güncel hava durumu bilgisi getirir",
                parameters={"city": "Şehir adı (örn: Istanbul, Ankara)"}
            )
        """
        # TODO: Aracı _tools dictionary'sine kaydet
        # self._tools[name] = {
        #     "func": func,
        #     "description": description,
        #     "parameters": parameters
        # }

        if name in self._tools:
            raise ValueError(f"Araç zaten kayıtlı: {name}")

        self._tools[name] = {
            "func": func,
            "description": description,
            "parameters": parameters
        }
    
    def get_tools_description(self) -> str:
        """
        Tüm araçların LLM için formatlanmış açıklamasını döndürür.
        
        Bu metod Agent'ın system prompt'una eklenir.
        LLM bu açıklamaya bakarak hangi aracı kullanacağına karar verir.
        
        Returns:
            str: Formatlanmış araç listesi
            
        Örnek çıktı:
            - get_weather: Belirtilen şehir için güncel hava durumu bilgisi getirir
              Parametreler: city (Şehir adı)
            
            - get_exchange_rate: Para birimi çevirisi yapar
              Parametreler: from_currency (Kaynak para birimi), to_currency (Hedef para birimi), amount (Miktar)
        """
        # TODO: Tüm araçları güzel bir formatta listele
        # description = ""
        # for name, tool in self._tools.items():
        #     description += f"- {name}: {tool['description']}\n"
        #     params = ", ".join([f"{k} ({v})" for k, v in tool["parameters"].items()])
        #     description += f"  Parametreler: {params}\n\n"
        # return description

        description = ""

        for name, tool in self._tools.items():
            description += f"- {name}: {tool['description']}\n"

            if tool["parameters"]:
                params = ", ".join(
                    [f"{param} ({desc})" for param, desc in tool["parameters"].items()]
                )
                description += f"  Parametreler: {params}\n"

            description += "\n"

        return description.strip()
    
    def execute(self, tool_name: str, **kwargs) -> any:
        """
        Bir aracı çalıştır.
        
        Args:
            tool_name: Çalıştırılacak aracın adı
            **kwargs: Araca gönderilecek parametreler
        
        Returns:
            Aracın döndürdüğü sonuç
        
        Raises:
            ValueError: Araç bulunamazsa
        
        Örnek:
            result = registry.execute("get_weather", city="Istanbul")
            result = registry.execute("get_exchange_rate", from_currency="USD", to_currency="TRY", amount=100)
        """
        # TODO: Aracı bul
        # if tool_name not in self._tools:
        #     raise ValueError(f"Araç bulunamadı: {tool_name}")
        
        # TODO: Aracı çalıştır ve sonucu döndür
        # tool = self._tools[tool_name]
        # return tool["func"](**kwargs)

        if tool_name not in self._tools:
            raise ValueError(f"Araç bulunamadı: {tool_name}")

        tool = self._tools[tool_name]
        func = tool["func"]

        return func(**kwargs)
    
    def list_tools(self) -> list:
        """
        Kayıtlı araçların isimlerini listele.
        
        Returns:
            list: Araç isimleri listesi
        
        Örnek:
            >>> registry.list_tools()
            ["get_weather", "get_exchange_rate"]
        """
        return list(self._tools.keys())
    
    def has_tool(self, tool_name: str) -> bool:
        """
        Bir aracın kayıtlı olup olmadığını kontrol et.
        
        Args:
            tool_name: Kontrol edilecek araç adı
        
        Returns:
            bool: Araç varsa True, yoksa False
        """
        return tool_name in self._tools


# =============================================================================
# VARSAYILAN ARAÇLARI KAYDET
# =============================================================================
# Bu fonksiyon tüm araçları kayıtlı bir registry döndürür
# Agent bu fonksiyonu kullanarak hazır bir registry alabilir

def create_default_registry() -> ToolRegistry:
    """
    Varsayılan araçlarla dolu bir ToolRegistry oluşturur.
    
    Returns:
        ToolRegistry: Weather ve Currency araçları kayıtlı registry
    
    Kullanım:
        registry = create_default_registry()
        agent = Agent(tool_registry=registry)
    """
    # TODO: Bu fonksiyonu tamamla
    # from tools.weather import get_weather
    # from tools.currency import get_exchange_rate
    
    # registry = ToolRegistry()
    
    # registry.register(
    #     name="get_weather",
    #     func=get_weather,
    #     description="Belirtilen şehir için güncel hava durumu bilgisi getirir (sıcaklık, durum, nem)",
    #     parameters={"city": "Şehir adı (örn: Istanbul, Ankara, London)"}
    # )
    
    # registry.register(
    #     name="get_exchange_rate",
    #     func=get_exchange_rate,
    #     description="Bir para birimini diğerine çevirir ve güncel kuru gösterir",
    #     parameters={
    #         "from_currency": "Kaynak para birimi kodu (örn: USD, EUR)",
    #         "to_currency": "Hedef para birimi kodu (örn: TRY, GBP)",
    #         "amount": "Çevrilecek miktar (sayı)"
    #     }
    # )
    
    # return registry

    from tools.weather import get_weather
    from tools.currency import get_exchange_rate

    registry = ToolRegistry()

    registry.register(
        name="get_weather",
        func=get_weather,
        description="Belirtilen şehir için güncel hava durumu bilgisi getirir (sıcaklık, durum, nem)",
        parameters={
            "city": "Şehir adı (örn: Istanbul, Ankara, London)"
        }
    )

    registry.register(
        name="get_exchange_rate",
        func=get_exchange_rate,
        description="Bir para birimini diğerine çevirir ve güncel kuru gösterir",
        parameters={
            "from_currency": "Kaynak para birimi kodu (örn: USD, EUR)",
            "to_currency": "Hedef para birimi kodu (örn: TRY, GBP)",
            "amount": "Çevrilecek miktar (sayı)"
        }
    )

    return registry


# =============================================================================
# TEST KODU
# =============================================================================

if __name__ == "__main__":
    # Test registry
    print("=== Tool Registry Test ===\n")
    
    # Basit test fonksiyonu
    def dummy_weather(city):
        return f"{city}: 20°C, güneşli"
    
    def dummy_currency(from_currency, to_currency, amount):
        return f"{amount} {from_currency} = {amount * 30} {to_currency}"
    
    # Registry oluştur ve araçları kaydet
    registry = ToolRegistry()
    
    registry.register(
        name="get_weather",
        func=dummy_weather,
        description="Hava durumu getirir",
        parameters={"city": "Şehir adı"}
    )
    
    registry.register(
        name="get_exchange_rate",
        func=dummy_currency,
        description="Döviz çevirir",
        parameters={"from_currency": "Kaynak", "to_currency": "Hedef", "amount": "Miktar"}
    )
    
    # Testler
    print("Kayıtlı araçlar:", registry.list_tools())
    print()
    print("Araç açıklamaları:")
    print(registry.get_tools_description())
    print()
    print("Weather test:", registry.execute("get_weather", city="Istanbul"))
    print("Currency test:", registry.execute("get_exchange_rate", from_currency="USD", to_currency="TRY", amount=100))
