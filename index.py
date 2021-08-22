from pytube import YouTube
import os
import shutil
import click
import tkinter as tk

def complete(stream, filePath):
    routes = filePath.split('\\')
    fileName = routes[len(routes) - 1]
    #mover el archivo al directorio descargas
    shutil.move(fileName, f"Descargas/{fileName}")
    print(f"Descarga completa, su archivo se encuentra en la ruta {os.path.dirname(os.path.abspath(__file__))}\\Descargas")

def progress_bar(stream, chunck, remaining):
    with click.progressbar(chunck) as bar:
        for i in bar:
            pass 

def create_sub_folder():
    if(not os.path.isdir("Descargas")):
        os.makedirs("Descargas")

def download_fromYT(link):
    yt = YouTube(link, on_complete_callback=complete, on_progress_callback=progress_bar)
    print(f"Descargando: {yt.title}...")
    stream = yt.streams.filter(only_audio=True).first()
    stream.download()


## program
link = input("Ingrese url de youtube: ")
create_sub_folder()
download_fromYT(link)