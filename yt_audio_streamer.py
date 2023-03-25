import pafy
import os
os.add_dll_directory(r'C:/Program Files/VideoLAN/VLC')
import time
from time import sleep
import PySimpleGUI as sg

import vlc

Instance = vlc.Instance()    
player = Instance.media_player_new()

# ------------------------ GET YT URL FROM NAME ------------------------------------
def play_song(height):
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options

    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    search_query = height
    print(search_query)
    
    link = None
    while (link == None):
        driver.get('https://www.youtube.com/results?search_query={}'.format(search_query))
        select = driver.find_element(By.CSS_SELECTOR, 'div#contents ytd-item-section-renderer>div#contents a#thumbnail')
        link = select.get_attribute('href')
        print(link)

# ------------------------ YT player -----------------------------------------------

    url = link # CHANGE THIS IF YOU WOULD LIKE TO INPUT THE URL, e.g "https://www.youtube.com/watch?v=xm7TWFiZgTw&ab_channel=MCANJIM"
    video = pafy.new(url)
    best = video.getbestaudio()
    name = best.title
    playurl = best.url

    
    Media = Instance.media_new(playurl)
    Media.get_mrl()
    player.set_media(Media)
    player.video_set_scale(0.6)
    player.play()

    current_audio_time = player.get_time()

    return name

# ------------------------------ GUI ----------------------------------------------

layout = [[sg.Input('', enable_events=True, key='-INPUT-', font=('Arial Bold', 15), size=(16, 10))],
          [sg.Button('Submit', font=('Arial Bold', 10))],
          [sg.Text("MUSIC PLAYING: "), sg.Text(key='text3')],
          [sg.Button("Play"), sg.Button("Pause"), sg.Button("Restart"), sg.Button("Stop")], 
          [sg.Text(key='text'), sg.Text('|'), sg.Text(size=(15,1), key='text2')],
          [sg.ProgressBar(1000, orientation='h', size=(16, 10), border_width=0, key='-PROGRESS_BAR-')]
        ]

progress_bar=0
trigger = 0

# Create the window
window = sg.Window("Pedro YT Player", layout, margins=(5, 5), size=(200, 200))

# ----------------------------------------------------------------------------------

#MAIN LOOP
while True:
    pass
    event, values = window.read(timeout=1000)
    time_obj1=time.gmtime(int(player.get_time()/1000))
    window['text'].update(time.strftime("%M:%S",time_obj1))
    time_obj2=time.gmtime(int(player.get_length()/1000))
    window['text2'].update(time.strftime("%M:%S",time_obj2))
    if (trigger == 1):
        if (int(player.get_length()/1000) != 0):
            progress_bar = progress_bar+1000/int(player.get_length()/1000)
        window['-PROGRESS_BAR-'].update(progress_bar)
    # End program if user closes window or
    # presses the OK button
    if event == sg.WIN_CLOSED:
        break
    elif event == "Submit":
        trigger = 1
        print(values['-INPUT-'])
        height = values['-INPUT-']
        rame = play_song(height)
        window['text3'].update(rame)
        window['-INPUT-'].update([])
    elif event == "Play":
        trigger = 1
        player.play()
    elif event == "Pause":
        trigger = 0
        player.pause()
    elif event == "Restart":
        trigger = 1
        progress_bar = 0
        window['-PROGRESS_BAR-'].update(progress_bar)
        player.stop()
        player.play()
    elif event == "Stop":
        trigger = 0
        progress_bar = 0
        window['-PROGRESS_BAR-'].update(progress_bar)
        player.stop()

window.close()
