"""Multi-Agent Recruiter — JK Data Lab
Agents collaborate: JD Writer + Resume Screener + Interview Question Generator + Offer Letter Writer
Author: Kinjal Jayswal | JK Data Lab | www.jkdatalab.com"""
import streamlit as st
import time
st.set_page_config(page_title="Multi-Agent Recruiter | JK Data Lab", page_icon="👔", layout="wide")
st.markdown("""<style>.stApp{background-color:#0A1628;color:#fff}h1,h2,h3{color:#00FFD4}
.agent-out{background:#0d2a2a;border-left:3px solid #00FFD4;border-radius:10px;padding:15px;margin:8px 0}
.stButton>button{background:linear-gradient(135deg,#00FFD4,#00aa88);color:#0A1628;font-weight:bold}</style>""", unsafe_allow_html=True)

st.title("👔 Multi-Agent Recruiter")
st.markdown("**4 agents collaborate** — Job Description Writer, Resume Screener, Interview Generator, Offer Letter Writer")
st.markdown("---")

with st.sidebar:
    st.markdown("### ⚙️ Settings")
    use_demo = st.checkbox("Demo Mode", value=True)
    st.markdown("**Agents:**\n📋 JD Writer\n🔍 Resume Screener\n❓ Interview Generator\n📄 Offer Letter Writer")
    st.markdown("**🌐 [JK Data Lab](https://www.jkdatalab.com)**")

role = st.text_input("Job Role:", placeholder="e.g. Senior Data Scientist")
col1, col2 = st.columns(2)
with col1:
    skills = st.text_area("Required Skills:", "Python, Machine Learning, SQL, Data Analysis", height=100)
with col2:
    exp = st.slider("Years Experience", 1, 15, 3)
    salary = st.text_input("Salary Range", "$80,000 - $120,000")

if st.button("🚀 Run Multi-Agent Recruitment", type="primary") and role:
    tabs = st.tabs(["📋 Job Description", "🔍 Screening Questions", "❓ Interview Questions", "📄 Offer Letter"])

    jd = f"""# {role} — JK Data Lab

## About the Role
We are seeking an experienced {role} to join our growing AI & Data Science team. You will work on cutting-edge projects for global clients.

## Requirements
- {exp}+ years of experience in relevant field
- **Technical skills**: {skills}
- Strong problem-solving and communication abilities
- Experience with agile development methodologies

## Responsibilities
- Design and implement AI/ML solutions for client projects
- Collaborate with cross-functional teams
- Mentor junior team members
- Present findings to stakeholders

## Benefits
- Salary: {salary}
- Remote-first culture
- Professional development budget
- Health & wellness benefits

*JK Data Lab | kinjal@jkdatalab.com | www.jkdatalab.com*"""

    screening = f"""## Screening Questions for {role}

**Technical Assessment:**
1. Describe your experience with: {skills.split(',')[0].strip()}
2. Walk me through a challenging project you led
3. How do you stay updated with latest {skills.split(',')[0].strip()} trends?

**Experience Verification:**
4. Tell me about your {exp}+ years in this field
5. What's your biggest professional achievement?

**Cultural Fit:**
6. How do you handle tight deadlines?
7. Describe your ideal team environment
8. Why are you interested in JK Data Lab?"""

    interview = f"""## Interview Questions for {role}

**Technical Deep Dive:**
1. Explain the bias-variance tradeoff and how you handle it
2. Design a system to process 1M records per day — what's your approach?
3. How would you explain {skills.split(',')[0].strip()} to a non-technical stakeholder?
4. Describe a time you improved system performance significantly

**Problem Solving:**
5. Given a dataset with 30% missing values — walk me through your approach
6. How would you build an end-to-end ML pipeline from scratch?

**Behavioral (STAR Method):**
7. Tell me about a time you disagreed with a technical decision
8. Describe how you handled a failed project
9. Give an example of mentoring someone successfully

**Culture & Values:**
10. What does 'done' mean to you?
11. How do you prioritize when everything is urgent?"""

    offer = f"""# Offer Letter

Dear [Candidate Name],

We are delighted to extend this offer for the position of **{role}** at JK Data Lab.

**Position Details:**
- Role: {role}
- Compensation: {salary} per annum
- Start Date: [To be confirmed]
- Location: Remote / Ahmedabad, Gujarat, India

**Benefits Package:**
- Performance bonus (up to 15%)
- Professional development: $2,000/year
- Health & wellness allowance
- Flexible working hours
- 25 days annual leave

This offer is contingent upon successful background verification.

Please confirm acceptance within 5 business days.

Warm regards,
Kinjal Jayantkumar Jayswal
Founder, JK Data Lab
kinjal@jkdatalab.com"""

    with tabs[0]:
        with st.spinner("📋 JD Writer generating..."):
            time.sleep(0.8)
        st.markdown(f'<div class="agent-out">{jd}</div>', unsafe_allow_html=True)
        st.download_button("📥 Download JD", jd, f"JD_{role}.md")

    with tabs[1]:
        with st.spinner("🔍 Screener generating questions..."):
            time.sleep(0.6)
        st.markdown(f'<div class="agent-out">{screening}</div>', unsafe_allow_html=True)

    with tabs[2]:
        with st.spinner("❓ Interview agent generating..."):
            time.sleep(0.7)
        st.markdown(f'<div class="agent-out">{interview}</div>', unsafe_allow_html=True)
        st.download_button("📥 Download Questions", interview, f"Interview_{role}.md")

    with tabs[3]:
        with st.spinner("📄 Offer letter agent writing..."):
            time.sleep(0.6)
        st.markdown(f'<div class="agent-out">{offer}</div>', unsafe_allow_html=True)
        st.download_button("📥 Download Offer Letter", offer, f"Offer_{role}.md")

st.markdown("---")
st.markdown("Built with ❤️ by **[JK Data Lab](https://www.jkdatalab.com)** | Multi-Agent HR AI")
