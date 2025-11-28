# Underwater-Image-Object-Segmentation-Model-for-Ocean-Exploration

본 코드는 [XMem: Long-Term Video Object Segmentation with an Atkinson-Shiffrin Memory Model](https://github.com/hkchengrex/XMem)를 기본으로 하여 작성되었습니다.
해양 탐사를 위한 수중 이미지 객체 분할 모델입니다.

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
![xmem_whale-ezgif com-video-to-gif-converter (1)](https://github.com/user-attachments/assets/b7c5d414-70bb-4e19-b3aa-b1574b344cd9)

![xmem_ugly_fish-ezgif com-video-to-gif-converter+(1)](https://github.com/user-attachments/assets/0f306cfd-798e-4974-bb41-9f46ae9b6bfa)
