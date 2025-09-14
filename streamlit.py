import streamlit as st

#Basic UI elements

def basic_ui_element():
    st.title("Basic UI Elements")
    st.header("Header")
    st.subheader("Sub Header")
    st.text("This is a Text Element")
    st.write("We can write content")
    st.markdown("markdown content")
    st.code("print('Hello world'), language='python'")
    st.latex(r'''a^2 + b^2 =c^2''')
    st.caption("This is a captionn element")
    st.error("This is a Error message")
    st.warning("Warning message")
    st.info("Information message")
    input= st.text_input("Enter your text input")

    if input:
        st.write(f"your text: {input}")

    number_input=st.number_input("Select your number")

    if number_input:
        st.write(f"Your number:{number_input}")
    
    st.date_input("This is a Date Calendar")
    st.time_input("Time input")

   

    if st.checkbox("checkbox element"):
        st.write("Checkbox is selected")   

    if st.button("Click me"):
        st.success("Button clicked")     

    st.radio("This is a radio button",("option1","option2","option3"))
    st.selectbox("Select box",("option1","option2","option3"))
    st.slider("select your option", 0, 100, 10)

#Display data
import pandas as pd
import numpy as np

def data_display():
    st.title("Data Display")
    df = pd.DataFrame(
        {
            'Column1': [1,2,3,4],
            'Column2': [6,5,7,8]
        }
    )
    st.write("DataFrame")
    st.dataframe(df)

    st.write("Table")
    st.table(df)
    st.write("JSON data ")
    st.json(
        {'name': 'Chandra',
        'stuff': [
            'stuff1',
            'stuff2',
            'stuff3'
        ]
        })


#Charts and Visualizations
import plotly.express as px

def charts_visuals():
    st.title("Charts and Visualizations")

    df=pd.DataFrame({
        'x': np.random.randn(100),
        'y': np.random.randn(100)
                    })

    st.line_chart(df)
    st.bar_chart(df)
    st.area_chart(df)
    fig = px.scatter(df, x='x', y='y', title="Scatter Plot")
    st.plotly_chart(fig)



#Layouts and Containers
def layout_containers():
    st.title("Layouts and Containers")
    st.sidebar.title("Sidebar Title")
    st.sidebar.write("Sidebar content")
    col1, col2 = st.columns(2)
    with col1:
        st.write("Column1 content")
    
    with col2:
        st.write("Column2 content")

    with st.expander("Expand to see more"):
        st.write("content within expander")

    tab1,tab2 = st.tabs(["Tab1","Tab2"])  
    with tab1:
        st.write("This is a Tab1 content")

    with tab2:
        st.write("This is a Tab2 content")

#Sessions
def state_management():
    st.title("State Management")
    if 'counter' not in st.session_state:
        st.session_state.counter=0
    def increment_counter():
        st.session_state.counter +=1

    st.button("Increment Counter", on_click=increment_counter)
    st.write("Counter:",st.session_state.counter)        
    with st.form("my_form"):
        st.text_input("Please enter text input")
        st.text_input("Enter your age")

        #To disable a form submit button in Streamlit when a text input is empty, you can dynamically control the disabled state of the button using st.session_state
       
       
        submit_button = st.form_submit_button("Submit")
        if submit_button:
            st.success("Form submitted successfully")


def file_handle():
    upload_file = st.file_uploader("Upload file", type=["csv","xlsx"])
    if upload_file is not None:
        if upload_file.name.endswith('csv'):
            df= pd.read_csv(upload_file)
            st.write("Data Frame from csv")
            st.dataframe(df)
        elif upload_file.name.endswith('xlsx'):
            df=pd.read_excel(upload_file)  
            st.write("Data Frame from xlsx file")
            st.dataframe(df)  


import time

#Progress and status
def progress_status():
    st.title("Progress and status")
    progress_bar= st.progress(0)

    for i in range(100):
            time.sleep(0.1)
            progress_bar.progress(i+1)
    st.success("Progress completed")

    with st.spinner("Loading..."):
        time.sleep(2)
        st.success("Spinner completed")    

    st.subheader("Status messages")
    st.error("Error message")
    st.warning("Warning message")
    st.info("Info message")
    st.success("Success message")


#CSS markdown
def advance():
    st.subheader("Custom Css styling")
    st.markdown("""
                <style>
                .big-font{
                            font-size: 20px !important;
                            font-weight: bold;
                            color: blue;
                }
                </style>
                """, unsafe_allow_html=True
                )
    st.markdown('<p class="big-font"> text from a custom css class</p>', 
                unsafe_allow_html=True
                )


def main():
    st.set_page_config(page_title="Streamlit Tutorial" ,
                       page_icon="🧊",                 # Can be emoji or URL to .ico/.png
                       layout="wide",           # 'centered' (default) or 'wide'
                         initial_sidebar_state="expanded",
                        menu_items={
                        'Get Help': 'https://docs.streamlit.io/',
                         'Report a bug': "https://github.com/chandrasai-Durgapu/streamlit-app/issues",
                         'About': "# My App\nThis is a demo Streamlit app."
                                 }
                        )

    st.sidebar.title("🧊 Streamlit Tutorial")
    page= st.sidebar.selectbox("Choose a section",
                               ["Basic UI", 
                                "Data Display", 
                                "Charts", 
                                "Layouts", 
                                "State", 
                                "Files", 
                                "Progress", 
                                "Advanced"]
                            )
    if page=="Basic UI":
        basic_ui_element()
    elif page=="Data Display":
        data_display()
    elif page=="Charts":
        charts_visuals()
    elif page=="Layouts":
        layout_containers()
    elif page=="State":
        state_management()
    elif page=="Files":
        file_handle()
    elif page=="Progress":
        progress_status()
    elif page=="Advanced":
        advance()


if __name__=="__main__":
    main()