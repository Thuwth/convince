# from ..tasks.kimi_task import *
from ..tasks.llama_task import *

class Llama_inference():
    def __init__(
            self,
            path_configs,
            configs,
    ):
        super(self, Llama_inference).__init__()
        self.sys_path = path_configs["system_path"]
        if "user_path" in path_configs.keys():
            self.user_path = path_configs["user_path"]
        self.configs = configs

    def file_summary(self):
        response = get_file_summary(
            file_path=self.configs["file_path"],
            sys_path=self.sys_path,
            api_key=self.configs.api_key,
            temp=self.configs["model"]["temperature"]
        )
        return response

    def words_recommended_questions(self):
        response = get_words_recommended_questions(
            file_path=self.configs["file_path"],
            sys_path=self.sys_path,
            user_path=self.user_path,
            selected_text=self.configs["selected_text"],
            api_key=self.configs["api_key"],
            temp = self.configs["model"]["temperature"]
        )
        return response

    def chat_recommended_questions(self, history):
        max_history_len = self.configs["max_history_length"]
        if len(history) <= int(max_history_len):
            trunc_history = history
        else:
            trunc_history = history[-int(max_history_len):]
        messages, response = get_chat_recommended_questions(
            file_path=self.configs["file_path"],
            sys_path=self.sys_path,
            user_path=self.user_path,
            history=trunc_history,
            api_key=self.configs["api_key"],
            temp=self.configs["model"]["temperature"],
        )
        history.append(
            {
                "messages": messages,
                "response": response,
            }
        )
        return response

    def words_explanation(self):
        response = get_words_recommended_questions(
            file_path=self.configs["file_path"],
            sys_path=self.sys_path,
            user_path=self.user_path,
            selected_text=self.configs["selected_text"],
            api_key=self.configs["api_key"],
            temp=self.configs["model"]["temperature"],
        )
        return response

    def chat_answer(self, history):
        if "selected_text" not in self.configs.keys():
            selected_text = ''
        else:
            selected_text = self.configs["selected_text"]
        max_history_len = self.configs["max_history_length"]
        if len(history) <= int(max_history_len):
            trunc_history = history
        else:
            trunc_history = history[-int(max_history_len) :]
        messages, response = get_chat_answer(
            file_path=self.configs["file_path"],
            sys_path=self.sys_path,
            user_path=self.user_path,
            history=trunc_history,
            selected_text=selected_text,
            query=self.configs["query"],
            api_key=self.configs["spi_key"],
            temp=self.configs["model"]["temperature"]
        )
        history.append(
            {
                "messages": messages,
                "response": response
            }
        )
        return response
    
