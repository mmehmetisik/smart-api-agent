"""
config.py - Konfigürasyon Dosyası
=================================
Görev: Team Lead (Mehmet)
Durum: TAMAMLANDI

Bu dosya tüm API anahtarlarını ve ayarları içerir.
Öğrenciler bu dosyayı KENDİ .env dosyalarıyla kullanacak.
"""

import os
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

# =============================================================================
# API ANAHTARLARI
# =============================================================================
# Bu değerler .env dosyasından okunur
# Asla bu dosyaya gerçek API key yazmayın!

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
EXCHANGERATE_API_KEY = os.getenv("EXCHANGERATE_API_KEY")

# =============================================================================
# MODEL AYARLARI
# =============================================================================

# Groq'ta kullanılacak model
# Not: llama-3.1 deprecated olduğu için llama-3.3'e güncellendi
MODEL_NAME = "llama-3.3-70b-versatile"

# Agent'ın maksimum düşünme döngüsü (sonsuz döngüyü önler)
MAX_ITERATIONS = 5

# LLM sıcaklık ayarı (0 = deterministik, 1 = yaratıcı)
TEMPERATURE = 0.1

# =============================================================================
# API URL'LERİ
# =============================================================================

OPENWEATHER_BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
EXCHANGERATE_BASE_URL = "https://api.exchangerate-api.com/v4/latest"

# =============================================================================
# UYGULAMA AYARLARI
# =============================================================================

# Streamlit sayfa ayarları
APP_TITLE = "🤖 Smart API Agent"
APP_ICON = "🤖"

# Debug modu (True ise detaylı log gösterir)
DEBUG_MODE = True