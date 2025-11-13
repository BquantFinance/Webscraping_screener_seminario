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
    
    .asset-badge {
        display: inline-block;
        padding: 8px 16px;
        margin: 5px;
        border-radius: 20px;
        font-weight: 600;
        font-size: 1rem;
    }
    
    .badge-stocks {
        background: rgba(0, 212, 255, 0.2);
        border: 2px solid #00d4ff;
        color: #00d4ff;
    }
    
    .badge-etfs {
        background: rgba(0, 255, 170, 0.2);
        border: 2px solid #00ffaa;
        color: #00ffaa;
    }
    
    .badge-crypto {
        background: rgba(255, 170, 0, 0.2);
        border: 2px solid #ffaa00;
        color: #ffaa00;
    }
    
    .badge-forex {
        background: rgba(170, 0, 255, 0.2);
        border: 2px solid #aa00ff;
        color: #aa00ff;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1>📊 FINANCIAL SCREENER MASTERCLASS</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.3rem; color: #00ffaa; margin-bottom: 20px;'>Seminario Intensivo: Web Scraping y Screening Avanzado con Python</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.2rem; color: #ffffff; margin-bottom: 40px;'>Stocks • ETFs • Crypto • Forex</p>", unsafe_allow_html=True)

# Asset class badges
st.markdown("""
<div style='text-align: center; margin-bottom: 40px;'>
    <span class='asset-badge badge-stocks'>📈 58,168 STOCKS</span>
    <span class='asset-badge badge-etfs'>💼 30,167 ETFs</span>
    <span class='asset-badge badge-crypto'>₿ 67,476 CRYPTO</span>
    <span class='asset-badge badge-forex'>💱 7,174 FOREX</span>
</div>
""", unsafe_allow_html=True)

# Key numbers in a row
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("<div class='big-stat'><span class='number'>162,985</span><span class='label'>Instrumentos Totales</span></div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='big-stat'><span class='number'>~600</span><span class='label'>Métricas Promedio</span></div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div class='big-stat'><span class='number'>64</span><span class='label'>Países (Stocks)</span></div>", unsafe_allow_html=True)
with col4:
    st.markdown("<div class='big-stat'><span class='number'>4</span><span class='label'>Asset Classes</span></div>", unsafe_allow_html=True)

st.markdown("---")

# Main content
st.markdown("""
## 🎯 Sobre el Seminario

En este seminario intensivo de **3 horas** aprenderás a construir tu propio sistema profesional de screening para **múltiples asset classes**: acciones, ETFs, criptomonedas y forex. Te enseñaré el proceso completo: desde la **extracción masiva de datos financieros mediante web scraping**, hasta la **construcción de screeners avanzados** con múltiples criterios de filtrado.

No usaremos plataformas de terceros ni screeners online. Construirás tu **propia herramienta desde cero**, con control total sobre los datos y la lógica de filtrado. Al finalizar, tendrás acceso a bases de datos con **162,985 instrumentos financieros** que incluyen **58,168 acciones** de 64 países, **30,167 ETFs**, **67,476 criptomonedas** y **7,174 pares de forex**, cada uno con cientos de métricas que cubren análisis fundamental, técnico y métricas avanzadas de calidad.

### 📚 ¿Qué Aprenderás Exactamente?

**Parte 1: Web Scraping de Datos Financieros Multi-Asset (90 minutos)**
- Extracción de datos desde APIs financieras: autenticación, headers, rate limiting
- Técnicas de scraping específicas para cada asset class (stocks, ETFs, crypto, forex)
- Manejo de diferentes estructuras de datos según el tipo de instrumento
- Procesamiento de respuestas JSON y manejo de errores en peticiones HTTP
- Construcción de pipelines ETL unificados: extracción, transformación y carga
- Limpieza y normalización de datos financieros para análisis cross-asset
- Estructuración en DataFrames de Pandas con esquemas compatibles

**Parte 2: Construcción de Screeners Multi-Asset (90 minutos)**
- Arquitectura de un screener universal: diseño modular y escalable
- Filtros específicos por asset class y filtros comunes cross-asset
- Combinación de múltiples criterios: fundamental + técnico + calidad
- Screening de correlaciones entre assets (stocks vs crypto, forex vs commodities)
- Sistemas de scoring y ranking personalizados por categoría
- Backtesting de estrategias de screening: validación histórica
- Exportación de resultados y generación de reportes multi-asset

## 💎 Las Bases de Datos

Trabajarás con **cuatro bases de datos profesionales** que contienen un total de **162,985 instrumentos financieros** con datos reales y actualizados.

### 📈 STOCKS: 58,168 Acciones Globales | 982 Métricas

La base de datos de acciones cubre **58,168 acciones** distribuidas en **64 mercados** de todo el mundo con **982 métricas** por acción.

**Cobertura Geográfica:** **América** (13,041 acciones - 22.4%), **India** (5,441 - 9.4%), **Japón** (4,336 - 7.5%), **Canadá** (4,140 - 7.1%), **Corea del Sur** (3,964 - 6.8%), **Taiwan** (2,602 - 4.5%), **Hong Kong** (2,560 - 4.4%), **Reino Unido** (2,137 - 3.7%), **Australia** (2,087 - 3.6%), **Alemania** (1,535 - 2.6%), **Vietnam** (1,300 - 2.2%), y 53 países más.

**Principales Exchanges:** **TSE** (Tokio - 4,234), **NASDAQ** (4,230), **KRX** (Corea - 3,964), **NSE** (India - 2,989), **OTC** (2,881), **AMEX** (2,738), **HKEX** (Hong Kong - 2,560), **BSE** (India - 2,452), **NYSE** (2,106), **ASX** (Australia - 2,087), **LSE** (Londres - 2,065), **TSX** (Toronto - 1,925), y 78 exchanges más.

**Métricas de Stocks (982):**
- **Fundamental (373):** Valoración (27), Rentabilidad (38), Solvencia (64), Crecimiento (41), Cash Flow (65), Dividendos (43), Calidad (14: Piotroski F-Score, Altman Z-Score, Sloan Ratio, Graham Numbers, Tobin's Q), Per Share (81)
- **Técnicas (249):** Moving Averages (66: SMA + EMA), Osciladores (50: RSI, Stochastic, MACD, CCI, Momentum), Trend & Volatility (75: ADX, Ichimoku, Bollinger Bands, ATR), Patrones de Velas (27), Pivot Points (31)
- **Performance & Risk (44):** Performance multi-timeframe (18), Volatilidad (9), Volumen (17)
- **Analyst Data (54):** Recomendaciones, Price targets, Forecasts, Surprises

**Timeframes:** Todas las métricas fundamentales en 5 perspectivas temporales: Quarterly (FQ) - 112 métricas, Semi-Annual (FH) - 35, Fiscal Year (FY) - 129, TTM - 69, Current - 30

**Capitalización:** Mega Cap (>$200B): 386 | Large Cap ($10B-$200B): 2,514 | Mid Cap ($2B-$10B): 3,554 | Small Cap ($300M-$2B): 7,602 | Micro Cap (<$300M): 28,106

**Sectores (21):** Finance (7,479), Technology Services (3,653), Producer Manufacturing (3,772), Non-Energy Minerals (3,652), Health Technology (3,091), Electronic Technology (2,669), y 15 sectores más.

### 💼 ETFs: 30,167 Fondos Cotizados | 202 Métricas

Base de datos completa de ETFs con **30,167 fondos** listados en múltiples exchanges globales, incluyendo **202 métricas especializadas**.

**Métricas de ETFs (202):**
- **Características del Fondo:** AUM (Assets Under Management), Expense ratio, Asset class, Focus, Category, Niche, Strategy, Holdings region, Index tracked, Index provider, Brand, Issuer
- **Estructura:** Leverage ratio, UCITS compliant, Currency hedged, Holds derivatives, Transparent holdings, K1 form, Selection criteria, Weighting scheme, Weight top 10/25/50
- **Performance:** NAV performance (YTD, 1M, 3M, 6M, 1Y, 3Y, 5Y), Total returns, Fund flows (YTD, 1M, 3M, 1Y, 3Y, 5Y), AUM performance por periodo
- **Dividendos:** Dividend yield, Indicated annual dividend, Dividend frequency, Dividend treatment
- **Análisis Técnico:** Todos los indicadores técnicos estándar (RSI, MACD, Moving Averages, Bollinger Bands, Stochastic, ADX, Ichimoku, Pivot Points, 27 patrones de velas)
- **Risk Metrics:** Beta (1Y/3Y/5Y), Volatility (D/W/M), Volume analysis, Performance metrics
- **Clasificación:** País, Exchange, Currency, Sector exposure, Geographic exposure

**Tipos de ETFs Cubiertos:** Equity ETFs, Bond ETFs, Commodity ETFs, Currency ETFs, Sector ETFs, Country/Region ETFs, Thematic ETFs, Smart Beta ETFs, Leveraged/Inverse ETFs, Multi-asset ETFs

### ₿ CRYPTO: 67,476 Criptomonedas | 421 Métricas

Base de datos masiva con **67,476 criptomonedas** incluyendo tokens, coins, DeFi tokens, NFT collections, y **421 métricas especializadas**.

**Métricas de Crypto (421):**
- **Market Data:** Market cap, Fully diluted value, Circulating supply, Total supply, Total shares outstanding/diluted, Price 52-week high/low
- **DEX Analytics (más de 100 métricas):** Trading volume (15m, 1h, 4h, 12h, 24h), Buy/Sell volume por timeframe, Buyers/Sellers count por periodo, Transaction counts (15m, 1h, 4h, 12h, 24h), Unique transactions, Total liquidity, Buys/Sells counts por periodo, Created time
- **Technical Analysis Completo:** Todos los indicadores (RSI, MACD, SMA, EMA, Stochastic, ADX, Bollinger Bands, Ichimoku, Pivot Points, ATR, CCI, Momentum, Aroon, VWAP)
- **Candlestick Patterns:** 27 patrones detectados automáticamente
- **On-chain Metrics:** Centralization score, Blockchain ID, Total value traded, Volume base/quote
- **Performance:** Multi-timeframe (5D, 1W, 1M, 3M, 6M, 1Y, YTD, 3Y, 5Y, 10Y, All-time), 24h changes
- **Volatility & Risk:** Volatility diaria/semanal/mensual, Gap analysis, High/Low tracking
- **Volume Analysis:** Volume, Volume changes, Average volumes, Relative volume, Value traded

**Exchanges Cubiertos:** PancakeSwap, Bitget, Bithumb, BinanceUS, Pangolin, Aerodrome, Phemex, OKX, Uniswap, SushiSwap, y 100+ exchanges más (CEX y DEX)

**Blockchains:** Ethereum, BSC, Polygon, Avalanche, Arbitrum, Optimism, Solana, Base, y más

### 💱 FOREX: 7,174 Pares de Divisas | 379 Métricas

Base de datos completa de forex con **7,174 pares de divisas** de múltiples brokers y **379 métricas técnicas**.

**Métricas de Forex (379):**
- **Información del Par:** Exchange code, Pair name, Description, Base currency, Quote currency, Currency priority (major/minor/exotic)
- **Price Data:** Bid, Ask, Bid-ask spread, Close, Open, High, Low, Price 52-week high/low con fechas, All-time high/low con fechas
- **Technical Analysis Completo (250+ métricas):** 
  - Moving Averages: 33 EMA + 33 SMA (periodos 2 a 300)
  - Oscillators: RSI (11 variaciones), Stochastic (22 configs), MACD, CCI, Williams %R, Ultimate Oscillator, Momentum, ROC, Awesome Oscillator
  - Trend Indicators: ADX completo (26 indicadores), Ichimoku Cloud (8 componentes), Aroon, Parabolic SAR
  - Volatility: Bollinger Bands (6 configs), ATR, ATRP, ADR, ADRP, Keltner Channels, Donchian Channels
  - Volume: VWAP, VWMA, Volume, Value traded, Average volumes, Relative volume
  - Pivot Points: 31 cálculos (Classic, Fibonacci, Woodie, Camarilla, Demark)
- **Candlestick Patterns:** 27 patrones (Doji, Hammer, Engulfing, Harami, Morning/Evening Star, etc.)
- **Performance:** Multi-timeframe (5D, 1W, 1M, 3M, 6M, 1Y, YTD, 3Y, 5Y, 10Y, All-time)
- **Volatility Metrics:** Daily, Weekly, Monthly volatility
- **Gap Analysis:** Gap, Gap up/down with absolute values
- **Change Metrics:** Multiple timeframe changes (5, 15, 30, 60 periods)

**Brokers/Providers Cubiertos:** ThinkMarkets, EasyMarkets, FX_IDC (ICE), IBKR, OANDA, y más

**Categorías de Pares:** Majors (USD pairs), Minors (cross pairs), Exotics (emerging market currencies)

**Cobertura Geográfica:** Pares que incluyen divisas de todos los continentes: USD, EUR, GBP, JPY, CHF, AUD, NZD, CAD (majors), más divisas asiáticas (CNY, INR, KRW, SGD, THB), latinoamericanas (MXN, BRL, ARS, CLP, PEN), africanas (ZAR, NGN), y más.

## 🔄 Ventajas del Enfoque Multi-Asset

Al trabajar con **4 asset classes diferentes** en un solo sistema, obtendrás:

**1. Visión Holística del Mercado:** Entiende correlaciones entre assets (cuando crypto sube, ¿qué pasa con tech stocks?). Identifica rotaciones de capital entre asset classes. Detecta oportunidades de arbitraje o divergencias.

**2. Estrategias Cross-Asset:** Crea portfolios diversificados usando el mismo screener. Compara valuaciones relativas (P/E de stocks vs ratios de crypto). Identifica sectores ganadores en múltiples mercados simultáneamente.

**3. Eficiencia Operativa:** Un solo código base para 4 asset classes. Reutilización de funciones de análisis técnico. Pipeline ETL unificado. Reportes consolidados.

**4. Mayor Alcance:** 162,985 instrumentos vs 500-5,000 en screeners online típicos. Oportunidades en mercados que otros ignoran (small cap crypto, ETFs nicho, forex exóticos). Coverage verdaderamente global.
""")

st.markdown("---")

st.markdown("""
## ⚡ ¿Por Qué Construir Tu Propio Sistema?

### La Realidad de los Screeners Online

Los screeners disponibles en internet (gratuitos o de pago) tienen **limitaciones importantes**: normalmente ofrecen entre 500 y 5,000 instrumentos (principalmente USA stocks), con 20 a 80 métricas predefinidas, **limitados a una sola asset class** (stocks O crypto O forex, nunca integrados). No tienes acceso a datos históricos completos, dependes completamente de sus actualizaciones, la personalización es muy limitada o inexistente, funcionan como "caja negra" sin que entiendas la lógica interna, suelen tener límites diarios de búsquedas, y requieren **múltiples suscripciones** si quieres cubrir varios asset classes (30-200€/mes por plataforma).

### Tu Propio Sistema Multi-Asset

Con lo que aprenderás en este seminario construirás un sistema con **162,985 instrumentos** de **4 asset classes** (30-50x más cobertura que screeners típicos), **600+ métricas promedio** por instrumento, **análisis cross-asset** en una sola herramienta, **control total** sobre el dataset y actualizaciones, **personalización ilimitada** de filtros y criterios, código **open source** que puedes modificar y adaptar, **sin límites** de uso ni búsquedas, y **pago único** - el sistema es tuyo para siempre sin mensualidades.

**Ventaja económica:** Para tener cobertura comparable necesitarías suscribirte a: screener de stocks (50€/mes) + screener de crypto (40€/mes) + datos de forex (30€/mes) + ETF analytics (40€/mes) = **160€/mes = 1,920€/año**. En su lugar, haces una **inversión única de 89€** y obtienes un sistema integrado que cubre todo.

**Ventaja técnica:** Aprendes el proceso completo - no solo usas una herramienta, sino que entiendes cómo funciona y puedes adaptarla a tus necesidades específicas. Puedes agregar nuevas métricas, crear tus propias fórmulas, combinar indicadores de formas únicas, construir estrategias de screening cross-asset completamente personalizadas, y detectar correlaciones entre mercados que las plataformas separadas nunca mostrarían.
""")

st.markdown("---")

st.markdown("""
## 🎓 Casos Prácticos Durante el Seminario

Durante las 3 horas veremos ejemplos reales de estrategias de screening **tanto single-asset como cross-asset**:

### Estrategias Single-Asset

**Value Investing (Stocks):** Filtrado de acciones infravaloradas usando P/E < 15, P/B < 1.5, ROE > 15%, Debt/Equity < 0.5, Piotroski F-Score > 7, Dividend Yield > 3%. Aprenderás a combinar múltiples ratios de valoración con métricas de calidad financiera.

**ETF Rotation Strategy:** Identificación de ETFs sectoriales con mejor momentum usando Performance 3M > 10%, AUM > $500M, Expense ratio < 0.5%, Fund flows positive, Beta 1Y > 1.2. Detectar rotaciones de capital entre sectores.

**Crypto Momentum:** Selección de cryptos con alto volumen y momentum: 24h volume > $1M, DEX liquidity > $500K, RSI entre 50-70, Price > SMA20 y SMA50, Buyers 24h > Sellers 24h. Filtrar tokens con tracción real vs pump & dump.

**Forex Technical Breakout:** Pares de divisas cerca de niveles técnicos clave: Price near 52-week high, ADX > 25 (strong trend), MACD bullish crossover, Volume > average 30d, Major currency pairs only. Capturas breakouts con confirmación técnica.

### Estrategias Cross-Asset

**Risk-On / Risk-Off Detector:** Compara performance de: Growth stocks vs Value stocks, High-yield bonds ETFs vs Treasury ETFs, Emerging market currencies vs Safe haven currencies (JPY, CHF, USD), Crypto vs Gold ETFs. Identifica el sentimiento general del mercado.

**Sector Rotation Cross-Market:** Encuentra sectores ganadores simultáneamente en: US stocks de ese sector, ETFs sectoriales correspondientes, Related crypto tokens (ej: DeFi tokens si finance está fuerte). Valida tendencias cuando múltiples asset classes confirman.

**Inflation Hedge Portfolio:** Screener que combina: Commodities ETFs con positive momentum, REITs con dividend yield > 4%, Gold & Silver positions, Inflation-protected bonds ETFs, Crypto con baja correlación (potential store of value). Construcción automática de portfolio anti-inflación.

**Volatility Arbitrage:** Detecta discrepancias de volatilidad: Stocks con volatility < 20% pero sector ETF con volatility > 30%, Crypto con RSI < 30 mientras sector DeFi está sobrevalorado, Forex pairs con diverging volatilities. Oportunidades de trading basadas en mean reversion.

Cada estrategia incluye el código completo, la lógica de filtrado, y la interpretación de resultados.
""")

st.markdown("---")

st.markdown("""
## 🔧 Stack Tecnológico

El seminario utiliza **Python** como lenguaje principal con las siguientes librerías: **Pandas** y **NumPy** para manipulación y análisis de datos multi-asset, **Requests** para peticiones HTTP a APIs, **BeautifulSoup** y **Selenium** para scraping web cuando es necesario, **Plotly** y **Matplotlib** para visualizaciones cross-asset, **TALib** para indicadores técnicos avanzados, y **Scikit-learn** para análisis estadístico y correlaciones.

No necesitas experiencia previa con todas estas librerías - te explicaré cada una durante el seminario. Solo necesitas conocimientos básicos de Python (variables, loops, funciones) y familiaridad con Pandas (deseable pero no obligatorio). El nivel es **intermedio-avanzado** pero estructurado para que cualquiera con bases de Python pueda seguirlo.
""")

st.markdown("---")

st.markdown("""
## 🎁 Material Incluido

Con tu inscripción al seminario recibes:

### Código Fuente Completo Multi-Asset
- Scripts de scraping documentados para cada asset class
- Pipeline ETL profesional unificado con manejo de errores
- Módulos de análisis específicos y compartidos entre assets
- Funciones de screening cross-asset
- Notebooks Jupyter con explicaciones detalladas por categoría
- Sistema de correlación entre asset classes

### Cuatro Bases de Datos Completas
- **Stocks:** CSV con 58,168 acciones y 982 métricas
- **ETFs:** CSV con 30,167 fondos y 202 métricas
- **Crypto:** CSV con 67,476 criptomonedas y 421 métricas
- **Forex:** CSV con 7,174 pares y 379 métricas
- Diccionario de datos completo (explicación de cada métrica por asset class)
- Scripts de actualización para refrescar los datos

### Documentación Extensiva
- Guía técnica de 80+ páginas sobre todas las métricas
- Estrategias de screening single-asset y cross-asset
- 15 casos de estudio reales completamente resueltos
- Best practices para scraping multi-source
- Guía de correlaciones históricas entre asset classes
- Troubleshooting guide con soluciones a problemas comunes

### Grabación Completa
- Acceso ilimitado a la grabación del seminario
- Puedes revisarla las veces que necesites
- Transcripción con timestamps para búsqueda rápida
- Material complementario descargable
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
    
    **Requisitos técnicos:** Ordenador con Python 3.8+ instalado, conexión a internet estable, 4GB RAM mínimo, 2GB espacio libre (para las bases de datos)
    
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
        ✓ Todo el código fuente multi-asset<br>
        ✓ 4 bases de datos completas (162K+ instrumentos)<br>
        ✓ Documentación técnica (80+ páginas)<br>
        ✓ 15 casos prácticos resueltos<br>
        ✓ Soporte 30 días post-seminario
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.markdown("""
## 👥 ¿Para Quién Es Este Seminario?

**Perfecto para ti si:**
- Eres **inversor multi-asset** que quiere analizar stocks, ETFs, crypto y forex en un solo lugar
- Trabajas como **analista financiero** o **trader** y necesitas herramientas más potentes
- Eres **gestor de carteras** diversificadas buscando automatizar la selección
- Te interesa el **trading cuantitativo** en múltiples mercados
- Quieres **independencia** de plataformas y **control total** sobre tus datos
- Necesitas analizar **miles de instrumentos** de forma rápida y eficiente
- Buscas detectar **correlaciones cross-asset** que otros no ven
- Quieres crear **estrategias personalizadas** únicas en el mercado

**Requisitos previos:**
- Python básico: debes saber qué son variables, listas, diccionarios, loops (for/while), funciones, y cómo importar librerías
- Conocimientos de finanzas: entender conceptos básicos de valoración, análisis técnico, y diferentes asset classes
- Familiaridad con Pandas es un plus pero no obligatorio (te explicaré lo necesario)
- Ganas de aprender, practicar y hacer preguntas

**No es para ti si:**
- No tienes ninguna experiencia con Python (necesitas al menos lo básico)
- Buscas un curso de "introducción a las finanzas" - asumimos que entiendes los conceptos fundamentales
- Quieres una solución "click and go" sin entender cómo funciona - aquí construimos desde cero
- No estás dispuesto a invertir tiempo en practicar después del seminario
- Solo te interesa un único asset class y no quieres visión multi-mercado
""")

st.markdown("---")

st.markdown("""
<div style='text-align: center; padding: 50px 20px; background: linear-gradient(135deg, rgba(0, 212, 255, 0.1), rgba(0, 255, 170, 0.1)); border-radius: 15px; margin: 40px 0;'>
    <h2 style='color: #00d4ff; font-size: 2.5rem; margin-bottom: 20px;'>
        🚀 Un Sistema Universal Para Todos los Mercados
    </h2>
    <p style='font-size: 1.3rem; color: #ffffff; line-height: 1.8; max-width: 900px; margin: 20px auto;'>
        Deja de usar 4 plataformas diferentes que te cobran cada mes.<br>
        Deja de analizar manualmente instrumentos con información fragmentada.<br><br>
        Construye un sistema único que analiza:<br>
        <strong style='color: #00d4ff;'>58,168 Stocks</strong> • 
        <strong style='color: #00ffaa;'>30,167 ETFs</strong> • 
        <strong style='color: #ffaa00;'>67,476 Crypto</strong> • 
        <strong style='color: #aa00ff;'>7,174 Forex</strong><br><br>
        <strong style='color: #00d4ff;'>162,985 instrumentos totales. 4 asset classes. 1 solo sistema.</strong><br>
        Control total. Personalización ilimitada. Tuyo para siempre.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

st.markdown("""
<div style='text-align: center; padding: 30px;'>
    <p style='font-size: 1.2rem; color: #00d4ff; margin-bottom: 15px;'>
        💡 <strong>No más decisiones por rumores. Invierte con DATOS en cualquier mercado.</strong>
    </p>
    <p style='font-size: 1rem; color: #888; margin-top: 20px;'>
        © 2026 BQuant Finance | Financial Screener Masterclass<br>
        Para más información: <strong style='color: #00ffaa;'>@Gsnchez</strong> | bquantfinance.com
    </p>
</div>
""", unsafe_allow_html=True)
