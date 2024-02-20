from pytube import YouTube
import streamlit as st
import base64
import re


# to set a colour as a background
# def MyBG_colour(wch_colour):
#     my_colour = f"<style> .stApp {{background-color: {wch_colour};}} </style>"
#     st.markdown(my_colour, unsafe_allow_html=True)
#
# MyBG_colour("#418253")  # or pass in the hex code: Eg. MyBG_colour("#90CAF9")


# setting background image.........
# step 1: set the image
@st.cache_data  # Streamlit decorator used to cache the output of a function based on its inputs
def get_img(file):
    with open(file, "rb") as f:  # rb : binary read mode
        data = f.read()
    return base64.b64encode(data).decode()


local_image_path = "background.png"  # Make sure the image is in the same folder
img = get_img(local_image_path)

# step 2: Define the CSS style with the background image
page_bg_img = f"""
<style>
    .stApp {{
        background-image: url("data:image/png;base64,{img}");
        background-size: cover;
    }}
</style>
"""

# step 3: Display the background image using Markdown
st.markdown(page_bg_img, unsafe_allow_html=True)

# function for bordered text
def bordered_text(label_text):
    # Define CSS style for the border
    border_style = """
        border: 1px solid white;
        border-radius: 30px;
        padding: 40px;
    """
    # Apply the border style to the text using HTML
    html_text = f'<div style="{border_style}"><h2 style="font-weight:bold">{label_text}</h2></div>'
    # Render the HTML
    st.markdown(html_text, unsafe_allow_html=True)


bordered_text("Download YouTube videos for free  ▶️ ️🎉")
st.divider()  # making a horizontal divider


# function regex pattern for youtube videos url recognitions
def is_youtube_url(url):  # returns true if the url matches the pattern . else return false
    # Regular expression to match YouTube URLs
    youtube_pattern = re.compile(
        r'(?:https?://)?(?:www\.)?(?:youtube\.com(?:/[^/]+/.+/.+|/.+/)|youtu\.be/)([a-zA-Z0-9_-]{11})')
    return bool(re.match(youtube_pattern, url))


# Get the YouTube video URL input with a placeholder
url = st.text_input(" ", placeholder="Enter the YouTube video URL")
isValidURL = is_youtube_url(url)


# Custom styling for the button
custom_css = """
    <style>
    .stButton>button {
        background-color: #4CAF50; /* Green background */
        color: white; /* White text */
        padding: 15px 30px; /* Padding */
        text-align: center; /* Text alignment */
        text-decoration: none; /* Text decoration */
        display: inline-block; /* Display as inline-block */
        font-size: 18px; /* Font size */
        margin: 10px 0px; /* Margin */
        transition-duration: 0.4s; /* Transition duration */
        cursor: pointer; /* Cursor pointer */
        border-radius: 30px; /* Border radius */
        border: none; /* No border */
        box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2); /* Box shadow */
    }

    .stButton>button:hover {
        background-color: #45a049; /* Darker green background on hover */
        transform: scale(1.05); /* Scale the button slightly on hover */
        color: white; /* Ensure text color remains white on hover */
    }

    .stButton>button:active {
        color: white; /* Ensure text color remains white on click */
    }
    </style>
"""

# Inject custom CSS for the button
st.markdown(custom_css, unsafe_allow_html=True)

# button click or not
click = st.button("Download")  # if the user clicks, it becomes true .. else remains false

if click:
    if url == "" or isValidURL == False: # checks if there is no url or the url doesn't match the pattern of youtube url
        st.error("Invalid or Empty URL")
    else:
        # creating a YouTube object
        yt = YouTube(url)

        # stream = available versions, progressive = video can be played while downloading, order_by resolution =
        # ordering from low to high resolution, desc = making the order descending, first = choosing the first one
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

        # Create an empty container for the download message
        download_message = st.empty()

        # # Download the chosen stream
        # stream.download()  # by default the downloads will be saved in the current folder

        # Specify the folder where you want to save the video
        folder_path = '/home/bandhan/Downloads'

        try : 
           # Download the video to the specified folder
           stream.download(output_path=folder_path)
            
        except:
            # Downloading in the default folder 
            stream.download()
            
        # show this message after successfully downloading
           st.success("Video downloaded successfully!")
            
# Set up a container to hold the text at the bottom
st.markdown(
    """
    <div style="position: fixed; bottom: 70px; left: 50%; transform: translateX(-50%); text-align: center;">
        <p>© 2024 created by Bandhan. All rights reserved.</p>
    </div>
    """,
    unsafe_allow_html=True
)
