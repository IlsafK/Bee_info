from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList

from kivymd.uix.list import OneLineListItem

from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout

from kivymd.font_definitions import fonts
from kivymd.icon_definitions import md_icons

from kivymd.uix.menu import MDDropdownMenu
from kivy.clock import Clock

from kivy.uix.layout import Layout

from kivymd.uix.picker import MDDatePicker
import datetime

from kivymd.uix.label import MDLabel
from kivy.uix.label import Label

KV = '''
#https://stackoverflow.com/questions/65698145/kivymd-tab-name-containing-icons-and-text
# this import will prevent disappear tabs through some clicks on them)))
#:import md_icons kivymd.icon_definitions.md_icons
#:import fonts kivymd.font_definitions.fonts

# Menu item in the DrawerList list.
<ItemDrawer>:
    theme_text_color: "Custom"
    on_release: self.parent.set_color_item(self)

    IconLeftWidget:
        id: icon
        icon: root.icon
        theme_text_color: "Custom"
        text_color: root.text_color


<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"

    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height

        Image:
            id: avatar
            size_hint: None, None
            size: "56dp", "56dp"
            source: "data/logo/logobee.png"

    MDLabel:
        text: app.title
        font_style: "Button"
        size_hint_y: None
        height: self.texture_size[1]

    MDLabel:
        text: app.by_who
        font_style: "Caption"
        size_hint_y: None
        height: self.texture_size[1]

    ScrollView:

        DrawerList:
            id: md_list



Screen:

    MDNavigationLayout:

        ScreenManager:

            Screen:

                BoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: app.title
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]
                        right_action_items: [["star-outline", lambda x: app.on_star_click()]]
                        md_bg_color: 0.7, 1, 0, 1
                        
                    MDTabs:
                        id: tabs
                        on_tab_switch: app.on_tab_switch(*args)                        
                        height: "48dp"
                        tab_indicator_anim: False
                        background_color: 1, 0.5, 0, 1
                        
                        Tab:
                            id: tab1
                            name: 'tab1'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['beehive-outline']}[/size][/font] Оялар "
                            
                            BoxLayout:
                                orientation: 'vertical'
                                padding: "10dp"
                                
                                BoxLayout:
                                    GridLayout:
                                        padding: 10
                                        spacing: 7
                                        cols: 3
                                        BoxLayout:
                                            orientation: 'vertical'
                                            MDLabel:
                                                size_hint: (1, .15)
                                                text: " Әнкә корт:"
                                                halign: "left"
                                                theme_text_color: "Custom"
                                                text_color: 1, 0, 0, 1
                                            Button:
                                                id: buttons1
                                                on_press: app.choice(1)
                                                background_color: (1, 1, 0, 1)
                                        BoxLayout:
                                            orientation: 'vertical'
                                            MDLabel:
                                                size_hint: (1, .15)
                                                text: " Канаты:"
                                                halign: "left"
                                                theme_text_color: "Custom"
                                                text_color: 1, 0, 0, 1
                                            Button:
                                                id: buttons2
                                                on_press: app.choice(2)
                                                background_color: (1, 1, 0, 1)
                                        BoxLayout:
                                            orientation: 'vertical'
                                            MDLabel:
                                                size_hint: (1, .15)
                                                text: " Әнкәнең елы:"
                                                halign: "left"
                                                theme_text_color: "Custom"
                                                text_color: 1, 0, 0, 1
                                            Button:
                                                id: buttons3
                                                on_press: app.choice(3)
                                                background_color: (1, 1, 0, 1)
                                        BoxLayout:
                                            orientation: 'vertical'
                                            MDLabel:
                                                size_hint: (1, .15)
                                                text: " Кая:"
                                                halign: "left"
                                                theme_text_color: "Custom"
                                                text_color: 1, 0, 0, 1
                                            Button:
                                                id: buttons4
                                                on_press: app.choice(4)
                                                background_color: (1, 1, 0, 1)
                                        BoxLayout:
                                            orientation: 'vertical'
                                            MDLabel:
                                                size_hint: (1, .15)
                                                text: " Сетка:"
                                                halign: "left"
                                                theme_text_color: "Custom"
                                                text_color: 1, 0, 0, 1
                                            Button:
                                                id: buttons5
                                                on_press: app.choice(5)
                                                background_color: (1, 1, 0, 1)
                                        BoxLayout:
                                            orientation: 'vertical'
                                            MDLabel:
                                                size_hint: (1, .15)
                                                text: " Корпус:"
                                                halign: "left"
                                                theme_text_color: "Custom"
                                                text_color: 1, 0, 0, 1
                                            Button:
                                                id: buttons6
                                                on_press: app.choice(6)
                                                background_color: (1, 1, 0, 1)
                                BoxLayout:
                                    size_hint: (1, .15)
                                    BoxLayout:
                                        TextInput:
                                            id: data_input
                                            multiline: False
                                            size_hint: (1, 1)
                                    BoxLayout:
                                        size_hint: (.8, 1)
                                        Button:
                                            id: button_confirm
                                            font_size: 40
                                            background_normal: ''
                                            background_color: (1, 0, 0, 1)
                                            text: 'Подтвердить'
                                            on_release: app.confirm()
                                        Button:
                                            id: button_delet
                                            font_size: 40
                                            background_normal: ''
                                            background_color: (0, 0, 1, 1)
                                            text: 'Удалить'
                                            on_release: app.delet()
                                            
                                BoxLayout:
                                    ScrollView:
                                
                                        MDList:
                                    
                                            OneLineAvatarIconListItem:
                                                on_release: app.data_read()
                                                text: 'A1'
                                    
                                                IconLeftWidget:
                                                    icon: "beehive-outline"
                                    
                                            OneLineAvatarIconListItem:
                                                on_release: print("Click 2!")
                                                text: 'A2'
                                    
                                                IconLeftWidget:
                                                    icon: "beehive-outline"
                        
                        Tab:
                            id: tab2
                            name: 'tab2'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['bee']}[/size][/font] Бал"
                            BoxLayout:
                                orientation: 'vertical'
                                padding: "10dp"
                                spacing: "10dp"
                                BoxLayout:
                                    orientation: 'horizontal'
                                    size_hint: (1, 0.15)
                                    MDLabel:
                                        size_hint: (0.10, 1)
                                        text: "Банка саны: "
                                        halign: "left"
                                    MDSlider:
                                        id: slider
                                        size_hint: (0.75, 1)
                                        min: 0
                                        max: 100
                                        value: 1
                                        hint: False
                                    MDLabel:
                                        id: number_of_cans 
                                        size_hint: (0.10, 1)
                                        text: str(int(slider.value))
                                        font_style: "H4"
                                        halign: "center"
                                        theme_text_color: "Custom"
                                        text_color: 0, 0, 1, 1
                                BoxLayout:
                                    orientation: 'horizontal'
                                    size_hint: (1, 0.10)
                                    BoxLayout:
                                        MDLabel:
                                            size_hint: (0.20, 1)
                                            text: "Кая:"
                                            halign: "center"
                                        TextInput:
                                            id: data_input_where
                                            multiline: False
                                            size_hint: (0.80, 1)
                                    BoxLayout:
                                        MDLabel:
                                            size_hint: (0.20, 1)
                                            text: "Кайчан:"
                                            halign: "center"
                                        TextInput:
                                            id: data_input_when
                                            multiline: False
                                            size_hint: (0.80, 1)
                                BoxLayout:
                                    orientation: 'horizontal'
                                    size_hint: (1, 0.1)
                                    pos_hint: {"center_x": .5}
                                    MDLabel:
                                        size_hint: (0.1, 1)
                                        text: "Бәясе:"
                                        halign: "center"
                                    TextInput:
                                        id: data_input_price
                                        multiline: False
                                        size_hint: (0.4, 1)
                                    BoxLayout:
                                        size_hint: (.1, 1)
                                    Button:
                                        id: add
                                        text: "Добавить"
                                        font_size: 40
                                        size_hint: (0.2, 1)
                                        background_normal: ''
                                        background_color: (0, 0, 1, 1)
                                        on_release: app.add()
                                    Button:
                                        id: add
                                        text: "Удалить"
                                        font_size: 40
                                        size_hint: (0.2, 1)
                                        background_normal: ''
                                        background_color: (1, 0, 0, 1)
                                        on_release: app.delet_info_honey()
                                BoxLayout:
                                    orientation: 'horizontal'
                                    TextInput:
                                        id: info_add_honey
                                        haligh: "left"
                                                                         
                        Tab:
                            id: tab3
                            name: 'tab3'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['chart-areaspline']}[/size][/font] График"
                            
                        Tab:
                            id: tab4
                            name: 'tab4'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['chart-pie']}[/size][/font] Диаграмма"
                        
                        Tab:
                            id: tab5
                            name: 'tab5'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['book-open-variant']}[/size][/font] Натиҗә"


        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                id: content_drawer
'''

class ContentNavigationDrawer(BoxLayout):
    pass


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color

class Tab(MDFloatLayout, MDTabsBase):
    pass

class beeinfoApp(MDApp):
    title = "Бал кортлары турында мәгълүмәт"
    by_who = "Капалка"
    nomer_confirm = 0
    nomer = 0

    def build(self):
        # self.theme_cls.theme_style = "Light"  # "Dark"  # "Light"
        return Builder.load_string(KV)
        #return self.screen

    def on_start(self):
        icons_item_menu_lines = {
            "account-circle": "Автор турында",
            "beehive-outline": "Оялар турында мәгълүмәт",
            "bee": "Бал табышы",
            "github": "Github",
        }
        icons_item_menu_tabs = {
            "beehive-outline": "Оялар",  # ab-testing
            "bee": "Бал",
            "chart-areaspline": "График",
            "chart-pie": "Диаграмма",  # chart-arc
            "book-open-variant": "Нәтиҗә",
        }
        for icon_name in icons_item_menu_lines.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item_menu_lines[icon_name])
            )
        # To auto generate tabs
        #for icon_name, name_tab in icons_item_menu_tabs.items():
        #    self.root.ids.tabs.add_widget(
        #        Tab(
        #        text = f" [ref={name_tab}][font={fonts[-1]['fn_regular']}]{md_icons[icon_name]}[/font][/ref]  {name_tab}")
        #     )

    def on_tab_switch(
            self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        '''Called when switching tabs.

        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <__main__.Tab object>;
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        :param tab_text: text or name icon of tab;
        '''

        print(tab_text)

    def on_star_click(self):
        print("star clicked!")
    def confirm(self):
        self.root.ids.button_confirm.background_color = (0, 1, 0, 1)
        self.nomer_confirm = 1

    def data_write_txt(self, id, confirm_data_1):
        f = open('data.txt', 'r', -1, 'utf-8')
        f.seek(0)
        text_read1 = f.readline()
        text_read2 = f.readline()
        text_read3 = f.readline()
        text_read4 = f.readline()
        text_read5 = f.readline()
        text_read6 = f.readline()
        if id == 1:
            text_read1 = confirm_data_1
        elif id == 2:
            text_read2 = confirm_data_1
        elif id == 3:
            text_read3 = confirm_data_1
        elif id == 4:
            text_read4 = confirm_data_1
        elif id == 5:
            text_read5 = confirm_data_1
        elif id == 6:
            text_read6 = confirm_data_1
        f.seek(0)
        f = open('data.txt', 'w', -1, 'utf-8')
        f.write(f"{text_read1}")
        f.write(f"{text_read2}")
        f.write(f"{text_read3}")
        f.write(f"{text_read4}")
        f.write(f"{text_read5}")
        f.write(f"{text_read6}")
        print(text_read6)
        f.close()

    def choice(self, button_id):
        if self.nomer_confirm == 1:
            self.root.ids.button_confirm.background_color = (1, 0, 0, 1)
            self.nomer_confirm = 0
            confirm_data = self.root.ids.data_input.text
            if button_id == 1:
                self.root.ids.buttons1.text = confirm_data
                self.data_write_txt(1, confirm_data)
            elif button_id == 2:
                self.root.ids.buttons2.text = confirm_data
                self.data_write_txt(2, confirm_data)
            elif button_id == 3:
                self.root.ids.buttons3.text = confirm_data
                self.data_write_txt(3, confirm_data)
            elif button_id == 4:
                self.root.ids.buttons4.text = confirm_data
                self.data_write_txt(4, confirm_data)
            elif button_id == 5:
                self.root.ids.buttons5.text = confirm_data
                self.data_write_txt(5, confirm_data)
            elif button_id == 6:
                self.root.ids.buttons6.text = confirm_data
                self.data_write_txt(6, confirm_data)
    def delet(self):
        self.root.ids.data_input.text = ""

    def data_read(self):
        f = open('data.txt', 'r', -1, 'utf-8')
        x1 = f.readline()
        x2 = f.readline()
        x3 = f.readline()
        x4 = f.readline()
        x5 = f.readline()
        x6 = f.readline()
        f.close()
        self.root.ids.buttons1.text = x1
        self.root.ids.buttons2.text = x2
        self.root.ids.buttons3.text = x3
        self.root.ids.buttons4.text = x4
        self.root.ids.buttons5.text = x5
        self.root.ids.buttons6.text = x6
    def add(self):
        where = self.root.ids.data_input_where.text
        when = self.root.ids.data_input_when.text
        price = self.root.ids.data_input_price.text
        can = self.root.ids.number_of_cans.text
        summa = can*price
        if not ((where and when and price) == ""):
            self.nomer = self.nomer + 1
            f = open('honey.txt', 'a', -1, 'utf-8')
            f.write(f"{self.nomer}. {where} - {when} - {price}$ - {can} банка\n")
            f.close()
            f = open('honey.txt', 'r', -1, 'utf-8')
            self.root.ids.info_add_honey.text = f'{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}' \
                                                f'{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}' \
                                                f'{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}' \
                                                f'{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}' \
                                                f'{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}' \
                                                f'{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}{f.readline()}'
            f.close()
    def delet_info_honey(self):
        price = self.root.ids.data_input_price.text
        price = price.upper()
        if price == 'DELETE':
            self.nomer = 0
            f = open('honey.txt', 'w', -1, 'utf-8')
            f.write("   Бал саткан турында мәгълүмәт...\n")
            f.close()
    def text_input(self):
        text_inputs = self.root.ids.data_input_when.text
        if len(text_inputs) == 2:
            self.root.ids.data_input_when.text = f'{text_inputs}.'

if __name__ == '__main__':
    try:
        f = open('data.txt', 'r')
    except FileNotFoundError:
        f = open('data.txt', 'w', -1, 'utf-8')
        for n in range(100):
            f.write('нет информации\n')
        f.close()
    try:
        f = open('honey.txt', 'r')
    except:
        f = open('honey.txt', 'w', -1, 'utf-8')
        f.write("   Бал саткан турында мәгълүмәт...\n")
        f.close()
    while True:
        beeinfoApp().run()