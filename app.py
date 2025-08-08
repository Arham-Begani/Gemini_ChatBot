from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
genai.configure(api_key= os.getenv("keys"))
model = genai.GenerativeModel('gemini-1.5-flash')
