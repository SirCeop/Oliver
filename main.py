
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from plyer import tts, stt


class OliverApp(App):

    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=20
        )

        self.texto = Label(
            text="🤖 OLIVER\n\nSeu assistente está pronto!",
            font_size=24
        )

        botao = Button(
            text="🎤 FALAR COM OLIVER",
            font_size=24
        )

        botao.bind(on_press=self.ouvir)

        layout.add_widget(self.texto)
        layout.add_widget(botao)

        return layout

    def ouvir(self, instance):
        self.texto.text = "🎤 Estou ouvindo..."

        try:
            stt.start()
            stt.bind(on_results=self.resultado)

        except Exception as e:
            self.texto.text = "Erro ao abrir microfone:\n" + str(e)

    def resultado(self, recognizer, results):
        if results:
            frase = results[0]

            self.texto.text = (
                "Você disse:\n\n"
                + frase
                + "\n\n🤖 Oliver: Entendi!"
            )

            tts.speak("Entendi. Você disse " + frase)


if __name__ == "__main__":
    OliverApp().run()
