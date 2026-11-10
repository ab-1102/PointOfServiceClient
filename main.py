import webview


class Api:
    def hello(self, data):
        print(data)


window = webview.create_window(
    title="SOL Bites POS",
    url="https://ab11pos.streamlit.app",
    width=1280,
    height=800,
    resizable=True,
    js_api=Api()
)

webview.start()