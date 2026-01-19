# 🤖 Smart API Agent

> Doğal dille konuşun, agent sizin için API'leri çağırsın!

Smart API Agent, kullanıcının doğal dilde sorduğu soruları anlayan ve cevaplamak için gerekli API'leri otomatik olarak çağıran bir yapay zeka asistanıdır. 

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31+-red.svg)
![Groq](https://img.shields.io/badge/LLM-Groq-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🎯 Ne Yapıyor?

```
Kullanıcı: "İstanbul'da hava nasıl ve 100 dolar kaç TL?"

Agent düşünür:
💭 Kullanıcı iki bilgi istiyor: hava durumu ve döviz kuru
🔧 get_weather(city="Istanbul") çağırılıyor...
📊 Sonuç: 18°C, parçalı bulutlu
💭 Hava durumunu aldım, şimdi döviz kurunu almalıyım
🔧 get_exchange_rate(from="USD", to="TRY", amount=100) çağırılıyor...
📊 Sonuç: 3,247 TRY

Agent: "İstanbul'da hava 18°C ve parçalı bulutlu. 100 dolar şu an 3,247 TL."
```

## 🚀 Özellikler

- 🌤️ **Hava Durumu Sorgulama** - Herhangi bir şehrin anlık hava durumu
- 💱 **Döviz Çevirme** - Güncel kurlarla para birimi çevirisi
- 🔗 **Zincirleme Sorgular** - Tek soruda birden fazla bilgi
- 🧠 **Düşünce Görselleştirme** - Agent'ın düşünce sürecini görün
- 💬 **Doğal Dil** - Türkçe konuşun, Türkçe cevap alın

## 📁 Proje Yapısı

```
smart-api-agent/
├── app.py                  # Streamlit arayüzü
├── config.py               # Konfigürasyon
├── requirements.txt        # Bağımlılıklar
├── .env.example            # Ortam değişkenleri örneği
│
├── agent/
│   ├── core.py             # Agent ana döngüsü (ReAct)
│   └── prompts.py          # System prompt'lar
│
├── tools/
│   ├── weather.py          # Hava durumu aracı
│   ├── currency.py         # Döviz kuru aracı
│   └── registry.py         # Araç yönetimi
│
└── utils/
    └── parser.py           # LLM çıktı parser'ı
```

## 🛠️ Kurulum

### 1. Repoyu klonlayın

```bash
git clone https://github.com/mmehmetisik/smart-api-agent.git
cd smart-api-agent
```

### 2. Virtual environment oluşturun

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Bağımlılıkları yükleyin

```bash
pip install -r requirements.txt
```

### 4. API anahtarlarını ayarlayın

```bash
cp .env.example .env
# .env dosyasını düzenleyin ve API anahtarlarınızı ekleyin
```

### 5. Uygulamayı çalıştırın

```bash
streamlit run app.py
```

## 🔑 API Anahtarları

Bu proje 3 API kullanır (hepsi ücretsiz tier'a sahip):

| API | Amaç | Kayıt Linki |
|-----|------|-------------|
| Groq | LLM (Llama 3.1) | [console.groq.com](https://console.groq.com/keys) |
| OpenWeatherMap | Hava durumu | [openweathermap.org](https://openweathermap.org/api) |
| ExchangeRate | Döviz kuru | [exchangerate-api.com](https://www.exchangerate-api.com/) |

## 📚 Öğrenilen Kavramlar

Bu proje şu kavramları öğretmek için tasarlanmıştır:

### 1. Agent Nedir?
```
Agent = LLM (Beyin) + Tools (Araçlar) + Loop (Karar Döngüsü)
```

### 2. ReAct Pattern
**Re**asoning + **Act**ing - Düşün, hareket et, gözlemle, tekrarla.

### 3. Tool Calling
LLM'in dış dünya ile etkileşime geçmesi için araç kullanımı.

### 4. Prompt Engineering
Agent'ın doğru davranması için system prompt tasarımı.

## 👥 Ekip

| İsim | Görev | Dosyalar |
|------|-------|----------|
| Gözde | Weather Tool | `tools/weather.py` |
| İrem | Currency Tool | `tools/currency.py` |
| Gamze | Registry & Parser | `tools/registry.py`, `utils/parser.py` |
| Onur | Agent Core | `agent/core.py`, `agent/prompts.py` |
| Mehmet | Team Lead & UI | `app.py`, koordinasyon |

## 📄 Lisans

MIT License - Detaylar için [LICENSE](LICENSE) dosyasına bakın.

## 🔗 Kaynaklar

- [Groq API Docs](https://console.groq.com/docs)
- [OpenWeatherMap API](https://openweathermap.org/current)
- [Streamlit Docs](https://docs.streamlit.io/)
- [ReAct Paper](https://arxiv.org/abs/2210.03629)

---

⭐ Bu proje faydalı olduysa yıldız vermeyi unutmayın!
