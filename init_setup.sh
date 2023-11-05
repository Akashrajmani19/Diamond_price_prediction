echo [$(date)]: "Start"

echo [$(date)]: "Creating env with python 3.8 version"

conda create --prefix ./env python=3.8 -y

echo [$(date)]: "Activating the environment"

conda activate ./env

echo [$(date)]: "Installing the dev requirements"

conda install -r requirements.txt

echo [$(date)]: "END"
