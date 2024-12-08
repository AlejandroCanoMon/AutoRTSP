import os
import subprocess
import datetime
import argparse

#output directory 
OUTPUT_DIR = "./grabaciones"
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

#stream recording
def grabar_stream(rtsp_url, duracion, output_dir):
   
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(output_dir, f"stream_{timestamp}.mp4")
    
    print(f"Grabando el stream desde {rtsp_url} durante {duracion} segundos...")
    print(f"Archivo de salida: {output_file}")

    #use of ffmpeg
    comando = [
        "ffmpeg",
        "-i", rtsp_url,          #url
        "-t", str(duracion),     #time
        "-c:v", "copy",         
        "-c:a", "copy",          
        output_file              
    ]

    try:
        subprocess.run(comando, check=True)
        print(f"Grabación completada: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error durante la grabación: {e}")

def main():
    #script arguments
    parser = argparse.ArgumentParser(description="Script para grabar stream RTSP")
    parser.add_argument(
        "-u", "--url", 
        required=True, 
        help="URL del stream RTSP"
    )
    parser.add_argument(
        "-t", "--time", 
        type=int, 
        required=True, 
        help="Duración de la grabación en segundos"
    )

    args = parser.parse_args()
    rtsp_url = args.url
    duracion = args.time

    grabar_stream(rtsp_url, duracion, OUTPUT_DIR)

if __name__ == "__main__":
    main()
