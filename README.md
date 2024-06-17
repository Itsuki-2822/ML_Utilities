# ML_Utilities
このリポジトリは、筆者が作成した機械学習関連の関数を保存するためのものです。

This repository is for storing machine learning-related functions created by the author.

以下の手順では、リポジトリから`util`ディレクトリのみをクローンする方法を説明します。

The following steps explain how to clone only the `util` directory from the repository.

## 手順 / Steps

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

4. **`util`フォルダのみをスパースチェックアウトで取得する**
   
   **Get only the `util` folder with sparse checkout**

    ```sh
    git sparse-checkout set util
    ```

5. **`util`フォルダを自分のワークスペースにコピーする**
   
   **Copy the `util` folder to your workspace**

    ```sh
    cp -r util ../
    ```

6. **一時的にクローンしたリポジトリを削除する**
   
   **Delete the temporarily cloned repository**

    ```sh
    cd ..
    rm -rf temp_clone
    ```

以上の手順で、`ML_Utilities`リポジトリの`util`ディレクトリのみをクローンして、ワークスペースにコピーすることができます。

By following these steps, you can clone only the `util` directory from the `ML_Utilities` repository and copy it to your workspace.
