
import streamlit as st
import cv2
import numpy as np
import torch

def show():
    def detect_food(image):
        # Load YOLOv5 model from local directory
        model = torch.hub.load('yolov5', 'yolov5s', source='local')  # Update with your local path
        results = model(image)
        return results
    def visualize_detections(image, results):
        df = results.pandas().xyxy[0]  # Get detections as a DataFrame
        detected_items = []  # List to store detected food items
        for _, row in df.iterrows():
            if row['confidence'] > 0.5:  # Confidence threshold
                xmin, ymin, xmax, ymax = int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax'])
                label = row['name']
                confidence = row['confidence']
                detected_items.append((label, confidence))  # Store the label and confidence
                # Draw bounding box and label on the image
                cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (255, 0, 0), 2)
                cv2.putText(image, f'{label}: {confidence:.2f}', (xmin, ymin - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        return image, detected_items  # Return both the modified image and detected items
    st.title("Food Detection App")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        # Read and decode the image
        image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), 1)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB
        st.image(image_rgb, caption='Uploaded Image', use_column_width=True)
        # Detect food items
        results = detect_food(image)
        # Visualize detections and store detected food names
        result_image, detected_items = visualize_detections(image_rgb.copy(), results)
        # Create editable text input fields for detected food items
        if detected_items:
            st.image(result_image, caption='Detected Food Items', use_column_width=True)
            st.write("Edit detected ingredients:")
            for index, item in enumerate(detected_items):
                label, confidence = item
                edited_name = st.text_input(f"Ingredient {index+1} (Confidence: {confidence:.2f})", value=label)
                detected_items[index] = edited_name  # Store edited names
            st.write("Ingredients: " + ", ".join(detected_items))
            
        else:
            st.write("No food items detected.")
    if st.button("Get my recipe!"):
            st.session_state.page = "results"
