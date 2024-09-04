# Kimi Templates

我把 Tempalates 按照需求分成 user 和 system，调用的时候只需要调用对应任务的 system 和 user template 之后将其拼在一起即可使用。
下面是各 prompt 中的变量：

|        | get_file_summary | get_chat_recommended_questions | get_words_recommended_questions | get_words_explanation | get_chat_answer             |
|--------|------------------|--------------------------------|---------------------------------|-----------------------|-----------------------------|
| system | paper_text       | paper_text                     | paper_text                      | paper_text            | paper_text                  |
| user   | None             | history                        | selected_text                   | selected_text         | history/selected_text/query |