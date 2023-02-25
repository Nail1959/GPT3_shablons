# coding=utf8
# Importing Dependencies
from chronological import read_prompt, cleaned_completion, main


# Пример краткой "выжимки из текста"
# Prompt источник: https://ru.wikipedia.org/wiki/AlphaGo

async def summarization_example():
    
    # Используется текстовый файл ('summarize_for_AlphaGo') в папке prompts как входной параметр prompt
    prompt_summarize = read_prompt('summarize_for_AlphaGo')
    
    # Вызов completion метода с заданными параметрами GPT-3
    # Параметы: max_tokens=100 количество используемых токенов,
    # engine="davinci" - модель,
    # temperature=0.9, - недерменированность ответа программы, диапазон от 0 до 1
    # top_p=1, диапазон от 0 до 1
    # frequency_penalty=0.2, диапазон от 0 до 1
    # stop=["\n\n"]
    completion_summarize = await cleaned_completion(prompt_summarize, max_tokens=100, engine="davinci",
                                                    temperature=0.9, top_p=1, frequency_penalty=0.2, stop=["\n\n"])
    
    # возвращает ответ
    return completion_summarize

# Designing the end-to-end async workflow, capable of running multiple prompts in parallel  
async def workflow():

    # Асинхронный вызов summarization function
    text_summ_example = await summarization_example()
    text_summ_example = text_summ_example.replace('. ', '.\n')

    # Вывод результата в консоли
    print('-------------------------')
    print('Basic Example Response: {0}'.format(text_summ_example))
    print('-------------------------')
    # Вывод результата в текстовый файл
    with open('summary_response.txt', encoding='UTF-8', mode='w') as f:
        f.write(f'Basic Example Response: {text_summ_example}')

# invoke Chronology by using the main function to run the async workflow
main(workflow)
