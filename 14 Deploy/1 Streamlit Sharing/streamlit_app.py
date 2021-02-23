import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
from PIL import ImageFilter, ImageEnhance

image = Image.open("birds.jpg")

fig = plt.figure()

option = st.selectbox(
    "Select an Option",
    [
        "Show Image",
        "Rotate Image",
        "Create Thumbnail",
        "Crop Image",
        "Merge Images",
        "Flip Image",
        "Black & White",
        "Filters - Sharpen",
        "Filters - Edge Enhance",
        "Contrast Image",
    ],
)

if option == "Show Image":
    plt.imshow(image)
    plt.axis("off")
    st.pyplot(fig)
elif option == "Rotate Image":
    rotated_image = image.rotate(90)
    plt.imshow(rotated_image)
    plt.axis("off")
    st.pyplot(fig)
elif option == "Create Thumbnail":
    size = 300, 300
    image.thumbnail(size)
    image.save("thumb.png")
    plt.imshow(image)
    plt.axis("off")
    st.pyplot(fig)
elif option == "Crop Image":
    box = (50, 100, 200, 200)
    cropped_image = image.crop(box)
    plt.imshow(cropped_image)
    plt.axis("off")
    st.pyplot(fig)

elif option == "Merge Images":
    logo = Image.open("icon.png")
    position = (0, 300)
    image.paste(logo, position, logo)
    plt.imshow(image)
    plt.axis("off")
    st.pyplot(fig)
elif option == "Flip Image":
    flipped_image = image.transpose(Image.FLIP_TOP_BOTTOM)
    plt.imshow(flipped_image)
    plt.axis("off")
    st.pyplot(fig)
elif option == "Black & White":
    bw = image.convert("1")
    plt.imshow(bw)
    plt.axis("off")
    st.pyplot(fig)
elif option == "Filters - Sharpen":
    sharp = image.filter(ImageFilter.SHARPEN)
    plt.imshow(sharp)
    plt.axis("off")
    st.pyplot(fig)
elif option == "Filters - Edge Enhance":
    edge = image.filter(ImageFilter.EDGE_ENHANCE)
    plt.imshow(edge)
    plt.axis("off")
    st.pyplot(fig)
elif option == "Contrast Image":
    contrast = ImageEnhance.Contrast(image).enhance(2)
    plt.imshow(contrast)
    plt.axis("off")
    st.pyplot(fig)