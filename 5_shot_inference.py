import json

import random

def generate_few_shot_prompts(input_file, output_file, num_prompts=5):
    with open(input_file, 'r', encoding='utf-8') as f:
        all_data = [(idx, json.loads(line.strip())) for idx, line in enumerate(f)]

    selected_data = random.sample(all_data, num_prompts)

    few_shot_prompts = []

    for original_idx, data in selected_data:
        prompt = data['question']

        options = [f"{key}. {data['options'][key]}" for key in sorted(data['options'].keys())]

        response = data['answer_idx']


        few_shot_prompts.append({
            'original_idx': original_idx,
            'prompt': prompt,
            'options': options,
            'response': response
        })


    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(few_shot_prompts, f, ensure_ascii=False, indent=4)


input_file_path = "/Users/zhouxuan/Desktop/LLM_Benchmark4health/data/MedQA-USMILE/us/test.jsonl"
output_file_path = "/Users/zhouxuan/Desktop/LLM_Benchmark4health/few_shot_prompts/MedQA-USMLE/us/few_shot_prompts.json"
generate_few_shot_prompts(input_file_path, output_file_path)
