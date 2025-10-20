import streamlit as st
from streamlit_option_menu import option_menu
from modules import quiz_zone  # updated quiz_zone.py

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="AWS Virtual Lab Simulator",
    layout="wide",
    page_icon="☁️"
)

st.title("☁️ AWS Virtual Lab Simulator")
st.caption("Practice AWS Services Virtually — No Real Charges, Just Learning!")

# -------------------------------
# Sidebar Navigation
# -------------------------------
with st.sidebar:
    selected = option_menu(
        "AWS Virtual Console",
        ["🏠 Home", "🖥️ EC2 Simulator", "🪣 S3 Simulator", "🧰 IAM Simulator", "💰 Cost Estimator", "📚 Quiz Zone"],
        icons=["house", "cpu", "cloud-upload", "shield", "wallet2", "book"],
        menu_icon="cast",
        default_index=0
    )

# -------------------------------
# Pages
# -------------------------------

# 1️⃣ Home Page
if selected == "🏠 Home":
    st.header("Welcome to Your Virtual AWS Environment 🌍")
    st.write("""
        This is a **virtual AWS learning platform**.
        - Practice AWS concepts safely.
        - Experience the feel of AWS Console.
        - Learn by doing — no AWS account required!
    """)
    st.image("https://d1.awsstatic.com/product-marketing/AWS%20Certification/Certification%20Badges/AWS-Cloud-Practitioner_badge.14f857b2b278a5c3efed1c74a879a7e8b2db9ef2.png", width=250)

# 2️⃣ EC2 Simulator
elif selected == "🖥️ EC2 Simulator":
    from modules import ec2_simulator
    ec2_simulator.app()
    st.header("🖥️ EC2 Instance Simulator")
    import pandas as pd

    if "ec2_instances" not in st.session_state:
        st.session_state.ec2_instances = []

    instance_type = st.selectbox("Select Instance Type", ["t2.micro", "t2.small", "t3.medium", "m5.large"])
    region = st.selectbox("Select Region", ["us-east-1", "ap-south-1", "eu-west-1"])

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Launch Instance"):
            instance = {
                "ID": f"i-{len(st.session_state.ec2_instances)+1:04d}",
                "Type": instance_type,
                "Region": region,
                "State": "Running"
            }
            st.session_state.ec2_instances.append(instance)
            st.success(f"✅ Simulated EC2 Instance launched — ID: {instance['ID']}")
    with col2:
        if st.button("Stop All Instances"):
            for i in st.session_state.ec2_instances:
                i["State"] = "Stopped"
            st.warning("🛑 All EC2 Instances Stopped (simulated).")
    with col3:
        if st.button("Terminate All Instances"):
            st.session_state.ec2_instances = []
            st.error("❌ All EC2 Instances Terminated (simulated).")

    # Display instances
    if st.session_state.ec2_instances:
        st.subheader("Your EC2 Instances")
        df = pd.DataFrame(st.session_state.ec2_instances)
        st.table(df)
    else:
        st.info("No EC2 instances launched yet.")

# 3️⃣ S3 Simulator
elif selected == "🪣 S3 Simulator":
    from modules import s3_simulator
    s3_simulator.app()
    st.header("🪣 S3 Bucket Simulator")
    if "s3_buckets" not in st.session_state:
        st.session_state.s3_buckets = {}

    bucket_name = st.text_input("Enter Bucket Name")
    uploaded_file = st.file_uploader("Upload a file to simulate storage")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Create Bucket"):
            if bucket_name:
                st.session_state.s3_buckets[bucket_name] = []
                st.success(f"Bucket '{bucket_name}' created successfully (simulated).")
            else:
                st.error("Please enter a bucket name.")

    with col2:
        if st.button("Upload File"):
            if uploaded_file and bucket_name in st.session_state.s3_buckets:
                st.session_state.s3_buckets[bucket_name].append(uploaded_file.name)
                st.success(f"File '{uploaded_file.name}' uploaded to {bucket_name} (simulated).")
            else:
                st.error("Create bucket first and select a file to upload.")

    if st.session_state.s3_buckets:
        st.subheader("Your S3 Buckets")
        for b, files in st.session_state.s3_buckets.items():
            st.write(f"**{b}**: {files if files else 'No files uploaded yet.'}")

# 4️⃣ IAM Simulator
elif selected == "🧰 IAM Simulator":
    st.header("🧰 IAM Role Simulator")
    if "iam_users" not in st.session_state:
        st.session_state.iam_users = []

    user_name = st.text_input("Enter IAM Username")
    role = st.selectbox("Select Role", ["Admin", "Developer", "Viewer"])

    if st.button("Create User"):
        if user_name:
            st.session_state.iam_users.append({"Username": user_name, "Role": role})
            st.success(f"IAM User '{user_name}' with '{role}' role created (simulated).")
        else:
            st.error("Enter a username.")

    if st.session_state.iam_users:
        st.subheader("IAM Users")
        import pandas as pd
        df = pd.DataFrame(st.session_state.iam_users)
        st.table(df)
    else:
        st.info("No IAM users created yet.")

# 5️⃣ Cost Estimator
elif selected == "💰 Cost Estimator":
    st.header("💰 AWS Cost Estimator (Simulated)")
    compute_cost = st.slider("Compute Cost (per month)", 0, 1000, 100)
    storage_cost = st.slider("Storage Cost (per month)", 0, 500, 50)
    total = compute_cost + storage_cost
    st.metric(label="Estimated Monthly Cost", value=f"${total}")

# 6️⃣ Quiz Zone
elif selected == "📚 Quiz Zone":
    # Call the updated quiz_zone app()
    quiz_zone.app()
