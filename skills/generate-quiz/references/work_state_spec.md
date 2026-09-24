# 作問中の状態

## 目的

作問中の調査記録と、人間へ示す最終出力を分ける。生成と監査は同じ検査単位を使い、必要な判断が完了したことを確認してから次の工程へ進む。

引用、推論、候補比較はMarkdownで保持する。ID、問題文の版、採否、完了状態、参照関係はJSON manifestでも保持し、`scripts/work_state_check.py`で確定的に検査する。JSON manifestだけを判断根拠にせず、対応するMarkdownの内容を生成担当と監査担当が評価する。

## ファセットの交差領域

ファセット選択後、題材探索前に4軸の正規ノードキーと交差領域の確認記録をJSONへ保存し、`work_state_check.py --stage intersection-checkpoint`で検査する。確認記録には、開いた資料のURL、交差領域の広さを判断した理由、資料中に実名がある異なる候補二つ以上と各資料のURL、うち一件以上の初級学習資料と扱いの根拠、成立の判定を含める。広さの理由には、選択範囲に入る大区分と、異なる用途の資料で確かめた対象の種類・下位領域を対応させ、候補探索の経路を設けられるかを記す。委譲機能の有無は`execution.delegation_available`に記録する。別agentが確認する場合は、その正規IDと起動時の記録を`execution.agents`と`execution.assignment_log`へ保存する。委譲機能がない場合は、利用できない理由を記録して親agentが確認する。形式検査は資料の独立性や判断の妥当性を保証しない。

## 題材候補の探索状態

現在の問題番号について、次を保持する。

- 選択した4軸の正規ノードキー
- 資料から分けた下位領域、そこに含まれる解答対象の種類、各領域を探索したか
- 各領域で候補名を含めず入口を探した検索語・観点と、候補名から近接対象を探した経路
- 本文を開いた資料のURL・確認箇所と、そこで発見した候補
- 各候補の名称の使用箇所（資料で名称を確認できず除外した候補を除く）、選択範囲への所属理由、発見元、選択対象か、選択対象なら近接探索の記録
- 別経路の探索で各下位領域に開いた入口、元の探索と異なる観点、得た候補、元の資料と台帳を照合した結果
- 探索完了の反証調査で使った観点・検索語・開いた資料、得た候補と未探索経路の処理結果
- 各選択対象の代表説明、正答名・許容別名、説明案ごとの名称形成の分析、解答露出の予備判定
- 探索段階で選択対象となるか、除外する場合はその理由
- 抽選後に題材品質ゲートで棄却した場合は、満たせなかった条件
- 新しい有力候補が増えなくなったか

一つの解答対象を棄却しても、この状態は同じ問題番号で題材を再選定するために保持する。棄却した対象に固有の引用、推論、問題文、監査履歴は、新しい解答対象の作業状態へ渡さない。

題材候補の探索状態は最終出力へ含めない。探索が飽和したら露出予備検査の前に`work_state_check.py --stage discovery`で検査する。抽選に使う探索状態は`--stage selection`で確認する。解答対象を決めた後は探索台帳を含まない作問状態を別に作り、生成担当の起動時記録とともに`--stage generation-start`で確認する。

探索状態は、題材を抽選する前に `topic_pick.py` へ渡す。入口には本文を開いたURL、`opened: true`、確認箇所を`access_note`として記録する。下位領域の`source_searches`には、候補名を含めない入口探しを`mode: open`、既知候補からの近接探索を`mode: nearby`として記録する。候補の`discovery_entry_point_ids`と`coverage_area_ids`は、同じ`source_searches`の`entry_point_ids`と`found_candidate_ids`に対応させる。最初の候補を記録した時点と入口・候補を追加した節目に`--stage discovery-progress`でこの対応を検査する。内部知識から挙げ、まだ資料で確認していない候補は、途中状態では`discovery_entry_point_ids`を空配列にできる。資料の探索記録にその候補を加えたら発見元も記録し、`--stage discovery`までに対応を確定する。途中検査では探索の完了や露出予備検査の記録を要求しない。資料で名称を確認できず除外する候補を除き、`name_use_note`には名称の使用箇所を記す。`facet_membership_reason`には四軸の範囲に属すると判断した理由を記す。選択対象の`expansion_searches`には近接探索の検索先・調べた関係・得た候補IDを残す。検査を通った後で候補を追加した場合は、その候補からも探索を展開し、再度検査する。

`independent_review`には下位領域IDごとに、最初の探索と異なる観点、候補名を含めない検索語、別経路で開いた入口IDと候補ID、照合した元の入口IDと結果を記録する。`saturation_challenge`には別の立場・用途からの検索、開いた入口ID、得た候補ID、未探索経路の処理と完了状態を残す。形式検査の合格は資料の内容と記録が対応することや、探索の十分さを保証しない。

`disposition`は探索段階で選択対象となるかを表す。抽選後に題材品質ゲートで棄却した候補は`eligible`のまま、満たせなかった条件を`quality_rejection_reason`へ記録する。再抽選では、この記録がある全候補のIDを`topic_pick.py --exclude`へ渡す。

各選択対象と解答露出を理由に除外する候補の`exposure_screen`には、資料にある中心的説明を`central_description`、開いた資料の入口IDを`source_entry_point_ids`、名称形成の疑いを`formation_risk`（`suspected`または`none_detected`）、判断理由を`reason`として記録する。`suspected`なら`exposure_precheck`で異なる中核的な代表説明を少なくとも二つ調べ、許容名称と詳しく照合する。`formations`は名称と代表説明の組合せごとに一件作り、対応する許容名称の添字を`name_index`、代表説明の添字を`description_index`で記録する。調べた説明案と許容名称の各組合せを照合し、一つの説明で名称を形成できても、ほかの説明で形成できなければ選択対象に残す。`status: passed`は露出がないという意味ではなく、抽選前に回避不能な露出を立証できなかったことを表す。`unavoidable_exposure`で除外するには、調べたすべての代表説明で正答名または許容別名を解答側の知識なしに形成できる必要がある。形式検査は説明の妥当性を保証しないため、候補名を言い換えただけの説明を複数並べて除外しない。

## 解答対象ごとの作業状態

ユーザーが解答対象を直接指定した場合は`selection_mode: specified`と`user_specified_target`を記録し、題材探索担当の割当記録を要求しない。ファセットから抽選した場合は`selection_mode: random`とし、探索担当の割当記録を保持する。どちらの場合も、決まった解答対象について生成以降の検査を省かない。

解答対象が決まったら、その対象だけに属する作業状態を新しく作る。次を互いに識別できる形で保持する。

- 解答対象とユーザーの作問条件
- 資料、引用箇所、確認状態
- 予定命題と実現命題
- 手掛かり候補と採否
- 難易度の二つの参照集団
- 問題文にある専門用語と、その意味内容が命題理解に必要かの判断
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
- 問題文にある各専門用語と、その意味内容が命題理解に必要かの判断
- 前フリ・落としを構成する各手掛かりの中核性・代表性、準一意性、知名度
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
- 最終出力用の限定入力

見出しが存在することだけで、その内部の検査単位を完了扱いにしない。

構造の検査記録には`prefuri_segments`を置き、完成稿の各前フリを`passage`、解答対象について述べる内容を平叙文に戻した`target_predication`、独立した事実の累加として読める`reason`とともに記録する。前フリがなければ空配列とする。`work_state_check.py`は各`passage`が落としより前の問題文にあるかを確認し、叙述として読めるかは監査agentが完成稿から判定する。

連用中止・テ形接続がない場合も、完成稿を走査した結果として「該当なし」と記録する。接続がある場合は、左右の述定をそれぞれ省略のない形に戻し、並列、継起、理由、対立、手段、条件のどの関係が成立するかと、その判断理由を一箇所ずつ記録する。

構文型は問題文の質問表現から判定する。落としは作問時の予定ではなく、完成稿で核名詞句の直前に実際にある表現を記録する。核名詞は、解答対象の種類を表す上位分類とする。落としを構成する手掛かりIDと、各手掛かりが対象を直接説明するかも記録する。上位分類だけ、作品や人物の列挙だけ、付随的性質だけになっていないか、前フリと後限定を除いた文でも解答対象の直接的な説明と準一意性が成立するかを監査する。`work_state_check.py`は記録した文字列が問題文にあることと手掛かりとの参照関係を検査するが、構文型、落としの位置、核名詞が上位分類に当たるかは判定しない。

## 生成側の完了条件

外部資料によって評価する検査単位は、次が揃ったときに完了とする。

- 判断対象
- 結論
- 使用した資料中の情報と所在
- 資料中の情報から結論へ至る推論
- 直接記載、演繹、解釈、複数資料の総合の別
- 未解決の反例または対抗候補がないこと

日本語としての自然さなど、通常は外部資料を必要としない項目では、資料中の情報に代えて、実際に比較した二つ以上の問題文案と判断理由を記録する。解答露出では、解答を伏せた検査で挙がった候補と、問題文の意味および語形成から生じる候補を分ける。各候補について、名称を形成する要素、その入手元、形成規則、名称候補の形成に解答側の知識が必要か、形成後に標準名称だと確認するためだけに解答側の知識が必要かを別々に記録する。各要素を得るのに使う知識は、`quiz_generation_spec.md`第18節の区分に従い、`knowledge`（`surface`・`audience_known`・`answer_side`）に記録する。各値は、問題文の表層、想定層の既習知識、解答側の知識に当たる。`answer_side`とした要素には、その知識が想定プレイヤー層にとって明白に既習でない理由を`answer_side_reason`に記録する。

露出検査担当は問題文の版ごとに新しく割り当て、`execution.exposure_assignments`に版、正規ID、解答名を含まない依頼名、起動時の記録を残す。依頼名は`task_label`に記録する。`execution.assignment_log.exposure`の依頼名と成果物経路にも解答名を含めない。

対抗候補、露出候補、回答はIDで照合する。候補を最初に挙げた担当が、記録する時点でIDを付ける。後から候補を挙げる担当は、既存の候補と同じ対象なら既存のIDに対応付け、別の対象なら新しいIDを付ける。担当の記録にある名称を、ほかの担当、親、統括役が書き換えない。

露出候補には`id`を付ける。問題文の意味から挙げた候補には、挙げた担当がどの回答と同じ名称かを`answer_id`（該当がなければ`null`）で対応付ける。解答を伏せて挙げた候補には`answer_id`を置かず、解答を開示した後の`answer_review`で対応付ける。

`answer_review`には露出検査担当が解答を見た後に行う、各回答と露出候補の正誤判定を記録する。回答ごとに同一対象か、指定は十分か、明確な誤りがあるか、名称の適用範囲が一致するかを分け、結論、引用、理由を対応させる。露出候補の判定は`candidate_reviews`に`candidate_id`で置き、解答を伏せて挙げた候補には対応する回答の`answer_id`（該当がなければ`null`）も置く。露出候補を正答と判断した場合は解答一覧にも追加する。

生成側の必要な検査単位がすべて完了するまで、監査へ渡さない。

## 監査前の反証確認

生成工程の状態検査に合格した後、監査前に難易度と各手掛かりの準一意性を独立に反証する。`evidence_challenge`には現行問題文の版、問う知識、生成担当とは別の担当者を記録する。問う知識は作業状態の`asked_knowledge`と一致させる。`beginner`と`general`には開いた資料のURL、反証で見つけた事情、採用する引用IDと解決理由を置く。各手掛かりの記録は採用中の手掛かりIDに対応させ、逆引きで確認した対抗候補の`id`と名称、候補自身を扱う資料のURL、問題文の条件との照合、候補の採否と未解決の有無を置く。生成側の対抗候補をすべて照合し、独立調査で新しく見つけた有力候補も記録する。条件の相違を確認できない候補や生成側と採否が食い違う候補は、監査前に解決する。

## 監査結果

監査担当が解答の開示前に抽出した露出候補は、`exposure_review`へ問題文の版とSHA-256、候補の名称形成、照合した正答IDとともに記録する。解答の開示後に、各候補を生成側の露出候補の`exposure_candidate_id`と、同じ名称の回答の`answer_id`（該当がなければ`null`）に対応付ける。候補を挙げなかった場合も理由を残す。監査候補が生成側の露出検査にない場合は、生成側の判断を更新してから再監査する。

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

`final_input.topic_selection`には解答対象を`answer_target`、履歴補正の適用結果を`history_result`として置く。抽選した題材では、選択した四軸のノードを`facet_nodes`、それぞれの日本語の分類経路を`facet_paths`として置く。ユーザー指定の題材には`facet_paths`を置かない。完成稿に出す文章は`final_input.material.topic_selection`に置く。

`final_input.material`には完成稿の必須項目ごとの本文を置く。採用する引用は本文、書誌情報、所在を保持し、不採用の引用を混ぜない。引用本文は、原則としてその引用を最初に使う判断の文章に置き、後の判断の文章では参照先を特定できるようにする。「確認した内容との一致」には命題と外の関係の連体修飾節に対応する問題文の箇所を含める。問題文の長さには抽選値や判定器の内部表記を含めない。

最終出力を組み立てる担当には、次だけを渡す。

- 完成した問題と解答
- 採用した命題と根拠
- 採用した手掛かりと各評価
- 確定した難易度判断
- 確定した正誤判定
- 問題文の構造と表現評価
- 連体修飾節の内外関係と対応する命題
- 問題文の長さと判定
- 参考文献

棄却候補、検索過程、監査の往復、既出問題との比較過程、不採用の命題・手掛かり・表現は渡さない。

外部資料を根拠にした各判断には、監査で確認した逐語引用の本文、所在、資料の書誌情報とURL、引用から判断へ至る推論を添える。引用IDや要約だけを渡さない。必要な引用を限定入力へ収録できない場合は、組立てへ進まない。

## JSON manifest

JSON manifestは、検査対象を具体的な内容へ結び付け、確定的な参照整合性と工程境界を検査するために使う。IDだけのレコードや、複数の専門用語・解答候補・出力項目を一つのIDにまとめたレコードを置かない。

資料には書誌情報と逐語引用を置く。命題には問題文の対応箇所、真偽を判定する文、引用ID、引用から判断へ至る理由、推論の種類を置く。一つの命題内に複数の項・限定がある場合は、検証要素ごとにも引用ID、理由、推論の種類を置く。手掛かりには問題文中の文字列と命題IDを置き、中核性、準一意性、知名度の各判断へ結論、理由、引用IDを置く。準一意性には比較範囲、対抗候補、単独で十分に絞れること、依存する他の手掛かりがないことを置く。専門用語と解答候補は一語・一候補ごとにレコードを分ける。最終出力の必須項目も項目ごとに固定IDを使い、内容の保存先を示す。

各`competitors`項目には、候補の`id`と`name`、その候補を扱う資料の`evidence_ids`を置く。手掛かりに書かれた条件ごとの`passage`、`matches`（真偽値）、`reason`、`evidence_ids`を`conditions`に置く。候補を別対象として退けるか同一対象の別名として扱うかを`disposition`（`excluded`・`same_target`）と`reason`で示す。別対象を退ける場合だけ、相違する条件の`passage`を`exclusion_passage`へ置く。条件の引用IDは候補の引用IDへ、候補の引用IDは準一意性の引用IDへ含める。

問う知識の内容を`asked_knowledge`に記録し、難易度の独立検査は`difficulty_review`に記録する。後者の`asked_knowledge`には検査対象とした問う知識、`answer_granularity`には要求する解答知識の細かさ、`beginner`と`general`には各集団の`status`、`reason`、`evidence_ids`を置く。`reviewer_id`には難易度検査担当の正規識別子を記録し、委譲機能がない場合は`self`とする。一般層側の`other_access_paths`には、定義的な資料とは別に名称と代表情報の対応が共有され得る経路を`path`、実際に調べた内容を`search_record`、その対応への接触を確認できたかを`outcome`、調査結果を`result`、確認した資料の引用IDを`evidence_ids`として置く。`outcome`は`confirmed`または`not_confirmed`とし、前者では引用IDを必須とする。後者では引用IDを空にできるが、調べた範囲を超える不在の根拠とは扱わない。

初学者側の`name_learning`には解答対象の名称を学ぶ位置を、`relation_learning`には問う関係を対象の特徴として学ぶ位置を記録する。`learning_connection`には両者を結び付け、要求する粒度の知識を1〜2年以内に学びうると判断する推論を記録する。それぞれに`reason`と`evidence_ids`を置き、引用IDを初学者側の`evidence_ids`にも含める。同じ引用を複数の判断に使えるが、その引用が各判断をどう支えるかは別々に示す。

作文前に`--stage difficulty`で解答対象、問う知識、資料中の逐語引用、難易度の独立検査、担当記録を検査する。問う知識を変更したら難易度を再検査し、`difficulty_review.asked_knowledge`を更新する。完成稿については、`checks`の両参照集団の検査単位に問う知識を記録し、問題文の版、監査結果と対応させる。難易度担当の判定に対する監査結果は`difficulty_review.audit`に記録し、作文前と生成工程では`pending`、監査後は`passed`とする。構造検査は、問う知識と問題文の意味上の一致、資料からの推論の妥当性、工程の実行時刻を保証しない。

専門用語の`term`には、現行問題文にある表記を記録する。命題理解に意味内容が必要かを`meaning_needed`に記録する。必要な場合は、語の意味を確認した引用と理由を`meaning_evidence_ids`・`meaning_reason`、想定プレイヤー層がその意味を明白に知っていると判断する引用と理由を`audience_evidence_ids`・`audience_reason`に分ける。必要ない場合は、意味内容を知らなくても問題文を理解できる理由を`understanding_without_meaning`に記録する。同じ引用を両方に使うときも、語義の確認と既習性の判断をそれぞれ説明する。

`terminology_review`には、生成担当とは別の担当者の`reviewer_id`と`draft_version`を置く。独立検査の担当者は生成側の語IDを知らずに専門用語を抽出し、各語の表記と意味内容が命題理解に必要かを判断する。その後に生成側の用語一覧を受け取り、同じ語の記録へ生成側の語IDを対応付け、生成側にない語には新しい語IDを付ける。必要な語には語義と既習性それぞれの判定・理由・引用IDを、不要な語には意味内容を知らなくても文意が通る理由を記録する。該当語がない場合も空の`terms`を記録する。独立検査で列挙した語と必要性の判断が生成側と一致し、必要な語の両判断が合格し、生成側で採用した引用ID集合の全件を独立検査の記録に含めるまで、生成工程の状態検査を通さない。独立検査の監査結果は`terminology_review.audit`に記録し、生成工程では`pending`、監査後は`passed`とする。監査では語の抽出漏れ、意味内容の要否、語義・既習性の根拠と推論を確認する。構造検査は、問題文からの語の抽出、必要性の判断、引用が判断を実際に支えるかまでは判定しない。

`final_input`は監査前に確定する。`final_input.relative_clauses`には、現行問題文の各連体修飾節を`passage`、内の関係か外の関係かを`relation`（`inner`・`outer`）として置き、判断理由を`reason`として記録する。外の関係では、修飾節が表す内容と解答対象を結ぶ命題IDを`relation_proposition_ids`に置く。連体修飾節がなければ空配列とする。`work_state_check.py`は各`passage`が問題文にあって重複しないことと、外の関係だけに命題IDがあることを確認し、節の漏れ、内外関係の判断、命題が関係を表すかは監査担当が判定する。`final_input.quote_ids`には採用中の判断に用いた引用IDを過不足なく置く。`other_access_paths`の調査だけに用いた引用は含めない。

監査合格後は、組立て担当と最終照合担当の割当記録を加える以外に、採用項目と`final_input`を変更しない。最終段階では、完成したMarkdownと監査に使った状態ファイルそのものを`work_state_check.py --stage final --output 完成稿.md 状態.json`へ渡す。`work_state_check.py`は逐語引用の本文が出力に実在することを確認し、引用と結論の意味上の対応は最終照合担当が資料本文に戻って判定する。

最終照合担当が完成稿を確認したら、`final_review`に`status: passed`、担当の正規識別子を`reviewer_id`、照合した引用・回答・手掛かりのIDを`quote_ids`・`answer_ids`・`clue_ids`、各検査の結果を`checks`（`current_draft`・`evidence_and_inference`・`difficulty`・`competitors`・`answer_judging`・`exposure`）、照合した完成稿のファイル内容のSHA-256を`output_sha256`として記録する。委譲機能がない場合の`reviewer_id`は`self`とする。完成稿を直した場合は再照合し、ハッシュも更新する。この記録は照合の対象と結果を検査するもので、判断の妥当性を機械的に証明するものではない。

生成工程ではすべての `audit` を `pending` とした状態で `--stage generation` を通す。監査担当だけが結果を更新し、`--stage audit` を通す。これにより、完成後に生成と監査の状態をまとめて作ることを認めない。

委譲機能を利用できる環境では、ファセットの交差領域の確認、探索、生成、難易度と専門用語の独立検査、解答露出検査、監査、最終出力の組立て、最終照合を別々のagentへ割り当てる。親agentは起動toolが返した正規の識別子を起動直後に `execution.agents` へ記録し、各成果物に記載された担当識別子と照合する。候補変更時にも、継続して使う探索担当の識別子を別名へ置き換えない。利用できない環境では、その事実と理由を記録する。

具体的なJSONの形は `scripts/work_state_check.py` が検査するフィールドに従う。次は架空のURLを使った題材探索状態の形式例である。

```json
{
  "facet_nodes": {"subject": "subject::66", "place": "place::ROOT", "time": "time::ROOT", "type": "type::ROOT"},
  "execution": {"delegation_available": true, "agents": {"intersection": "agent-1", "exploration": "agent-2", "alternate_exploration": "agent-3", "saturation_review": "agent-4"}, "assignment_log": {"intersection": {"agent_id": "agent-1", "recorded_at_spawn": true, "artifact_refs": ["intersection.md"]}, "exploration": {"agent_id": "agent-2", "recorded_at_spawn": true, "artifact_refs": ["exploration.md"]}, "alternate_exploration": {"agent_id": "agent-3", "recorded_at_spawn": true, "artifact_refs": ["alternate_exploration.md"]}, "saturation_review": {"agent_id": "agent-4", "recorded_at_spawn": true, "artifact_refs": ["saturation_review.md"]}}},
  "intersection_review": {
    "source_refs": ["https://example.org/outline", "https://example.org/lesson"],
    "candidate_examples": [
      {"name": "アンモニアソーダ法", "source_ref": "https://example.org/outline", "beginner_source_ref": "https://example.org/lesson", "beginner_learning_basis": "高校化学の教材が、炭酸ナトリウムの工業的製法として名称と反応の流れを学習項目にしている"},
      {"name": "クメン法", "source_ref": "https://example.org/outline"}
    ],
    "scope_reason": "産業分類表の化学工業の区分（無機・有機・高分子等）と、実務記事が扱う製法・装置の種類から、区分ごとに探索経路を設けられる",
    "result": "viable"
  },
  "entry_points": [
    {"id": "E1", "kind": "分類表", "label": "産業分類", "url": "https://example.org/industry", "access_note": "分類項目", "opened": true},
    {"id": "E2", "kind": "事典索引", "label": "化学事典", "url": "https://example.org/encyclopedia", "access_note": "索引項目", "opened": true},
    {"id": "E3", "kind": "利用者記事", "label": "実務記事", "url": "https://example.org/practice", "access_note": "記事本文", "opened": true},
    {"id": "E4", "kind": "産業誌", "label": "産業誌記事", "url": "https://example.org/trade", "access_note": "記事本文", "opened": true}
  ],
  "coverage_areas": [
    {"id": "D1", "label": "無機化学工業", "basis": "産業分類表で無機化学工業が独立した区分になっている", "target_kinds": "工業技術", "explored": true, "entry_point_ids": ["E1"], "source_searches": [{"mode": "open", "query": "無機化学工業 技術", "angle": "分類表の区分に挙がる製法名を探す", "result": "アンモニアソーダ法を発見", "entry_point_ids": ["E1"], "found_candidate_ids": ["K1"], "next_searches": []}]},
    {"id": "D2", "label": "有機化学工業", "basis": "化学事典の索引で有機工業化学の製法がまとめて挙げられている", "target_kinds": "工業技術", "explored": true, "entry_point_ids": ["E2"], "source_searches": [{"mode": "open", "query": "有機化学工業 技術", "angle": "事典索引の製法項目を探す", "result": "クメン法を発見", "entry_point_ids": ["E2"], "found_candidate_ids": ["K2"], "next_searches": []}]}
  ],
  "candidates": [
    {"id": "K1", "label": "アンモニアソーダ法", "coverage_area_ids": ["D1"], "discovery_entry_point_ids": ["E1"], "name_use_note": "化学事典の本文で、炭酸ナトリウムの製法の名称として使われている", "facet_membership_reason": "炭酸ナトリウムを工業的に製造する方法で、化学工業のうち無機化学工業に当たる", "disposition": "eligible", "expanded": true, "expansion_searches": [{"source_or_query": "化学事典のアンモニアソーダ法の項の関連項目", "relation_checked": "炭酸ナトリウムを得る別の製法", "found_candidate_ids": []}], "exposure_screen": {"central_description": "食塩と石灰石から炭酸ナトリウムを工業的に得る製法", "source_entry_point_ids": ["E1"], "formation_risk": "none_detected", "reason": "説明にアンモニアを使うことが現れず、名称の「アンモニア」を説明から得られない"}},
    {"id": "K2", "label": "クメン法", "coverage_area_ids": ["D2"], "discovery_entry_point_ids": ["E2"], "name_use_note": "化学事典の索引と本文で、フェノールの製法の名称として使われている", "facet_membership_reason": "フェノールとアセトンを工業的に製造する方法で、化学工業のうち有機化学工業に当たる", "disposition": "eligible", "expanded": true, "expansion_searches": [{"source_or_query": "クメン法 原料 製法", "relation_checked": "ベンゼンとプロピレンを原料とする別の製法", "found_candidate_ids": []}], "exposure_screen": {"central_description": "ベンゼンとプロピレンからクメンを経てフェノールとアセトンを得る製法", "source_entry_point_ids": ["E2"], "formation_risk": "suspected", "reason": "説明に現れる「クメン」と、製法を表す「法」から名称を作れる可能性がある"}, "exposure_precheck": {"representative_descriptions": ["ベンゼンとプロピレンからクメンを経てフェノールとアセトンを得る製法", "ベンゼンとプロピレンからフェノールとアセトンを同時に得る製法"], "accepted_names": ["クメン法"], "formations": [{"name": "クメン法", "name_index": 0, "description_index": 0, "formation_rule": "説明中の中間体の名称に、製法を表す「法」を付ける", "components": [{"form": "クメン", "source": "説明中の「クメンを経て」", "knowledge": "surface"}, {"form": "法", "source": "製法を表す接尾要素", "knowledge": "audience_known"}], "formation_requires_answer_side_knowledge": false, "standard_name_confirmation_requires_answer_side_knowledge": true}, {"name": "クメン法", "name_index": 0, "description_index": 1, "formation_rule": "中間体の名称に、製法を表す「法」を付ける", "components": [{"form": "クメン", "source": "中間体がクメンであるという知識", "knowledge": "answer_side", "answer_side_reason": "説明に中間体が現れず、中間体がクメンであることはこの製法そのものについての知識である"}, {"form": "法", "source": "製法を表す接尾要素", "knowledge": "audience_known"}], "formation_requires_answer_side_knowledge": true, "standard_name_confirmation_requires_answer_side_knowledge": true}], "status": "passed"}}
  ],
  "independent_review": [
    {"id": "D1", "difference_from_exploration": "工場の工程を実務者が説明する記事から探す", "source_discovery_query": "無機化学工業 実務者 利用", "checked_entry_point_ids": ["E3"], "found_candidate_ids": [], "spotchecked_entry_point_ids": ["E1"], "spotcheck_result": "分類表の無機化学工業の項目とアンモニアソーダ法の記載を照合した"},
    {"id": "D2", "difference_from_exploration": "産業誌が扱う製造プロセスから探す", "source_discovery_query": "有機化学工業 産業誌", "checked_entry_point_ids": ["E4"], "found_candidate_ids": [], "spotchecked_entry_point_ids": ["E2"], "spotcheck_result": "事典索引の有機工業化学の項目とクメン法の記載を照合した"}
  ],
  "saturation_challenge": {"search_perspective": "工場見学や業界団体による一般向けの解説", "query": "化学工業 現場 使用", "opened_entry_point_ids": ["E3", "E4"], "found_candidate_ids": [], "resolution": "開いた資料に新しい製法名はなく、既存の候補と一致した", "resolved": true},
  "frontier_ids": [],
  "saturated": true
}
```

作問状態では、現在の問題で必要となる共通検査単位を省略せずに置く。`work_state_check.py`が内容の存在と参照関係を認めても、引用と推論の意味上の妥当性は、生成側と監査側が別途判断する。
