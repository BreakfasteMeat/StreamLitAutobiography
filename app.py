import streamlit as st
import pandas as pd
import numpy as np
import time

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)



# --- PAGE CONFIG ---
st.set_page_config(
    page_title="My Portfolio | Streamlit Demo",
    page_icon="🎨",
    layout="wide",
)

# --- SIDEBAR ---
st.sidebar.title("🌟 Navigation")
page = st.sidebar.radio("Go to", ["Home", "About Me", "Projects"])

st.sidebar.divider()
st.sidebar.info("Built using Streamlit")

# --- HOME PAGE ---
if page == "Home":


    st.title("👋 Welcome to My Portfolio!")
    st.subheader("Hi, I’m **Seth**, a Computer Science student & developer.")
    st.markdown(
        """
        Welcome to my digital portfolio!  
        Here, you’ll find my **background**, **projects**, and **ways to contact me**.  
        I love creating applications using **Python**, **Java**, and **web technologies**.
        """
    )


    st.metric("Projects Completed", 4, "+1 this month")
    st.metric("Cups of Coffee", 288)

    st.success("Explore my projects using the sidebar!")

# --- ABOUT ME PAGE ---
elif page == "About Me":
    st.header("📘 About Me")

    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("images/me.jpg", caption="That’s me!")

    with col2:
        st.write(
            """
            **Name:** Seth Emia  
            **Course:** BS Computer Science  
            **Interests:** Software Development, Web Development, Game Programming 
            """
        )
        st.markdown(
            """
            ### 🧠 My Story  
            I’m passionate about creating things that combine logic and creativity.  
            I enjoy exploring full-stack development, mobile apps, and fun coding projects.  

            Outside tech, I love gaming and currently learning the piano 🎹.
            """
        )
    st.markdown(
        """
        ## Early Life and Education
        > I was born and raised in Cebu City. I studied elementary and middle school in **Little Angels Montessori School**. I then
        > was able to enter **Cebu City National Science High School** and studied Junior High School and Senior High School there.
        > I took STEM as my strand in SHS 
        > In high school, I enjoyed subjects like **Mathematics**, **Science**, and especially **Programming** in Grade 10.
        > This inspired me to pursue Computer Science for my college degree.
        > I am now currently taking Bachelor of Science in Computer Science in **Cebu Institute of Technology - University**.
        """)
    col1, col2, col3 = st.columns([1,1,1],gap="small")

    with col1:
        st.markdown("<h3 style='text-align: center;'>Little Angels Montessori School</h3>", unsafe_allow_html=True)
        _,mid,_ = st.columns([1,3,1])

        with mid:
            st.image("images/lams_logo.png")

    with col2:
        st.markdown("<h3 style='text-align: center;'>Cebu City National Science High School</h3>", unsafe_allow_html=True)
        _, mid, _ = st.columns([1, 3, 1])

        with mid:
            st.image("images/scihi_logo.png")

    with col3:
        st.markdown("<h3 style='text-align: center;'>Cebu Institute of Technology - University</h3>", unsafe_allow_html=True)
        _, mid, _ = st.columns([1, 3, 1])

        with mid:
            st.image("images/cit_logo.png")
    st.divider()
    st.subheader("📋 Current Information")

    data = {
        "Detail": ["Full Name", "Gender", "Current Address", "Birthdate"],
        "Information": [
            "Seth Nathaniel Galacio Emia",
            "Male",
            "Tisa, Cebu City, Cebu, Philippines",
            "March 05, 2005"
        ]
    }

    df = pd.DataFrame(data)
    st.table(df)
    tisa_coordinates = {
        'latitude':[10.303331005933412],
        'longitude':[123.87098718168049]
    }
    df = pd.DataFrame(tisa_coordinates)
    st.map(df)

    st.divider()

    st.header("Favorites")

    st.subheader("🎵 Music & Entertainment")
    st.markdown("Favorite Music")
    st.audio("audio/Rick Astley - Never Gonna Give You Up (Official Video) (4K Remaster).mp3")
    st.markdown("Favorite Band")
    st.image("images/band.png")

    st.subheader("🍔 Food & Drinks")
    st.markdown("Favorite cuisine: Filipino Cuisine")
    st.image("images/pinoy_cuisine.jpeg")
    st.markdown("Favorite dish: Ginataang Utan Bisaya")
    st.markdown("unfortunately i cannot find an appetizing picture online")

    st.divider()

    st.subheader("💡 Skills Overview")
    skills = {
        "Python": 45,
        "C#":20,
        "C++": 50,
        "Java": 75,
        "HTML/CSS/JS": 50,
        "Kotlin": 20,
        "ReactJS":10,
        "Django": 20,

    }

    for skill, percent in skills.items():
        st.write(f"**{skill}**")
        st.progress(percent / 100)

# --- PROJECTS PAGE ---
elif page == "Projects":
    st.header("🧩 My Projects")

    tab1, tab2, tab3, tab4= st.tabs(["🚀 2D Physics Engine (Ongoing)", "𖣯 Quad Trees", "🌳 Binary Trees"," 🌐 Graph Data Structure (Ongoing)"])

    with tab1:
        st.subheader("2D ️Java Physics Engine")
        st.write("A Physics engine made purely in Java with JavaFX GUI Framework")
        st.image("images/physics_pic.png")

        st.expander("View Details").write(
            """
            - Features: Accurate Physics, Spawn Circles and Boxes  
            - Tools: Java w/ JavaFX  
            """
        )

    with tab2:
        st.subheader("Quad Tree Visualized")
        st.write("Visualized Quad Tree. Used for efficient and fast collision detection for 2 Dimensional games")
        st.image("images/quad_tree.png")

    with tab3:
        st.subheader("Binary Tree Visualized")
        st.write("Visualized Binary Trees.")
        st.image("images/binary_trees.png")
        st.expander("View Details").write(
            """
            - Features: Toggleable AVL Self-Balancing Tree, Add and Remove nodes, Searching Algorithms, Show minimum and maximum values  
            - Tools: Java w/ Swing  
            """
        )

    with tab4:
        st.subheader("Graph Data Structure Visualized (Ongoing)")
        st.write("Visualized Graph Data Structure, with draggable nodes")
        st.image("images/graph.png")
        st.expander("View Details").write(
            """
            - Features: Add Draggable nodes, Connect Nodes, Perform DFS and BFS Search  
            - Tools: Java w/ JavaFX
            """
        )
# --- CONTACT PAGE ---
elif page == "Contact":
    st.header("📬 Get in Touch")
    st.write("I’d love to hear from you! Fill out the form below.")

    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit = st.form_submit_button("Send Message")

        if submit:
            if name and email and message:
                st.success(f"✅ Thanks {name}, your message has been sent!")
                with st.spinner("Processing..."):
                    time.sleep(2)
            else:
                st.error("⚠️ Please fill out all fields before submitting.")

    st.divider()
    st.info("📧 You can also reach me at: **seth.emia@example.com**")
    st.link_button("Visit my GitHub", "https://github.com/yourusername")

# --- FOOTER ---
st.divider()
st.caption("© 2025 Seth Emia | Created with Streamlit 🎈")
