import streamlit as st
import pandas as pd

def process_files(uploaded_file):
    if uploaded_file:
        df = pd.read_excel(uploaded_file, nrows=30)

        st.dataframe(df, height=300)  # Display the data as a DataFrame with a fixed height

        col1, col2 = st.columns(2)

        if col1.button("Remove Duplicates"):
            # Check for duplicates in the first column by default and remove them
            df_no_duplicates = df.drop_duplicates(df.columns[0])
            col1.dataframe(df_no_duplicates, height=300)  # Display the data without duplicate rows

        if col2.button("Submit anyway"):
            # Add your code for "Submit anyway" action here
            pass

def main():
    st.title("First Project")

    uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx", "xls"])

    if uploaded_file is not None:
        file_extension = uploaded_file.name.split('.')[-1]

        if file_extension in ('xlsx', 'xls'):
            st.text("Excel file uploaded. You can process it here.")

            

            process_files(uploaded_file)

        else:
            st.text("Unsupported file type. Please upload an Excel file (XLSX or XLS).")

if __name__ == "__main__":
    main()
