import json
import pdb

from pycocoevalcap.bleu.bleu import Bleu
from pycocoevalcap.meteor import Meteor
from pycocoevalcap.rouge import Rouge




#model_path = './weights/llama_chat/tokenizer.model'
#tokenizer = Tokenizer(model_path)

# For iu-xray
with open("./few_shot_prompts/iu-xray/few_shot_prompt.json", "r") as f:
    few_shot_data = json.load(f)

few_shot_uids = set(item["uid"] for item in few_shot_data)
print(few_shot_uids)

def compute_scores(gts, res):
    """
    Performs the MS COCO evaluation using the Python 3 implementation (https://github.com/salaniz/pycocoevalcap)

    :param gts: Dictionary with the image ids and their gold captions,
    :param res: Dictionary with the image ids ant their generated captions
    :print: Evaluation score (the mean of the scores of all the instances) for each measure
    """
    # Set up scorers
    scorers = [
        (Bleu(4), ["BLEU_1", "BLEU_2", "BLEU_3", "BLEU_4"]),
        (Meteor(), "METEOR"),
        (Rouge(), "ROUGE_L")
    ]
    eval_res = {}
    total_scorers = len(scorers)
    processed_scorers = 0

    # Compute score for each metric
    for scorer, method in scorers:
        try:
            score, scores = scorer.compute_score(gts, res, verbose=0)
        except TypeError:
            score, scores = scorer.compute_score(gts, res)

        processed_scorers += 1
        print(f"Processed {processed_scorers}/{total_scorers} scorers.")

        if type(method) == list:
            for sc, m in zip(score, method):
                eval_res[m] = sc
        else:
            eval_res[method] = score

    return eval_res

with open("./data/iu-xray/iu-xray.json", "r") as f:
    real_data = json.load(f)
with open("/Users/sid/Desktop/LLM_Benchmark4health/results/RRS/iu-xray/gpt/gpt3.5/gpt_shot.json", "r") as f:
    generated_data = json.load(f)


#real_data = real_data['test']
gts = {}
res = {}

for entry in real_data:
    impression = entry["impression"].replace("\n", " ")
    #token_ids = tokenizer.encode(impression, bos=False, eos=False)
    gts[entry["uid"]] = [impression]

for entry in generated_data:
    generated_impression = entry["generated_impression"].replace("\n", " ")
    #token_ids = tokenizer.encode(generated_impression, bos=False, eos=False)
    res[entry["uid"]] = [generated_impression]




missing_uids = set(gts.keys()) - set(res.keys())


for uid in missing_uids:
    del gts[uid]


scores = compute_scores(gts, res)
print(scores)
