# ML_Utilities
このリポジトリは、筆者が作成した機械学習関連の関数を保存するためのものです。

以下の手順では、リポジトリから`util`ディレクトリのみをクローンする方法を説明します。

## 手順

1. **クローン先のワークスペースに移動する**

    ```sh
    cd path/to/your_work_directory
    ```

2. **スパースチェックアウトでリポジトリを一時的にクローンする**

    ```sh
    git clone --filter=blob:none --sparse https://github.com/Itsuki-2822/ML_Utilities.git temp_clone
    ```

3. **クローンしたリポジトリに移動する**

    ```sh
    cd temp_clone
    ```

4. **`util`フォルダのみをスパースチェックアウトで取得する**

    ```sh
    git sparse-checkout set util
    ```

5. **`util`フォルダを自分のワークスペースにコピーする**

    ```sh
    cp -r util ../
    ```

6. **一時的にクローンしたリポジトリを削除する**

    ```sh
    cd ..
    rm -rf temp_clone
    ```

以上の手順で、`ML_Utilities`リポジトリの`util`ディレクトリのみをクローンして、ワークスペースにコピーすることができます。
