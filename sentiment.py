import streamlit as st
import requests
from textblob import TextBlob

# Function to get GitHub project details
def get_github_project_details(username, repo_name):
    url = f"https://api.github.com/repos/{username}/{repo_name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

# Function to perform sentiment analysis
def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    if sentiment_score > 0:
        return "Positive"
    elif sentiment_score < 0:
        return "Negative"
    else:
        return "Neutral"

# Main function
def main():
    st.title("GitHub Project Sentiment Analysis")
    
    # Input fields
    username = st.text_input("Enter GitHub username:")
    repo_name = st.text_input("Enter GitHub repository name:")
    
    # Button to fetch project details
    if st.button("Fetch Project Details"):
        if username and repo_name:
            project_details = get_github_project_details(username, repo_name)
            if project_details:
                st.write("Project Details:")
                st.write("Name:", project_details['name'])
                st.write("Description:", project_details['description'])
                st.write("Language:", project_details['language'])
                st.write("Stars:", project_details['stargazers_count'])
                st.write("Forks:", project_details['forks'])
                
                # Sentiment analysis on project description
                description = project_details['description']
                sentiment = analyze_sentiment(description)
                st.write("Sentiment of Project Description:", sentiment)
            else:
                st.write("Invalid GitHub username/repository name.")
        else:
            st.write("Please enter both GitHub username and repository name.")

# Run the app
if _name_ == "_main_":
    main()