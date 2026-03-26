
import streamlit as st
import pandas as pd
import hashlib
import plotly.express as px
from datetime import datetime
from PIL import Image
import folium
from streamlit_folium import st_folium
import random

# --- SAHIFA SOZLAMALARI ---
st.set_page_config(page_title="EcoCarbon AI | Blockchain Green Tech", page_icon="🌳", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #2e7d32; color: white; height: 3em; border: none; }
    .stMetric { border-radius: 15px; padding: 15px; border: 1px solid #e0e0e0; background: white; }
    .status-active { color: #4CAF50; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- MIYA (MANTIQ VA AI SIMULATSIYASI) ---
def get_secure_hash(data_string):
    return hashlib.sha256(data_string.encode()).hexdigest()

def analyze_image_integrity(img):
    """AI: Rasmning haqiqiyligini tekshirish simulatsiyasi"""
    integrity_score = random.randint(85, 99)
    return integrity_score

def calculate_forecast(t_type, age):
    """Kelajakdagi 10 yillik prognoz"""
    ratios = {"Archa": 22, "Chinor": 45, "Mevali": 15, "Terak": 30, "Eman": 50}
    base = ratios.get(t_type, 10)
    years = list(range(1, 11))
    growth = [base * (age + y) / 1000 for y in years]
    return pd.DataFrame({"Yil": [f"+{y}" for y in years], "Kredit (t)": growth})

# --- SIDEBAR NAVIGATSIYA ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2329/2329003.png", width=80)
    st.title("EcoCarbon Engine v2.0")
    st.markdown("---")
    choice = st.radio("Menyu", ["🌐 Global Dashboard", "🛰️ Sun'iy Yo'ldosh Nazorati", "💎 Kredit Savdosi", "📜 Tizim Loglari"])
    st.markdown("---")
    st.success("Tizim Himoyalangan: SHA-256")

# --- 1-BO'LIM: GLOBAL DASHBOARD ---
if choice == "🌐 Global Dashboard":
    st.title("🌍 Global Ekologik Monitoring")
    
    # Metrikalar
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Jami Saqlangan CO2", "142.5 tonna", "+2.4t")
    m2.metric("Faol Kiber-IDlar", "1,248 ta", "+12")
    m3.metric("O'rtacha Kredit Narxi", "$68.42", "+$1.2")
    m4.metric("Xavfsizlik Darajasi", "99.9%", "Stable")

    # Xarita va Grafik
    c1, c2 = st.columns([2, 1])
    with c1:
        st.subheader("📍 Sertifikatlangan hududlar")
        m = folium.Map(location=[41.3111, 69.2405], zoom_start=12, tiles="Stamen Terrain")
        # Namuna nuqtalar
        folium.CircleMarker([41.3111, 69.2405], radius=10, color="green", fill=True, popup="Markaziy Bog'").add_to(m)
        folium.CircleMarker([41.2900, 69.2000], radius=8, color="darkgreen", fill=True, popup="Eko-Hudud #45").add_to(m)
        st_folium(m, width=700, height=400)
    
    with c2:
        st.subheader("📈 Kredit O'sish Prognozi")
        sample_data = calculate_forecast("Chinor", 5)
        fig = px.line(sample_data, x="Yil", y="Kredit (t)", template="plotly_white", color_discrete_sequence=['#2e7d32'])
        st.plotly_chart(fig, use_container_width=True)

# --- 2-BO'LIM: SERTIFIKATLASH ---
elif choice == "🛰️ Sun'iy Yo'ldosh Nazorati":
    st.title("🛰️ Yangi Aktivni Sertifikatlash")
    st.write("Daraxtning GPS koordinatalari va tasviri asosida kiber-pasport yarating.")

    with st.expander("📝 Ma'lumotlarni kiritish", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            t_name = st.text_input("Daraxtga nom bering:", "Mening Chinorim")
            t_type = st.selectbox("Turi:", ["Archa", "Chinor", "Mevali", "Terak", "Eman"])
            t_age = st.slider("Yoshi:", 1, 100, 10)
        with col2:
            lat = st.number_input("Kenglik (Lat):", value=41.3111, format="%.6f")
            lon = st.number_input("Uzunlik (Lon):", value=69.2405, format="%.6f")
            photo = st.file_uploader("Daraxt rasmini yuklang:", type=['jpg', 'jpeg', 'png'])

    if st.button("🔍 Skunnerlash va Tasdiqlash"):
        if photo:
            with st.spinner('AI Metadata va Tasvirni tahlil qilmoqda...'):
                # Hisob-kitoblar
                ratios = {"Archa": 22, "Chinor": 45, "Mevali": 15, "Terak": 30, "Eman": 50}
                co2 = ratios.get(t_type) * t_age / 1000
                integrity = analyze_image_integrity(photo)
                tx_hash = get_secure_hash(f"{lat}{lon}{t_type}")
                
                st.divider()
                res1, res2 = st.columns([1, 2])
                with res1:
                    st.image(photo, use_column_width=True)
                with res2:
                    st.success(f"✅ AKTIV TASDIQLANDI! (Ishonch: {integrity}%)")
                    st.code(f"Kiber-ID: {tx_hash[:16].upper()}")
                    st.write(f"**Daraxt:** {t_type} | **Kredit:** {co2:.4f} t | **Qiymat:** ${co2*68:.2f}")
                    st.info(f"📍 GPS koordinatalar bazaga muhrlandi: {lat}, {lon}")
        else:
            st.error("Iltimos, avval rasm yuklang!")

# --- 3-BO'LIM: BOZOR ---
elif choice == "💎 Kredit Savdosi":
    st.title("💎 Karbon Kreditlar Birjasi")
    st.info("Sizning kreditlaringizni sotib olishga tayyor global xaridorlar:")
    
    market_data = pd.DataFrame({
        "Xaridor": ["Tesla Global", "Amazon NetZero", "UzAuto Motors", "Google Cloud"],
        "Sotib olish narxi": ["$72.5", "$68.0", "$64.5", "$70.2"],
        "Talab (Ton)": ["5000", "15000", "200", "12000"],
        "Xavfsizlik": ["Verified", "Verified", "High", "Verified"]
    })
    st.table(market_data)
    
    st.subheader("💳 Mening Hisobim")
    st.write("Balansingiz: **0.450 Karbon Kredit ($30.60)**")
    if st.button("Puldagi ekvivalentni yechib olish (Withdraw)"):
        st.warning("Pul mablag'larini yechish uchun hamyoningizni (Metamask/Bank) ulang.")

# --- 4-BO'LIM: TIZIM LOGLARI ---
elif choice == "📜 Tizim Loglari":
    st.title("📜 Blockchain Tranzaksiyalar Logi")
    st.write("Tizimdagi barcha harakatlar SHA-256 shifrlangan holatda saqlanadi.")
    
    log_data = pd.DataFrame({
        "Vaqt": [str(datetime.now()) for _ in range(5)],
        "Harakat": ["New Asset", "Sale", "Verification", "New Asset", "System Audit"],
        "Hash ID": [get_secure_hash(str(i))[:24] for i in range(5)],
        "Status": ["Confirmed", "Success", "Success", "Confirmed", "Secure"]
    })
    st.dataframe(log_data, use_container_width=True)

# Footer
st.sidebar.markdown("---")
st.sidebar.caption("v2.0.4 | Hackathon Edition")
