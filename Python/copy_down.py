from __future__ import print_function
from bs4 import BeautifulSoup

import os
import sys
import urllib

version = "1.0"

def main_folder():
    if os.path.exists('GUROchan'):
        os.chdir("GUROchan")
    else:
        print("[GUROchan image downloader] Criando pasta 'GUROchan' ...")
        os.makedirs("GUROchan")

def board_thread_folder (board_name, folder_name):
    if os.path.exists(board_name):
        os.chdir(board_name)
    else:
        print("[GUROchan image downloader] Criando pasta'"+ board_name + "'...") 
        os.makedirs(board_name)
        os.chdir
    if os.path.exists(folder_name):
        os.chdir
    else:
        print("[GUROchan image downloader] Criando pasta '" + folder_name + "' ...")
        os.makedirs(folder_name)
        os.chdir(folder_name)


def get_page_info(url):
    global response

    print('\n [GUROchan image downloader] Rescuperando infomações de URL ...')

    response = urllib.urlopen(url).read().decode("utf-8")
    soup = BeautifulSoup(response, 'html.parser')

    get_title = soup.title.string.replace("Gurochan :: ", "")
    get_title_folder = get_title.replace(" ","_").replace("/", "-")

    get_board_value = soup.find('input', {'name' : "board"}, {'type' : 'hidden'}).get('value')

    if get_board_value == "g":
        get_board = "Guro"
    elif get_board_value == "f":
        get_board = "Freakshow"
    elif get_board_value == "s":
        get_board = "Scat"
    elif get_board_value == "fur":
        get_board = "Furry"
    elif get_board_value == "art":
        get_board = "Artwork"
    elif get_board_value == "3dcg":
        get_board = "3DCG"
    elif get_board_value == "p2p":
        get_board = "File-Sharing"
    elif get_board_value == "req":
        get_board = "Resquests"
    elif get_board_value == "rp":
        get_board = "Role-playing"
    elif get_board_value == "dis":
        get_board = "Discussion"
    elif get_board_value = "lit":
        get_board = "Literature"
    else:
        get_board = "Other"
    
    return [get_title_folder, get_title, get_board]

# Download das imagens
def download_images(img, currebt, total):
    download_link = "htt"

