# Agent Skillsでの利用

このディレクトリでは、日本語の競技クイズを作成する `generate-quiz` を配布しています。あわせて、生成した問題をLaTeX問題集として組版する付属スキル `quiz-book-latex` も収録しています。どちらも[Agent Skills](https://agentskills.io) 形式におおむね準拠しています。

## generate-quiz

日本語の競技クイズを作成する、このリポジトリの中心となるスキルです。共通の作問仕様・出力形式は[リポジトリのREADME](../README.md)を参照してください。

### インストール

[skills CLI](https://github.com/vercel-labs/skills) でインストールできます。

```bash
npx skills add Watson496/generate-quiz
```

手動でインストールする場合は、リポジトリのルートで次を実行します。

```bash
cp -r skills/generate-quiz ~/.agents/skills/
```

プロジェクト単位で使う場合は `<プロジェクト>/.agents/skills/` に置きます。他のAI agentでは、それぞれのドキュメントに従ってskillの配置先に置いてください。

Web検索（裏取りに必須）と、Pythonスクリプトを実行できるシェル（標準ライブラリのみ使用）が必要です。

### 使い方

AI agentとのセッションで作問を依頼します。条件を指定しなければ、題材を重み付き乱択で選んで1問作ります。

```text
/generate-quiz
```

主題・問題数・文字数などを指定できます。文字数は「以内・以下・ちょうど・厳守」をハード制約、「前後・程度・くらい」をソフト目標として扱い分けます。

```text
/generate-quiz 音楽を主題に3問
/generate-quiz 60文字以内で1問
/generate-quiz 100文字前後で1問
```

自然言語で「クイズを作って」「早押しクイズを1問」のように依頼しても自動起動します。過去問を渡すと、それを履歴として題材選択に反映します（古い順に並べ、末尾を最新として読みます）。

```text
以下は古い順に並べた過去問です。この履歴を考慮して次の1問を作ってください。

問題：……
解答：……
```

### 初期確認

新しいセッションで無指定の作問を依頼し、同梱Pythonスクリプトによる抽選とWebでの裏取りが実行されることを確認します。出力内容は[作問結果の確認](../README.md#作問結果の確認)に従って確認してください。

### 配布ファイル

```text
generate-quiz/
  SKILL.md        作問の工程制御
  references/     ファセットカタログと3つの仕様
  scripts/        履歴補正付き乱択・文字数判定・ファセットノード抽出
```

`SKILL.md` は工程制御、`references/` は詳細な定義と判断基準を担います。ファセットカタログは1ファイル最大約260KBあるため、作問時には `scripts/facet_node.py` で必要なノードのブロックだけを取り出します。

## quiz-book-latex

`generate-quiz` で作成したMarkdown群を、問題一覧と問別解説を備えたLaTeX問題集へ組版する付属スキルです。

### インストール

手動でインストールする場合は、リポジトリのルートで次を実行します。

```bash
cp -r skills/quiz-book-latex ~/.agents/skills/
```

プロジェクト単位で使う場合は `<プロジェクト>/.agents/skills/` に置きます。他のAI agentでは、それぞれのドキュメントに従ってskillの配置先に置いてください。

Pandoc 3以降、LuaLaTeX、`latexmk`、Biberが必要です。

### 使い方

`generate-quiz` 形式のMarkdownを格納したディレクトリと、出力先を指定して問題集の作成を依頼します。問題・解答一覧、全付帯情報を含む問別解説、印刷可能なページ参照とPDF内リンク、BibLaTeXによる参考文献を備えたLaTeXプロジェクトとPDFを作成します。

```text
quiz-book-latexを使って quizzes/ から quiz-book/ に問題集を作って
```

### 配布ファイル

```text
quiz-book-latex/
  SKILL.md        問題集生成の工程制御
  agents/         UI表示用メタデータ
  assets/         LaTeXプロジェクトのテンプレート
  references/     入力Markdownの形式
  scripts/        入力検証・変換・PDF生成
```
