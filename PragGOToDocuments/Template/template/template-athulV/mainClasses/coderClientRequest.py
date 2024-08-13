
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

#For future cases - - - - we have our agents inherit form this
class CoderClientRequest:
    def __init__(self, prompt, model, userInput, streaming):
        self.prompt = prompt
        self.model = model
        self.client = OpenAI()
        self.userInput = userInput
        self.streaming = streaming

    def generate(self):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self.prompt},
                {"role": "user", "content": self.userInput}
            ],
            temperature=0.7,
            stream=self.streaming,
            max_tokens= 4096
        )

        output = ""
        print()
        if self.streaming:
            for chunk in response:
                if chunk.choices[0].delta.content is not None:
                    print(chunk.choices[0].delta.content, end="")
                    output += chunk.choices[0].delta.content
        else:
            output = response
        #Returns a json object
        return output
    
# Testing
# testObject = ClientRequest("You are a helpful assistant", "gpt-4o", "What is the meaning of life", True)
# testObject.generate()