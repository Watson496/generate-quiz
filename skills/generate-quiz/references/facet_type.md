# type ファセットカタログ — 全階層

各 `FACET_NODE` ブロックは一つの親ノードと、その直接の子を自己完結的に収録しています。
細分化する場合は、検索で得た親ブロックの `DIRECT_CHILDREN` を全件比較してください。
ラベル・コード・注記は元データ由来です。独自ノードを追加しないでください。

## FACET_NODE `type::ontology`

- FACET: `type`
- NODE_KEY: `type::ontology`
- CODE: `ontology`
- LABEL: オントロジー型ファセット
- PARENT_KEY: `type::ROOT`
- PATH_CODES: `ontology`
- PATH_LABELS: オントロジー型ファセット
- LEAF: false
- DIRECT_CHILDREN_COUNT: 3

### DIRECT_CHILDREN

- `type::endurant` | CODE `endurant` | 持続体
- `type::perdurant` | CODE `perdurant` | 事象
- `type::abstract` | CODE `abstract` | 抽象的対象

<!-- END_FACET_NODE -->

## FACET_NODE `type::endurant`

- FACET: `type`
- NODE_KEY: `type::endurant`
- CODE: `endurant`
- LABEL: 持続体
- PARENT_KEY: `type::ontology`
- PATH_CODES: `ontology` > `endurant`
- PATH_LABELS: オントロジー型ファセット ＞ 持続体
- LEAF: false
- DIRECT_CHILDREN_COUNT: 8

### DIRECT_CHILDREN

- `type::endurant.human` | CODE `endurant.human` | 人物
- `type::endurant.animal` | CODE `endurant.animal` | 動物
- `type::endurant.natural_body` | CODE `endurant.natural_body` | 自然物
- `type::endurant.geo_feature` | CODE `endurant.geo_feature` | 自然地物
- `type::endurant.artifact` | CODE `endurant.artifact` | 人工物
- `type::endurant.social_object` | CODE `endurant.social_object` | 制度・組織
- `type::endurant.information_object` | CODE `endurant.information_object` | 情報オブジェクト
- `type::endurant.collection` | CODE `endurant.collection` | 集合

<!-- END_FACET_NODE -->

## FACET_NODE `type::endurant.human`

- FACET: `type`
- NODE_KEY: `type::endurant.human`
- CODE: `endurant.human`
- LABEL: 人物
- PARENT_KEY: `type::endurant`
- PATH_CODES: `ontology` > `endurant` > `endurant.human`
- PATH_LABELS: オントロジー型ファセット ＞ 持続体 ＞ 人物
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

### INCLUDING

個人名，歴史上の人物，作家，研究者，発明家など

<!-- END_FACET_NODE -->

## FACET_NODE `type::endurant.animal`

- FACET: `type`
- NODE_KEY: `type::endurant.animal`
- CODE: `endurant.animal`
- LABEL: 動物
- PARENT_KEY: `type::endurant`
- PATH_CODES: `ontology` > `endurant` > `endurant.animal`
- PATH_LABELS: オントロジー型ファセット ＞ 持続体 ＞ 動物
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

### INCLUDING

人間以外の動物種または個体

<!-- END_FACET_NODE -->

## FACET_NODE `type::endurant.natural_body`

- FACET: `type`
- NODE_KEY: `type::endurant.natural_body`
- CODE: `endurant.natural_body`
- LABEL: 自然物
- PARENT_KEY: `type::endurant`
- PATH_CODES: `ontology` > `endurant` > `endurant.natural_body`
- PATH_LABELS: オントロジー型ファセット ＞ 持続体 ＞ 自然物
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

### INCLUDING

鉱物，植物個体，天体，化学元素など

<!-- END_FACET_NODE -->

## FACET_NODE `type::endurant.geo_feature`

- FACET: `type`
- NODE_KEY: `type::endurant.geo_feature`
- CODE: `endurant.geo_feature`
- LABEL: 自然地物
- PARENT_KEY: `type::endurant`
- PATH_CODES: `ontology` > `endurant` > `endurant.geo_feature`
- PATH_LABELS: オントロジー型ファセット ＞ 持続体 ＞ 自然地物
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

### INCLUDING

山脈，河川，湖沼，峡谷など場所と結びついた地物

<!-- END_FACET_NODE -->

## FACET_NODE `type::endurant.artifact`

- FACET: `type`
- NODE_KEY: `type::endurant.artifact`
- CODE: `endurant.artifact`
- LABEL: 人工物
- PARENT_KEY: `type::endurant`
- PATH_CODES: `ontology` > `endurant` > `endurant.artifact`
- PATH_LABELS: オントロジー型ファセット ＞ 持続体 ＞ 人工物
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

### INCLUDING

機械，建造物，乗り物，製品，道具，料理そのもの

<!-- END_FACET_NODE -->

## FACET_NODE `type::endurant.social_object`

- FACET: `type`
- NODE_KEY: `type::endurant.social_object`
- CODE: `endurant.social_object`
- LABEL: 制度・組織
- PARENT_KEY: `type::endurant`
- PATH_CODES: `ontology` > `endurant` > `endurant.social_object`
- PATH_LABELS: オントロジー型ファセット ＞ 持続体 ＞ 制度・組織
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

### INCLUDING

官庁，企業，学校，法律上の制度，役職，団体

<!-- END_FACET_NODE -->

## FACET_NODE `type::endurant.information_object`

- FACET: `type`
- NODE_KEY: `type::endurant.information_object`
- CODE: `endurant.information_object`
- LABEL: 情報オブジェクト
- PARENT_KEY: `type::endurant`
- PATH_CODES: `ontology` > `endurant` > `endurant.information_object`
- PATH_LABELS: オントロジー型ファセット ＞ 持続体 ＞ 情報オブジェクト
- LEAF: false
- DIRECT_CHILDREN_COUNT: 5

### DIRECT_CHILDREN

- `type::endurant.information_object.work` | CODE `endurant.information_object.work` | 作品
- `type::endurant.information_object.theory` | CODE `endurant.information_object.theory` | 理論
- `type::endurant.information_object.law` | CODE `endurant.information_object.law` | 法則・定理
- `type::endurant.information_object.concept` | CODE `endurant.information_object.concept` | 概念
- `type::endurant.information_object.standard` | CODE `endurant.information_object.standard` | 規格・基準

### INCLUDING

媒体から独立した内容としての作品・理論・定理・概念・規格

<!-- END_FACET_NODE -->

## FACET_NODE `type::endurant.information_object.work`

- FACET: `type`
- NODE_KEY: `type::endurant.information_object.work`
- CODE: `endurant.information_object.work`
- LABEL: 作品
- PARENT_KEY: `type::endurant.information_object`
- PATH_CODES: `ontology` > `endurant` > `endurant.information_object` > `endurant.information_object.work`
- PATH_LABELS: オントロジー型ファセット ＞ 持続体 ＞ 情報オブジェクト ＞ 作品
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

### INCLUDING

小説，映画，楽曲，絵画などの作品内容

<!-- END_FACET_NODE -->

## FACET_NODE `type::endurant.information_object.theory`

- FACET: `type`
- NODE_KEY: `type::endurant.information_object.theory`
- CODE: `endurant.information_object.theory`
- LABEL: 理論
- PARENT_KEY: `type::endurant.information_object`
- PATH_CODES: `ontology` > `endurant` > `endurant.information_object` > `endurant.information_object.theory`
- PATH_LABELS: オントロジー型ファセット ＞ 持続体 ＞ 情報オブジェクト ＞ 理論
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

### INCLUDING

科学理論，学説，モデル

<!-- END_FACET_NODE -->

## FACET_NODE `type::endurant.information_object.law`

- FACET: `type`
- NODE_KEY: `type::endurant.information_object.law`
- CODE: `endurant.information_object.law`
- LABEL: 法則・定理
- PARENT_KEY: `type::endurant.information_object`
- PATH_CODES: `ontology` > `endurant` > `endurant.information_object` > `endurant.information_object.law`
- PATH_LABELS: オントロジー型ファセット ＞ 持続体 ＞ 情報オブジェクト ＞ 法則・定理
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

### INCLUDING

自然法則，数学定理，経験法則

<!-- END_FACET_NODE -->

## FACET_NODE `type::endurant.information_object.concept`

- FACET: `type`
- NODE_KEY: `type::endurant.information_object.concept`
- CODE: `endurant.information_object.concept`
- LABEL: 概念
- PARENT_KEY: `type::endurant.information_object`
- PATH_CODES: `ontology` > `endurant` > `endurant.information_object` > `endurant.information_object.concept`
- PATH_LABELS: オントロジー型ファセット ＞ 持続体 ＞ 情報オブジェクト ＞ 概念
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

### INCLUDING

用語，概念，思想，定義される知的対象

<!-- END_FACET_NODE -->

## FACET_NODE `type::endurant.information_object.standard`

- FACET: `type`
- NODE_KEY: `type::endurant.information_object.standard`
- CODE: `endurant.information_object.standard`
- LABEL: 規格・基準
- PARENT_KEY: `type::endurant.information_object`
- PATH_CODES: `ontology` > `endurant` > `endurant.information_object` > `endurant.information_object.standard`
- PATH_LABELS: オントロジー型ファセット ＞ 持続体 ＞ 情報オブジェクト ＞ 規格・基準
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

### INCLUDING

標準，規格，仕様，ガイドライン

<!-- END_FACET_NODE -->

## FACET_NODE `type::endurant.collection`

- FACET: `type`
- NODE_KEY: `type::endurant.collection`
- CODE: `endurant.collection`
- LABEL: 集合
- PARENT_KEY: `type::endurant`
- PATH_CODES: `ontology` > `endurant` > `endurant.collection`
- PATH_LABELS: オントロジー型ファセット ＞ 持続体 ＞ 集合
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

### INCLUDING

固定メンバーで構成されるチーム，委員会，バンドなど

<!-- END_FACET_NODE -->

## FACET_NODE `type::perdurant`

- FACET: `type`
- NODE_KEY: `type::perdurant`
- CODE: `perdurant`
- LABEL: 事象
- PARENT_KEY: `type::ontology`
- PATH_CODES: `ontology` > `perdurant`
- PATH_LABELS: オントロジー型ファセット ＞ 事象
- LEAF: false
- DIRECT_CHILDREN_COUNT: 3

### DIRECT_CHILDREN

- `type::perdurant.event` | CODE `perdurant.event` | 出来事
- `type::perdurant.process` | CODE `perdurant.process` | 過程
- `type::perdurant.state` | CODE `perdurant.state` | 状態

<!-- END_FACET_NODE -->

## FACET_NODE `type::perdurant.event`

- FACET: `type`
- NODE_KEY: `type::perdurant.event`
- CODE: `perdurant.event`
- LABEL: 出来事
- PARENT_KEY: `type::perdurant`
- PATH_CODES: `ontology` > `perdurant` > `perdurant.event`
- PATH_LABELS: オントロジー型ファセット ＞ 事象 ＞ 出来事
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

### INCLUDING

戦争，会議，災害，大会，事件，発見の回

<!-- END_FACET_NODE -->

## FACET_NODE `type::perdurant.process`

- FACET: `type`
- NODE_KEY: `type::perdurant.process`
- CODE: `perdurant.process`
- LABEL: 過程
- PARENT_KEY: `type::perdurant`
- PATH_CODES: `ontology` > `perdurant` > `perdurant.process`
- PATH_LABELS: オントロジー型ファセット ＞ 事象 ＞ 過程
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

### INCLUDING

反応，活動，製造，研究，運用プロセス

<!-- END_FACET_NODE -->

## FACET_NODE `type::perdurant.state`

- FACET: `type`
- NODE_KEY: `type::perdurant.state`
- CODE: `perdurant.state`
- LABEL: 状態
- PARENT_KEY: `type::perdurant`
- PATH_CODES: `ontology` > `perdurant` > `perdurant.state`
- PATH_LABELS: オントロジー型ファセット ＞ 事象 ＞ 状態
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

### INCLUDING

継続する状態，相，宣言下の状態，社会状況

<!-- END_FACET_NODE -->

## FACET_NODE `type::abstract`

- FACET: `type`
- NODE_KEY: `type::abstract`
- CODE: `abstract`
- LABEL: 抽象的対象
- PARENT_KEY: `type::ontology`
- PATH_CODES: `ontology` > `abstract`
- PATH_LABELS: オントロジー型ファセット ＞ 抽象的対象
- LEAF: false
- DIRECT_CHILDREN_COUNT: 4

### DIRECT_CHILDREN

- `type::abstract.place` | CODE `abstract.place` | 場所・領域
- `type::abstract.time` | CODE `abstract.time` | 時間
- `type::abstract.quality` | CODE `abstract.quality` | 性質
- `type::abstract.quantity` | CODE `abstract.quantity` | 数量

<!-- END_FACET_NODE -->

## FACET_NODE `type::abstract.place`

- FACET: `type`
- NODE_KEY: `type::abstract.place`
- CODE: `abstract.place`
- LABEL: 場所・領域
- PARENT_KEY: `type::abstract`
- PATH_CODES: `ontology` > `abstract` > `abstract.place`
- PATH_LABELS: オントロジー型ファセット ＞ 抽象的対象 ＞ 場所・領域
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

### INCLUDING

行政区画，地域，海域，施設の場所としての側面

<!-- END_FACET_NODE -->

## FACET_NODE `type::abstract.time`

- FACET: `type`
- NODE_KEY: `type::abstract.time`
- CODE: `abstract.time`
- LABEL: 時間
- PARENT_KEY: `type::abstract`
- PATH_CODES: `ontology` > `abstract` > `abstract.time`
- PATH_LABELS: オントロジー型ファセット ＞ 抽象的対象 ＞ 時間
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

### INCLUDING

時代区分，年代，暦日，年次

<!-- END_FACET_NODE -->

## FACET_NODE `type::abstract.quality`

- FACET: `type`
- NODE_KEY: `type::abstract.quality`
- CODE: `abstract.quality`
- LABEL: 性質
- PARENT_KEY: `type::abstract`
- PATH_CODES: `ontology` > `abstract` > `abstract.quality`
- PATH_LABELS: オントロジー型ファセット ＞ 抽象的対象 ＞ 性質
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

### INCLUDING

属性，物性，色，形，性能指標

<!-- END_FACET_NODE -->

## FACET_NODE `type::abstract.quantity`

- FACET: `type`
- NODE_KEY: `type::abstract.quantity`
- CODE: `abstract.quantity`
- LABEL: 数量
- PARENT_KEY: `type::abstract`
- PATH_CODES: `ontology` > `abstract` > `abstract.quantity`
- PATH_LABELS: オントロジー型ファセット ＞ 抽象的対象 ＞ 数量
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

### INCLUDING

数，定数，単位，測定量，指標値

<!-- END_FACET_NODE -->
