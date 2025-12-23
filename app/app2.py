# import streamlit as st
# import time
# import random

# # ---------------- Page Config ----------------
# st.set_page_config(
#     page_title="Veritas AI - Fake News Detector",
#     page_icon="🛡️",
#     layout="centered",
#     initial_sidebar_state="collapsed"
# )

# # ---------------- Custom CSS (Ported from HTML) ----------------
# st.markdown("""
# <style>
# /* Import Font */
# @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
# @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');

# html, body, [class*="css"] {
#     font-family: 'Plus Jakarta Sans', sans-serif;
# }

# /* Main Background with Gradients */
# .stApp {
#     background-color: #f0f4f8;
#     background-image: 
#         radial-gradient(at 0% 0%, rgba(37, 99, 235, 0.1) 0px, transparent 50%),
#         radial-gradient(at 100% 100%, rgba(139, 92, 246, 0.1) 0px, transparent 50%);
#     background-attachment: fixed;
# }

# /* Glass Panel Styling */
# .glass-panel {
#     background: rgba(255, 255, 255, 0.95);
#     backdrop-filter: blur(12px);
#     border: 1px solid rgba(255, 255, 255, 0.6);
#     box-shadow: 
#         0 4px 6px -1px rgba(0, 0, 0, 0.05),
#         0 10px 15px -3px rgba(0, 0, 0, 0.05),
#         0 0 0 1px rgba(0,0,0,0.02);
#     padding: 2rem;
#     border-radius: 1rem;
#     margin-bottom: 2rem;
# }

# /* Header Text Styles */
# .hero-title {
#     font-size: 3rem;
#     font-weight: 800;
#     text-align: center;
#     background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
#     -webkit-background-clip: text;
#     -webkit-text-fill-color: transparent;
#     line-height: 1.2;
#     margin-bottom: 0.5rem;
# }

# .gradient-accent {
#     background: linear-gradient(135deg, #2563eb, #4f46e5);
#     -webkit-background-clip: text;
#     -webkit-text-fill-color: transparent;
# }

# /* Streamlit Button Overrides to match 'btn-glass' */
# div.stButton > button {
#     width: 100%;
#     background: white;
#     border: 1px solid #e2e8f0;
#     color: #475569;
#     font-weight: 600;
#     padding: 0.6rem 1rem;
#     border-radius: 0.5rem;
#     transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
# }

# div.stButton > button:hover {
#     border-color: #3b82f6;
#     transform: translateY(-2px);
#     box-shadow: 0 4px 12px rgba(37, 99, 235, 0.1);
#     color: #2563eb;
# }

# div.stButton > button:active {
#     background-color: #f1f5f9;
# }

# /* Result Card Styles */
# .result-card {
#     border-radius: 0.75rem;
#     padding: 1.5rem;
#     box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
#     animation: fadeInUp 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards;
#     margin-top: 1.5rem;
# }

# .result-real {
#     background: linear-gradient(to right, #ecfdf5, #f0fdfa);
#     border-left: 4px solid #10b981;
#     border: 1px solid #d1fae5;
# }

# .result-fake {
#     background: linear-gradient(to right, #fef2f2, #fff1f2);
#     border-left: 4px solid #f43f5e;
#     border: 1px solid #ffe4e6;
# }

# @keyframes fadeInUp {
#     from { opacity: 0; transform: translateY(20px); }
#     to { opacity: 1; transform: translateY(0); }
# }

# /* Progress Bar Customization */
# .stProgress > div > div > div > div {
#     background-image: linear-gradient(45deg,rgba(255,255,255,.15) 25%,transparent 25%,transparent 50%,rgba(255,255,255,.15) 50%,rgba(255,255,255,.15) 75%,transparent 75%,transparent);
#     background-size: 1rem 1rem;
# }
# </style>
# """, unsafe_allow_html=True)

# # ---------------- Session State Init ----------------
# if "news_text" not in st.session_state:
#     st.session_state.news_text = ""

# # ---------------- Header Section ----------------
# st.markdown("""
#     <div style="text-align: center; margin-bottom: 2rem;">
#         <div style="display: inline-block; padding: 0.25rem 0.75rem; background: #eff6ff; color: #2563eb; border-radius: 9999px; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; border: 1px solid #dbeafe; margin-bottom: 1.5rem;">
#             Veritas AI
#         </div>
#         <h1 class="hero-title">
#             Detect Misinformation <br>
#             <span class="gradient-accent">Instantly & Accurately</span>
#         </h1>
#         <p style="color: #64748b; font-size: 1.125rem; max-width: 42rem; margin: 0 auto;">
#             Harnessing advanced NLP to analyze semantic patterns and source credibility.
#         </p>
#     </div>
# """, unsafe_allow_html=True)

# # ---------------- Simulation Logic (Ported from JS) ----------------
# def simulate_prediction(text):
#     """
#     Simulates the JS logic from the HTML file.
#     Replace this function with real Model inference when needed.
#     """
#     lower_text = text.lower()
    
#     # Keywords from HTML
#     fake_keywords = [
#         'sleeping for only two hours', '150 years', 'no health problems', 
#         'hide this secret', 'lizard people', 'shocking', 'leaked', 'delete this'
#     ]
#     real_keywords = [
#         'ministry of education', 'digital learning', 'rural areas', 'officials said', 
#         'nasa', 'study', 'research', 'reported', 'announced'
#     ]
    
#     fake_score = 0
#     real_score = 0
    
#     for word in fake_keywords:
#         if word in lower_text: fake_score += 2
            
#     for word in real_keywords:
#         if word in lower_text: real_score += 2
            
#     # Heuristic
#     if fake_score == 0 and real_score == 0:
#         # Deterministic "random" based on length
#         if len(text) % 2 == 0:
#             return True, 65.42
#         else:
#             return False, 72.15
            
#     is_real = real_score >= fake_score
#     confidence = 92.0 + (random.random() * 7)
    
#     return is_real, round(confidence, 2)

# # ---------------- Real Model Logic (Placeholder) ----------------
# # Uncomment this section to use the actual PyTorch model
# """
# @st.cache_resource
# def load_model():
#     # from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification
#     # tokenizer = DistilBertTokenizerFast.from_pretrained("./model")
#     # model = DistilBertForSequenceClassification.from_pretrained("./model")
#     return None, None 

# # tokenizer, model = load_model()
# """

# # ---------------- Main Glass Panel ----------------
# st.markdown('<div class="glass-panel">', unsafe_allow_html=True)

# # Input Label & Char Count
# text_len = len(st.session_state.news_text)
# st.markdown(f"""
#     <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
#         <label style="font-size: 0.875rem; font-weight: 700; color: #334155; text-transform: uppercase; letter-spacing: 0.05em;">
#             📰 News Content
#         </label>
#         <span style="font-size: 0.75rem; color: #94a3b8; font-weight: 500;">{text_len} chars</span>
#     </div>
# """, unsafe_allow_html=True)

# # Text Area
# st.session_state.news_text = st.text_area(
#     "Content",
#     value=st.session_state.news_text,
#     height=200,
#     placeholder="Paste article text or headline here for analysis...",
#     label_visibility="collapsed"
# )

# # Demo Buttons Logic
# col1, col2, col3 = st.columns([1, 1, 2])

# with col1:
#     if st.button("🟢 Real Demo"):
#         st.session_state.news_text = "The Ministry of Education has launched a new digital learning initiative aimed at improving access to online courses for students in rural areas, officials said on Tuesday. The program includes subsidized tablets and free internet connectivity for qualifying households."
#         st.rerun()

# with col2:
#     if st.button("🔴 Fake Demo"):
#         st.session_state.news_text = "Scientists have proven that sleeping for only two hours a day can make humans live up to 150 years without any health problems. The government is trying to hide this secret method to keep the population dependent on expensive healthcare!"
#         st.rerun()

# # ---------------- Analysis Section ----------------
# result_html = ""

# with col3:
#     # Use a primary-styled button logic via CSS targeting or just standard button
#     analyze_clicked = st.button("✨ ANALYZE VERACITY", type="primary")

# if analyze_clicked:
#     if not st.session_state.news_text.strip():
#         st.error("Please enter text to analyze.")
#     else:
#         # Simulate Loading
#         with st.spinner("Analyzing patterns..."):
#             time.sleep(1.2) # Simulate processing time
#             is_real, conf = simulate_prediction(st.session_state.news_text)
            
#             # Prepare Result HTML
#             if is_real:
#                 theme_color = "emerald"
#                 bar_color = "#10b981"
#                 icon = "fa-circle-check"
#                 title = "Likely Authentic"
#                 subtext = "Content aligns with verified sources and standard reporting patterns."
#                 card_class = "result-real"
#                 text_color = "#065f46"
#             else:
#                 theme_color = "rose"
#                 bar_color = "#f43f5e"
#                 icon = "fa-triangle-exclamation"
#                 title = "Likely Misinformation"
#                 subtext = "Significant anomalies detected. Claims deviate from established consensus."
#                 card_class = "result-fake"
#                 text_color = "#9f1239"

#             result_html = f"""
#             <div class="result-card {card_class}">
#                 <div style="display: flex; justify-content: space-between; align-items: start;">
#                     <div style="display: flex; gap: 1rem; align-items: center;">
#                         <div style="font-size: 2rem; color: {text_color};">
#                             <i class="fa-solid {icon}"></i>
#                         </div>
#                         <div>
#                             <h3 style="font-size: 1.25rem; font-weight: 700; color: {text_color}; margin: 0;">{title}</h3>
#                             <p style="font-size: 0.875rem; color: {text_color}; opacity: 0.9; margin-top: 0.25rem;">{subtext}</p>
#                         </div>
#                     </div>
#                     <span style="padding: 0.25rem 0.75rem; background: rgba(255,255,255,0.6); border-radius: 0.5rem; font-weight: 700; color: {text_color}; border: 1px solid rgba(0,0,0,0.05);">
#                         {conf}%
#                     </span>
#                 </div>
#                 <div style="margin-top: 1.5rem; border-top: 1px solid rgba(0,0,0,0.05); padding-top: 1rem;">
#                     <div style="display: flex; justify-content: space-between; font-size: 0.75rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; color: {text_color}; opacity: 0.8; margin-bottom: 0.5rem;">
#                         <span>Confidence Score</span>
#                         <span>High Certainty</span>
#                     </div>
#                     <!-- Custom Progress Bar HTML since we want specific colors -->
#                     <div style="width: 100%; height: 0.75rem; background: white; border-radius: 9999px; overflow: hidden; box-shadow: inset 0 1px 2px rgba(0,0,0,0.1);">
#                         <div style="width: {conf}%; height: 100%; background: {bar_color}; border-radius: 9999px; transition: width 1s ease;"></div>
#                     </div>
#                     <div style="display: flex; gap: 1rem; margin-top: 1rem; font-size: 0.75rem; color: #64748b;">
#                         <div><i class="fa-solid fa-server"></i> Model: DistilBERT v2.5</div>
#                         <div><i class="fa-solid fa-clock"></i> Time: 0.12s</div>
#                     </div>
#                 </div>
#             </div>
#             """

# st.markdown('</div>', unsafe_allow_html=True) # End Glass Panel

# # ---------------- Display Results ----------------
# if result_html:
#     st.markdown(result_html, unsafe_allow_html=True)

# # ---------------- Footer ----------------
# st.markdown("""
#     <div style="text-align: center; color: #94a3b8; font-size: 0.875rem; margin-top: 3rem; font-weight: 500;">
#         © 2025 Veritas AI · Advanced Fake News Detection System
#     </div>
# """, unsafe_allow_html=True


