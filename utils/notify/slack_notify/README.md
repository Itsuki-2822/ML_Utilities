# How to use Slack_notify

このREADMEではSlack APIを用いて、Slackに通知を送る方法を

## Slack apiを用いた、Slack Botのセットアップ

[Slack api](https://api.slack.com)にアクセス

右上の「Your apps」をクリック

![image](https://github.com/Itsuki-2822/ML_Utilities/assets/135577168/c0b2ae97-60ac-4ff8-975f-6ccf925095b7)

真ん中の画面真ん中の[Create an App]をクリック

![image](https://github.com/Itsuki-2822/ML_Utilities/assets/135577168/48972444-c128-4c52-91a0-6d18288daa47)

[From scratch]を選択

![image](https://github.com/Itsuki-2822/ML_Utilities/assets/135577168/2ebb6a54-a3b5-46b9-b511-6db28743cec2)

- [App Name と Workspace]を設定
- 設定後 Create Appをクリック

![image](https://github.com/Itsuki-2822/ML_Utilities/assets/135577168/943f4916-c59b-4758-8268-2dd9aefe6cf4)

サイドバーの[Incoming Webhooks]をクリックして、OFFをONに変更

![image](https://github.com/Itsuki-2822/ML_Utilities/assets/135577168/6195b842-ae19-4106-8890-e784592f7e0d)

画面下部の[Add New Webhook to Workspace]をクリック

![image](https://github.com/Itsuki-2822/ML_Utilities/assets/135577168/299ed31c-e81d-4617-81c0-40e578fb82ad)

- 作成したNotify_bot がアプリとして投稿することのできる投稿先チャンネルを指定
- 許可するをクリック

![image](https://github.com/Itsuki-2822/ML_Utilities/assets/135577168/f058c499-1f97-4e0b-a54c-52618f215d96)

このようになっていたら、作成したNotify_botが投稿先チャンネルへのリンクが成功です。

![image](https://github.com/Itsuki-2822/ML_Utilities/assets/135577168/b3375ce2-5c53-4a83-9f88-8cb7308f1ee1)

お疲れ様でした。
