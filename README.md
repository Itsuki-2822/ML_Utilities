# ML_Utilities
このリポジトリは、筆者が作成した機械学習関連の関数を保存するためのものです。

This repository is for storing machine learning-related functions created by the author.

ここでは以下の2点について説明します：

This document explains the following two points:

- **リポジトリから`utils`ディレクトリのみをクローンする方法**

  **How to clone only the `utils` directory from the repository**
  
- **`util`関数が更新されたときにその更新をあなたのワークスペースに反映させる方法**

  **How to update your workspace when the `utils` functions are updated**

## ディレクトリを追加する手順 / Steps to Add a Directory

1. **クローン先のワークスペースに移動する**
   
   **Move to the target workspace**

    ```sh
    cd path/to/your_workspace
    ```

2. **スパースチェックアウトでリポジトリを一時的にクローンする**
   
   **Temporarily clone the repository with sparse checkout**

    ```sh
    git clone --filter=blob:none --sparse https://github.com/Itsuki-2822/ML_Utilities.git temp_clone
    ```

3. **クローンしたリポジトリに移動する**
   
   **Move to the cloned repository**

    ```sh
    cd temp_clone
    ```

4. **`utils`フォルダのみをスパースチェックアウトで取得する**
   
   **Get only the `utils` folder with sparse checkout**

    ```sh
    git sparse-checkout set utils
    ```

5. **`utils`フォルダを自分のワークスペースにコピーする**
   
   **Copy the `utils` folder to your workspace**

    ```sh
    cp -r utils ../
    ```

6. **一時的にクローンしたリポジトリを削除する**
   
   **Delete the temporarily cloned repository**

    ```sh
    cd ..
    rm -rf temp_clone
    ```

以上の手順で、`ML_Utilities`リポジトリの`utils`ディレクトリのみをクローンして、ワークスペースにコピーすることができます。

By following these steps, you can clone only the `utils` directory from the `ML_Utilities` repository and copy it to your workspace.


## 更新を反映させる手順 / Steps to Update
更新の反映はスクリプトファイルを用いて行います。ですが、ここではスクリプトファイルについての詳しい説明は省きます。

The updates are applied using a script file. However, a detailed explanation of the script file is omitted here.

### 初回のみ行う手順 / One-Time Setup

1. **スクリプトを実行可能にする**

   **Make the script executable**

    ```sh
    chmod +x utils/update_utils.sh
    ```

### 更新手順 / Update Steps

`utils`の更新を反映させるために、以下のコマンドを実行します。

To apply updates to the `utils` functions, run the following command:

```sh
./utils/update_utils.sh
```

以上の手順で、ML_Utilitiesリポジトリのutilsディレクトリの更新を、ワークスペースに反映させることができます。

By following these steps,The updates applied.
