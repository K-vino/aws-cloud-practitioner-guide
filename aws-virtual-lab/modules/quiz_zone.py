import streamlit as st
import random
import time

# -------------------------------
# QUIZ DATA
# -------------------------------

QUIZ_QUESTIONS = [
    # Domain 1: Cloud Concepts
    {
        "domain": "Cloud Concepts",
        "question": "What is the main benefit of using the AWS Cloud?",
        "options": ["Lower latency", "Pay-as-you-go pricing", "Free hardware upgrades", "Unlimited storage forever"],
        "answer": "Pay-as-you-go pricing",
        "explanation": "AWS Cloud lets you pay only for what you use without upfront cost — a key cloud benefit."
    },
    {
        "domain": "Cloud Concepts",
        "question": "Which statement best describes elasticity in AWS?",
        "options": ["Ability to reduce costs automatically", "Ability to automatically scale resources up or down based on demand", "Ability to move data across regions", "Ability to store any amount of data"],
        "answer": "Ability to automatically scale resources up or down based on demand",
        "explanation": "Elasticity means the system automatically adjusts capacity as workload changes."
    },

    # Domain 2: Security & Compliance
    {
        "domain": "Security & Compliance",
        "question": "In the Shared Responsibility Model, which task is AWS responsible for?",
        "options": ["Patching guest OS", "Securing physical data centers", "Managing IAM permissions", "Configuring network ACLs"],
        "answer": "Securing physical data centers",
        "explanation": "AWS is responsible for 'security OF the cloud' including physical data centers and infrastructure."
    },
    {
        "domain": "Security & Compliance",
        "question": "Which AWS service helps you manage user access and permissions?",
        "options": ["AWS Shield", "AWS WAF", "AWS IAM", "AWS CloudTrail"],
        "answer": "AWS IAM",
        "explanation": "AWS Identity and Access Management (IAM) controls access to AWS resources securely."
    },

    # Domain 3: Technology
    {
        "domain": "Technology",
        "question": "Which AWS service is used to launch virtual servers?",
        "options": ["Amazon EC2", "Amazon S3", "AWS Lambda", "Amazon RDS"],
        "answer": "Amazon EC2",
        "explanation": "Amazon Elastic Compute Cloud (EC2) lets you create and manage virtual machines."
    },
    {
        "domain": "Technology",
        "question": "Which AWS service allows you to run code without provisioning servers?",
        "options": ["AWS Fargate", "AWS Lambda", "Amazon Lightsail", "Amazon EC2"],
        "answer": "AWS Lambda",
        "explanation": "AWS Lambda is a serverless compute service that runs code automatically when triggered."
    },

    # Domain 4: Billing & Pricing
    {
        "domain": "Billing & Pricing",
        "question": "Which AWS pricing model charges you only for what you use?",
        "options": ["Reserved Instances", "Pay-as-you-go", "Dedicated Hosts", "Subscription Model"],
        "answer": "Pay-as-you-go",
        "explanation": "In the pay-as-you-go model, you pay only for consumed resources without upfront commitments."
    },
    {
        "domain": "Billing & Pricing",
        "question": "Which tool helps you estimate AWS costs before deployment?",
        "options": ["AWS Pricing Calculator", "AWS Budgets", "Cost Explorer", "Billing Dashboard"],
        "answer": "AWS Pricing Calculator",
        "explanation": "The AWS Pricing Calculator lets you estimate the cost of services before launching them."
    },
]

# -------------------------------
# HELPER FUNCTIONS
# -------------------------------

def get_random_questions(num_questions=5):
    """Return a random subset of quiz questions"""
    return random.sample(QUIZ_QUESTIONS, num_questions)

def show_result(score, total):
    """Display quiz results"""
    st.success(f"🎯 You scored {score} out of {total}!")
    percentage = (score / total) * 100
    if percentage == 100:
        st.balloons()
        st.markdown("🏆 **Perfect Score! You're AWS Ready!**")
    elif percentage >= 80:
        st.markdown("✅ Excellent! You have strong AWS knowledge.")
    elif percentage >= 50:
        st.markdown("⚡ Good try! Keep practicing to master all domains.")
    else:
        st.markdown("🧠 Review AWS concepts and try again!")

# -------------------------------
# MAIN FUNCTION
# -------------------------------

def app():
    st.header("📚 AWS Cloud Practitioner Practice Quiz")
    st.write("Test your knowledge across all AWS domains — Cloud, Security, Tech, and Billing 💡")

    # Initialize session state
    if "quiz_started" not in st.session_state:
        st.session_state.quiz_started = False
        st.session_state.questions = []
        st.session_state.current_index = 0
        st.session_state.score = 0
        st.session_state.rerun_flag = False

    # Start Quiz
    if not st.session_state.quiz_started:
        num_q = st.slider("Number of Questions", 3, len(QUIZ_QUESTIONS), 5)
        if st.button("🚀 Start Quiz"):
            st.session_state.quiz_started = True
            st.session_state.questions = get_random_questions(num_q)
            st.session_state.current_index = 0
            st.session_state.score = 0
            st.session_state.rerun_flag = not st.session_state.rerun_flag

    # Quiz in progress
    else:
        total = len(st.session_state.questions)
        index = st.session_state.current_index
        question = st.session_state.questions[index]

        st.subheader(f"Q{index+1}/{total}: {question['question']}")
        st.caption(f"📘 Domain: {question['domain']}")
        choice = st.radio("Choose your answer:", question["options"], key=index)

        if st.button("Submit Answer"):
            if choice == question["answer"]:
                st.success("✅ Correct!")
                st.session_state.score += 1
            else:
                st.error(f"❌ Incorrect! Correct answer: **{question['answer']}**")
            st.info(f"💡 Explanation: {question['explanation']}")
            time.sleep(1.2)

            # Next question
            st.session_state.current_index += 1
            if st.session_state.current_index >= total:
                st.session_state.quiz_started = False
                show_result(st.session_state.score, total)
            else:
                st.session_state.rerun_flag = not st.session_state.rerun_flag

    # Restart button
    if st.button("🔁 Restart Quiz"):
        st.session_state.quiz_started = False
        st.session_state.questions = []
        st.session_state.current_index = 0
        st.session_state.score = 0
        st.session_state.rerun_flag = not st.session_state.rerun_flag
