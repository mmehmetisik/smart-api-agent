"""
app.py - Streamlit Ana Uygulaması
=================================
Görev: Team Lead (Mehmet)
Branch: main geliştirme (tüm parçalar birleştikten sonra)
Durum: YAPILACAK (en son yapılacak)

Bu dosya uygulamanın arayüzünü oluşturur.
Tüm diğer parçalar tamamlandıktan sonra yazılacak.

ÖZELLİKLER:
1. Chat arayüzü (kullanıcı mesaj yazar)
2. Agent cevabı gösterir
3. Düşünce sürecini expander'da gösterir
4. Hangi araçların çağrıldığını gösterir

BAĞIMLILIKLAR:
- agent/core.py (Onur'un görevi) - TAMAMLANMIŞ OLMALI
- tools/ (Gözde ve İrem'in görevi) - TAMAMLANMIŞ OLMALI
- utils/parser.py (Gamze'nin görevi) - TAMAMLANMIŞ OLMALI

ÇALIŞTIRMA:
    streamlit run app.py
"""

import streamlit as st
from agent.core import Agent
from tools.registry import create_default_registry


# =============================================================================
# SAYFA AYARLARI
# =============================================================================

st.set_page_config(
    page_title="🤖 Smart API Agent",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Smart API Agent")
st.markdown("*Doğal dille konuşun, agent sizin için API'leri çağırsın!*")

# =============================================================================
# SESSION STATE (Oturum Durumu)
# =============================================================================
# Streamlit her etkileşimde sayfayı yeniden çalıştırır
# Session state, verilerimizi korumamızı sağlar

if "messages" not in st.session_state:
    st.session_state.messages = []

if "agent" not in st.session_state:
    # TODO: Agent'ı başlat (tüm parçalar tamamlandığında)
    # registry = create_default_registry()
    # st.session_state.agent = Agent(tool_registry=registry)
    st.session_state.agent = None  # Şimdilik None

# =============================================================================
# CHAT GEÇMİŞİNİ GÖSTER
# =============================================================================

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
        # Eğer assistant mesajıysa ve düşünce süreci varsa göster
        if message["role"] == "assistant" and "thoughts" in message:
            with st.expander("🧠 Düşünce Süreci", expanded=False):
                for thought in message["thoughts"]:
                    if thought["type"] == "thought":
                        st.info(f"💭 {thought['content']}")
                    elif thought["type"] == "action":
                        st.warning(f"🔧 Araç: {thought['tool']}({thought['params']})")
                    elif thought["type"] == "observation":
                        st.success(f"📊 Sonuç: {thought['content']}")

# =============================================================================
# KULLANICI INPUT
# =============================================================================

if prompt := st.chat_input("Bir şey sorun... (örn: İstanbul'da hava nasıl?)"):
    # Kullanıcı mesajını ekle
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Agent cevabı
    with st.chat_message("assistant"):
        # TODO: Agent'ı çalıştır (tüm parçalar tamamlandığında)
        # with st.spinner("Düşünüyorum..."):
        #     response, thoughts = st.session_state.agent.run(prompt)
        
        # Şimdilik placeholder
        response = "⚠️ Agent henüz hazır değil. Tüm parçalar tamamlandığında çalışacak!"
        thoughts = []
        
        st.markdown(response)
        
        # Düşünce sürecini göster (varsa)
        if thoughts:
            with st.expander("🧠 Düşünce Süreci", expanded=True):
                for thought in thoughts:
                    if thought["type"] == "thought":
                        st.info(f"💭 {thought['content']}")
                    elif thought["type"] == "action":
                        st.warning(f"🔧 Araç: {thought['tool']}({thought['params']})")
                    elif thought["type"] == "observation":
                        st.success(f"📊 Sonuç: {thought['content']}")
    
    # Assistant mesajını kaydet
    st.session_state.messages.append({
        "role": "assistant",
        "content": response,
        "thoughts": thoughts
    })

# =============================================================================
# SIDEBAR - BİLGİLER
# =============================================================================

with st.sidebar:
    st.header("ℹ️ Hakkında")
    st.markdown("""
    Bu uygulama bir **AI Agent** demonstrasyonudur.
    
    **Mevcut Araçlar:**
    - 🌤️ Hava Durumu (OpenWeatherMap)
    - 💱 Döviz Kuru (ExchangeRate API)
    
    **Örnek Sorular:**
    - "İstanbul'da hava nasıl?"
    - "100 dolar kaç TL?"
    - "Ankara'da hava nasıl ve 50 euro kaç lira?"
    """)
    
    st.divider()
    
    st.header("🔧 Geliştirici Bilgisi")
    st.markdown("""
    **Proje:** Smart API Agent
    
    **Ekip:**
    - Gözde (Weather Tool)
    - İrem (Currency Tool)
    - Gamze (Registry & Parser)
    - Onur (Agent Core)
    - Mehmet (Team Lead & UI)
    """)
    
    # Sohbeti temizle butonu
    if st.button("🗑️ Sohbeti Temizle"):
        st.session_state.messages = []
        st.rerun()
