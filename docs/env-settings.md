# Environment Settings

## python runtime
- 3.11.9
```zsh
brew install pyenv
pyenv install 3.11.9
pyenv global 3.11.9 
# pyenv global # 3.11.9
```

## python virtual environment
- Java의 Maven/Gradle 의존성 관리와 비슷
```zsh
python -m venv .venv
source .venv/bin/activate
pip install requests numpy pandas
pip freeze > requirements.txt
# pip install -r requirements.txt 
# deactivate
```

