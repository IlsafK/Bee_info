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
                                    orientation: 'horizontal'                               
                                    
                                    MDIconButton:
                                        icon: "calendar-month"
                                        
                                    MDTextField:
                                        id: start_date
                                        hint_text: "Start date"
                                        on_focus: if self.focus: app.date_dialog.open()
                                
                                BoxLayout:
                                    orientation: 'horizontal'                         
                                    
                                    MDIconButton:
                                        icon: "cash"
                                        
                                    MDTextField:
                                        id: loan
                                        hint_text: "Loan"
                                    
                                BoxLayout:
                                    orientation: 'horizontal'                                
                                    
                                    MDIconButton:
                                        icon: "clock-time-five-outline"
                                            
                                    MDTextField:
                                        id: months
                                        hint_text: "Months"
                                    
                                BoxLayout:
                                    orientation: 'horizontal'                                 
                                    
                                    MDIconButton:
                                        icon: "bank"
                                            
                                    MDTextField:
                                        id: interest
                                        hint_text: "Interest, %"
                                    
                                    MDTextField:
                                        id: payment_type
                                        hint_text: "Payment type"
                                        on_focus: if self.focus: app.menu.open()
                                
                                MDSeparator:
                                    height: "1dp"
                                    
                                
                                BoxLayout:
                                    orientation: 'horizontal'
                                 
                        
                        Tab:
                            id: tab2
                            name: 'tab2'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['bee']}[/size][/font] Бал"
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
                                                text_color: 0, 0, 1,
                                            Button:
                                                id: buttons1
                                                on_press: app.choice(1)
                                                background_color: (1, 1, 0, 1)
                                        Button:
                                            id: buttons2
                                            on_press: app.choice(2)
                                            background_color: (1, 1, 0, 1)
                                        Button:
                                            id: buttons3
                                            text: 'press me'
                                            on_press: app.choice(3)
                                            background_color: (1, 1, 0, 1)
                                        Button:
                                            id: buttons4
                                            text: 'press me'
                                            on_press: app.choice(4)
                                            background_color: (1, 1, 0, 1)
                                        Button:
                                            id: buttons5
                                            text: 'press me'
                                            on_press: app.choice(5)
                                            background_color: (1, 1, 0, 1)
                                        Button:
                                            id: buttons6
                                            text: 'press me'
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
                                            font_size: 20
                                            background_normal: ''
                                            background_color: (1, 0, 0, 1)
                                            text: 'Подтвердить'
                                            on_release: app.confirm()
                                        Button:
                                            id: button_delet
                                            font_size: 20
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
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)
        # https://kivymd.readthedocs.io/en/latest/components/menu/?highlight=MDDropDownItem#center-position
        #menu_items = [{"icon": "git", "text": f"Item {i}"} for i in range(5)]
        menu_items = [{"icon": "format-text-rotation-angle-up", "text": "annuity"},
                      {"icon": "format-text-rotation-angle-down", "text": "differentiated"}]
        self.menu = MDDropdownMenu(
            caller=self.screen.ids.payment_type,
            items=menu_items,
            position="auto",
            width_mult=4,
        )
        self.menu.bind(on_release=self.set_item)


    def set_item(self, instance_menu, instance_menu_item):
        def set_item(interval):
            self.screen.ids.payment_type.text = instance_menu_item.text
            instance_menu.dismiss()

        Clock.schedule_once(set_item, 0.5)

    def build(self):
        # self.theme_cls.theme_style = "Light"  # "Dark"  # "Light"
        # return Builder.load_string(KV)
        return self.screen

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

    def choice(self, button_id):
        if self.nomer_confirm == 1:
            self.root.ids.button_confirm.background_color = (1, 0, 0, 1)
            self.nomer_confirm = 0
            confirm_data = self.root.ids.data_input.text
            if button_id == 1:
                self.root.ids.buttons1.text = confirm_data
                f = open('data.txt', 'w')
                for n in range(5):
                    f.write("1\n")
                f.write(confirm_data)
                f.close()
            elif button_id == 2:
                self.root.ids.buttons2.text = confirm_data
            elif button_id == 3:
                self.root.ids.buttons3.text = confirm_data
            elif button_id == 4:
                self.root.ids.buttons4.text = confirm_data
            elif button_id == 5:
                self.root.ids.buttons5.text = confirm_data
            elif button_id == 6:
                self.root.ids.buttons6.text = confirm_data
    def delet(self):
        self.root.ids.data_input.text = ""

    def data_read(self):
        f = open('data.txt', 'r')
        x1 = f.readline()
        x2 = f.readline()
        x3 = f.readline()
        f.close()
        self.root.ids.buttons1.text = x1
        self.root.ids.buttons2.text = x2
        self.root.ids.buttons3.text = x3

if __name__ == '__main__':
    beeinfoApp().run()