# ML_Utilities
このリポジトリは、筆者が作成した機械学習関連の関数を保存するためのものです。

This repository is for storing machine learning-related functions created by the author.

以下の手順では、リポジトリから`util`ディレクトリのみをクローンする方法と、`util`関数が更新されたときにその更新をあなたのワークスペースに反映させる手順を説明します。

The following steps explain how to clone only the `util` directory from the repository and how to update your workspace when the `util` functions are updated.

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


## 更新を反映させる手順 / Steps to Update

`util`関数が更新されたときに、その更新をあなたのワークスペースに反映させる手順を説明します。

The following steps explain how to update your workspace when the `util` functions are updated.

### 初回のみ行う手順 / One-Time Setup

1. **スクリプトを実行可能にする**

   **Make the script executable**

    ```sh
    chmod +x util/update_util.sh
    ```

### 更新手順 / Update Steps

`util`関数の更新を反映させるために、以下のコマンドを実行します。

To apply updates to the `util` functions, run the following command:

```sh
./util/update_util.sh
