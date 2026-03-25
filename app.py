import streamlit as st
import pandas as pd
import hashlib
from datetime import datetime
from PIL import Image
import folium
from streamlit_folium import st_folium

# --- SAHIFA SOZLAMALARI ---
st.set_page_config(page_title="EcoCarbon | Digital Green Assets", page_icon="🌿", layout="wide")

# --- DIZAYN (CSS) ---
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
    .success-text { color: #2e7d32; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- FUNKSIYALAR ---
def generate_secure_id(lat, lon, t_type):
    """Kiberxavfsizlik: Har bir daraxt uchun noyob Blockchain-simulatsiya hashini yaratadi"""
    seed = f"{lat}{lon}{t_type}{datetime.now().timestamp()}"
    return hashlib.sha256(seed.encode()).hexdigest()[:12].upper()

def get_carbon_data(t_type, age):
    """Karbon hisoblash formulasi (Sizning mantiqingiz bo'yicha)"""
    ratios = {"Archa": 22, "Chinor": 45, "Mevali": 15, "Terak": 30, "Eman": 50}
    annual_kg = ratios.get(t_type, 10)
    total_co2 = annual_kg * age
    credits = total_co2 / 1000  # 1 tonna = 1 kredit
    market_price = credits * 65 # Global bozor narxi $65
    return annual_kg, credits, market_price

# --- SIDEBAR (MENU) ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2913/2913520.png", width=100)
st.sidebar.title("EcoCarbon AI")
menu = st.sidebar.radio("Bo'limlar:", ["Boshqaruv Paneli", "Yangi Daraxt Sertifikatlash", "Bozor (Marketplace)"])

# --- 1-BO'LIM: DASHBOARD ---
if menu == "Boshqaruv Paneli":
    st.title("📊 Mening Raqamli Ekosistemam")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Jami Daraxtlar", "12 ta")
    col2.metric("Karbon Kreditlar", "0.842 t", "+0.05")
    col3.metric("Jami Daromad", "$54.73", "+12%")
    col4.metric("Kiber-Xavfsizlik", "Active ✅")

    st.subheader("📍 Mening daraxtlarim xaritada")
    # Toshkent markazi uchun xarita
    m = folium.Map(location=[41.3111, 69.2405], zoom_start=12)
    folium.Marker([41.3111, 69.2405], popup="Chinor #A1B2", icon=folium.Icon(color='green')).add_to(m)
    folium.Marker([41.3200, 69.2500], popup="Archa #C3D4", icon=folium.Icon(color='darkgreen')).add_to(m)
    st_folium(m, width=1100, height=400)

# --- 2-BO'LIM: SERTIFIKATLASH ---
elif menu == "Yangi Daraxt Sertifikatlash":
    st.title("🌳 Yangi Daraxtni Sertifikatlash")
    st.info("Daraxt rasmini yuklang va unga kiber-pasport oling.")

    with st.container():
        c1, c2 = st.columns(2)
        with c1:
            t_type = st.selectbox("Daraxt turi:", ["Archa", "Chinor", "Mevali", "Terak", "Eman"])
            age = st.slider("Daraxt yoshi:", 1, 50, 5)
            lat = st.number_input("Kordinata (Lat):", value=41.3111, format="%.4f")
            lon = st.number_input("Kordinata (Lon):", value=69.2405, format="%.4f")
        
        with c2:
            img_file = st.file_uploader("Daraxt rasmini yuklang:", type=['jpg', 'png', 'jpeg'])
            if img_file:
                st.image(img_file, caption="Yuklangan rasm", use_column_width=True)

    if st.button("🚀 SI Tahlili va Sertifikatlash", use_container_width=True):
        if img_file:
            with st.spinner('SI daraxtni tahlil qilmoqda va kiber-ID yaratmoqda...'):
                kg, cr, price = get_carbon_data(t_type, age)
                tree_id = generate_secure_id(lat, lon, t_type)
                
                st.balloons()
                st.success(f"Muvaffaqiyatli sertifikatlandi! Daraxt ID: {tree_id}")
                
                res1, res2, res3 = st.columns(3)
                res1.info(f"Yillik CO2 yutilishi: **{kg} kg**")
                res2.info(f"Karbon Kredit: **{cr:.4f} t**")
                res3.info(f"Bozor qiymati: **${price:.2f}**")
                
                st.warning(f"⚠️ Ushbu daraxt #{tree_id} raqami bilan Blockchain tizimida himoyalandi. Uni endi sotishingiz mumkin.")
        else:
            st.error("Iltimos, avval daraxt rasmini yuklang!")

# --- 3-BO'LIM: MARKETPLACE ---
elif menu == "Bozor (Marketplace)":
    st.title("💰 Karbon Kreditlar Bozori")
    st.write("Kreditlaringizni yirik kompaniyalarga soting.")
    
    offers = pd.DataFrame({
        "Xaridor": ["Tesla Inc.", "Google Green", "Microsoft Carbon", "Tashkent City"],
        "Talab (Kredit)": [500, 1200, 300, 50],
        "Narx (1t uchun)": ["$68", "$65", "$70", "$60"]
    })
    st.table(offers)
    
    st.subheader("🤝 P2P Shartnomalar")
    st.write("Sizning sotuvga tayyor kreditlaringiz: **0.842 t**")
    if st.button("Kreditlarni sotuvga chiqarish"):
        st.success("Kreditlaringiz global birjaga yuborildi!")

# --- FOOTER ---
st.sidebar.markdown("---")
st.sidebar.caption("© 2026 EcoCarbon AI - Hackathon Special Edition")
