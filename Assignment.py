pip install matplotlib
pip install streamlit
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def generate_normal_distribution(mean, std_dev, num_samples):
    return np.random.normal(mean, std_dev, num_samples)

def plot_histogram(data):
    plt.hist(data, bins=20, density=True, alpha=0.7, color='blue')
    plt.xlabel('Value')
    plt.ylabel('Probability')
    plt.title('Histogram of Normal Distribution')
    plt.grid(True)
    st.pyplot()

def save_to_csv(data):
    df = pd.DataFrame(data, columns=['Value'])
    csv_string = df.to_csv(index=False)
    return csv_string

def main():
    st.title("Normal Distribution Generator")

    mean = st.number_input("Enter mean value:", value=0.0)
    std_dev = st.number_input("Enter standard deviation:", value=1.0)
    num_samples = st.number_input("Enter number of samples:", value=100, step=1)

    generate_button = st.button("Generate Data")

    if generate_button:
        data = generate_normal_distribution(mean, std_dev, num_samples)
        plot_histogram(data)
        csv_string = save_to_csv(data)

        st.markdown("### Generated Data")
        st.dataframe(pd.DataFrame(data, columns=['Value']))

        st.markdown("### Histogram")
        plot_histogram(data)

        # Create a link to download the CSV file
        csv_download_link = create_download_link(csv_string, "generated_data.csv")
        st.markdown(csv_download_link, unsafe_allow_html=True)

def create_download_link(data, filename):
    csv = data.encode()
    b64 = base64.b64encode(csv).decode()
    return f'<a href="data:file/csv;base64,{b64}" download="{filename}">Download CSV</a>'

if __name__ == "__main__":
    main()
