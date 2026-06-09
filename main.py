from openai import OpenAI
import OpenAI

client = OpenAI()#Insert API Key Here

response = client.chat.completions.create(
    model = 'gpt-4o-mini',
    messages=[
        {
            "role": "system",
            "content": "You are a helpful learning assistant that is tasked with helping the user understand the concepts they wish to learn.", #Gives AI context to answer user's prompts and give the basic idea of what the pattern they retain in their memory
        },
        {
            "role": "user",
            "content": "Explain to me the basics of AI.",
        },
    ],
),

print(response.choices[0].message.content)