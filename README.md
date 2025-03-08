# bioinspired
Repository for the bio-inspired algorithms class

# Enviroment
```bash
source env/bin/activate
```

# Add Dep
```bash
poetry add $(pip freeze --local | grep -v '^\-e' | cut -d = -f 1)
```

# Install Dep
```bash
poetry install
```

# Run App
```bash
streamlit run ./app.py
```