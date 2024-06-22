import subprocess

def mac_send_notification(title, message):
    script = f'display notification "{message}" with title "{title}"'
    subprocess.run(["osascript", "-e", script])

#mac_send_notification('実行完了', 'プログラムの実行が完了しました。')