import yt_dlp as youtube_dl
from youtubesearchpython import VideosSearch

def youtube_search(query,req_id):
    ydl_opts = {
    'outtmpl': f'./media/{req_id}/%(title)s.%(ext)s',
    "format": "bestaudio[ext=m4a]"
    }
    videosSearch = VideosSearch(query, limit = 1)
    results = videosSearch.result()
    videos = []
    for result in results['result']:
        video_id = result['id']
        video_title = result['title']
        video_thumb = result['thumbnails'][0]['url']
        videos.append({'id': video_id, 'title': video_title, 'thumb':video_thumb})
    song_url_endp=videos[0].get("id")
    try:
        link = f"https://www.youtube.com/watch?v={song_url_endp}"
        title = videos[0].get("title")
        thumb_song = videos[0].get("thumb")
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
             info_dict = ydl.extract_info(link, download=False)
             audio_file = ydl.prepare_filename(info_dict)
             ydl.process_info(info_dict)
             print(audio_file)
             
    except Exception as e:
        print(e)
        pass