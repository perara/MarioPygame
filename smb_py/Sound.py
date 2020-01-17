from smb_py import loaders


class Sound(object):
    def __init__(self):
        self.sounds = {}
        self.load_sounds()

    def load_sounds(self):
        self.sounds['overworld'] = loaders.get_sound('sounds/overworld.wav')
        self.sounds['overworld_fast'] = loaders.get_sound('sounds/overworld-fast.wav')
        self.sounds['level_end'] = loaders.get_sound('sounds/levelend.wav')
        self.sounds['coin'] = loaders.get_sound('sounds/coin.wav')
        self.sounds['small_mario_jump'] = loaders.get_sound('sounds/jump.wav')
        self.sounds['big_mario_jump'] = loaders.get_sound('sounds/jumpbig.wav')
        self.sounds['brick_break'] = loaders.get_sound('sounds/blockbreak.wav')
        self.sounds['block_hit'] = loaders.get_sound('sounds/blockhit.wav')
        self.sounds['mushroom_appear'] = loaders.get_sound('sounds/mushroomappear.wav')
        self.sounds['mushroom_eat'] = loaders.get_sound('sounds/mushroomeat.wav')
        self.sounds['death'] = loaders.get_sound('sounds/death.wav')
        self.sounds['pipe'] = loaders.get_sound('sounds/pipe.wav')
        self.sounds['kill_mob'] = loaders.get_sound('sounds/kill_mob.wav')
        self.sounds['game_over'] = loaders.get_sound('sounds/gameover.wav')
        self.sounds['scorering'] = loaders.get_sound('sounds/scorering.wav')
        self.sounds['fireball'] = loaders.get_sound('sounds/fireball.wav')
        self.sounds['shot'] = loaders.get_sound('sounds/shot.wav')

    def play(self, name, loops, volume):
        self.sounds[name].play(loops=loops)
        self.sounds[name].set_volume(volume)

    def stop(self, name):
        self.sounds[name].stop()

    def start_fast_music(self, core):
        if core.get_map().get_name() == '1-1':
            self.stop('overworld')
            self.play('overworld_fast', 99999, 0.5)
