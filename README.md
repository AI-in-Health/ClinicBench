# ClinicBench
Large Language Models in the Clinic: A Comprehensive Benchmark

## Abstract:

The adoption of large language models (LLMs) to assist clinicians has attracted remarkable attention. Existing works mainly adopt the close-ended question-answering (QA) task with answer options for evaluation. However, many clinical decisions involve answering open-ended questions without pre-set options. To better understand LLMs in the clinic, we construct a benchmark ClinicBench. We first collect eleven existing datasets covering diverse clinical language generation, understanding, and reasoning tasks. Furthermore, we construct six novel datasets and complex clinical tasks that are close to real-world practice, i.e., referral QA, treatment recommendation, hospitalization (long document) summarization, patient education, pharmacology QA and drug interaction for emerging drugs. We conduct an extensive evaluation of twenty-two LLMs under both zero-shot and few-shot settings. Finally, we invite medical experts to evaluate the clinical usefulness of LLMs.

## Structure
```
The root of this repo/
    dataset                             # Benchmark Datasets
    ├── dataset1
    │── dataset2                 
    ├──  .
    ├──  .
    ├──  .
    │── dataset17
    metrics                             # Evaluation Metrics
    ├── bleu
    ├── cider
    ├── meteor          
    ├── rouge
    results                             # LLM-generated Outputs
    ├── dataset1
    │── dataset2                 
    ├──  .
    ├──  .
    ├──  .
    codes                              # Evaluation Codes
    │
    └── ...
```
The `data` folder contains the following subfolders:
- The `mimic_cxr` folder contains MIMIC-CXR image data and corresponding annotation (eg., image id, report etc...).
- The `finetune` folder contains the image data and corresponding annotation (eg., image id, report etc...) of the downstream dataset. 
- The `pretrained` folder contains the initialized weights for our model which will download automatically when you run the code.
- The `decoder_config` and `checkpoint` folders contain the configuration file of the model, and its weights, respectively.
