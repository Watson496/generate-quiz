# ChatGPTでの利用

このディレクトリでは、日本語の競技クイズを作成する `generate-quiz` のChatGPT向け設定を配布しています。

## generate-quiz

[generate-quiz/](generate-quiz/) のInstructionsとKnowledgeをGPTの編集画面へ登録します。共通の作問仕様・出力形式は[リポジトリのREADME](../README.md)を参照してください。

### セットアップ

GPTの名称は任意に設定できます。編集画面で、次の3つを設定します。

Instructions欄には [generate-quiz/Instructions.txt](generate-quiz/Instructions.txt) の内容をそのまま貼り付けます。設計目標は6,500文字以内、編集画面の上限は8,000文字で、現在は3,799文字（UTF-8で9,951バイト）です。

Knowledgeには `generate-quiz/knowledge/` の18ファイルだけを登録します。元のYAML、ZIP、旧プロンプト、参考論文、評価ファイルは登録しません。ファセットカタログは、元YAMLの分類内容・コード・階層・注記を保ったまま、GPTが親ノードと直接の子を一度に取得しやすいMarkdownブロックへ変換したものです。subjectのみ最上位コードごとに9分割し、place・time・typeは各1ファイルにしています。

登録するファイルは次のとおりです。

```text
facet_index.md
facet_place.md
facet_subject_0.md
facet_subject_1.md
facet_subject_2.md
facet_subject_3.md
facet_subject_5.md
facet_subject_6.md
facet_subject_7.md
facet_subject_8.md
facet_subject_9.md
facet_time.md
facet_type.md
output_structure_spec.md
quiz_generation_spec.md
selection_and_history_spec.md
verification_and_judging_spec.md
work_state_template.md
```

Capabilitiesは「Web Search」と「Code Interpreter & Data Analysis」を有効にします。Web Searchは毎問の裏取り、手掛かり単位の比較対象・対抗候補探索、情報選択の確認、難易度の校正に使います。Code InterpreterのPythonは、ファセットと題材の重み付き乱択、履歴補正、文字数の計測と確率的な採否判定、作業状態の確定的な検査に使います。

### 使い方

条件を指定しなければ、題材を重み付き乱択で選んで1問作ります。

```text
問題を作って
```

主題・問題数・文字数などを指定できます。文字数は「以内・以下・ちょうど・厳守」をハード制約、「前後・程度・くらい」をソフト目標として扱い分けます。

```text
音楽を主題に1問作って
60文字以内で1問作って
100文字前後で1問作って
```

過去問を渡すと、それを履歴として題材選択に反映します。順序を指定しなければ、上から古い順・末尾を最新として読みます。

```text
以下は古い順に並べた過去問です。この履歴を考慮して次の1問を作ってください。

問題：……
解答：……
```

### 初期確認

新しいPreviewチャットで無指定の作問を依頼し、Pythonの抽選とWebでの裏取りが実行されることを確認します。出力内容は[作問結果の確認](../README.md#作問結果の確認)に従って確認してください。

### 配布ファイル

```text
generate-quiz/
  Instructions.txt  GPTのInstructions欄に貼り付ける工程制御
  knowledge/        Knowledgeへ登録する18ファイル
```

`Instructions.txt`は工程、状態遷移、各段階の完了条件を担います。`knowledge/`は詳細な定義と判断基準、作業状態の定型を担います。Knowledgeの内訳は、ファセット索引と分類カタログの13ファイル、題材選定・履歴、問題文生成、裏取り・正誤判定、最終出力の4つの仕様、および作業状態の定型です。
