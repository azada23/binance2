import streamlit as st

# تعديل لون الخلفية والواجهة باستخدام CSS ليتماشى مع الصورة
st.markdown("""
    <style>
    .stApp {
        background-color: #1a1a1d;
        color: white;
    }
    div[role="button"] {
        color: #4CAF50;
    }
    label {
        color: white;
    }
    .block-container {
        padding: 1rem;
        max-width: 360px;
        margin: 0 auto;
    }
    </style>
    """, unsafe_allow_html=True)

# عنوان الواجهة
st.title("Crypto Trading Simulator")

# تنسيق مشابه للواجهة من الصورة
st.subheader("Settings")

# إعدادات العملة، نوع الصفقة والرافعة المالية
col1, col2 = st.columns(2)
with col1:
    trade_type = st.selectbox("Order Type", ["Market Order", "Limit Order"], key='order_type_1')
with col2:
    leverage = st.selectbox("Leverage", ["1x", "5x", "10x", "20x", "50x"], key='leverage_1')

# إعدادات العزل
margin_type = st.selectbox("Margin Type", ["Isolated", "Cross"], key='margin_type_1')

# إدخال الأسعار: سعر الدخول، وقف الخسارة، والربح المستهدف
st.subheader("Trade Details")
entry_price = st.number_input("Entry Price", value=10400.00, key='entry_price_1')
stop_loss = st.number_input("Stop Loss", value=10300.00, key='stop_loss_1')
take_profit = st.number_input("Take Profit", value=10600.00, key='take_profit_1')

# تنفيذ الصفقة
if st.button("Execute Trade", key='execute_1'):
    st.success(f"Trade executed: {trade_type} with {leverage} leverage on {margin_type}.")
    st.info(f"Entry Price: {entry_price}, Stop Loss: {stop_loss}, Take Profit: {take_profit}")

# تحسين التصميم ليكون مناسبًا لواجهة الهاتف
st.markdown("""
    <style>
    /* تكبير الأزرار والحقول لتتناسب مع شاشة الهاتف */
    button, input {
        font-size: 1.2em;
    }
    .stButton>button {
        width: 100%;
        padding: 1rem;
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
    }
    .stTextInput>div {
        width: 100%;
    }
    .stNumberInput>div {
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)
