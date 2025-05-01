import sqlite3
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.list import MDList, OneLineListItem
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from math import sqrt, sin, cos, tan
import time

# Initialize Database
def init_db():
    conn = sqlite3.connect("history.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS history (id INTEGER PRIMARY KEY, calculation TEXT)"""
    )
    conn.commit()
    conn.close()

KV = """
ScreenManager:
    StartupScreen:
    MainScreen:
    HelpScreen:
    HistoryScreen:
    ConverterScreen:

<StartupScreen>:
    name: "startup"
    FloatLayout:  # Allow absolute positioning

        MDTopAppBar:
            title: "Welcome"
            elevation: 4
            pos_hint: {"top": 1}
            size_hint_x: 1
            size_hint_y: None
            height: "56dp"  # Standard toolbar height

        MDBoxLayout:
            orientation: "vertical"
            spacing: 20
            size_hint: 0.8, None
            height: self.minimum_height
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

            MDRaisedButton:
                text: "Open Calculator"
                size_hint_x: 1
                on_release: app.open_calculator()

            MDRaisedButton:
                text: "Help"
                size_hint_x: 1
                on_release: app.open_help_screen()

            MDRaisedButton:
                text: "Converter"
                size_hint_x: 1
                on_release: app.open_converter_screen()



<MainScreen>:
    name: "main"
    FloatLayout:

        MDTopAppBar:
            title: "Calculator"
            elevation: 4
            pos_hint: {"top": 1}
            size_hint_x: 1
            size_hint_y: None
            height: "56dp"
            left_action_items: [["arrow-left", lambda x: app.back_to_startup()]]
            right_action_items: [["history", lambda x: app.open_history_screen()]]

        MDBoxLayout:
            orientation: "vertical"
            spacing: 10
            padding: 10
            size_hint: 1, None
            height: self.minimum_height
            pos_hint: {"top": 0.9}  # Positioned under the AppBar
            y: "50dp"

            MDTextField:
                id: input_field
                hint_text: "Enter expression"
                font_size: 32
                halign: "center"
                mode: "rectangle"
                size_hint_x: 0.5
                pos_hint: {"center_x": 0.5}

            GridLayout:
                cols: 4
                spacing: 10
                size_hint_y: None
                height: "300dp"
                pos_hint: {"center_x": 0.8}

                MDRaisedButton:
                    text: "7"
                    on_release: app.on_button_press(self)
                MDRaisedButton:
                    text: "8"
                    on_release: app.on_button_press(self)
                MDRaisedButton:
                    text: "9"
                    on_release: app.on_button_press(self)
                MDRaisedButton:
                    text: "/"
                    on_release: app.on_button_press(self)
                MDRaisedButton:
                    text: "4"
                    on_release: app.on_button_press(self)
                MDRaisedButton:
                    text: "5"
                    on_release: app.on_button_press(self)
                MDRaisedButton:
                    text: "6"
                    on_release: app.on_button_press(self)
                MDRaisedButton:
                    text: "*"
                    on_release: app.on_button_press(self)
                MDRaisedButton:
                    text: "1"
                    on_release: app.on_button_press(self)
                MDRaisedButton:
                    text: "2"
                    on_release: app.on_button_press(self)
                MDRaisedButton:
                    text: "3"
                    on_release: app.on_button_press(self)
                MDRaisedButton:
                    text: "-"
                    on_release: app.on_button_press(self)
                MDRaisedButton:
                    text: "C"
                    on_release: app.on_button_press(self)
                MDRaisedButton:
                    text: "0"
                    on_release: app.on_button_press(self)
                MDRaisedButton:
                    text: "="
                    on_release: app.on_button_press(self)
                MDRaisedButton:
                    text: "+"
                    on_release: app.on_button_press(self)
                MDRaisedButton:
                    text: "\u221a"
                    on_release: app.on_button_press(self)
                MDRaisedButton:
                    text: "sin"
                    on_release: app.on_button_press(self)
                MDRaisedButton:
                    text: "cos"
                    on_release: app.on_button_press(self)
                MDRaisedButton:
                    text: "tan"
                    on_release: app.on_button_press(self)


<HelpScreen>:
    name: "help"
    MDBoxLayout:
        orientation: "vertical"
        padding: 20
        spacing: 20

        MDTopAppBar:
            title: "Help"
            elevation: 4
            left_action_items: [["arrow-left", lambda x: app.back_to_startup()]]

        MDLabel:
            text: "Use the calculator or converter. For support, visit www.examplehelp.com"
            halign: "center"
            font_style: "H6"

<HistoryScreen>:
    name: "history"
    MDBoxLayout:
        orientation: "vertical"
        padding: 20
        spacing: 20

        MDTopAppBar:
            title: "History"
            elevation: 4
            left_action_items: [["arrow-left", lambda x: app.back_to_main()]]

        ScrollView:
            MDList:
                id: history_list

<ConverterScreen>:
    name: "converter"
    MDBoxLayout:
        orientation: "vertical"
        spacing: 20
        padding: 20

        MDTopAppBar:
            title: "Converter"
            elevation: 4
            left_action_items: [["arrow-left", lambda x: app.back_to_startup()]]

        MDTextField:
            id: input_value
            hint_text: "Enter value"
            mode: "rectangle"
            size_hint_x: 0.8
            pos_hint: {"center_x": 0.5}

        MDRaisedButton:
            text: "Kg to Lbs"
            on_release: app.convert("kg_to_lbs")
        MDRaisedButton:
            text: "Lbs to Kg"
            on_release: app.convert("lbs_to_kg")
        MDRaisedButton:
            text: "Meters to Feet"
            on_release: app.convert("m_to_ft")
        MDRaisedButton:
            text: "Feet to Meters"
            on_release: app.convert("ft_to_m")

        MDLabel:
            id: output_label
            text: "Result will appear here"
            halign: "center"
            font_style: "H6"
"""

class StartupScreen(Screen):
    pass

class MainScreen(Screen):
    pass

class HelpScreen(Screen):
    pass

class HistoryScreen(Screen):
    pass

class ConverterScreen(Screen):
    pass

class CalculatorApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.theme_style = "Dark"
        self.conn = sqlite3.connect("history.db")
        self.cursor = self.conn.cursor()
        self.last_clear_time = time.time()
        return Builder.load_string(KV)

    def on_stop(self):
        self.conn.close()

    def on_button_press(self, instance):
        text = instance.text
        input_field = self.root.get_screen("main").ids.input_field

        if text in "+-*/" and (not input_field.text or input_field.text[-1] in "+-*/"):
            return

        if text == "C":
            if time.time() - self.last_clear_time < 1:
                input_field.text = ""
            else:
                input_field.text = input_field.text[:-1]
            self.last_clear_time = time.time()

        elif text == "=":
            try:
                expression = input_field.text
                result = str(eval(expression))
                input_field.text = result
                self.save_to_db(f"{expression} = {result}")
            except ZeroDivisionError:
                input_field.text = "Cannot divide by zero"
            except Exception:
                input_field.text = "Invalid expression"

        elif text == "√":
            input_field.text = str(sqrt(float(input_field.text)))
        elif text == "sin":
            input_field.text = str(sin(float(input_field.text)))
        elif text == "cos":
            input_field.text = str(cos(float(input_field.text)))
        elif text == "tan":
            input_field.text = str(tan(float(input_field.text)))
        else:
            input_field.text += text

    def save_to_db(self, calculation):
        self.cursor.execute("INSERT INTO history (calculation) VALUES (?)", (calculation,))
        self.conn.commit()

    def open_calculator(self):
        self.root.current = "main"

    def open_help_screen(self):
        self.root.current = "help"

    def open_converter_screen(self):
        self.root.current = "converter"

    def back_to_startup(self):
        self.root.current = "startup"

    def back_to_main(self):
        self.root.current = "main"

    def open_history_screen(self):
        self.root.current = "history"
        self.load_history()

    def load_history(self):
        history_screen = self.root.get_screen("history")
        history_list = history_screen.ids.history_list
        history_list.clear_widgets()
        self.cursor.execute("SELECT calculation FROM history")
        rows = self.cursor.fetchall()
        for row in rows:
            history_list.add_widget(OneLineListItem(text=row[0]))

    def convert(self, conversion_type):
        screen = self.root.get_screen("converter")
        input_value = screen.ids.input_value.text
        output_label = screen.ids.output_label

        try:
            value = float(input_value)
            if conversion_type == "kg_to_lbs":
                output_label.text = f"{value * 2.20462:.2f} lbs"
            elif conversion_type == "lbs_to_kg":
                output_label.text = f"{value / 2.20462:.2f} kg"
            elif conversion_type == "m_to_ft":
                output_label.text = f"{value * 3.28084:.2f} ft"
            elif conversion_type == "ft_to_m":
                output_label.text = f"{value / 3.28084:.2f} m"
        except ValueError:
            output_label.text = "Invalid input"

if __name__ == "__main__":
    init_db()
    CalculatorApp().run()
