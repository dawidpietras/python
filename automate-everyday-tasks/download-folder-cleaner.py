import os
import shutil

file_ext = {'pdf': 'Dokumenty', 'doc': 'Dokumenty', 'ocx': 'Dokumenty', 'mp3': 'Muzyka',
            'jpg': 'Obrazy', 'png': 'Obrazy', 'exe': 'Pliki Instalacyjne', 'zip': 'Archiwa', 'mp4': 'Filmy',
            'avi': 'Filmy', 'ptx': 'Dokumenty', 'msi': 'Pliki Instalacyjne', 'iso': 'Pliki Instalacyjne',
            'odp': 'Dokumenty', 'txt': 'Dokumenty'}
download_path = r"C:\Users\Lenovo\Downloads"
file_names = os.listdir(download_path)


def check_directory(dir):
    folder_type_list = {file_ext[file] for file in file_ext}
    print(folder_type_list)
    for i in folder_type_list:
        existence_folder = os.path.join(dir, i)
        if not os.path.isdir(existence_folder):
            os.mkdir(existence_folder)


def sort_file():
    for file in file_names:
        for dict_key in file_ext:
            if file[-3:] == dict_key:
                src_folder = os.path.join(download_path, file)
                dest_folder = os.path.join(download_path, file_ext[dict_key], file)
                shutil.move(src_folder, dest_folder)
                break


check_directory(download_path)
sort_file()
