# TwitterFlamingPrevention

Twitter初心者向けの炎上防止アプリ

【既存の機能】
http://見守り.jp/

既存のツイッターclientアプリの中のSNS炎上報知器に注目
1. 公開設定チェック
2．NGワードのチャック
3. 炎上感知
4. 外部アカウントとの比較
5. 個人情報検出

【追加機能（予定）】
6. 相互チェックの上で投稿する機能
→そもそも炎上するかしないかセルフチェックができるような枠組み

が必要
どのようなものが過去に炎上したのかを知る指標に基づいて自己また

は相互チェックを可能にする



【使い方】
・Requirementsがまだかけてませんが, 
- mecab-python
- twitter-python
- Nude
が追加で必要です。

・tweetforbeginner.pyを起動

【改善点】
・既存のアプリは形態素を考慮しておらず、NGワード辞書追加が面倒
→形態素と極性スコアを同時にとるようにし、NGワードの取得を容易

にした。(また極性スコアによるNG判定も予定していた)

・画像に対するケアがなかったので、画像についての炎上防止を行う

機能を追加。様々なものが考えられるが、公序良俗に反する恐れのあ

るものを検出。

・チェック項目のボックスを追加し、これらを全て✔しないと投稿が

できない仕様になっている。
(友人のアカウントにツイート内容を送り、本来ならばそこで✔をして

もらう仕様にする予定でした。)


