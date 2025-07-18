# Cartoonify Webcam
This project applies a cartoon effect to your live webcam feed using OpenCV and displays it in real-time with Streamlit.

## Features

* Live webcam capture
* Real-time cartoon effect
* Adjustable sliders for:

  * Edge line thickness
  * Blur strength
  * Number of color clusters
* Option to take snapshots

## How It Works
The cartoon effect is created by combining:

* Edge detection using adaptive thresholding
* Color simplification using K-means clustering
* Image smoothing with bilateral filtering

### Clone the repository


git clone https://github.com/your-username/cartoonify_webcam.git
cd cartoonify_webcam


### Set up environment
conda create -n cartoonify_env python=3.11
conda activate cartoonify_env

### Install dependencies

pip install -r requirements.txt

### Run the app

streamlit run app.py

## Project Structure

cartoonify_webcam/
├── app.py
├── cartoonify_webcam.py
├── requirements.txt
├── README.md

## Requirements
* OpenCV
* NumPy
* Streamlit

