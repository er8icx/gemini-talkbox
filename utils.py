import google.generativeai as genai
import os
import markdown2
genai.configure(api_key="your-api-key")
def call_gemini(prompt):
    model =genai.GenerativeModel("gemini-1.5-flash")
    response=model.generate_content(prompt)
    html_output=markdown2.markdown(response.text)
    return html_output