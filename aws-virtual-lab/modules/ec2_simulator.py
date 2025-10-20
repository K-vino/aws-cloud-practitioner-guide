import streamlit as st
import pandas as pd

def app():
    st.header("🖥️ EC2 Instance Simulator")

    # Initialize session state
    if "ec2_instances" not in st.session_state:
        st.session_state.ec2_instances = []

    # Instance selection with unique keys
    instance_type = st.selectbox(
        "Select Instance Type", 
        ["t2.micro", "t2.small", "t3.medium", "m5.large"],
        key="ec2_instance_type"
    )
    region = st.selectbox(
        "Select Region", 
        ["us-east-1", "ap-south-1", "eu-west-1"],
        key="ec2_region"
    )

    # Buttons for EC2 actions with unique keys
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Launch Instance", key="launch_instance"):
            instance = {
                "ID": f"i-{len(st.session_state.ec2_instances)+1:04d}",
                "Type": instance_type,
                "Region": region,
                "State": "Running"
            }
            st.session_state.ec2_instances.append(instance)
            st.success(f"✅ Simulated EC2 Instance launched — ID: {instance['ID']}")

    with col2:
        if st.button("Stop All Instances", key="stop_instances"):
            for i in st.session_state.ec2_instances:
                i["State"] = "Stopped"
            st.warning("🛑 All EC2 Instances Stopped (simulated).")

    with col3:
        if st.button("Terminate All Instances", key="terminate_instances"):
            st.session_state.ec2_instances = []
            st.error("❌ All EC2 Instances Terminated (simulated).")

    # Display instances
    if st.session_state.ec2_instances:
        st.subheader("Your EC2 Instances")
        df = pd.DataFrame(st.session_state.ec2_instances)
        st.table(df)
    else:
        st.info("No EC2 instances launched yet.")
