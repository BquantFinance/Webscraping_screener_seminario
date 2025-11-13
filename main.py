import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Stock Screener Masterclass",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for dark mode and beautiful styling
st.markdown("""
<style>
    /* Main background and text */
    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
    }
    
    /* Headers */
    h1 {
        color: #00d4ff;
        text-align: center;
        font-size: 3.5rem !important;
        font-weight: 800 !important;
        text-shadow: 0 0 20px rgba(0, 212, 255, 0.5);
        padding: 20px 0;
        margin-bottom: 30px;
    }
    
    h2 {
        color: #00d4ff;
        font-size: 2rem !important;
        font-weight: 700 !important;
        margin-top: 40px;
        margin-bottom: 20px;
        border-bottom: 3px solid #00d4ff;
        padding-bottom: 10px;
    }
    
    h3 {
        color: #00ffaa;
        font-size: 1.5rem !important;
        font-weight: 600 !important;
        margin-top: 20px;
    }
    
    /* Metric cards */
    .metric-card {
        background: linear-gradient(135deg, rgba(0, 212, 255, 0.1) 0%, rgba(0, 255, 170, 0.1) 100%);
        border-radius: 15px;
        padding: 25px;
        margin: 15px 0;
        border: 2px solid rgba(0, 212, 255, 0.3);
        box-shadow: 0 8px 32px rgba(0, 212, 255, 0.2);
        transition: all 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(0, 212, 255, 0.4);
        border-color: rgba(0, 212, 255, 0.6);
    }
    
    .big-number {
        font-size: 3rem;
        font-weight: 800;
        color: #00d4ff;
        text-shadow: 0 0 10px rgba(0, 212, 255, 0.5);
    }
    
    .metric-label {
        font-size: 1.1rem;
        color: #ffffff;
        margin-top: 10px;
    }
    
    /* Feature boxes */
    .feature-box {
        background: rgba(0, 212, 255, 0.05);
        border-left: 4px solid #00d4ff;
        padding: 20px;
        margin: 15px 0;
        border-radius: 8px;
        backdrop-filter: blur(10px);
    }
    
    .feature-box:hover {
        background: rgba(0, 212, 255, 0.1);
        border-left-width: 6px;
    }
    
    /* Lists */
    .stMarkdown ul {
        list-style-type: none;
        padding-left: 0;
    }
    
    .stMarkdown li {
        padding: 10px 0;
        font-size: 1.1rem;
        color: #ffffff;
    }
    
    .stMarkdown li:before {
        content: "✓ ";
        color: #00ffaa;
        font-weight: bold;
        font-size: 1.3rem;
        margin-right: 10px;
    }
    
    /* Highlight boxes */
    .highlight-box {
        background: linear-gradient(135deg, rgba(0, 255, 170, 0.15) 0%, rgba(0, 212, 255, 0.15) 100%);
        border-radius: 15px;
        padding: 30px;
        margin: 25px 0;
        border: 2px solid rgba(0, 255, 170, 0.3);
        box-shadow: 0 8px 32px rgba(0, 255, 170, 0.2);
    }
    
    /* Price tag */
    .price-tag {
        background: linear-gradient(135deg, #00d4ff 0%, #00ffaa 100%);
        color: #000000;
        padding: 30px 60px;
        font-size: 3rem;
        font-weight: 900;
        border-radius: 20px;
        text-align: center;
        margin: 30px auto;
        box-shadow: 0 10px 40px rgba(0, 212, 255, 0.5);
        display: inline-block;
    }
    
    /* CTA Button */
    .cta-button {
        background: linear-gradient(135deg, #00d4ff 0%, #00ffaa 100%);
        color: #000000;
        padding: 20px 50px;
        font-size: 1.5rem;
        font-weight: 800;
        border-radius: 50px;
        border: none;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        margin: 30px auto;
        cursor: pointer;
        box-shadow: 0 10px 40px rgba(0, 212, 255, 0.4);
        transition: all 0.3s ease;
    }
    
    .cta-button:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 50px rgba(0, 212, 255, 0.6);
    }
    
    /* Stats grid */
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 20px;
        margin: 30px 0;
    }
    
    /* Sidebar */
    .css-1d391kg {
        background: linear-gradient(180deg, #1a1a2e 0%, #16213e 100%);
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background: rgba(0, 212, 255, 0.1);
        border-radius: 8px;
        color: #00d4ff !important;
        font-weight: 600;
    }
    
    /* Divider */
    hr {
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, #00d4ff, transparent);
        margin: 40px 0;
    }
    
    /* Badge */
    .badge {
        display: inline-block;
        padding: 8px 15px;
        background: rgba(0, 212, 255, 0.2);
        border: 1px solid #00d4ff;
        border-radius: 20px;
        color: #00d4ff;
        font-weight: 600;
        margin: 5px;
        font-size: 0.9rem;
    }
    
    /* Table styling */
    .dataframe {
        background: rgba(0, 0, 0, 0.3);
        border-radius: 10px;
        padding: 10px;
    }
    
    /* Section divider */
    .section-divider {
        height: 3px;
        background: linear-gradient(90deg, #00d4ff, #00ffaa, #00d4ff);
        margin: 50px 0;
        border-radius: 3px;
    }
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("<h1>🚀 STOCK SCREENER MASTERCLASS</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.5rem; color: #00ffaa; margin-bottom: 50px;'>Domina el Web Scraping y Stock Screening con Python</p>", unsafe_allow_html=True)

# Key Stats Section
st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class='metric-card'>
        <div class='big-number'>58,168</div>
        <div class='metric-label'>Acciones Globales</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='metric-card'>
        <div class='big-number'>982</div>
        <div class='metric-label'>Métricas por Acción</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='metric-card'>
        <div class='big-number'>64</div>
        <div class='metric-label'>Mercados Cubiertos</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class='metric-card'>
        <div class='big-number'>57M+</div>
        <div class='metric-label'>Datos Totales</div>
    </div>
    """, unsafe_allow_html=True)

# About Section
st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)
st.markdown("## 🎯 ¿Qué Aprenderás?")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class='highlight-box'>
        <h3>📡 Web Scraping de Datos Financieros</h3>
        <ul>
            <li>Extracción masiva de datos desde APIs financieras</li>
            <li>Técnicas de scraping a gran escala</li>
            <li>Manejo de peticiones, headers y autenticación</li>
            <li>Procesamiento y limpieza de datos financieros</li>
            <li>Construcción de pipelines ETL automatizados</li>
            <li>Almacenamiento eficiente en DataFrames</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='highlight-box'>
        <h3>🔍 Construcción de Screeners Avanzados</h3>
        <ul>
            <li>Arquitectura de screeners profesionales</li>
            <li>Filtros multi-criterio y combinaciones lógicas</li>
            <li>Sistemas de scoring y ranking personalizados</li>
            <li>Backtesting de estrategias de screening</li>
            <li>Dashboards interactivos con visualizaciones</li>
            <li>Exportación y reporting automatizado</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Database Features
st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)
st.markdown("## 💎 La Base de Datos Más Completa")

tab1, tab2, tab3, tab4 = st.tabs(["📊 Análisis Fundamental", "📈 Análisis Técnico", "🎯 Métricas de Calidad", "🌍 Cobertura Global"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class='feature-box'>
            <h3>Valoración (27 métricas)</h3>
            <p>• P/E, P/B, P/S, P/FCF<br>
            • EV/EBITDA, EV/Revenue<br>
            • PEG Ratio<br>
            • Graham Numbers<br>
            • Precio vs Working Capital</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='feature-box'>
            <h3>Rentabilidad (38 métricas)</h3>
            <p>• Márgenes (Neto, Operativo, Bruto)<br>
            • ROE, ROA, ROIC, ROC<br>
            • Return on Tangible Assets<br>
            • EBITDA Margin<br>
            • Pre-tax & After-tax Margin</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='feature-box'>
            <h3>Crecimiento (41 métricas)</h3>
            <p>• YoY, QoQ en todas las líneas<br>
            • CAGR 5 años<br>
            • Crecimiento de EPS, Revenue, EBITDA<br>
            • Free Cash Flow Growth<br>
            • Capital Expenditures Growth</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='feature-box'>
            <h3>Solvencia (64 métricas)</h3>
            <p>• Debt/Equity, Current Ratio, Quick Ratio<br>
            • Interest Coverage<br>
            • Altman Z-Score<br>
            • Cash to Debt Ratios<br>
            • Working Capital Analysis</p>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class='feature-box'>
            <h3>Moving Averages (66)</h3>
            <p>• 33 SMA (2 a 300 períodos)<br>
            • 33 EMA (2 a 300 períodos)<br>
            • Golden Cross / Death Cross<br>
            • Hull MA</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='feature-box'>
            <h3>Osciladores (50)</h3>
            <p>• RSI (25 variaciones)<br>
            • Stochastic (22 configs)<br>
            • MACD (3 componentes)<br>
            • CCI, Momentum, ROC</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='feature-box'>
            <h3>Trend & Volatility (75)</h3>
            <p>• ADX (26 indicadores)<br>
            • Ichimoku Cloud (8 líneas)<br>
            • Bollinger Bands (6 configs)<br>
            • ATR, Keltner, Donchian</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='feature-box'>
            <h3>Patrones (27)</h3>
            <p>• Doji, Hammer, Engulfing<br>
            • Morning/Evening Star<br>
            • 3 White Soldiers<br>
            • Harami, Shooting Star</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='feature-box'>
            <h3>Pivot Points (31)</h3>
            <p>• Classic Pivots<br>
            • Fibonacci Pivots<br>
            • Woodie Pivots<br>
            • Camarilla & Demark</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='feature-box'>
            <h3>Otros (35)</h3>
            <p>• VWAP, VWMA<br>
            • Aroon, Parabolic SAR<br>
            • Chaikin Money Flow<br>
            • Ultimate Oscillator</p>
        </div>
        """, unsafe_allow_html=True)

with tab3:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class='highlight-box'>
            <h3>🏆 Piotroski F-Score</h3>
            <p style='color: #ffffff;'>Score de 0-9 que evalúa la fortaleza financiera de una empresa basándose en 9 criterios:</p>
            <ul>
                <li>Rentabilidad (ROA, Cash Flow, etc.)</li>
                <li>Apalancamiento y Liquidez</li>
                <li>Eficiencia Operativa</li>
            </ul>
            <p style='color: #00ffaa; font-weight: 600;'>Cobertura: 55.5% (FY) / 39.0% (TTM)</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='highlight-box'>
            <h3>💀 Altman Z-Score</h3>
            <p style='color: #ffffff;'>Predicción de riesgo de quiebra en los próximos 2 años:</p>
            <ul>
                <li>Z > 2.99: Zona Segura</li>
                <li>1.81 < Z < 2.99: Zona Gris</li>
                <li>Z < 1.81: Zona de Peligro</li>
            </ul>
            <p style='color: #00ffaa; font-weight: 600;'>Cobertura: 7.3% (FY) / 52.2% (TTM)</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='highlight-box'>
            <h3>✨ Sloan Ratio</h3>
            <p style='color: #ffffff;'>Evalúa la calidad de los beneficios comparando accruals vs cash flow:</p>
            <ul>
                <li>Ratio negativo = Buenos beneficios</li>
                <li>Ratio positivo alto = Alerta</li>
                <li>Detecta manipulación contable</li>
            </ul>
            <p style='color: #00ffaa; font-weight: 600;'>Cobertura: 65.7% (FY) / 65.6% (TTM)</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='highlight-box'>
            <h3>💰 Graham Numbers + Tobin's Q</h3>
            <p style='color: #ffffff;'>Estimación de valor intrínseco y eficiencia de mercado:</p>
            <ul>
                <li>Graham Numbers: Valor justo según Benjamin Graham</li>
                <li>Tobin's Q: Market Value vs Replacement Cost</li>
                <li>Zmijewski Score: Distress financiero</li>
            </ul>
            <p style='color: #00ffaa; font-weight: 600;'>Cobertura: 43-66%</p>
        </div>
        """, unsafe_allow_html=True)

with tab4:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class='feature-box'>
            <h3>🌎 Mercados Principales</h3>
            <p><span class='badge'>América: 13,041</span> <span class='badge'>India: 5,441</span><br>
            <span class='badge'>Japón: 4,336</span> <span class='badge'>Canadá: 4,140</span><br>
            <span class='badge'>Corea: 3,964</span> <span class='badge'>Taiwan: 2,602</span><br>
            <span class='badge'>Hong Kong: 2,560</span> <span class='badge'>UK: 2,137</span></p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='feature-box'>
            <h3>💼 Capitalización de Mercado</h3>
            <p>• Mega Cap (>$200B): <strong style='color: #00ffaa;'>386</strong><br>
            • Large Cap ($10B-$200B): <strong style='color: #00ffaa;'>2,514</strong><br>
            • Mid Cap ($2B-$10B): <strong style='color: #00ffaa;'>3,554</strong><br>
            • Small Cap ($300M-$2B): <strong style='color: #00ffaa;'>7,602</strong><br>
            • Micro Cap (<$300M): <strong style='color: #00ffaa;'>28,106</strong></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='feature-box'>
            <h3>🏛️ Top Exchanges</h3>
            <p><span class='badge'>TSE: 4,234</span> <span class='badge'>NASDAQ: 4,230</span><br>
            <span class='badge'>KRX: 3,964</span> <span class='badge'>NSE: 2,989</span><br>
            <span class='badge'>OTC: 2,881</span> <span class='badge'>AMEX: 2,738</span><br>
            <span class='badge'>NYSE: 2,106</span> <span class='badge'>ASX: 2,087</span></p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='feature-box'>
            <h3>🏢 Sectores Cubiertos</h3>
            <p>• Finance: <strong style='color: #00ffaa;'>7,479</strong><br>
            • Technology Services: <strong style='color: #00ffaa;'>3,653</strong><br>
            • Producer Manufacturing: <strong style='color: #00ffaa;'>3,772</strong><br>
            • Non-Energy Minerals: <strong style='color: #00ffaa;'>3,652</strong><br>
            • Health Technology: <strong style='color: #00ffaa;'>3,091</strong><br>
            • + 16 sectores más</p>
        </div>
        """, unsafe_allow_html=True)

# What You'll Receive
st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)
st.markdown("## 🎁 Lo Que Recibes")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class='highlight-box' style='height: 100%;'>
        <h3>📦 Código & Datos</h3>
        <ul>
            <li>Base de datos completa (CSV)</li>
            <li>Scripts de scraping documentados</li>
            <li>Pipeline ETL profesional</li>
            <li>Notebooks Jupyter explicativos</li>
            <li>Código modular y reutilizable</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='highlight-box' style='height: 100%;'>
        <h3>🛠️ Herramientas</h3>
        <ul>
            <li>Dashboard Streamlit completo</li>
            <li>Templates de screeners</li>
            <li>Funciones de análisis</li>
            <li>Sistema de backtesting</li>
            <li>Módulos de visualización</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='highlight-box' style='height: 100%;'>
        <h3>📚 Documentación</h3>
        <ul>
            <li>Guía completa de métricas</li>
            <li>Estrategias de screening</li>
            <li>Casos de estudio reales</li>
            <li>Best practices</li>
            <li>Grabación del seminario</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Technical Stack
st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)
st.markdown("## 🔧 Stack Tecnológico")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class='feature-box'>
        <h3>🐍 Python</h3>
        <p>Pandas, NumPy, Requests, BeautifulSoup, Selenium</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='feature-box'>
        <h3>📊 Análisis</h3>
        <p>TALib, Plotly, Matplotlib, Scikit-learn</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='feature-box'>
        <h3>🌐 Web Scraping</h3>
        <p>APIs REST, JSON, Proxies, Rate Limiting</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class='feature-box'>
        <h3>💻 Dashboard</h3>
        <p>Streamlit, CSS Custom, Responsive Design</p>
    </div>
    """, unsafe_allow_html=True)

# Target Audience
st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)
st.markdown("## 👥 ¿Para Quién Es Este Seminario?")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class='highlight-box'>
        <h3>✅ Perfecto Para Ti Si:</h3>
        <ul>
            <li>Quieres sistematizar tu análisis de inversiones</li>
            <li>Buscas automatizar la recopilación de datos</li>
            <li>Necesitas analizar cientos de acciones rápidamente</li>
            <li>Quieres construir tus propias herramientas</li>
            <li>Te interesa el análisis cuantitativo</li>
            <li>Eres trader, inversor, o analista financiero</li>
            <li>Estudiaste finanzas y quieres skills técnicos</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='highlight-box'>
        <h3>📋 Requisitos Previos:</h3>
        <ul>
            <li>Python básico (variables, loops, funciones)</li>
            <li>Conocimientos básicos de finanzas</li>
            <li>Familiaridad con pandas (deseable)</li>
            <li>Ganas de aprender y practicar</li>
        </ul>
        <h3 style='margin-top: 30px;'>🚀 Nivel:</h3>
        <p style='color: #ffffff;'>Intermedio - Avanzado<br>
        <strong style='color: #00ffaa;'>3 horas intensivas + material complementario</strong></p>
    </div>
    """, unsafe_allow_html=True)

# Competitive Advantage
st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)
st.markdown("## ⚡ Ventaja Competitiva")

st.markdown("""
<div style='background: linear-gradient(135deg, rgba(255, 0, 100, 0.1) 0%, rgba(255, 200, 0, 0.1) 100%); 
            border-radius: 20px; padding: 40px; margin: 30px 0; border: 2px solid rgba(255, 100, 0, 0.3);'>
    <h3 style='text-align: center; color: #ff6b6b; font-size: 2rem;'>Screeners Online vs Tu Propio Sistema</h3>
    <br>
    <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 40px; margin-top: 20px;'>
        <div>
            <h4 style='color: #ff6b6b;'>❌ Screeners Online:</h4>
            <ul style='color: #ffffff;'>
                <li>Datos limitados (500-3,000 acciones)</li>
                <li>20-80 métricas predefinidas</li>
                <li>Sin acceso a datos históricos completos</li>
                <li>Dependes de sus actualizaciones</li>
                <li>Sin personalización avanzada</li>
                <li>Suscripciones mensuales de 30-200€/mes</li>
                <li>Caja negra (no controlas la lógica)</li>
                <li>Límites de búsquedas diarias</li>
            </ul>
        </div>
        <div>
            <h4 style='color: #00ffaa;'>✅ Tu Propio Sistema:</h4>
            <ul style='color: #ffffff;'>
                <li><strong style='color: #00ffaa;'>58,168 acciones</strong> globales</li>
                <li><strong style='color: #00ffaa;'>982 métricas</strong> por acción</li>
                <li><strong style='color: #00ffaa;'>Control total</strong> del dataset</li>
                <li><strong style='color: #00ffaa;'>Actualizas</strong> cuando quieras</li>
                <li><strong style='color: #00ffaa;'>Personalización ilimitada</strong></li>
                <li><strong style='color: #00ffaa;'>Pago único</strong> - tuyo para siempre</li>
                <li><strong style='color: #00ffaa;'>Código abierto</strong> - modificable</li>
                <li><strong style='color: #00ffaa;'>Sin límites</strong> de uso</li>
            </ul>
        </div>
    </div>
    <h3 style='text-align: center; color: #00d4ff; margin-top: 40px; font-size: 2.5rem;'>
        🚀 10-20x más acciones | 12-50x más métricas | Libertad Total
    </h3>
    <p style='text-align: center; color: #ffffff; font-size: 1.3rem; margin-top: 20px;'>
        En lugar de pagar 30-50€/mes indefinidamente, inviertes una vez<br>
        y obtienes un sistema profesional que puedes usar para siempre
    </p>
</div>
""", unsafe_allow_html=True)

# Case Studies
st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)
st.markdown("## 📈 Casos Prácticos Incluidos")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class='feature-box'>
        <h3>💰 Value Investing</h3>
        <p>• P/E < 15 & P/B < 1.5<br>
        • ROE > 15%<br>
        • Debt/Equity < 0.5<br>
        • Piotroski F-Score > 7<br>
        • Dividend Yield > 3%</p>
    </div>
    """, unsafe_allow_html=True)
    
with col2:
    st.markdown("""
    <div class='feature-box'>
        <h3>🚀 Growth Stocks</h3>
        <p>• Revenue Growth > 20%<br>
        • EPS Growth > 25%<br>
        • PEG Ratio < 1.5<br>
        • Sloan Ratio < 0<br>
        • Strong momentum (RSI)</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='feature-box'>
        <h3>👑 Quality Investing</h3>
        <p>• ROE > 20% consistente<br>
        • Altman Z-Score > 3<br>
        • FCF Margin > 15%<br>
        • Low volatility<br>
        • Continuous dividends</p>
    </div>
    """, unsafe_allow_html=True)

# Timeframes
st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)
st.markdown("## 📅 Análisis Multi-Timeframe")

st.markdown("""
<div class='highlight-box'>
    <h3 style='text-align: center;'>Todas las métricas disponibles en 5 perspectivas temporales:</h3>
    <br>
    <div style='display: grid; grid-template-columns: repeat(5, 1fr); gap: 20px; text-align: center;'>
        <div>
            <h4 style='color: #00d4ff;'>Quarterly (FQ)</h4>
            <p style='font-size: 2rem; color: #00ffaa; font-weight: 800;'>112</p>
            <p style='color: #ffffff;'>métricas</p>
        </div>
        <div>
            <h4 style='color: #00d4ff;'>Semi-Annual (FH)</h4>
            <p style='font-size: 2rem; color: #00ffaa; font-weight: 800;'>35</p>
            <p style='color: #ffffff;'>métricas</p>
        </div>
        <div>
            <h4 style='color: #00d4ff;'>Fiscal Year (FY)</h4>
            <p style='font-size: 2rem; color: #00ffaa; font-weight: 800;'>129</p>
            <p style='color: #ffffff;'>métricas</p>
        </div>
        <div>
            <h4 style='color: #00d4ff;'>TTM</h4>
            <p style='font-size: 2rem; color: #00ffaa; font-weight: 800;'>69</p>
            <p style='color: #ffffff;'>métricas</p>
        </div>
        <div>
            <h4 style='color: #00d4ff;'>Current</h4>
            <p style='font-size: 2rem; color: #00ffaa; font-weight: 800;'>30</p>
            <p style='color: #ffffff;'>métricas</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Final CTA
st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

st.markdown("""
<div style='text-align: center; padding: 60px 20px; 
            background: linear-gradient(135deg, rgba(0, 212, 255, 0.15) 0%, rgba(0, 255, 170, 0.15) 100%);
            border-radius: 30px; margin: 50px 0;'>
    <h2 style='font-size: 3rem; color: #00d4ff; margin-bottom: 20px;'>
        🚀 Transforma Tu Forma de Analizar Acciones
    </h2>
    <p style='font-size: 1.5rem; color: #ffffff; margin: 30px 0;'>
        De análisis manual de 5-10 acciones con métricas básicas<br>
        A <strong style='color: #00ffaa;'>screening sistemático de 58,168 acciones</strong> con criterios profesionales
    </p>
    <p style='font-size: 1.3rem; color: #00d4ff; margin: 40px 0;'>
        ✓ No más decisiones por intuición<br>
        ✓ No más dependencia de plataformas<br>
        ✓ Control total sobre tus herramientas
    </p>
</div>
""", unsafe_allow_html=True)

# Pricing Section
st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)
st.markdown("## 💰 Información y Precio")

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("""
    <div class='highlight-box'>
        <h3>📋 Detalles del Seminario:</h3>
        <p style='color: #ffffff; font-size: 1.2rem; line-height: 2;'>
        <strong style='color: #00ffaa;'>⏱️ Duración:</strong> 3 horas intensivas<br>
        <strong style='color: #00ffaa;'>📹 Formato:</strong> Online vía Zoom<br>
        <strong style='color: #00ffaa;'>🎥 Grabación:</strong> Incluida (acceso ilimitado)<br>
        <strong style='color: #00ffaa;'>📚 Material:</strong> Código + Datos + Documentación<br>
        <strong style='color: #00ffaa;'>🔧 Nivel:</strong> Intermedio-Avanzado<br>
        <strong style='color: #00ffaa;'>🗣️ Idioma:</strong> Español
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='highlight-box' style='text-align: center; padding: 50px 20px;'>
        <h3 style='color: #00d4ff; margin-bottom: 30px;'>💎 Inversión Única</h3>
        <div class='price-tag'>
            89€
        </div>
        <p style='color: #ffffff; font-size: 1.2rem; margin-top: 30px;'>
        <strong style='color: #00ffaa;'>Incluye:</strong><br>
        ✓ Acceso al seminario en vivo<br>
        ✓ Grabación para siempre<br>
        ✓ Todo el código fuente<br>
        ✓ Base de datos completa<br>
        ✓ Documentación técnica<br>
        ✓ Casos prácticos<br>
        ✓ Templates y herramientas
        </p>
    </div>
    """, unsafe_allow_html=True)

# Contact Section
st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)
st.markdown("## 📧 Sobre el Instructor")

st.markdown("""
<div class='highlight-box'>
    <div style='display: grid; grid-template-columns: 1fr 2fr; gap: 40px; align-items: center;'>
        <div style='text-align: center;'>
            <div style='width: 150px; height: 150px; margin: 0 auto; background: linear-gradient(135deg, #00d4ff, #00ffaa); 
                        border-radius: 50%; display: flex; align-items: center; justify-content: center;'>
                <span style='font-size: 4rem;'>👨‍💻</span>
            </div>
            <h3 style='color: #00d4ff; margin-top: 20px;'>@Gsnchez</h3>
        </div>
        <div>
            <p style='color: #ffffff; font-size: 1.2rem; line-height: 1.8;'>
            <strong style='color: #00ffaa;'>Quantitative Finance Professional</strong><br><br>
            Especializado en análisis cuantitativo y desarrollo de herramientas financieras.<br>
            Creador de <strong style='color: #00d4ff;'>bquantfinance.com</strong> y del newsletter 
            <strong style='color: #00d4ff;'>BQuant Fund Lab</strong>.<br><br>
            Docente en programas de Master of Finance & Banking, enfocado en la aplicación práctica 
            de Python para análisis financiero y trading cuantitativo.
            </p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; padding: 40px; color: #666;'>
    <p style='font-size: 1.3rem; color: #00d4ff; margin-bottom: 20px;'>
        💡 <strong>Deja de invertir por rumores. Invierte con DATOS.</strong>
    </p>
    <p style='font-size: 1.1rem; color: #00ffaa; margin-bottom: 30px;'>
        🎯 Construye tu propio sistema de análisis profesional en 3 horas
    </p>
    <p style='margin-top: 20px; color: #888;'>
        © 2024 BQuant Finance | Stock Screener Masterclass
    </p>
</div>
""", unsafe_allow_html=True)
