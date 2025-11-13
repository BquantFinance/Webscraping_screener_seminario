import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Financial Screener Masterclass",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
    }
    
    h1 {
        color: #00d4ff;
        text-align: center;
        font-size: 3.5rem !important;
        font-weight: 900 !important;
        text-shadow: 0 0 30px rgba(0, 212, 255, 0.6);
        margin-bottom: 15px;
        margin-top: 30px;
    }
    
    h2 {
        color: #00ffaa;
        font-size: 2rem !important;
        font-weight: 700 !important;
        text-align: center;
        margin: 40px 0 30px 0;
    }
    
    p {
        color: #ffffff;
        font-size: 1.2rem;
        line-height: 1.6;
        text-align: center;
    }
    
    .asset-card {
        background: linear-gradient(135deg, rgba(0, 212, 255, 0.15), rgba(0, 255, 170, 0.15));
        border: 2px solid rgba(0, 212, 255, 0.4);
        border-radius: 20px;
        padding: 30px;
        margin: 20px 0;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .asset-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(0, 212, 255, 0.3);
        border-color: rgba(0, 212, 255, 0.8);
    }
    
    .asset-icon {
        font-size: 4rem;
        margin-bottom: 15px;
    }
    
    .asset-title {
        font-size: 2rem;
        font-weight: 800;
        color: #00d4ff;
        margin: 15px 0;
    }
    
    .asset-stat {
        font-size: 3rem;
        font-weight: 900;
        color: #00ffaa;
        margin: 10px 0;
    }
    
    .asset-label {
        font-size: 1.1rem;
        color: #ffffff;
        margin: 5px 0;
    }
    
    .asset-metrics {
        font-size: 1.5rem;
        font-weight: 700;
        color: #ffaa00;
        margin-top: 15px;
    }
    
    .price-section {
        background: linear-gradient(135deg, #00f5ff 0%, #00ffaa 25%, #00f5ff 50%, #00ffaa 75%, #00f5ff 100%);
        background-size: 300% 300%;
        border-radius: 25px;
        padding: 50px;
        margin: 60px 0 40px 0;
        text-align: center;
        animation: gradient-flow 4s ease infinite;
        box-shadow: 0 0 40px rgba(0, 255, 170, 0.6), 0 0 80px rgba(0, 245, 255, 0.4);
        border: 3px solid rgba(0, 255, 255, 0.8);
        position: relative;
        overflow: hidden;
    }
    
    .price-section::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, transparent, rgba(255, 255, 255, 0.3), transparent);
        animation: shine 3s infinite;
    }
    
    @keyframes gradient-flow {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    @keyframes shine {
        0% { transform: translateX(-100%) translateY(-100%) rotate(45deg); }
        100% { transform: translateX(100%) translateY(100%) rotate(45deg); }
    }
    
    .price-amount {
        font-size: 6rem;
        font-weight: 900;
        color: #000000;
        margin: 20px 0;
        text-shadow: 0 0 20px rgba(255, 255, 255, 0.8);
        animation: scale-pulse 2s ease-in-out infinite;
        position: relative;
        z-index: 1;
    }
    
    @keyframes scale-pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }
    
    .price-label {
        font-size: 1.5rem;
        font-weight: 700;
        color: #000000;
        margin-bottom: 30px;
        position: relative;
        z-index: 1;
    }
    
    .benefit-box {
        background: rgba(0, 0, 0, 0.3);
        border-radius: 15px;
        padding: 30px;
        margin: 30px 0;
    }
    
    .benefit-title {
        font-size: 2rem;
        font-weight: 800;
        color: #00d4ff;
        margin-bottom: 20px;
        text-align: center;
    }
    
    .benefit-text {
        font-size: 1.3rem;
        color: #ffffff;
        line-height: 1.8;
        text-align: center;
    }
    
    .highlight {
        color: #00ffaa;
        font-weight: 800;
    }
    
    .cta-button {
        display: block;
        background: linear-gradient(135deg, #ff0080, #ff8c00, #ff0080);
        background-size: 300% 300%;
        color: #ffffff;
        font-size: 2.5rem;
        font-weight: 900;
        text-align: center;
        padding: 35px 70px;
        border-radius: 60px;
        text-decoration: none;
        margin: 50px auto;
        max-width: 700px;
        box-shadow: 0 0 30px rgba(255, 0, 128, 0.6), 0 0 60px rgba(255, 140, 0, 0.4), 0 15px 50px rgba(255, 0, 128, 0.5);
        animation: button-glow 3s ease infinite, button-float 3s ease-in-out infinite;
        border: 4px solid #ffffff;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
        text-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
    }
    
    .cta-button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent);
        animation: slide-shine 2s infinite;
    }
    
    @keyframes slide-shine {
        0% { left: -100%; }
        100% { left: 100%; }
    }
    
    .cta-button:hover {
        transform: scale(1.08) translateY(-8px);
        box-shadow: 0 0 50px rgba(255, 0, 128, 0.9), 0 0 100px rgba(255, 140, 0, 0.7), 0 20px 70px rgba(255, 0, 128, 0.8);
        text-decoration: none;
        color: #ffffff;
    }
    
    @keyframes button-glow {
        0%, 100% { 
            box-shadow: 0 0 30px rgba(255, 0, 128, 0.6), 0 0 60px rgba(255, 140, 0, 0.4), 0 15px 50px rgba(255, 0, 128, 0.5);
            background-position: 0% 50%;
        }
        50% { 
            box-shadow: 0 0 50px rgba(255, 0, 128, 0.9), 0 0 100px rgba(255, 140, 0, 0.7), 0 15px 70px rgba(255, 0, 128, 0.8);
            background-position: 100% 50%;
        }
    }
    
    @keyframes button-float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    .urgency-text {
        text-align: center;
        font-size: 1.5rem;
        color: #ff0080;
        font-weight: 900;
        margin: 20px 0;
        animation: blink-urgent 1.5s ease-in-out infinite;
        text-shadow: 0 0 20px rgba(255, 0, 128, 0.8);
    }
    
    @keyframes blink-urgent {
        0%, 100% { 
            opacity: 1; 
            transform: scale(1);
        }
        50% { 
            opacity: 0.7;
            transform: scale(1.05);
        }
    }
    
    .includes-list {
        position: relative;
        z-index: 1;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1>&#128640; FINANCIAL SCREENER MASTERCLASS</h1>", unsafe_allow_html=True)
st.markdown("<p style='font-size: 1.5rem; color: #00ffaa; margin-bottom: 30px;'>Web Scraping + Stock Screening en Python | 3 Horas Intensivas</p>", unsafe_allow_html=True)

# CTA Button at the TOP - SUPER FLASHY!
st.markdown("""
<div style='text-align: center; margin: 40px 0 60px 0;'>
    <p class='urgency-text'>&#9889;&#9889;&#9889; PLAZAS LIMITADAS &#9889;&#9889;&#9889;</p>
    <a href='https://bquantfinance.com/courses/seminario-scraping-screener/' target='_blank' class='cta-button'>
        &#128293;&#128293; INSCRÍBETE AHORA &#128293;&#128293;
    </a>
</div>
""", unsafe_allow_html=True)

st.markdown("<h2>&#128202; Las 4 Bases de Datos</h2>", unsafe_allow_html=True)

# Asset Cards
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class='asset-card'>
        <div class='asset-icon'>&#128200;</div>
        <div class='asset-title'>STOCKS</div>
        <div class='asset-stat'>58,168</div>
        <div class='asset-label'>Acciones Globales</div>
        <div class='asset-label'>64 Países | 90 Exchanges</div>
        <div class='asset-metrics'>982 métricas/acción</div>
        <div class='asset-label' style='margin-top: 15px; font-size: 0.95rem;'>
            Fundamental &bull; Técnico &bull; Calidad<br>
            Piotroski &bull; Altman Z-Score &bull; Sloan Ratio
        </div>
    </div>
    """, unsafe_allow_html=True)
    
with col2:
    st.markdown("""
    <div class='asset-card'>
        <div class='asset-icon'>&#128188;</div>
        <div class='asset-title'>ETFs</div>
        <div class='asset-stat'>30,167</div>
        <div class='asset-label'>Fondos Cotizados</div>
        <div class='asset-label'>Todas las categorías y regiones</div>
        <div class='asset-metrics'>202 métricas/fondo</div>
        <div class='asset-label' style='margin-top: 15px; font-size: 0.95rem;'>
            AUM &bull; Expense Ratio &bull; Fund Flows<br>
            NAV Performance &bull; Holdings
        </div>
    </div>
    """, unsafe_allow_html=True)

col3, col4 = st.columns(2)

with col3:
    st.markdown("""
    <div class='asset-card'>
        <div class='asset-icon'>&#8383;</div>
        <div class='asset-title'>CRYPTO</div>
        <div class='asset-stat'>67,476</div>
        <div class='asset-label'>Criptomonedas & Tokens</div>
        <div class='asset-label'>CEX + DEX | Todas las blockchains</div>
        <div class='asset-metrics'>421 métricas/crypto</div>
        <div class='asset-label' style='margin-top: 15px; font-size: 0.95rem;'>
            DEX Analytics &bull; On-chain &bull; Market Cap<br>
            Liquidity &bull; Volume 24h
        </div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class='asset-card'>
        <div class='asset-icon'>&#128177;</div>
        <div class='asset-title'>FOREX</div>
        <div class='asset-stat'>7,174</div>
        <div class='asset-label'>Pares de Divisas</div>
        <div class='asset-label'>Majors &bull; Minors &bull; Exotics</div>
        <div class='asset-metrics'>379 métricas/par</div>
        <div class='asset-label' style='margin-top: 15px; font-size: 0.95rem;'>
            Análisis Técnico Completo<br>
            Bid-Ask Spread &bull; Volatility
        </div>
    </div>
    """, unsafe_allow_html=True)

# Total Summary
st.markdown("""
<div style='text-align: center; margin: 50px 0; padding: 30px; background: rgba(0, 212, 255, 0.1); border-radius: 15px;'>
    <p style='font-size: 2.5rem; font-weight: 900; color: #00d4ff; margin-bottom: 10px;'>
        162,985 INSTRUMENTOS TOTALES
    </p>
    <p style='font-size: 1.3rem; color: #ffffff;'>
        Un solo sistema para analizar todos los mercados financieros
    </p>
</div>
""", unsafe_allow_html=True)

# Why Section
st.markdown("<h2>&#128161; Por Qué Es Crítico</h2>", unsafe_allow_html=True)

col5, col6 = st.columns(2)

with col5:
    st.markdown("""
    <div class='benefit-box' style='background: rgba(255, 100, 100, 0.15); border-left: 4px solid #ff6b6b;'>
        <div class='benefit-title' style='color: #ff6b6b;'>&#10060; Screeners Online</div>
        <div class='benefit-text' style='font-size: 1.2rem;'>
            500-5,000 instrumentos<br>
            20-80 métricas básicas<br>
            Una sola asset class<br>
            Sin personalización<br>
            Caja negra<br><br>
            <span style='font-size: 1.5rem; font-weight: 800; color: #ff6b6b;'>
                XX€/mes
            </span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col6:
    st.markdown("""
    <div class='benefit-box' style='background: rgba(0, 255, 170, 0.15); border-left: 4px solid #00ffaa;'>
        <div class='benefit-title' style='color: #00ffaa;'>&#9989; Tu Sistema</div>
        <div class='benefit-text' style='font-size: 1.2rem;'>
            162,985 instrumentos<br>
            600+ métricas/instrumento<br>
            4 asset classes integradas<br>
            Control total + código<br>
            Cross-asset analysis<br><br>
            <span style='font-size: 1.5rem; font-weight: 800; color: #00ffaa;'>
                89€ una sola vez
            </span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Web Scraping + Screening Value
st.markdown("""
<div class='benefit-box'>
    <div class='benefit-title'>&#128295; Web Scraping + Screening = Ventaja Competitiva</div>
    <div class='benefit-text'>
        <strong style='color: #00d4ff;'>Web Scraping:</strong> Extrae datos que otros no tienen.<br>
        <strong style='color: #00ffaa;'>Screening:</strong> Filtra 162K instrumentos.<br>
        <strong style='color: #ffaa00;'>Combinación:</strong> Sistema único.<br><br>
        <span class='highlight'>Detecta oportunidades antes que el mercado</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Price Section - NUEVO DISEÑO MÁS FLASHY
st.markdown("""
<div class='price-section'>
    <div class='price-label'>INVERSIÓN ÚNICA</div>
    <div class='price-amount'>89€</div>
    <div class='includes-list' style='font-size: 1.3rem; color: #000000; font-weight: 600; margin-top: 20px;'>
        &#9989; 3 horas de seminario en vivo (Zoom)<br>
        &#9989; Grabación con acceso ilimitado<br>
        &#9989; 4 bases de datos completas (162K+ instrumentos)<br>
        &#9989; Todo el código fuente documentado<br>
        &#9989; Pipeline ETL profesional<br>
    </div>
</div>
""", unsafe_allow_html=True)

# CTA Button BOTTOM - SUPER FLASHY!
st.markdown("""
<div style='text-align: center; margin: 60px 0;'>
    <p class='urgency-text'>&#9889;&#9889;&#9889; PLAZAS LIMITADAS &#9889;&#9889;&#9889;</p>
    <a href='https://bquantfinance.com/courses/seminario-scraping-screener/' target='_blank' class='cta-button'>
        &#128293;&#128293; INSCRÍBETE AHORA &#128293;&#128293;
    </a>
    <p class='urgency-text' style='margin-top: 20px;'>&#9201; Última oportunidad</p>
</div>
""", unsafe_allow_html=True)

# Extra flashy reminder
st.markdown("""
<div style='text-align: center; margin: 40px 0; padding: 40px; background: linear-gradient(135deg, rgba(255, 0, 128, 0.2), rgba(255, 140, 0, 0.2)); border-radius: 20px; border: 2px solid #ff0080; box-shadow: 0 0 30px rgba(255, 0, 128, 0.4);'>
    <p style='font-size: 2rem; font-weight: 900; color: #ff0080; margin-bottom: 15px; text-shadow: 0 0 20px rgba(255, 0, 128, 0.6);'>
        &#11088; NO PIERDAS ESTA OPORTUNIDAD &#11088;
    </p>
    <p style='font-size: 1.4rem; color: #ffffff; line-height: 1.8;'>
        Construye tu propio sistema de screening profesional<br>
        <span style='color: #00ffaa; font-weight: 800;'>162,985 instrumentos</span> &bull; 
        <span style='color: #00d4ff; font-weight: 800;'>4 asset classes</span> &bull; 
        <span style='color: #ffaa00; font-weight: 800;'>Control total</span><br><br>
        <strong style='font-size: 1.8rem; color: #ff0080; text-shadow: 0 0 15px rgba(255, 0, 128, 0.8);'>Solo 89€</strong>
    </p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div style='text-align: center; margin: 50px 0; padding: 40px;'>
    <p style='font-size: 1.5rem; color: #00d4ff; font-weight: 700;'>
        &#128640; De análisis manual a sistema automático.
    </p>
    <p style='font-size: 1.1rem; color: #888; margin-top: 30px;'>
        &copy; 2025 BQuantFinance | @Gsnchez | bquantfinance.com
    </p>
</div>
""", unsafe_allow_html=True)
