import csv
import json
import random
import os


def generate_prompts_from_csv(input_path, output_folder, num_samples=1):
    if not os.path.exists(input_path):
        print(f"Error: File '{input_path}' does not exist!")
        return

    with open(input_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        data = [row for row in reader]

    selected_samples = random.sample(data, num_samples)

    prompts = []
    for sample in selected_samples:
        key = sample['key']
        prompt = sample['discharge_instruction'].replace("\n", " ")
        response = sample['discharge_summary'].replace("\n", " ")

        prompts.append({
            "key": key,
            "prompt": prompt,
            "response": response
        })


    os.makedirs(output_folder, exist_ok=True)

    output_path = os.path.join(output_folder, "few_shot_prompts.json")
    with open(output_path, 'w') as json_file:
        json.dump(prompts, json_file, indent=4)

    print(f"Prompts saved to '{output_path}'")


input_path = "/Users/sid/Desktop/LLM_Benchmark4health/data/MIMIC-III/test.csv"
output_folder = "/Users/sid/Desktop/LLM_Benchmark4health/few_shot_prompts/mimic-III"
generate_prompts_from_csv(input_path, output_folder)
