
import streamlit as st
from time import sleep
from streamlit_lottie import st_lottie
import re
import requests

st.set_page_config("Visualizer", ":sunglasses:",layout="wide")

with st.container():
    st.header('Hello World!')
    st.title('Algorithm Visualizer By Unisimplex')
    st.write('This simple Website Will let you visualize algorithms. Happy coding !!! ')

def lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def bubble_sort():
    for i in range(0,arsize-1):
        for j in range(0,arsize-i-1):
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
                print("swapped")
                sort_chart.bar_chart(a ,x=axis, use_container_width=True)
                sleep(wait)

def Selection_Sort():
    for i in range((len(a))-1):
        min_i = i
        for j in range(i,len(a)):
            if a[min_i] > a[j]:
                min_i = j

        temp = a[min_i]
        a[min_i] = a[i]
        a[i]=temp
        print("swapped")
        sort_chart.bar_chart(a,x=axis ,use_container_width=True)
        sleep(wait)

def x_axis(x):
    for i in range(len(x)):
        x_axis = x_axis + str(x[i])
        return x_axis

ani = lottie("https://assets3.lottiefiles.com/packages/lf20_vnikrcia.json")

####### Input of array lambda function
num = lambda x : [int(i) for i in re.split("[^0-9]", x) if i != ""]

#####unsorted array
us_list = []



with st.container():
    st.write("---")
    left_column, right_column = st.columns((1,2))
    with left_column:
                
        ######## algorithm selection

        selected = st.selectbox('Please select Algorithm', ['Bubble Sort', 'Selection Sort', 'More to come', '..........'])
        arsize = st.slider("Select the size of array",0,50,0)
        wait = st.slider("Select the time to wait before swapping",0,10,0)
        axis = x_axis(us_list)
        ele = st.text_input("Enter the Array ")
        with st.container():
            st_lottie(ani, height=300, key="coding")

    with right_column:
        if len(num(ele)) != arsize:
            st.write("Array Size mismatched ")
        else:
            a = num(ele)
            us_list = num(ele)
        st.subheader("Unsorted Array")
        unsort_chart = st.empty()
        st.header("Sorted Array")
        sort_chart = st.empty()

        if st.button('Start'):
            if selected == 'Bubble Sort':
                    unsort_chart.bar_chart(us_list)
                    bubble_sort()
            elif selected == 'Selection Sort':
                unsort_chart.bar_chart(us_list)
                Selection_Sort()
        else:
            pass
    


st.write("[Instagram](https://www.instagram.com/unisimplex/)")
