# Underwater-Image-Object-Segmentation-Model-for-Ocean-Exploration

본 코드는 [XMem: Long-Term Video Object Segmentation with an Atkinson-Shiffrin Memory Model](https://github.com/hkchengrex/XMem)를 기본으로 하여 작성되었습니다.
해양 탐사를 위한 수중 이미지 객체 분할 모델입니다.

## Environment
- **OS:** Ubuntu 20.04  
- **Python:** 3.10.18  
- **PyTorch:** 2.0.1  
- **CUDA:** 11.7  
- **GPU:** Required for training/inference  

---
## Pretrained Weights
1. **기본 가중치 다운로드**  
[XMem.pth](https://github.com/hkchengrex/XMem) 를 다운로드 후 `saves/` 폴더에 저장.

2. **어댑터 가중치 추출**  

```bash
python extractor.py
```
```bash
saves/
 ├─ XMem.pth
 └─ key_encoder_weights.pth
```
