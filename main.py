from openai import OpenAI

client = OpenAI() #Insert OpenAI key here

response = client.chat.completions.create(
    model = 'gpt-4o-mini',
    messages = [
        {
            "role": "system",
            "content": "You are a helpful learning assistant tasked with helping the user understand concepts they ask."
        },
        {
            "role": "user",
            "content": "Teach me the basics of machine learning."
        },
    ],
)

print(response.choices[0].message.content)