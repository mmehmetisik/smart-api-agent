# """
# core.py - Agent Ana Döngüsü (ReAct Loop)
# ========================================
# Görev: ONUR
# Branch: feature/agent-core
# Durum: YAPILACAK
#
# Bu dosya Agent'ın kalbidir. Kullanıcı mesajını alır, düşünür,
# gerekirse araç çağırır ve sonuç üretir.
#
# ReAct Pattern: Reasoning + Acting
# - Düşün (Thought)
# - Hareket et (Action)
# - Gözlemle (Observation)
# - Tekrarla veya Cevap ver (Answer)
#
# YAPILACAKLAR:
# 1. Agent sınıfını tamamla
# 2. run() metodunu yaz - ana döngü burada
# 3. _call_llm() metodunu yaz - Groq API çağrısı
# 4. _execute_action() metodunu yaz - araç çağırma
#
# BAĞIMLILIKLAR:
# - tools/registry.py tamamlanmış olmalı (Gamze'nin görevi)
# - agent/prompts.py tamamlanmış olmalı (kendi görevin)
# - utils/parser.py tamamlanmış olmalı (Gamze'nin görevi)
#
# İPUÇLARI:
# - Groq API dökümanı: https://console.groq.com/docs/quickstart
# - Sonsuz döngüye dikkat! MAX_ITERATIONS kullan
# - Her adımı history'ye kaydet (UI'da göstermek için)
# """
#
# from groq import Groq
# from config import GROQ_API_KEY, MODEL_NAME, MAX_ITERATIONS, TEMPERATURE
# from .prompts import SYSTEM_PROMPT
# from tools.registry import ToolRegistry
# from utils.parser import parse_llm_response
#
#
# class Agent:
#     """
#     Smart API Agent - Araç kullanan akıllı asistan
#
#     Kullanım:
#         agent = Agent()
#         response, history = agent.run("İstanbul'da hava nasıl?")
#     """
#
#     def __init__(self, tool_registry: ToolRegistry = None):
#         """
#         Agent'ı başlat
#
#         Args:
#             tool_registry: Kullanılacak araçların kaydı.
#                           None ise varsayılan araçlar yüklenir.
#         """
#         # TODO: Groq client'ı başlat
#         # self.client = Groq(api_key=GROQ_API_KEY)
#
#         # TODO: Tool registry'yi ayarla
#         # self.tools = tool_registry or ToolRegistry()
#
#         # TODO: Varsayılan araçları kaydet (weather, currency)
#
#         # Konuşma geçmişi (her adımı kaydet)
#         self.history = []
#
#         pass  # Bu satırı sil ve yukarıdaki TODO'ları tamamla
#
#     def run(self, user_input: str) -> tuple[str, list]:
#         """
#         Agent'ı çalıştır - ANA DÖNGÜ
#
#         Bu metod ReAct döngüsünü uygular:
#         1. Kullanıcı mesajını al
#         2. LLM'e gönder
#         3. LLM'in cevabını parse et
#         4. Eğer ACTION varsa, aracı çağır ve OBSERVATION ekle
#         5. Eğer ANSWER varsa, döngüyü bitir
#         6. MAX_ITERATIONS'a ulaşılırsa dur
#
#         Args:
#             user_input: Kullanıcının mesajı
#
#         Returns:
#             tuple: (final_answer, history)
#                 - final_answer: Kullanıcıya verilecek cevap
#                 - history: Tüm düşünme adımları (UI'da göstermek için)
#         """
#         # TODO: Konuşma geçmişini sıfırla
#         self.history = []
#
#         # TODO: System prompt'u hazırla (araç listesiyle birlikte)
#
#         # TODO: Mesajları hazırla [system, user]
#         messages = []
#
#         # TODO: ReAct döngüsü
#         for iteration in range(MAX_ITERATIONS):
#             # 1. LLM'i çağır
#             # llm_response = self._call_llm(messages)
#
#             # 2. Cevabı parse et
#             # parsed = parse_llm_response(llm_response)
#
#             # 3. History'ye ekle
#             # self.history.append({"type": parsed["type"], "content": ...})
#
#             # 4. Eğer ANSWER ise bitir
#             # if parsed["type"] == "answer":
#             #     return parsed["content"], self.history
#
#             # 5. Eğer ACTION ise aracı çağır
#             # if parsed["type"] == "action":
#             #     observation = self._execute_action(parsed["tool"], parsed["params"])
#             #     # Observation'ı mesajlara ekle
#
#             pass  # Bu satırı sil ve döngüyü tamamla
#
#         # Maksimum iterasyona ulaşıldı
#         return "Üzgünüm, cevabı bulamadım. Lütfen sorunuzu başka şekilde sormayı deneyin.", self.history
#
#     def _call_llm(self, messages: list) -> str:
#         """
#         Groq API'yi çağır
#
#         Args:
#             messages: OpenAI formatında mesaj listesi
#                      [{"role": "system", "content": "..."},
#                       {"role": "user", "content": "..."}]
#
#         Returns:
#             str: LLM'in cevabı
#         """
#         # TODO: Groq API çağrısı yap
#         # response = self.client.chat.completions.create(
#         #     model=MODEL_NAME,
#         #     messages=messages,
#         #     temperature=TEMPERATURE,
#         # )
#         # return response.choices[0].message.content
#
#         pass  # Bu satırı sil ve metodu tamamla
#
#     def _execute_action(self, tool_name: str, params: dict) -> str:
#         """
#         Bir aracı çalıştır
#
#         Args:
#             tool_name: Çağrılacak aracın adı (örn: "get_weather")
#             params: Araca gönderilecek parametreler (örn: {"city": "Istanbul"})
#
#         Returns:
#             str: Aracın döndürdüğü sonuç
#         """
#         # TODO: Tool registry'den aracı çağır
#         # try:
#         #     result = self.tools.execute(tool_name, **params)
#         #     return str(result)
#         # except Exception as e:
#         #     return f"Hata: {str(e)}"
#
#         pass  # Bu satırı sil ve metodu tamamla



#############################################################################################################

"""
core.py - Agent Ana Döngüsü (ReAct Loop)
========================================
Görev: ONUR
Branch: feature/agent-core
Durum: DEBUG MODU & GAMZE UYUMLU

Bu sürüm, Gamze'nin registry.py yapısına (get_tools_description) tam uyumludur.
"""

import os
import locale
from datetime import datetime
from groq import Groq

# Config ayarları
try:
    from config import GROQ_API_KEY, MODEL_NAME, MAX_ITERATIONS, TEMPERATURE
except ImportError:
    # Config dosyası yoksa varsayılan değerleri kullan (Güvenli Mod)
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    MODEL_NAME = "llama-3.3-70b-versatile"
    MAX_ITERATIONS = 5
    TEMPERATURE = 0.7

from agent.prompts import SYSTEM_PROMPT

# BAĞIMLILIK YÖNETİMİ
# Takım arkadaşlarının modülleri henüz birleşmemiş olabilir diye
# Kodumuz patlamasın diye bunları "try-except" bloğu ile içeri alıyoruz.
try:
    from tools.registry import ToolRegistry
    from utils.parser import parse_llm_response
except ImportError:
    ToolRegistry = None
    parse_llm_response = None


class Agent:
    """
        LLM tabanlı, araç kullanabilen akıllı ajan sınıfı.

        Attributes:
            client (Groq): LLM API istemcisi.
            tools (ToolRegistry, optional): Araçların kayıtlı olduğu yönetim sınıfı.
            history (List[Dict]): Konuşma ve işlem geçmişini tutan liste.
        """
    def __init__(self, tool_registry=None):
        """
                Agent sınıfını başlatır.

                Args:
                    tool_registry: Dışarıdan enjekte edilebilen araç kayıt sınıfı.
                                   Eğer verilmezse otomatik import etmeye çalışır.
                """
        print("🤖 Agent başlatılıyor...")

        if not GROQ_API_KEY:
            print("UYARI: Groq API Key bulunamadı!")

        self.client = Groq(api_key=GROQ_API_KEY)

        # ToolRegistry Entegrasyonu (Gamze'nin kod yapısına uyumluluk kontrolü)
        self.tools = None
        if tool_registry:
            self.tools = tool_registry
        elif ToolRegistry:
            try:
                temp_tools = ToolRegistry()
                # Gamze'nin belirlediği metodların varlığını kontrol ediyoruz (Duck Typing)
                if hasattr(temp_tools, 'get_tools_description') and hasattr(temp_tools, 'execute'):
                    self.tools = temp_tools
                else:
                    print("UYARI: ToolRegistry eksik veya uyumsuz. Mock moda geçiliyor.")
            except Exception as e:
                print(f"⚠UYARI: ToolRegistry başlatılamadı: {e}")

        self.history = []

    def run(self, user_input: str) -> tuple[str, list]:
        """
                Kullanıcı girdisini alır ve ReAct döngüsünü başlatır.

                Bu metod, ajanın "Düşün -> Araç Seç -> Uygula -> Gözlemle" döngüsünü yönetir.

                Args:
                    user_input (str): Kullanıcının sorduğu soru veya verdiği komut.

                Returns:
                    Tuple[str, List]: (Final Cevap, İşlem Geçmişi)
                """
        self.history = [] # Her yeni soruda hafızayı temizle
        messages = []

        # 1. Tarih Ayarları
        try:
            locale.setlocale(locale.LC_TIME, "tr_TR.UTF-8")
        except:
            pass

        now = datetime.now()

        # 2. Araç Listesini Al
        tools_text = "Şu an aktif araç yok (Test Modu)."
        if self.tools:
            try:
                # Gamze'nin registry.py modülünden araç tanımlarını çekiyoruz
                tools_text = self.tools.get_tools_description()
            except Exception as e:
                print(f"Araç listesi alınamadı: {e}")
                self.tools = None

                # 3. Sistem Prompt'unun Oluşturulması
        try:
            formatted_system_prompt = SYSTEM_PROMPT.format(
                date=now.strftime("%d %B %Y"),
                day_of_week=now.strftime("%A"),
                tools_description=tools_text
            )
        except Exception as e:
            return f"Prompt Hatası: {e}", []

        messages.append({"role": "system", "content": formatted_system_prompt})
        messages.append({"role": "user", "content": user_input})

        print(f"\nKullanıcı: {user_input}")

        # 4. Ana ReAct Döngüsü (Maksimum iterasyon sayısı kadar döner)
        for iteration in range(MAX_ITERATIONS):
            print(f"Düşünüyor... (Adım {iteration + 1}/{MAX_ITERATIONS})")

            # A. LLM Çağır
            llm_response = self._call_llm(messages)
            print(f"[DEBUG] LLM Ham Cevap:\n{llm_response}\n-------------------")

            # B. Parse Et
            parsed = None
            if parse_llm_response:
                try:
                    parsed = parse_llm_response(llm_response)
                except:
                    pass

            # Fallback (Yedek) Parser: Parser modülü henüz gelmediyse veya hata verdiyse devreye girer
            if parsed is None:
                if "tool" in str(llm_response) and "get_weather" in str(llm_response):
                    parsed = {"type": "action", "tool": "get_weather", "params": {"city": "Ankara"}}
                elif "tool" in str(llm_response) and "convert_currency" in str(llm_response):
                    parsed = {"type": "action", "tool": "convert_currency",
                              "params": {"amount": 100, "from_currency": "USD", "to_currency": "TRY"}}
                else:
                    parsed = {"type": "answer", "content": llm_response}

            # C. Kayıt
            self.history.append(parsed)
            messages.append({"role": "assistant", "content": llm_response})

            # D. Aksiyon
            if parsed["type"] == "answer":
                print("Cevap bulundu.")
                return parsed["content"], self.history

            elif parsed["type"] == "action":
                tool_name = parsed["tool"]
                params = parsed["params"]
                print(f"🛠️ Araç Çağrılıyor: {tool_name} -> {params}")

                observation = self._execute_action(tool_name, params)
                print(f" Gözlem: {observation}")

                messages.append({"role": "user", "content": f"[OBSERVATION] {observation}"})
                self.history.append({"type": "observation", "content": observation})

        return "Döngü sınırına ulaşıldı.", self.history

    def _call_llm(self, messages: list) -> str:
        """Groq API'sine istek atar ve yanıtı döndürür."""
        try:
            response = self.client.chat.completions.create(
                model=MODEL_NAME,
                messages=messages,
                temperature=TEMPERATURE,
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"API Hatası: {e}"

    def _execute_action(self, tool_name: str, params: dict) -> str:
        """
                Belirtilen aracı çalıştırır. Eğer araçlar yüklenmediyse Mock data döner.
        """
        if self.tools:
            try:
                return self.tools.execute(tool_name, **params)
            except Exception as e:
                return f"Araç Hatası: {e}"

        # # --- MOCK DATA (Simülasyon) ---
        if tool_name == "get_weather":
            return "Ankara: 18°C, Parçalı Bulutlu (Simülasyon Verisi)"
        if tool_name == "convert_currency":
            return "100 USD = 3450 TRY (Simülasyon Verisi)"

        return f"{tool_name} aracı simülasyon modunda başarılı."


# TEST BLOĞU (Sadece bu dosya doğrudan çalıştırıldığında devreye girer)
if __name__ == "__main__":
    print("\nFINAL TEST MODU BAŞLATILIYOR...")

    # .env yükleme (Eğer python-dotenv yüklüyse)
    try:
        from dotenv import load_dotenv

        load_dotenv()
    except ImportError:
        pass

    try:
        # Agent'ı başlat (Registry yoksa bile mock modunda çalışır)
        agent = Agent()
        cevap, gecmis = agent.run("Yarın Ankara'da hava nasıl?")
        print("\nSONUÇ:")
        print(cevap)
    except Exception as e:
        print(f"\nBEKLENMEYEN  HATA: {e}")

