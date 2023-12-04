import tkinter as tk
import util as ut


class Settings:

    def __init__(self, start_game_func):
        self.root = tk.Tk()
        self.root.geometry(f'{ut.SETTINGS_SCREEN[0]}x{ut.SETTINGS_SCREEN[1]}')
        icon = tk.PhotoImage(file='tab_icon.png')
        self.root.iconphoto(True, icon)
        self.root.config(bg=ut.SETTINGS_BG)
        # self.root.state('zoomed')
        self.root.title('Game of Life ' + ut.VERSION + ' - Settings')

        self.frame_1 = tk.Frame(self.root, bg=ut.SETTINGS_BG, )
        self.frame_1.grid(row=0, padx=(ut.SETTINGS_PAD, 0), sticky=tk.W)

        self.start_game_func = start_game_func

        self.start_game_button = tk.Button(self.frame_1, text='Start Game', width=25, command=self.start_game,
                                           bg=ut.BUTTON_COLOR)
        self.start_game_button.grid(row=7, pady=(ut.SETTINGS_PAD, 0), sticky=tk.W)

        self.mod_entry = tk.Entry(self.frame_1, exportselection=False)
        self.screen_length_entry = tk.Entry(self.frame_1, exportselection=False)
        self.screen_high_entry = tk.Entry(self.frame_1, exportselection=False)
        self.square_size_entry = tk.Entry(self.frame_1, exportselection=False)
        self.ticks_entry = tk.Entry(self.frame_1, exportselection=False)
        self.volume_entry = tk.Entry(self.frame_1, exportselection=False)
        self.sound = tk.IntVar()
        self.sound_check = tk.Checkbutton(self.frame_1, text='Sound', variable=self.sound)
        self.sound_check.grid(row=6, sticky=tk.W, pady=(ut.SETTINGS_PAD, 0))
        self.entry_list = [self.mod_entry, self.screen_high_entry, self.screen_length_entry, self.square_size_entry,
                           self.ticks_entry, self.volume_entry]

        self.init_interface()
        self.frame_1.mainloop()

    def start_game(self):
        players = self.mod_entry.get()
        if players.isdigit() and 0 < int(players) < ut.MOD:
            ut.MOD = int(players) + 1

        screen_length = self.screen_length_entry.get()
        if screen_length.isdigit():
            ut.SCREEN_SIZE[0] = int(screen_length)

        screen_high = self.screen_high_entry.get()
        if screen_high.isdigit():
            ut.SCREEN_SIZE[0] = int(screen_high)

        square_size = self.square_size_entry.get()
        if square_size.isdigit() and 0 < int(square_size) < min(ut.SCREEN_SIZE[0], ut.SCREEN_SIZE[1]):
            ut.SQUARE_SIZE = int(square_size)

        ticks = self.ticks_entry.get()
        if ticks.isdigit() and int(ticks) >= 0:
            ut.GAME_TICK = int(ticks)

        volume = self.volume_entry.get()
        if volume.isdigit() and 0 < int(volume) < 1:
            ut.SOUND_VOLUME = int(volume)

        ut.SOUND_ON = self.sound.get() == 1

        self.root.destroy()
        self.start_game_func()

    def init_interface(self):
        labels = [tk.Label(self.frame_1, text='Number of Colors (up to 7)', bg=ut.SETTINGS_BG),
                  tk.Label(self.frame_1, text='Screen Length', bg=ut.SETTINGS_BG),
                  tk.Label(self.frame_1, text='Screen High', bg=ut.SETTINGS_BG),
                  tk.Label(self.frame_1, text='Square Size', bg=ut.SETTINGS_BG),
                  tk.Label(self.frame_1, text='Game Tick (in milliseconds)', bg=ut.SETTINGS_BG),
                  tk.Label(self.frame_1, text='Sound Volume (from 0 to 1)', bg=ut.SETTINGS_BG)]

        for i, label in enumerate(labels):
            label.grid(row=i, pady=(ut.SETTINGS_PAD, 0), sticky=tk.W)

        for i, e in enumerate(self.entry_list):
            e.grid(row=i, column=1, pady=(ut.SETTINGS_PAD, 0), sticky=tk.W)
            e.insert(0, ut.DEFAULT_SETTINGS[i])
