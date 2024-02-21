conda create -n pully_env python=3.7
conda activate  pully_env
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyuul

source activate deepscreen_env
pip install -r requirements.txt
conda activate  deepscreen_env