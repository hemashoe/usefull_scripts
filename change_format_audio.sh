for f in *.mkv; do ffmpeg -i "${f}"  "${f%.*}.mp4"  ; done
