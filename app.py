import kivy

'''


//////////////test file
    хотел сделать интерфейс, но решил делать уже на c++


'''

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout


class MyApp(App):
    def build(self):
        al = BoxLayout(orientation='vertical', padding=[250])

        al.add_widget(TextInput())
        al.add_widget(TextInput())
        al.add_widget(Button(text='login', size_hint=[.5, .5]))

        return al


if __name__ == '__main__':
    MyApp().run()
