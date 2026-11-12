import webview
import printer

printer = printer.Printer()

print()
print("__-___-__--_-_")

class Api:
    def hello(self, data):
        print(data, flush=True)
        return "received"

    def print_bill(self, items):
        for item in items:
            printer.items.append(item)

        #printer.print()

window = webview.create_window(
    title="SOL Bites POS",
    url="https://ab11pos.streamlit.app",
    width=1280,
    height=800,
    resizable=True,
    js_api=Api()
)

webview.start()