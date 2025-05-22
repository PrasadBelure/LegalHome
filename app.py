import streamlit as st
import time

# Configure page
st.set_page_config(
    page_title="LexScanCite - AI-Powered Legal Assistant",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for modern UI (properly formatted for Streamlit)
st.markdown("""
<style>
    /* Hide Streamlit branding and improve base styling */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp > header {visibility: hidden;}
    
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    /* Base styling */
    .stApp {
        font-family: 'Inter', sans-serif;
    }
    
    /* Hero section */
    .hero-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 4rem 2rem;
        border-radius: 20px;
        margin: 2rem 0;
        text-align: center;
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        position: relative;
        overflow: hidden;
    }
    
    .hero-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000"><defs><radialGradient id="a" cx="50%" cy="50%"><stop offset="0%" stop-color="%23ffffff" stop-opacity="0.1"/><stop offset="100%" stop-color="%23ffffff" stop-opacity="0"/></radialGradient></defs><circle cx="50%" cy="50%" r="50%" fill="url(%23a)"/></svg>');
        pointer-events: none;
    }
    
    .hero-title {
        font-size: 4rem;
        font-weight: 800;
        color: white;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        position: relative;
        z-index: 1;
    }
    
    .hero-subtitle {
        font-size: 1.4rem;
        color: rgba(255,255,255,0.9);
        margin-bottom: 2rem;
        font-weight: 300;
        position: relative;
        z-index: 1;
    }
    
    .hero-description {
        font-size: 1.1rem;
        color: rgba(255,255,255,0.8);
        max-width: 700px;
        margin: 0 auto;
        line-height: 1.6;
        position: relative;
        z-index: 1;
    }
    
    /* Feature cards section */
    .features-title {
        font-size: 2.5rem;
        font-weight: 700;
        text-align: center;
        margin: 3rem 0 2rem 0;
        background: linear-gradient(135deg, #667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    /* Stats section */
    .stats-container {
        background: linear-gradient(135deg, #2c3e50, #34495e);
        padding: 3rem 2rem;
        border-radius: 20px;
        margin: 3rem 0;
        text-align: center;
    }
    
    .stats-title {
        color: white;
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 2rem;
    }
    
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 2rem;
        margin-top: 2rem;
    }
    
    .stat-item {
        text-align: center;
        padding: 1.5rem;
        background: rgba(255,255,255,0.1);
        border-radius: 15px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.1);
    }
    
    .stat-number {
        font-size: 3rem;
        font-weight: 800;
        color: #3498db;
        display: block;
        margin-bottom: 0.5rem;
    }
    
    .stat-label {
        font-size: 1rem;
        color: rgba(255,255,255,0.8);
    }
    
    /* About section */
    .about-container {
        background: rgba(248, 249, 250, 0.5);
        padding: 3rem 2rem;
        border-radius: 20px;
        margin: 3rem 0;
        border: 1px solid rgba(229, 231, 235, 0.5);
    }
    
    .about-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: #2c3e50;
        margin-bottom: 2rem;
        text-align: center;
    }
    
    .about-text {
        font-size: 1.1rem;
        line-height: 1.8;
        color: #4a5568;
        margin-bottom: 2rem;
    }
    
    .tech-section {
        margin: 2rem 0;
    }
    
    .tech-title {
        font-size: 1.5rem;
        font-weight: 600;
        color: #2c3e50;
        margin-bottom: 1rem;
    }
    
    .tech-badges {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
        margin: 1rem 0;
    }
    
    .tech-badge {
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 25px;
        font-size: 0.9rem;
        font-weight: 600;
        box-shadow: 0 2px 10px rgba(102, 126, 234, 0.3);
        transition: transform 0.2s ease;
    }
    
    .tech-badge:hover {
        transform: translateY(-2px);
    }
    
    .innovations-list {
        list-style: none;
        padding: 0;
    }
    
    .innovations-list li {
        background: white;
        margin: 1rem 0;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
    
    .innovations-list li strong {
        color: #667eea;
    }
    
    /* Footer */
    .footer-container {
        text-align: center;
        padding: 3rem 2rem;
        background: linear-gradient(135deg, #f8f9fa, #e9ecef);
        border-radius: 20px;
        margin: 3rem 0;
    }
    
    .footer-title {
        font-size: 1.8rem;
        font-weight: 700;
        color: #2c3e50;
        margin-bottom: 1rem;
    }
    
    .footer-text {
        font-size: 1.1rem;
        color: #6c757d;
        margin-bottom: 2rem;
    }
    
    .footer-credits {
        font-size: 0.9rem;
        color: #adb5bd;
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 2.5rem;
        }
        .hero-subtitle {
            font-size: 1.2rem;
        }
        .features-title {
            font-size: 2rem;
        }
        .stats-grid {
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 1rem;
        }
        .tech-badges {
            justify-content: center;
        }
    }
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero-container">
    <div class="hero-title">⚖️ LexScanCite</div>
    <div class="hero-subtitle">AI-Powered Legal Assistant for the Digital Age</div>
    <div class="hero-description">
        Revolutionizing legal research and document analysis with cutting-edge AI technology. 
        Streamline your legal workflow with intelligent incident analysis and comprehensive document processing.
    </div>
</div>
""", unsafe_allow_html=True)

# Features Section Title
st.markdown('<div class="features-title">🚀 Choose Your Legal AI Tool</div>', unsafe_allow_html=True)

# Create two columns for feature cards
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <div style="background: white; padding: 2rem; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); height: 100%; border: 1px solid #e5e7eb;">
        <div style="text-align: center; margin-bottom: 1.5rem;">
            <div style="font-size: 4rem; margin-bottom: 1rem;">🔍</div>
            <h3 style="font-size: 1.8rem; font-weight: 700; color: #2c3e50; margin-bottom: 1rem;">Legal Incident Analyzer</h3>
            <p style="color: #6b7280; font-size: 1rem; line-height: 1.6; margin-bottom: 1.5rem;">
                Transform incident descriptions into relevant IPC sections using advanced AI-powered analysis
            </p>
        </div>
        <div style="margin-bottom: 2rem;">
            <div style="display: flex; align-items: center; margin-bottom: 0.75rem; padding: 0.5rem; background: #f0f9ff; border-radius: 8px;">
                <span style="color: #10b981; margin-right: 0.5rem; font-weight: bold;">✓</span>
                <span style="color: #374151; font-size: 0.95rem;">AI-powered crime type detection</span>
            </div>
            <div style="display: flex; align-items: center; margin-bottom: 0.75rem; padding: 0.5rem; background: #f0f9ff; border-radius: 8px;">
                <span style="color: #10b981; margin-right: 0.5rem; font-weight: bold;">✓</span>
                <span style="color: #374151; font-size: 0.95rem;">Semantic similarity matching with SBERT</span>
            </div>
            <div style="display: flex; align-items: center; margin-bottom: 0.75rem; padding: 0.5rem; background: #f0f9ff; border-radius: 8px;">
                <span style="color: #10b981; margin-right: 0.5rem; font-weight: bold;">✓</span>
                <span style="color: #374151; font-size: 0.95rem;">Comprehensive IPC section mapping</span>
            </div>
            <div style="display: flex; align-items: center; margin-bottom: 0.75rem; padding: 0.5rem; background: #f0f9ff; border-radius: 8px;">
                <span style="color: #10b981; margin-right: 0.5rem; font-weight: bold;">✓</span>
                <span style="color: #374151; font-size: 0.95rem;">Real-time legal analysis & punishment details</span>
            </div>
            <div style="display: flex; align-items: center; margin-bottom: 0.75rem; padding: 0.5rem; background: #f0f9ff; border-radius: 8px;">
                <span style="color: #10b981; margin-right: 0.5rem; font-weight: bold;">✓</span>
                <span style="color: #374151; font-size: 0.95rem;">Gemini AI integration for legal reasoning</span>
            </div>
        </div>
        <div style="text-align: center;">
            <a href="https://prasadbelure-legalagentworking-app-eczbbc.streamlit.app/" target="_blank" 
               style="display: inline-block; background: linear-gradient(45deg, #3b82f6, #1d4ed8); color: white; padding: 12px 30px; 
                      border-radius: 25px; text-decoration: none; font-weight: 600; font-size: 1rem; 
                      box-shadow: 0 4px 15px rgba(59, 130, 246, 0.3); transition: all 0.3s ease;">
                🚀 Launch Incident Analyzer
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="background: white; padding: 2rem; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); height: 100%; border: 1px solid #e5e7eb;">
        <div style="text-align: center; margin-bottom: 1.5rem;">
            <div style="font-size: 4rem; margin-bottom: 1rem;">📄</div>
            <h3 style="font-size: 1.8rem; font-weight: 700; color: #2c3e50; margin-bottom: 1rem;">Legal Document Analyzer</h3>
            <p style="color: #6b7280; font-size: 1rem; line-height: 1.6; margin-bottom: 1.5rem;">
                Comprehensive legal document processing, analysis, and understanding platform
            </p>
        </div>
        <div style="margin-bottom: 2rem;">
            <div style="display: flex; align-items: center; margin-bottom: 0.75rem; padding: 0.5rem; background: #fdf4ff; border-radius: 8px;">
                <span style="color: #10b981; margin-right: 0.5rem; font-weight: bold;">✓</span>
                <span style="color: #374151; font-size: 0.95rem;">Multi-format document processing (PDF/TXT)</span>
            </div>
            <div style="display: flex; align-items: center; margin-bottom: 0.75rem; padding: 0.5rem; background: #fdf4ff; border-radius: 8px;">
                <span style="color: #10b981; margin-right: 0.5rem; font-weight: bold;">✓</span>
                <span style="color: #374151; font-size: 0.95rem;">AI-powered 3-level summarization</span>
            </div>
            <div style="display: flex; align-items: center; margin-bottom: 0.75rem; padding: 0.5rem; background: #fdf4ff; border-radius: 8px;">
                <span style="color: #10b981; margin-right: 0.5rem; font-weight: bold;">✓</span>
                <span style="color: #374151; font-size: 0.95rem;">Legal term extraction & explanation</span>
            </div>
            <div style="display: flex; align-items: center; margin-bottom: 0.75rem; padding: 0.5rem; background: #fdf4ff; border-radius: 8px;">
                <span style="color: #10b981; margin-right: 0.5rem; font-weight: bold;">✓</span>
                <span style="color: #374151; font-size: 0.95rem;">Semantic search within documents</span>
            </div>
            <div style="display: flex; align-items: center; margin-bottom: 0.75rem; padding: 0.5rem; background: #fdf4ff; border-radius: 8px;">
                <span style="color: #10b981; margin-right: 0.5rem; font-weight: bold;">✓</span>
                <span style="color: #374151; font-size: 0.95rem;">Document comparison & Q&A system</span>
            </div>
        </div>
        <div style="text-align: center;">
            <a href="https://prasadbelure-legalagentipc-app-dvb6hh.streamlit.app/" target="_blank" 
               style="display: inline-block; background: linear-gradient(45deg, #9333ea, #7c3aed); color: white; padding: 12px 30px; 
                      border-radius: 25px; text-decoration: none; font-weight: 600; font-size: 1rem; 
                      box-shadow: 0 4px 15px rgba(147, 51, 234, 0.3); transition: all 0.3s ease;">
                📄 Launch Document Analyzer
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Stats Section
st.markdown("""
<div class="stats-container">
    <div class="stats-title">📊 Project Impact</div>
    <div class="stats-grid">
        <div class="stat-item">
            <span class="stat-number">2</span>
            <div class="stat-label">AI-Powered Modules</div>
        </div>
        <div class="stat-item">
            <span class="stat-number">3</span>
            <div class="stat-label">AI Models Integrated</div>
        </div>
        <div class="stat-item">
            <span class="stat-number">500+</span>
            <div class="stat-label">IPC Sections Covered</div>
        </div>
        <div class="stat-item">
            <span class="stat-number">95%</span>
            <div class="stat-label">Analysis Accuracy</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# # About Section
# st.markdown("""
# <div class="about-container">
#     <div class="about-title">📋 About LexScanCite</div>
    
#     <div style="background: white; padding: 2rem; border-radius: 15px; margin-bottom: 2rem; border-left: 5px solid #667eea;">
#         <h4 style="color: #667eea; font-size: 1.3rem; margin-bottom: 1rem;">🎓 Final Year Project - AI in Legal Technology</h4>
#         <div class="about-text">
#             LexScanCite represents the convergence of artificial intelligence and legal technology, designed to democratize access to legal information and streamline legal research processes. This comprehensive platform leverages state-of-the-art AI models to provide intelligent legal assistance for both legal professionals and citizens.
#         </div>
#     </div>
    
#     <div class="tech-section">
#         <div class="tech-title">🔧 Technology Stack</div>
#         <div class="tech-badges">
#             <span class="tech-badge">🤖 Gemini 1.5 Flash</span>
#             <span class="tech-badge">🧠 InLegal-SBERT</span>
#             <span class="tech-badge">📊 Streamlit</span>
#             <span class="tech-badge">🔍 FAISS</span>
#             <span class="tech-badge">📄 PyPDF2</span>
#             <span class="tech-badge">🐍 Python</span>
#             <span class="tech-badge">📈 Pandas</span>
#             <span class="tech-badge">🎯 SentenceTransformers</span>
#         </div>
#     </div>
    
#     <div class="tech-section">
#         <div class="tech-title">✨ Key Innovations</div>
#         <ul class="innovations-list">
#             <li><strong>Dual-Purpose Architecture:</strong> Incident analysis and document processing in one platform</li>
#             <li><strong>AI-First Approach:</strong> Multiple AI models working in harmony for superior results</li>
#             <li><strong>Indian Legal Focus:</strong> Specifically optimized for Indian Penal Code and legal system</li>
#             <li><strong>Real-time Processing:</strong> Instant analysis and results for improved user experience</li>
#             <li><strong>Semantic Understanding:</strong> Goes beyond keyword matching to understand legal context</li>
#         </ul>
#     </div>
# </div>
# """, unsafe_allow_html=True)

# Interactive Demo Section
st.markdown("---")

# Create demo button with better styling
demo_col1, demo_col2, demo_col3 = st.columns([1, 2, 1])

with demo_col2:
    if st.button("🎉 **Quick Demo Overview**", key="demo_btn", use_container_width=True):
        st.balloons()
        st.success("🚀 **Welcome to LexScanCite!** Choose any module above to get started with AI-powered legal analysis!")
        
        # Demo sections
        col_demo1, col_demo2 = st.columns(2)
        
        with col_demo1:
            with st.expander("🔍 **Incident Analyzer Demo Flow**", expanded=True):
                st.markdown("""
                **Step-by-step process:**
                1. **Input:** Describe any criminal incident in plain language
                2. **AI Processing:** Gemini extracts legal summary and identifies crime type
                3. **Matching:** SBERT finds relevant IPC sections semantically
                4. **Ranking:** AI re-ranks results for maximum relevance
                5. **Output:** Get comprehensive IPC sections with punishments
                """)
        
        with col_demo2:
            with st.expander("📄 **Document Analyzer Demo Flow**", expanded=True):
                st.markdown("""
                **Step-by-step process:**
                1. **Upload:** Support for PDF/TXT legal documents
                2. **Processing:** AI extracts and cleans document content
                3. **Analysis:** 3-level summarization and term extraction
                4. **Search:** Semantic search within document content
                5. **Insights:** Q&A system and document comparison tools
                """)

# Footer
st.markdown("""
<div class="footer-container">
    <div class="footer-title">🎯 Ready to Experience AI-Powered Legal Analysis?</div>
    <div class="footer-text">
        Choose your tool above and discover how AI can transform legal research and analysis.
    </div>
    <div class="footer-credits">
        Developed as a Final Year Project | LexScanCite © 2024 | Powered by Advanced AI
    </div>
</div>
""", unsafe_allow_html=True)

# Sidebar with additional info
with st.sidebar:
    st.markdown("### 🔗 Quick Access")
    st.markdown("""
    **Direct Links:**
    - [🔍 Incident Analyzer](https://prasadbelure-legalagentworking-app-eczbbc.streamlit.app/)
    - [📄 Document Analyzer](https://prasadbelure-legalagentipc-app-dvb6hh.streamlit.app/)
    """)
    
    st.markdown("---")
    
    st.markdown("### 📱 Usage Tips")
    st.info("""
    **For Best Experience:**
    - Use desktop for full features
    - Both apps are mobile-responsive
    - Bookmark this page for quick access
    - Try the demo overview button above
    """)
    
    st.markdown("---")
    
    st.markdown("### 🏆 Project Info")
    st.markdown("""
    **Key Features:**
    - 🤖 Advanced AI Integration
    - ⚡ Real-time Analysis
    - 🎯 High Accuracy
    - 📱 Mobile Friendly
    - 🔒 Secure Processing
    """)