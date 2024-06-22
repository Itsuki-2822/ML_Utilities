from plyer import notification

def windows_send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon=None, 
        timeout=10, 
    )

#windows_send_notification('実行完了', 'プログラムの実行が完了しました。')