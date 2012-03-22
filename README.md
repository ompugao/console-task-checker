Task Checker on Console Ver 0.2.3
---

# このアプリケーションについて
このアプリケーションはコンソール上で**タスク管理**ができます。  

# 使い方
    $ task [option] [args]

# オプション
1. create [日付のフォーマット] [タスクの中身]  
2. list [[日付のフォーマット]..]
3. update [[タスクの番号], [日付フォーマット], [タスクの中身]]
4. delete [[タスクの番号] or [all]..]

(※)Version 0.2.2にてオプション名の改変を行いました。  


## create
* 新しいタスクを追加します。  
* 日付のフォーマットは`YYYY/MM/DD`です。  

## list
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


![colorcode](https://img.skitch.com/20120318-bayfhndxu9bit8ikqthm6hxk97.png)


## update
* タスクをアップデートします。
* updateオプションをつけて、第二引数に何も指定しない場合は、現在存在しているタスクの番号を出力します。
* 第二引数、第三引数、第四引数にそれぞれタスクの番号、変更後の日付のフォーマット、変更後のタスクの中身を指定すると、
* 指定したタスクのアップデート（変更）ができます。


## delete
* タスクを削除します。
* deleteオプションをつけて、第二引数に何も指定しない場合は、現在存在しているタスクの番号を出力します。

![deletemode](https://img.skitch.com/20120321-psbcf99krcbpq1kf3cn5mtcigw.png)

* 第二引数にタスクの番号を指定すると、その番号のタスクがあるかチェックしたあと、その番号のタスクを削除します。
* 第二引数に`all`オプションを指定すると、現在存在している全てのタスクを削除するモードに入ります。
* このモードを使うときは十分気をつけてください。
* 注意 : **このモードを使用した後のトラブルについては一切責任を負えません。**


# Installation

    $ git clone git://github.com/alice1017/console-task-checker.git
	$ cd console-task-checker
	$ python setup.py build install



# License
MIT License  


- - - 

# Change Log
### Version 0.2.2
1. CRUD理論に則りオプション名を改変しました。
2. タスクを削除する機能を作製
