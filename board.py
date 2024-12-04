import streamlit as st
from PIL import Image, ImageFont, ImageDraw, ImageFilter

ARCHITECT = "Tcitrogg"
BIO_URL   = "https://bnierimi.vercel.app"

# Set the page title
st.set_page_config(page_title="Joint Christmas Carol | DPMaker", page_icon=Image.open("dpmaker.png"))



def image_side_text(ist_holder, image_url="dpmaker.png", image_width=44, markdown="<h1 style=\"margin-top: -0.5rem;\">DPMaker</h1>", columns=[4, 20]):
    ist_var = ist_holder.container()
    col1, col2 = ist_holder.columns(columns)
    with ist_var:
        with col1:
            st.image(image_url, width=image_width)
        with col2:
            st.markdown(markdown, unsafe_allow_html=True)

# Title

st.image("will-be-at-carol-banner.png", use_column_width=True)
st.title("✨ Joint Christmas Carol'24")

st.markdown("""
✨🤩 Tell a friend to bring a friend!!! :wink::sunglasses:
- Date: **8th December 2024**
- Time: **5PM**
- Venue: **University Of Ilorin, PS Auditorium**
""")

# side bar
sidebar = st.sidebar

with st.container(border=True):
    # Upload base image
    base_image = st.file_uploader("Upload Your Photo", type=["jpg", "jpeg", "png"])
    # Upload design image
    # design_image = st.file_uploader("Upload Design Image", type=["jpg", "jpeg", "png"])
    design_image = "design.png"

    user_name = st.text_input("Enter your name:", placeholder="Your Name")

if user_name:
    st.subheader(f"Welcome **{user_name}**!")

with st.container(border=True):

    def aspect_ratio(ar_width, original_width, original_height):
        ar_value = original_height / original_width
        ar_height = int(ar_width * ar_value)
        return (ar_width, ar_height)

    if base_image and design_image and user_name:
        # st.divider()
        # Open the images
        base_img = Image.open(base_image)
        # base_img.save(f"{base_image}.png", format="PNG")
        design_img = Image.open(design_image)
        # design_img.save(f"{design_image}.png", format="PNG")
        duplicated_base_image = base_img.resize(aspect_ratio(1000, base_img.width, base_img.height))

        crop_box = (0, 0, 2000, 2000)
        base_img = base_img.crop(crop_box)
        base_img = base_img.filter(ImageFilter.GaussianBlur(5))

        # Resize design if necessary
        # design_width = st.slider("Design Width", 10, base_img.width, design_img.width)
        # design_height = st.slider("Design Height", 10, base_img.height, design_img.height)
        design_width = design_img.width
        design_height = design_img.height
        design_img = design_img.resize((design_width, design_height))

        # Choose placement coordinates
        x_offset = st.slider("Horizontal Image Position", 0, 2000, 208)
        y_offset = st.slider("Vertical Image Position", -400, 2000, 307)

        # Create a copy of the base image to overlay on
        combined_image = base_img.copy()
        combined_image.paste(duplicated_base_image, (x_offset, y_offset))
        combined_image.paste(design_img, (0, 0), design_img)

        # Optional: Get position input for the text
        text_position_x = st.slider("Horizontal Text Position", -400, combined_image.width, 1384)
        # text_position_x = st.slider("Text X Position", -400, combined_image.width, int(combined_image.width / 2))
        text_position_y = st.slider("Vertical Text Position", -400, combined_image.height, 730)
        # text_position_y = st.slider("Text Y Position", -400, combined_image.height, int(combined_image.height / 2))
        
        # Optional: Font size
        font_size = st.slider("Font Size", 10, 200, 75)

        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except IOError:
            font = ImageFont.load_default(font_size)

        # Draw the text on the image
        draw = ImageDraw.Draw(combined_image)
        draw.text((text_position_x, text_position_y), user_name, fill="black", font=font)

        # combined_image = combined_image.resize((design_width, design_height))

        # Display the resulting image
        st.image(combined_image, caption="Combined Image", use_column_width=True)

        # Option to save the combined image
        save_button = st.button("Save Combined Image")
        if save_button:
            combined_image.save("combined_image.png")
            st.success("Image saved as combined_image.png")

st.markdown("#")

image_side_text(st, columns=[2.5, 37], markdown="<h1 style=\"margin-top: -1.3rem;\">DPMaker</h1>")
st.markdown("####")
image_side_text(st, image_url="tcitrogg-logo-purple.svg", image_width=25, markdown=f"Made by <br>[yours **{ARCHITECT}**]({BIO_URL})", columns=[2.5, 65])


# sidebar.write("""""" )
# sidebar.write("""""" )
# sidebar.write("""""" )
# sidebar.write("""""" )
# sidebar.write("""""" )
# sidebar.write("""""" )
# sidebar.write("""""" )
# sidebar.write("""""" )
# sidebar.write("""""" )
# sidebar.write("""""" )
# sidebar.write("""""" )
# sidebar.write("""""" )
# sidebar.write("""""" )
# sidebar.write("""""" )
# sidebar.write("""""" )
# sidebar.write("""""" )
# sidebar.write("""""" )
# sidebar.write("""""" )
# sidebar.divider()

# image_side_text(sidebar, image_url="tcitrogg-logo-purple.svg", image_width=25, markdown=f"[Made by **{ARCHITECT}**]({BIO_URL})", columns=[2.5, 25])