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

## urls.py

 コントローラになる。
 urlpatternsにurlを突っ込む。

 url(正規表現, 読み込むview, name=)

### pythonの正規表現

 rプレフィクス付きの文字列
 
```
  r'^$'
```

 名前付きのパターン。
```
  r'?P<name>pattern'
```

 名前付きパターンはviewで受け取れる

```
  def viewfunc(request, name):
```

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
する。ちゃんとmodelをimportしておくこと


## template

 $applicationdirectory/templates

 を作る

 この中にテンプレートを書く。

 django.template.loader.get\_templateに、templatesより下の.htmlの名前を書く

 作ったtemplateからrenderを読んでHttpResponseに渡す。第二引数に辞書を渡すとテンプレ内で使える変数になる


