import streamlit as st
import base64

def main():
    # Set page configuration and title
    st.set_page_config(page_title="Data Decoder", page_icon=":chart_with_upwards_trend:", layout="wide")

    # Define CSS for background image
    hide_streamlit_style = """
    <style>
    #MainMenu, footer, header {
        visibility: hidden;
    }
    .stApp {
    background-image: linear-gradient(to right, #5E2750, #000000);/*Dark Purple to black */
    background-image: linear-gradient(to right, #6A040F, #000000);/*Dark Red to black */
    background-image: linear-gradient(to right, #333333, #000000);/*Dark Grey to black */
    background-image: linear-gradient(to right, #1E5631, #000000);/*Dark Green to black */
    background-image: linear-gradient(to right, #00416A, #000000);/*Dark blue to black */
    }
    .stMarkdown h1 {
    text-align: center;
    color:#ffffffba;
    font-family: "Poppins", sans-serif;
    font-family: "Kanit", sans-serif;
    font-weight: 700 !important;
    font-style: normal;
    font-size: 65px;
    text-shadow: 3px 3px 5px rgba(100,100, 100, 100);
    }
    h2 {
        color: #ffffffba; /* Set font color to white */
        font-size: 30px !important;
        text-align:center;
        margin-top:90px;
        text-shadow: 3px 3px 5px rgba(100,100, 100, 100);
        font-family: "Poppins", sans-serif;
    }
    .stMarkdown p {
        color:#FFFFFF; /* Set font color to white */
        font-size: 20px !important;
        font-family: "Poppins", sans-serif;
    }
    .stMarkdown p:first-child {
    text-align: center;
    color:#FFFFFF; /* Set font color to white */
    font-size: 15px !important;
    font-family: "Poppins", sans-serif;

}
    .st-emotion-cache-1dtefog{
    color:#FFFFFF;
    font-size:20px;
    }
    .welcome-text{
    color:#FFFFFF;
    }
    .welcomecontainer{
    position: absolute;
    left:-20px;
    top:-40px;
    }
    </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    st.markdown(
    """
    <style>
    h4 {
        color: #FFFFFF; /* Set font color to white */
        font-size: 20px !important;
        font-weight: 300 !important;
        background-color: #212121;
        border-radius: 15px;
        padding-left: 30px;
        padding-right: 30px;
        padding-top: 20px;
        padding-bottom: 20px;
        font-family: "Poppins", sans-serif;
        margin-bottom: 40px;
        margin-top: 40px;
        border: 2px solid #000000;
        opacity:0.7;
        width: 600px;
    }

    h5 {
        color: #FFFFFF; /* Set font color to white */
        font-size: 20px !important;
        font-weight: 300 !important;
        background-color: #212121;
        border-radius: 15px;
        padding-right: 30px;
        padding-left: 30px;
        padding-top: 20px;
        padding-bottom: 20px;
        margin-left: 27rem;
        font-family: "Poppins", sans-serif;
        border: 2px solid #000000;
        opacity:0.7;
        width: 600px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

    # Title
    st.markdown("<h1 data-fallback-text='DATA DECODER'>DATA DECODER</h1>", unsafe_allow_html=True)
     # Container for welcome message
    st.markdown("<div class='welcomecontainer'>", unsafe_allow_html=True)
    st.markdown("<div class='welcome-text'>", unsafe_allow_html=True)
    st.markdown("""
    Welcome to our Data Analytics Website!
    We're glad you're here! Explore and discover the world of data analytics.
    """)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<h4>The field of data analytics encompasses a wide range of techniques and methods for extracting meaningful patterns and insights from data.</h4>", unsafe_allow_html=True)
    st.markdown("<h5>Data visualization plays a crucial role in making complex datasets more understandable and accessible to a wider audience.</h5>", unsafe_allow_html=True)
    st.markdown("<h4>Data quality is paramount in data analytics, as inaccurate or incomplete data can lead to flawed analysis and decision-making.</h4>", unsafe_allow_html=True)
    st.markdown("<h5>The rise of big data has led to the need for scalable and distributed data analytics platforms capable of processing and analyzing massive datasets.", unsafe_allow_html=True)
    st.markdown("<h4>Data analytics is not just about analyzing historical data but also about predicting future trends and outcomes using advanced forecasting techniques.</h4>", unsafe_allow_html=True)
    st.markdown("<h5>Data ethics involves addressing ethical considerations and biases inherent in data collection, analysis, and interpretation.</h5>", unsafe_allow_html=True)

    st.header("Explore Data Analytics Possibilities with Us")
    # Information about websites
    with st.expander("1. Data Input and Processing"):
        st.markdown("""
        Users can upload Excel sheets containing any type of data, from sales figures to survey responses. Our website then processes this data, extracting relevant information and preparing it for visualization.
        """, unsafe_allow_html=True)

    with st.expander("2. Visualization Options"):
        st.markdown("""
        Users can choose from a variety of visualization options to represent their data. These may include:
        Bar charts
        Pie charts
        Line Chart
        Scatter plots
        Treemap
        Bar Chart with Secondary Y-Axis
        """, unsafe_allow_html=True)

    with st.expander("3. Interactive Exploration"):
        st.markdown("""
        The generated graphs are interactive, allowing users to explore different aspects of their data. They can zoom in, filter data points, hover over data points for more information, and more.
        """, unsafe_allow_html=True)

    with st.expander("4. Customization"):
        st.markdown("""
        Users have the option to customize their graphs by adjusting colors, labels, titles, and other parameters to suit their preferences and needs.
        """, unsafe_allow_html=True)

    with st.expander("5. Insights and Analysis"):
        st.markdown("""
         Users can derive insights and perform analysis on their data based on the visualizations generated. This may include identifying trends, patterns, correlations, outliers, and other insights that can inform decision-making.
        """, unsafe_allow_html=True)

    with st.expander("6. Facilitating Export and Sharing of Insights"):
        st.markdown("""
         Users can download the generated visualizations and data in various formats (e.g., PNG, PDF, CSV) for use in reports, presentations, or further analysis. Additionally, they can share their findings with others by generating shareable links or embedding visualizations in other web pages.
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
