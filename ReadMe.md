# このアプリケーションについて
このアプリケーションはコンソール上で**タスク管理**ができます。  

# 使い方
    $ taskcheck [option] [args]

# オプション
1. --add [日付のフォーマット] [タスクの中身]  
2. --show [[日付のフォーマット]..]

## add
* 新しいタスクを追加します。  
* 日付のフォーマットは`YYYY/MM/DD`です。  

## show
* 現在登録されているタスクのリストを出力します。  
* 引数に何も指定しない場合は全てのタスクを出力します。  
* 引数に日付のフォーマットを指定した場合、その日付のタスクを出力します。  
* 日付のフォーマットは `YYYY/MM/` か `YYYY/MM/DD` です。  

