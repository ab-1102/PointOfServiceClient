
import webview

window = webview.create_window(
    title="SOL Bites POS Prototype",
    url="https://ab11pos.streamlit.app",
    width=1280,
    height=800,
    resizable=True
)



webview.start()
