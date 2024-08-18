import json
import random

def load_data(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

def select_few_shot_prompts(data, n=3):
    normal_data = [item for item in data if "normal" in item["findings"].lower()]
    abnormal_data = [item for item in data if "abnormal" in item["findings"].lower()]

    if len(normal_data) + len(abnormal_data) < n:
        raise ValueError("Not enough data to select from.")

    selected_prompts = random.sample(normal_data, n//2)
    selected_prompts.extend(random.sample(abnormal_data, n - len(selected_prompts)))

    return selected_prompts

def save_to_file(prompts, filename):
    transformed_data = [
        {"uid": item["uid"], "prompt": item["findings"], "response": item["impression"]}
        for item in prompts
    ]

    with open(filename, 'w') as f:
        json.dump(transformed_data, f, indent=4)

data = load_data("./data/iu-xray/iu-xray.json")
few_shot_prompts = select_few_shot_prompts(data, 3)
save_to_file(few_shot_prompts, "./few_shot_prompts/iu-xray/few_shot_prompt.json")
