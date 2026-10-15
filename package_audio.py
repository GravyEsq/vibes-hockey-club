import json,subprocess,zipfile
from pathlib import Path
root=Path(__file__).parent
data=json.loads((root/'docs/data.json').read_text(encoding='utf-8'))
meta={}
ffprobe=r'C:\Program Files\Jellyfin\Server\ffprobe.exe'
for l in data['lessons']:
    p=root/'docs/audio'/(l['id']+'.mp3')
    length=float(subprocess.check_output([ffprobe,'-v','error','-show_entries','format=duration','-of','default=noprint_wrappers=1:nokey=1',str(p)],text=True).strip())
    assert p.stat().st_size>10000 and length>30
    meta[l['id']]={'bytes':p.stat().st_size,'duration':length}
(root/'docs/audio-meta.json').write_text(json.dumps(meta),encoding='utf-8')
for pack in range(3):
    path=root/'docs/audio'/f'road-trip-{pack+1}.zip'
    with zipfile.ZipFile(path,'w',zipfile.ZIP_STORED) as z:
        for i,l in enumerate(data['lessons'][pack*6:(pack+1)*6],pack*6+1):
            z.write(root/'docs/audio'/(l['id']+'.mp3'),f'{i:02d}-{l["id"]}.mp3')
        z.writestr('READ-ME.txt','The Vibes Hockey Club\nOriginal hockey learning course. Synthetic narration. Edition 15 October 2026.\nExtract the MP3s and open in numerical order in your preferred audio player.\nCurrent-season game results are not read aloud. Historical outcomes are discussed.\n')
    assert path.stat().st_size<25*1024*1024
print(f'{len(meta)} MP3s, {sum(x["duration"] for x in meta.values())/60:.1f} minutes, {sum(x["bytes"] for x in meta.values())/1048576:.1f} MB; 3 ZIP packs validated.')
