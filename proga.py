import streamlit as st
from datetime import datetime
import time

st.set_page_config(page_title="Circle • Dubai", page_icon="🔥", layout="centered")

# ==================== PREMIUM DESIGN ====================
st.markdown("""
<style>
    .stApp { background: linear-gradient(135deg, #0f172a, #1e2937); color: white; }
    .glass { background: rgba(255,255,255,0.085); 
              backdrop-filter: blur(32px) saturate(180%); 
              border-radius: 28px; 
              border: 1px solid rgba(234,179,8,0.25); 
              box-shadow: 0 25px 50px -12px rgb(0 0 0 / 0.6); padding: 24px; }
    .gold { color: #eab308; }
    .title { font-family: 'Playfair Display', serif; letter-spacing: -0.06em; font-weight: 700; }
    .live { animation: pulse 2s infinite; }
    @keyframes pulse { 0%,100% { opacity: 1; } 50% { opacity: 0.4; } }
    .message-user { background: #eab308; color: black; padding: 12px 18px; border-radius: 20px 20px 4px 20px; max-width: 80%; margin-left: auto; }
    .message-assistant { background: rgba(255,255,255,0.1); padding: 12px 18px; border-radius: 20px 20px 20px 4px; }
</style>
""", unsafe_allow_html=True)

# ==================== SESSION STATE ====================
if "onboarded" not in st.session_state:
    st.session_state.onboarded = False
if "page" not in st.session_state:
    st.session_state.page = "Energy"
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Привет, Алексей! Как прошёл твой день в Дубае?"}]
if "live_count" not in st.session_state:
    st.session_state.live_count = 392

# ==================== ONBOARDING ====================
if not st.session_state.onboarded:
    st.markdown("<h1 class='title text-7xl text-center gold'>Circle</h1>", unsafe_allow_html=True)
    st.markdown("<p class='text-center text-2xl text-zinc-300 mt-6'>The Social OS for Dubai</p>", unsafe_allow_html=True)
    st.markdown("<p class='text-center text-xl mt-12'>Build your real life through movement and meaningful people.</p>", unsafe_allow_html=True)
    
    st.markdown("### Кто ты сегодня?")
    cols = st.columns(2)
    with cols[0]:
        if st.button("Founder / Entrepreneur", use_container_width=True, type="primary"):
            st.session_state.onboarded = True
            st.rerun()
    with cols[1]:
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

# ==================== SIDEBAR ====================
st.sidebar.markdown("<h1 class='title text-5xl gold'>Circle</h1>", unsafe_allow_html=True)
st.sidebar.caption("Dubai • Social Operating System")
page = st.sidebar.radio("Навигация", 
    ["🏠 Energy", "🗺️ Live Map", "💬 Chat", "🔍 Discover", "🌀 Circles", "👤 Profile"],
    label_visibility="collapsed", index=["Energy", "Live Map", "Chat", "Discover", "Circles", "Profile"].index(st.session_state.page))

st.session_state.page = page

# ==================== PAGES ====================

if page == "🏠 Energy":
    st.markdown(f"<h1 class='title text-5xl text-center'>Добро пожаловать, Алексей</h1>", unsafe_allow_html=True)
    st.markdown(f"<p class='text-emerald-400 text-xl text-center'>**{st.session_state.live_count}** человек в движении прямо сейчас <span class='live'>● LIVE</span></p>", unsafe_allow_html=True)
    
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.markdown("**AI Match • 98%**")
    st.write("**Дмитрий** — Ex-Y Combinator, Fintech Founder\n\nИщет партнёра на падел + обсуждение раунда $3M. 1.2 км от тебя.")
    if st.button("Написать Дмитрию сейчас", type="primary", use_container_width=True):
        st.success("Сообщение отправлено! Дмитрий ответил за 8 минут: «19:30 в Emirates Padel — идеально»")
        st.balloons()
    st.markdown('</div>', unsafe_allow_html=True)

    st.info("14 человек из твоего круга уже активны в Marina, Downtown и JLT")

elif page == "🗺️ Live Map":
    st.title("Live Map • Dubai")
    st.write("Люди из твоего круга прямо сейчас")
    
    import folium
    from streamlit_folium import st_folium
    m = folium.Map(location=[25.2048, 55.2708], zoom_start=12, tiles="CartoDB dark_matter")
    folium.Marker([25.2048, 55.2708], popup="Marina — 12 человек играют в падел", icon=folium.Icon(color="gold", icon="star")).add_to(m)
    folium.Marker([25.0775, 55.1400], popup="Downtown — 7 человек на пробежке", icon=folium.Icon(color="green")).add_to(m)
    folium.Marker([25.2358, 55.2892], popup="JLT — Wellness Circle", icon=folium.Icon(color="blue")).add_to(m)
    st_folium(m, width=700, height=520)

elif page == "💬 Chat":
    st.title("Чат с Дмитрием")
    st.caption("Он онлайн • ответил 3 минуты назад")
    
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f"<div class='message-user'>{msg['content']}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='glass message-assistant'>{msg['content']}</div>", unsafe_allow_html=True)
    
    prompt = st.chat_input("Напиши сообщение...")
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.session_state.messages.append({"role": "assistant", "content": "Отлично! Давай сегодня в 19:30 в Emirates Padel Club?"})
        st.rerun()

elif page == "🔍 Discover":
    st.title("Discover")
    st.subheader("Люди, которых тебе стоит знать")
    col1, col2 = st.columns(2)
    with col1:
        st.success("Анна • 34 • Wellness Founder")
        if st.button("Отправить запрос Анне"):
            st.balloons()
            st.success("Анна приняла запрос!")
    with col2:
        st.info("Ахмед • Real Estate • Ищет теннис-партнёра")

elif page == "🌀 Circles":
    st.title("Мои Circles")
    st.markdown('<div class="glass"><h3>Founders Padel Club</h3><p>Ты — Ambassador • Level 9 • 47 участников</p></div>', unsafe_allow_html=True)
    st.button("Создать свой закрытый Circle", type="primary", use_container_width=True)

elif page == "👤 Profile":
    st.title("Твой профиль")
    st.markdown("<h2 class='gold text-4xl'>Level 9 • Rising Luminary</h2>", unsafe_allow_html=True)
    st.metric("Social Capital", "3,420", "↑ 240 сегодня")
    st.write("Badges: Padel Elite • First Mover • Dubai Connector • Community Architect")

# ==================== FOOTER ====================
st.sidebar.caption(f"🕒 {datetime.now().strftime('%H:%M')} • Dubai, UAE")
st.sidebar.caption("v11 • Полностью готовое приложение")