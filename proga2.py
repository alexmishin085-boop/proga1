import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Circle • Dubai", page_icon="🔥", layout="centered")

# ====================== PREMIUM CSS ======================
st.markdown("""
<style>
    .stApp { background: linear-gradient(135deg, #0f172a, #1e2937); color: white; }
    .glass { background: rgba(255,255,255,0.09); 
              backdrop-filter: blur(32px) saturate(180%); 
              border-radius: 28px; 
              border: 1px solid rgba(234,179,8,0.25); 
              box-shadow: 0 25px 50px -12px rgb(0 0 0 / 0.6); padding: 24px; }
    .gold { color: #eab308; }
    .title { font-family: 'Playfair Display', serif; letter-spacing: -0.06em; font-weight: 700; }
    .live { animation: pulse 2s infinite; }
    @keyframes pulse { 0%,100% { opacity: 1; } 50% { opacity: 0.4; } }
</style>
""", unsafe_allow_html=True)

# ====================== SESSION STATE ======================
if 'onboarded' not in st.session_state:
    st.session_state.onboarded = False
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Energy"
if 'messages' not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Привет, Алексей! Готов к движу сегодня?"}]

# ====================== ONBOARDING ======================
if not st.session_state.onboarded:
    st.markdown("<h1 class='title text-7xl text-center gold'>Circle</h1>", unsafe_allow_html=True)
    st.markdown("<p class='text-center text-2xl text-zinc-300 mt-6'>The Social OS for Dubai</p>", unsafe_allow_html=True)
    st.markdown("<p class='text-center text-xl mt-12 mb-8'>Build your real life through movement and meaningful people.</p>", unsafe_allow_html=True)

    st.markdown("### Кто ты?")
    if st.button("Founder / Entrepreneur", type="primary", use_container_width=True):
        st.session_state.onboarded = True
        st.rerun()
    if st.button("Русскоязычный экспат", use_container_width=True):
        st.session_state.onboarded = True
        st.rerun()
    if st.button("Premium Wellness & Lifestyle", use_container_width=True):
        st.session_state.onboarded = True
        st.rerun()
    if st.button("Padel & Elite Community", use_container_width=True):
        st.session_state.onboarded = True
        st.rerun()
    st.stop()

# ====================== SIDEBAR ======================
st.sidebar.markdown("<h1 class='title text-5xl gold'>Circle</h1>", unsafe_allow_html=True)
st.sidebar.caption("Dubai • Social Operating System")

pages = {
    "🏠 Energy": "Energy",
    "🗺️ Live Map": "Live Map",
    "💬 Chat": "Chat",
    "🔍 Discover": "Discover",
    "🌀 Circles": "Circles",
    "👤 Profile": "Profile"
}

selected = st.sidebar.radio("Навигация", options=pages.keys(), label_visibility="collapsed")
st.session_state.current_page = pages[selected]

# ====================== MAIN PAGES ======================
if st.session_state.current_page == "Energy":
    st.markdown("<h1 class='title text-5xl text-center'>Добро пожаловать, Алексей</h1>", unsafe_allow_html=True)
    st.markdown(f"<p class='text-emerald-400 text-xl text-center'>**392** человека в движении сейчас <span class='live'>● LIVE</span></p>", unsafe_allow_html=True)

    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.subheader("AI Match • 98%")
    st.write("**Дмитрий** — Ex-Y Combinator Fintech Founder\n1.2 км от тебя • Ищет падел + бизнес разговор")
    if st.button("Написать Дмитрию сейчас", type="primary", use_container_width=True):
        st.success("Сообщение отправлено! Дмитрий ответил: «19:30 в Emirates Padel Club?»")
        st.balloons()
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.current_page == "Live Map":
    st.title("Live Map • Dubai")
    st.write("Кто из твоего круга активен прямо сейчас")
    try:
        import folium
        from streamlit_folium import st_folium
        m = folium.Map(location=[25.2048, 55.2708], zoom_start=12, tiles="CartoDB dark_matter")
        folium.Marker([25.2048, 55.2708], popup="Marina — 12 человек", icon=folium.Icon(color="gold")).add_to(m)
        folium.Marker([25.0775, 55.1400], popup="Downtown — 8 человек", icon=folium.Icon(color="green")).add_to(m)
        st_folium(m, width=700, height=500)
    except:
        st.error("Карта загружается... (убедись, что streamlit-folium установлен)")

elif st.session_state.current_page == "Chat":
    st.title("Чат с Дмитрием")
    st.caption("Онлайн • 2 минуты назад")

    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f"<div style='text-align:right; margin: 8px 0;'><span style='background:#eab308; color:black; padding:12px 18px; border-radius:20px 20px 4px 20px;'>{msg['content']}</span></div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='glass' style='display:inline-block; margin:8px 0;'>{msg['content']}</div>", unsafe_allow_html=True)

    prompt = st.chat_input("Напиши сообщение...")
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.session_state.messages.append({"role": "assistant", "content": "Круто! Давай сегодня в 19:30 в Emirates Padel?"})
        st.rerun()

elif st.session_state.current_page == "Discover":
    st.title("Discover")
    st.subheader("Рекомендуемые люди")
    if st.button("Отправить запрос Анне (Wellness Founder)"):
        st.success("Запрос отправлен! Анна приняла его.")

elif st.session_state.current_page == "Circles":
    st.title("Мои Circles")
    st.markdown('<div class="glass"><h3>Founders Padel Club</h3><p>Ты — Ambassador • Level 9</p></div>', unsafe_allow_html=True)
    st.button("Создать новый Circle", type="primary", use_container_width=True)

elif st.session_state.current_page == "Profile":
    st.title("Твой профиль")
    st.markdown("<h2 class='gold text-4xl'>Level 9 • Rising Luminary</h2>", unsafe_allow_html=True)
    st.metric("Social Capital", "3,420", "↑ 240 сегодня")

# Footer
st.sidebar.caption(f"🕒 {datetime.now().strftime('%H:%M')} • Dubai, UAE")
st.sidebar.caption("v12 • Стабильная версия")