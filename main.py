import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Stock Screener Masterclass - Web Scraping & Screening en Python",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for dark mode and clean styling
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
    }
    
    h1 {
        color: #00d4ff;
        text-align: center;
        font-size: 3rem !important;
        font-weight: 800 !important;
        text-shadow: 0 0 20px rgba(0, 212, 255, 0.5);
        margin-bottom: 10px;
    }
    
    h2 {
        color: #00d4ff;
        font-size: 2rem !important;
        font-weight: 700 !important;
        margin-top: 50px;
        margin-bottom: 20px;
        border-bottom: 2px solid #00d4ff;
        padding-bottom: 10px;
    }
    
    h3 {
        color: #00ffaa;
        font-size: 1.5rem !important;
        font-weight: 600 !important;
        margin-top: 30px;
        margin-bottom: 15px;
    }
    
    p, li {
        color: #ffffff;
        font-size: 1.1rem;
        line-height: 1.8;
    }
    
    .big-stat {
        text-align: center;
        padding: 20px;
        margin: 10px;
        background: rgba(0, 212, 255, 0.1);
        border-radius: 10px;
        border: 1px solid rgba(0, 212, 255, 0.3);
    }
    
    .big-stat .number {
        font-size: 2.5rem;
        font-weight: 800;
        color: #00d4ff;
        display: block;
    }
    
    .big-stat .label {
        font-size: 1rem;
        color: #ffffff;
        display: block;
        margin-top: 5px;
    }
    
    .highlight {
        background: rgba(0, 255, 170, 0.1);
        padding: 20px;
        border-left: 4px solid #00ffaa;
        margin: 20px 0;
        border-radius: 5px;
    }
    
    .warning {
        background: rgba(255, 100, 100, 0.1);
        padding: 20px;
        border-left: 4px solid #ff6b6b;
        margin: 20px 0;
        border-radius: 5px;
    }
    
    .price-box {
        background: linear-gradient(135deg, #00d4ff, #00ffaa);
        color: #000000;
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        margin: 30px auto;
        max-width: 400px;
    }
    
    .price-box .amount {
        font-size: 4rem;
        font-weight: 900;
    }
    
    strong {
        color: #00ffaa;
    }
    
    ul {
        margin: 15px 0;
    }
    
    hr {
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, #00d4ff, transparent);
        margin: 50px 0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1>📊 STOCK SCREENER MASTERCLASS</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.3rem; color: #00ffaa; margin-bottom: 40px;'>Seminario Intensivo: Web Scraping y Stock Screening con Python</p>", unsafe_allow_html=True)

# Key numbers in a row
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("<div class='big-stat'><span class='number'>58,168</span><span class='label'>Acciones</span></div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='big-stat'><span class='number'>982</span><span class='label'>Métricas/Acción</span></div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div class='big-stat'><span class='number'>64</span><span class='label'>Países</span></div>", unsafe_allow_html=True)
with col4:
    st.markdown("<div class='big-stat'><span class='number'>90</span><span class='label'>Exchanges</span></div>", unsafe_allow_html=True)

st.markdown("---")

# Main content
st.markdown("""
## 🎯 Sobre el Seminario

En este seminario intensivo de **3 horas** aprenderás a construir tu propio sistema profesional de stock screening utilizando Python. Te enseñaré el proceso completo: desde la **extracción masiva de datos financieros mediante web scraping**, hasta la **construcción de screeners avanzados** con múltiples criterios de filtrado.

No usaremos plataformas de terceros ni screeners online. Construirás tu **propia herramienta desde cero**, con control total sobre los datos y la lógica de filtrado. Al finalizar, tendrás acceso a una base de datos con **58,168 acciones** de **64 países** diferentes, cada una con **982 métricas** que incluyen análisis fundamental, técnico y métricas avanzadas de calidad.

### 📚 ¿Qué Aprenderás Exactamente?

**Parte 1: Web Scraping de Datos Financieros (90 minutos)**
- Extracción de datos desde APIs financieras: autenticación, headers, rate limiting
- Técnicas de scraping a gran escala: cómo obtener datos de miles de acciones eficientemente
- Procesamiento de respuestas JSON y manejo de errores en peticiones HTTP
- Construcción de pipelines ETL: extracción, transformación y carga de datos
- Limpieza y normalización de datos financieros para análisis
- Estructuración en DataFrames de Pandas para análisis posterior

**Parte 2: Construcción de Screeners Profesionales (90 minutos)**
- Arquitectura de un screener: diseño modular y escalable
- Filtros simples y complejos: operadores lógicos (AND, OR, NOT)
- Combinación de múltiples criterios: fundamental + técnico + calidad
- Sistemas de scoring y ranking personalizados
- Backtesting de estrategias de screening: validación histórica
- Exportación de resultados y generación de reportes

## 💎 La Base de Datos

Trabajarás con una base de datos profesional que contiene **58,168 acciones** distribuidas en **64 mercados** de todo el mundo. Son datos reales, actualizados, listos para usar.

### 🌍 Cobertura Geográfica

Los datos cubren los principales mercados financieros globales con la siguiente distribución: **América** (13,041 acciones - 22.4%), **India** (5,441 - 9.4%), **Japón** (4,336 - 7.5%), **Canadá** (4,140 - 7.1%), **Corea del Sur** (3,964 - 6.8%), **Taiwan** (2,602 - 4.5%), **Hong Kong** (2,560 - 4.4%), **Reino Unido** (2,137 - 3.7%), **Australia** (2,087 - 3.6%), **Alemania** (1,535 - 2.6%), **Vietnam** (1,300 - 2.2%), **Malasia** (1,097 - 1.9%), **Tailandia** (986 - 1.7%), **Francia** (973 - 1.7%), **Israel** (963 - 1.7%), **Suecia** (928 - 1.6%), **Indonesia** (903 - 1.6%), **Brasil** (898 - 1.5%), y otros 46 países más incluyendo Polonia, Turquía, Singapur, Pakistán, Suiza, Rusia, Italia, Bangladesh, España, Noruega, Sri Lanka, Países Bajos, Filipinas, Egipto, Rumanía, Dinamarca, Finlandia, Chile, México, Emiratos Árabes Unidos, Nueva Zelanda, Nigeria, Grecia, Kuwait, Bélgica, Colombia, Luxemburgo, Marruecos, Austria, Argentina, Hungría, Perú, Qatar, Kenia, Portugal, Estonia, Chipre, República Checa, Lituania, Venezuela, Islandia, Bahréin, Irlanda, Serbia, Letonia, y Eslovaquia.

Las principales **exchanges** incluidas son: **TSE** (Tokio - 4,234 acciones), **NASDAQ** (4,230), **KRX** (Corea - 3,964), **NSE** (India - 2,989), **OTC** (2,881), **AMEX** (2,738), **HKEX** (Hong Kong - 2,560), **BSE** (India - 2,452), **NYSE** (2,106), **ASX** (Australia - 2,087), **LSE** (Londres - 2,065), **TSX** (Toronto - 1,925), **XETR** (Alemania - 1,466), **EURONEXT** (1,404), **TSXV** (1,359), y 75 exchanges adicionales.

### 📊 Las 982 Métricas Disponibles

Cada acción de la base de datos tiene **982 métricas diferentes** organizadas en múltiples categorías:

**Métricas Fundamentales (373 métricas):**
- **Valoración (27):** P/E ratio, P/B ratio, P/S ratio, Price/Free Cash Flow, EV/EBITDA, EV/Revenue, EV/EBIT, PEG ratio, Enterprise Value, Graham Numbers, Price/Working Capital, y más
- **Rentabilidad (38):** Net margin, Operating margin, Gross margin, ROE (Return on Equity), ROA (Return on Assets), ROIC (Return on Invested Capital), ROC, Return on Tangible Assets, Return on Common Equity, EBITDA margin, Pre-tax margin, After-tax margin, y variaciones
- **Solvencia y Salud Financiera (64):** Debt/Equity, Current ratio, Quick ratio, Debt/Assets, Long-term debt ratios, Interest coverage, Altman Z-Score, Zmijewski Score, Cash ratios, Working capital metrics, Total debt to capital, Net debt to EBITDA
- **Crecimiento (41):** YoY growth (revenue, earnings, EBITDA, FCF), QoQ growth, CAGR 5 años, EPS growth, Capital expenditures growth, Total assets growth, Debt growth
- **Cash Flow (65):** Free Cash Flow, Operating Cash Flow, Cash from investing/financing activities, FCF margin, FCF per share, Capital expenditures, Cash flow coverage ratios
- **Dividendos (43):** Dividend yield, Payout ratio, Dividends per share, Continuous dividend growth/payout, Dividend dates, Indicated annual dividend, Buyback yield
- **Calidad (14):** Piotroski F-Score (0-9), Altman Z-Score (bankruptcy prediction), Sloan Ratio (earnings quality), Graham Numbers, Tobin's Q ratio, Zmijewski Score, Sustainable growth rate
- **Per Share (81):** Todas las métricas anteriores calculadas por acción (EPS, Book value, Revenue, EBITDA, EBIT, Cash, Free cash flow, Operating cash flow, Capex, Working capital, etc.)

**Métricas Técnicas (249 indicadores):**
- **Moving Averages (66):** 33 SMA (periodos 2-300) + 33 EMA (periodos 2-300), incluyendo señales de Golden Cross y Death Cross
- **Osciladores (50):** RSI en 25 variaciones y periodos, Stochastic (22 configuraciones: K y D), MACD (macd, signal, histogram), CCI, Momentum, ROC, Williams %R, Ultimate Oscillator
- **Trend & Volatility (75):** ADX con 26 indicadores incluyendo +DI y -DI, Ichimoku Cloud (8 componentes: Tenkan, Kijun, Senkou A/B, Chikou), Bollinger Bands (6 configuraciones), ATR, ATRP, Keltner Channels, Donchian Channels
- **Patrones de Velas (27):** Detección automática de Doji, Doji Dragonfly, Doji Gravestone, Hammer, Hanging Man, Inverted Hammer, Shooting Star, Bullish/Bearish Engulfing, Bullish/Bearish Harami, Morning Star, Evening Star, Three White Soldiers, Three Black Crows, Marubozu (White/Black), Spinning Tops, Long Shadows, Kicking, Abandoned Baby, TriStar
- **Pivot Points (31):** 5 metodologías completas (Classic, Fibonacci, Woodie, Camarilla, Demark) con resistencias R1/R2/R3 y soportes S1/S2/S3
- **Otros (35):** VWAP, VWMA, Aroon Up/Down, Parabolic SAR, Chaikin Money Flow, Money Flow Index, BBPower, Hull MA, Awesome Oscillator

**Performance & Risk (44 métricas):**
- **Performance (18):** Rendimientos en múltiples timeframes: 5D, 1W, 1M, 3M, 6M, 1Y, YTD, 3Y, 5Y, 10Y, All-time. También ajustados por market cap
- **Volatilidad (9):** Beta 1Y/3Y/5Y, ATR, ATRP, Volatilidad diaria/semanal/mensual
- **Volumen (17):** Volume, Average volume (10/30/60/90 días), Relative volume, Volume change, Premarket/Postmarket volume, Value traded

**Analyst & Forecasts (54 métricas):**
Recomendaciones de analistas (Buy/Hold/Sell), Price targets (high/low/average/median), Earnings forecasts (próximos FQ/FH/FY), Revenue forecasts, EPS surprises, Revenue surprises, Earnings release dates, Non-GAAP estimaciones

### 📅 Perspectivas Temporales

Todas las métricas fundamentales están disponibles en **5 timeframes diferentes** para análisis temporal completo:
- **Quarterly (FQ):** 112 métricas trimestrales
- **Semi-Annual (FH):** 35 métricas semestrales  
- **Fiscal Year (FY):** 129 métricas anuales
- **Trailing Twelve Months (TTM):** 69 métricas de últimos 12 meses
- **Current Period:** 30 métricas del periodo actual

### 💼 Distribución por Capitalización

La base de datos cubre todo el espectro de capitalizaciones de mercado con **42,162 acciones** con datos de market cap: **Mega Cap** (>$200B): 386 acciones (0.9%), **Large Cap** ($10B-$200B): 2,514 acciones (6.0%), **Mid Cap** ($2B-$10B): 3,554 acciones (8.4%), **Small Cap** ($300M-$2B): 7,602 acciones (18.0%), **Micro Cap** (<$300M): 28,106 acciones (66.7%). Capitalización media: $17.6B, mediana: $91.3M.

### 🏢 Sectores Cubiertos

**21 sectores principales:** Finance (7,479 acciones), Technology Services (3,653), Producer Manufacturing (3,772), Non-Energy Minerals (3,652), Process Industries (3,359), Health Technology (3,091), Electronic Technology (2,669), Commercial Services (2,078), Consumer Non-Durables (1,963), Retail Trade, Energy Minerals, Consumer Services, Utilities, Transportation, Consumer Durables, Distribution Services, Industrial Services, Health Services, Communications, Government, y Miscellaneous (13,142).
""")

st.markdown("---")

st.markdown("""
## ⚡ ¿Por Qué Construir Tu Propio Sistema?

### La Realidad de los Screeners Online

Los screeners disponibles en internet (gratuitos o de pago) tienen **limitaciones importantes**: normalmente ofrecen entre 500 y 3,000 acciones (principalmente USA), con 20 a 80 métricas predefinidas. No tienes acceso a datos históricos completos, dependes completamente de sus actualizaciones, la personalización es muy limitada o inexistente, funcionan como "caja negra" sin que entiendas la lógica interna, suelen tener límites diarios de búsquedas, y requieren suscripciones mensuales que van de 30€ a 200€/mes.

### Tu Propio Sistema

Con lo que aprenderás en este seminario construirás un sistema con **58,168 acciones** de **64 países** (10-20x más cobertura), **982 métricas** por acción (12-50x más profundidad analítica), **control total** sobre el dataset y actualizaciones, **personalización ilimitada** de filtros y criterios, código **open source** que puedes modificar y adaptar, **sin límites** de uso ni búsquedas, y **pago único** - el sistema es tuyo para siempre sin mensualidades.

**Ventaja económica:** En lugar de pagar 30-50€/mes indefinidamente (360-600€/año), haces una **inversión única de 89€** y obtienes un sistema profesional que puedes usar, modificar y actualizar cuando quieras, sin depender de nadie.

**Ventaja técnica:** Aprendes el proceso completo - no solo usas una herramienta, sino que entiendes cómo funciona y puedes adaptarla a tus necesidades específicas. Puedes agregar nuevas métricas, crear tus propias fórmulas, combinar indicadores de formas únicas, y construir estrategias de screening completamente personalizadas.
""")

st.markdown("---")

st.markdown("""
## 🎓 Casos Prácticos Durante el Seminario

Durante las 3 horas veremos ejemplos reales de estrategias de screening:

**Value Investing:** Filtrado de acciones infravaloradas usando P/E < 15, P/B < 1.5, ROE > 15%, Debt/Equity < 0.5, Piotroski F-Score > 7, Dividend Yield > 3%. Aprenderás a combinar múltiples ratios de valoración con métricas de calidad financiera.

**Growth Stocks:** Identificación de empresas de alto crecimiento con Revenue Growth > 20% YoY, EPS Growth > 25%, PEG Ratio < 1.5, Sloan Ratio < 0 (buena calidad de earnings), Strong momentum técnico (RSI, Moving Averages). Verás cómo filtrar empresas con crecimiento sostenible vs crecimiento artificial.

**Quality Investing:** Selección de empresas con ROE > 20% consistente en múltiples años, Altman Z-Score > 3 (baja probabilidad de quiebra), Free Cash Flow Margin > 15%, Low volatility (Beta < 1), Continuous dividends. Aprenderás a construir filtros que priorizan la solidez financiera sobre el crecimiento agresivo.

**Dividend Aristocrats:** Búsqueda de empresas con dividendos crecientes y sostenibles usando Dividend Yield > 2%, Continuous Dividend Growth > 5 años, Payout Ratio < 60%, FCF to Dividend ratio > 1.5, Positive revenue growth.

**Technical Momentum:** Screening basado en señales técnicas como Golden Cross (SMA50 > SMA200), RSI entre 50-70 (momentum positivo sin sobreventa), MACD bullish crossover, Price above all major MAs, Volume > average 60 días.

Cada estrategia incluye el código completo, la lógica de filtrado, y la interpretación de resultados.
""")

st.markdown("---")

st.markdown("""
## 🔧 Stack Tecnológico

El seminario utiliza **Python** como lenguaje principal con las siguientes librerías: **Pandas** y **NumPy** para manipulación y análisis de datos, **Requests** para peticiones HTTP a APIs, **BeautifulSoup** y **Selenium** para scraping web cuando es necesario, **Plotly** y **Matplotlib** para visualizaciones, **TALib** para indicadores técnicos avanzados, y **Scikit-learn** para análisis estadístico.

No necesitas experiencia previa con todas estas librerías - te explicaré cada una durante el seminario. Solo necesitas conocimientos básicos de Python (variables, loops, funciones) y familiaridad con Pandas (deseable pero no obligatorio). El nivel es **intermedio-avanzado** pero estructurado para que cualquiera con bases de Python pueda seguirlo.
""")

st.markdown("---")

st.markdown("""
## 🎁 Material Incluido

Con tu inscripción al seminario recibes:

### Código Fuente Completo
- Scripts de scraping documentados línea por línea
- Pipeline ETL profesional con manejo de errores
- Módulos de análisis y filtrado reutilizables
- Notebooks Jupyter con explicaciones detalladas
- Funciones de visualización y reporting

### Base de Datos
- CSV con las 58,168 acciones y 982 métricas
- Diccionario de datos completo (explicación de cada métrica)
- Scripts de actualización para refrescar los datos

### Documentación
- Guía técnica de 50+ páginas sobre todas las métricas
- Estrategias de screening con ejemplos de código
- 10 casos de estudio reales completamente resueltos
- Best practices para scraping a gran escala
- Troubleshooting guide con soluciones a problemas comunes

### Grabación
- Acceso ilimitado a la grabación del seminario
- Puedes revisarla las veces que necesites
- Transcripción con timestamps para búsqueda rápida
""")

st.markdown("---")

# Pricing
st.markdown("## 💰 Información y Precio")

col1, col2 = st.columns([3, 2])

with col1:
    st.markdown("""
    ### Detalles del Seminario
    
    **Duración:** 3 horas intensivas (con descanso de 10 minutos a mitad)
    
    **Formato:** Online en vivo vía Zoom - sesión interactiva donde puedes hacer preguntas en tiempo real
    
    **Fecha:** [Próximas fechas disponibles - consultar]
    
    **Horario:** [A confirmar según inscripciones]
    
    **Grabación:** Incluida con acceso ilimitado - si no puedes asistir en vivo o quieres repasar el contenido
    
    **Idioma:** Español
    
    **Nivel:** Intermedio-Avanzado (requiere Python básico)
    
    **Requisitos técnicos:** Ordenador con Python 3.8+ instalado, conexión a internet estable, 4GB RAM mínimo
    
    **Soporte:** Grupo privado para resolver dudas post-seminario durante 30 días
    """)

with col2:
    st.markdown("""
    <div class='price-box'>
        <div style='font-size: 1.2rem; margin-bottom: 10px;'>Inversión Única</div>
        <div class='amount'>89€</div>
        <div style='font-size: 1rem; margin-top: 15px;'>IVA incluido</div>
    </div>
    
    <div class='highlight'>
        <strong>✓ Acceso inmediato al material preparatorio</strong><br>
        ✓ Seminario en vivo de 3 horas<br>
        ✓ Grabación para siempre<br>
        ✓ Todo el código fuente<br>
        ✓ Base de datos completa (58K acciones)<br>
        ✓ Documentación técnica (50+ páginas)<br>
        ✓ 10 casos prácticos resueltos<br>
        ✓ Soporte 30 días post-seminario
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.markdown("""
## 👥 ¿Para Quién Es Este Seminario?

**Perfecto para ti si:**
- Eres **inversor** o **trader** que quiere sistematizar el análisis de acciones con datos objetivos
- Trabajas como **analista financiero** y necesitas herramientas más potentes que los screeners comerciales
- Eres **gestor de carteras** buscando automatizar la selección de valores
- Estudiaste **finanzas** o **economía** y quieres adquirir skills técnicos muy demandados
- Te interesa el **análisis cuantitativo** y quieres construir tus propias herramientas
- Quieres **independencia** de plataformas de terceros y control total sobre tus datos
- Necesitas analizar **cientos de acciones** de forma rápida y eficiente
- Buscas crear **estrategias de screening personalizadas** que otros no tienen

**Requisitos previos:**
- Python básico: debes saber qué son variables, listas, diccionarios, loops (for/while), funciones, y cómo importar librerías
- Conocimientos de finanzas: entender qué es P/E ratio, ROE, Free Cash Flow, deuda, márgenes - conceptos básicos
- Familiaridad con Pandas es un plus pero no obligatorio (te explicaré lo necesario)
- Ganas de aprender, practicar y hacer preguntas

**No es para ti si:**
- No tienes ninguna experiencia con Python (necesitas al menos lo básico)
- Buscas un curso de "introducción a las finanzas" - asumimos que entiendes los conceptos fundamentales
- Quieres una solución "click and go" sin entender cómo funciona - aquí construimos desde cero
- No estás dispuesto a invertir tiempo en practicar después del seminario
""")

st.markdown("---")

st.markdown("""
<div style='text-align: center; padding: 50px 20px; background: linear-gradient(135deg, rgba(0, 212, 255, 0.1), rgba(0, 255, 170, 0.1)); border-radius: 15px; margin: 40px 0;'>
    <h2 style='color: #00d4ff; font-size: 2.5rem; margin-bottom: 20px;'>
        🚀 De Análisis Manual a Sistema Profesional en 3 Horas
    </h2>
    <p style='font-size: 1.3rem; color: #ffffff; line-height: 1.8; max-width: 900px; margin: 20px auto;'>
        Deja de depender de screeners limitados que te cobran cada mes.<br>
        Deja de analizar manualmente 5-10 acciones con métricas básicas.<br><br>
        Construye tu propio sistema con <strong style='color: #00ffaa;'>58,168 acciones</strong> de <strong style='color: #00ffaa;'>64 países</strong> 
        y <strong style='color: #00ffaa;'>982 métricas</strong> por acción.<br><br>
        <strong style='color: #00d4ff;'>Control total. Personalización ilimitada. Tuyo para siempre.</strong>
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

st.markdown("""
<div style='text-align: center; padding: 30px;'>
    <p style='font-size: 1.2rem; color: #00d4ff; margin-bottom: 15px;'>
        💡 <strong>No más decisiones por rumores. Invierte con DATOS.</strong>
    </p>
    <p style='font-size: 1rem; color: #888; margin-top: 20px;'>
        © 2024 BQuant Finance | Stock Screener Masterclass<br>
        Para más información: <strong style='color: #00ffaa;'>@Gsnchez</strong> | bquantfinance.com
    </p>
</div>
""", unsafe_allow_html=True)
