$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Speech
$taskRoot = $PSScriptRoot
$speaker = New-Object System.Speech.Synthesis.SpeechSynthesizer
$speaker.SelectVoice('Microsoft Zira Desktop')
$speaker.Rate = 0
$audioOutput = Join-Path $taskRoot 'docs/audio'
New-Item -ItemType Directory -Force -Path $audioOutput | Out-Null
$course = Get-Content -LiteralPath (Join-Path $taskRoot 'docs/data.json') -Raw -Encoding UTF8 | ConvertFrom-Json
$ffmpegPath = 'C:\Program Files\Jellyfin\Server\ffmpeg.exe'
foreach ($chapter in $course.lessons) {
    $wavePath = Join-Path $audioOutput ($chapter.id + '.wav')
    $mp3Path = Join-Path $audioOutput ($chapter.id + '.mp3')
    $scriptPath = Join-Path $taskRoot ('audio-scripts/' + $chapter.id + '.txt')
    $speaker.SetOutputToWaveFile($wavePath)
    $speaker.Speak([System.IO.File]::ReadAllText($scriptPath))
    $speaker.SetOutputToNull()
    & $ffmpegPath -hide_banner -loglevel error -y -i $wavePath -codec:a libmp3lame -b:a 64k -ac 1 -metadata ('title=' + $chapter.title) -metadata 'album=The Vibes Hockey Club' $mp3Path
    if ($LASTEXITCODE -ne 0) { throw 'Audio compression failed.' }
    Remove-Item -LiteralPath $wavePath
    Write-Output ('Completed audio: ' + $chapter.id)
}
$speaker.Dispose()
Write-Output 'All audio chapters generated.'
