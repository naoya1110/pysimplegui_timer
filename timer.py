# パッケージのインポート
import PySimpleGUI as sg
import time
import winsound

t_set_text = "2:00"
t_text = t_set_text


# ウィンドウのカラーテーマ設定
sg.theme("DefaultNoMoreNagging") 

# 部品を作成
## CLOSEボタン
close_button_element = sg.Button(
                                button_text="CLOSE",    # 表示するテキスト
                                #button_color="blue",    # ボタンの色
                                size=(8,2),            # サイズ
                                font=('Arial',40),
                                key="CLOSE"             # キー：イベントの判定に必要
                                )

## START
start_button_element = sg.Button(
                                button_text="START",    # 表示するテキスト
                                #button_color="blue",    # ボタンの色
                                size=(8,2),            # サイズ
                                font=('Arial',40),
                                key="START"             # キー：イベントの判定に必要
                                )

## STOP
stop_button_element = sg.Button(
                                button_text="STOP",    # 表示するテキスト
                                #button_color="blue",    # ボタンの色
                                size=(8,2),            # サイズ
                                font=('Arial',40),
                                key="STOP"             # キー：イベントの判定に必要
                                )

## RESET
reset_button_element = sg.Button(
                                button_text="RESET",    # 表示するテキスト
                                #button_color="blue",    # ボタンの色
                                size=(8,2),            # サイズ
                                font=('Arial',40),
                                key="RESET"             # キー：イベントの判定に必要
                                )

time_text_element = sg.Text(text = t_text,
                             size = (7,1),
                             font=('Arial',300),
                             background_color="white",
                             text_color = "green",
                             justification= "center",
                             key="TIME TEXT")



# アプリのレイアウトを設定，部品を2次元配列で配置
layout = [[time_text_element],
                  [start_button_element, stop_button_element, reset_button_element, close_button_element]]

# ウィンドウを設定
window = sg.Window(
                    title="Timer App",  # ウィンドウのタイトル
                    layout=layout,              # レイアウト
                    size=(1200, 650)             # ウィンドウの大きさ
                    )

is_started = False
is_stopped = False
is_beeped = False


mm, ss = t_set_text.split(":")
t_set = 60*int(mm)+int(ss)
t_remain = t_set

# 無限ループ
while True:
    
    # アプリ内で発生したイベントを読み取る
    event, values = window.read(timeout=20)
    
    # アプリの終了判定，CLOSEボタンが押される，または×ボタンが押される
    if event == "CLOSE" or event == sg.WIN_CLOSED:
        break
    
    if event == "START":
        is_started = True
        t_start = time.time()
    
    if is_started:
        t_elapsed = time.time() - t_start
        t_remain = t_set - t_elapsed
        
        if t_remain >= 0:
            text_color = "green"
        else:
            text_color = "red"
            t_remain = abs(t_remain)
            if not is_beeped:
                winsound.Beep(500, 500)
                is_beeped = True
        
        print(t_remain, t_set, t_elapsed)
        t_text = f"{int(t_remain//60)}:{str(int(t_remain%60)).zfill(2)}"
        
        time_text_element.update(t_text, text_color=text_color)
    
    if event=="STOP":
        is_started = False
        is_finished = True
    
    if event == "RESET":
        is_started = False
        is_finished = False
        is_beeped = False
        t_remain = t_set
        text_color = "green"
        time_text_element.update(t_set_text, text_color=text_color)
        
    
    time.sleep(0.1)
        

# アプリを終了（ウィンドウを閉じる）
window.close()