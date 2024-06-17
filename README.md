# ML_Utilities
このリポジトリは筆者が作成したML関係の関数を保存しておくリポジトリである。

以下はこのリポジトリの`util`ディレクトリのみを使用者のワークスペースにクローンする方法について手順を明記したものである。

## How to
#### クローン先のワークスペースに移動
  
`cd path/to/your_work_directory`

#### temp_cloneに筆者のリポジトリの util フォルダをスパースチェックアウトでクローンする

`git clone --filter=blob:none --sparse https://github.com/Itsuki-2822/ML_Utilities.git temp_clone`

`cd temp_clone`

`git sparse-checkout set util`

#### util フォルダを自分のワークスペースにコピーする

`cp -r util ../`

#### temp_cloneを削除する

`cd ..`

`rm -rf temp_clone`
