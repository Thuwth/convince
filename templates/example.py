import os

from jinja2 import Template

file_path = os.path.abspath(os.path.dirname(__file__))

# In the actual application scenario you need to change the information such as paper_text and history.
paper_text = "This is the paper content."
history = []
for i in range(2):
    history.append("history_" + str(i))
print(history)

temp_path = os.path.join(file_path, "get_words_answers.jinja")

# code for how to use jinja file
reader = open(temp_path, encoding="latin1")
temp = Template(reader.read())

prompt = temp.render(
    paper_text=paper_text,
    history=history
)
print(prompt)
