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
│   ├── compare_categorical_columns.py
│   ├── cyclical_encoding.py
│   ├── find_significant_categories.py
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
from compare_categorical_columns import compare_categorical_columns
from cyclical_encoding import cyclical_encoding
from find_significant_categories import find_significant_categories
from Adversarial_Validator import Adversarial_Validator
from FeatureImportanceVisualizer import FeatureImportanceVisualizer
```
