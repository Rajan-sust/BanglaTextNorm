"""
__author__ = "Rajan Saha Raju"
__email__ = "rajan-ictc@sust.edu"
"""

from groq import Groq

client = Groq()

def ask_llm(system_prompt: str, user_prompt: str, json_mode=False) -> str:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        temperature=0.5,
        max_completion_tokens=8192,
        top_p=1, 
        stream=False,
        response_format={"type": "json_object"} if json_mode else None,
        stop=None
    )
    return response.choices[0].message.content




if __name__ == "__main__":
    r = ask_llm("You are a helpful assistant.", "What is the capital of France?")
    print(r)
