import openai

# p = ''''''

f = []
while True:
    a = input()
    if a:
        f.append(a)
    else:
        break

# f = (p.splitlines())
while '*' in f:
    f.remove('*')
while '1 балл' in f:
    f.remove('1 балл')
questions = list()
for i in range(0, len(f), 5):
    questions.append(
        f'Выберите один самый верный ответ на вопрос и укажите цифру "{f[i]}"\n1. {f[i + 1]}\n2. {f[i + 2]}\n3. {f[i + 3]}\n4. {f[i + 4]}')

openai.api_key = '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'

answers = list()
for i in range(len(questions)):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Q: {questions[i]}\nA:",
        temperature=0,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    print(f"{f[i * 5]}\n    {response['choices'][0]['text']}")
    answers.append(response['choices'][0]['text'])

print('\n', '\n'.join(answers))
