import streamlit as st

# عنوان التطبيق
st.title("Crypto Trading Simulator")

# اختيار العملة
currency = st.selectbox("Select Currency", ["BTC/USDT", "ETH/USDT", "BNB/USDT"])

# اختيار الرافعة المالية
leverage = st.slider("Leverage (x)", min_value=1, max_value=100, value=10)

# اختيار نوع الصفقة
trade_type = st.selectbox("Trade Type", ["Market Order", "Limit Order"])

# إدخال الأسعار
entry_price = st.number_input("Entry Price", value=10400.00)
stop_loss = st.number_input("Stop Loss", value=10300.00)
take_profit = st.number_input("Take Profit", value=10600.00)

# زر لتنفيذ الصفقة
if st.button("Execute Trade"):
    st.write(f"Trade executed: {currency} with {leverage}x leverage.")
    st.write(f"Entry Price: {entry_price}, Stop Loss: {stop_loss}, Take Profit: {take_profit}")

import streamlit as st

# تعديل لون الخلفية والواجهة باستخدام CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #1a1a1d;
        color: white;
    }
    div[role="button"] {
        color: #4CAF50;
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
    trade_type = st.selectbox("Order Type", ["Market Order", "Limit Order"], key='order_type', label_visibility="collapsed")
with col2:
    leverage = st.selectbox("Leverage", ["1x", "5x", "10x", "20x", "50x"], key='leverage', label_visibility="collapsed")

# إعدادات العزل
margin_type = st.selectbox("Margin Type", ["Isolated", "Cross"], key='margin_type', label_visibility="collapsed")

# إدخال الأسعار: سعر الدخول، وقف الخسارة، والربح المستهدف
st.subheader("Trade Details")
entry_price = st.number_input("Entry Price", value=10400.00)
stop_loss = st.number_input("Stop Loss", value=10300.00)
take_profit = st.number_input("Take Profit", value=10600.00)

# تنفيذ الصفقة
if st.button("Execute Trade", key='execute', help="Click to execute your trade"):
    st.success(f"Trade executed: {trade_type} with {leverage} leverage on {margin_type}.")
    st.info(f"Entry Price: {entry_price}, Stop Loss: {stop_loss}, Take Profit: {take_profit}")


