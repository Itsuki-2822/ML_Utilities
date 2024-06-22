# Explanation of how to import 
このREADMEでは筆者が作成したカスタムモジュールをインポートする方法について説明します。

In this README, we explain how to import custom modules created by the author.

まず、下記のようなディレクトリ構造になっていること確認してください。

First, make sure that your directory structure is as follows:

```bash
your_repository/
│
├── utils/
│   ├── notify/
│   │   ├── Mac_Send_Notification.py
│   │   └── Windows_Send_Notification.py
│   ├── PermutationFeatureSelector.py
│   ├── Compare_Categorical_Columns.py
│   ├── Cyclical_Encoder.py
│   ├── Find_Significant_Categories.py
│   ├── Adversarial_Validator.py
│   ├── FeatureImportanceVisualizer.py
│   └── update_utils.sh
│
├── scripts/
│   └── your_sample_script.py
└── ...
```
### カスタムモジュールのインポート / Import Custom Modules
```python
import sys
sys.path.append('../utils')

from PermutationFeatureSelector import PermutationFeatureSelector
from Compare_Categorical_Columns import Compare_Categorical_Columns
from Cyclical_Encoder import Cyclical_Encoder
from Find_Significant_Categories import Find_Significant_Categories
from Adversarial_Validator import Adversarial_Validator
from FeatureImportanceVisualizer import FeatureImportanceVisualizer
```
