from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
#import time
from datetime import datetime
from kivy.core.window import Window
from kivy.metrics import dp
class NotesApp(App):
    def build(self):

        self.current_window = ''

        Window.bind(on_key_down=self.on_keyboard_down)

        self.file_with_dict = open('text_files/notes_file.txt', 'r').read()
        self.dict_with_color = eval(self.file_with_dict)
        print('WINDOW_COLOR_FROM_FILE:      ', self.dict_with_color['window_color'])
        if self.dict_with_color['window_color'] == 'white':
            Window.clearcolor = (1, 1, 1, 1)
        elif self.dict_with_color['window_color'] == 'black':
            Window.clearcolor = (0, 0, 0, 1)


        ############ buttons color ###################

        #Window.clearcolor = (0.2, 0, 0.2, 1)

        if self.dict_with_color['window_color'] == 'black':
            self.button_color_group_1 = (1, 1, 1, .3)
            self.button_color_group_2 = (1, 0, 0, .5)
            self.text_on_label_color_group_1 = (1, 1, 1, 1)
            self.text_color_on_button_group_1 = (1, 1, 1, 1)
            self.textinput_background_color = (1, 1, 1, .1)
            self.textinput_text_color = (1, 1, 1, 1)
        elif self.dict_with_color['window_color'] == 'white':
            self.button_color_group_1 = (1, .4, 0, .3)
            self.button_color_group_2 = (10, 1, 1, .7)
            self.text_on_label_color_group_1 = (0, 0, 0, 1)
            self.text_color_on_button_group_1 = (0, 0, 0, .8)
            self.textinput_background_color = (1, 0, 0, .05)
            self.textinput_text_color = (0, 0, 0, 1)



        #self.button_color_group_1 = (1, 1, 0, 1)
        #self.button_color_group_2 = (10, 1, 1, 1)
        #self.text_on_label_color_group_1 = (0, 0, 0, 1)

        ##############################################




        self.current_window_color = self.dict_with_color['window_color']
        print('CURRENT WINDOW COLOR :',self.current_window_color)


        self.password_from_file = self.dict_with_color['password']
        print('PASSWORD FROM FILE: ',self.password_from_file)
        self.current_password = self.password_from_file





        self.current_date = datetime.now().date()
        self.year = str(self.current_date.year)
        self.month = str(self.current_date.month)
        self.day = str(self.current_date.day)
        if int(self.day) < 10:
            self.day = '0' + self.day








        '''

        self.time = time.asctime().split(' ')
        print(self.time)

        if self.time[1] == 'Jan':
            self.month_in_chislo = '01'
        elif self.time[1] == 'Feb':
            self.month_in_chislo = '02'
        elif self.time[1] == 'Mar':
            self.month_in_chislo = '03'
        elif self.time[1] == 'Apr':
            self.month_in_chislo = '04'
        elif self.time[1] == 'May':
            self.month_in_chislo = '05'
        elif self.time[1] == 'Jun':
            self.month_in_chislo = '06'
        elif self.time[1] == 'Jul':
            self.month_in_chislo = '07'
        elif self.time[1] == 'Aug':
            self.month_in_chislo = '08'
        elif self.time[1] == 'Sep':
            self.month_in_chislo = '09'
        elif self.time[1] == 'Oct':
            self.month_in_chislo = '10'
        elif self.time[1] == 'Nov':
            self.month_in_chislo = '11'
        elif self.time[1] == 'Dec':
            self.month_in_chislo = '12'
        else:
            self.month_in_chislo = '00'
            
        '''

        self.notes_count_str = eval(open('text_files/notes_file.txt', 'r').read())

        self.date_of_first_login = self.notes_count_str['date_of_first_login']
        self.window_color = self.notes_count_str['window_color'] # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        print('WINDOW COLOR: ', self.window_color)
        print('First login:    ',self.date_of_first_login)

        if self.date_of_first_login == '':
            print('NONE !!!!!!!')
            self.notes_count_str['date_of_first_login'] = self.day + '.' + self.month + '.' + self.year
            print('IT WAS DETETIME !!!')


            '''
            if self.time[2] == '':
                self.notes_count_str['date_of_first_login'] = self.time[3] + '.' + self.month_in_chislo + '.' + self.time[-1]
            else:
                self.notes_count_str['date_of_first_login'] = self.time[2] + '.' + self.month_in_chislo + '.' + self.time[-1]
            '''


            self.notes_count_str_on_saving = open('text_files/notes_file.txt', 'w')
            self.notes_count_str_on_saving.write(str(self.notes_count_str))
            self.notes_count_str_on_saving.close()
        else:
            print('First_Login_From_File:    ', self.notes_count_str['date_of_first_login'])


        self.notes_count = int(self.notes_count_str['notes_count'])
        self.notes_count_real = int(self.notes_count_str['notes_count_real'])
        print('REAL:  ',self.notes_count_real)
        self.button_height = 150
        self.gridlayout_height = dp(self.notes_count_real * self.button_height + 100) #<<<<<<<<<<<<<< changed to real





        self.add_note_button = Button(text = 'New',
                                      font_size = 20,
                                      size_hint = (0.3, 0.1),
                                      pos_hint = {'x': 0.69, 'y': 0.89},
                                      on_release = self.add_note,
                                      background_color=self.button_color_group_2,
                                      color=self.text_color_on_button_group_1)

        self.settings_button = Button(text = 'Settings',
                                      font_size = 20,
                                      size_hint = (0.3, 0.1),
                                      pos_hint = {'x': 0.01, 'y': 0.89},
                                      on_release = self.open_app_settings,
                                      background_color=self.button_color_group_2,
                                      color=self.text_color_on_button_group_1)




        self.g = GridLayout(cols = 1,
                            size_hint_y = None,
                            spacing = dp(10),
                            padding = dp(10),
                            height = self.gridlayout_height)


        self.g.orientation = 'bt-lr'




        self.list_of_notes = ScrollView(size_hint = (1, 0.87),
                            pos_hint = {'x': 0, 'y': 0.01})



        self.text_on_empty = Label(text='Empty...\n\nPress "New" to add note',
                                  size_hint=(1, None),
                                  height=dp(150),
                                  font_size=30,
                                  color=self.text_on_label_color_group_1)


        ###########################################################

        for x in range(1, int(self.notes_count) + 1):

            ############################# reading from file ################################

            self.file_with_count_of_notes_in_loop = open('text_files/notes_file.txt', 'r').read()
            self.dict_with_notes_count_in_loop = eval(self.file_with_count_of_notes_in_loop)
            self.name_of_note_in_notes_file_in_loop = 'note_' + str(x)

            if self.name_of_note_in_notes_file_in_loop in self.dict_with_notes_count_in_loop:

                self.title_of_note_in_loop = self.dict_with_notes_count_in_loop[self.name_of_note_in_notes_file_in_loop]['title']

                ################################################################################

                if len(self.title_of_note_in_loop) > 20:
                    self.title_of_note_in_loop = str(self.dict_with_notes_count_in_loop[self.name_of_note_in_notes_file_in_loop]['title'])[:20] + '...'
                if self.title_of_note_in_loop == '':
                    self.title_of_note_in_loop = 'Without title'

                '''
                self.month_in_chislo = 0
                if self.time[1] == 'Jan':
                    self.month_in_chislo = '01'
                elif self.time[1] == 'Feb':
                    self.month_in_chislo = '02'
                elif self.time[1] == 'Mar':
                    self.month_in_chislo = '03'
                elif self.time[1] == 'Apr':
                    self.month_in_chislo = '04'
                elif self.time[1] == 'May':
                    self.month_in_chislo = '05'
                elif self.time[1] == 'Jun':
                    self.month_in_chislo = '06'
                elif self.time[1] == 'Jul':
                    self.month_in_chislo = '07'
                elif self.time[1] == 'Aug':
                    self.month_in_chislo = '08'
                elif self.time[1] == 'Sep':
                    self.month_in_chislo = '09'
                elif self.time[1] == 'Oct':
                    self.month_in_chislo = '10'
                elif self.time[1] == 'Nov':
                    self.month_in_chislo = '11'
                elif self.time[1] == 'Dec':
                    self.month_in_chislo = '12'
                else:
                    self.month_in_chislo = '00'
                self.date_on_note = self.time[2] + '.' + self.month_in_chislo + '.' + self.time[-1]
                '''

                self.date_on_note = self.day + '.' + self.month + '.' + self.year


                if x == 1:
                    #self.date_on_note_from_dict = '00.00.0000'
                    self.date_on_note_from_dict = self.dict_with_notes_count_in_loop['date_of_first_login']
                else:
                    self.date_on_note_from_dict = self.dict_with_notes_count_in_loop[self.name_of_note_in_notes_file_in_loop]['time_of_creation']

                #self.text_on_note = "Without title" + "\n\n" + str(x) + ')     ' + self.date_on_note # <<<<<<<<<<<<<<<
                self.text_on_note = self.title_of_note_in_loop + "\n\n" + str(x) + ')     ' + self.date_on_note_from_dict
                self.b = Button(text = self.text_on_note,
                                size_hint=(1, None),
                                height = dp(self.button_height),
                                font_size=30,
                                on_release = self.open_note,
                                halign = 'center',
                                background_color=self.button_color_group_1,
                                color=self.text_color_on_button_group_1)

                self.b.bind(width=self.update_text_size_on_note_button)  #note buttons binding

                self.g.add_widget(self.b)

        self.gridlayout_height = dp(self.notes_count_real * self.button_height + 10 * (self.notes_count_real + 1)) #<<<<<<<<<<<<<< changed to real
        self.g.height = self.gridlayout_height

        if self.notes_count_real == 0:
            self.g.add_widget(self.text_on_empty)
            self.g.height = dp(200)

        #############################################################

        self.list_of_notes.add_widget(self.g)

        self.page_1 = FloatLayout()
        self.page_1.add_widget(self.list_of_notes)
        self.page_1.add_widget(self.add_note_button)
        self.page_1.add_widget(self.settings_button)

        ############ enter password window ###############

        self.enter_password_layout = FloatLayout()
        self.scrolllayout_in_enter_password_layout = ScrollView(size_hint=(1, 1),
                                                                 pos_hint={'x': 0, 'y': 0})
        self.gridlayout_in_enter_password_layout = GridLayout(cols=1,
                                                               size_hint_y=None,
                                                               spacing=dp(10),
                                                               padding=dp(10),
                                                               height=dp(600))
        self.text_on_enter_password = Label(text='Enter password:',
                                              size_hint=(1, None),
                                              height=dp(150),
                                              font_size=30,
                                              color=self.text_on_label_color_group_1)

        self.textinput_in_enter_password = TextInput(hint_text='Enter password ...',
                                                     size_hint=(1, None),
                                                     height=dp(150),
                                                     font_size=30,
                                                     background_color = self.textinput_background_color,
                                                     foreground_color = self.textinput_text_color)

        self.textinput_in_enter_password.focused = False

        self.text_on_enter_password_incorrect_password = Label(text='',
                         size_hint=(0.3, 0.2),
                         font_size=20,
                         pos_hint={'x': 0, 'y': 0.8},
                         color=(1.0, 0.0, 0.0, 1.0))

        self.check_the_password_button = Button(text='OK',
                         size_hint=(0.3, 0.2),
                         font_size=30,
                         pos_hint={'x': 0, 'y': 0.8},
                         on_release=self.check_the_password,
                         background_color=self.button_color_group_1,
                         color = self.text_color_on_button_group_1)
        self.textinput_in_enter_password.multiline = False

        self.enter_password_layout.add_widget(self.scrolllayout_in_enter_password_layout)
        self.scrolllayout_in_enter_password_layout.add_widget(self.gridlayout_in_enter_password_layout)
        self.gridlayout_in_enter_password_layout.add_widget(self.text_on_enter_password)
        self.gridlayout_in_enter_password_layout.add_widget(self.textinput_in_enter_password)
        self.gridlayout_in_enter_password_layout.add_widget(self.text_on_enter_password_incorrect_password)
        self.gridlayout_in_enter_password_layout.add_widget(self.check_the_password_button)

        ##################################################

        self.main_app_layout = FloatLayout()
        # self.main_app_layout.add_widget(self.page_1)
        if self.password_from_file == '':
            self.main_app_layout.add_widget(self.page_1)
            self.current_window = 'page_1'
            print('CURRENT WINDOW : ', self.current_window)
        else:
            self.main_app_layout.add_widget(self.enter_password_layout)
            self.current_window = 'enter_password_layout'
            print('CURRENT WINDOW : ', self.current_window)

        '''
        if self.password_from_file == 'None':
            self.main_app_layout.add_widget(self.page_1)
        else:
            print('password was changed ...')
        '''



        #   page to open note


        self.layout_with_note = FloatLayout()
        self.layout_with_note_textinput = TextInput(hint_text = 'Enter text here ...',
                                                    size_hint=(.98, 0.74), ############################ <<<<<<<<<<<<<<<
                                                    pos_hint={'x': 0.01, 'y': 0.01},
                                                    font_size=20,
                                                    background_color=self.textinput_background_color,
                                                    foreground_color=self.textinput_text_color)
        self.back_to_page_1_button = Button(text = '< back',
                                            size_hint=(0.3, 0.1),
                                            font_size=20,
                                            pos_hint={'x': 0.01, 'y': 0.89},
                                            on_release = self.back_to_1_page,
                                            background_color=self.button_color_group_2,
                                            color=self.text_color_on_button_group_1)
        self.layout_with_note_ok_button = Button(text = 'OK',
                                            size_hint=(0.3, 0.1),
                                            font_size=20,
                                            pos_hint={'x': 0.69, 'y': 0.89},
                                            on_release = self.ok_button_in_note_page,
                                            background_color=self.button_color_group_2,
                                            color=self.text_color_on_button_group_1)
        self.layout_with_note_delete_button = Button(text = 'delete',
                                            size_hint=(0.3, 0.1),
                                            font_size=20,
                                            pos_hint={'x': 0.37, 'y': 0.89},
                                            on_release = self.delete_note,
                                            background_color=self.button_color_group_2,
                                            color=self.text_color_on_button_group_1)

        ######### Title of note #############################################

        self.layout_with_note_title = TextInput(hint_text = 'Title ...',
                                                size_hint=(.98, 0.1),
                                                pos_hint={'x': 0.01, 'y': 0.75},
                                                font_size=30,
                                                background_color=self.textinput_background_color,
                                                foreground_color=self.textinput_text_color)
        self.layout_with_note_title.multiline = False

        #####################################################################

        self.layout_with_note.add_widget(self.layout_with_note_textinput)
        self.layout_with_note.add_widget(self.back_to_page_1_button)
        self.layout_with_note.add_widget(self.layout_with_note_ok_button)
        self.layout_with_note.add_widget(self.layout_with_note_delete_button)
        self.layout_with_note.add_widget(self.layout_with_note_title) ########### <<<<<<<<<<<<<<<<<<<<<<<<<



        ###################

        ####################### settings ###############################


        self.settings_layout = FloatLayout()
        self.scrolllayout_in_settings_page = ScrollView(size_hint = (1, 0.87),
                                                        pos_hint = {'x': 0, 'y': 0})
        self.gridlayout_in_settings_page = GridLayout(cols = 1,
                                            size_hint_y = None,
                                            spacing = dp(10),
                                            padding = dp(10),
                                            height = dp(330))
        self.current_note = None
        self.back_to_page_1_button_2 = Button(text='< back',
                                            size_hint=(0.3, 0.1),
                                            font_size=20,
                                            pos_hint={'x': 0.01, 'y': 0.89},
                                            on_release=self.back_to_1_page,
                                            background_color=self.button_color_group_2,
                                            color=self.text_color_on_button_group_1)
        self.appearance_button = Button(text = 'Appearance >',
                                        size_hint = (1, None),
                                        height = dp(150),
                                        font_size = 30,
                                        on_release = self.open_appearance_page,
                                        background_color=self.button_color_group_1,
                                        color=self.text_color_on_button_group_1)
        self.password_button = Button(text='Password >',
                                        size_hint=(1, None),
                                        height=dp(150),
                                        font_size=30,
                                        on_release=self.create_or_change_password,
                                        background_color=self.button_color_group_1,
                                        color=self.text_color_on_button_group_1)

        self.gridlayout_in_settings_page.add_widget(self.appearance_button)
        self.gridlayout_in_settings_page.add_widget(self.password_button)

        self.settings_layout.add_widget(self.back_to_page_1_button_2)
        self.scrolllayout_in_settings_page.add_widget(self.gridlayout_in_settings_page)
        self.settings_layout.add_widget(self.scrolllayout_in_settings_page)



        ##############################################################

        ############## create_or_change_password_layout ##############

        self.create_or_change_password_layout = FloatLayout()
        self.scrolllayout_in_create_or_change_password_layout = ScrollView(size_hint=(1, 0.87),
                                                        pos_hint={'x': 0, 'y': 0})
        self.gridlayout_in_create_or_change_password_layout = GridLayout(cols=1,
                                                      size_hint_y=None,
                                                      spacing=dp(10),
                                                      padding=dp(10),
                                                      height=dp(170))
        self.create_password_button = Button(text='Create >',
                                        size_hint=(1, None),
                                        height=dp(150),
                                        font_size=30,
                                        on_release=self.create_password,
                                        background_color=self.button_color_group_1,
                                        color=self.text_color_on_button_group_1)
        self.change_password_button = Button(text='Change password >',
                                        size_hint=(1, None),
                                        height=dp(150),
                                        font_size=30,
                                        on_release=self.create_password,
                                        background_color=self.button_color_group_1,
                                        color=self.text_color_on_button_group_1)
        self.remove_password_button = Button(text='Remove password >',
                                        size_hint=(1, None),
                                        height=dp(150),
                                        font_size=30,
                                        on_release=self.remove_password,
                                        background_color=self.button_color_group_1,
                                        color=self.text_color_on_button_group_1)
        self.back_to_settings_button_3 = Button(text='< back',
                                              size_hint=(0.3, 0.1),
                                              font_size=20,
                                              pos_hint={'x': 0.01, 'y': 0.89},
                                              on_release=self.back_to_settings,
                                              background_color=self.button_color_group_2,
                                              color=self.text_color_on_button_group_1)
        self.create_or_change_password_layout.add_widget(self.scrolllayout_in_create_or_change_password_layout)
        self.scrolllayout_in_create_or_change_password_layout.add_widget(self.gridlayout_in_create_or_change_password_layout)
        self.create_or_change_password_layout.add_widget(self.back_to_settings_button_3)

        ##############################################################

        ############## create_password_layout ##############

        self.create_password_layout = FloatLayout()
        self.scrolllayout_in_create_password_layout = ScrollView(size_hint=(1, 0.87),
                                                        pos_hint={'x': 0, 'y': 0})
        self.gridlayout_in_create_password_layout = GridLayout(cols=1,
                                                      size_hint_y=None,
                                                      spacing=dp(10),
                                                      padding=dp(10),
                                                      height=dp(490))
        self.text_button = Label(text='Password:',
                                    size_hint=(1, None),
                                    height=dp(150),
                                    font_size=30,
                                    color=self.text_on_label_color_group_1)
        self.back_to_create_or_change_password_layout = Button(text='< back',
                                              size_hint=(0.3, 0.1),
                                              font_size=20,
                                              pos_hint={'x': 0.01, 'y': 0.89},
                                              on_release=self.create_or_change_password,
                                              background_color=self.button_color_group_2,
                                              color=self.text_color_on_button_group_1)
        self.textinput_with_new_password = TextInput(hint_text = 'Password ...',
                                                    size_hint=(1, None),
                                                    height=dp(150),
                                                    font_size=30,
                                                    background_color=self.textinput_background_color,
                                                    foreground_color=self.textinput_text_color)

        self.textinput_with_new_password.multiline = False
        self.save_password_button = Button(text = 'OK',
                                  size_hint=(1, None),
                                  height=dp(150),
                                  font_size=30,
                                  on_release=self.save_password,
                                  background_color=self.button_color_group_1,
                                  color=self.text_color_on_button_group_1)
        self.create_password_layout.add_widget(self.scrolllayout_in_create_password_layout)
        self.scrolllayout_in_create_password_layout.add_widget(self.gridlayout_in_create_password_layout)
        self.create_password_layout.add_widget(self.back_to_create_or_change_password_layout)
        self.gridlayout_in_create_password_layout.add_widget(self.text_button)
        self.gridlayout_in_create_password_layout.add_widget(self.textinput_with_new_password)
        self.gridlayout_in_create_password_layout.add_widget(self.save_password_button)

        ##############################################################

        ################## appearance ################################

        self.appearance_layout = FloatLayout()
        self.scrolllayout_in_appearance_page = ScrollView(size_hint=(1, 0.87),
                                                        pos_hint={'x': 0, 'y': 0})
        self.gridlayout_in_appearance_page = GridLayout(cols=1,
                                                      size_hint_y=None,
                                                      spacing=dp(10),
                                                      padding=dp(10),
                                                      height=dp(490))
        self.current_note = None
        self.back_to_settings_button = Button(text='< back',
                                              size_hint=(0.3, 0.1),
                                              font_size=20,
                                              pos_hint={'x': 0.01, 'y': 0.89},
                                              on_release=self.back_to_settings,
                                              background_color=self.button_color_group_2,
                                              color=self.text_color_on_button_group_1)
        self.appearance_button_text = Label(text='Theme:',
                                        size_hint=(1, None),
                                        height=dp(150),
                                        font_size=30,
                                        color=self.text_on_label_color_group_1)

        self.appearance_button_white_window = Button(text='Light',
                                        size_hint=(1, None),
                                        height=dp(150),
                                        font_size=30,
                                        on_release=self.white_window,
                                        background_color=self.button_color_group_1,
                                        color=self.text_color_on_button_group_1)

        self.appearance_button_black_window = Button(text='Dark',
                                                     size_hint=(1, None),
                                                     height=dp(150),
                                                     font_size=30,
                                                     on_release=self.black_window,
                                                     background_color=self.button_color_group_1,
                                                     color=self.text_color_on_button_group_1)

        self.gridlayout_in_appearance_page.add_widget(self.appearance_button_text)
        self.gridlayout_in_appearance_page.add_widget(self.appearance_button_white_window)
        self.gridlayout_in_appearance_page.add_widget(self.appearance_button_black_window)

        self.appearance_layout.add_widget(self.back_to_settings_button)
        self.scrolllayout_in_appearance_page.add_widget(self.gridlayout_in_appearance_page)
        self.appearance_layout.add_widget(self.scrolllayout_in_appearance_page)



        ##############################################################


        ######################## adaptive text ########################

        self.settings_button.bind(width=self.update_text_size)
        self.add_note_button.bind(width=self.update_text_size)
        self.text_on_enter_password.bind(width=self.update_text_size_on_enter_password)
        print('Notes real: ', self.notes_count_real)
        if self.notes_count_real != 0:
            self.b.bind(width=self.update_text_size_on_note_button)
        self.textinput_in_enter_password.bind(width=self.update_text_size_on_enter_password)
        self.check_the_password_button.bind(width=self.update_text_size_on_enter_password)

        self.back_to_page_1_button.bind(width=self.update_text_size)
        self.layout_with_note_ok_button.bind(width=self.update_text_size)
        self.layout_with_note_delete_button.bind(width=self.update_text_size)
        self.layout_with_note_title.bind(width=self.update_text_size_on_note_button)
        self.layout_with_note_textinput.bind(width=self.update_text_size_on_note_button)

        self.back_to_page_1_button_2.bind(width=self.update_text_size)
        self.appearance_button.bind(width=self.update_text_size_on_note_button)
        self.password_button.bind(width=self.update_text_size_on_note_button)

        self.back_to_settings_button.bind(width=self.update_text_size)
        self.appearance_button_text.bind(width=self.update_text_size_on_note_button)
        self.appearance_button_white_window.bind(width=self.update_text_size_on_note_button)
        self.appearance_button_black_window.bind(width=self.update_text_size_on_note_button)

        self.back_to_settings_button_3.bind(width=self.update_text_size)
        self.create_password_button.bind(width=self.update_text_size_on_note_button)
        self.change_password_button.bind(width=self.update_text_size_on_note_button)
        self.remove_password_button.bind(width=self.update_text_size_on_note_button)

        self.back_to_create_or_change_password_layout.bind(width=self.update_text_size)
        self.text_button.bind(width=self.update_text_size_on_note_button)
        self.textinput_with_new_password.bind(width=self.update_text_size_on_note_button)
        self.save_password_button.bind(width=self.update_text_size_on_note_button)

        self.text_on_enter_password_incorrect_password.bind(width=self.update_text_size_on_incorrect_password_text)

        self.text_on_empty.bind(width=self.update_text_size_on_note_button)

        ###############################################################




        return self.main_app_layout

    def update_text_size(self, instance, value):
        print(value)
        print(Window.width)
        if int(Window.width) <= 2000:
            print('< 380 !!!')
            instance.font_size = value / 9
        else:
            instance.font_size = value / 12

    def update_text_size_on_note_button(self, instance, value):



        if int(Window.width) <= 400:
            #print('< 380 !!!')
            instance.font_size = value / 15
            print('adaptive text ...')
        elif int(Window.width) > 400 and int(Window.width) <= 600:
            instance.font_size = value / 17
            print(Window.width)
            print('adaptive text ...')


        elif int(Window.width) > 600 and int(Window.width) <= 732:
            instance.font_size = value / 20
            print(Window.width)
            print('adaptive text ...')
        elif int(Window.width) > 732 and int(Window.width) <= 900:
            instance.font_size = value / 25
            print(Window.width)
            print('adaptive text ...')
        elif int(Window.width) > 900 and int(Window.width) <= 1100:
            instance.font_size = value / 30
            print(Window.width)
            print('adaptive text ...')
        elif int(Window.width) > 1100 and int(Window.width) <= 1300:
            instance.font_size = value / 35
            print(Window.width)
            print('adaptive text ...')
        elif int(Window.width) > 1300 and int(Window.width) <= 1500:
            instance.font_size = value / 40
            print(Window.width)
            print('adaptive text ...')
        elif int(Window.width) > 1500 and int(Window.width) <= 1800:
            instance.font_size = value / 45
            print(Window.width)
            print('adaptive text ...')


    def update_text_size_on_enter_password(self, instance, value):
        print(Window.width)
        if int(Window.width) <= 2000:
            print('< 380 !!!')
            instance.font_size = value / 15

    def update_text_size_on_incorrect_password_text(self, instance, value):
        print(Window.width)
        if int(Window.width) <= 2000:
            print('< 380 !!!')
            instance.font_size = value / 25


    def add_note(self, instance):


        if self.notes_count_real == 0:
            self.g.remove_widget(self.text_on_empty)


        self.notes_count += 1
        self.notes_count_real += 1

        self.gridlayout_height = dp(self.notes_count_real * self.button_height + 10 * (self.notes_count_real + 1)) #<<<<<<<<<<<<<< changed to real
        self.g.height = self.gridlayout_height

        #########################################################

        self.file_with_count_of_notes = open('text_files/notes_file.txt', 'r').read()
        self.dict_with_notes_count = eval(self.file_with_count_of_notes)
        self.dict_with_notes_count['notes_count'] = str(self.notes_count)
        self.dict_with_notes_count['notes_count_real'] = str(self.notes_count_real)

        self.current_date = datetime.now().date()
        self.year = str(self.current_date.year)
        self.month = str(self.current_date.month)
        self.day = str(self.current_date.day)
        if int(self.day) < 10:
            self.day = '0' + self.day

        self.date_on_added_note = self.day + '.' + self.month + '.' + self.year

        print('IT WAS DATETIME !!!')

        '''
        self.time = time.asctime().split(' ')
        if self.time[2] == '':
            self.date_on_added_note = self.time[3] + '.' + str(self.month_in_chislo) + '.' + self.time[-1]
        else:
            self.date_on_added_note = self.time[2] + '.' + str(self.month_in_chislo) + '.' + self.time[-1]
        print(self.date_on_added_note)
        '''



        self.name_of_note_in_notes_file = 'note_' + str(self.notes_count)
        self.dict_with_notes_count[self.name_of_note_in_notes_file] = {'title':'', 'text':'', 'time_of_creation':self.date_on_added_note}


        self.text_on_buttton = self.dict_with_notes_count[self.name_of_note_in_notes_file]['title'] + "\n\n" + str(self.notes_count) + ')     ' + self.dict_with_notes_count[self.name_of_note_in_notes_file]['time_of_creation']
        self.b = Button(text=self.text_on_buttton,
                        size_hint=(1, None),
                        height=dp(self.button_height),
                        font_size=30,
                        on_release = self.open_note,
                        halign = 'center',
                        background_color=self.button_color_group_1,
                        color=self.text_color_on_button_group_1)
        self.b.bind(width=self.update_text_size_on_note_button)  # note buttons binding
        if self.dict_with_notes_count[self.name_of_note_in_notes_file]['title'] == '':
            self.b.text = 'Without title' + "\n\n" + str(self.notes_count) + ')     ' + self.dict_with_notes_count[self.name_of_note_in_notes_file]['time_of_creation']
        self.g.add_widget(self.b)


        self.file_with_notes_count_write = open('text_files/notes_file.txt', 'w')
        self.file_with_notes_count_write.write(str(self.dict_with_notes_count))
        self.file_with_notes_count_write.close()

        #########################################################

        print('Added !')
        print(self.dict_with_notes_count)

    def open_note(self, instance):
        self.open_note_title = instance.text

        #print(self.notes_count)
        #print(len(str(self.notes_count)))
        #self.open_note_title_number_of_note = self.open_note_title.split(')')[0][-1]
        self.open_note_title_number_of_note = int(str(self.open_note_title.split('     ')[0].split('\n\n')[1])[:-1])
        self.name_of_note_in_dict = 'note_' + str(self.open_note_title_number_of_note)
        self.current_note = self.open_note_title_number_of_note
        print(str(self.open_note_title.split('     ')[0].split('\n\n')[1])[:-1])
        #print(self.current_note) ############## <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<,
        #print(self.current_note)

        self.main_app_layout.clear_widgets()
        self.main_app_layout.add_widget(self.layout_with_note)

        self.file_open_note = open('text_files/notes_file.txt', 'r').read()
        self.dict_file_open_note = eval(self.file_open_note)


        #self.read_from_text_file = open('text_files/notes_file.txt', 'r').read()
        self.layout_with_note_textinput.text = self.dict_file_open_note[self.name_of_note_in_dict]['text']
        self.layout_with_note_title.text = self.dict_file_open_note[self.name_of_note_in_dict]['title']

        ##############

        self.current_window = 'Note'
        print('CURRENT WINDOW : ', self.current_window)


    def back_to_1_page(self, instamce):



        self.current_window = 'page_1'
        print('CURRENT WINDOW : ', self.current_window)

        print('Current note', self.current_note)
        print(self.layout_with_note_textinput.text)
        print(self.layout_with_note_title.text)

        ####################################################

        if self.current_note != None:

            self.file_with_count_of_notes_on_close = open('text_files/notes_file.txt', 'r').read()
            self.dict_with_notes_count_on_close = eval(self.file_with_count_of_notes_on_close)
            self.name_of_note_in_notes_file_on_close = 'note_' + str(self.current_note)
            if self.name_of_note_in_notes_file_on_close in self.dict_with_notes_count_on_close:
                if self.current_note == 1:
                    self.dict_with_notes_count_on_close[self.name_of_note_in_notes_file_on_close] = {'title': self.layout_with_note_title.text, 'text': self.layout_with_note_textinput.text}

                else:
                    self.dict_with_notes_count_on_close[self.name_of_note_in_notes_file_on_close] = {'title': self.layout_with_note_title.text, 'text': self.layout_with_note_textinput.text, 'time_of_creation':self.dict_with_notes_count_on_close[self.name_of_note_in_notes_file_on_close]['time_of_creation']}
            #print('NOTHING TO SAVE ...')

            self.file_with_notes_count_write_on_close = open('text_files/notes_file.txt', 'w')
            self.file_with_notes_count_write_on_close.write(str(self.dict_with_notes_count_on_close))
            self.file_with_notes_count_write_on_close.close()

        ####################################################



        self.main_app_layout.clear_widgets()
        #self.main_app_layout.add_widget(self.page_1) <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<,


        '''
        self.file = open('text_files/notes_file.txt', 'w')
        self.file.write(self.layout_with_note_textinput.text)
        self.file.close()
        '''

        self.main_app_layout.add_widget(self.page_1)


        #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        self.g.clear_widgets()

        for x in range(1, int(self.notes_count) + 1):
            self.file_with_count_of_notes_in_loop = open('text_files/notes_file.txt', 'r').read()
            self.dict_with_notes_count_in_loop = eval(self.file_with_count_of_notes_in_loop)
            self.name_of_note_in_notes_file_in_loop = 'note_' + str(x)
            if self.name_of_note_in_notes_file_in_loop in self.dict_with_notes_count_in_loop:
                self.title_of_note_in_loop = self.dict_with_notes_count_in_loop[self.name_of_note_in_notes_file_in_loop]['title']
                if len(self.title_of_note_in_loop) > 20:
                    self.title_of_note_in_loop = str(self.dict_with_notes_count_in_loop[self.name_of_note_in_notes_file_in_loop]['title'])[:20] + '...'
                if self.title_of_note_in_loop == '':
                    self.title_of_note_in_loop = 'Without title'

                ################################################################################


                '''
                self.month_in_chislo = 0

                if self.time[1] == 'Jan':
                    self.month_in_chislo = '01'
                elif self.time[1] == 'Feb':
                    self.month_in_chislo = '02'
                elif self.time[1] == 'Mar':
                    self.month_in_chislo = '03'
                elif self.time[1] == 'Apr':
                    self.month_in_chislo = '04'
                elif self.time[1] == 'May':
                    self.month_in_chislo = '05'
                elif self.time[1] == 'Jun':
                    self.month_in_chislo = '06'
                elif self.time[1] == 'Jul':
                    self.month_in_chislo = '07'
                elif self.time[1] == 'Aug':
                    self.month_in_chislo = '08'
                elif self.time[1] == 'Sep':
                    self.month_in_chislo = '09'
                elif self.time[1] == 'Oct':
                    self.month_in_chislo = '10'
                elif self.time[1] == 'Nov':
                    self.month_in_chislo = '11'
                elif self.time[1] == 'Dec':
                    self.month_in_chislo = '12'
                else:
                    self.month_in_chislo = '00'
                '''


                #self.date_on_note = self.time[2] + '.' + self.month_in_chislo + '.' + self.time[-1]
                self.date_on_note = self.day + '.' + self.month + '.' + self.year
                print('DATETIME')

                if x == 1:
                    #self.date_on_note_from_dict = '00.00.0000'
                    self.date_on_note_from_dict = self.dict_with_notes_count_in_loop['date_of_first_login']
                else:
                    self.date_on_note_from_dict = self.dict_with_notes_count_in_loop[self.name_of_note_in_notes_file_in_loop]['time_of_creation']

                # self.text_on_note = "Without title" + "\n\n" + str(x) + ')     ' + self.date_on_note # <<<<<<<<<<<<<<<
                self.text_on_note = self.title_of_note_in_loop + "\n\n" + str(x) + ')     ' + self.date_on_note_from_dict
                self.b = Button(text=self.text_on_note,
                                size_hint=(1, None),
                                height=dp(self.button_height),
                                font_size=30,
                                on_release=self.open_note,
                                halign='center',
                                background_color=self.button_color_group_1,
                                color=self.text_color_on_button_group_1)
                self.b.bind(width=self.update_text_size_on_note_button)  # note buttons binding
                self.g.add_widget(self.b)

        if self.notes_count_real == 0:
            self.g.add_widget(self.text_on_empty)
            self.g.height = dp(200)

    def ok_button_in_note_page(self, instance):

        if self.current_note != None:

            ####################################################

            self.file_with_count_of_notes_on_close = open('text_files/notes_file.txt', 'r').read()
            self.dict_with_notes_count_on_close = eval(self.file_with_count_of_notes_on_close)
            self.name_of_note_in_notes_file_on_close = 'note_' + str(self.current_note)
            if self.current_note == 1:
                self.dict_with_notes_count_on_close[self.name_of_note_in_notes_file_on_close] = {'title': self.layout_with_note_title.text, 'text': self.layout_with_note_textinput.text}

            else:
                self.dict_with_notes_count_on_close[self.name_of_note_in_notes_file_on_close] = {'title': self.layout_with_note_title.text, 'text': self.layout_with_note_textinput.text, 'time_of_creation':self.dict_with_notes_count_on_close[self.name_of_note_in_notes_file_on_close]['time_of_creation']}

            self.file_with_notes_count_write_on_close = open('text_files/notes_file.txt', 'w')
            self.file_with_notes_count_write_on_close.write(str(self.dict_with_notes_count_on_close))
            self.file_with_notes_count_write_on_close.close()

            ####################################################

            print('saved !')

    def delete_note(self, instance):

        self.notes_count_real -= 1

        self.gridlayout_height = dp(self.notes_count_real * self.button_height + 10 * (self.notes_count_real + 1)) #<<<<<<<<<<<<<< changed to real
        self.g.height = self.gridlayout_height

        self.file_with_count_of_notes_on_close = open('text_files/notes_file.txt', 'r').read()
        self.dict_with_notes_count_on_close = eval(self.file_with_count_of_notes_on_close)

        self.dict_with_notes_count_on_close['notes_count_real'] = str(self.notes_count_real)

        self.name_of_note_in_notes_file_on_close = 'note_' + str(self.current_note)

        print('deleted: ', self.name_of_note_in_notes_file_on_close)

        print(self.dict_with_notes_count_on_close)

        del self.dict_with_notes_count_on_close[self.name_of_note_in_notes_file_on_close]
        #del self.dict_with_notes_count_on_close['note_1']
        print(self.dict_with_notes_count_on_close)

        self.file_with_notes_count_write_on_close = open('text_files/notes_file.txt', 'w')
        self.file_with_notes_count_write_on_close.write(str(self.dict_with_notes_count_on_close))
        self.file_with_notes_count_write_on_close.close()

        print(self.name_of_note_in_notes_file_on_close)
        print('deleted !')

        #################################################################

        self.main_app_layout.clear_widgets()
        self.main_app_layout.add_widget(self.page_1)
        self.g.clear_widgets()

        for x in range(1, int(self.notes_count) + 1):
            self.file_with_count_of_notes_in_loop = open('text_files/notes_file.txt', 'r').read()
            print(self.file_with_count_of_notes_in_loop)
            self.dict_with_notes_count_in_loop = eval(self.file_with_count_of_notes_in_loop)
            self.name_of_note_in_notes_file_in_loop = 'note_' + str(x)
            if self.name_of_note_in_notes_file_in_loop in self.dict_with_notes_count_in_loop:
                self.title_of_note_in_loop = self.dict_with_notes_count_in_loop[self.name_of_note_in_notes_file_in_loop]['title']
                if len(self.title_of_note_in_loop) > 20:
                    self.title_of_note_in_loop = str(self.dict_with_notes_count_in_loop[self.name_of_note_in_notes_file_in_loop]['title'])[:20] + '...'
                if self.title_of_note_in_loop == '':
                    self.title_of_note_in_loop = 'Without title'

                ################################################################################

                '''
                self.month_in_chislo = 0

                if self.time[1] == 'Jan':
                    self.month_in_chislo = '01'
                elif self.time[1] == 'Feb':
                    self.month_in_chislo = '02'
                elif self.time[1] == 'Mar':
                    self.month_in_chislo = '03'
                elif self.time[1] == 'Apr':
                    self.month_in_chislo = '04'
                elif self.time[1] == 'May':
                    self.month_in_chislo = '05'
                elif self.time[1] == 'Jun':
                    self.month_in_chislo = '06'
                elif self.time[1] == 'Jul':
                    self.month_in_chislo = '07'
                elif self.time[1] == 'Aug':
                    self.month_in_chislo = '08'
                elif self.time[1] == 'Sep':
                    self.month_in_chislo = '09'
                elif self.time[1] == 'Oct':
                    self.month_in_chislo = '10'
                elif self.time[1] == 'Nov':
                    self.month_in_chislo = '11'
                elif self.time[1] == 'Dec':
                    self.month_in_chislo = '12'
                else:
                    self.month_in_chislo = '00'
                '''

                #self.date_on_note = self.time[2] + '.' + self.month_in_chislo + '.' + self.time[-1]

                self.date_on_note = self.day + '.' + self.month + '.' + self.year

                if x == 1:
                    #self.date_on_note_from_dict = '00.00.0000'
                    self.date_on_note_from_dict = self.dict_with_notes_count_in_loop['date_of_first_login']
                else:
                    self.date_on_note_from_dict = \
                    self.dict_with_notes_count_in_loop[self.name_of_note_in_notes_file_in_loop]['time_of_creation']

                # self.text_on_note = "Without title" + "\n\n" + str(x) + ')     ' + self.date_on_note # <<<<<<<<<<<<<<<
                self.text_on_note = self.title_of_note_in_loop + "\n\n" + str(
                    x) + ')     ' + self.date_on_note_from_dict
                self.b = Button(text=self.text_on_note,
                                size_hint=(1, None),
                                height=dp(self.button_height),
                                font_size=30,
                                on_release=self.open_note,
                                halign='center',
                                background_color=self.button_color_group_1,
                                color=self.text_color_on_button_group_1)
                self.b.bind(width=self.update_text_size_on_note_button)  # note buttons binding
                self.g.add_widget(self.b)


        self.current_note = None

        if self.notes_count_real == 0:
            self.g.add_widget(self.text_on_empty)
            self.g.height = dp(200)

    def on_pause(self):
        try:
            self.ok_button_in_note_page(1)
        except:
            pass

    def on_stop(self):
        try:
            self.ok_button_in_note_page(1)
        except:
            pass

        print('saved!')

    def open_app_settings(self, instance):
        print('settings ! hehehe')
        self.main_app_layout.clear_widgets()
        self.main_app_layout.add_widget(self.settings_layout)

        self.current_window = 'settings'
        print('CURRENT WINDOW : ', self.current_window)

    def open_appearance_page(self, instance):
        self.main_app_layout.clear_widgets()
        self.main_app_layout.add_widget(self.appearance_layout)

        self.current_window = 'appearance'
        print('CURRENT WINDOW : ', self.current_window)

    def back_to_settings(self, instance):
        print('back')
        self.main_app_layout.clear_widgets()
        self.main_app_layout.add_widget(self.settings_layout)

        self.current_window = 'settings'
        print('CURRENT WINDOW : ', self.current_window)

    def white_window(self, instance):
        print('white')
        Window.clearcolor = (1, 1, 1, 1)
        self.button_color_group_1 = (1, .4, 0, .3)
        self.button_color_group_2 = (10, 1, 1, .7)
        self.text_on_label_color_group_1 = (0, 0, 0, 1)
        self.text_color_on_button_group_1 = (0, 0, 0, .8)

        self.textinput_background_color = (1, 0, 0, .05)
        self.textinput_text_color = (0, 0, 0, 1)

        self.textinput_in_enter_password.background_color = self.textinput_background_color
        self.textinput_in_enter_password.foreground_color = self.textinput_text_color
        self.layout_with_note_textinput.background_color = self.textinput_background_color
        self.layout_with_note_textinput.foreground_color = self.textinput_text_color
        self.layout_with_note_title.background_color = self.textinput_background_color
        self.layout_with_note_title.foreground_color = self.textinput_text_color
        self.textinput_with_new_password.background_color = self.textinput_background_color
        self.textinput_with_new_password.foreground_color = self.textinput_text_color

        #here


        self.back_to_settings_button.background_color = self.button_color_group_2
        self.back_to_settings_button.color = self.text_color_on_button_group_1
        self.appearance_button_text.color = self.text_on_label_color_group_1
        self.appearance_button_white_window.background_color = self.button_color_group_1
        self.appearance_button_white_window.color = self.text_color_on_button_group_1
        self.appearance_button_black_window.background_color = self.button_color_group_1
        self.appearance_button_black_window.color = self.text_color_on_button_group_1
        self.back_to_page_1_button_2.background_color = self.button_color_group_2
        self.back_to_page_1_button_2.color = self.text_color_on_button_group_1
        self.appearance_button.background_color = self.button_color_group_1
        self.appearance_button.color = self.text_color_on_button_group_1
        self.password_button.background_color = self.button_color_group_1
        self.password_button.color = self.text_color_on_button_group_1

        self.create_password_button.background_color = self.button_color_group_1
        self.create_password_button.color = self.text_color_on_button_group_1
        self.change_password_button.background_color = self.button_color_group_1
        self.change_password_button.color = self.text_color_on_button_group_1
        self.remove_password_button.background_color = self.button_color_group_1
        self.remove_password_button.color = self.text_color_on_button_group_1
        self.back_to_settings_button_3.background_color = self.button_color_group_2
        self.back_to_settings_button_3.color = self.text_color_on_button_group_1

        self.text_button.color = self.text_color_on_button_group_1
        self.back_to_create_or_change_password_layout.background_color = self.button_color_group_2
        self.back_to_create_or_change_password_layout.color = self.text_color_on_button_group_1
        self.save_password_button.background_color = self.button_color_group_1
        self.save_password_button.color = self.text_color_on_button_group_1

        self.add_note_button.background_color = self.button_color_group_2
        self.add_note_button.color = self.text_color_on_button_group_1
        self.settings_button.background_color = self.button_color_group_2
        self.settings_button.color = self.text_color_on_button_group_1

        self.back_to_page_1_button.background_color = self.button_color_group_2
        self.back_to_page_1_button.color = self.text_color_on_button_group_1
        self.layout_with_note_ok_button.background_color = self.button_color_group_2
        self.layout_with_note_ok_button.color = self.text_color_on_button_group_1
        self.layout_with_note_delete_button.background_color = self.button_color_group_2
        self.layout_with_note_delete_button.color = self.text_color_on_button_group_1

        self.text_on_empty.color = self.text_color_on_button_group_1



        ####### writing to a file ################

        self.file_with_dict = open('text_files/notes_file.txt', 'r').read()
        self.dict_with_color = eval(self.file_with_dict)
        self.dict_with_color['window_color'] = 'white'

        self.file_with_dict_on_close = open('text_files/notes_file.txt', 'w')
        self.file_with_dict_on_close.write(str(self.dict_with_color))
        self.file_with_dict_on_close.close()

        self.current_window_color = 'white'
        print('CURRENT WINDOW COLOR : ',self.current_window_color)

        ##########################################

    def black_window(self, instance):
        print('black')
        Window.clearcolor = (0, 0, 0, 1)

        self.button_color_group_1 = (1, 1, 1, .3)
        self.button_color_group_2 = (1, 0, 0, .5)
        self.text_on_label_color_group_1 = (1, 1, 1, 1)
        self.text_color_on_button_group_1 = (1, 1, 1, 1)

        self.textinput_background_color = (1, 1, 1, .1)
        self.textinput_text_color = (1, 1, 1, 1)

        self.textinput_in_enter_password.background_color = self.textinput_background_color
        self.textinput_in_enter_password.foreground_color = self.textinput_text_color
        self.layout_with_note_textinput.background_color = self.textinput_background_color
        self.layout_with_note_textinput.foreground_color = self.textinput_text_color
        self.layout_with_note_title.background_color = self.textinput_background_color
        self.layout_with_note_title.foreground_color = self.textinput_text_color
        self.textinput_with_new_password.background_color = self.textinput_background_color
        self.textinput_with_new_password.foreground_color = self.textinput_text_color

        self.appearance_button_text.color = self.text_on_label_color_group_1

        self.back_to_settings_button.background_color = self.button_color_group_2
        self.back_to_settings_button.color = self.text_color_on_button_group_1
        self.appearance_button_text.color = self.text_on_label_color_group_1
        self.appearance_button_white_window.background_color = self.button_color_group_1
        self.appearance_button_white_window.color = self.text_color_on_button_group_1
        self.appearance_button_black_window.background_color = self.button_color_group_1
        self.appearance_button_black_window.color = self.text_color_on_button_group_1
        self.back_to_page_1_button_2.background_color = self.button_color_group_2
        self.back_to_page_1_button_2.color = self.text_color_on_button_group_1
        self.appearance_button.background_color = self.button_color_group_1
        self.appearance_button.color = self.text_color_on_button_group_1
        self.password_button.background_color = self.button_color_group_1
        self.password_button.color = self.text_color_on_button_group_1

        self.create_password_button.background_color = self.button_color_group_1
        self.create_password_button.color = self.text_color_on_button_group_1
        self.change_password_button.background_color = self.button_color_group_1
        self.change_password_button.color = self.text_color_on_button_group_1
        self.remove_password_button.background_color = self.button_color_group_1
        self.remove_password_button.color = self.text_color_on_button_group_1
        self.back_to_settings_button_3.background_color = self.button_color_group_2
        self.back_to_settings_button_3.color = self.text_color_on_button_group_1

        self.text_button.color = self.text_color_on_button_group_1
        self.back_to_create_or_change_password_layout.background_color = self.button_color_group_2
        self.back_to_create_or_change_password_layout.color = self.text_color_on_button_group_1
        self.save_password_button.background_color = self.button_color_group_1
        self.save_password_button.color = self.text_color_on_button_group_1

        self.add_note_button.background_color = self.button_color_group_2
        self.add_note_button.color = self.text_color_on_button_group_1
        self.settings_button.background_color = self.button_color_group_2
        self.settings_button.color = self.text_color_on_button_group_1

        self.back_to_page_1_button.background_color = self.button_color_group_2
        self.back_to_page_1_button.color = self.text_color_on_button_group_1
        self.layout_with_note_ok_button.background_color = self.button_color_group_2
        self.layout_with_note_ok_button.color = self.text_color_on_button_group_1
        self.layout_with_note_delete_button.background_color = self.button_color_group_2
        self.layout_with_note_delete_button.color = self.text_color_on_button_group_1

        self.text_on_empty.color = self.text_color_on_button_group_1


        print('TEXT ON LABEL COLOR : ', self.text_on_label_color_group_1)
        print('LABEL COLOR IN APP : ', self.appearance_button_text.color)

        ####### writing to a file ################

        self.file_with_dict = open('text_files/notes_file.txt', 'r').read()
        self.dict_with_color = eval(self.file_with_dict)
        self.dict_with_color['window_color'] = 'black'

        self.file_with_dict_on_close = open('text_files/notes_file.txt', 'w')
        self.file_with_dict_on_close.write(str(self.dict_with_color))
        self.file_with_dict_on_close.close()

        self.current_window_color = 'black'
        print('CURRENT WINDOW COLOR : ',self.current_window_color)

        ##########################################

    def create_or_change_password(self, instance):

        self.current_window = 'create_or_change_password'
        print('CURRENT WINDOW : ', self.current_window)

        '''
        self.password_from_file_for_layout = open('text_files/notes_file.txt', 'r').read()
        self.password_from_file_for_layout_dict = eval(self.password_from_file_for_layout)
        self.password_from_file = self.password_from_file_for_layout_dict['password']
        '''

        print('password XD')
        self.main_app_layout.clear_widgets()
        self.main_app_layout.add_widget(self.create_or_change_password_layout)
        print('CURRENT PASSWORD: ', self.current_password)
        if self.current_password == '':
            self.gridlayout_in_create_or_change_password_layout.clear_widgets()
            self.gridlayout_in_create_or_change_password_layout.add_widget(self.create_password_button)
            self.gridlayout_in_create_or_change_password_layout.height = dp(170)
            self.text_button.text = 'Password:'
        else:
            self.gridlayout_in_create_or_change_password_layout.clear_widgets()
            self.gridlayout_in_create_or_change_password_layout.add_widget(self.change_password_button)
            self.gridlayout_in_create_or_change_password_layout.add_widget(self.remove_password_button)
            self.gridlayout_in_create_or_change_password_layout.height = dp(330)
            self.text_button.text = 'New password:'

    def create_password(self, instance):

        self.current_window = 'create_password'
        print('CURRENT WINDOW : ', self.current_window)


        print('create')
        self.main_app_layout.clear_widgets()
        self.main_app_layout.add_widget(self.create_password_layout)

    def save_password(self, instance):

        self.text_from_textinput_with_password = self.textinput_with_new_password.text
        print(self.text_from_textinput_with_password)
        self.file_with_old_password = open('text_files/notes_file.txt', 'r').read()
        self.dict_with_old_password = eval(self.file_with_old_password)
        self.dict_with_old_password['password'] = self.text_from_textinput_with_password
        self.file_with_old_password_on_close = open('text_files/notes_file.txt', 'w')
        self.file_with_old_password_on_close.write(str(self.dict_with_old_password))
        self.file_with_old_password_on_close.close()

        print('PASSWORD SAVED')
        self.current_password = self.text_from_textinput_with_password

        self.create_or_change_password(1)

    def remove_password(self, instance):

        self.file_with_old_password_on_remove = open('text_files/notes_file.txt', 'r').read()
        self.dict_with_old_password_on_remove = eval(self.file_with_old_password_on_remove)
        self.dict_with_old_password_on_remove['password'] = ''
        self.file_with_old_password_on_close_on_remove = open('text_files/notes_file.txt', 'w')
        self.file_with_old_password_on_close_on_remove.write(str(self.dict_with_old_password_on_remove))
        self.file_with_old_password_on_close_on_remove.close()
        self.current_password = ''
        self.create_or_change_password(1)

        print('PASSWORD REMOWED !')

    def check_the_password(self, instance):
        print('Nice password !')
        self.text_from_textinput_in_enter_password = self.textinput_in_enter_password.text
        if self.text_from_textinput_in_enter_password == self.password_from_file:
            print('YEEEEEEEEEEEEEEES!')
            self.main_app_layout.clear_widgets()
            self.main_app_layout.add_widget(self.page_1)

            self.current_window = 'page_1'
            print('CURRENT WINDOW : ', self.current_window)

        else:
            print('NOOOOOOOOOOOOOOOO!')
            self.text_on_enter_password_incorrect_password.text = 'Incorrect password...'



    def on_keyboard_down(self, instance, keyboard, keycode, text, modifiers):
        #print('###############')
        #print('INSTANCE : ', instance)
        #print('KEYBOARD : ', keyboard)
        #print('CEYCODE : ', keycode)
        #print('TEXT : ', text)
        #print('MODIFIERS : ', modifiers)
        #print('###############')
        #print(keycode)
        #print(text)
        #print('looooooooooool')
        if keycode == 41:
            if self.current_window == 'page_1':
                print('Esc')
                return True
            if self.current_window == 'Note':
                self.back_to_1_page(1)
                return True
            if self.current_window == 'settings':
                self.back_to_1_page(1)
                return True
            if self.current_window == 'appearance':
                self.back_to_settings(1)
                return True
            if self.current_window == 'create_or_change_password':
                self.back_to_settings(1)
                return True
            if self.current_window == 'create_password':
                self.create_or_change_password(1)
                return True

        if keycode == 40 and self.current_window == 'enter_password_layout':
            self.check_the_password(1)
        if keycode == 88 and self.current_window == 'enter_password_layout':
            self.check_the_password(1)

        if keycode == 58:
            print('It was F1')
            return True




NotesApp().run()

