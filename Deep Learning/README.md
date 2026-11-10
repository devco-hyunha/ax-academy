# Deep Learning Study

딥러닝 학습 노트 저장소입니다. 세션별로 내용을 정리합니다.

머신러닝 노트는 [`../Machine Learning/`](../Machine%20Learning/)에 있습니다.

## 처음 읽는 분

1. **순서:** [`session01.md`](./session01.md)부터 번호 순으로 읽습니다. 각 문서 위·아래 **이동** 링크로 이전·다음 세션을 열 수 있습니다.
2. **읽는 팁:** 본문의 **이 세션이 하는 일**과 **쉽게 이해하기**를 먼저 읽은 뒤, 표·코드를 보시면 부담이 덜합니다.

## 세션 목록

- [`session01.md`](./session01.md) — 딥러닝 기초 1 (함수·미분, 신경망 입문, 선형회귀·경사하강, PyTorch 환경)
- [`session02.md`](./session02.md) — 딥러닝 기초 2 (NumPy, 선형대수, 벡터 내적)
- [`session03.md`](./session03.md) — 딥러닝 기초 3 (텐서 차원·모양·view)
- [`session04.md`](./session04.md) — 딥러닝 기초 3 (행렬곱·연산 + 사용자 Dataset·DataLoader)
- [`session05.md`](./session05.md) — 딥러닝 기초 3 (`__call__`·Compose·MNIST·DataLoader)
- [`session06.md`](./session06.md) — 딥러닝 기초 4 (ANN·퍼셉트론·활성화·nn.Module·TensorDataset)
- [`session07.md`](./session07.md) — 딥러닝 기초 5 (선형회귀·state_dict·SGD·Optimizer 3연타·autograd)
- [`session08.md`](./session08.md) — 딥러닝 기초 6 (커스텀 Module·LinearReg·다출력·Linear(4,2) 학습)

## PyTorch 노트북

- [`PyTorch/01_tensor_linear_regression.ipynb`](./PyTorch/01_tensor_linear_regression.ipynb) — 텐서 · autograd · `y=wx+b` 경사하강 입문 (`torch-env` 권장)
- [`PyTorch/02_tensor_ndim_view.ipynb`](./PyTorch/02_tensor_ndim_view.ipynb) — 텐서 ndim · shape · view
- [`PyTorch/03_tensor_matmul_ops.ipynb`](./PyTorch/03_tensor_matmul_ops.ipynb) — 행렬곱 · item · sum · argmax
- [`PyTorch/04_custom_dataset.ipynb`](./PyTorch/04_custom_dataset.ipynb) — 사용자 Dataset · DataLoader
- [`PyTorch/05_mnist_transforms_dataloader.ipynb`](./PyTorch/05_mnist_transforms_dataloader.ipynb) — Compose · MNIST · DataLoader · 시각화
- [`PyTorch/06_tensor_dataset.ipynb`](./PyTorch/06_tensor_dataset.ipynb) — TensorDataset · DataLoader
- [`PyTorch/07_linear_train_loop.ipynb`](./PyTorch/07_linear_train_loop.ipynb) — nn.Linear · MSE · SGD · state_dict 학습 루프
- [`PyTorch/08_custom_linear_module.ipynb`](./PyTorch/08_custom_linear_module.ipynb) — 수동 forward · LinearReg · `__call__` · mse_loss
- [`PyTorch/09_multi_output_linear.ipynb`](./PyTorch/09_multi_output_linear.ipynb) — Linear(4,2) · MSE · SGD · 다출력 학습 루프

## 파일 규칙

- 각 세션은 `sessionNN.md`로 순번을 매긴다
- 새 세션이 추가되면 session02.md 이후부터 이어간다
