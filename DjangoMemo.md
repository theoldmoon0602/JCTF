# DjangoMemo

Djangoの知見をメモる

## 新しいプロジェクトを作るとき

```
django_admin startproject $(projectname)
```

## プロジェクトとは

　ぷろじぇくとのこと

## 新しいアプリケーションを作るとき

```
python manage.py startapp $(applicationname)
```

## アプリケーションとは

　モジュールのようなもの。プロジェクトに依存しない。


## views.py

 viewを管理する。多分ページ単位で、ページ名の関数を作る。そいつはHttpResponseオブジェクトを返す

## models.py

 modelを書く。modelは、django.db.Models.modelクラスを継承する

### modelの持つfield

 これらはDBに保存されるためちょっと独自な方を持つ。リファレンス見ろ

#### int

 models.Integerfield([default])

#### str

 models.CharField(max\_length)

### modelを有効化する

 modelを作ったらそれをprojectに伝える必要がある。
 $projectname/settings.pyのINSTALLED\_APPSに'$applicationname.apps.($Applicationnames)Config'を追加する。

 例えばpollsというアプリケーションなら、'polls.apps.PollsConfig'になる。

 それから、次を実行する。

```
python manage.py makemigrations
python manage.py migrate
```

## adminを作る

```
python manage.py createsuperuser
```

対話でadmin作れる


### adminでモデルを操作する

$applicationname/admin.pyを編集

```
admin.site.register($modelname)
```
する



