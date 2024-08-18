import pandas as pd
import os
import fire
import logging
from llama import Llama, Dialog

def main(ckpt_dir, tokenizer_path, temperature=1, top_p=1, max_seq_len=4096, max_batch_size=1, max_gen_len=None):
    # Setup logging
    logging.basicConfig(filename='error_log.txt', level=logging.ERROR)

    directory_path = 'test_sets/'
    result_directory = 'result/'
    os.makedirs(result_directory, exist_ok=True)

    try:
        all_files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f)) and f.endswith('.csv')]

        generator = Llama.build(ckpt_dir=ckpt_dir, tokenizer_path=tokenizer_path, max_seq_len=max_seq_len, max_batch_size=max_batch_size)

        for file in all_files:
            try:
                df = pd.read_csv(os.path.join(directory_path, file))
                dialogs = [[{"role": "user", "content": content}] for content in df['input']]

                results = generator.chat_completion(dialogs, max_gen_len=max_gen_len, temperature=temperature, top_p=top_p)

                df['llama-70b-chat'] = [result['generation']['content'] for result in results]
                df.to_csv(os.path.join(result_directory, file), index=False)
            except Exception as e:
                logging.error(f"Error processing file {file}: {e}")

    except Exception as e:
        logging.error(f"Error in main function: {e}")

if __name__ == "__main__":
    fire.Fire(main)
