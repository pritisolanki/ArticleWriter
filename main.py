import openai
import streamlit as st
import os

openai.api_key = os.getenv('openAikey')

def generate_article(keyword,writing_style,word):
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages = [
          {"role": "system", "content": "You are world renowned writer. You have been given a task to write an article based on a keyword in a specific writing style with a specific word count. You have to write an article based on the keyword: "+keyword+" in "+writing_style+" style with "+str(word)+" words."},
          {"role": "user", "content": "Generate an article based on the keyword: "+keyword+" in "+writing_style+" style with "+str(word)+" words. Add the title to the article. In footer,add appropriate hashtags."},
      ]
    )
    return response.choices[0].message['content'];

st.title("Article Generator")
keyword = st.text_input("Enter the keyword")
writing_style = st.selectbox("Enter the writing style",["Funny","Formal","Informal","Professional"])
word_count = st.slider("Word count",300,1000,300);
submit = st.button("Generate Article")

if submit:
    message = st.empty()
    message.text("Generating article....")
    article = generate_article(keyword,writing_style,word_count)
    message.text("")
    st.write(article)
    st.download_button(label= "Download Article", data=article, file_name="article.txt", mime="text/plain")
