import torch

pretrain = torch.load('saves/XMem.pth')

# key_encoder 안의 weight만 추출
key_encoder_weights = {k.replace('key_encoder.', ''): v 
                       for k, v in pretrain.items() 
                       if k.startswith('key_encoder.')}

# 파일로 저장
torch.save(key_encoder_weights, 'saves/key_encoder_weights.pth')

print("key_encoder weights 저장 완료: saves/key_encoder_weights.pth")
