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

 viewを管理する。多分ページ単位で、ページ名の関数を作る。そいつはHttpResponseオブジェクトかrenderの戻り値を返す
 他にもいろいろ返せる。HttpResponseRedirectとか。

### generic views

 ある程度のテンプレートとして、generic.viewというものが用意されている。例えば、
 
- generic.ListView
- generic.DetailView

 こいつらを継承したクラスを作ってやってごにょごにょすると、決まりきった形のページなら楽に作れる
 
 やっぱりいくつルールがある。

- urlsでいままでviews.<funcname>としていたところをviews.<ClassName>.as_view()としなくちゃいけない
- デフォルトではpkという名前のついた正規表現を受け取る
- デフォルトでは<modelname>_detail.htmlや<modelname>_list.htmlというテンプレートを読む。変えたければ、template_nameという変数に名前を代入する。

### reverse関数

 正規表現からurlを逆引きしてくる関数。大体はtemplateの中のurlと一緒。たとえば

```
reverse('polls:results', args=(3,))
```

　とすると、polls/3/resultsが帰ってくる

### get_object_or_404

　DBからオブジェクトをSELECTする。

```
obj = get_object_or_404(Question, pk=1)
```

 pkはprimary keyの略。Questionはモデルのクラス名（文字列ではなくてそのままクラスを突っ込む



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


