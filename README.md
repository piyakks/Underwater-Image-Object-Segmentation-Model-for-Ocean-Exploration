# Underwater-Image-Object-Segmentation-Model-for-Ocean-Exploration

본 코드는 [XMem: Long-Term Video Object Segmentation with an Atkinson-Shiffrin Memory Model](https://github.com/hkchengrex/XMem)를 기본으로 하여 작성되었습니다.

해양 탐사를 위한 수중 영상 객체 분할 모델.

## Model_Overview
![그림1](https://github.com/user-attachments/assets/3235923a-7f5c-4196-bb42-ea9be1a191b2)
## Adapter_detail
![그림3](https://github.com/user-attachments/assets/bf54e236-bee0-4ed2-9b56-c81015378fe5)

## Environment
- **OS:** Ubuntu 20.04  
- **Python:** 3.10.18  
- **PyTorch:** 2.0.1  
- **CUDA:** 11.7  
- **GPU:** RTX 3090 24GB

---
## training
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
3. 학습
```bash
torchrun --nproc_per_node=[gpu] --master_port=25763 train.py  --exp_id retrain_stage3_only  --stage 3  --load_network_control saves/XMem.pth 
```   
## inference
```bash
python eval.py --model [path to model file] --output [where to save the output] --dataset [which dataset to evaluate on] --split [val for validation or test for test-dev]
```

## Result
![xmem_whale-ezgif com-video-to-gif-converter (1)](https://github.com/user-attachments/assets/b3e987e1-72d9-4572-8a33-ff2401b28b3e)
![xmem_ugly_fish-ezgif com-video-to-gif-converter (1)](https://github.com/user-attachments/assets/6c4534f4-d812-49c6-8ef7-5cc3c1a88d00)
## Result_table
<img width="564" height="560" alt="image" src="https://github.com/user-attachments/assets/cd11acd0-abf6-4afd-b923-3f2b8ed54b53" />


