# coding=utf8
# Importing Dependencies
from chronological import read_prompt, cleaned_completion, main
import os
import time

def csv_to_prompt(file_name='data_for_task2.csv'):
    file_out = file_name.replace('.csv', '.txt')
    file_out_path = os.path.join('prompts', file_out)
    try:
        os.remove(file_out_path)
    except:
        pass
    fout = open(file_out_path, mode='a', encoding='utf-8')
    fout_list = list()
    with open(file_name, newline='') as f:
        reader = f.readlines()
        for row in reader:
            str = row.split(';')  # str список из двух элементов
            if len(str) > 2 or len(str) < 2:
                break
            try:
                fout_list.append(str[0]+': ' + str[1].replace('\n',''))
            except:
                break
    max_rate = len(fout_list)
    fout = open(file_out_path, mode='a', encoding='utf-8')
    fout.write(f'Range the emotion in these emails and sort by range from {max_rate} to 1, most positive is {max_rate} :\n\n')
    for l in fout_list:
        fout.write(l)

    fout.write('\n'+'Response must have form: \nRate:\nE-mail:\n')
    fout.close()

    return file_out
async def classify_emails_by_emotions():

    f_prompt = csv_to_prompt(file_name='data_for_task2.csv')
    prompt_classify = read_prompt(f_prompt.replace('.txt',''))
    completion_classify = await cleaned_completion(prompt_classify, max_tokens=900, engine="davinci",
                                                temperature=0.9, top_p=1, frequency_penalty=0.1) #, stop=["\n\n"])
    # time.sleep(30)
    # возвращает ответ
    return completion_classify

async def workflow():

    # Асинхронный вызов функции ранжирования emails по эмоциям
    text_classify = await classify_emails_by_emotions()
    # text_classify = text_classify.replace('. ', '.\n')

    # Вывод результата в консоли
    print('-------------------------')
    print(f'Response: {text_classify}')
    print('-------------------------')
    # Вывод результата в текстовый файл
    with open('classify_response.txt', encoding='UTF-8', mode='w') as f:
        f.write(f'  Response:\n {text_classify}')

# invoke Chronology by using the main function to run the async workflow
main(workflow)