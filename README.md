# Underwater-Image-Object-Segmentation-Model-for-Ocean-Exploration
본 코드는 [XMem: Long-Term Video Object Segmentation with an Atkinson-Shiffrin Memory Model](https://github.com/hkchengrex/XMem)를 기본으로 하여 작성되었습니다

---

## Environment

- **OS:** Ubuntu 20.04  
- **Python:** 3.10.18  
- **PyTorch:** 2.0.1  
- **CUDA:** 11.7  
- **GPU:** Required for training/inference  

---

## train
기본 가중치([XMem.pth](https://github.com/hkchengrex/XMem))를 다운 후 saves/에 저장 \\
어뎁터 가중치 생성
```bash
python extractor.py
