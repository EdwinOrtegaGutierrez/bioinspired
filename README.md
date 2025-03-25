# bioinspired
Repository for the bio-inspired algorithms class

# Enviroment
```bash
source env/bin/activate
```

# Add Dep
```bash
python -m pip freeze > requirements.txt
```

# Install Dep
```bash
sudo pip3 install -r requirements.txt
```

# Run App
```bash
streamlit run ./🏠_Home.py --server.port=8080 --server.address=0.0.0.0
```

# Deploy
## Create Image
```bash
sudo docker build -t webapp-streamlit .
```
## Run Image as Container
```bash
sudo docker run -p 8080:8080 webapp-streamlit
```