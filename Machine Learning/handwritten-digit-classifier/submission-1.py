import torch
import torch.nn as nn
from torchtyping import TensorType

class Solution(nn.Module):
    def __init__(self):
        super().__init__()
        torch.manual_seed(0)
        
        self.architecture = nn.Sequential(
            nn.Linear(28*28, 512),
            nn.ReLU(),
            nn.Dropout(p=0.2, inplace=True),
            nn.Linear(512, 10),
            nn.Sigmoid()
        )
        
    
    def forward(self, images: TensorType[float]) -> TensorType[float]:
        torch.manual_seed(0)
        prediction = self.architecture.forward(images)
        return torch.round(prediction, decimals=4)
        # Return the model's prediction to 4 decimal places