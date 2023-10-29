import torch.nn as nn
from model.NewtonDN_detail import NewtonDNNet


class NewtonDN_model(nn.Module):
    def __init__(self):
        super(NewtonDN_model, self).__init__()
        self.swin_unet = NewtonDNNet(img_size=256,
                               patch_size=4,
                               in_chans=3,
                               out_chans=3,
                               embed_dim=96,
                               depths=[8, 8, 8, 8],
                               num_heads=[8, 8, 8, 8],
                               window_size=8,
                               mlp_ratio=4.0,
                               qkv_bias=True,
                               qk_scale=8,
                               drop_rate=0.,
                               drop_path_rate=0.1,
                               ape=False,
                               patch_norm=True,
                               use_checkpoint=False)


    def forward(self, x):
        if x.size()[1] == 1:
            x = x.repeat(1, 3, 1, 1)
        logits = self.swin_unet(x)
        return logits

