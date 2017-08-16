import os, hashlib, sys
import requests
headers = {'User-Agent': 'SubDB/1.0 (get_my_subtitle/1.0; http://github.com/mohi7solanki/get-my-subtitle)'}

def get_hash(name):
        readsize = 64 * 1024
        with open(name, 'rb') as f:
            size = os.path.getsize(name)
            data = f.read(readsize)
            f.seek(-readsize, os.SEEK_END)
            data += f.read(readsize)
        return hashlib.md5(data).hexdigest()

def get_subtitle(file_path):
    url = "http://api.thesubdb.com/?action=download&hash=" + get_hash(file_path) + "&language=en"
    r = requests.get(url, headers = headers)
    if r.status_code == 200:
        with open(file_path[:file_path.rfind('.')]+'.srt','wb') as file:
            file.write(r.content)
        print('Subtitles for {} download successfully!'.format(file_path))
    else:
        print('Sorry! No Subtitle for this video.')


if __name__ == '__main__':
	get_subtitle(sys.argv[1])
