from openai import OpenAI
from vllm import LLM, SampleParams
import os
from utils import *

def get_response(api_key, messages, temp):
    client = OpenAI(
        api_key=api_key,
        base_url="http://long-llama3-cache-predict-v1.insage-inference.ksvc.ibmc.t9kcloud.cn/v1/",
    )
    completion = client.chat.completions.create(
        model = "llama3-8b",
        messages = messages,
        temperature = temp
    )
    response = completion.choice[0].message
    return response

def get_file_summary(file_path, sys_path, api_key, temp):
    """
    Get pdf summary using llama.
    Args:
        file_path: [str]
            file path of pdf
        sys_path: [str]
            path of system prompt
        api_key: [str
            your llama3-8b openai api key
        temp: [float]
            temperature of llm generation
    """
    paper_text = extract_text_from_pdf(file_path)
    messages = read_summary_prompt(sys_path, paper_text)
    response = get_response(
        api_key=api_key,
        messages=messages,
        temp=temp
    )
    return response

def get_words_recommended_questions(
        file_path,
        sys_path,
        user_path,
        selected_text,
        api_key,
        temp,
):
    paper_text = extract_text_from_pdf(file_path)
    messages = read_words_prompt(
        sys_path=sys_path,
        user_path=user_path,
        paper_text=paper_text,
        selected_text=selected_text
    )
    response = get_response(
        api_key=api_key,
        messages=messages,
        temp=temp
    )
    return response

def get_chat_recommended_questions(
        file_path,
        sys_path,
        user_path,
        history,
        api_key,
        temp
):
    paper_text = extract_text_from_pdf(file_path)
    messages = read_words_prompt(
        sys_path=sys_path,
        user_path=user_path,
        paper_text=paper_text,
        history=history,
    )
    response = get_response(api_key=api_key, messages=messages, temp=temp)
    return messages, response

def get_words_explanation(
        file_path,
        sys_path,
        user_path,
        selected_text,
        api_key,
        temp
):
    paper_text = extract_text_from_pdf(file_path)
    messages = read_words_prompt(
        sys_path=sys_path,
        user_path=user_path,
        paper_text=paper_text,
        selected_text=selected_text
    )
    response = get_response(
        api_key=api_key,
        messages=messages,
        temp=temp
    )
    return response

def get_chat_answer(
        file_path,
        sys_path,
        user_path,
        history,
        selected_text,
        query,
        api_key,
        temp
):
    paper_text = extract_text_from_pdf(file_path)
    messages = read_chat_answer_prompt(
        sys_path=sys_path,
        user_path=user_path,
        paper_text=paper_text,
        history=history,
        selected_text=selected_text,
        query=query
    )
    response = get_response(
        api_key=api_key,
        messages=messages,
        temp=temp
    )
    return messages, response
    