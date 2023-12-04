import util as ut
import pygame


class GridMusic:
    SOUND_OVERLAP = 5  # min 2

    def __init__(self):
        self.sounds = []
        self.alive_cells_list = []
        pygame.mixer.init()

    @staticmethod
    def note_num(alive_cells):
        val = round(min(220, max(0, alive_cells - 20)) * 87 / 220)
        return val

    @staticmethod
    def note_num_2(alive_cells):
        return round(1/(-alive_cells/(7 * ut.NUM_OF_CELLS) - 1/87) + 87)

    def play_sound(self, alive_cells):
        self.alive_cells_list.append(alive_cells)
        note = self.note_num_2(alive_cells)
        tone_file_path = 'notes/' + ut.NOTES[note] + '.wav'
        s = pygame.mixer.Sound(tone_file_path)
        s.set_volume(ut.SOUND_VOLUME)
        self.sounds.append(s)
        self.advance_sounds()

    def advance_sounds(self):
        if len(self.sounds) > GridMusic.SOUND_OVERLAP:
            self.sounds[-GridMusic.SOUND_OVERLAP].stop()
        self.sounds[-1].play()