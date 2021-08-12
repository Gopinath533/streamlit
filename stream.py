import streamlit as st
import pandas as pd
import time

##Display text
st.title("STREAMLIT")
st.text("Fixed width")
st.markdown("_markdown_")
st.latex(r"""e^{i\pi} + 1 = 0""")
st.write('Most objects')
st.write(['st', 'is<', 3, 4, 'gopinath'])
st.title('My title')
st.header('My header')
st.subheader('My sub')
st.code('for i in range(8): foo()')
data = [1, 2, 3, 4, 5, 6, 7]
df = pd.DataFrame(data)

##Display data
st.dataframe(df)
st.write(df)


st.table(df)
# st.json({'foo':'bar','fu':'ba'})

#Display CHarts
import numpy as np
chart_data = pd.DataFrame(
np.random.randn(20, 3),
columns=['a', 'b', 'c'])
st.line_chart(chart_data)
st.area_chart(chart_data)
st.bar_chart(chart_data)
#st.pyplot(flg)
st.altair_chart(chart_data).encode
st.vega_lite_chart(df, {
 'mark': {'type': 'square', 'tooltip': True},
 'encoding': {
     'x': {'field': 'a', 'type': 'quantitative'},
     'y': {'field': 'b', 'type': 'quantitative'},
     'size': {'field': 'c', 'type': 'quantitative'},
     'color': {'field': 'c', 'type': 'quantitative'},
 },
})


#st.plotly_chart(data)
#st.bokeh_chart(data)
#st.pydeck_chart(data)
#st.deck_gl_chart(data)
#st.graphviz_chart(data)
#st.map(data)

#Display interactive widges
st.button("Hit Me")
st.checkbox("Check me out")
st.radio("Radio",[1, 2, 3])
st.selectbox('select',[1, 2, 3])
st.multiselect('Multiselect',[1, 2, 3])
st.slider('Slide me', min_value = 0, max_value = 5)
st.select_slider('slide to select',options=[['red', 'orange'], ['yellow', 'green'], ['blue', 'indigo'], ['violet']])
st.text_input("enter a number")
st.text_area('Area for textual entry')
st.number_input('enter a number')
st.date_input('Data input')
#st.text_area('Area for textual entry')
st.date_input('date input')
st.time_input('tome entry')
st.file_uploader('File uploader')
st.color_picker('pick a color')


import time
# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(10):
# Update the progress bar with each iteration.
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)
st.spinner()
with st.spinner(text ='In progress'):
    time.sleep(2)
    st.success('done')
st.balloons()
st.error('Error message')
st.warning("warning message")
st.info("info message")
st.success("success message")

#placeholders,help and options
with st.empty():
    for seconds in range(5):
        st.write(f" {seconds} seconds have passed")
        time.sleep(1)
        st.write("X 1 minute over!")
placeholder = st.empty()
# Replace the placeholder with some text:
#placeholder.text("Hello")
# Replace the text with a chart:
placeholder.line_chart({"data": [1, 5, 2, 6]})
# Replace the chart with several elements:
#with placeholder.beta_container():
 #   st.write("This is one element")
  #  st.write("This is another")
# Clear all those elements:
#placeholder.empty()
