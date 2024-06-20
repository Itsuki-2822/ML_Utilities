#!/bin/bash

# 現在のディレクトリを保存
CURRENT_DIR=$(pwd)

# temp_cloneディレクトリの作成と移動
mkdir -p ../temp_clone
cd ../temp_clone

# リポジトリの初期化とリモート追加
git init
git remote add origin https://github.com/Itsuki-2822/ML_Utilities.git

# スパースチェックアウトの設定とpull
git sparse-checkout init --cone
git sparse-checkout set util
git pull origin main

# utilフォルダをコピー
cp -r util "$CURRENT_DIR/"

# 一時ディレクトリの削除
cd "$CURRENT_DIR"
rm -rf ../temp_clone
