import subprocess

def Mac_Send_Notification(title, message):
    script = f'display notification "{message}" with title "{title}"'
    subprocess.run(["osascript", "-e", script])

#Mac_Send_Notification('実行完了', 'プログラムの実行が完了しました。')