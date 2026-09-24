---
name: generate-quiz
description: 日本語の競技早押しクイズ（SC型・OV型）を新規作成する。ファセット分類と履歴補正による題材の重み付き乱択、Web検索に基づく難易度・裏取り・手掛かり・成立性の評価、許容度曲線による文字数調整までを行い、判断根拠を添えて定型出力する。「クイズを作って」「問題を作って」「早押しクイズ」「○文字以内で1問」「この履歴を踏まえて次の問題」などで自動起動。
argument-hint: <作問条件（主題・問題数・文字数・履歴など。すべて省略可）>
---

# 役割

日本語の競技早押しクイズを新規作成する。ユーザーの明示的な指定は既定値・既定規則より優先する。指定が両立不能でない限り事前質問をせず、直ちに作問する。明示的な改稿依頼では題材を差し替えず、既存問題を改稿する。

ユーザーが対象プレイヤー層を別に指定しない限り、題材領域、候補探索、weight、難易度、中核性・代表性、準一意性、用語理解、知名度、解答、正誤判定を含む全判断を日本語文化圏基準で行う。外国の分野や地域が主題でも、日本語文化圏での共有度、重要性、学習上の位置に基づいて判断する。

`references/`の各仕様は背景資料ではなく、指定された工程で必ず適用する規範である。記憶や一般知識で代替しない。

以下の`$SKILL_DIR`は、このskillのディレクトリを指す。

# 既定値

- 問題数：1問
- 主題：指定がなければファセットと履歴から重み付き乱択
- 難易度：当該分野（大学で専攻として学ぶ分野に相当する広さ）を継続的に学び始めて1〜2年以内の人には基礎・概説知識として正答を期待できる一方、その分野を特に学んでいない一般的な日本語話者には通常は正答を期待しにくい水準
- 長さ：80文字付近の許容度を最大とし、典型的な広がりがおおむね20文字、長い側にやや裾を引く分布
- 構文：題材と正答範囲に応じたSC型またはOV型

# 開始時に読む仕様

作問へ着手する前に、次を全文読む。

1. [`references/workflow_spec.md`](references/workflow_spec.md)
2. [`references/work_state_spec.md`](references/work_state_spec.md)

複数問でも一問でも、`workflow_spec.md`のステップを一問ずつ完了させる。作業状態は`work_state_spec.md`の単位で保持し、解答対象を変更したときは旧対象の状態を引き継がない。

# 担当ごとに読む仕様

判断は、工程のステップごとに起動する担当が行う。各担当が読む仕様は担当表[`references/roles.json`](references/roles.json)で定め、依頼文で指定する。担当は、判断を始める前に指定された仕様を全文読む。

出力直前に全仕様を読み直して済ませず、各仕様を必要とする判断へ入る前に読む。作業状態の検査単位を使い、適用済みかを記録する。

# 必須ツール

- 同梱スクリプトにはPython 3.14以上を使用する。
- 毎問Web検索を使う。検索手段が一切使えない場合は、内部知識で代替せず作問を中止する。
- ステップの構成と依頼文、重み付き乱択、履歴補正、文字数判定、作業状態の構造検査は、必ず同梱スクリプトを実行する。
  - ステップの構成と依頼文：`scripts/assignment_plan.py`
  - ファセットの抽選：`scripts/weighted_pick.py`
  - 題材候補の抽選：`scripts/topic_pick.py`
  - 文字数と採否：`scripts/length_check.py`
  - ファセットノードの取得：`scripts/facet_node.py`
  - 作業状態の構造検査：`scripts/work_state_check.py`
- `python3`の実行に失敗したら再試行する。再試行でも失敗した場合は作問を中止する。ユーザーが明示的に許可した場合だけ、重み付き選択を代替できる。乱数シードは設定・表示しない。

各スクリプトの終了コードは、`0`が正常、`1`が候補なし・改稿・状態修正が必要、`2`が入力や呼出しの不備である。`2`では呼出し方を修正して再実行する。

# スクリプトの呼出し

ステップの構成と、統括役と担当への依頼文は、担当表から決める。

```bash
python3 "$SKILL_DIR/scripts/assignment_plan.py" steps
python3 "$SKILL_DIR/scripts/assignment_plan.py" coordinate 3
python3 "$SKILL_DIR/scripts/assignment_plan.py" assign exploration
```

ファセットカタログは全文を読まず、必要なブロックだけを取得する。

```bash
python3 "$SKILL_DIR/scripts/facet_node.py" 'subject::7'
python3 "$SKILL_DIR/scripts/facet_node.py" --children 'place::(1/9)'
python3 "$SKILL_DIR/scripts/facet_node.py" --grep '音楽'
```

抽選は、候補ごとの基礎weightと履歴距離をJSONで渡す。

```bash
python3 "$SKILL_DIR/scripts/weighted_pick.py" <<'JSON'
{"candidates":[
  {"key":"subject::78","label":"音楽","base_weight":3.2,"history_distances":[2]},
  {"key":"subject::79","label":"レクリエーション．娯楽．スポーツ","base_weight":2.4}
]}
JSON
```

題材候補の抽選には、探索状態のJSONを`topic_pick.py`へ渡す。このスクリプトは探索状態にある選択対象のIDと抽選用JSONの候補IDが一致することを検査する。題材品質ゲートで候補を棄却した場合は、その候補の`quality_rejection_reason`に理由を記録し、記録済みの全候補IDを`--exclude <key>`で渡して再抽選する。探索段階の`disposition`は書き換えない。ファセットの抽選には`weighted_pick.py`を使う。

```bash
python3 "$SKILL_DIR/scripts/topic_pick.py" state.json --json candidates.json
```

問題文の版ごとに文字数判定の`DRAW`を保持する。同じ版を監査するときは`--draw`へ同じ値を渡し、再抽選しない。

作業状態のJSON manifestは、工程に応じて次のいずれかで検査する。

```bash
python3 "$SKILL_DIR/scripts/work_state_check.py" --stage intersection-checkpoint state.json
python3 "$SKILL_DIR/scripts/work_state_check.py" --stage discovery-progress state.json
python3 "$SKILL_DIR/scripts/work_state_check.py" --stage discovery state.json
python3 "$SKILL_DIR/scripts/work_state_check.py" --stage selection state.json
python3 "$SKILL_DIR/scripts/work_state_check.py" --stage generation-start state.json
python3 "$SKILL_DIR/scripts/work_state_check.py" --stage difficulty state.json
python3 "$SKILL_DIR/scripts/work_state_check.py" --stage generation state.json
python3 "$SKILL_DIR/scripts/work_state_check.py" --stage audit state.json
python3 "$SKILL_DIR/scripts/work_state_check.py" --stage final --output completed.md state.json
```

# 最終出力

最終出力には、`work_state_spec.md`で定めた限定入力だけを使い、`output_structure_spec.md`に従う。内部のweight、コード、抽選過程、不採用候補、予定命題、検索過程、監査の往復、スクリプトの生出力を表示しない。

# 完了条件

次をすべて満たしたときだけ、一問を確定する。

- 生成側の全検査単位が完了している。
- 独立監査の全検査単位が合格している。
- 現行問題文の版について、文字数判定と作業状態の検査に合格している。
- 最終出力が限定入力と一致し、検討過程を含まない。

確定した問題を履歴へ加えてから、次の問題を始める。指定された問題数の全問を確定して履歴へ加えたときに完了とする。
