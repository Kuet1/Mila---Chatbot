from transformers import AutoTokenizer, GPT2LMHeadModel
import torch




class ChatController:
    
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("openai-community/gpt2")
        self.model = GPT2LMHeadModel.from_pretrained("openai-community/gpt2")

    def generate_response(self, message: str, max_length: int = 100):
        """
        
        Create a answer using the users input

        """
        try:

            inputs = self.tokenizer(message, return_tensors="pt")

            outputs = self.model.generate(
                inputs["input_ids"],
                max_length=max_length,
                num_return_sequences=1,
                do_sample=True,
                top_k=50,
                top_p=0.95,
                temperature=0.7
                )
            
            
            response = self.tokenizer.decode(outputs[0], skip_special_token=True)
            return response
        
        except Exception as e:
            return f"Erro ao gerara resposta: {str(e)}"