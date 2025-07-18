import streamlit as st
import cv2
import numpy as np
from cartoonify_webcam import cartoonify_frame

st.set_page_config(page_title="Cartoonify App", layout="centered")
st.title("🎨 Live Cartoonifier with Webcam")

# Sidebar Sliders
st.sidebar.header("🎛️ Adjust Cartoon Settings")
line_size = st.sidebar.slider("Edge Line Size", 1, 15, 7, step=2)
blur_value = st.sidebar.slider("Blur Value", 1, 15, 7, step=2)
k = st.sidebar.slider("Color Quantization (K-Means)", 2, 10, 5)

run = st.checkbox("Start Webcam")
take_snapshot = st.button("📸 Take Snapshot")

FRAME_WINDOW = st.image([])
snapshot_placeholder = st.empty()

# Webcam Setup
if "cap" not in st.session_state:
    st.session_state.cap = None

if run:
    if st.session_state.cap is None:
        st.session_state.cap = cv2.VideoCapture(0)
    cap = st.session_state.cap

    ret, frame = cap.read()
    if not ret:
        st.warning("Failed to grab frame from webcam")
    else:
        frame = cv2.flip(frame, 1)
        frame_resized = cv2.resize(frame, (480, 360))
        
        # Update cartoonify_frame to accept params
        from cartoonify_webcam import cartoonify_frame
        cartoon = cartoonify_frame(
            frame_resized,
            line_size=line_size,
            blur_value=blur_value,
            k=k
        )

        combined = np.hstack((frame_resized, cartoon))
        combined_rgb = cv2.cvtColor(combined, cv2.COLOR_BGR2RGB)
        FRAME_WINDOW.image(combined_rgb)

        if take_snapshot:
            snapshot_rgb = cv2.cvtColor(cartoon, cv2.COLOR_BGR2RGB)
            st.success("📸 Snapshot Taken! Right-click to save.")
            snapshot_placeholder.image(snapshot_rgb, caption="Your Cartoon Snapshot")
else:
    if st.session_state.cap:
        st.session_state.cap.release()
        st.session_state.cap = None
