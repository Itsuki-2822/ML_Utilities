# How to use Slack_notify

ここでは以下の2点について説明します：

This document explains the following two points:

- **Slack botのセットアップ**
  
- **発行されたWebhook URLを環境変数（VScode）に設定する**


## Slack apiを用いた、Slack Botのセットアップ

#### 1.  [Slack api](https://api.slack.com) にアクセス

#### 2.  右上の`Your apps`をクリック

  ![image](https://github.com/Itsuki-2822/ML_Utilities/assets/135577168/c0b2ae97-60ac-4ff8-975f-6ccf925095b7)

#### 3. 真ん中の画面真ん中の`Create an App`をクリック

![image](https://github.com/Itsuki-2822/ML_Utilities/assets/135577168/48972444-c128-4c52-91a0-6d18288daa47)

#### 4. `From scratch`を選択

![image](https://github.com/Itsuki-2822/ML_Utilities/assets/135577168/2ebb6a54-a3b5-46b9-b511-6db28743cec2)

#### 5. 作成する APP Name と 導入する Workspaceの設定
- `App Name` と `Pick a workspace to develop your app in`を設定
- 設定後 `Create App`をクリック

![image](https://github.com/Itsuki-2822/ML_Utilities/assets/135577168/943f4916-c59b-4758-8268-2dd9aefe6cf4)

#### 6. サイドバーの`Incoming Webhooks`をクリックして、`OFF`を`ON`に変更

![image](https://github.com/Itsuki-2822/ML_Utilities/assets/135577168/6195b842-ae19-4106-8890-e784592f7e0d)

#### 7. 画面下部の`Add New Webhook to Workspace`をクリック

![image](https://github.com/Itsuki-2822/ML_Utilities/assets/135577168/299ed31c-e81d-4617-81c0-40e578fb82ad)

#### 8. 作成した `Notify_bot` がアプリとして投稿することのできる投稿先チャンネルを指定
- 投稿先チャンネルを選択後、`許可する`をクリック

![image](https://github.com/Itsuki-2822/ML_Utilities/assets/135577168/f058c499-1f97-4e0b-a54c-52618f215d96)

##### 以上の手順が完了したら、Notify_botの設定が終わり、Webhook URLも取得できています。

![image](https://github.com/Itsuki-2822/ML_Utilities/assets/135577168/b3375ce2-5c53-4a83-9f88-8cb7308f1ee1)

## 発行されたWebhook URLを環境変数（VScode）に設定する
### 1. `.env`ファイルの作成:
- プロジェクトのルートディレクトリに `.env` ファイルを作成。
- `.env` ファイルに以下の内容を追加する（実際のWebhook URLに置き換えて）：
  ```bash
  SLACK_WEBHOOK_URL= 'your_webhook_url'
  ```
### 2. `settings.json` の編集
- コマンドパレットを開く
  - Mac（command + shift + P）
  - Windows（Ctrl + Shift + P）
- 検索Windowで「setting」を入力
- `Preferences: Open Settings(JSON)`を選択
  - `settings.json` に以下の設定を追加。これにより、Python拡張機能が `.env` ファイルを読み込むようになる：
    ```bash
    "python.envFile": "${workspaceFolder}/.env"
    ```
