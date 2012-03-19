Task Checker on Console Ver 0.2.1
---

# このアプリケーションについて
このアプリケーションはコンソール上で**タスク管理**ができます。  

# 使い方
    $ taskcheck [option] [args]

# オプション
1. --add [日付のフォーマット] [タスクの中身]  
2. --show [[日付のフォーマット]..]

(※)現在まだdeleteオプションを実装できてません  

## add
* 新しいタスクを追加します。  
* 日付のフォーマットは`YYYY/MM/DD`です。  

## show
* 現在登録されているタスクのリストを出力します。  
* 引数に何も指定しない場合は全てのタスクを出力します。  
* 引数に日付のフォーマットを指定した場合、その日付のタスクを出力します。  
* 日付のフォーマットは `YYYY/MM/` か `YYYY/MM/DD` です。  

- - - 

### 色設定
* 期限が0日(つまり当日)の場合は`Red`
* 期限が0以下（つまり期限がきれている)場合は`Yellow`
* 期限が3日以内の場合は`Magenta`
* 期限が一週間以内の場合は `Cyan`
* 期限が一ヶ月以内の場合は`Green`
* 上記以外は全て`White`


![showmode](https://img.skitch.com/20120318-bayfhndxu9bit8ikqthm6hxk97.png)


# License
MIT License  
