from transformers import AutoTokenizer,AutoModelForCausalLM
import os
from huggingface_hub import snapshot_download
from dotenv import load_dotenv

class DownloadTextModel:
    def __init__(self, model_name:str, save_dir:str) -> None:
        """
        Intialized the model and sets generation configuration
        Args:
            model_file (str): Model file path in string format
            save_dir (str): Download folder
        Raises:
            TypeError: If the model file is not a string. 
        """
        self.save_dir = save_dir
        self.model_name = model_name
        if not os.path.exists(self.save_dir):
            print(f"Creating {self.save_dir} folder")
            os.makedirs(self.save_dir)
        #self.download_tokenizer()
        self.download_model()

    def download_tokenizer(self):
        """
        Download the tokenizer into save directory

        Returns:
            AutoTokenizer: downloded model
        """
        tokenizer_save_path = f"{self.save_dir}/tokenizer"
        print(f"Downloading tokenizer into {tokenizer_save_path} folder")
        tokenizer = AutoTokenizer.from_pretrained(self.model_name,)
        return tokenizer.save_pretrained(tokenizer_save_path)
       
    def download_model(self):
        """
        Download a Hugging Face model to a specified directory
        
        :param model_name: Name of the model on Hugging Face (e.g., 'gpt2')
        :param output_dir: Directory to save the model
        """
        # Download the model
        snapshot_download(
            repo_id=self.model_name,allow_patterns=["*.md", "*.json"],
            local_dir=self.save_dir,ignore_patterns="vocab.json",
            local_dir_use_symlinks=False
        )
        print(f"Model {self.model_name} downloaded to {self.save_dir}")
    
    def download_model_backup(self):
        """
        Downloads a text model based on the specified model name and assigns to self.model

        Returns: 
            AutoModelForCausalLM: The loaded model instance.
        """ 
        model_savepath = f"{self.save_dir}/model"
        print(f"Model downloading into {model_savepath} folder\n")
        model = AutoModelForCausalLM.from_pretrained(self.model_name)
        return model.save_pretrained(model_savepath)

if __name__ =="__main__":
    load_dotenv()
    MODEL_NAME = os.getenv("MODEL_NAME","meta-llama/Llama-3.2-1B") 
    MODEL_DIR = os.getenv("MODEL_DIR","Llama-3.2-1B")
    DownloadTextModel(model_name=MODEL_NAME,save_dir=MODEL_DIR)
   
    #snapshot_download(repo_id="tiiuae/falcon-rw-1b",local_dir=save_folder)
