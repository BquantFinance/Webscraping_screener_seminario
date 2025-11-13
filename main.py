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
        background: linear-gradient(135deg, #00d4ff, #00ffaa);
        border-radius: 25px;
        padding: 50px;
        margin: 60px 0 40px 0;
        text-align: center;
    }
    
    .price-amount {
        font-size: 5rem;
        font-weight: 900;
        color: #000000;
        margin: 20px 0;
    }
    
    .price-label {
        font-size: 1.5rem;
        font-weight: 700;
        color: #000000;
        margin-bottom: 30px;
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
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1>&#128640; FINANCIAL SCREENER MASTERCLASS</h1>", unsafe_allow_html=True)
st.markdown("<p style='font-size: 1.5rem; color: #00ffaa; margin-bottom: 50px;'>Web Scraping + Stock Screening en Python | 3 Horas Intensivas</p>", unsafe_allow_html=True)

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
            Fundamental • Técnico • Calidad<br>
            Piotroski • Altman Z-Score • Sloan Ratio
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
            AUM • Expense Ratio • Fund Flows<br>
            NAV Performance • Holdings
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
            DEX Analytics • On-chain • Market Cap<br>
            Liquidity • Volume 24h
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
        <div class='asset-label'>Majors • Minors • Exotics</div>
        <div class='asset-metrics'>379 métricas/par</div>
        <div class='asset-label' style='margin-top: 15px; font-size: 0.95rem;'>
            Análisis Técnico Completo<br>
            Bid-Ask Spread • Volatility
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
                160€/mes = 1,920€/año
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
        <strong style='color: #00d4ff;'>Web Scraping:</strong> Extrae datos que otros no tienen acceso<br>
        <strong style='color: #00ffaa;'>Screening:</strong> Filtra 162K instrumentos en segundos<br>
        <strong style='color: #ffaa00;'>Combinación:</strong> Sistema único que nadie más tiene<br><br>
        <span class='highlight'>Detecta oportunidades antes que el mercado</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Price Section
st.markdown("""
<div class='price-section'>
    <div class='price-label'>INVERSIÓN ÚNICA</div>
    <div class='price-amount'>89€</div>
    <div style='font-size: 1.3rem; color: #000000; font-weight: 600; margin-top: 20px;'>
        &#9989; 3 horas de seminario en vivo (Zoom)<br>
        &#9989; Grabación con acceso ilimitado<br>
        &#9989; 4 bases de datos completas (162K+ instrumentos)<br>
        &#9989; Todo el código fuente documentado<br>
        &#9989; Pipeline ETL profesional<br>
        &#9989; 15 casos prácticos resueltos<br>
        &#9989; Soporte 30 días
    </div>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div style='text-align: center; margin: 50px 0; padding: 40px;'>
    <p style='font-size: 1.5rem; color: #00d4ff; font-weight: 700;'>
        &#128640; De análisis manual a sistema profesional en 3 horas
    </p>
    <p style='font-size: 1.1rem; color: #888; margin-top: 30px;'>
        &copy; 2024 BQuant Finance | @Gsnchez | bquantfinance.com
    </p>
</div>
""", unsafe_allow_html=True)
