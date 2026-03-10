import os
#from dotenv import load_dotenv
import streamlit as st

from langchain_openai import ChatOpenAI
#from langchain.schema import SystemMessage, HumanMessage
from langchain_core.messages import SystemMessage, HumanMessage

# .envファイルの読み込み（OPENAI_API_KEYを取得）
#load_dotenv()

# -------------------------------
# LLMに問い合わせる関数
# -------------------------------
def ask_llm(user_input, expert_type):
    """
    入力テキストと専門家タイプを受け取り
    LLMの回答を返す関数
    """

    # 専門家タイプに応じてシステムメッセージを変更
    if expert_type == "ITエンジニア":
        system_prompt = "あなたは優秀なITエンジニアです。技術的に正確で分かりやすい回答をしてください。"
    elif expert_type == "旅行アドバイザー":
        system_prompt = "あなたは経験豊富な旅行アドバイザーです。旅行初心者にも分かりやすく提案してください。"
    else:
        system_prompt = "あなたは親切なアシスタントです。"

    # LLMの初期化
    llm = ChatOpenAI(
        model_name="gpt-4o-mini",
        temperature=0
    )

    # メッセージ作成
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_input)
    ]

    # LLM実行
    result = llm(messages)

    return result.content


# -------------------------------
# Streamlit UI
# -------------------------------

st.title("LangChain LLM Webアプリ")

st.write("""
このアプリは **LangChain + OpenAI + Streamlit** を使用したサンプルアプリです。

### 使い方
1. 専門家の種類を選択してください  
2. 質問を入力してください  
3. 「送信」ボタンを押すとAIが回答します
""")

# 専門家選択（ラジオボタン）
expert = st.radio(
    "専門家の種類を選択してください",
    ("ITエンジニア", "旅行アドバイザー")
)

# テキスト入力
user_input = st.text_input("質問を入力してください")

# ボタン
if st.button("送信"):

    if user_input == "":
        st.warning("質問を入力してください")

    else:
        with st.spinner("AIが回答を生成しています..."):
            answer = ask_llm(user_input, expert)

        st.subheader("AIの回答")
        st.write(answer)