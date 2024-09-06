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
