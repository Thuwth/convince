import fitz
from jinja2 import Template

def extract_text_from_pdf(file_path):
    """
    Extract text from pdf file.

    Args:
        file_path: the path of pdf file
    """
    doc = fitz.open(file_path)
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    doc.close()
    return full_text

def read_summary_prompt(sys_path, paper_text):
    sys_render = open(sys_path, encoding="latin1")
    sys_temp = Template(sys_render.read())
    Prompt = sys_temp.render(
        paper_text=paper_text
    )
    Input = ""
    messages = [
                {"role": "system", "content": Prompt},
                {"role": "user", "content": Input}
            ]
    return messages

def read_words_prompt(
        sys_path,
        user_path,
        paper_text,
        selected_text,
):
    sys_render = open(sys_path, encoding="latin1")
    sys_temp = Template(sys_render.read())
    user_render = open(user_path, encoding="latin1")
    user_temp = Template(user_render.read())
    Prompt = sys_temp.render(
        paper_text=paper_text
    )
    Input = user_temp.render(
        selected_text=selected_text
    )
    messages = [
                {"role": "system", "content": Prompt},
                {"role": "user", "content": Input}
            ]
    return messages

def read_chat_recommended_prompt(
        sys_path,
        user_path,
        paper_text,
        history,
):
    sys_render = open(sys_path, encoding="latin1")
    sys_temp = Template(sys_render.read())
    user_render = open(user_path, encoding="latin1")
    user_temp = Template(user_render.read())
    Prompt = sys_temp.render(
        paper_text=paper_text
    )
    Input = user_temp.render(
        history=history
    )
    messages = [
                {"role": "system", "content": Prompt},
                {"role": "user", "content": Input}
            ]
    return messages

def read_chat_answer_prompt(
        sys_path,
        user_path,
        paper_text,
        history,
        selected_text,
        query
):
    sys_render = open(sys_path, encoding="latin1")
    sys_temp = Template(sys_render.read())
    user_render = open(user_path, encoding="latin1")
    user_temp = Template(user_render.read())
    Prompt = sys_temp.render(
        paper_text=paper_text
    )
    Input = user_temp.render(
        history=history,
        selected_text=selected_text,
        query=query
    )
    messages = [
                {"role": "system", "content": Prompt},
                {"role": "user", "content": Input}
            ]
    return messages