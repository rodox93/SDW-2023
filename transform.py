import openai

openai.api_key  = 'chave api openai'

def generate_ai_news(user):
    completion = openai.ChatCompletion.create(
        model="text-davinci-003",
        messages=[
            {
                "role":"system", 
                "content":"Você é um especialista em marketing bancário."
            },
            {
                "role": "user", 
                "content": f"Crie uma mensagem para {user['name']} sobre a importância dos investimentos (máximo de 100 caracteres)!"
            }
        ]
    )
    return completion.choices[0].message.content.strip('\"')

for user in users:
    news = generate_ai_news(user)
    print(news)
    user['news'].append({
        "description" : news
    })
