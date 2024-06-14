active virtual env
```
env/Scripts/Activate.ps1 
pip install -r requirements.txt
```

Conda 
```
conda create -n venv python numpy pandas
conda activate venv
```
Copy file to persisten volume
```
kubectl cp .\models swapify/swapify-face-swap-deployment-696cdfc486-8ht6g:/root/.insightface/models
kubectl cp .\model\inswapper_128.onnx swapify/swapify-face-swap-deployment-696cdfc486-8ht6g:/app/model
```
Docker build
```
docker build -f Dockerfile -t swapify/face-swap-service .
docker tag swapify/face-swap-service registry.digitalocean.com/swapify/face-swap-service
docker push registry.digitalocean.com/swapify/face-swap-service
```