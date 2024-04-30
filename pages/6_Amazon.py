# import streamlit as st
# import pandas as pd
# import datetime
# from PIL import Image
# import plotly.express as px
# import plotly.graph_objects as go

# # reading the data from the Excel file
# df = pd.read_excel("Amazon.xlsx")
# st.set_page_config(layout="wide")
# st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)
# image = Image.open('adidas-logo.jpg')

# col1, col2 = st.columns([0.1, 0.9])
# with col1:
#     st.image(image, width=100)

# html_title = """
#     <style>
#     .title-test {
#     font-weight:bold;
#     padding:5px;
#     border-radius:6px;
#     }
#     </style>
#     <center><h1 class="title-test">Amazon Interactive Sales Dashboard</h1></center>"""
# with col2:
#     st.markdown(html_title, unsafe_allow_html=True)

# col3, col4 = st.columns([0.3, 0.7])
# with col3:
#     box_date = str(datetime.datetime.now().strftime("%d %B %Y"))
#     st.write(f"Last updated by:  \n {box_date}")

# with col4:
#     fig = px.bar(df, x="ship-city", y="Amount", labels={"Amount": "Amount ($)"}, 
#                  title="Total Sales by City", hover_data=["Amount"],
#                  template="gridon", height=500)
#     st.plotly_chart(fig, use_container_width=True)

# _, view1, dwn1 = st.columns([0.15, 0.35, 0.5])
# with view1:
#     expander = st.expander("City-wise Sales")
#     data = df.groupby(by="ship-city")["Amount"].sum()
#     expander.write(data)
# with dwn1:
#     st.download_button("Get Data", data=data.to_csv().encode("utf-8"),
#                        file_name="CitySales.csv", mime="text/csv")

# result = df.groupby(by=pd.Grouper(key='Date', freq='M'))["Amount"].sum().reset_index()

# with view1:
#     expander = st.expander("Monthly Sales")
#     expander.write(result)
# with dwn1:
#     st.download_button("Get Data", data=result.to_csv().encode("utf-8"),
#                        file_name="MonthlySales.csv", mime="text/csv")

# st.divider()

# _, col5 = st.columns([0.1, 1])
# fig1 = px.line(result, x="Date", y="Amount", title="Total Sales Over Time",
#                template="gridon")
# with col5:
#     st.plotly_chart(fig1, use_container_width=True)

# st.divider()

# _, col6 = st.columns([0.1, 1])
# with col6:
#     st.subheader(":point_right: Sales Details")
#     st.write(df)

# _, _, dwn2 = st.columns([0.5, 0.45, 0.45])
# with dwn2:
#     st.download_button("Get Raw Data", data=df.to_csv().encode("utf-8"),
#                        file_name="SalesRawData.csv", mime="text/csv")
