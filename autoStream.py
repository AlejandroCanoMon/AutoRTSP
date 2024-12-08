import os
import subprocess
import datetime
import argparse

#create output directory
OUTPUT_DIR = "./grabaciones"
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

#stream record
def grabar_stream(rtsp_url, duracion, output_dir):

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(output_dir, f"stream_{timestamp}.mp4")
    
    print(f"Grabando el stream desde {rtsp_url} durante {duracion} segundos...")
    print(f"Archivo de salida: {output_file}")

    #use of FFMPEG
    comando = [
        "ffmpeg",
        "-i", rtsp_url,          #url
        "-t", str(duracion),     #time in sec
        "-c:v", "copy",          
        "-c:a", "copy",          
        output_file              
    ]

    try:
        subprocess.run(comando, check=True)
        print(f"Grabación completada: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error durante la grabación: {e}")

#stream visualizer
def visualizar_stream(rtsp_url):
    print(f"Abriendo el stream desde {rtsp_url} en tiempo real...")

    comando = [
        "ffplay",
        "-i", rtsp_url,   
        "-loglevel", "quiet"  
    ]

    try:
        subprocess.run(comando, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error al abrir el streaming: {e}")

def main():
    #script arguments
    parser = argparse.ArgumentParser(description="Script para visualizar o grabar stream RTSP")
    parser.add_argument(
        "-u", "--url", 
        required=True, 
        help="URL del stream RTSP"
    )
    parser.add_argument(
        "-t", "--time", 
        type=int, 
        help="Duración de la grabación en segundos (solo para grabar)"
    )
    parser.add_argument(
        "-m", "--mode", 
        required=True, 
        type=int,
        choices=[1, 2], 
        help="Modo de uso: 1 para ver el stream, 2 para grabar el stream"
    )

    args = parser.parse_args()
    rtsp_url = args.url
    mode = args.mode


    if mode == 1:
        visualizar_stream(rtsp_url)
    elif mode == 2:
        if args.time is None:
            print("Debes especificar la duración con -t o --time para grabar el stream.")
        else:
            grabar_stream(rtsp_url, args.time, OUTPUT_DIR)

if __name__ == "__main__":
    main()
