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

import os
import locale
from datetime import datetime
from groq import Groq

# FIX: Model güncellendi (3.1 -> 3.3)
try:
    from config import GROQ_API_KEY, MODEL_NAME, MAX_ITERATIONS, TEMPERATURE
except ImportError:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    MODEL_NAME = "llama-3.3-70b-versatile"  # GÜNCELLEME BURADA
    MAX_ITERATIONS = 5
    TEMPERATURE = 0.7

from agent.prompts import SYSTEM_PROMPT


class Agent:
    def __init__(self, tool_registry=None):
        self.client = Groq(api_key=GROQ_API_KEY)
        self.tools = tool_registry
        self.history = []

    def run(self, user_input: str):
        self.history = []
        messages = []

        now = datetime.now()
        prompt = SYSTEM_PROMPT.format(
            date=now.strftime("%d %B %Y"),
            day_of_week=now.strftime("%A"),
            tools_description="Tools list placeholder"
        )

        messages.append({"role": "system", "content": prompt})
        messages.append({"role": "user", "content": user_input})
        print(f"👤 Kullanıcı: {user_input}")

        for i in range(MAX_ITERATIONS):
            print(f"🔄 Düşünüyor... Adım {i + 1}")
            response = self._call_llm(messages)
            return response, self.history

    def _call_llm(self, messages):
        response = self.client.chat.completions.create(
            model=MODEL_NAME, messages=messages, temperature=TEMPERATURE
        )
        return response.choices[0].message.content