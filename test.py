import argparse
import json
#from models.llama import LLamaModel
#from models.gpt import GPTModel


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--task', type=str, required=True)
    parser.add_argument('--dataset', type=str, required=True)
    parser.add_argument('--model', type=str, required=True)
    parser.add_argument('--few-shot', type=int, default=0, choices=[0, 1, 3, 5], help='Number of few-shot prompts to use. Valid values: 0, 1, 3, 5.')
    args = parser.parse_args()

    with open(f'./config/{args.model}/{args.task}_{args.model}_{args.dataset}_config.json', 'r') as f:
        config = json.load(f)

    config['num_shots'] = args.few_shot

    if args.model == 'llama':
        from tasks.radiology_report_summarization.llama import iu_xray, mimic_cxr
        from tasks.Discharge_Summary_Generation.llama import mimicIII
        from tasks.Medical_Text_Reasoning.llama import mu
    elif args.model == 'llama_chat':
        from tasks.radiology_report_summarization.llama_chat import iu_xray, mimic_cxr
        from tasks.Medical_Text_Reasoning.llama_chat import mu
    elif args.model == 'gpt':
        from tasks.radiology_report_summarization.gpt import mimic_cxr,iu_xray
    elif args.model == 'chatglm':
        from tasks.radiology_report_summarization.chatglm import mimic_cxr,iu_xray
    else:
        raise ValueError(f"Unknown model '{args.model}'")

    if args.task == 'RRS':
        if args.dataset == 'mimic_cxr':
            task = mimic_cxr.MimicCXR(config)
        elif args.dataset == 'iu_xray':
            task = iu_xray.IUXRay(config)
        else:
            raise ValueError(f"Unknown dataset '{args.dataset}' for task '{args.task}'")
    elif args.task == 'DSG':
        if args.dataset =='mimic_III':
            task = mimicIII.MimicIII(config)
        else:
            raise ValueError(f"Unknown dataset '{args.dataset}' for task '{args.task}'")
    elif args.task == 'MTR':
        if args.dataset =='MU':
            task = mu.MedQA_USMLE(config)
        else:
            raise ValueError(f"Unknown dataset '{args.dataset}' for task '{args.task}'")
    if args.model == 'llama':
        model = LLamaModel(config)
    elif args.model == 'llama_chat':
        model = LLamaModel(config)
    if args.model == 'gpt':
        model = GPTModel(config)
    elif args.model == 'chatglm':
        model = ChatGlmModel(config)

    task.run(model)
