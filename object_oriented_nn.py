import torch
import torch.nn as nn
import torch.nn.functional as F

class Network(nn.Module): 
    def __init__(self):
        super(Network, self).__init__()
        self.conv1 = nn.Conv2d(in_channels = 1, out_channels =6, kernel_size = 5)
        self.conv2 = nn.Conv2d(in_channels = 6, out_channels = 12, kernel_size =5)

        self.fc1 = nn.Linear(in_features = 12*4*4, out_features = 120)
        self.fc2 = nn.Linear(in_features = 120, out_features = 60)
        self.out = nn.Linear(in_features = 60, out_features = 10)
    

    def forward(self, t):
        #1:input layer
        t = t

        #2:hidden conv layer 1
        t = self.conv1(t)
        t = F.relu(t)
        t = F.max_pool2d(t, kernel_size = 2, strides = 2)

        #3:hidden conv layer 2
        t = self.conv2(t)
        t = F.relu(t)
        t = F.max_pool2d(t, kernel_size = 2, strides = 2 )

        #4: hidden linear layer 1
        t = t.reshape(-1, 12*4*4)
        t = self.fc1(t)
        t = F.relu(t)

        #5: hiddn linear layer 2
        t = self.fc2(t)
        t = F.relu(t)

        #6: output layer
        t = self.out(t)
        
        return t

        
