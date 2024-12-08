# RTSP Stream Recorder

This Python script automates the recording of RTSP streams using FFmpeg. You can specify the stream URL and the recording duration as command-line parameters.

## Requirements

1. **Python 3**: Make sure you have Python 3 installed on your system.
2. **FFmpeg**: Install FFmpeg if you don’t already have it.
   - On Linux (Debian/Ubuntu):
     ```bash
     sudo apt update && sudo apt install ffmpeg
     ```
   - On Windows: Download the binary from [ffmpeg.org](https://ffmpeg.org/) and configure it in your system `PATH`.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/AlejandroCanoMon/AutoRTSP.git

2. Navigate to the project directory:
   ```bash
   cd AutoRTSP
3. Ensure `ffmpeg` is installed and accessible from your system's `PATH`.

## Usage

Run the script from the terminal, specifying the stream URL and the recording duration.
  ```bash
  python autoStream.py -u <RTSP_URL> -m <MODE(1 - STREAM, 2 - RECORD) -t <DURATION_IN_SECONDS>
  ```

## Example
  To stream from `rtsp://192.168.25.1:8080/stream`:
  ```bash
  python autoStream.py -u rtsp://192.168.25.1:8080/stream -m 1
  ```
  To record a stream from `rtsp://192.168.25.1:8080/stream` for 60 seconds:
  ```bash
  python autoStream.py -u rtsp://192.168.25.1:8080/stream -m 2 -t 60
  ```
  The recorded file will be saved in the `./grabaciones` directory with a unique name based on the current date and time.


## Parameters

    -u or --url: Specifies the RTSP stream URL.
    -t or --time: Duration of the recording in seconds.
    -m: mode: 1 - streaming, 2 - record

Example Output

      Recording stream from rtsp://192.168.25.1:8080/stream for 60 seconds...
      Output file: ./grabaciones/stream_20241207_143000.mp4
      Recording completed: ./grabaciones/stream_20241207_143000.mp4

Customization

You can modify the script to fit your needs:

    Change the output file format or codec.
    Enable continuous recording in defined intervals.
    Add an argument --output-dir to specify a custom output directory.

Contributions

If you have suggestions, find bugs, or want to contribute to the project, feel free to open an issue or submit a pull request.
License

This project is licensed under the MIT License. See the LICENSE file for details.
