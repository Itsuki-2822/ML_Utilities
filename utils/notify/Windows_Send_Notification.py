from plyer import notification

def Windows_Send_Notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon=None, 
        timeout=10, 
    )

#Windows_Send_Notification('実行完了', 'プログラムの実行が完了しました')