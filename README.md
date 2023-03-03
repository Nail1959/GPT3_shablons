# GPT3_shablons
Shablons for working with OpenAI GPT API.

Пример использования OpenAI GPT API.

в файле /prompts/summarize_for_AlphaGo.txt .
взято описание из википедии https://en.wikipedia.org/wiki/AlphaGo .
программа text_sumarization.py выведет краткую информацию с заданным 
максимальным количеством токенов.

программа classify_emails_by_emotions.py ранжирование сообщений по эмоциональной окраски сообщения
из тестовой задачи №2

За основу взята информация из книги "GPT-3" авторов Sandra Kublik, Shubham Saboo.
Книга посвещена возможностям GPT-3, API, перспективам развития направления.

1. Необходимо зарегестрироваться в openai.com. Для России необходимо установить VPN и получить SMS оповещение.
1. Необходимо получить API secret key и вписать его в файл .env.
3. pip install -r requirements.txt.

Папка prompts_html содержит примеры ввода (prompt) для разных возможных задач. 
Примеры взяты из видеокурса chatgpt-101-supercharge-prompts. Реализованы в виде java-scripts.