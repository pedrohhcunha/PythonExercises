from pygame import mixer
mixer.init()
mixer.music.load('tocar_mp3.mp3')
mixer.music.play()
input('Agora você escuta?')
