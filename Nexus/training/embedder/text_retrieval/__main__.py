import json
from transformers import HfArgumentParser

from Nexus.training.embedder.text_retrieval import *

def main():
    data_config_path='/root/Nexus/examples/text_retrieval/training/embedder/data_config.json'
    train_config_path='/root/Nexus/examples/text_retrieval/training/embedder/training_config.json'
    model_config_path='/root/Nexus/examples/text_retrieval/training/embedder/model_config.json'
    
    model_args = TextEmbedderModelArguments.from_json(model_config_path)
    data_args = TextEmbedderDataArguments.from_json(data_config_path)
    training_args = TextEmbedderTrainingArguments.from_json(train_config_path)
    runner = TextEmbedderRunner(
        model_args=model_args,
        data_args=data_args,
        training_args=training_args
    )
    runner.run()


if __name__ == "__main__":
    main()
