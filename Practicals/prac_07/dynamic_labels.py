from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names_list = {"Kaity Brown", "Abigail Dota", "Fredalin Jacobs"}
        # Name list

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.add_widgets()
        return self.root

    def add_widgets(self):
        for name in self.names_list:
            temp_label = Label(text=name, id=name)
            self.root.ids.entries_box.add_widget(temp_label)


DynamicLabelsApp().run()
