# 作問中の状態

## 目的

作問中の調査記録と、人間へ示す最終出力を分ける。生成と監査は同じ検査単位を使い、必要な判断が完了したことを確認してから次の工程へ進む。

引用、推論、候補比較はMarkdownで保持する。ID、問題文の版、採否、完了状態、参照関係はJSON manifestでも保持し、`scripts/work_state_check.py`で確定的に検査する。JSON manifestだけを判断根拠にせず、対応するMarkdownの内容を生成担当と監査担当が評価する。

## ファセットの交差領域

ファセット選択後、題材探索前に4軸の正規ノードキーと交差領域の確認記録をJSONへ保存し、`work_state_check.py --stage intersection-checkpoint`で検査する。確認記録には、開いた資料のURL、資料中に実名がある異なる候補二つ以上と各資料のURL、うち一件以上の初級学習資料と扱いの根拠、交差領域の広さを判断した理由、成立の判定を含める。委譲機能の有無は`execution.delegation_available`に記録する。別agentが確認する場合は、その正規IDと起動時の記録を`execution.agents`と`execution.assignment_log`へ保存する。委譲機能がない場合は、利用できない理由を記録して親agentが確認する。形式検査は資料の独立性や判断の妥当性を保証しない。

## 題材候補の探索状態

現在の問題番号について、次を保持する。

- 選択した4軸の正規ノードキー
- 資料から分けた下位領域、そこに含まれる解答対象の種類、各領域を探索したか
- 各領域で候補名を含めず入口を探した検索語・観点と、候補名から近接対象を探した経路
- 本文を開いた資料のURL・確認箇所と、そこで発見した候補
- 各候補の名称の使用箇所（資料で名称を確認できず除外した候補を除く）、選択範囲への所属理由、発見元、選択対象か、選択対象なら近接探索の記録
- 別経路の探索で各下位領域に開いた入口、元の探索と異なる観点、得た候補、親agentが元の資料と台帳を照合した結果
- 探索完了の反証調査で使った観点・検索語・開いた資料、得た候補と未探索経路の処理結果
- 各選択対象の代表説明、正答名・許容別名、説明案ごとの名称形成の分析、解答露出の予備判定
- 探索段階で選択対象となるか、除外する場合はその理由
- 抽選後に題材品質ゲートで棄却した場合は、満たせなかった条件
- 新しい有力候補が増えなくなったか

一つの解答対象を棄却しても、この状態は同じ問題番号で題材を再選定するために保持する。棄却した対象に固有の引用、推論、問題文、監査履歴は、新しい解答対象の作業状態へ渡さない。

題材候補の探索状態は最終出力へ含めない。探索が飽和したら露出予備検査の前に`work_state_check.py --stage discovery`で検査する。

探索状態は、題材を抽選する前に `topic_pick.py` へ渡す。入口には本文を開いたURL、`opened: true`、確認箇所を`access_note`として記録する。下位領域の`source_searches`には、候補名を含めない入口探しを`mode: open`、既知候補からの近接探索を`mode: nearby`として記録する。資料で名称を確認できず除外する候補を除き、`name_use_note`には名称の使用箇所を記す。`facet_membership_reason`には四軸の範囲に属すると判断した理由を記す。選択対象の`expansion_searches`には近接探索の検索先・調べた関係・得た候補IDを残す。検査を通った後で候補を追加した場合は、その候補からも探索を展開し、再度検査する。

`independent_review`には下位領域IDごとに、最初の探索と異なる観点、候補名を含めない検索語、別経路で開いた入口IDと候補ID、親agentが照合した元の入口IDと結果を記録する。`saturation_challenge`には別の立場・用途からの検索、開いた入口ID、得た候補ID、未探索経路の処理と完了状態を残す。形式検査の合格は資料の内容と記録が対応することや、探索の十分さを保証しない。

`disposition`は探索段階で選択対象となるかを表す。抽選後に題材品質ゲートで棄却した候補は`eligible`のまま、満たせなかった条件を`quality_rejection_reason`へ記録する。再抽選では、この記録がある全候補のIDを`topic_pick.py --exclude`へ渡す。

露出予備検査の`formations`は名称と代表説明の組合せごとに一件作り、対応する代表説明の添字を`description_index`で記録する。調べた説明案と許容名称の各組合せを照合し、一つの説明で名称を形成できても、ほかの説明で形成できなければ選択対象に残す。`status: passed`は露出がないという意味ではなく、抽選前に回避不能な露出を立証できなかったことを表す。`unavoidable_exposure`で除外するには、異なる中核的な代表説明を少なくとも二つ調べ、そのすべてで正答名または許容別名を対象固有知識なしに形成できる必要がある。形式検査は説明の妥当性を保証しないため、候補名を言い換えただけの説明を複数並べて除外しない。

## 解答対象ごとの作業状態

解答対象を選んだら、その対象だけに属する作業状態を新しく作る。次を互いに識別できる形で保持する。

- 解答対象とユーザーの作問条件
- 資料、引用箇所、確認状態
- 予定命題と実現命題
- 手掛かり候補と採否
- 難易度の二つの参照集団
- 命題理解に必要な専門用語
- 解答、別解、正誤判定
- 問題文の各版
- 問題文の構造、表現、解答露出、文字数判定
- 監査結果と未解決の指摘
- 最終出力を組み立てるための限定入力

資料には資料IDを付け、同じ資料の引用箇所を別に識別する。命題と手掛かりにはそれぞれIDを付け、根拠となる資料と引用箇所をIDで参照する。

## 問題文の版

問題文の表現を変更するたびに版を更新する。文字数判定、実現命題、前フリ・落とし・後限定、表現品質、解答露出、監査結果には対象とした版を付ける。

言い換えだけで真偽条件が変わらない命題は同じIDを維持する。主体、関係、条件、時点、断定の強さなどが変わり、真偽条件が変わった場合は新しい命題IDを付ける。

同じ手掛かり情報の表現だけを変えた場合は、手掛かりIDを維持する。情報を差し替えた場合と、複数の手掛かりを統合・分割した場合は、新しい手掛かりIDを付ける。

旧版に対する文字数判定、表現評価、解答露出検査、監査結果を新しい版へ流用しない。

## 現行状態と不採用履歴

生成、修正、監査の間で常時渡す現行状態は、次に限る。

- 採用中または未評価の命題、手掛かり、資料
- 現行問題文と、その版に対応する検査
- 未解決の監査指摘

不採用になった命題、手掛かり、表現は、ID、不採用理由、再検討できる条件、必要な場合の資料IDだけを再試行防止用の記録へ残す。旧問題文の全文、解消済みの監査説明、使わなくなった引用全文を常時引き継がない。

詳細を保存できる環境では、必要になったときだけ保存先から読み直す。

## 生成と監査に共通する検査単位

生成側と監査側は、次を同じ単位で検査する。

- 各実現命題
- 難易度の二つの参照集団
- 命題理解に必要な各専門用語
- 各手掛かりの中核性・代表性、準一意性、知名度
- 複数の手掛かり順序案
- 別解候補と各正誤判定
- 解答露出
- 前フリ、落とし、後限定
- 完成稿の質問表現とSC型・OV型の別、核名詞句、直前の落とし、落としが対象を直接説明する理由
- 連用中止・テ形接続の全箇所と、左右の述定、意味上の主体、時制・相、接続関係
- 日本語としての自然さ
- 意味の伝わりやすさ
- 確認した内容との一致
- 前から読んだときの理解しやすさ
- 文字数判定
- 最終出力の各必須要素

見出しが存在することだけで、その内部の検査単位を完了扱いにしない。

連用中止・テ形接続がない場合も、完成稿を走査した結果として「該当なし」と記録する。接続がある場合は、左右の述定をそれぞれ省略のない形に戻し、並列、継起、理由、対立、手段、条件のどの関係が成立するかと、その判断理由を一箇所ずつ記録する。

構文型は問題文の質問表現から判定する。落としは作問時の予定ではなく、完成稿で核名詞句の直前に実際にある表現を記録する。核名詞は、解答対象の種類を表す上位分類とする。落としを構成する手掛かりIDと、各手掛かりが対象を直接説明するかも記録する。上位分類だけ、作品や人物の列挙だけ、付随的性質だけになっていないか、前フリと後限定を除いた文でも解答対象の直接的な説明と準一意性が成立するかを監査する。`work_state_check.py`は一部の代名詞的・メタ言語的な核名詞、文字列の位置、質問形式、手掛かりとの参照関係を検査するが、上位分類と対象の意味関係までは判定しない。

## 生成側の完了条件

外部資料によって評価する検査単位は、次が揃ったときに完了とする。

- 判断対象
- 結論
- 使用した資料中の情報と所在
- 資料中の情報から結論へ至る推論
- 直接記載、演繹、解釈、複数資料の総合の別
- 未解決の反例または対抗候補がないこと

日本語としての自然さなど、通常は外部資料を必要としない項目では、資料中の情報に代えて、実際に比較した二つ以上の問題文案と判断理由を記録する。解答露出では、解答を伏せた検査で挙がった候補と、問題文の意味および語形成から生じる候補を分ける。各候補について、名称を形成する要素、その入手元、形成規則、名称候補の形成に対象との対応知識が必要か、形成後に標準名称だと確認するためだけに対応知識が必要かを別々に記録する。形成に対応知識が必要な場合は、その知識なしには選べない名称要素も記録する。

生成側の必要な検査単位がすべて完了するまで、監査へ渡さない。

## 監査結果

監査側は各検査単位へ次のいずれかを記録する。

- `pending`：未検査
- `passed`：資料、推論、判断、記載が成立している
- `missing`：判断を支える資料と推論は成立するが、必要な引用、所在、対応関係、推論が候補出力に欠けている
- `failed`：資料の対象・役割・範囲・粒度が結論に届かない、反例が残るなど、記載の補充だけでは合格にできない

`missing`または`failed`では、次のどこを修正する必要があるかも記録する。

- 最終出力の記載
- 根拠資料または推論
- 問題文の表現
- 個別の手掛かり
- 手掛かりの組合せまたは順序
- 正答範囲または正誤判定
- 解答対象

監査側の必要な検査単位がすべて`passed`になるまで、問題を確定しない。

## 最終出力用の限定入力

最終出力を組み立てる担当には、次だけを渡す。

- 完成した問題と解答
- 採用した命題と根拠
- 採用した手掛かりと各評価
- 確定した難易度判断
- 確定した正誤判定
- 問題文の構造と表現評価
- 問題文の長さと判定
- 参考文献

棄却候補、検索過程、監査の往復、既出問題との比較過程、不採用の命題・手掛かり・表現は渡さない。

## JSON manifest

JSON manifestは、検査対象を具体的な内容へ結び付け、確定的な参照整合性と工程境界を検査するために使う。IDだけのレコードや、複数の専門用語・解答候補・出力項目を一つのIDにまとめたレコードを置かない。

資料には書誌情報と逐語引用を置く。命題には問題文の対応箇所、真偽を判定する文、引用ID、引用から判断へ至る理由、推論の種類を置く。一つの命題内に複数の項・限定がある場合は、検証要素ごとにも引用ID、理由、推論の種類を置く。手掛かりには問題文中の文字列と命題IDを置き、中核性、準一意性、知名度の各判断へ結論、理由、引用IDを置く。準一意性には比較範囲、対抗候補、単独で十分に絞れること、依存する他の手掛かりがないことを置く。専門用語と解答候補は一語・一候補ごとにレコードを分ける。最終出力の必須項目も項目ごとに固定IDを使い、内容の保存先を示す。

生成工程ではすべての `audit` を `pending` とした状態で `--stage generation` を通す。監査担当だけが結果を更新し、`--stage audit` を通す。これにより、完成後に生成と監査の状態をまとめて作ることを認めない。

委譲機能を利用できる環境では、交差領域の確認、探索、生成、解答露出検査、監査、最終出力を別々のagentへ割り当てる。親agentは起動toolが返した正規の識別子を起動直後に `execution.agents` へ記録し、各成果物に記載された担当識別子と照合する。候補変更時にも、継続して使う探索担当の識別子を別名へ置き換えない。利用できない環境では、その事実と理由を記録する。

具体的なJSONの形は `scripts/work_state_check.py` が検査するフィールドに従う。次は架空の名称・URLを使った題材探索状態の形式例である。

```json
{
  "facet_nodes": {"subject": "subject::66", "place": "place::ROOT", "time": "time::ROOT", "type": "type::ROOT"},
  "execution": {"delegation_available": true, "agents": {"intersection": "agent-1", "exploration": "agent-2", "alternate_exploration": "agent-3", "saturation_review": "agent-4"}, "assignment_log": {"intersection": {"agent_id": "agent-1", "recorded_at_spawn": true, "artifact_refs": ["intersection.md"]}, "exploration": {"agent_id": "agent-2", "recorded_at_spawn": true, "artifact_refs": ["exploration.md"]}, "alternate_exploration": {"agent_id": "agent-3", "recorded_at_spawn": true, "artifact_refs": ["alternate_exploration.md"]}, "saturation_review": {"agent_id": "agent-4", "recorded_at_spawn": true, "artifact_refs": ["saturation_review.md"]}}},
  "intersection_review": {
    "source_refs": ["https://example.org/outline", "https://example.org/lesson"],
    "candidate_examples": [
      {"name": "候補1", "source_ref": "https://example.org/outline", "beginner_source_ref": "https://example.org/lesson", "beginner_learning_basis": "名称と代表情報を学習項目として扱う"},
      {"name": "候補2", "source_ref": "https://example.org/outline"}
    ],
    "scope_reason": "対象の種類と下位領域を区分できる",
    "result": "viable"
  },
  "entry_points": [
    {"id": "E1", "kind": "分類表", "label": "産業分類", "url": "https://example.org/industry", "access_note": "分類項目", "opened": true},
    {"id": "E2", "kind": "事典索引", "label": "化学事典", "url": "https://example.org/encyclopedia", "access_note": "索引項目", "opened": true},
    {"id": "E3", "kind": "利用者記事", "label": "実務記事", "url": "https://example.org/practice", "access_note": "記事本文", "opened": true},
    {"id": "E4", "kind": "産業誌", "label": "産業誌記事", "url": "https://example.org/trade", "access_note": "記事本文", "opened": true}
  ],
  "coverage_areas": [
    {"id": "D1", "label": "無機化学工業", "basis": "分類表の区分", "target_kinds": "工業技術", "explored": true, "entry_point_ids": ["E1"], "source_searches": [{"mode": "open", "query": "無機化学工業 技術", "angle": "分野の分類", "result": "候補1を発見", "entry_point_ids": ["E1"], "found_candidate_ids": ["K1"], "next_searches": []}]},
    {"id": "D2", "label": "有機化学工業", "basis": "事典の区分", "target_kinds": "工業技術", "explored": true, "entry_point_ids": ["E2"], "source_searches": [{"mode": "open", "query": "有機化学工業 技術", "angle": "分野の索引", "result": "候補2を発見", "entry_point_ids": ["E2"], "found_candidate_ids": ["K2"], "next_searches": []}]}
  ],
  "candidates": [
    {"id": "K1", "label": "候補1", "coverage_area_ids": ["D1"], "discovery_entry_point_ids": ["E1"], "name_use_note": "本文で対象の名称として使われる", "facet_membership_reason": "選択した四軸の内側にある", "disposition": "eligible", "expanded": true, "expansion_searches": [{"source_or_query": "候補1の関連項目", "relation_checked": "同じ分野の並列項目", "found_candidate_ids": []}], "exposure_precheck": {"representative_descriptions": ["対象を説明する語句"], "accepted_names": ["候補1"], "formations": [{"name": "候補1", "description_index": 0, "formation_rule": "対象との既知の対応から名称を選ぶ", "components": [{"form": "候補1", "source": "対象との既知の対応", "knowledge": "target_association"}], "formation_requires_target_association": true, "formation_target_association_step": "名称要素を選ぶ", "standard_name_confirmation_requires_target_association": true}], "status": "passed"}},
    {"id": "K2", "label": "候補2", "coverage_area_ids": ["D2"], "discovery_entry_point_ids": ["E2"], "name_use_note": "本文で対象の名称として使われる", "facet_membership_reason": "選択した四軸の内側にある", "disposition": "eligible", "expanded": true, "expansion_searches": [{"source_or_query": "候補2の関連項目", "relation_checked": "同じ分野の並列項目", "found_candidate_ids": []}], "exposure_precheck": {"representative_descriptions": ["対象を説明する語句"], "accepted_names": ["候補2"], "formations": [{"name": "候補2", "description_index": 0, "formation_rule": "対象との既知の対応から名称を選ぶ", "components": [{"form": "候補2", "source": "対象との既知の対応", "knowledge": "target_association"}], "formation_requires_target_association": true, "formation_target_association_step": "名称要素を選ぶ", "standard_name_confirmation_requires_target_association": true}], "status": "passed"}}
  ],
  "independent_review": [
    {"id": "D1", "difference_from_exploration": "実務者の利用場面", "source_discovery_query": "無機化学工業 実務者 利用", "checked_entry_point_ids": ["E3"], "found_candidate_ids": [], "spotchecked_entry_point_ids": ["E1"], "spotcheck_result": "分類項目と候補を照合した"},
    {"id": "D2", "difference_from_exploration": "産業誌の利用場面", "source_discovery_query": "有機化学工業 産業誌", "checked_entry_point_ids": ["E4"], "found_candidate_ids": [], "spotchecked_entry_point_ids": ["E2"], "spotcheck_result": "索引項目と候補を照合した"}
  ],
  "saturation_challenge": {"search_perspective": "別の書き手の産業資料", "query": "化学工業 現場 使用", "opened_entry_point_ids": ["E3", "E4"], "found_candidate_ids": [], "resolution": "新しい候補なし", "resolved": true},
  "frontier_ids": [],
  "saturated": true
}
```

作問状態では、現在の問題で必要となる共通検査単位を省略せずに置く。`work_state_check.py`が内容の存在と参照関係を認めても、引用と推論の意味上の妥当性は、生成側と監査側が別途判断する。
