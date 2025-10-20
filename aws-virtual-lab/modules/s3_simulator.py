import streamlit as st

def app():
    st.header("🪣 S3 Bucket Simulator")

    # Initialize session state
    if "s3_buckets" not in st.session_state:
        st.session_state.s3_buckets = {}

    # Input bucket name and file upload with unique keys
    bucket_name = st.text_input("Enter Bucket Name", key="s3_bucket_name")
    uploaded_file = st.file_uploader("Upload a file to simulate storage", key="s3_file_upload")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Create Bucket", key="s3_create_bucket"):
            if bucket_name:
                if bucket_name not in st.session_state.s3_buckets:
                    st.session_state.s3_buckets[bucket_name] = []
                    st.success(f"Bucket '{bucket_name}' created successfully (simulated).")
                else:
                    st.warning(f"Bucket '{bucket_name}' already exists.")
            else:
                st.error("Please enter a bucket name.")

    with col2:
        if st.button("Upload File", key="s3_upload_file"):
            if uploaded_file and bucket_name in st.session_state.s3_buckets:
                st.session_state.s3_buckets[bucket_name].append(uploaded_file.name)
                st.success(f"File '{uploaded_file.name}' uploaded to {bucket_name} (simulated).")
            else:
                st.error("Create a bucket first and select a file to upload.")

    # Display buckets and their files
    if st.session_state.s3_buckets:
        st.subheader("Your S3 Buckets")
        for b, files in st.session_state.s3_buckets.items():
            st.write(f"**{b}**: {files if files else 'No files uploaded yet.'}")
    else:
        st.info("No S3 buckets created yet.")
