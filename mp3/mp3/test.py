import vlc

song = vlc.MediaPlayer("/home/kali/Desktop/mp3/BassitJaEbal/65daysofstatic - Mountainhead.mp3")
song.play()
print(song.mlr)