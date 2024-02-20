# Download YouTube videos for free using this Streamlit web application 👾 !

![Screenshot from 2024-02-21 01-58-58](https://github.com/bandhan-majumder/yt_video_downloader/assets/133476557/ecc7eb78-49a8-4b2a-ad45-6312607748d3)


# go to the site : https://ytvideodownloader-bm.streamlit.app/

## Table of Contents
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [Contributing](#contributing)

## Features
- Download YouTube videos for free.
- Automatically chooses the best resolution available.
- Simple and intuitive user interface.

## Setup
1. Clone the repository:
    ```bash
    git clone https://github.com/bandhan-majumder/yt_video_downloader.git
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Place your background image named `background.png` in the root directory of the project.

## Usage
1. Run the Streamlit app:
    ```bash
    streamlit run main.py
    ```

2. Access the Streamlit app in your web browser:
    ```
    http://localhost:8501
    ```

3. Enter the YouTube video URL in the provided text input.

4. Make sure you have given proper permissions. If not, then give the permissions to the /home/Downloads directory. Or adjust it according to your path.

   ```bash
    sudo chmod 777 /home/Downloads
    ```
   
5. Click the "Download" button to initiate the download process.

6. Wait for the download to complete. Upon completion, a success message will be displayed.

## Contributing
Contributions are welcome! Here's how you can contribute:
- Fork the repository.
- Create a new branch (`git checkout -b feature/new-feature`).
- Make your changes.
- Commit your changes (`git commit -am 'Add new feature'`).
- Push to the branch (`git push origin feature/new-feature`).
- Create a new pull request.

