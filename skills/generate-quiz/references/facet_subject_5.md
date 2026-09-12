# subject ファセットカタログ — 最上位コード 5

各 `FACET_NODE` ブロックは一つの親ノードと、その直接の子を自己完結的に収録しています。
細分化する場合は、検索で得た親ブロックの `DIRECT_CHILDREN` を全件比較してください。
ラベル・コード・注記は元データ由来です。独自ノードを追加しないでください。

## FACET_NODE `subject::5`

- FACET: `subject`
- NODE_KEY: `subject::5`
- CODE: `5`
- LABEL: 数学．自然科学
- PARENT_KEY: `subject::ROOT`
- PATH_CODES: `5`
- PATH_LABELS: 数学．自然科学
- LEAF: false
- DIRECT_CHILDREN_COUNT: 10

### DIRECT_CHILDREN

- `subject::502/504` | CODE `502/504` | 環境科学．資源保護．環境に対する脅威とそれからの保護
- `subject::51` | CODE `51` | 数学
- `subject::52` | CODE `52` | 天文学．天体物理学．宇宙論．測地学
- `subject::53` | CODE `53` | 物理学
- `subject::54` | CODE `54` | 化学．結晶学．鉱物学
- `subject::55` | CODE `55` | 地球科学．地質学
- `subject::56` | CODE `56` | 古生物学
- `subject::57` | CODE `57` | 生物科学一般
- `subject::58` | CODE `58` | 植物学
- `subject::59` | CODE `59` | 動物学

<!-- END_FACET_NODE -->

## FACET_NODE `subject::502/504`

- FACET: `subject`
- NODE_KEY: `subject::502/504`
- CODE: `502/504`
- LABEL: 環境科学．資源保護．環境に対する脅威とそれからの保護
- PARENT_KEY: `subject::5`
- PATH_CODES: `5` > `502/504`
- PATH_LABELS: 数学．自然科学 ＞ 環境科学．資源保護．環境に対する脅威とそれからの保護
- LEAF: false
- DIRECT_CHILDREN_COUNT: 2

### DIRECT_CHILDREN

- `subject::502` | CODE `502` | 環境とその保護
- `subject::504` | CODE `504` | 環境への脅威

<!-- END_FACET_NODE -->

## FACET_NODE `subject::502`

- FACET: `subject`
- NODE_KEY: `subject::502`
- CODE: `502`
- LABEL: 環境とその保護
- PARENT_KEY: `subject::502/504`
- PATH_CODES: `5` > `502/504` > `502`
- PATH_LABELS: 数学．自然科学 ＞ 環境科学．資源保護．環境に対する脅威とそれからの保護 ＞ 環境とその保護
- LEAF: false
- DIRECT_CHILDREN_COUNT: 1

### DIRECT_CHILDREN

- `subject::502.3/.7` | CODE `502.3/.7` | 環境の構成部分

<!-- END_FACET_NODE -->

## FACET_NODE `subject::502.3/.7`

- FACET: `subject`
- NODE_KEY: `subject::502.3/.7`
- CODE: `502.3/.7`
- LABEL: 環境の構成部分
- PARENT_KEY: `subject::502`
- PATH_CODES: `5` > `502/504` > `502` > `502.3/.7`
- PATH_LABELS: 数学．自然科学 ＞ 環境科学．資源保護．環境に対する脅威とそれからの保護 ＞ 環境とその保護 ＞ 環境の構成部分
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::504`

- FACET: `subject`
- NODE_KEY: `subject::504`
- CODE: `504`
- LABEL: 環境への脅威
- PARENT_KEY: `subject::502/504`
- PATH_CODES: `5` > `502/504` > `504`
- PATH_LABELS: 数学．自然科学 ＞ 環境科学．資源保護．環境に対する脅威とそれからの保護 ＞ 環境への脅威
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::51`

- FACET: `subject`
- NODE_KEY: `subject::51`
- CODE: `51`
- LABEL: 数学
- PARENT_KEY: `subject::5`
- PATH_CODES: `5` > `51`
- PATH_LABELS: 数学．自然科学 ＞ 数学
- LEAF: false
- DIRECT_CHILDREN_COUNT: 11

### DIRECT_CHILDREN

- `subject::510` | CODE `510` | 数学の基本的・一般的問題
- `subject::511` | CODE `511` | 整数論
- `subject::512` | CODE `512` | 代数学
- `subject::514` | CODE `514` | 幾何学
- `subject::515.1` | CODE `515.1` | 位相数学
- `subject::517` | CODE `517` | 解析学
- `subject::519.1` | CODE `519.1` | 組合せ論．グラフ理論
- `subject::519.2` | CODE `519.2` | 確率論．数理統計学
- `subject::519.6` | CODE `519.6` | コンピュータ数学．数値解析
- `subject::519.7` | CODE `519.7` | 数学的サイバネティックス
- `subject::519.8` | CODE `519.8` | オペレーションズ・リサーチ(OR)の数学的理論

<!-- END_FACET_NODE -->

## FACET_NODE `subject::510`

- FACET: `subject`
- NODE_KEY: `subject::510`
- CODE: `510`
- LABEL: 数学の基本的・一般的問題
- PARENT_KEY: `subject::51`
- PATH_CODES: `5` > `51` > `510`
- PATH_LABELS: 数学．自然科学 ＞ 数学 ＞ 数学の基本的・一般的問題
- LEAF: false
- DIRECT_CHILDREN_COUNT: 3

### DIRECT_CHILDREN

- `subject::510.2` | CODE `510.2` | 記号論理学の一般的問題．数学基礎論
- `subject::510.3` | CODE `510.3` | 集合論
- `subject::510.6` | CODE `510.6` | 記号論理学

<!-- END_FACET_NODE -->

## FACET_NODE `subject::510.2`

- FACET: `subject`
- NODE_KEY: `subject::510.2`
- CODE: `510.2`
- LABEL: 記号論理学の一般的問題．数学基礎論
- PARENT_KEY: `subject::510`
- PATH_CODES: `5` > `51` > `510` > `510.2`
- PATH_LABELS: 数学．自然科学 ＞ 数学 ＞ 数学の基本的・一般的問題 ＞ 記号論理学の一般的問題．数学基礎論
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::510.3`

- FACET: `subject`
- NODE_KEY: `subject::510.3`
- CODE: `510.3`
- LABEL: 集合論
- PARENT_KEY: `subject::510`
- PATH_CODES: `5` > `51` > `510` > `510.3`
- PATH_LABELS: 数学．自然科学 ＞ 数学 ＞ 数学の基本的・一般的問題 ＞ 集合論
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::510.6`

- FACET: `subject`
- NODE_KEY: `subject::510.6`
- CODE: `510.6`
- LABEL: 記号論理学
- PARENT_KEY: `subject::510`
- PATH_CODES: `5` > `51` > `510` > `510.6`
- PATH_LABELS: 数学．自然科学 ＞ 数学 ＞ 数学の基本的・一般的問題 ＞ 記号論理学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::511`

- FACET: `subject`
- NODE_KEY: `subject::511`
- CODE: `511`
- LABEL: 整数論
- PARENT_KEY: `subject::51`
- PATH_CODES: `5` > `51` > `511`
- PATH_LABELS: 数学．自然科学 ＞ 数学 ＞ 整数論
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::512`

- FACET: `subject`
- NODE_KEY: `subject::512`
- CODE: `512`
- LABEL: 代数学
- PARENT_KEY: `subject::51`
- PATH_CODES: `5` > `51` > `512`
- PATH_LABELS: 数学．自然科学 ＞ 数学 ＞ 代数学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::514`

- FACET: `subject`
- NODE_KEY: `subject::514`
- CODE: `514`
- LABEL: 幾何学
- PARENT_KEY: `subject::51`
- PATH_CODES: `5` > `51` > `514`
- PATH_LABELS: 数学．自然科学 ＞ 数学 ＞ 幾何学
- LEAF: false
- DIRECT_CHILDREN_COUNT: 1

### DIRECT_CHILDREN

- `subject::514.7` | CODE `514.7` | 微分幾何学．幾何学における代数的・解析的方法

<!-- END_FACET_NODE -->

## FACET_NODE `subject::514.7`

- FACET: `subject`
- NODE_KEY: `subject::514.7`
- CODE: `514.7`
- LABEL: 微分幾何学．幾何学における代数的・解析的方法
- PARENT_KEY: `subject::514`
- PATH_CODES: `5` > `51` > `514` > `514.7`
- PATH_LABELS: 数学．自然科学 ＞ 数学 ＞ 幾何学 ＞ 微分幾何学．幾何学における代数的・解析的方法
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::515.1`

- FACET: `subject`
- NODE_KEY: `subject::515.1`
- CODE: `515.1`
- LABEL: 位相数学
- PARENT_KEY: `subject::51`
- PATH_CODES: `5` > `51` > `515.1`
- PATH_LABELS: 数学．自然科学 ＞ 数学 ＞ 位相数学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::517`

- FACET: `subject`
- NODE_KEY: `subject::517`
- CODE: `517`
- LABEL: 解析学
- PARENT_KEY: `subject::51`
- PATH_CODES: `5` > `51` > `517`
- PATH_LABELS: 数学．自然科学 ＞ 数学 ＞ 解析学
- LEAF: false
- DIRECT_CHILDREN_COUNT: 1

### DIRECT_CHILDREN

- `subject::517.9` | CODE `517.9` | 微分方程式．積分方程式．その他の関数方程式

<!-- END_FACET_NODE -->

## FACET_NODE `subject::517.9`

- FACET: `subject`
- NODE_KEY: `subject::517.9`
- CODE: `517.9`
- LABEL: 微分方程式．積分方程式．その他の関数方程式
- PARENT_KEY: `subject::517`
- PATH_CODES: `5` > `51` > `517` > `517.9`
- PATH_LABELS: 数学．自然科学 ＞ 数学 ＞ 解析学 ＞ 微分方程式．積分方程式．その他の関数方程式
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::519.1`

- FACET: `subject`
- NODE_KEY: `subject::519.1`
- CODE: `519.1`
- LABEL: 組合せ論．グラフ理論
- PARENT_KEY: `subject::51`
- PATH_CODES: `5` > `51` > `519.1`
- PATH_LABELS: 数学．自然科学 ＞ 数学 ＞ 組合せ論．グラフ理論
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::519.2`

- FACET: `subject`
- NODE_KEY: `subject::519.2`
- CODE: `519.2`
- LABEL: 確率論．数理統計学
- PARENT_KEY: `subject::51`
- PATH_CODES: `5` > `51` > `519.2`
- PATH_LABELS: 数学．自然科学 ＞ 数学 ＞ 確率論．数理統計学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::519.6`

- FACET: `subject`
- NODE_KEY: `subject::519.6`
- CODE: `519.6`
- LABEL: コンピュータ数学．数値解析
- PARENT_KEY: `subject::51`
- PATH_CODES: `5` > `51` > `519.6`
- PATH_LABELS: 数学．自然科学 ＞ 数学 ＞ コンピュータ数学．数値解析
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::519.7`

- FACET: `subject`
- NODE_KEY: `subject::519.7`
- CODE: `519.7`
- LABEL: 数学的サイバネティックス
- PARENT_KEY: `subject::51`
- PATH_CODES: `5` > `51` > `519.7`
- PATH_LABELS: 数学．自然科学 ＞ 数学 ＞ 数学的サイバネティックス
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::519.8`

- FACET: `subject`
- NODE_KEY: `subject::519.8`
- CODE: `519.8`
- LABEL: オペレーションズ・リサーチ(OR)の数学的理論
- PARENT_KEY: `subject::51`
- PATH_CODES: `5` > `51` > `519.8`
- PATH_LABELS: 数学．自然科学 ＞ 数学 ＞ オペレーションズ・リサーチ(OR)の数学的理論
- LEAF: false
- DIRECT_CHILDREN_COUNT: 2

### DIRECT_CHILDREN

- `subject::519.83` | CODE `519.83` | ゲーム理論
- `subject::519.85` | CODE `519.85` | 数理計画法

<!-- END_FACET_NODE -->

## FACET_NODE `subject::519.83`

- FACET: `subject`
- NODE_KEY: `subject::519.83`
- CODE: `519.83`
- LABEL: ゲーム理論
- PARENT_KEY: `subject::519.8`
- PATH_CODES: `5` > `51` > `519.8` > `519.83`
- PATH_LABELS: 数学．自然科学 ＞ 数学 ＞ オペレーションズ・リサーチ(OR)の数学的理論 ＞ ゲーム理論
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::519.85`

- FACET: `subject`
- NODE_KEY: `subject::519.85`
- CODE: `519.85`
- LABEL: 数理計画法
- PARENT_KEY: `subject::519.8`
- PATH_CODES: `5` > `51` > `519.8` > `519.85`
- PATH_LABELS: 数学．自然科学 ＞ 数学 ＞ オペレーションズ・リサーチ(OR)の数学的理論 ＞ 数理計画法
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::52`

- FACET: `subject`
- NODE_KEY: `subject::52`
- CODE: `52`
- LABEL: 天文学．天体物理学．宇宙論．測地学
- PARENT_KEY: `subject::5`
- PATH_CODES: `5` > `52`
- PATH_LABELS: 数学．自然科学 ＞ 天文学．天体物理学．宇宙論．測地学
- LEAF: false
- DIRECT_CHILDREN_COUNT: 5

### DIRECT_CHILDREN

- `subject::520` | CODE `520` | 天文学のための装置と手法
- `subject::521` | CODE `521` | 理論天文学．天体力学
- `subject::523` | CODE `523` | 太陽系
- `subject::524` | CODE `524` | 恒星．恒星系．宇宙
- `subject::528` | CODE `528` | 測地学．測量．写真測量．リモートセンシング．地図作成法

<!-- END_FACET_NODE -->

## FACET_NODE `subject::520`

- FACET: `subject`
- NODE_KEY: `subject::520`
- CODE: `520`
- LABEL: 天文学のための装置と手法
- PARENT_KEY: `subject::52`
- PATH_CODES: `5` > `52` > `520`
- PATH_LABELS: 数学．自然科学 ＞ 天文学．天体物理学．宇宙論．測地学 ＞ 天文学のための装置と手法
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::521`

- FACET: `subject`
- NODE_KEY: `subject::521`
- CODE: `521`
- LABEL: 理論天文学．天体力学
- PARENT_KEY: `subject::52`
- PATH_CODES: `5` > `52` > `521`
- PATH_LABELS: 数学．自然科学 ＞ 天文学．天体物理学．宇宙論．測地学 ＞ 理論天文学．天体力学
- LEAF: false
- DIRECT_CHILDREN_COUNT: 1

### DIRECT_CHILDREN

- `subject::521.9` | CODE `521.9` | 位置天文学．球面天文学

<!-- END_FACET_NODE -->

## FACET_NODE `subject::521.9`

- FACET: `subject`
- NODE_KEY: `subject::521.9`
- CODE: `521.9`
- LABEL: 位置天文学．球面天文学
- PARENT_KEY: `subject::521`
- PATH_CODES: `5` > `52` > `521` > `521.9`
- PATH_LABELS: 数学．自然科学 ＞ 天文学．天体物理学．宇宙論．測地学 ＞ 理論天文学．天体力学 ＞ 位置天文学．球面天文学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::523`

- FACET: `subject`
- NODE_KEY: `subject::523`
- CODE: `523`
- LABEL: 太陽系
- PARENT_KEY: `subject::52`
- PATH_CODES: `5` > `52` > `523`
- PATH_LABELS: 数学．自然科学 ＞ 天文学．天体物理学．宇宙論．測地学 ＞ 太陽系
- LEAF: false
- DIRECT_CHILDREN_COUNT: 4

### DIRECT_CHILDREN

- `subject::523.3` | CODE `523.3` | 地球－月系
- `subject::523.4` | CODE `523.4` | 惑星および衛星．惑星学
- `subject::523.6` | CODE `523.6` | 惑星間の物質．彗星．流星．隕石
- `subject::523.9` | CODE `523.9` | 太陽．太陽物理学

<!-- END_FACET_NODE -->

## FACET_NODE `subject::523.3`

- FACET: `subject`
- NODE_KEY: `subject::523.3`
- CODE: `523.3`
- LABEL: 地球－月系
- PARENT_KEY: `subject::523`
- PATH_CODES: `5` > `52` > `523` > `523.3`
- PATH_LABELS: 数学．自然科学 ＞ 天文学．天体物理学．宇宙論．測地学 ＞ 太陽系 ＞ 地球－月系
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::523.4`

- FACET: `subject`
- NODE_KEY: `subject::523.4`
- CODE: `523.4`
- LABEL: 惑星および衛星．惑星学
- PARENT_KEY: `subject::523`
- PATH_CODES: `5` > `52` > `523` > `523.4`
- PATH_LABELS: 数学．自然科学 ＞ 天文学．天体物理学．宇宙論．測地学 ＞ 太陽系 ＞ 惑星および衛星．惑星学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::523.6`

- FACET: `subject`
- NODE_KEY: `subject::523.6`
- CODE: `523.6`
- LABEL: 惑星間の物質．彗星．流星．隕石
- PARENT_KEY: `subject::523`
- PATH_CODES: `5` > `52` > `523` > `523.6`
- PATH_LABELS: 数学．自然科学 ＞ 天文学．天体物理学．宇宙論．測地学 ＞ 太陽系 ＞ 惑星間の物質．彗星．流星．隕石
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::523.9`

- FACET: `subject`
- NODE_KEY: `subject::523.9`
- CODE: `523.9`
- LABEL: 太陽．太陽物理学
- PARENT_KEY: `subject::523`
- PATH_CODES: `5` > `52` > `523` > `523.9`
- PATH_LABELS: 数学．自然科学 ＞ 天文学．天体物理学．宇宙論．測地学 ＞ 太陽系 ＞ 太陽．太陽物理学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::524`

- FACET: `subject`
- NODE_KEY: `subject::524`
- CODE: `524`
- LABEL: 恒星．恒星系．宇宙
- PARENT_KEY: `subject::52`
- PATH_CODES: `5` > `52` > `524`
- PATH_LABELS: 数学．自然科学 ＞ 天文学．天体物理学．宇宙論．測地学 ＞ 恒星．恒星系．宇宙
- LEAF: false
- DIRECT_CHILDREN_COUNT: 7

### DIRECT_CHILDREN

- `subject::524.1` | CODE `524.1` | 宇宙線．一次宇宙線
- `subject::524.3` | CODE `524.3` | 恒星
- `subject::524.4` | CODE `524.4` | 星団．星のアソシエーション
- `subject::524.5` | CODE `524.5` | 星間物質．銀河星雲
- `subject::524.6` | CODE `524.6` | 銀河
- `subject::524.7` | CODE `524.7` | 銀河系外星雲
- `subject::524.8` | CODE `524.8` | 宇宙．全宇宙．宇宙論

<!-- END_FACET_NODE -->

## FACET_NODE `subject::524.1`

- FACET: `subject`
- NODE_KEY: `subject::524.1`
- CODE: `524.1`
- LABEL: 宇宙線．一次宇宙線
- PARENT_KEY: `subject::524`
- PATH_CODES: `5` > `52` > `524` > `524.1`
- PATH_LABELS: 数学．自然科学 ＞ 天文学．天体物理学．宇宙論．測地学 ＞ 恒星．恒星系．宇宙 ＞ 宇宙線．一次宇宙線
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::524.3`

- FACET: `subject`
- NODE_KEY: `subject::524.3`
- CODE: `524.3`
- LABEL: 恒星
- PARENT_KEY: `subject::524`
- PATH_CODES: `5` > `52` > `524` > `524.3`
- PATH_LABELS: 数学．自然科学 ＞ 天文学．天体物理学．宇宙論．測地学 ＞ 恒星．恒星系．宇宙 ＞ 恒星
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::524.4`

- FACET: `subject`
- NODE_KEY: `subject::524.4`
- CODE: `524.4`
- LABEL: 星団．星のアソシエーション
- PARENT_KEY: `subject::524`
- PATH_CODES: `5` > `52` > `524` > `524.4`
- PATH_LABELS: 数学．自然科学 ＞ 天文学．天体物理学．宇宙論．測地学 ＞ 恒星．恒星系．宇宙 ＞ 星団．星のアソシエーション
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::524.5`

- FACET: `subject`
- NODE_KEY: `subject::524.5`
- CODE: `524.5`
- LABEL: 星間物質．銀河星雲
- PARENT_KEY: `subject::524`
- PATH_CODES: `5` > `52` > `524` > `524.5`
- PATH_LABELS: 数学．自然科学 ＞ 天文学．天体物理学．宇宙論．測地学 ＞ 恒星．恒星系．宇宙 ＞ 星間物質．銀河星雲
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::524.6`

- FACET: `subject`
- NODE_KEY: `subject::524.6`
- CODE: `524.6`
- LABEL: 銀河
- PARENT_KEY: `subject::524`
- PATH_CODES: `5` > `52` > `524` > `524.6`
- PATH_LABELS: 数学．自然科学 ＞ 天文学．天体物理学．宇宙論．測地学 ＞ 恒星．恒星系．宇宙 ＞ 銀河
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::524.7`

- FACET: `subject`
- NODE_KEY: `subject::524.7`
- CODE: `524.7`
- LABEL: 銀河系外星雲
- PARENT_KEY: `subject::524`
- PATH_CODES: `5` > `52` > `524` > `524.7`
- PATH_LABELS: 数学．自然科学 ＞ 天文学．天体物理学．宇宙論．測地学 ＞ 恒星．恒星系．宇宙 ＞ 銀河系外星雲
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::524.8`

- FACET: `subject`
- NODE_KEY: `subject::524.8`
- CODE: `524.8`
- LABEL: 宇宙．全宇宙．宇宙論
- PARENT_KEY: `subject::524`
- PATH_CODES: `5` > `52` > `524` > `524.8`
- PATH_LABELS: 数学．自然科学 ＞ 天文学．天体物理学．宇宙論．測地学 ＞ 恒星．恒星系．宇宙 ＞ 宇宙．全宇宙．宇宙論
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::528`

- FACET: `subject`
- NODE_KEY: `subject::528`
- CODE: `528`
- LABEL: 測地学．測量．写真測量．リモートセンシング．地図作成法
- PARENT_KEY: `subject::52`
- PATH_CODES: `5` > `52` > `528`
- PATH_LABELS: 数学．自然科学 ＞ 天文学．天体物理学．宇宙論．測地学 ＞ 測地学．測量．写真測量．リモートセンシング．地図作成法
- LEAF: false
- DIRECT_CHILDREN_COUNT: 7

### DIRECT_CHILDREN

- `subject::528.1` | CODE `528.1` | 測地学と写真測量法における誤差と補正の理論
- `subject::528.2` | CODE `528.2` | 地球の形状．地球の測定．数理の測地学
- `subject::528.3` | CODE `528.3` | 測地測量
- `subject::528.4` | CODE `528.4` | 野外測量．陸地測量．土地測量
- `subject::528.5` | CODE `528.5` | 測地機器および装置
- `subject::528.8` | CODE `528.8` | リモート・センシング
- `subject::528.9` | CODE `528.9` | 地図学．地図作成

<!-- END_FACET_NODE -->

## FACET_NODE `subject::528.1`

- FACET: `subject`
- NODE_KEY: `subject::528.1`
- CODE: `528.1`
- LABEL: 測地学と写真測量法における誤差と補正の理論
- PARENT_KEY: `subject::528`
- PATH_CODES: `5` > `52` > `528` > `528.1`
- PATH_LABELS: 数学．自然科学 ＞ 天文学．天体物理学．宇宙論．測地学 ＞ 測地学．測量．写真測量．リモートセンシング．地図作成法 ＞ 測地学と写真測量法における誤差と補正の理論
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::528.2`

- FACET: `subject`
- NODE_KEY: `subject::528.2`
- CODE: `528.2`
- LABEL: 地球の形状．地球の測定．数理の測地学
- PARENT_KEY: `subject::528`
- PATH_CODES: `5` > `52` > `528` > `528.2`
- PATH_LABELS: 数学．自然科学 ＞ 天文学．天体物理学．宇宙論．測地学 ＞ 測地学．測量．写真測量．リモートセンシング．地図作成法 ＞ 地球の形状．地球の測定．数理の測地学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::528.3`

- FACET: `subject`
- NODE_KEY: `subject::528.3`
- CODE: `528.3`
- LABEL: 測地測量
- PARENT_KEY: `subject::528`
- PATH_CODES: `5` > `52` > `528` > `528.3`
- PATH_LABELS: 数学．自然科学 ＞ 天文学．天体物理学．宇宙論．測地学 ＞ 測地学．測量．写真測量．リモートセンシング．地図作成法 ＞ 測地測量
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::528.4`

- FACET: `subject`
- NODE_KEY: `subject::528.4`
- CODE: `528.4`
- LABEL: 野外測量．陸地測量．土地測量
- PARENT_KEY: `subject::528`
- PATH_CODES: `5` > `52` > `528` > `528.4`
- PATH_LABELS: 数学．自然科学 ＞ 天文学．天体物理学．宇宙論．測地学 ＞ 測地学．測量．写真測量．リモートセンシング．地図作成法 ＞ 野外測量．陸地測量．土地測量
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::528.5`

- FACET: `subject`
- NODE_KEY: `subject::528.5`
- CODE: `528.5`
- LABEL: 測地機器および装置
- PARENT_KEY: `subject::528`
- PATH_CODES: `5` > `52` > `528` > `528.5`
- PATH_LABELS: 数学．自然科学 ＞ 天文学．天体物理学．宇宙論．測地学 ＞ 測地学．測量．写真測量．リモートセンシング．地図作成法 ＞ 測地機器および装置
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::528.8`

- FACET: `subject`
- NODE_KEY: `subject::528.8`
- CODE: `528.8`
- LABEL: リモート・センシング
- PARENT_KEY: `subject::528`
- PATH_CODES: `5` > `52` > `528` > `528.8`
- PATH_LABELS: 数学．自然科学 ＞ 天文学．天体物理学．宇宙論．測地学 ＞ 測地学．測量．写真測量．リモートセンシング．地図作成法 ＞ リモート・センシング
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::528.9`

- FACET: `subject`
- NODE_KEY: `subject::528.9`
- CODE: `528.9`
- LABEL: 地図学．地図作成
- PARENT_KEY: `subject::528`
- PATH_CODES: `5` > `52` > `528` > `528.9`
- PATH_LABELS: 数学．自然科学 ＞ 天文学．天体物理学．宇宙論．測地学 ＞ 測地学．測量．写真測量．リモートセンシング．地図作成法 ＞ 地図学．地図作成
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::53`

- FACET: `subject`
- NODE_KEY: `subject::53`
- CODE: `53`
- LABEL: 物理学
- PARENT_KEY: `subject::5`
- PATH_CODES: `5` > `53`
- PATH_LABELS: 数学．自然科学 ＞ 物理学
- LEAF: false
- DIRECT_CHILDREN_COUNT: 7

### DIRECT_CHILDREN

- `subject::53.01/.09` | CODE `53.01/.09` | 物理学現象，観測・測定・研究方法の理論および性質に関する固有補助番号
- `subject::531/534` | CODE `531/534` | 力学
- `subject::535` | CODE `535` | 光学
- `subject::536` | CODE `536` | 熱．熱力学．統計物理学
- `subject::537` | CODE `537` | 電気学．磁気学．電磁気学
- `subject::538.9` | CODE `538.9` | 固体物理学
- `subject::539` | CODE `539` | 物質の物理的性質

<!-- END_FACET_NODE -->

## FACET_NODE `subject::53.01/.09`

- FACET: `subject`
- NODE_KEY: `subject::53.01/.09`
- CODE: `53.01/.09`
- LABEL: 物理学現象，観測・測定・研究方法の理論および性質に関する固有補助番号
- PARENT_KEY: `subject::53`
- PATH_CODES: `5` > `53` > `53.01/.09`
- PATH_LABELS: 数学．自然科学 ＞ 物理学 ＞ 物理学現象，観測・測定・研究方法の理論および性質に関する固有補助番号
- LEAF: false
- DIRECT_CHILDREN_COUNT: 9

### DIRECT_CHILDREN

- `subject::53.01` | CODE `53.01` | 現象の理論と性質
- `subject::53.02` | CODE `53.02` | 現象の一般法則
- `subject::53.03` | CODE `53.03` | 現象の発生と原因
- `subject::53.04` | CODE `53.04` | 現象の効果
- `subject::53.05` | CODE `53.05` | 現象の観測と記録
- `subject::53.06` | CODE `53.06` | 現象の利用
- `subject::53.07` | CODE `53.07` | 現象の発生と研究のための装置
- `subject::53.08` | CODE `53.08` | 測定および測定装置の設計の一般的原理
- `subject::53.09` | CODE `53.09` | 基本的な物理的効果への現象の依存性

<!-- END_FACET_NODE -->

## FACET_NODE `subject::53.01`

- FACET: `subject`
- NODE_KEY: `subject::53.01`
- CODE: `53.01`
- LABEL: 現象の理論と性質
- PARENT_KEY: `subject::53.01/.09`
- PATH_CODES: `5` > `53` > `53.01/.09` > `53.01`
- PATH_LABELS: 数学．自然科学 ＞ 物理学 ＞ 物理学現象，観測・測定・研究方法の理論および性質に関する固有補助番号 ＞ 現象の理論と性質
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::53.02`

- FACET: `subject`
- NODE_KEY: `subject::53.02`
- CODE: `53.02`
- LABEL: 現象の一般法則
- PARENT_KEY: `subject::53.01/.09`
- PATH_CODES: `5` > `53` > `53.01/.09` > `53.02`
- PATH_LABELS: 数学．自然科学 ＞ 物理学 ＞ 物理学現象，観測・測定・研究方法の理論および性質に関する固有補助番号 ＞ 現象の一般法則
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::53.03`

- FACET: `subject`
- NODE_KEY: `subject::53.03`
- CODE: `53.03`
- LABEL: 現象の発生と原因
- PARENT_KEY: `subject::53.01/.09`
- PATH_CODES: `5` > `53` > `53.01/.09` > `53.03`
- PATH_LABELS: 数学．自然科学 ＞ 物理学 ＞ 物理学現象，観測・測定・研究方法の理論および性質に関する固有補助番号 ＞ 現象の発生と原因
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::53.04`

- FACET: `subject`
- NODE_KEY: `subject::53.04`
- CODE: `53.04`
- LABEL: 現象の効果
- PARENT_KEY: `subject::53.01/.09`
- PATH_CODES: `5` > `53` > `53.01/.09` > `53.04`
- PATH_LABELS: 数学．自然科学 ＞ 物理学 ＞ 物理学現象，観測・測定・研究方法の理論および性質に関する固有補助番号 ＞ 現象の効果
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::53.05`

- FACET: `subject`
- NODE_KEY: `subject::53.05`
- CODE: `53.05`
- LABEL: 現象の観測と記録
- PARENT_KEY: `subject::53.01/.09`
- PATH_CODES: `5` > `53` > `53.01/.09` > `53.05`
- PATH_LABELS: 数学．自然科学 ＞ 物理学 ＞ 物理学現象，観測・測定・研究方法の理論および性質に関する固有補助番号 ＞ 現象の観測と記録
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::53.06`

- FACET: `subject`
- NODE_KEY: `subject::53.06`
- CODE: `53.06`
- LABEL: 現象の利用
- PARENT_KEY: `subject::53.01/.09`
- PATH_CODES: `5` > `53` > `53.01/.09` > `53.06`
- PATH_LABELS: 数学．自然科学 ＞ 物理学 ＞ 物理学現象，観測・測定・研究方法の理論および性質に関する固有補助番号 ＞ 現象の利用
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::53.07`

- FACET: `subject`
- NODE_KEY: `subject::53.07`
- CODE: `53.07`
- LABEL: 現象の発生と研究のための装置
- PARENT_KEY: `subject::53.01/.09`
- PATH_CODES: `5` > `53` > `53.01/.09` > `53.07`
- PATH_LABELS: 数学．自然科学 ＞ 物理学 ＞ 物理学現象，観測・測定・研究方法の理論および性質に関する固有補助番号 ＞ 現象の発生と研究のための装置
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::53.08`

- FACET: `subject`
- NODE_KEY: `subject::53.08`
- CODE: `53.08`
- LABEL: 測定および測定装置の設計の一般的原理
- PARENT_KEY: `subject::53.01/.09`
- PATH_CODES: `5` > `53` > `53.01/.09` > `53.08`
- PATH_LABELS: 数学．自然科学 ＞ 物理学 ＞ 物理学現象，観測・測定・研究方法の理論および性質に関する固有補助番号 ＞ 測定および測定装置の設計の一般的原理
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::53.09`

- FACET: `subject`
- NODE_KEY: `subject::53.09`
- CODE: `53.09`
- LABEL: 基本的な物理的効果への現象の依存性
- PARENT_KEY: `subject::53.01/.09`
- PATH_CODES: `5` > `53` > `53.01/.09` > `53.09`
- PATH_LABELS: 数学．自然科学 ＞ 物理学 ＞ 物理学現象，観測・測定・研究方法の理論および性質に関する固有補助番号 ＞ 基本的な物理的効果への現象の依存性
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::531/534`

- FACET: `subject`
- NODE_KEY: `subject::531/534`
- CODE: `531/534`
- LABEL: 力学
- PARENT_KEY: `subject::53`
- PATH_CODES: `5` > `53` > `531/534`
- PATH_LABELS: 数学．自然科学 ＞ 物理学 ＞ 力学
- LEAF: false
- DIRECT_CHILDREN_COUNT: 4

### DIRECT_CHILDREN

- `subject::531` | CODE `531` | 一般力学．固体および剛体の力学
- `subject::532` | CODE `532` | 流体力学一般．液体の力学
- `subject::533` | CODE `533` | 気体の力学．空気力学．プラズマ物理学
- `subject::534` | CODE `534` | 振動．音響学

<!-- END_FACET_NODE -->

## FACET_NODE `subject::531`

- FACET: `subject`
- NODE_KEY: `subject::531`
- CODE: `531`
- LABEL: 一般力学．固体および剛体の力学
- PARENT_KEY: `subject::531/534`
- PATH_CODES: `5` > `53` > `531/534` > `531`
- PATH_LABELS: 数学．自然科学 ＞ 物理学 ＞ 力学 ＞ 一般力学．固体および剛体の力学
- LEAF: false
- DIRECT_CHILDREN_COUNT: 9

### DIRECT_CHILDREN

- `subject::531-1/-9` | CODE `531-1/-9` | 力学に関する固有補助番号
- `subject::531.1` | CODE `531.1` | 運動学．運動の数学的・力学的幾何学
- `subject::531.2` | CODE `531.2` | 静力学．力．つりあい．引力
- `subject::531.3` | CODE `531.3` | 動力学
- `subject::531.4` | CODE `531.4` | 仕事．重量．質量．摩擦
- `subject::531.5` | CODE `531.5` | 重力．振子．弾道学
- `subject::531.6` | CODE `531.6` | 機械的エネルギー．機械的エネルギー保存
- `subject::531.7` | CODE `531.7` | 幾何学的および機械的量の測定
- `subject::531.8` | CODE `531.8` | 機械の理論一般．工業力学一般

<!-- END_FACET_NODE -->

## FACET_NODE `subject::531-1/-9`

- FACET: `subject`
- NODE_KEY: `subject::531-1/-9`
- CODE: `531-1/-9`
- LABEL: 力学に関する固有補助番号
- PARENT_KEY: `subject::531`
- PATH_CODES: `5` > `53` > `531/534` > `531` > `531-1/-9`
- PATH_LABELS: 数学．自然科学 ＞ 物理学 ＞ 力学 ＞ 一般力学．固体および剛体の力学 ＞ 力学に関する固有補助番号
- LEAF: false
- DIRECT_CHILDREN_COUNT: 5

### DIRECT_CHILDREN

- `subject::531-1` | CODE `531-1` | 一次元．直線
- `subject::531-2` | CODE `531-2` | 二次元．平面．表面
- `subject::531-3` | CODE `531-3` | 三次元．立体．空間
- `subject::531-4` | CODE `531-4` | 超空間
- `subject::531-9` | CODE `531-9` | 非ユークリッド空間

<!-- END_FACET_NODE -->

## FACET_NODE `subject::531-1`

- FACET: `subject`
- NODE_KEY: `subject::531-1`
- CODE: `531-1`
- LABEL: 一次元．直線
- PARENT_KEY: `subject::531-1/-9`
- PATH_CODES: `5` > `53` > `531/534` > `531` > `531-1/-9` > `531-1`
- PATH_LABELS: 数学．自然科学 ＞ 物理学 ＞ 力学 ＞ 一般力学．固体および剛体の力学 ＞ 力学に関する固有補助番号 ＞ 一次元．直線
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::531-2`

- FACET: `subject`
- NODE_KEY: `subject::531-2`
- CODE: `531-2`
- LABEL: 二次元．平面．表面
- PARENT_KEY: `subject::531-1/-9`
- PATH_CODES: `5` > `53` > `531/534` > `531` > `531-1/-9` > `531-2`
- PATH_LABELS: 数学．自然科学 ＞ 物理学 ＞ 力学 ＞ 一般力学．固体および剛体の力学 ＞ 力学に関する固有補助番号 ＞ 二次元．平面．表面
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::531-3`

- FACET: `subject`
- NODE_KEY: `subject::531-3`
- CODE: `531-3`
- LABEL: 三次元．立体．空間
- PARENT_KEY: `subject::531-1/-9`
- PATH_CODES: `5` > `53` > `531/534` > `531` > `531-1/-9` > `531-3`
- PATH_LABELS: 数学．自然科学 ＞ 物理学 ＞ 力学 ＞ 一般力学．固体および剛体の力学 ＞ 力学に関する固有補助番号 ＞ 三次元．立体．空間
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::531-4`

- FACET: `subject`
- NODE_KEY: `subject::531-4`
- CODE: `531-4`
- LABEL: 超空間
- PARENT_KEY: `subject::531-1/-9`
- PATH_CODES: `5` > `53` > `531/534` > `531` > `531-1/-9` > `531-4`
- PATH_LABELS: 数学．自然科学 ＞ 物理学 ＞ 力学 ＞ 一般力学．固体および剛体の力学 ＞ 力学に関する固有補助番号 ＞ 超空間
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::531-9`

- FACET: `subject`
- NODE_KEY: `subject::531-9`
- CODE: `531-9`
- LABEL: 非ユークリッド空間
- PARENT_KEY: `subject::531-1/-9`
- PATH_CODES: `5` > `53` > `531/534` > `531` > `531-1/-9` > `531-9`
- PATH_LABELS: 数学．自然科学 ＞ 物理学 ＞ 力学 ＞ 一般力学．固体および剛体の力学 ＞ 力学に関する固有補助番号 ＞ 非ユークリッド空間
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::531.1`

- FACET: `subject`
- NODE_KEY: `subject::531.1`
- CODE: `531.1`
- LABEL: 運動学．運動の数学的・力学的幾何学
- PARENT_KEY: `subject::531`
- PATH_CODES: `5` > `53` > `531/534` > `531` > `531.1`
- PATH_LABELS: 数学．自然科学 ＞ 物理学 ＞ 力学 ＞ 一般力学．固体および剛体の力学 ＞ 運動学．運動の数学的・力学的幾何学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::531.2`

- FACET: `subject`
- NODE_KEY: `subject::531.2`
- CODE: `531.2`
- LABEL: 静力学．力．つりあい．引力
- PARENT_KEY: `subject::531`
- PATH_CODES: `5` > `53` > `531/534` > `531` > `531.2`
- PATH_LABELS: 数学．自然科学 ＞ 物理学 ＞ 力学 ＞ 一般力学．固体および剛体の力学 ＞ 静力学．力．つりあい．引力
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::531.3`

- FACET: `subject`
- NODE_KEY: `subject::531.3`
- CODE: `531.3`
- LABEL: 動力学
- PARENT_KEY: `subject::531`
- PATH_CODES: `5` > `53` > `531/534` > `531` > `531.3`
- PATH_LABELS: 数学．自然科学 ＞ 物理学 ＞ 力学 ＞ 一般力学．固体および剛体の力学 ＞ 動力学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::531.4`

- FACET: `subject`
- NODE_KEY: `subject::531.4`
- CODE: `531.4`
- LABEL: 仕事．重量．質量．摩擦
- PARENT_KEY: `subject::531`
- PATH_CODES: `5` > `53` > `531/534` > `531` > `531.4`
- PATH_LABELS: 数学．自然科学 ＞ 物理学 ＞ 力学 ＞ 一般力学．固体および剛体の力学 ＞ 仕事．重量．質量．摩擦
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::531.5`

- FACET: `subject`
- NODE_KEY: `subject::531.5`
- CODE: `531.5`
- LABEL: 重力．振子．弾道学
- PARENT_KEY: `subject::531`
- PATH_CODES: `5` > `53` > `531/534` > `531` > `531.5`
- PATH_LABELS: 数学．自然科学 ＞ 物理学 ＞ 力学 ＞ 一般力学．固体および剛体の力学 ＞ 重力．振子．弾道学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::531.6`

- FACET: `subject`
- NODE_KEY: `subject::531.6`
- CODE: `531.6`
- LABEL: 機械的エネルギー．機械的エネルギー保存
- PARENT_KEY: `subject::531`
- PATH_CODES: `5` > `53` > `531/534` > `531` > `531.6`
- PATH_LABELS: 数学．自然科学 ＞ 物理学 ＞ 力学 ＞ 一般力学．固体および剛体の力学 ＞ 機械的エネルギー．機械的エネルギー保存
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::531.7`

- FACET: `subject`
- NODE_KEY: `subject::531.7`
- CODE: `531.7`
- LABEL: 幾何学的および機械的量の測定
- PARENT_KEY: `subject::531`
- PATH_CODES: `5` > `53` > `531/534` > `531` > `531.7`
- PATH_LABELS: 数学．自然科学 ＞ 物理学 ＞ 力学 ＞ 一般力学．固体および剛体の力学 ＞ 幾何学的および機械的量の測定
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::531.8`

- FACET: `subject`
- NODE_KEY: `subject::531.8`
- CODE: `531.8`
- LABEL: 機械の理論一般．工業力学一般
- PARENT_KEY: `subject::531`
- PATH_CODES: `5` > `53` > `531/534` > `531` > `531.8`
- PATH_LABELS: 数学．自然科学 ＞ 物理学 ＞ 力学 ＞ 一般力学．固体および剛体の力学 ＞ 機械の理論一般．工業力学一般
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::532`

- FACET: `subject`
- NODE_KEY: `subject::532`
- CODE: `532`
- LABEL: 流体力学一般．液体の力学
- PARENT_KEY: `subject::531/534`
- PATH_CODES: `5` > `53` > `531/534` > `532`
- PATH_LABELS: 数学．自然科学 ＞ 物理学 ＞ 力学 ＞ 流体力学一般．液体の力学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::533`

- FACET: `subject`
- NODE_KEY: `subject::533`
- CODE: `533`
- LABEL: 気体の力学．空気力学．プラズマ物理学
- PARENT_KEY: `subject::531/534`
- PATH_CODES: `5` > `53` > `531/534` > `533`
- PATH_LABELS: 数学．自然科学 ＞ 物理学 ＞ 力学 ＞ 気体の力学．空気力学．プラズマ物理学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::534`

- FACET: `subject`
- NODE_KEY: `subject::534`
- CODE: `534`
- LABEL: 振動．音響学
- PARENT_KEY: `subject::531/534`
- PATH_CODES: `5` > `53` > `531/534` > `534`
- PATH_LABELS: 数学．自然科学 ＞ 物理学 ＞ 力学 ＞ 振動．音響学
- LEAF: false
- DIRECT_CHILDREN_COUNT: 5

### DIRECT_CHILDREN

- `subject::534.4` | CODE `534.4` | 音の分析と合成
- `subject::534.5` | CODE `534.5` | 振動の構成
- `subject::534.6` | CODE `534.6` | 音響測定
- `subject::534.7` | CODE `534.7` | 生理的音響学．医学音響学
- `subject::534.8` | CODE `534.8` | 音響学の応用(理論)

<!-- END_FACET_NODE -->

## FACET_NODE `subject::534.4`

- FACET: `subject`
- NODE_KEY: `subject::534.4`
- CODE: `534.4`
- LABEL: 音の分析と合成
- PARENT_KEY: `subject::534`
- PATH_CODES: `5` > `53` > `531/534` > `534` > `534.4`
- PATH_LABELS: 数学．自然科学 ＞ 物理学 ＞ 力学 ＞ 振動．音響学 ＞ 音の分析と合成
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::534.5`

- FACET: `subject`
- NODE_KEY: `subject::534.5`
- CODE: `534.5`
- LABEL: 振動の構成
- PARENT_KEY: `subject::534`
- PATH_CODES: `5` > `53` > `531/534` > `534` > `534.5`
- PATH_LABELS: 数学．自然科学 ＞ 物理学 ＞ 力学 ＞ 振動．音響学 ＞ 振動の構成
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::534.6`

- FACET: `subject`
- NODE_KEY: `subject::534.6`
- CODE: `534.6`
- LABEL: 音響測定
- PARENT_KEY: `subject::534`
- PATH_CODES: `5` > `53` > `531/534` > `534` > `534.6`
- PATH_LABELS: 数学．自然科学 ＞ 物理学 ＞ 力学 ＞ 振動．音響学 ＞ 音響測定
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::534.7`

- FACET: `subject`
- NODE_KEY: `subject::534.7`
- CODE: `534.7`
- LABEL: 生理的音響学．医学音響学
- PARENT_KEY: `subject::534`
- PATH_CODES: `5` > `53` > `531/534` > `534` > `534.7`
- PATH_LABELS: 数学．自然科学 ＞ 物理学 ＞ 力学 ＞ 振動．音響学 ＞ 生理的音響学．医学音響学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::534.8`

- FACET: `subject`
- NODE_KEY: `subject::534.8`
- CODE: `534.8`
- LABEL: 音響学の応用(理論)
- PARENT_KEY: `subject::534`
- PATH_CODES: `5` > `53` > `531/534` > `534` > `534.8`
- PATH_LABELS: 数学．自然科学 ＞ 物理学 ＞ 力学 ＞ 振動．音響学 ＞ 音響学の応用(理論)
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::535`

- FACET: `subject`
- NODE_KEY: `subject::535`
- CODE: `535`
- LABEL: 光学
- PARENT_KEY: `subject::53`
- PATH_CODES: `5` > `53` > `535`
- PATH_LABELS: 数学．自然科学 ＞ 物理学 ＞ 光学
- LEAF: false
- DIRECT_CHILDREN_COUNT: 3

### DIRECT_CHILDREN

- `subject::535.1` | CODE `535.1` | 光の理論
- `subject::535.2` | CODE `535.2` | 放射の伝播とエネルギー論．測光
- `subject::535.3` | CODE `535.3` | 伝播．反射．屈折．吸収．放出

<!-- END_FACET_NODE -->

## FACET_NODE `subject::535.1`

- FACET: `subject`
- NODE_KEY: `subject::535.1`
- CODE: `535.1`
- LABEL: 光の理論
- PARENT_KEY: `subject::535`
- PATH_CODES: `5` > `53` > `535` > `535.1`
- PATH_LABELS: 数学．自然科学 ＞ 物理学 ＞ 光学 ＞ 光の理論
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::535.2`

- FACET: `subject`
- NODE_KEY: `subject::535.2`
- CODE: `535.2`
- LABEL: 放射の伝播とエネルギー論．測光
- PARENT_KEY: `subject::535`
- PATH_CODES: `5` > `53` > `535` > `535.2`
- PATH_LABELS: 数学．自然科学 ＞ 物理学 ＞ 光学 ＞ 放射の伝播とエネルギー論．測光
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::535.3`

- FACET: `subject`
- NODE_KEY: `subject::535.3`
- CODE: `535.3`
- LABEL: 伝播．反射．屈折．吸収．放出
- PARENT_KEY: `subject::535`
- PATH_CODES: `5` > `53` > `535` > `535.3`
- PATH_LABELS: 数学．自然科学 ＞ 物理学 ＞ 光学 ＞ 伝播．反射．屈折．吸収．放出
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::536`

- FACET: `subject`
- NODE_KEY: `subject::536`
- CODE: `536`
- LABEL: 熱．熱力学．統計物理学
- PARENT_KEY: `subject::53`
- PATH_CODES: `5` > `53` > `536`
- PATH_LABELS: 数学．自然科学 ＞ 物理学 ＞ 熱．熱力学．統計物理学
- LEAF: false
- DIRECT_CHILDREN_COUNT: 2

### DIRECT_CHILDREN

- `subject::536.5` | CODE `536.5` | 温度．温度目盛．温度測定．温度計．温度制御
- `subject::536.7` | CODE `536.7` | 熱力学．エネルギー論

<!-- END_FACET_NODE -->

## FACET_NODE `subject::536.5`

- FACET: `subject`
- NODE_KEY: `subject::536.5`
- CODE: `536.5`
- LABEL: 温度．温度目盛．温度測定．温度計．温度制御
- PARENT_KEY: `subject::536`
- PATH_CODES: `5` > `53` > `536` > `536.5`
- PATH_LABELS: 数学．自然科学 ＞ 物理学 ＞ 熱．熱力学．統計物理学 ＞ 温度．温度目盛．温度測定．温度計．温度制御
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::536.7`

- FACET: `subject`
- NODE_KEY: `subject::536.7`
- CODE: `536.7`
- LABEL: 熱力学．エネルギー論
- PARENT_KEY: `subject::536`
- PATH_CODES: `5` > `53` > `536` > `536.7`
- PATH_LABELS: 数学．自然科学 ＞ 物理学 ＞ 熱．熱力学．統計物理学 ＞ 熱力学．エネルギー論
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::537`

- FACET: `subject`
- NODE_KEY: `subject::537`
- CODE: `537`
- LABEL: 電気学．磁気学．電磁気学
- PARENT_KEY: `subject::53`
- PATH_CODES: `5` > `53` > `537`
- PATH_LABELS: 数学．自然科学 ＞ 物理学 ＞ 電気学．磁気学．電磁気学
- LEAF: false
- DIRECT_CHILDREN_COUNT: 5

### DIRECT_CHILDREN

- `subject::537.2` | CODE `537.2` | 静電気．静電気学
- `subject::537.3` | CODE `537.3` | 電流．動電学
- `subject::537.6` | CODE `537.6` | 磁気
- `subject::537.6/.8` | CODE `537.6/.8` | 磁気．電磁気
- `subject::537.8` | CODE `537.8` | 電磁気．電磁場．電気力学

<!-- END_FACET_NODE -->

## FACET_NODE `subject::537.2`

- FACET: `subject`
- NODE_KEY: `subject::537.2`
- CODE: `537.2`
- LABEL: 静電気．静電気学
- PARENT_KEY: `subject::537`
- PATH_CODES: `5` > `53` > `537` > `537.2`
- PATH_LABELS: 数学．自然科学 ＞ 物理学 ＞ 電気学．磁気学．電磁気学 ＞ 静電気．静電気学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::537.3`

- FACET: `subject`
- NODE_KEY: `subject::537.3`
- CODE: `537.3`
- LABEL: 電流．動電学
- PARENT_KEY: `subject::537`
- PATH_CODES: `5` > `53` > `537` > `537.3`
- PATH_LABELS: 数学．自然科学 ＞ 物理学 ＞ 電気学．磁気学．電磁気学 ＞ 電流．動電学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::537.6`

- FACET: `subject`
- NODE_KEY: `subject::537.6`
- CODE: `537.6`
- LABEL: 磁気
- PARENT_KEY: `subject::537`
- PATH_CODES: `5` > `53` > `537` > `537.6`
- PATH_LABELS: 数学．自然科学 ＞ 物理学 ＞ 電気学．磁気学．電磁気学 ＞ 磁気
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::537.6/.8`

- FACET: `subject`
- NODE_KEY: `subject::537.6/.8`
- CODE: `537.6/.8`
- LABEL: 磁気．電磁気
- PARENT_KEY: `subject::537`
- PATH_CODES: `5` > `53` > `537` > `537.6/.8`
- PATH_LABELS: 数学．自然科学 ＞ 物理学 ＞ 電気学．磁気学．電磁気学 ＞ 磁気．電磁気
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::537.8`

- FACET: `subject`
- NODE_KEY: `subject::537.8`
- CODE: `537.8`
- LABEL: 電磁気．電磁場．電気力学
- PARENT_KEY: `subject::537`
- PATH_CODES: `5` > `53` > `537` > `537.8`
- PATH_LABELS: 数学．自然科学 ＞ 物理学 ＞ 電気学．磁気学．電磁気学 ＞ 電磁気．電磁場．電気力学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::538.9`

- FACET: `subject`
- NODE_KEY: `subject::538.9`
- CODE: `538.9`
- LABEL: 固体物理学
- PARENT_KEY: `subject::53`
- PATH_CODES: `5` > `53` > `538.9`
- PATH_LABELS: 数学．自然科学 ＞ 物理学 ＞ 固体物理学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::539`

- FACET: `subject`
- NODE_KEY: `subject::539`
- CODE: `539`
- LABEL: 物質の物理的性質
- PARENT_KEY: `subject::53`
- PATH_CODES: `5` > `53` > `539`
- PATH_LABELS: 数学．自然科学 ＞ 物理学 ＞ 物質の物理的性質
- LEAF: false
- DIRECT_CHILDREN_COUNT: 4

### DIRECT_CHILDREN

- `subject::539.1` | CODE `539.1` | 核物理学．原子物理学．分子物理学
- `subject::539.2` | CODE `539.2` | 分子系の性質と構造
- `subject::539.5` | CODE `539.5` | 変形性に影響する物性
- `subject::539.6` | CODE `539.6` | 分子間力

<!-- END_FACET_NODE -->

## FACET_NODE `subject::539.1`

- FACET: `subject`
- NODE_KEY: `subject::539.1`
- CODE: `539.1`
- LABEL: 核物理学．原子物理学．分子物理学
- PARENT_KEY: `subject::539`
- PATH_CODES: `5` > `53` > `539` > `539.1`
- PATH_LABELS: 数学．自然科学 ＞ 物理学 ＞ 物質の物理的性質 ＞ 核物理学．原子物理学．分子物理学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::539.2`

- FACET: `subject`
- NODE_KEY: `subject::539.2`
- CODE: `539.2`
- LABEL: 分子系の性質と構造
- PARENT_KEY: `subject::539`
- PATH_CODES: `5` > `53` > `539` > `539.2`
- PATH_LABELS: 数学．自然科学 ＞ 物理学 ＞ 物質の物理的性質 ＞ 分子系の性質と構造
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::539.5`

- FACET: `subject`
- NODE_KEY: `subject::539.5`
- CODE: `539.5`
- LABEL: 変形性に影響する物性
- PARENT_KEY: `subject::539`
- PATH_CODES: `5` > `53` > `539` > `539.5`
- PATH_LABELS: 数学．自然科学 ＞ 物理学 ＞ 物質の物理的性質 ＞ 変形性に影響する物性
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::539.6`

- FACET: `subject`
- NODE_KEY: `subject::539.6`
- CODE: `539.6`
- LABEL: 分子間力
- PARENT_KEY: `subject::539`
- PATH_CODES: `5` > `53` > `539` > `539.6`
- PATH_LABELS: 数学．自然科学 ＞ 物理学 ＞ 物質の物理的性質 ＞ 分子間力
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::54`

- FACET: `subject`
- NODE_KEY: `subject::54`
- CODE: `54`
- LABEL: 化学．結晶学．鉱物学
- PARENT_KEY: `subject::5`
- PATH_CODES: `5` > `54`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学
- LEAF: false
- DIRECT_CHILDREN_COUNT: 8

### DIRECT_CHILDREN

- `subject::54-1/-4` | CODE `54-1/-4` | 物質の状態に関する固有補助番号
- `subject::54.01/.08` | CODE `54.01/.08` | 組成，製造，調整製，分析に関する固有補助番号
- `subject::542` | CODE `542` | 実験室における化学．調製および実験化学
- `subject::543` | CODE `543` | 分析化学
- `subject::544` | CODE `544` | 物理化学
- `subject::546` | CODE `546` | 無機化学
- `subject::547` | CODE `547` | 有機化学
- `subject::548/549` | CODE `548/549` | 鉱物学関連の科学．結晶学．鉱物学

<!-- END_FACET_NODE -->

## FACET_NODE `subject::54-1/-4`

- FACET: `subject`
- NODE_KEY: `subject::54-1/-4`
- CODE: `54-1/-4`
- LABEL: 物質の状態に関する固有補助番号
- PARENT_KEY: `subject::54`
- PATH_CODES: `5` > `54` > `54-1/-4`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 物質の状態に関する固有補助番号
- LEAF: false
- DIRECT_CHILDREN_COUNT: 3

### DIRECT_CHILDREN

- `subject::54-1` | CODE `54-1` | 物質の状態
- `subject::54-3` | CODE `54-3` | 特定の種類の化合物
- `subject::54-4` | CODE `54-4` | 化学品．試薬

<!-- END_FACET_NODE -->

## FACET_NODE `subject::54-1`

- FACET: `subject`
- NODE_KEY: `subject::54-1`
- CODE: `54-1`
- LABEL: 物質の状態
- PARENT_KEY: `subject::54-1/-4`
- PATH_CODES: `5` > `54` > `54-1/-4` > `54-1`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 物質の状態に関する固有補助番号 ＞ 物質の状態
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::54-3`

- FACET: `subject`
- NODE_KEY: `subject::54-3`
- CODE: `54-3`
- LABEL: 特定の種類の化合物
- PARENT_KEY: `subject::54-1/-4`
- PATH_CODES: `5` > `54` > `54-1/-4` > `54-3`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 物質の状態に関する固有補助番号 ＞ 特定の種類の化合物
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::54-4`

- FACET: `subject`
- NODE_KEY: `subject::54-4`
- CODE: `54-4`
- LABEL: 化学品．試薬
- PARENT_KEY: `subject::54-1/-4`
- PATH_CODES: `5` > `54` > `54-1/-4` > `54-4`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 物質の状態に関する固有補助番号 ＞ 化学品．試薬
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::54.01/.08`

- FACET: `subject`
- NODE_KEY: `subject::54.01/.08`
- CODE: `54.01/.08`
- LABEL: 組成，製造，調整製，分析に関する固有補助番号
- PARENT_KEY: `subject::54`
- PATH_CODES: `5` > `54` > `54.01/.08`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 組成，製造，調整製，分析に関する固有補助番号
- LEAF: false
- DIRECT_CHILDREN_COUNT: 6

### DIRECT_CHILDREN

- `subject::54.01` | CODE `54.01` | 化学物質と系．起源．産出．相
- `subject::54.02` | CODE `54.02` | 組成．構造．同位体
- `subject::54.05` | CODE `54.05` | 製造．調整．分離．精製など
- `subject::54.06` | CODE `54.06` | 分析，研究およびハンドリング一般
- `subject::54.07` | CODE `54.07` | 調製，研究，分析のための装置と設備
- `subject::54.08` | CODE `54.08` | 測定の原理，方法，技術．測定装置

<!-- END_FACET_NODE -->

## FACET_NODE `subject::54.01`

- FACET: `subject`
- NODE_KEY: `subject::54.01`
- CODE: `54.01`
- LABEL: 化学物質と系．起源．産出．相
- PARENT_KEY: `subject::54.01/.08`
- PATH_CODES: `5` > `54` > `54.01/.08` > `54.01`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 組成，製造，調整製，分析に関する固有補助番号 ＞ 化学物質と系．起源．産出．相
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::54.02`

- FACET: `subject`
- NODE_KEY: `subject::54.02`
- CODE: `54.02`
- LABEL: 組成．構造．同位体
- PARENT_KEY: `subject::54.01/.08`
- PATH_CODES: `5` > `54` > `54.01/.08` > `54.02`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 組成，製造，調整製，分析に関する固有補助番号 ＞ 組成．構造．同位体
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::54.05`

- FACET: `subject`
- NODE_KEY: `subject::54.05`
- CODE: `54.05`
- LABEL: 製造．調整．分離．精製など
- PARENT_KEY: `subject::54.01/.08`
- PATH_CODES: `5` > `54` > `54.01/.08` > `54.05`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 組成，製造，調整製，分析に関する固有補助番号 ＞ 製造．調整．分離．精製など
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::54.06`

- FACET: `subject`
- NODE_KEY: `subject::54.06`
- CODE: `54.06`
- LABEL: 分析，研究およびハンドリング一般
- PARENT_KEY: `subject::54.01/.08`
- PATH_CODES: `5` > `54` > `54.01/.08` > `54.06`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 組成，製造，調整製，分析に関する固有補助番号 ＞ 分析，研究およびハンドリング一般
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::54.07`

- FACET: `subject`
- NODE_KEY: `subject::54.07`
- CODE: `54.07`
- LABEL: 調製，研究，分析のための装置と設備
- PARENT_KEY: `subject::54.01/.08`
- PATH_CODES: `5` > `54` > `54.01/.08` > `54.07`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 組成，製造，調整製，分析に関する固有補助番号 ＞ 調製，研究，分析のための装置と設備
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::54.08`

- FACET: `subject`
- NODE_KEY: `subject::54.08`
- CODE: `54.08`
- LABEL: 測定の原理，方法，技術．測定装置
- PARENT_KEY: `subject::54.01/.08`
- PATH_CODES: `5` > `54` > `54.01/.08` > `54.08`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 組成，製造，調整製，分析に関する固有補助番号 ＞ 測定の原理，方法，技術．測定装置
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::542`

- FACET: `subject`
- NODE_KEY: `subject::542`
- CODE: `542`
- LABEL: 実験室における化学．調製および実験化学
- PARENT_KEY: `subject::54`
- PATH_CODES: `5` > `54` > `542`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 実験室における化学．調製および実験化学
- LEAF: false
- DIRECT_CHILDREN_COUNT: 9

### DIRECT_CHILDREN

- `subject::542.1` | CODE `542.1` | 化学実験室
- `subject::542.2` | CODE `542.2` | 実験装置機器一般．実験手法一般
- `subject::542.3` | CODE `542.3` | 重量・質量測定．体積測定
- `subject::542.4` | CODE `542.4` | 熱またはおよび冷熱の利用
- `subject::542.5` | CODE `542.5` | 火炎の利用．ブローランプ
- `subject::542.6` | CODE `542.6` | 液体を用いる作業
- `subject::542.7` | CODE `542.7` | 気体を用いる作業
- `subject::542.8` | CODE `542.8` | 物理的・物理化学的・電気的操作
- `subject::542.9` | CODE `542.9` | 化学反応．特定の化学的過程

<!-- END_FACET_NODE -->

## FACET_NODE `subject::542.1`

- FACET: `subject`
- NODE_KEY: `subject::542.1`
- CODE: `542.1`
- LABEL: 化学実験室
- PARENT_KEY: `subject::542`
- PATH_CODES: `5` > `54` > `542` > `542.1`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 実験室における化学．調製および実験化学 ＞ 化学実験室
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::542.2`

- FACET: `subject`
- NODE_KEY: `subject::542.2`
- CODE: `542.2`
- LABEL: 実験装置機器一般．実験手法一般
- PARENT_KEY: `subject::542`
- PATH_CODES: `5` > `54` > `542` > `542.2`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 実験室における化学．調製および実験化学 ＞ 実験装置機器一般．実験手法一般
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::542.3`

- FACET: `subject`
- NODE_KEY: `subject::542.3`
- CODE: `542.3`
- LABEL: 重量・質量測定．体積測定
- PARENT_KEY: `subject::542`
- PATH_CODES: `5` > `54` > `542` > `542.3`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 実験室における化学．調製および実験化学 ＞ 重量・質量測定．体積測定
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::542.4`

- FACET: `subject`
- NODE_KEY: `subject::542.4`
- CODE: `542.4`
- LABEL: 熱またはおよび冷熱の利用
- PARENT_KEY: `subject::542`
- PATH_CODES: `5` > `54` > `542` > `542.4`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 実験室における化学．調製および実験化学 ＞ 熱またはおよび冷熱の利用
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::542.5`

- FACET: `subject`
- NODE_KEY: `subject::542.5`
- CODE: `542.5`
- LABEL: 火炎の利用．ブローランプ
- PARENT_KEY: `subject::542`
- PATH_CODES: `5` > `54` > `542` > `542.5`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 実験室における化学．調製および実験化学 ＞ 火炎の利用．ブローランプ
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::542.6`

- FACET: `subject`
- NODE_KEY: `subject::542.6`
- CODE: `542.6`
- LABEL: 液体を用いる作業
- PARENT_KEY: `subject::542`
- PATH_CODES: `5` > `54` > `542` > `542.6`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 実験室における化学．調製および実験化学 ＞ 液体を用いる作業
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::542.7`

- FACET: `subject`
- NODE_KEY: `subject::542.7`
- CODE: `542.7`
- LABEL: 気体を用いる作業
- PARENT_KEY: `subject::542`
- PATH_CODES: `5` > `54` > `542` > `542.7`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 実験室における化学．調製および実験化学 ＞ 気体を用いる作業
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::542.8`

- FACET: `subject`
- NODE_KEY: `subject::542.8`
- CODE: `542.8`
- LABEL: 物理的・物理化学的・電気的操作
- PARENT_KEY: `subject::542`
- PATH_CODES: `5` > `54` > `542` > `542.8`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 実験室における化学．調製および実験化学 ＞ 物理的・物理化学的・電気的操作
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::542.9`

- FACET: `subject`
- NODE_KEY: `subject::542.9`
- CODE: `542.9`
- LABEL: 化学反応．特定の化学的過程
- PARENT_KEY: `subject::542`
- PATH_CODES: `5` > `54` > `542` > `542.9`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 実験室における化学．調製および実験化学 ＞ 化学反応．特定の化学的過程
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::543`

- FACET: `subject`
- NODE_KEY: `subject::543`
- CODE: `543`
- LABEL: 分析化学
- PARENT_KEY: `subject::54`
- PATH_CODES: `5` > `54` > `543`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 分析化学
- LEAF: false
- DIRECT_CHILDREN_COUNT: 6

### DIRECT_CHILDREN

- `subject::543.2` | CODE `543.2` | 化学的分析法
- `subject::543.3` | CODE `543.3` | 水のサンプリングと分析
- `subject::543.4` | CODE `543.4` | 分光分析の方法．光学的分析法
- `subject::543.5` | CODE `543.5` | 物理化学的分析法(光学的方法を除く)
- `subject::543.6` | CODE `543.6` | 各種物質の分析．製造条件下での分析による検査
- `subject::543.9` | CODE `543.9` | 生物学的・生化学的反応による分析．分析に利用される生物学的方法

<!-- END_FACET_NODE -->

## FACET_NODE `subject::543.2`

- FACET: `subject`
- NODE_KEY: `subject::543.2`
- CODE: `543.2`
- LABEL: 化学的分析法
- PARENT_KEY: `subject::543`
- PATH_CODES: `5` > `54` > `543` > `543.2`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 分析化学 ＞ 化学的分析法
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::543.3`

- FACET: `subject`
- NODE_KEY: `subject::543.3`
- CODE: `543.3`
- LABEL: 水のサンプリングと分析
- PARENT_KEY: `subject::543`
- PATH_CODES: `5` > `54` > `543` > `543.3`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 分析化学 ＞ 水のサンプリングと分析
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::543.4`

- FACET: `subject`
- NODE_KEY: `subject::543.4`
- CODE: `543.4`
- LABEL: 分光分析の方法．光学的分析法
- PARENT_KEY: `subject::543`
- PATH_CODES: `5` > `54` > `543` > `543.4`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 分析化学 ＞ 分光分析の方法．光学的分析法
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::543.5`

- FACET: `subject`
- NODE_KEY: `subject::543.5`
- CODE: `543.5`
- LABEL: 物理化学的分析法(光学的方法を除く)
- PARENT_KEY: `subject::543`
- PATH_CODES: `5` > `54` > `543` > `543.5`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 分析化学 ＞ 物理化学的分析法(光学的方法を除く)
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::543.6`

- FACET: `subject`
- NODE_KEY: `subject::543.6`
- CODE: `543.6`
- LABEL: 各種物質の分析．製造条件下での分析による検査
- PARENT_KEY: `subject::543`
- PATH_CODES: `5` > `54` > `543` > `543.6`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 分析化学 ＞ 各種物質の分析．製造条件下での分析による検査
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::543.9`

- FACET: `subject`
- NODE_KEY: `subject::543.9`
- CODE: `543.9`
- LABEL: 生物学的・生化学的反応による分析．分析に利用される生物学的方法
- PARENT_KEY: `subject::543`
- PATH_CODES: `5` > `54` > `543` > `543.9`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 分析化学 ＞ 生物学的・生化学的反応による分析．分析に利用される生物学的方法
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::544`

- FACET: `subject`
- NODE_KEY: `subject::544`
- CODE: `544`
- LABEL: 物理化学
- PARENT_KEY: `subject::54`
- PATH_CODES: `5` > `54` > `544`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 物理化学
- LEAF: false
- DIRECT_CHILDREN_COUNT: 8

### DIRECT_CHILDREN

- `subject::544.01/.07` | CODE `544.01/.07` | 化学物質・化学系物理化学に関する固有補助番号下位区分
- `subject::544.1` | CODE `544.1` | 物質の化学的構造
- `subject::544.2` | CODE `544.2` | 固体・液体・気体の物理化学
- `subject::544.3` | CODE `544.3` | 化学熱力学
- `subject::544.4` | CODE `544.4` | 反応速度論．触媒作用
- `subject::544.5` | CODE `544.5` | 高エネルギー過程の化学
- `subject::544.6` | CODE `544.6` | 電気化学
- `subject::544.7` | CODE `544.7` | 表面現象およびコロイドの化学

<!-- END_FACET_NODE -->

## FACET_NODE `subject::544.01/.07`

- FACET: `subject`
- NODE_KEY: `subject::544.01/.07`
- CODE: `544.01/.07`
- LABEL: 化学物質・化学系物理化学に関する固有補助番号下位区分
- PARENT_KEY: `subject::544`
- PATH_CODES: `5` > `54` > `544` > `544.01/.07`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 物理化学 ＞ 化学物質・化学系物理化学に関する固有補助番号下位区分
- LEAF: false
- DIRECT_CHILDREN_COUNT: 4

### DIRECT_CHILDREN

- `subject::544.01` | CODE `544.01` | 化学物質，化学系．産出．自然状態．相
- `subject::544.02` | CODE `544.02` | 化学組成．構造．同位体など
- `subject::544.03` | CODE `544.03` | 物理的性質および現象．定数．物質の状態と特性に影響する効果
- `subject::544.07` | CODE `544.07` | 機器および設備

<!-- END_FACET_NODE -->

## FACET_NODE `subject::544.01`

- FACET: `subject`
- NODE_KEY: `subject::544.01`
- CODE: `544.01`
- LABEL: 化学物質，化学系．産出．自然状態．相
- PARENT_KEY: `subject::544.01/.07`
- PATH_CODES: `5` > `54` > `544` > `544.01/.07` > `544.01`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 物理化学 ＞ 化学物質・化学系物理化学に関する固有補助番号下位区分 ＞ 化学物質，化学系．産出．自然状態．相
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::544.02`

- FACET: `subject`
- NODE_KEY: `subject::544.02`
- CODE: `544.02`
- LABEL: 化学組成．構造．同位体など
- PARENT_KEY: `subject::544.01/.07`
- PATH_CODES: `5` > `54` > `544` > `544.01/.07` > `544.02`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 物理化学 ＞ 化学物質・化学系物理化学に関する固有補助番号下位区分 ＞ 化学組成．構造．同位体など
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::544.03`

- FACET: `subject`
- NODE_KEY: `subject::544.03`
- CODE: `544.03`
- LABEL: 物理的性質および現象．定数．物質の状態と特性に影響する効果
- PARENT_KEY: `subject::544.01/.07`
- PATH_CODES: `5` > `54` > `544` > `544.01/.07` > `544.03`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 物理化学 ＞ 化学物質・化学系物理化学に関する固有補助番号下位区分 ＞ 物理的性質および現象．定数．物質の状態と特性に影響する効果
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::544.07`

- FACET: `subject`
- NODE_KEY: `subject::544.07`
- CODE: `544.07`
- LABEL: 機器および設備
- PARENT_KEY: `subject::544.01/.07`
- PATH_CODES: `5` > `54` > `544` > `544.01/.07` > `544.07`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 物理化学 ＞ 化学物質・化学系物理化学に関する固有補助番号下位区分 ＞ 機器および設備
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::544.1`

- FACET: `subject`
- NODE_KEY: `subject::544.1`
- CODE: `544.1`
- LABEL: 物質の化学的構造
- PARENT_KEY: `subject::544`
- PATH_CODES: `5` > `54` > `544` > `544.1`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 物理化学 ＞ 物質の化学的構造
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::544.2`

- FACET: `subject`
- NODE_KEY: `subject::544.2`
- CODE: `544.2`
- LABEL: 固体・液体・気体の物理化学
- PARENT_KEY: `subject::544`
- PATH_CODES: `5` > `54` > `544` > `544.2`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 物理化学 ＞ 固体・液体・気体の物理化学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::544.3`

- FACET: `subject`
- NODE_KEY: `subject::544.3`
- CODE: `544.3`
- LABEL: 化学熱力学
- PARENT_KEY: `subject::544`
- PATH_CODES: `5` > `54` > `544` > `544.3`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 物理化学 ＞ 化学熱力学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::544.4`

- FACET: `subject`
- NODE_KEY: `subject::544.4`
- CODE: `544.4`
- LABEL: 反応速度論．触媒作用
- PARENT_KEY: `subject::544`
- PATH_CODES: `5` > `54` > `544` > `544.4`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 物理化学 ＞ 反応速度論．触媒作用
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::544.5`

- FACET: `subject`
- NODE_KEY: `subject::544.5`
- CODE: `544.5`
- LABEL: 高エネルギー過程の化学
- PARENT_KEY: `subject::544`
- PATH_CODES: `5` > `54` > `544` > `544.5`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 物理化学 ＞ 高エネルギー過程の化学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::544.6`

- FACET: `subject`
- NODE_KEY: `subject::544.6`
- CODE: `544.6`
- LABEL: 電気化学
- PARENT_KEY: `subject::544`
- PATH_CODES: `5` > `54` > `544` > `544.6`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 物理化学 ＞ 電気化学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::544.7`

- FACET: `subject`
- NODE_KEY: `subject::544.7`
- CODE: `544.7`
- LABEL: 表面現象およびコロイドの化学
- PARENT_KEY: `subject::544`
- PATH_CODES: `5` > `54` > `544` > `544.7`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 物理化学 ＞ 表面現象およびコロイドの化学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::546`

- FACET: `subject`
- NODE_KEY: `subject::546`
- CODE: `546`
- LABEL: 無機化学
- PARENT_KEY: `subject::54`
- PATH_CODES: `5` > `54` > `546`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 無機化学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::547`

- FACET: `subject`
- NODE_KEY: `subject::547`
- CODE: `547`
- LABEL: 有機化学
- PARENT_KEY: `subject::54`
- PATH_CODES: `5` > `54` > `547`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 有機化学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::548/549`

- FACET: `subject`
- NODE_KEY: `subject::548/549`
- CODE: `548/549`
- LABEL: 鉱物学関連の科学．結晶学．鉱物学
- PARENT_KEY: `subject::54`
- PATH_CODES: `5` > `54` > `548/549`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 鉱物学関連の科学．結晶学．鉱物学
- LEAF: false
- DIRECT_CHILDREN_COUNT: 2

### DIRECT_CHILDREN

- `subject::548` | CODE `548` | 結晶学
- `subject::549` | CODE `549` | 鉱物学．鉱物の個別的研究

<!-- END_FACET_NODE -->

## FACET_NODE `subject::548`

- FACET: `subject`
- NODE_KEY: `subject::548`
- CODE: `548`
- LABEL: 結晶学
- PARENT_KEY: `subject::548/549`
- PATH_CODES: `5` > `54` > `548/549` > `548`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 鉱物学関連の科学．結晶学．鉱物学 ＞ 結晶学
- LEAF: false
- DIRECT_CHILDREN_COUNT: 6

### DIRECT_CHILDREN

- `subject::548.1` | CODE `548.1` | 数理結晶学．結晶の連続体理論
- `subject::548.2` | CODE `548.2` | 結晶成長．結晶集合体
- `subject::548.3` | CODE `548.3` | 結晶化学
- `subject::548.4` | CODE `548.4` | 結晶中の不規則性
- `subject::548.5` | CODE `548.5` | 結晶の生成・成長・溶解
- `subject::548.7` | CODE `548.7` | 結晶の微細構造．結晶の不連続体理論

<!-- END_FACET_NODE -->

## FACET_NODE `subject::548.1`

- FACET: `subject`
- NODE_KEY: `subject::548.1`
- CODE: `548.1`
- LABEL: 数理結晶学．結晶の連続体理論
- PARENT_KEY: `subject::548`
- PATH_CODES: `5` > `54` > `548/549` > `548` > `548.1`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 鉱物学関連の科学．結晶学．鉱物学 ＞ 結晶学 ＞ 数理結晶学．結晶の連続体理論
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::548.2`

- FACET: `subject`
- NODE_KEY: `subject::548.2`
- CODE: `548.2`
- LABEL: 結晶成長．結晶集合体
- PARENT_KEY: `subject::548`
- PATH_CODES: `5` > `54` > `548/549` > `548` > `548.2`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 鉱物学関連の科学．結晶学．鉱物学 ＞ 結晶学 ＞ 結晶成長．結晶集合体
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::548.3`

- FACET: `subject`
- NODE_KEY: `subject::548.3`
- CODE: `548.3`
- LABEL: 結晶化学
- PARENT_KEY: `subject::548`
- PATH_CODES: `5` > `54` > `548/549` > `548` > `548.3`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 鉱物学関連の科学．結晶学．鉱物学 ＞ 結晶学 ＞ 結晶化学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::548.4`

- FACET: `subject`
- NODE_KEY: `subject::548.4`
- CODE: `548.4`
- LABEL: 結晶中の不規則性
- PARENT_KEY: `subject::548`
- PATH_CODES: `5` > `54` > `548/549` > `548` > `548.4`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 鉱物学関連の科学．結晶学．鉱物学 ＞ 結晶学 ＞ 結晶中の不規則性
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::548.5`

- FACET: `subject`
- NODE_KEY: `subject::548.5`
- CODE: `548.5`
- LABEL: 結晶の生成・成長・溶解
- PARENT_KEY: `subject::548`
- PATH_CODES: `5` > `54` > `548/549` > `548` > `548.5`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 鉱物学関連の科学．結晶学．鉱物学 ＞ 結晶学 ＞ 結晶の生成・成長・溶解
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::548.7`

- FACET: `subject`
- NODE_KEY: `subject::548.7`
- CODE: `548.7`
- LABEL: 結晶の微細構造．結晶の不連続体理論
- PARENT_KEY: `subject::548`
- PATH_CODES: `5` > `54` > `548/549` > `548` > `548.7`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 鉱物学関連の科学．結晶学．鉱物学 ＞ 結晶学 ＞ 結晶の微細構造．結晶の不連続体理論
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::549`

- FACET: `subject`
- NODE_KEY: `subject::549`
- CODE: `549`
- LABEL: 鉱物学．鉱物の個別的研究
- PARENT_KEY: `subject::548/549`
- PATH_CODES: `5` > `54` > `548/549` > `549`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 鉱物学関連の科学．結晶学．鉱物学 ＞ 鉱物学．鉱物の個別的研究
- LEAF: false
- DIRECT_CHILDREN_COUNT: 1

### DIRECT_CHILDREN

- `subject::549.2/.8` | CODE `549.2/.8` | 鉱物分類学

<!-- END_FACET_NODE -->

## FACET_NODE `subject::549.2/.8`

- FACET: `subject`
- NODE_KEY: `subject::549.2/.8`
- CODE: `549.2/.8`
- LABEL: 鉱物分類学
- PARENT_KEY: `subject::549`
- PATH_CODES: `5` > `54` > `548/549` > `549` > `549.2/.8`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 鉱物学関連の科学．結晶学．鉱物学 ＞ 鉱物学．鉱物の個別的研究 ＞ 鉱物分類学
- LEAF: false
- DIRECT_CHILDREN_COUNT: 7

### DIRECT_CHILDREN

- `subject::549.2` | CODE `549.2` | 天然元素および合金
- `subject::549.3` | CODE `549.3` | 硫化鉱物．硫黄含有塩
- `subject::549.4` | CODE `549.4` | ハロゲン化物
- `subject::549.5` | CODE `549.5` | 酸素化合物
- `subject::549.6` | CODE `549.6` | 珪酸塩．チタン酸塩．ジルコン酸塩．錫酸塩
- `subject::549.7` | CODE `549.7` | その他の酸素酸化合物
- `subject::549.8` | CODE `549.8` | 有機鉱物

<!-- END_FACET_NODE -->

## FACET_NODE `subject::549.2`

- FACET: `subject`
- NODE_KEY: `subject::549.2`
- CODE: `549.2`
- LABEL: 天然元素および合金
- PARENT_KEY: `subject::549.2/.8`
- PATH_CODES: `5` > `54` > `548/549` > `549` > `549.2/.8` > `549.2`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 鉱物学関連の科学．結晶学．鉱物学 ＞ 鉱物学．鉱物の個別的研究 ＞ 鉱物分類学 ＞ 天然元素および合金
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::549.3`

- FACET: `subject`
- NODE_KEY: `subject::549.3`
- CODE: `549.3`
- LABEL: 硫化鉱物．硫黄含有塩
- PARENT_KEY: `subject::549.2/.8`
- PATH_CODES: `5` > `54` > `548/549` > `549` > `549.2/.8` > `549.3`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 鉱物学関連の科学．結晶学．鉱物学 ＞ 鉱物学．鉱物の個別的研究 ＞ 鉱物分類学 ＞ 硫化鉱物．硫黄含有塩
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::549.4`

- FACET: `subject`
- NODE_KEY: `subject::549.4`
- CODE: `549.4`
- LABEL: ハロゲン化物
- PARENT_KEY: `subject::549.2/.8`
- PATH_CODES: `5` > `54` > `548/549` > `549` > `549.2/.8` > `549.4`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 鉱物学関連の科学．結晶学．鉱物学 ＞ 鉱物学．鉱物の個別的研究 ＞ 鉱物分類学 ＞ ハロゲン化物
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::549.5`

- FACET: `subject`
- NODE_KEY: `subject::549.5`
- CODE: `549.5`
- LABEL: 酸素化合物
- PARENT_KEY: `subject::549.2/.8`
- PATH_CODES: `5` > `54` > `548/549` > `549` > `549.2/.8` > `549.5`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 鉱物学関連の科学．結晶学．鉱物学 ＞ 鉱物学．鉱物の個別的研究 ＞ 鉱物分類学 ＞ 酸素化合物
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::549.6`

- FACET: `subject`
- NODE_KEY: `subject::549.6`
- CODE: `549.6`
- LABEL: 珪酸塩．チタン酸塩．ジルコン酸塩．錫酸塩
- PARENT_KEY: `subject::549.2/.8`
- PATH_CODES: `5` > `54` > `548/549` > `549` > `549.2/.8` > `549.6`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 鉱物学関連の科学．結晶学．鉱物学 ＞ 鉱物学．鉱物の個別的研究 ＞ 鉱物分類学 ＞ 珪酸塩．チタン酸塩．ジルコン酸塩．錫酸塩
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::549.7`

- FACET: `subject`
- NODE_KEY: `subject::549.7`
- CODE: `549.7`
- LABEL: その他の酸素酸化合物
- PARENT_KEY: `subject::549.2/.8`
- PATH_CODES: `5` > `54` > `548/549` > `549` > `549.2/.8` > `549.7`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 鉱物学関連の科学．結晶学．鉱物学 ＞ 鉱物学．鉱物の個別的研究 ＞ 鉱物分類学 ＞ その他の酸素酸化合物
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::549.8`

- FACET: `subject`
- NODE_KEY: `subject::549.8`
- CODE: `549.8`
- LABEL: 有機鉱物
- PARENT_KEY: `subject::549.2/.8`
- PATH_CODES: `5` > `54` > `548/549` > `549` > `549.2/.8` > `549.8`
- PATH_LABELS: 数学．自然科学 ＞ 化学．結晶学．鉱物学 ＞ 鉱物学関連の科学．結晶学．鉱物学 ＞ 鉱物学．鉱物の個別的研究 ＞ 鉱物分類学 ＞ 有機鉱物
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::55`

- FACET: `subject`
- NODE_KEY: `subject::55`
- CODE: `55`
- LABEL: 地球科学．地質学
- PARENT_KEY: `subject::5`
- PATH_CODES: `5` > `55`
- PATH_LABELS: 数学．自然科学 ＞ 地球科学．地質学
- LEAF: false
- DIRECT_CHILDREN_COUNT: 4

### DIRECT_CHILDREN

- `subject::550` | CODE `550` | 地質学などの補助学
- `subject::551` | CODE `551` | 一般地質学．気象学．気候学．歴史地質学．層位学．古地理学
- `subject::552` | CODE `552` | 岩石学．記載岩石学
- `subject::553` | CODE `553` | 経済地質学．鉱床

<!-- END_FACET_NODE -->

## FACET_NODE `subject::550`

- FACET: `subject`
- NODE_KEY: `subject::550`
- CODE: `550`
- LABEL: 地質学などの補助学
- PARENT_KEY: `subject::55`
- PATH_CODES: `5` > `55` > `550`
- PATH_LABELS: 数学．自然科学 ＞ 地球科学．地質学 ＞ 地質学などの補助学
- LEAF: false
- DIRECT_CHILDREN_COUNT: 7

### DIRECT_CHILDREN

- `subject::550.1` | CODE `550.1` | 自然地理学
- `subject::550.2` | CODE `550.2` | 地球天文学．宇宙進化論
- `subject::550.3` | CODE `550.3` | 地球物理学
- `subject::550.4` | CODE `550.4` | 地球化学
- `subject::550.7` | CODE `550.7` | 地球生物学．生物の地質学的作用
- `subject::550.8` | CODE `550.8` | 応用地質学および地球物理学．地質学的探鉱および探査
- `subject::550.93` | CODE `550.93` | 地球年代学．地質年代決定．絶対値決定

<!-- END_FACET_NODE -->

## FACET_NODE `subject::550.1`

- FACET: `subject`
- NODE_KEY: `subject::550.1`
- CODE: `550.1`
- LABEL: 自然地理学
- PARENT_KEY: `subject::550`
- PATH_CODES: `5` > `55` > `550` > `550.1`
- PATH_LABELS: 数学．自然科学 ＞ 地球科学．地質学 ＞ 地質学などの補助学 ＞ 自然地理学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::550.2`

- FACET: `subject`
- NODE_KEY: `subject::550.2`
- CODE: `550.2`
- LABEL: 地球天文学．宇宙進化論
- PARENT_KEY: `subject::550`
- PATH_CODES: `5` > `55` > `550` > `550.2`
- PATH_LABELS: 数学．自然科学 ＞ 地球科学．地質学 ＞ 地質学などの補助学 ＞ 地球天文学．宇宙進化論
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::550.3`

- FACET: `subject`
- NODE_KEY: `subject::550.3`
- CODE: `550.3`
- LABEL: 地球物理学
- PARENT_KEY: `subject::550`
- PATH_CODES: `5` > `55` > `550` > `550.3`
- PATH_LABELS: 数学．自然科学 ＞ 地球科学．地質学 ＞ 地質学などの補助学 ＞ 地球物理学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::550.4`

- FACET: `subject`
- NODE_KEY: `subject::550.4`
- CODE: `550.4`
- LABEL: 地球化学
- PARENT_KEY: `subject::550`
- PATH_CODES: `5` > `55` > `550` > `550.4`
- PATH_LABELS: 数学．自然科学 ＞ 地球科学．地質学 ＞ 地質学などの補助学 ＞ 地球化学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::550.7`

- FACET: `subject`
- NODE_KEY: `subject::550.7`
- CODE: `550.7`
- LABEL: 地球生物学．生物の地質学的作用
- PARENT_KEY: `subject::550`
- PATH_CODES: `5` > `55` > `550` > `550.7`
- PATH_LABELS: 数学．自然科学 ＞ 地球科学．地質学 ＞ 地質学などの補助学 ＞ 地球生物学．生物の地質学的作用
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::550.8`

- FACET: `subject`
- NODE_KEY: `subject::550.8`
- CODE: `550.8`
- LABEL: 応用地質学および地球物理学．地質学的探鉱および探査
- PARENT_KEY: `subject::550`
- PATH_CODES: `5` > `55` > `550` > `550.8`
- PATH_LABELS: 数学．自然科学 ＞ 地球科学．地質学 ＞ 地質学などの補助学 ＞ 応用地質学および地球物理学．地質学的探鉱および探査
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::550.93`

- FACET: `subject`
- NODE_KEY: `subject::550.93`
- CODE: `550.93`
- LABEL: 地球年代学．地質年代決定．絶対値決定
- PARENT_KEY: `subject::550`
- PATH_CODES: `5` > `55` > `550` > `550.93`
- PATH_LABELS: 数学．自然科学 ＞ 地球科学．地質学 ＞ 地質学などの補助学 ＞ 地球年代学．地質年代決定．絶対値決定
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::551`

- FACET: `subject`
- NODE_KEY: `subject::551`
- CODE: `551`
- LABEL: 一般地質学．気象学．気候学．歴史地質学．層位学．古地理学
- PARENT_KEY: `subject::55`
- PATH_CODES: `5` > `55` > `551`
- PATH_LABELS: 数学．自然科学 ＞ 地球科学．地質学 ＞ 一般地質学．気象学．気候学．歴史地質学．層位学．古地理学
- LEAF: false
- DIRECT_CHILDREN_COUNT: 6

### DIRECT_CHILDREN

- `subject::551.1/.4` | CODE `551.1/.4` | 一般地質学
- `subject::551.46` | CODE `551.46` | 海洋物理学．海中地形図．海洋底
- `subject::551.5` | CODE `551.5` | 気象学
- `subject::551.58` | CODE `551.58` | 気候学
- `subject::551.7` | CODE `551.7` | 歴史地質学．層位学
- `subject::551.8` | CODE `551.8` | 古地理学

<!-- END_FACET_NODE -->

## FACET_NODE `subject::551.1/.4`

- FACET: `subject`
- NODE_KEY: `subject::551.1/.4`
- CODE: `551.1/.4`
- LABEL: 一般地質学
- PARENT_KEY: `subject::551`
- PATH_CODES: `5` > `55` > `551` > `551.1/.4`
- PATH_LABELS: 数学．自然科学 ＞ 地球科学．地質学 ＞ 一般地質学．気象学．気候学．歴史地質学．層位学．古地理学 ＞ 一般地質学
- LEAF: false
- DIRECT_CHILDREN_COUNT: 4

### DIRECT_CHILDREN

- `subject::551.1` | CODE `551.1` | 地球の全体的構造
- `subject::551.2` | CODE `551.2` | 内部地球力学(内因的過程)
- `subject::551.3` | CODE `551.3` | 外部地球力学(外因性過程)
- `subject::551.4` | CODE `551.4` | 地形学．陸地の物理的形状の研究

<!-- END_FACET_NODE -->

## FACET_NODE `subject::551.1`

- FACET: `subject`
- NODE_KEY: `subject::551.1`
- CODE: `551.1`
- LABEL: 地球の全体的構造
- PARENT_KEY: `subject::551.1/.4`
- PATH_CODES: `5` > `55` > `551` > `551.1/.4` > `551.1`
- PATH_LABELS: 数学．自然科学 ＞ 地球科学．地質学 ＞ 一般地質学．気象学．気候学．歴史地質学．層位学．古地理学 ＞ 一般地質学 ＞ 地球の全体的構造
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::551.2`

- FACET: `subject`
- NODE_KEY: `subject::551.2`
- CODE: `551.2`
- LABEL: 内部地球力学(内因的過程)
- PARENT_KEY: `subject::551.1/.4`
- PATH_CODES: `5` > `55` > `551` > `551.1/.4` > `551.2`
- PATH_LABELS: 数学．自然科学 ＞ 地球科学．地質学 ＞ 一般地質学．気象学．気候学．歴史地質学．層位学．古地理学 ＞ 一般地質学 ＞ 内部地球力学(内因的過程)
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::551.3`

- FACET: `subject`
- NODE_KEY: `subject::551.3`
- CODE: `551.3`
- LABEL: 外部地球力学(外因性過程)
- PARENT_KEY: `subject::551.1/.4`
- PATH_CODES: `5` > `55` > `551` > `551.1/.4` > `551.3`
- PATH_LABELS: 数学．自然科学 ＞ 地球科学．地質学 ＞ 一般地質学．気象学．気候学．歴史地質学．層位学．古地理学 ＞ 一般地質学 ＞ 外部地球力学(外因性過程)
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::551.4`

- FACET: `subject`
- NODE_KEY: `subject::551.4`
- CODE: `551.4`
- LABEL: 地形学．陸地の物理的形状の研究
- PARENT_KEY: `subject::551.1/.4`
- PATH_CODES: `5` > `55` > `551` > `551.1/.4` > `551.4`
- PATH_LABELS: 数学．自然科学 ＞ 地球科学．地質学 ＞ 一般地質学．気象学．気候学．歴史地質学．層位学．古地理学 ＞ 一般地質学 ＞ 地形学．陸地の物理的形状の研究
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::551.46`

- FACET: `subject`
- NODE_KEY: `subject::551.46`
- CODE: `551.46`
- LABEL: 海洋物理学．海中地形図．海洋底
- PARENT_KEY: `subject::551`
- PATH_CODES: `5` > `55` > `551` > `551.46`
- PATH_LABELS: 数学．自然科学 ＞ 地球科学．地質学 ＞ 一般地質学．気象学．気候学．歴史地質学．層位学．古地理学 ＞ 海洋物理学．海中地形図．海洋底
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::551.5`

- FACET: `subject`
- NODE_KEY: `subject::551.5`
- CODE: `551.5`
- LABEL: 気象学
- PARENT_KEY: `subject::551`
- PATH_CODES: `5` > `55` > `551` > `551.5`
- PATH_LABELS: 数学．自然科学 ＞ 地球科学．地質学 ＞ 一般地質学．気象学．気候学．歴史地質学．層位学．古地理学 ＞ 気象学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::551.58`

- FACET: `subject`
- NODE_KEY: `subject::551.58`
- CODE: `551.58`
- LABEL: 気候学
- PARENT_KEY: `subject::551`
- PATH_CODES: `5` > `55` > `551` > `551.58`
- PATH_LABELS: 数学．自然科学 ＞ 地球科学．地質学 ＞ 一般地質学．気象学．気候学．歴史地質学．層位学．古地理学 ＞ 気候学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::551.7`

- FACET: `subject`
- NODE_KEY: `subject::551.7`
- CODE: `551.7`
- LABEL: 歴史地質学．層位学
- PARENT_KEY: `subject::551`
- PATH_CODES: `5` > `55` > `551` > `551.7`
- PATH_LABELS: 数学．自然科学 ＞ 地球科学．地質学 ＞ 一般地質学．気象学．気候学．歴史地質学．層位学．古地理学 ＞ 歴史地質学．層位学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::551.8`

- FACET: `subject`
- NODE_KEY: `subject::551.8`
- CODE: `551.8`
- LABEL: 古地理学
- PARENT_KEY: `subject::551`
- PATH_CODES: `5` > `55` > `551` > `551.8`
- PATH_LABELS: 数学．自然科学 ＞ 地球科学．地質学 ＞ 一般地質学．気象学．気候学．歴史地質学．層位学．古地理学 ＞ 古地理学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::552`

- FACET: `subject`
- NODE_KEY: `subject::552`
- CODE: `552`
- LABEL: 岩石学．記載岩石学
- PARENT_KEY: `subject::55`
- PATH_CODES: `5` > `55` > `552`
- PATH_LABELS: 数学．自然科学 ＞ 地球科学．地質学 ＞ 岩石学．記載岩石学
- LEAF: false
- DIRECT_CHILDREN_COUNT: 2

### DIRECT_CHILDREN

- `subject::552.1` | CODE `552.1` | 岩石の特徴と性質一般．物理的・物理化学的岩石学
- `subject::552.3/.6` | CODE `552.3/.6` | 火成岩．堆積岩，変成岩

<!-- END_FACET_NODE -->

## FACET_NODE `subject::552.1`

- FACET: `subject`
- NODE_KEY: `subject::552.1`
- CODE: `552.1`
- LABEL: 岩石の特徴と性質一般．物理的・物理化学的岩石学
- PARENT_KEY: `subject::552`
- PATH_CODES: `5` > `55` > `552` > `552.1`
- PATH_LABELS: 数学．自然科学 ＞ 地球科学．地質学 ＞ 岩石学．記載岩石学 ＞ 岩石の特徴と性質一般．物理的・物理化学的岩石学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::552.3/.6`

- FACET: `subject`
- NODE_KEY: `subject::552.3/.6`
- CODE: `552.3/.6`
- LABEL: 火成岩．堆積岩，変成岩
- PARENT_KEY: `subject::552`
- PATH_CODES: `5` > `55` > `552` > `552.3/.6`
- PATH_LABELS: 数学．自然科学 ＞ 地球科学．地質学 ＞ 岩石学．記載岩石学 ＞ 火成岩．堆積岩，変成岩
- LEAF: false
- DIRECT_CHILDREN_COUNT: 4

### DIRECT_CHILDREN

- `subject::552.3` | CODE `552.3` | 岩漿岩．火成岩
- `subject::552.4` | CODE `552.4` | 変成岩
- `subject::552.5` | CODE `552.5` | 堆積岩
- `subject::552.6` | CODE `552.6` | 隕石

<!-- END_FACET_NODE -->

## FACET_NODE `subject::552.3`

- FACET: `subject`
- NODE_KEY: `subject::552.3`
- CODE: `552.3`
- LABEL: 岩漿岩．火成岩
- PARENT_KEY: `subject::552.3/.6`
- PATH_CODES: `5` > `55` > `552` > `552.3/.6` > `552.3`
- PATH_LABELS: 数学．自然科学 ＞ 地球科学．地質学 ＞ 岩石学．記載岩石学 ＞ 火成岩．堆積岩，変成岩 ＞ 岩漿岩．火成岩
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::552.4`

- FACET: `subject`
- NODE_KEY: `subject::552.4`
- CODE: `552.4`
- LABEL: 変成岩
- PARENT_KEY: `subject::552.3/.6`
- PATH_CODES: `5` > `55` > `552` > `552.3/.6` > `552.4`
- PATH_LABELS: 数学．自然科学 ＞ 地球科学．地質学 ＞ 岩石学．記載岩石学 ＞ 火成岩．堆積岩，変成岩 ＞ 変成岩
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::552.5`

- FACET: `subject`
- NODE_KEY: `subject::552.5`
- CODE: `552.5`
- LABEL: 堆積岩
- PARENT_KEY: `subject::552.3/.6`
- PATH_CODES: `5` > `55` > `552` > `552.3/.6` > `552.5`
- PATH_LABELS: 数学．自然科学 ＞ 地球科学．地質学 ＞ 岩石学．記載岩石学 ＞ 火成岩．堆積岩，変成岩 ＞ 堆積岩
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::552.6`

- FACET: `subject`
- NODE_KEY: `subject::552.6`
- CODE: `552.6`
- LABEL: 隕石
- PARENT_KEY: `subject::552.3/.6`
- PATH_CODES: `5` > `55` > `552` > `552.3/.6` > `552.6`
- PATH_LABELS: 数学．自然科学 ＞ 地球科学．地質学 ＞ 岩石学．記載岩石学 ＞ 火成岩．堆積岩，変成岩 ＞ 隕石
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::553`

- FACET: `subject`
- NODE_KEY: `subject::553`
- CODE: `553`
- LABEL: 経済地質学．鉱床
- PARENT_KEY: `subject::55`
- PATH_CODES: `5` > `55` > `553`
- PATH_LABELS: 数学．自然科学 ＞ 地球科学．地質学 ＞ 経済地質学．鉱床
- LEAF: false
- DIRECT_CHILDREN_COUNT: 2

### DIRECT_CHILDREN

- `subject::553.2` | CODE `553.2` | 鉱石の生成．鉱物の生成
- `subject::553.3/.9` | CODE `553.3/.9` | 鉱石および鉱床．天然資源

<!-- END_FACET_NODE -->

## FACET_NODE `subject::553.2`

- FACET: `subject`
- NODE_KEY: `subject::553.2`
- CODE: `553.2`
- LABEL: 鉱石の生成．鉱物の生成
- PARENT_KEY: `subject::553`
- PATH_CODES: `5` > `55` > `553` > `553.2`
- PATH_LABELS: 数学．自然科学 ＞ 地球科学．地質学 ＞ 経済地質学．鉱床 ＞ 鉱石の生成．鉱物の生成
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::553.3/.9`

- FACET: `subject`
- NODE_KEY: `subject::553.3/.9`
- CODE: `553.3/.9`
- LABEL: 鉱石および鉱床．天然資源
- PARENT_KEY: `subject::553`
- PATH_CODES: `5` > `55` > `553` > `553.3/.9`
- PATH_LABELS: 数学．自然科学 ＞ 地球科学．地質学 ＞ 経済地質学．鉱床 ＞ 鉱石および鉱床．天然資源
- LEAF: false
- DIRECT_CHILDREN_COUNT: 7

### DIRECT_CHILDREN

- `subject::553.3` | CODE `553.3` | 鉱床(金属鉱床)一般．鉄鉱およびマンガン鉱
- `subject::553.4` | CODE `553.4` | 鉄・マンガン以外の鉱床
- `subject::553.5` | CODE `553.5` | 天然石鉱床
- `subject::553.6` | CODE `553.6` | 各種無機有用鉱物と土砂(主に金属を含まない)の鉱床
- `subject::553.7` | CODE `553.7` | 鉱泉
- `subject::553.8` | CODE `553.8` | 貴石．準貴石鉱床．宝石鉱床
- `subject::553.9` | CODE `553.9` | 炭素質の鉱床．炭化水素鉱床

<!-- END_FACET_NODE -->

## FACET_NODE `subject::553.3`

- FACET: `subject`
- NODE_KEY: `subject::553.3`
- CODE: `553.3`
- LABEL: 鉱床(金属鉱床)一般．鉄鉱およびマンガン鉱
- PARENT_KEY: `subject::553.3/.9`
- PATH_CODES: `5` > `55` > `553` > `553.3/.9` > `553.3`
- PATH_LABELS: 数学．自然科学 ＞ 地球科学．地質学 ＞ 経済地質学．鉱床 ＞ 鉱石および鉱床．天然資源 ＞ 鉱床(金属鉱床)一般．鉄鉱およびマンガン鉱
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::553.4`

- FACET: `subject`
- NODE_KEY: `subject::553.4`
- CODE: `553.4`
- LABEL: 鉄・マンガン以外の鉱床
- PARENT_KEY: `subject::553.3/.9`
- PATH_CODES: `5` > `55` > `553` > `553.3/.9` > `553.4`
- PATH_LABELS: 数学．自然科学 ＞ 地球科学．地質学 ＞ 経済地質学．鉱床 ＞ 鉱石および鉱床．天然資源 ＞ 鉄・マンガン以外の鉱床
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::553.5`

- FACET: `subject`
- NODE_KEY: `subject::553.5`
- CODE: `553.5`
- LABEL: 天然石鉱床
- PARENT_KEY: `subject::553.3/.9`
- PATH_CODES: `5` > `55` > `553` > `553.3/.9` > `553.5`
- PATH_LABELS: 数学．自然科学 ＞ 地球科学．地質学 ＞ 経済地質学．鉱床 ＞ 鉱石および鉱床．天然資源 ＞ 天然石鉱床
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::553.6`

- FACET: `subject`
- NODE_KEY: `subject::553.6`
- CODE: `553.6`
- LABEL: 各種無機有用鉱物と土砂(主に金属を含まない)の鉱床
- PARENT_KEY: `subject::553.3/.9`
- PATH_CODES: `5` > `55` > `553` > `553.3/.9` > `553.6`
- PATH_LABELS: 数学．自然科学 ＞ 地球科学．地質学 ＞ 経済地質学．鉱床 ＞ 鉱石および鉱床．天然資源 ＞ 各種無機有用鉱物と土砂(主に金属を含まない)の鉱床
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::553.7`

- FACET: `subject`
- NODE_KEY: `subject::553.7`
- CODE: `553.7`
- LABEL: 鉱泉
- PARENT_KEY: `subject::553.3/.9`
- PATH_CODES: `5` > `55` > `553` > `553.3/.9` > `553.7`
- PATH_LABELS: 数学．自然科学 ＞ 地球科学．地質学 ＞ 経済地質学．鉱床 ＞ 鉱石および鉱床．天然資源 ＞ 鉱泉
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::553.8`

- FACET: `subject`
- NODE_KEY: `subject::553.8`
- CODE: `553.8`
- LABEL: 貴石．準貴石鉱床．宝石鉱床
- PARENT_KEY: `subject::553.3/.9`
- PATH_CODES: `5` > `55` > `553` > `553.3/.9` > `553.8`
- PATH_LABELS: 数学．自然科学 ＞ 地球科学．地質学 ＞ 経済地質学．鉱床 ＞ 鉱石および鉱床．天然資源 ＞ 貴石．準貴石鉱床．宝石鉱床
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::553.9`

- FACET: `subject`
- NODE_KEY: `subject::553.9`
- CODE: `553.9`
- LABEL: 炭素質の鉱床．炭化水素鉱床
- PARENT_KEY: `subject::553.3/.9`
- PATH_CODES: `5` > `55` > `553` > `553.3/.9` > `553.9`
- PATH_LABELS: 数学．自然科学 ＞ 地球科学．地質学 ＞ 経済地質学．鉱床 ＞ 鉱石および鉱床．天然資源 ＞ 炭素質の鉱床．炭化水素鉱床
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::56`

- FACET: `subject`
- NODE_KEY: `subject::56`
- CODE: `56`
- LABEL: 古生物学
- PARENT_KEY: `subject::5`
- PATH_CODES: `5` > `56`
- PATH_LABELS: 数学．自然科学 ＞ 古生物学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::57`

- FACET: `subject`
- NODE_KEY: `subject::57`
- CODE: `57`
- LABEL: 生物科学一般
- PARENT_KEY: `subject::5`
- PATH_CODES: `5` > `57`
- PATH_LABELS: 数学．自然科学 ＞ 生物科学一般
- LEAF: false
- DIRECT_CHILDREN_COUNT: 9

### DIRECT_CHILDREN

- `subject::57.01/.08` | CODE `57.01/.08` | 生物学における一般法則，理論的観点，特徴，ファクターなどに関する固有補助番号
- `subject::572` | CODE `572` | 自然人類学
- `subject::573` | CODE `573` | 一般生態学と生物分布学．水生生物学．生物地理学
- `subject::574` | CODE `574` | 一般生物の多様性
- `subject::575` | CODE `575` | 一般遺伝学．一般細胞遺伝学
- `subject::576` | CODE `576` | 生命細胞生物学．細胞学
- `subject::577` | CODE `577` | 生命の物質的基盤．生化学．分子生物学．生物物理学
- `subject::578` | CODE `578` | ウィルス学
- `subject::579` | CODE `579` | 微生物学

<!-- END_FACET_NODE -->

## FACET_NODE `subject::57.01/.08`

- FACET: `subject`
- NODE_KEY: `subject::57.01/.08`
- CODE: `57.01/.08`
- LABEL: 生物学における一般法則，理論的観点，特徴，ファクターなどに関する固有補助番号
- PARENT_KEY: `subject::57`
- PATH_CODES: `5` > `57` > `57.01/.08`
- PATH_LABELS: 数学．自然科学 ＞ 生物科学一般 ＞ 生物学における一般法則，理論的観点，特徴，ファクターなどに関する固有補助番号
- LEAF: false
- DIRECT_CHILDREN_COUNT: 8

### DIRECT_CHILDREN

- `subject::57.01` | CODE `57.01` | 一般法則.理論的観点．特徴．性質
- `subject::57.02` | CODE `57.02` | 生物学的，生態学的プロセス
- `subject::57.03` | CODE `57.03` | 変異(特異性)のパターン
- `subject::57.04` | CODE `57.04` | ファクター．影響
- `subject::57.05` | CODE `57.05` | 制御系に関連する特性．さまざまなレベルでの制御系の原理
- `subject::57.06` | CODE `57.06` | 生物組織の命名法と分類．分類学
- `subject::57.07` | CODE `57.07` | 分析古生物学
- `subject::57.08` | CODE `57.08` | 生物学の技術，実験方法，実験装置

<!-- END_FACET_NODE -->

## FACET_NODE `subject::57.01`

- FACET: `subject`
- NODE_KEY: `subject::57.01`
- CODE: `57.01`
- LABEL: 一般法則.理論的観点．特徴．性質
- PARENT_KEY: `subject::57.01/.08`
- PATH_CODES: `5` > `57` > `57.01/.08` > `57.01`
- PATH_LABELS: 数学．自然科学 ＞ 生物科学一般 ＞ 生物学における一般法則，理論的観点，特徴，ファクターなどに関する固有補助番号 ＞ 一般法則.理論的観点．特徴．性質
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::57.02`

- FACET: `subject`
- NODE_KEY: `subject::57.02`
- CODE: `57.02`
- LABEL: 生物学的，生態学的プロセス
- PARENT_KEY: `subject::57.01/.08`
- PATH_CODES: `5` > `57` > `57.01/.08` > `57.02`
- PATH_LABELS: 数学．自然科学 ＞ 生物科学一般 ＞ 生物学における一般法則，理論的観点，特徴，ファクターなどに関する固有補助番号 ＞ 生物学的，生態学的プロセス
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::57.03`

- FACET: `subject`
- NODE_KEY: `subject::57.03`
- CODE: `57.03`
- LABEL: 変異(特異性)のパターン
- PARENT_KEY: `subject::57.01/.08`
- PATH_CODES: `5` > `57` > `57.01/.08` > `57.03`
- PATH_LABELS: 数学．自然科学 ＞ 生物科学一般 ＞ 生物学における一般法則，理論的観点，特徴，ファクターなどに関する固有補助番号 ＞ 変異(特異性)のパターン
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::57.04`

- FACET: `subject`
- NODE_KEY: `subject::57.04`
- CODE: `57.04`
- LABEL: ファクター．影響
- PARENT_KEY: `subject::57.01/.08`
- PATH_CODES: `5` > `57` > `57.01/.08` > `57.04`
- PATH_LABELS: 数学．自然科学 ＞ 生物科学一般 ＞ 生物学における一般法則，理論的観点，特徴，ファクターなどに関する固有補助番号 ＞ ファクター．影響
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::57.05`

- FACET: `subject`
- NODE_KEY: `subject::57.05`
- CODE: `57.05`
- LABEL: 制御系に関連する特性．さまざまなレベルでの制御系の原理
- PARENT_KEY: `subject::57.01/.08`
- PATH_CODES: `5` > `57` > `57.01/.08` > `57.05`
- PATH_LABELS: 数学．自然科学 ＞ 生物科学一般 ＞ 生物学における一般法則，理論的観点，特徴，ファクターなどに関する固有補助番号 ＞ 制御系に関連する特性．さまざまなレベルでの制御系の原理
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::57.06`

- FACET: `subject`
- NODE_KEY: `subject::57.06`
- CODE: `57.06`
- LABEL: 生物組織の命名法と分類．分類学
- PARENT_KEY: `subject::57.01/.08`
- PATH_CODES: `5` > `57` > `57.01/.08` > `57.06`
- PATH_LABELS: 数学．自然科学 ＞ 生物科学一般 ＞ 生物学における一般法則，理論的観点，特徴，ファクターなどに関する固有補助番号 ＞ 生物組織の命名法と分類．分類学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::57.07`

- FACET: `subject`
- NODE_KEY: `subject::57.07`
- CODE: `57.07`
- LABEL: 分析古生物学
- PARENT_KEY: `subject::57.01/.08`
- PATH_CODES: `5` > `57` > `57.01/.08` > `57.07`
- PATH_LABELS: 数学．自然科学 ＞ 生物科学一般 ＞ 生物学における一般法則，理論的観点，特徴，ファクターなどに関する固有補助番号 ＞ 分析古生物学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::57.08`

- FACET: `subject`
- NODE_KEY: `subject::57.08`
- CODE: `57.08`
- LABEL: 生物学の技術，実験方法，実験装置
- PARENT_KEY: `subject::57.01/.08`
- PATH_CODES: `5` > `57` > `57.01/.08` > `57.08`
- PATH_LABELS: 数学．自然科学 ＞ 生物科学一般 ＞ 生物学における一般法則，理論的観点，特徴，ファクターなどに関する固有補助番号 ＞ 生物学の技術，実験方法，実験装置
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::572`

- FACET: `subject`
- NODE_KEY: `subject::572`
- CODE: `572`
- LABEL: 自然人類学
- PARENT_KEY: `subject::57`
- PATH_CODES: `5` > `57` > `572`
- PATH_LABELS: 数学．自然科学 ＞ 生物科学一般 ＞ 自然人類学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::573`

- FACET: `subject`
- NODE_KEY: `subject::573`
- CODE: `573`
- LABEL: 一般生態学と生物分布学．水生生物学．生物地理学
- PARENT_KEY: `subject::57`
- PATH_CODES: `5` > `57` > `573`
- PATH_LABELS: 数学．自然科学 ＞ 生物科学一般 ＞ 一般生態学と生物分布学．水生生物学．生物地理学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::574`

- FACET: `subject`
- NODE_KEY: `subject::574`
- CODE: `574`
- LABEL: 一般生物の多様性
- PARENT_KEY: `subject::57`
- PATH_CODES: `5` > `57` > `574`
- PATH_LABELS: 数学．自然科学 ＞ 生物科学一般 ＞ 一般生物の多様性
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::575`

- FACET: `subject`
- NODE_KEY: `subject::575`
- CODE: `575`
- LABEL: 一般遺伝学．一般細胞遺伝学
- PARENT_KEY: `subject::57`
- PATH_CODES: `5` > `57` > `575`
- PATH_LABELS: 数学．自然科学 ＞ 生物科学一般 ＞ 一般遺伝学．一般細胞遺伝学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::576`

- FACET: `subject`
- NODE_KEY: `subject::576`
- CODE: `576`
- LABEL: 生命細胞生物学．細胞学
- PARENT_KEY: `subject::57`
- PATH_CODES: `5` > `57` > `576`
- PATH_LABELS: 数学．自然科学 ＞ 生物科学一般 ＞ 生命細胞生物学．細胞学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::577`

- FACET: `subject`
- NODE_KEY: `subject::577`
- CODE: `577`
- LABEL: 生命の物質的基盤．生化学．分子生物学．生物物理学
- PARENT_KEY: `subject::57`
- PATH_CODES: `5` > `57` > `577`
- PATH_LABELS: 数学．自然科学 ＞ 生物科学一般 ＞ 生命の物質的基盤．生化学．分子生物学．生物物理学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::578`

- FACET: `subject`
- NODE_KEY: `subject::578`
- CODE: `578`
- LABEL: ウィルス学
- PARENT_KEY: `subject::57`
- PATH_CODES: `5` > `57` > `578`
- PATH_LABELS: 数学．自然科学 ＞ 生物科学一般 ＞ ウィルス学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::579`

- FACET: `subject`
- NODE_KEY: `subject::579`
- CODE: `579`
- LABEL: 微生物学
- PARENT_KEY: `subject::57`
- PATH_CODES: `5` > `57` > `579`
- PATH_LABELS: 数学．自然科学 ＞ 生物科学一般 ＞ 微生物学
- LEAF: false
- DIRECT_CHILDREN_COUNT: 3

### DIRECT_CHILDREN

- `subject::579.2` | CODE `579.2` | 一般微生物学
- `subject::579.6` | CODE `579.6` | 応用微生物学
- `subject::579.8` | CODE `579.8` | 微生物

<!-- END_FACET_NODE -->

## FACET_NODE `subject::579.2`

- FACET: `subject`
- NODE_KEY: `subject::579.2`
- CODE: `579.2`
- LABEL: 一般微生物学
- PARENT_KEY: `subject::579`
- PATH_CODES: `5` > `57` > `579` > `579.2`
- PATH_LABELS: 数学．自然科学 ＞ 生物科学一般 ＞ 微生物学 ＞ 一般微生物学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::579.6`

- FACET: `subject`
- NODE_KEY: `subject::579.6`
- CODE: `579.6`
- LABEL: 応用微生物学
- PARENT_KEY: `subject::579`
- PATH_CODES: `5` > `57` > `579` > `579.6`
- PATH_LABELS: 数学．自然科学 ＞ 生物科学一般 ＞ 微生物学 ＞ 応用微生物学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::579.8`

- FACET: `subject`
- NODE_KEY: `subject::579.8`
- CODE: `579.8`
- LABEL: 微生物
- PARENT_KEY: `subject::579`
- PATH_CODES: `5` > `57` > `579` > `579.8`
- PATH_LABELS: 数学．自然科学 ＞ 生物科学一般 ＞ 微生物学 ＞ 微生物
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::58`

- FACET: `subject`
- NODE_KEY: `subject::58`
- CODE: `58`
- LABEL: 植物学
- PARENT_KEY: `subject::5`
- PATH_CODES: `5` > `58`
- PATH_LABELS: 数学．自然科学 ＞ 植物学
- LEAF: false
- DIRECT_CHILDREN_COUNT: 2

### DIRECT_CHILDREN

- `subject::581` | CODE `581` | 一般植物学
- `subject::582` | CODE `582` | 植物分類学

<!-- END_FACET_NODE -->

## FACET_NODE `subject::581`

- FACET: `subject`
- NODE_KEY: `subject::581`
- CODE: `581`
- LABEL: 一般植物学
- PARENT_KEY: `subject::58`
- PATH_CODES: `5` > `58` > `581`
- PATH_LABELS: 数学．自然科学 ＞ 植物学 ＞ 一般植物学
- LEAF: false
- DIRECT_CHILDREN_COUNT: 8

### DIRECT_CHILDREN

- `subject::581.1` | CODE `581.1` | 植物生理学
- `subject::581.2` | CODE `581.2` | 植物の病気．植物病理学
- `subject::581.3` | CODE `581.3` | 植物発生学
- `subject::581.4` | CODE `581.4` | 植物形態学．植物解剖学
- `subject::581.5` | CODE `581.5` | 植物生態学．植物と環境．植物の移動
- `subject::581.6` | CODE `581.6` | 応用植物学．植物の使用．技術植物学．経済植物学
- `subject::581.8` | CODE `581.8` | 植物組織学
- `subject::581.9` | CODE `581.9` | 植物地理学.地理学(植物地理学).植物の散布.植物相(フローラ).植物の地理分布

<!-- END_FACET_NODE -->

## FACET_NODE `subject::581.1`

- FACET: `subject`
- NODE_KEY: `subject::581.1`
- CODE: `581.1`
- LABEL: 植物生理学
- PARENT_KEY: `subject::581`
- PATH_CODES: `5` > `58` > `581` > `581.1`
- PATH_LABELS: 数学．自然科学 ＞ 植物学 ＞ 一般植物学 ＞ 植物生理学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::581.2`

- FACET: `subject`
- NODE_KEY: `subject::581.2`
- CODE: `581.2`
- LABEL: 植物の病気．植物病理学
- PARENT_KEY: `subject::581`
- PATH_CODES: `5` > `58` > `581` > `581.2`
- PATH_LABELS: 数学．自然科学 ＞ 植物学 ＞ 一般植物学 ＞ 植物の病気．植物病理学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::581.3`

- FACET: `subject`
- NODE_KEY: `subject::581.3`
- CODE: `581.3`
- LABEL: 植物発生学
- PARENT_KEY: `subject::581`
- PATH_CODES: `5` > `58` > `581` > `581.3`
- PATH_LABELS: 数学．自然科学 ＞ 植物学 ＞ 一般植物学 ＞ 植物発生学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::581.4`

- FACET: `subject`
- NODE_KEY: `subject::581.4`
- CODE: `581.4`
- LABEL: 植物形態学．植物解剖学
- PARENT_KEY: `subject::581`
- PATH_CODES: `5` > `58` > `581` > `581.4`
- PATH_LABELS: 数学．自然科学 ＞ 植物学 ＞ 一般植物学 ＞ 植物形態学．植物解剖学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::581.5`

- FACET: `subject`
- NODE_KEY: `subject::581.5`
- CODE: `581.5`
- LABEL: 植物生態学．植物と環境．植物の移動
- PARENT_KEY: `subject::581`
- PATH_CODES: `5` > `58` > `581` > `581.5`
- PATH_LABELS: 数学．自然科学 ＞ 植物学 ＞ 一般植物学 ＞ 植物生態学．植物と環境．植物の移動
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::581.6`

- FACET: `subject`
- NODE_KEY: `subject::581.6`
- CODE: `581.6`
- LABEL: 応用植物学．植物の使用．技術植物学．経済植物学
- PARENT_KEY: `subject::581`
- PATH_CODES: `5` > `58` > `581` > `581.6`
- PATH_LABELS: 数学．自然科学 ＞ 植物学 ＞ 一般植物学 ＞ 応用植物学．植物の使用．技術植物学．経済植物学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::581.8`

- FACET: `subject`
- NODE_KEY: `subject::581.8`
- CODE: `581.8`
- LABEL: 植物組織学
- PARENT_KEY: `subject::581`
- PATH_CODES: `5` > `58` > `581` > `581.8`
- PATH_LABELS: 数学．自然科学 ＞ 植物学 ＞ 一般植物学 ＞ 植物組織学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::581.9`

- FACET: `subject`
- NODE_KEY: `subject::581.9`
- CODE: `581.9`
- LABEL: 植物地理学.地理学(植物地理学).植物の散布.植物相(フローラ).植物の地理分布
- PARENT_KEY: `subject::581`
- PATH_CODES: `5` > `58` > `581` > `581.9`
- PATH_LABELS: 数学．自然科学 ＞ 植物学 ＞ 一般植物学 ＞ 植物地理学.地理学(植物地理学).植物の散布.植物相(フローラ).植物の地理分布
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::582`

- FACET: `subject`
- NODE_KEY: `subject::582`
- CODE: `582`
- LABEL: 植物分類学
- PARENT_KEY: `subject::58`
- PATH_CODES: `5` > `58` > `582`
- PATH_LABELS: 数学．自然科学 ＞ 植物学 ＞ 植物分類学
- LEAF: false
- DIRECT_CHILDREN_COUNT: 7

### DIRECT_CHILDREN

- `subject::582.091/.099` | CODE `582.091/.099` | 大きさと形による植物分類の固有補助番号の下位区分
- `subject::582.23` | CODE `582.23` | 細菌類．バクテリア
- `subject::582.24` | CODE `582.24` | 原生生物 Chromista 原虫
- `subject::582.261/.279` | CODE `582.261/.279` | 藻類
- `subject::582.28` | CODE `582.28` | 菌類/真菌類．かび
- `subject::582.29` | CODE `582.29` | 地衣植物類
- `subject::582.32/.998` | CODE `582.32/.998` | 植物界(分類学)

<!-- END_FACET_NODE -->

## FACET_NODE `subject::582.091/.099`

- FACET: `subject`
- NODE_KEY: `subject::582.091/.099`
- CODE: `582.091/.099`
- LABEL: 大きさと形による植物分類の固有補助番号の下位区分
- PARENT_KEY: `subject::582`
- PATH_CODES: `5` > `58` > `582` > `582.091/.099`
- PATH_LABELS: 数学．自然科学 ＞ 植物学 ＞ 植物分類学 ＞ 大きさと形による植物分類の固有補助番号の下位区分
- LEAF: false
- DIRECT_CHILDREN_COUNT: 5

### DIRECT_CHILDREN

- `subject::582.091` | CODE `582.091` | 高木(樹幹がある大きい木本)
- `subject::582.093` | CODE `582.093` | 低木(樹幹がない小さい木本)
- `subject::582.095` | CODE `582.095` | 下層低木
- `subject::582.097` | CODE `582.097` | ツタ類
- `subject::582.099` | CODE `582.099` | 草本かまたは非木本

<!-- END_FACET_NODE -->

## FACET_NODE `subject::582.091`

- FACET: `subject`
- NODE_KEY: `subject::582.091`
- CODE: `582.091`
- LABEL: 高木(樹幹がある大きい木本)
- PARENT_KEY: `subject::582.091/.099`
- PATH_CODES: `5` > `58` > `582` > `582.091/.099` > `582.091`
- PATH_LABELS: 数学．自然科学 ＞ 植物学 ＞ 植物分類学 ＞ 大きさと形による植物分類の固有補助番号の下位区分 ＞ 高木(樹幹がある大きい木本)
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::582.093`

- FACET: `subject`
- NODE_KEY: `subject::582.093`
- CODE: `582.093`
- LABEL: 低木(樹幹がない小さい木本)
- PARENT_KEY: `subject::582.091/.099`
- PATH_CODES: `5` > `58` > `582` > `582.091/.099` > `582.093`
- PATH_LABELS: 数学．自然科学 ＞ 植物学 ＞ 植物分類学 ＞ 大きさと形による植物分類の固有補助番号の下位区分 ＞ 低木(樹幹がない小さい木本)
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::582.095`

- FACET: `subject`
- NODE_KEY: `subject::582.095`
- CODE: `582.095`
- LABEL: 下層低木
- PARENT_KEY: `subject::582.091/.099`
- PATH_CODES: `5` > `58` > `582` > `582.091/.099` > `582.095`
- PATH_LABELS: 数学．自然科学 ＞ 植物学 ＞ 植物分類学 ＞ 大きさと形による植物分類の固有補助番号の下位区分 ＞ 下層低木
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::582.097`

- FACET: `subject`
- NODE_KEY: `subject::582.097`
- CODE: `582.097`
- LABEL: ツタ類
- PARENT_KEY: `subject::582.091/.099`
- PATH_CODES: `5` > `58` > `582` > `582.091/.099` > `582.097`
- PATH_LABELS: 数学．自然科学 ＞ 植物学 ＞ 植物分類学 ＞ 大きさと形による植物分類の固有補助番号の下位区分 ＞ ツタ類
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::582.099`

- FACET: `subject`
- NODE_KEY: `subject::582.099`
- CODE: `582.099`
- LABEL: 草本かまたは非木本
- PARENT_KEY: `subject::582.091/.099`
- PATH_CODES: `5` > `58` > `582` > `582.091/.099` > `582.099`
- PATH_LABELS: 数学．自然科学 ＞ 植物学 ＞ 植物分類学 ＞ 大きさと形による植物分類の固有補助番号の下位区分 ＞ 草本かまたは非木本
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::582.23`

- FACET: `subject`
- NODE_KEY: `subject::582.23`
- CODE: `582.23`
- LABEL: 細菌類．バクテリア
- PARENT_KEY: `subject::582`
- PATH_CODES: `5` > `58` > `582` > `582.23`
- PATH_LABELS: 数学．自然科学 ＞ 植物学 ＞ 植物分類学 ＞ 細菌類．バクテリア
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::582.24`

- FACET: `subject`
- NODE_KEY: `subject::582.24`
- CODE: `582.24`
- LABEL: 原生生物 Chromista 原虫
- PARENT_KEY: `subject::582`
- PATH_CODES: `5` > `58` > `582` > `582.24`
- PATH_LABELS: 数学．自然科学 ＞ 植物学 ＞ 植物分類学 ＞ 原生生物 Chromista 原虫
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::582.261/.279`

- FACET: `subject`
- NODE_KEY: `subject::582.261/.279`
- CODE: `582.261/.279`
- LABEL: 藻類
- PARENT_KEY: `subject::582`
- PATH_CODES: `5` > `58` > `582` > `582.261/.279`
- PATH_LABELS: 数学．自然科学 ＞ 植物学 ＞ 植物分類学 ＞ 藻類
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::582.28`

- FACET: `subject`
- NODE_KEY: `subject::582.28`
- CODE: `582.28`
- LABEL: 菌類/真菌類．かび
- PARENT_KEY: `subject::582`
- PATH_CODES: `5` > `58` > `582` > `582.28`
- PATH_LABELS: 数学．自然科学 ＞ 植物学 ＞ 植物分類学 ＞ 菌類/真菌類．かび
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::582.29`

- FACET: `subject`
- NODE_KEY: `subject::582.29`
- CODE: `582.29`
- LABEL: 地衣植物類
- PARENT_KEY: `subject::582`
- PATH_CODES: `5` > `58` > `582` > `582.29`
- PATH_LABELS: 数学．自然科学 ＞ 植物学 ＞ 植物分類学 ＞ 地衣植物類
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::582.32/.998`

- FACET: `subject`
- NODE_KEY: `subject::582.32/.998`
- CODE: `582.32/.998`
- LABEL: 植物界(分類学)
- PARENT_KEY: `subject::582`
- PATH_CODES: `5` > `58` > `582` > `582.32/.998`
- PATH_LABELS: 数学．自然科学 ＞ 植物学 ＞ 植物分類学 ＞ 植物界(分類学)
- LEAF: false
- DIRECT_CHILDREN_COUNT: 3

### DIRECT_CHILDREN

- `subject::582.32` | CODE `582.32` | 蘇苔類 (蘇類)
- `subject::582.361/.99` | CODE `582.361/.99` | 維管束植物
- `subject::582.4` | CODE `582.4` | 種子植物

<!-- END_FACET_NODE -->

## FACET_NODE `subject::582.32`

- FACET: `subject`
- NODE_KEY: `subject::582.32`
- CODE: `582.32`
- LABEL: 蘇苔類 (蘇類)
- PARENT_KEY: `subject::582.32/.998`
- PATH_CODES: `5` > `58` > `582` > `582.32/.998` > `582.32`
- PATH_LABELS: 数学．自然科学 ＞ 植物学 ＞ 植物分類学 ＞ 植物界(分類学) ＞ 蘇苔類 (蘇類)
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::582.361/.99`

- FACET: `subject`
- NODE_KEY: `subject::582.361/.99`
- CODE: `582.361/.99`
- LABEL: 維管束植物
- PARENT_KEY: `subject::582.32/.998`
- PATH_CODES: `5` > `58` > `582` > `582.32/.998` > `582.361/.99`
- PATH_LABELS: 数学．自然科学 ＞ 植物学 ＞ 植物分類学 ＞ 植物界(分類学) ＞ 維管束植物
- LEAF: false
- DIRECT_CHILDREN_COUNT: 1

### DIRECT_CHILDREN

- `subject::582.37/.39` | CODE `582.37/.39` | シダ植物類．Fernallies．シダ様胞子植物

<!-- END_FACET_NODE -->

## FACET_NODE `subject::582.37/.39`

- FACET: `subject`
- NODE_KEY: `subject::582.37/.39`
- CODE: `582.37/.39`
- LABEL: シダ植物類．Fernallies．シダ様胞子植物
- PARENT_KEY: `subject::582.361/.99`
- PATH_CODES: `5` > `58` > `582` > `582.32/.998` > `582.361/.99` > `582.37/.39`
- PATH_LABELS: 数学．自然科学 ＞ 植物学 ＞ 植物分類学 ＞ 植物界(分類学) ＞ 維管束植物 ＞ シダ植物類．Fernallies．シダ様胞子植物
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::582.4`

- FACET: `subject`
- NODE_KEY: `subject::582.4`
- CODE: `582.4`
- LABEL: 種子植物
- PARENT_KEY: `subject::582.32/.998`
- PATH_CODES: `5` > `58` > `582` > `582.32/.998` > `582.4`
- PATH_LABELS: 数学．自然科学 ＞ 植物学 ＞ 植物分類学 ＞ 植物界(分類学) ＞ 種子植物
- LEAF: false
- DIRECT_CHILDREN_COUNT: 2

### DIRECT_CHILDREN

- `subject::582.42/.49` | CODE `582.42/.49` | 針葉樹類．球果類．裸子植物
- `subject::582.5/.9` | CODE `582.5/.9` | 被子植物類．顕花植物

<!-- END_FACET_NODE -->

## FACET_NODE `subject::582.42/.49`

- FACET: `subject`
- NODE_KEY: `subject::582.42/.49`
- CODE: `582.42/.49`
- LABEL: 針葉樹類．球果類．裸子植物
- PARENT_KEY: `subject::582.4`
- PATH_CODES: `5` > `58` > `582` > `582.32/.998` > `582.4` > `582.42/.49`
- PATH_LABELS: 数学．自然科学 ＞ 植物学 ＞ 植物分類学 ＞ 植物界(分類学) ＞ 種子植物 ＞ 針葉樹類．球果類．裸子植物
- LEAF: false
- DIRECT_CHILDREN_COUNT: 3

### DIRECT_CHILDREN

- `subject::582.44` | CODE `582.44` | ソテツ門
- `subject::582.46` | CODE `582.46` | イチョウ植物門
- `subject::582.47` | CODE `582.47` | 裸子植物

<!-- END_FACET_NODE -->

## FACET_NODE `subject::582.44`

- FACET: `subject`
- NODE_KEY: `subject::582.44`
- CODE: `582.44`
- LABEL: ソテツ門
- PARENT_KEY: `subject::582.42/.49`
- PATH_CODES: `5` > `58` > `582` > `582.32/.998` > `582.4` > `582.42/.49` > `582.44`
- PATH_LABELS: 数学．自然科学 ＞ 植物学 ＞ 植物分類学 ＞ 植物界(分類学) ＞ 種子植物 ＞ 針葉樹類．球果類．裸子植物 ＞ ソテツ門
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::582.46`

- FACET: `subject`
- NODE_KEY: `subject::582.46`
- CODE: `582.46`
- LABEL: イチョウ植物門
- PARENT_KEY: `subject::582.42/.49`
- PATH_CODES: `5` > `58` > `582` > `582.32/.998` > `582.4` > `582.42/.49` > `582.46`
- PATH_LABELS: 数学．自然科学 ＞ 植物学 ＞ 植物分類学 ＞ 植物界(分類学) ＞ 種子植物 ＞ 針葉樹類．球果類．裸子植物 ＞ イチョウ植物門
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::582.47`

- FACET: `subject`
- NODE_KEY: `subject::582.47`
- CODE: `582.47`
- LABEL: 裸子植物
- PARENT_KEY: `subject::582.42/.49`
- PATH_CODES: `5` > `58` > `582` > `582.32/.998` > `582.4` > `582.42/.49` > `582.47`
- PATH_LABELS: 数学．自然科学 ＞ 植物学 ＞ 植物分類学 ＞ 植物界(分類学) ＞ 種子植物 ＞ 針葉樹類．球果類．裸子植物 ＞ 裸子植物
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::582.5/.9`

- FACET: `subject`
- NODE_KEY: `subject::582.5/.9`
- CODE: `582.5/.9`
- LABEL: 被子植物類．顕花植物
- PARENT_KEY: `subject::582.4`
- PATH_CODES: `5` > `58` > `582` > `582.32/.998` > `582.4` > `582.5/.9`
- PATH_LABELS: 数学．自然科学 ＞ 植物学 ＞ 植物分類学 ＞ 植物界(分類学) ＞ 種子植物 ＞ 被子植物類．顕花植物
- LEAF: false
- DIRECT_CHILDREN_COUNT: 2

### DIRECT_CHILDREN

- `subject::582.5` | CODE `582.5` | 単子葉類
- `subject::582.6/.9` | CODE `582.6/.9` | 双子葉類

<!-- END_FACET_NODE -->

## FACET_NODE `subject::582.5`

- FACET: `subject`
- NODE_KEY: `subject::582.5`
- CODE: `582.5`
- LABEL: 単子葉類
- PARENT_KEY: `subject::582.5/.9`
- PATH_CODES: `5` > `58` > `582` > `582.32/.998` > `582.4` > `582.5/.9` > `582.5`
- PATH_LABELS: 数学．自然科学 ＞ 植物学 ＞ 植物分類学 ＞ 植物界(分類学) ＞ 種子植物 ＞ 被子植物類．顕花植物 ＞ 単子葉類
- LEAF: false
- DIRECT_CHILDREN_COUNT: 5

### DIRECT_CHILDREN

- `subject::582.51` | CODE `582.51` | ヤシ類
- `subject::582.53` | CODE `582.53` | オモダカ目
- `subject::582.54/.56` | CODE `582.54/.56` | Commelinids
- `subject::582.57` | CODE `582.57` | ゆり目
- `subject::582.58` | CODE `582.58` | アスパラガス

<!-- END_FACET_NODE -->

## FACET_NODE `subject::582.51`

- FACET: `subject`
- NODE_KEY: `subject::582.51`
- CODE: `582.51`
- LABEL: ヤシ類
- PARENT_KEY: `subject::582.5`
- PATH_CODES: `5` > `58` > `582` > `582.32/.998` > `582.4` > `582.5/.9` > `582.5` > `582.51`
- PATH_LABELS: 数学．自然科学 ＞ 植物学 ＞ 植物分類学 ＞ 植物界(分類学) ＞ 種子植物 ＞ 被子植物類．顕花植物 ＞ 単子葉類 ＞ ヤシ類
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::582.53`

- FACET: `subject`
- NODE_KEY: `subject::582.53`
- CODE: `582.53`
- LABEL: オモダカ目
- PARENT_KEY: `subject::582.5`
- PATH_CODES: `5` > `58` > `582` > `582.32/.998` > `582.4` > `582.5/.9` > `582.5` > `582.53`
- PATH_LABELS: 数学．自然科学 ＞ 植物学 ＞ 植物分類学 ＞ 植物界(分類学) ＞ 種子植物 ＞ 被子植物類．顕花植物 ＞ 単子葉類 ＞ オモダカ目
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::582.54/.56`

- FACET: `subject`
- NODE_KEY: `subject::582.54/.56`
- CODE: `582.54/.56`
- LABEL: Commelinids
- PARENT_KEY: `subject::582.5`
- PATH_CODES: `5` > `58` > `582` > `582.32/.998` > `582.4` > `582.5/.9` > `582.5` > `582.54/.56`
- PATH_LABELS: 数学．自然科学 ＞ 植物学 ＞ 植物分類学 ＞ 植物界(分類学) ＞ 種子植物 ＞ 被子植物類．顕花植物 ＞ 単子葉類 ＞ Commelinids
- LEAF: false
- DIRECT_CHILDREN_COUNT: 2

### DIRECT_CHILDREN

- `subject::582.54` | CODE `582.54` | イネ目
- `subject::582.56` | CODE `582.56` | ショウガ目

<!-- END_FACET_NODE -->

## FACET_NODE `subject::582.54`

- FACET: `subject`
- NODE_KEY: `subject::582.54`
- CODE: `582.54`
- LABEL: イネ目
- PARENT_KEY: `subject::582.54/.56`
- PATH_CODES: `5` > `58` > `582` > `582.32/.998` > `582.4` > `582.5/.9` > `582.5` > `582.54/.56` > `582.54`
- PATH_LABELS: 数学．自然科学 ＞ 植物学 ＞ 植物分類学 ＞ 植物界(分類学) ＞ 種子植物 ＞ 被子植物類．顕花植物 ＞ 単子葉類 ＞ Commelinids ＞ イネ目
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::582.56`

- FACET: `subject`
- NODE_KEY: `subject::582.56`
- CODE: `582.56`
- LABEL: ショウガ目
- PARENT_KEY: `subject::582.54/.56`
- PATH_CODES: `5` > `58` > `582` > `582.32/.998` > `582.4` > `582.5/.9` > `582.5` > `582.54/.56` > `582.56`
- PATH_LABELS: 数学．自然科学 ＞ 植物学 ＞ 植物分類学 ＞ 植物界(分類学) ＞ 種子植物 ＞ 被子植物類．顕花植物 ＞ 単子葉類 ＞ Commelinids ＞ ショウガ目
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::582.57`

- FACET: `subject`
- NODE_KEY: `subject::582.57`
- CODE: `582.57`
- LABEL: ゆり目
- PARENT_KEY: `subject::582.5`
- PATH_CODES: `5` > `58` > `582` > `582.32/.998` > `582.4` > `582.5/.9` > `582.5` > `582.57`
- PATH_LABELS: 数学．自然科学 ＞ 植物学 ＞ 植物分類学 ＞ 植物界(分類学) ＞ 種子植物 ＞ 被子植物類．顕花植物 ＞ 単子葉類 ＞ ゆり目
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::582.58`

- FACET: `subject`
- NODE_KEY: `subject::582.58`
- CODE: `582.58`
- LABEL: アスパラガス
- PARENT_KEY: `subject::582.5`
- PATH_CODES: `5` > `58` > `582` > `582.32/.998` > `582.4` > `582.5/.9` > `582.5` > `582.58`
- PATH_LABELS: 数学．自然科学 ＞ 植物学 ＞ 植物分類学 ＞ 植物界(分類学) ＞ 種子植物 ＞ 被子植物類．顕花植物 ＞ 単子葉類 ＞ アスパラガス
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::582.6/.9`

- FACET: `subject`
- NODE_KEY: `subject::582.6/.9`
- CODE: `582.6/.9`
- LABEL: 双子葉類
- PARENT_KEY: `subject::582.5/.9`
- PATH_CODES: `5` > `58` > `582` > `582.32/.998` > `582.4` > `582.5/.9` > `582.6/.9`
- PATH_LABELS: 数学．自然科学 ＞ 植物学 ＞ 植物分類学 ＞ 植物界(分類学) ＞ 種子植物 ＞ 被子植物類．顕花植物 ＞ 双子葉類
- LEAF: false
- DIRECT_CHILDREN_COUNT: 1

### DIRECT_CHILDREN

- `subject::582.62` | CODE `582.62` | ブナ目

<!-- END_FACET_NODE -->

## FACET_NODE `subject::582.62`

- FACET: `subject`
- NODE_KEY: `subject::582.62`
- CODE: `582.62`
- LABEL: ブナ目
- PARENT_KEY: `subject::582.6/.9`
- PATH_CODES: `5` > `58` > `582` > `582.32/.998` > `582.4` > `582.5/.9` > `582.6/.9` > `582.62`
- PATH_LABELS: 数学．自然科学 ＞ 植物学 ＞ 植物分類学 ＞ 植物界(分類学) ＞ 種子植物 ＞ 被子植物類．顕花植物 ＞ 双子葉類 ＞ ブナ目
- LEAF: false
- DIRECT_CHILDREN_COUNT: 1

### DIRECT_CHILDREN

- `subject::582.622` | CODE `582.622` | カバノキ科

<!-- END_FACET_NODE -->

## FACET_NODE `subject::582.622`

- FACET: `subject`
- NODE_KEY: `subject::582.622`
- CODE: `582.622`
- LABEL: カバノキ科
- PARENT_KEY: `subject::582.62`
- PATH_CODES: `5` > `58` > `582` > `582.32/.998` > `582.4` > `582.5/.9` > `582.6/.9` > `582.62` > `582.622`
- PATH_LABELS: 数学．自然科学 ＞ 植物学 ＞ 植物分類学 ＞ 植物界(分類学) ＞ 種子植物 ＞ 被子植物類．顕花植物 ＞ 双子葉類 ＞ ブナ目 ＞ カバノキ科
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::59`

- FACET: `subject`
- NODE_KEY: `subject::59`
- CODE: `59`
- LABEL: 動物学
- PARENT_KEY: `subject::5`
- PATH_CODES: `5` > `59`
- PATH_LABELS: 数学．自然科学 ＞ 動物学
- LEAF: false
- DIRECT_CHILDREN_COUNT: 2

### DIRECT_CHILDREN

- `subject::591` | CODE `591` | 一般動物学
- `subject::592/599` | CODE `592/599` | 動物分類学

<!-- END_FACET_NODE -->

## FACET_NODE `subject::591`

- FACET: `subject`
- NODE_KEY: `subject::591`
- CODE: `591`
- LABEL: 一般動物学
- PARENT_KEY: `subject::59`
- PATH_CODES: `5` > `59` > `591`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 一般動物学
- LEAF: false
- DIRECT_CHILDREN_COUNT: 8

### DIRECT_CHILDREN

- `subject::591.1` | CODE `591.1` | 動物生理学
- `subject::591.2` | CODE `591.2` | 家畜以外の動物の病気．動物病理学
- `subject::591.3` | CODE `591.3` | 動物発生学．動物個体発生．個体の発生史
- `subject::591.4` | CODE `591.4` | 動物器官学．動物解剖学
- `subject::591.5` | CODE `591.5` | 動物習慣.生態学.動物行動学.動物と環境.生物機能学
- `subject::591.6` | CODE `591.6` | 動物経済学．応用動物学
- `subject::591.8` | CODE `591.8` | 動物組織学
- `subject::591.9` | CODE `591.9` | 動物地理学．動物相．動物の地理分布

<!-- END_FACET_NODE -->

## FACET_NODE `subject::591.1`

- FACET: `subject`
- NODE_KEY: `subject::591.1`
- CODE: `591.1`
- LABEL: 動物生理学
- PARENT_KEY: `subject::591`
- PATH_CODES: `5` > `59` > `591` > `591.1`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 一般動物学 ＞ 動物生理学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::591.2`

- FACET: `subject`
- NODE_KEY: `subject::591.2`
- CODE: `591.2`
- LABEL: 家畜以外の動物の病気．動物病理学
- PARENT_KEY: `subject::591`
- PATH_CODES: `5` > `59` > `591` > `591.2`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 一般動物学 ＞ 家畜以外の動物の病気．動物病理学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::591.3`

- FACET: `subject`
- NODE_KEY: `subject::591.3`
- CODE: `591.3`
- LABEL: 動物発生学．動物個体発生．個体の発生史
- PARENT_KEY: `subject::591`
- PATH_CODES: `5` > `59` > `591` > `591.3`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 一般動物学 ＞ 動物発生学．動物個体発生．個体の発生史
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::591.4`

- FACET: `subject`
- NODE_KEY: `subject::591.4`
- CODE: `591.4`
- LABEL: 動物器官学．動物解剖学
- PARENT_KEY: `subject::591`
- PATH_CODES: `5` > `59` > `591` > `591.4`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 一般動物学 ＞ 動物器官学．動物解剖学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::591.5`

- FACET: `subject`
- NODE_KEY: `subject::591.5`
- CODE: `591.5`
- LABEL: 動物習慣.生態学.動物行動学.動物と環境.生物機能学
- PARENT_KEY: `subject::591`
- PATH_CODES: `5` > `59` > `591` > `591.5`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 一般動物学 ＞ 動物習慣.生態学.動物行動学.動物と環境.生物機能学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::591.6`

- FACET: `subject`
- NODE_KEY: `subject::591.6`
- CODE: `591.6`
- LABEL: 動物経済学．応用動物学
- PARENT_KEY: `subject::591`
- PATH_CODES: `5` > `59` > `591` > `591.6`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 一般動物学 ＞ 動物経済学．応用動物学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::591.8`

- FACET: `subject`
- NODE_KEY: `subject::591.8`
- CODE: `591.8`
- LABEL: 動物組織学
- PARENT_KEY: `subject::591`
- PATH_CODES: `5` > `59` > `591` > `591.8`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 一般動物学 ＞ 動物組織学
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::591.9`

- FACET: `subject`
- NODE_KEY: `subject::591.9`
- CODE: `591.9`
- LABEL: 動物地理学．動物相．動物の地理分布
- PARENT_KEY: `subject::591`
- PATH_CODES: `5` > `59` > `591` > `591.9`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 一般動物学 ＞ 動物地理学．動物相．動物の地理分布
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::592/599`

- FACET: `subject`
- NODE_KEY: `subject::592/599`
- CODE: `592/599`
- LABEL: 動物分類学
- PARENT_KEY: `subject::59`
- PATH_CODES: `5` > `59` > `592/599`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学
- LEAF: false
- DIRECT_CHILDREN_COUNT: 6

### DIRECT_CHILDREN

- `subject::592` | CODE `592` | 無脊椎動物
- `subject::593.1` | CODE `593.1` | 原生動物
- `subject::593.4` | CODE `593.4` | 海綿動物
- `subject::594` | CODE `594` | 軟体動物
- `subject::595` | CODE `595` | 体節動物
- `subject::596/599` | CODE `596/599` | 脊策動物

<!-- END_FACET_NODE -->

## FACET_NODE `subject::592`

- FACET: `subject`
- NODE_KEY: `subject::592`
- CODE: `592`
- LABEL: 無脊椎動物
- PARENT_KEY: `subject::592/599`
- PATH_CODES: `5` > `59` > `592/599` > `592`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 無脊椎動物
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::593.1`

- FACET: `subject`
- NODE_KEY: `subject::593.1`
- CODE: `593.1`
- LABEL: 原生動物
- PARENT_KEY: `subject::592/599`
- PATH_CODES: `5` > `59` > `592/599` > `593.1`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 原生動物
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::593.4`

- FACET: `subject`
- NODE_KEY: `subject::593.4`
- CODE: `593.4`
- LABEL: 海綿動物
- PARENT_KEY: `subject::592/599`
- PATH_CODES: `5` > `59` > `592/599` > `593.4`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 海綿動物
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::594`

- FACET: `subject`
- NODE_KEY: `subject::594`
- CODE: `594`
- LABEL: 軟体動物
- PARENT_KEY: `subject::592/599`
- PATH_CODES: `5` > `59` > `592/599` > `594`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 軟体動物
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::595`

- FACET: `subject`
- NODE_KEY: `subject::595`
- CODE: `595`
- LABEL: 体節動物
- PARENT_KEY: `subject::592/599`
- PATH_CODES: `5` > `59` > `592/599` > `595`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 体節動物
- LEAF: false
- DIRECT_CHILDREN_COUNT: 1

### DIRECT_CHILDREN

- `subject::595.7` | CODE `595.7` | 昆虫類．六脚類

<!-- END_FACET_NODE -->

## FACET_NODE `subject::595.7`

- FACET: `subject`
- NODE_KEY: `subject::595.7`
- CODE: `595.7`
- LABEL: 昆虫類．六脚類
- PARENT_KEY: `subject::595`
- PATH_CODES: `5` > `59` > `592/599` > `595` > `595.7`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 体節動物 ＞ 昆虫類．六脚類
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::596/599`

- FACET: `subject`
- NODE_KEY: `subject::596/599`
- CODE: `596/599`
- LABEL: 脊策動物
- PARENT_KEY: `subject::592/599`
- PATH_CODES: `5` > `59` > `592/599` > `596/599`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物
- LEAF: false
- DIRECT_CHILDREN_COUNT: 2

### DIRECT_CHILDREN

- `subject::596.2` | CODE `596.2` | 被嚢動物
- `subject::597/599` | CODE `597/599` | 脊椎動物．脊椎動物亜門

<!-- END_FACET_NODE -->

## FACET_NODE `subject::596.2`

- FACET: `subject`
- NODE_KEY: `subject::596.2`
- CODE: `596.2`
- LABEL: 被嚢動物
- PARENT_KEY: `subject::596/599`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `596.2`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 被嚢動物
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::597/599`

- FACET: `subject`
- NODE_KEY: `subject::597/599`
- CODE: `597/599`
- LABEL: 脊椎動物．脊椎動物亜門
- PARENT_KEY: `subject::596/599`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門
- LEAF: false
- DIRECT_CHILDREN_COUNT: 4

### DIRECT_CHILDREN

- `subject::597.2/.5` | CODE `597.2/.5` | 魚類．魚(旧分類)
- `subject::597.6/.9` | CODE `597.6/.9` | 両生類
- `subject::598` | CODE `598` | トカゲ型類
- `subject::599` | CODE `599` | 哺乳綱．哺乳動物

<!-- END_FACET_NODE -->

## FACET_NODE `subject::597.2/.5`

- FACET: `subject`
- NODE_KEY: `subject::597.2/.5`
- CODE: `597.2/.5`
- LABEL: 魚類．魚(旧分類)
- PARENT_KEY: `subject::597/599`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `597.2/.5`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 魚類．魚(旧分類)
- LEAF: false
- DIRECT_CHILDREN_COUNT: 2

### DIRECT_CHILDREN

- `subject::597.3` | CODE `597.3` | 軟骨魚類
- `subject::597.4/.5` | CODE `597.4/.5` | 硬骨魚類(硬骨魚)

<!-- END_FACET_NODE -->

## FACET_NODE `subject::597.3`

- FACET: `subject`
- NODE_KEY: `subject::597.3`
- CODE: `597.3`
- LABEL: 軟骨魚類
- PARENT_KEY: `subject::597.2/.5`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `597.2/.5` > `597.3`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 魚類．魚(旧分類) ＞ 軟骨魚類
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::597.4/.5`

- FACET: `subject`
- NODE_KEY: `subject::597.4/.5`
- CODE: `597.4/.5`
- LABEL: 硬骨魚類(硬骨魚)
- PARENT_KEY: `subject::597.2/.5`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `597.2/.5` > `597.4/.5`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 魚類．魚(旧分類) ＞ 硬骨魚類(硬骨魚)
- LEAF: false
- DIRECT_CHILDREN_COUNT: 1

### DIRECT_CHILDREN

- `subject::597.42/.55` | CODE `597.42/.55` | 条鰭綱

<!-- END_FACET_NODE -->

## FACET_NODE `subject::597.42/.55`

- FACET: `subject`
- NODE_KEY: `subject::597.42/.55`
- CODE: `597.42/.55`
- LABEL: 条鰭綱
- PARENT_KEY: `subject::597.4/.5`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `597.2/.5` > `597.4/.5` > `597.42/.55`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 魚類．魚(旧分類) ＞ 硬骨魚類(硬骨魚) ＞ 条鰭綱
- LEAF: false
- DIRECT_CHILDREN_COUNT: 2

### DIRECT_CHILDREN

- `subject::597.42` | CODE `597.42` | 軟質亜綱
- `subject::597.5` | CODE `597.5` | 硬骨魚類

<!-- END_FACET_NODE -->

## FACET_NODE `subject::597.42`

- FACET: `subject`
- NODE_KEY: `subject::597.42`
- CODE: `597.42`
- LABEL: 軟質亜綱
- PARENT_KEY: `subject::597.42/.55`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `597.2/.5` > `597.4/.5` > `597.42/.55` > `597.42`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 魚類．魚(旧分類) ＞ 硬骨魚類(硬骨魚) ＞ 条鰭綱 ＞ 軟質亜綱
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::597.5`

- FACET: `subject`
- NODE_KEY: `subject::597.5`
- CODE: `597.5`
- LABEL: 硬骨魚類
- PARENT_KEY: `subject::597.42/.55`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `597.2/.5` > `597.4/.5` > `597.42/.55` > `597.5`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 魚類．魚(旧分類) ＞ 硬骨魚類(硬骨魚) ＞ 条鰭綱 ＞ 硬骨魚類
- LEAF: false
- DIRECT_CHILDREN_COUNT: 3

### DIRECT_CHILDREN

- `subject::597.535` | CODE `597.535` | ウナギ類
- `subject::597.541` | CODE `597.541` | ニシン類
- `subject::597.55` | CODE `597.55` | Euteleosti/Euteleostei

<!-- END_FACET_NODE -->

## FACET_NODE `subject::597.535`

- FACET: `subject`
- NODE_KEY: `subject::597.535`
- CODE: `597.535`
- LABEL: ウナギ類
- PARENT_KEY: `subject::597.5`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `597.2/.5` > `597.4/.5` > `597.42/.55` > `597.5` > `597.535`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 魚類．魚(旧分類) ＞ 硬骨魚類(硬骨魚) ＞ 条鰭綱 ＞ 硬骨魚類 ＞ ウナギ類
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::597.541`

- FACET: `subject`
- NODE_KEY: `subject::597.541`
- CODE: `597.541`
- LABEL: ニシン類
- PARENT_KEY: `subject::597.5`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `597.2/.5` > `597.4/.5` > `597.42/.55` > `597.5` > `597.541`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 魚類．魚(旧分類) ＞ 硬骨魚類(硬骨魚) ＞ 条鰭綱 ＞ 硬骨魚類 ＞ ニシン類
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::597.55`

- FACET: `subject`
- NODE_KEY: `subject::597.55`
- CODE: `597.55`
- LABEL: Euteleosti/Euteleostei
- PARENT_KEY: `subject::597.5`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `597.2/.5` > `597.4/.5` > `597.42/.55` > `597.5` > `597.55`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 魚類．魚(旧分類) ＞ 硬骨魚類(硬骨魚) ＞ 条鰭綱 ＞ 硬骨魚類 ＞ Euteleosti/Euteleostei
- LEAF: false
- DIRECT_CHILDREN_COUNT: 4

### DIRECT_CHILDREN

- `subject::597.551` | CODE `597.551` | 骨鰾上目
- `subject::597.552` | CODE `597.552` | 原棘鰭上目
- `subject::597.555` | CODE `597.555` | 側棘鰭上目
- `subject::597.556` | CODE `597.556` | 棘鰭上目

<!-- END_FACET_NODE -->

## FACET_NODE `subject::597.551`

- FACET: `subject`
- NODE_KEY: `subject::597.551`
- CODE: `597.551`
- LABEL: 骨鰾上目
- PARENT_KEY: `subject::597.55`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `597.2/.5` > `597.4/.5` > `597.42/.55` > `597.5` > `597.55` > `597.551`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 魚類．魚(旧分類) ＞ 硬骨魚類(硬骨魚) ＞ 条鰭綱 ＞ 硬骨魚類 ＞ Euteleosti/Euteleostei ＞ 骨鰾上目
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::597.552`

- FACET: `subject`
- NODE_KEY: `subject::597.552`
- CODE: `597.552`
- LABEL: 原棘鰭上目
- PARENT_KEY: `subject::597.55`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `597.2/.5` > `597.4/.5` > `597.42/.55` > `597.5` > `597.55` > `597.552`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 魚類．魚(旧分類) ＞ 硬骨魚類(硬骨魚) ＞ 条鰭綱 ＞ 硬骨魚類 ＞ Euteleosti/Euteleostei ＞ 原棘鰭上目
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::597.555`

- FACET: `subject`
- NODE_KEY: `subject::597.555`
- CODE: `597.555`
- LABEL: 側棘鰭上目
- PARENT_KEY: `subject::597.55`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `597.2/.5` > `597.4/.5` > `597.42/.55` > `597.5` > `597.55` > `597.555`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 魚類．魚(旧分類) ＞ 硬骨魚類(硬骨魚) ＞ 条鰭綱 ＞ 硬骨魚類 ＞ Euteleosti/Euteleostei ＞ 側棘鰭上目
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::597.556`

- FACET: `subject`
- NODE_KEY: `subject::597.556`
- CODE: `597.556`
- LABEL: 棘鰭上目
- PARENT_KEY: `subject::597.55`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `597.2/.5` > `597.4/.5` > `597.42/.55` > `597.5` > `597.55` > `597.556`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 魚類．魚(旧分類) ＞ 硬骨魚類(硬骨魚) ＞ 条鰭綱 ＞ 硬骨魚類 ＞ Euteleosti/Euteleostei ＞ 棘鰭上目
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::597.6/.9`

- FACET: `subject`
- NODE_KEY: `subject::597.6/.9`
- CODE: `597.6/.9`
- LABEL: 両生類
- PARENT_KEY: `subject::597/599`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `597.6/.9`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 両生類
- LEAF: false
- DIRECT_CHILDREN_COUNT: 3

### DIRECT_CHILDREN

- `subject::597.7` | CODE `597.7` | 裸ヘビ類(アシナミイモリ)
- `subject::597.8` | CODE `597.8` | カエル目(しっぽのない両生類)
- `subject::597.9` | CODE `597.9` | サンショウウオ(しっぽのある両生類)

<!-- END_FACET_NODE -->

## FACET_NODE `subject::597.7`

- FACET: `subject`
- NODE_KEY: `subject::597.7`
- CODE: `597.7`
- LABEL: 裸ヘビ類(アシナミイモリ)
- PARENT_KEY: `subject::597.6/.9`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `597.6/.9` > `597.7`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 両生類 ＞ 裸ヘビ類(アシナミイモリ)
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::597.8`

- FACET: `subject`
- NODE_KEY: `subject::597.8`
- CODE: `597.8`
- LABEL: カエル目(しっぽのない両生類)
- PARENT_KEY: `subject::597.6/.9`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `597.6/.9` > `597.8`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 両生類 ＞ カエル目(しっぽのない両生類)
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::597.9`

- FACET: `subject`
- NODE_KEY: `subject::597.9`
- CODE: `597.9`
- LABEL: サンショウウオ(しっぽのある両生類)
- PARENT_KEY: `subject::597.6/.9`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `597.6/.9` > `597.9`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 両生類 ＞ サンショウウオ(しっぽのある両生類)
- LEAF: false
- DIRECT_CHILDREN_COUNT: 2

### DIRECT_CHILDREN

- `subject::597.91` | CODE `597.91` | サイレン科
- `subject::597.94` | CODE `597.94` | イモリ科

<!-- END_FACET_NODE -->

## FACET_NODE `subject::597.91`

- FACET: `subject`
- NODE_KEY: `subject::597.91`
- CODE: `597.91`
- LABEL: サイレン科
- PARENT_KEY: `subject::597.9`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `597.6/.9` > `597.9` > `597.91`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 両生類 ＞ サンショウウオ(しっぽのある両生類) ＞ サイレン科
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::597.94`

- FACET: `subject`
- NODE_KEY: `subject::597.94`
- CODE: `597.94`
- LABEL: イモリ科
- PARENT_KEY: `subject::597.9`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `597.6/.9` > `597.9` > `597.94`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 両生類 ＞ サンショウウオ(しっぽのある両生類) ＞ イモリ科
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::598`

- FACET: `subject`
- NODE_KEY: `subject::598`
- CODE: `598`
- LABEL: トカゲ型類
- PARENT_KEY: `subject::597/599`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `598`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ トカゲ型類
- LEAF: false
- DIRECT_CHILDREN_COUNT: 2

### DIRECT_CHILDREN

- `subject::598.1/.2` | CODE `598.1/.2` | トカゲ型類
- `subject::598.2` | CODE `598.2` | 鳥類

<!-- END_FACET_NODE -->

## FACET_NODE `subject::598.1/.2`

- FACET: `subject`
- NODE_KEY: `subject::598.1/.2`
- CODE: `598.1/.2`
- LABEL: トカゲ型類
- PARENT_KEY: `subject::598`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `598` > `598.1/.2`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ トカゲ型類 ＞ トカゲ型類
- LEAF: false
- DIRECT_CHILDREN_COUNT: 1

### DIRECT_CHILDREN

- `subject::598.1` | CODE `598.1` | 爬虫類

<!-- END_FACET_NODE -->

## FACET_NODE `subject::598.1`

- FACET: `subject`
- NODE_KEY: `subject::598.1`
- CODE: `598.1`
- LABEL: 爬虫類
- PARENT_KEY: `subject::598.1/.2`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `598` > `598.1/.2` > `598.1`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ トカゲ型類 ＞ トカゲ型類 ＞ 爬虫類
- LEAF: false
- DIRECT_CHILDREN_COUNT: 4

### DIRECT_CHILDREN

- `subject::598.125` | CODE `598.125` | カメ科（カメ)
- `subject::598.16` | CODE `598.16` | 有麟類(爬虫類)
- `subject::598.18` | CODE `598.18` | クルロタシ類
- `subject::598.19` | CODE `598.19` | Avemetatarsalia(絶滅)

<!-- END_FACET_NODE -->

## FACET_NODE `subject::598.125`

- FACET: `subject`
- NODE_KEY: `subject::598.125`
- CODE: `598.125`
- LABEL: カメ科（カメ)
- PARENT_KEY: `subject::598.1`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `598` > `598.1/.2` > `598.1` > `598.125`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ トカゲ型類 ＞ トカゲ型類 ＞ 爬虫類 ＞ カメ科（カメ)
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::598.16`

- FACET: `subject`
- NODE_KEY: `subject::598.16`
- CODE: `598.16`
- LABEL: 有麟類(爬虫類)
- PARENT_KEY: `subject::598.1`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `598` > `598.1/.2` > `598.1` > `598.16`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ トカゲ型類 ＞ トカゲ型類 ＞ 爬虫類 ＞ 有麟類(爬虫類)
- LEAF: false
- DIRECT_CHILDREN_COUNT: 3

### DIRECT_CHILDREN

- `subject::598.161` | CODE `598.161` | トカゲ類(トカゲ)
- `subject::598.162` | CODE `598.162` | ヘビ／ヘビ類
- `subject::598.166` | CODE `598.166` | ミミズトカゲ亜目(ミミズトカゲ，虫トカゲ)

<!-- END_FACET_NODE -->

## FACET_NODE `subject::598.161`

- FACET: `subject`
- NODE_KEY: `subject::598.161`
- CODE: `598.161`
- LABEL: トカゲ類(トカゲ)
- PARENT_KEY: `subject::598.16`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `598` > `598.1/.2` > `598.1` > `598.16` > `598.161`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ トカゲ型類 ＞ トカゲ型類 ＞ 爬虫類 ＞ 有麟類(爬虫類) ＞ トカゲ類(トカゲ)
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::598.162`

- FACET: `subject`
- NODE_KEY: `subject::598.162`
- CODE: `598.162`
- LABEL: ヘビ／ヘビ類
- PARENT_KEY: `subject::598.16`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `598` > `598.1/.2` > `598.1` > `598.16` > `598.162`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ トカゲ型類 ＞ トカゲ型類 ＞ 爬虫類 ＞ 有麟類(爬虫類) ＞ ヘビ／ヘビ類
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::598.166`

- FACET: `subject`
- NODE_KEY: `subject::598.166`
- CODE: `598.166`
- LABEL: ミミズトカゲ亜目(ミミズトカゲ，虫トカゲ)
- PARENT_KEY: `subject::598.16`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `598` > `598.1/.2` > `598.1` > `598.16` > `598.166`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ トカゲ型類 ＞ トカゲ型類 ＞ 爬虫類 ＞ 有麟類(爬虫類) ＞ ミミズトカゲ亜目(ミミズトカゲ，虫トカゲ)
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::598.18`

- FACET: `subject`
- NODE_KEY: `subject::598.18`
- CODE: `598.18`
- LABEL: クルロタシ類
- PARENT_KEY: `subject::598.1`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `598` > `598.1/.2` > `598.1` > `598.18`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ トカゲ型類 ＞ トカゲ型類 ＞ 爬虫類 ＞ クルロタシ類
- LEAF: false
- DIRECT_CHILDREN_COUNT: 1

### DIRECT_CHILDREN

- `subject::598.182` | CODE `598.182` | クロコダイル亜科

<!-- END_FACET_NODE -->

## FACET_NODE `subject::598.182`

- FACET: `subject`
- NODE_KEY: `subject::598.182`
- CODE: `598.182`
- LABEL: クロコダイル亜科
- PARENT_KEY: `subject::598.18`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `598` > `598.1/.2` > `598.1` > `598.18` > `598.182`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ トカゲ型類 ＞ トカゲ型類 ＞ 爬虫類 ＞ クルロタシ類 ＞ クロコダイル亜科
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::598.19`

- FACET: `subject`
- NODE_KEY: `subject::598.19`
- CODE: `598.19`
- LABEL: Avemetatarsalia(絶滅)
- PARENT_KEY: `subject::598.1`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `598` > `598.1/.2` > `598.1` > `598.19`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ トカゲ型類 ＞ トカゲ型類 ＞ 爬虫類 ＞ Avemetatarsalia(絶滅)
- LEAF: false
- DIRECT_CHILDREN_COUNT: 2

### DIRECT_CHILDREN

- `subject::598.191` | CODE `598.191` | 翼竜類(絶滅)
- `subject::598.192` | CODE `598.192` | 恐竜類(恐竜)(絶滅)

<!-- END_FACET_NODE -->

## FACET_NODE `subject::598.191`

- FACET: `subject`
- NODE_KEY: `subject::598.191`
- CODE: `598.191`
- LABEL: 翼竜類(絶滅)
- PARENT_KEY: `subject::598.19`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `598` > `598.1/.2` > `598.1` > `598.19` > `598.191`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ トカゲ型類 ＞ トカゲ型類 ＞ 爬虫類 ＞ Avemetatarsalia(絶滅) ＞ 翼竜類(絶滅)
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::598.192`

- FACET: `subject`
- NODE_KEY: `subject::598.192`
- CODE: `598.192`
- LABEL: 恐竜類(恐竜)(絶滅)
- PARENT_KEY: `subject::598.19`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `598` > `598.1/.2` > `598.1` > `598.19` > `598.192`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ トカゲ型類 ＞ トカゲ型類 ＞ 爬虫類 ＞ Avemetatarsalia(絶滅) ＞ 恐竜類(恐竜)(絶滅)
- LEAF: false
- DIRECT_CHILDREN_COUNT: 3

### DIRECT_CHILDREN

- `subject::598.192.32` | CODE `598.192.32` | ティラノサウルス(絶滅)
- `subject::598.192.63` | CODE `598.192.63` | ディプロドクス科(絶滅)
- `subject::598.192.77` | CODE `598.192.77` | ケラドプス科(絶滅)

<!-- END_FACET_NODE -->

## FACET_NODE `subject::598.192.32`

- FACET: `subject`
- NODE_KEY: `subject::598.192.32`
- CODE: `598.192.32`
- LABEL: ティラノサウルス(絶滅)
- PARENT_KEY: `subject::598.192`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `598` > `598.1/.2` > `598.1` > `598.19` > `598.192` > `598.192.32`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ トカゲ型類 ＞ トカゲ型類 ＞ 爬虫類 ＞ Avemetatarsalia(絶滅) ＞ 恐竜類(恐竜)(絶滅) ＞ ティラノサウルス(絶滅)
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::598.192.63`

- FACET: `subject`
- NODE_KEY: `subject::598.192.63`
- CODE: `598.192.63`
- LABEL: ディプロドクス科(絶滅)
- PARENT_KEY: `subject::598.192`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `598` > `598.1/.2` > `598.1` > `598.19` > `598.192` > `598.192.63`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ トカゲ型類 ＞ トカゲ型類 ＞ 爬虫類 ＞ Avemetatarsalia(絶滅) ＞ 恐竜類(恐竜)(絶滅) ＞ ディプロドクス科(絶滅)
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::598.192.77`

- FACET: `subject`
- NODE_KEY: `subject::598.192.77`
- CODE: `598.192.77`
- LABEL: ケラドプス科(絶滅)
- PARENT_KEY: `subject::598.192`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `598` > `598.1/.2` > `598.1` > `598.19` > `598.192` > `598.192.77`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ トカゲ型類 ＞ トカゲ型類 ＞ 爬虫類 ＞ Avemetatarsalia(絶滅) ＞ 恐竜類(恐竜)(絶滅) ＞ ケラドプス科(絶滅)
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::598.2`

- FACET: `subject`
- NODE_KEY: `subject::598.2`
- CODE: `598.2`
- LABEL: 鳥類
- PARENT_KEY: `subject::598`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `598` > `598.2`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ トカゲ型類 ＞ 鳥類
- LEAF: false
- DIRECT_CHILDREN_COUNT: 25

### DIRECT_CHILDREN

- `subject::598.221` | CODE `598.221` | ダチョウ目(走鳥類)
- `subject::598.231` | CODE `598.231` | ペンギン目．ペンギン科
- `subject::598.233` | CODE `598.233` | カイツブリ目．ペンギン科
- `subject::598.234` | CODE `598.234` | ミズナギドリ類
- `subject::598.235` | CODE `598.235` | ペリカン類
- `subject::598.24` | CODE `598.24` | ツル類．チドリ目．コウノトリ類
- `subject::598.25` | CODE `598.25` | ガンカモ目
- `subject::598.26` | CODE `598.26` | キジ目.ハト科
- `subject::598.271` | CODE `598.271` | オウム，インコ目
- `subject::598.272` | CODE `598.272` | キツツキ類
- `subject::598.274` | CODE `598.274` | ホトトギス類.ツメバケイ
- `subject::598.279` | CODE `598.279` | ワシタカ．ワシタカ目．フクロウ目
- `subject::598.282` | CODE `598.282` | コトドリ．ムシクイ．ホウセキドリ．ミツスイ
- `subject::598.283` | CODE `598.283` | ヒバリ科
- `subject::598.284` | CODE `598.284` | ツバメ科
- `subject::598.285` | CODE `598.285` | セキレイ科
- `subject::598.286` | CODE `598.286` | ヒヨドリ科．エナガ科．ヨシキリ科
- `subject::598.287` | CODE `598.287` | 亜目スズメ科．カツオドリ
- `subject::598.288` | CODE `598.288` | カワガラス．コマドリ．マウシツグミ．イワヒバリ
- `subject::598.289` | CODE `598.289` | シジュウカラ，ゴジュウカラ，キバシリ，ハシリチルドリ
- `subject::598.291` | CODE `598.291` | Nectariniidae(タイヨウチョウ)
- `subject::598.292` | CODE `598.292` | コウライウグイス．モズ科(モズ)
- `subject::598.293` | CODE `598.293` | カラス科．フウチョウ科(極楽鳥)
- `subject::598.294` | CODE `598.294` | ムクドリ科．スズメ．ハタオリド科
- `subject::598.296` | CODE `598.296` | アトリ科．アメリカムシクイ

<!-- END_FACET_NODE -->

## FACET_NODE `subject::598.221`

- FACET: `subject`
- NODE_KEY: `subject::598.221`
- CODE: `598.221`
- LABEL: ダチョウ目(走鳥類)
- PARENT_KEY: `subject::598.2`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `598` > `598.2` > `598.221`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ トカゲ型類 ＞ 鳥類 ＞ ダチョウ目(走鳥類)
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::598.231`

- FACET: `subject`
- NODE_KEY: `subject::598.231`
- CODE: `598.231`
- LABEL: ペンギン目．ペンギン科
- PARENT_KEY: `subject::598.2`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `598` > `598.2` > `598.231`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ トカゲ型類 ＞ 鳥類 ＞ ペンギン目．ペンギン科
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::598.233`

- FACET: `subject`
- NODE_KEY: `subject::598.233`
- CODE: `598.233`
- LABEL: カイツブリ目．ペンギン科
- PARENT_KEY: `subject::598.2`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `598` > `598.2` > `598.233`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ トカゲ型類 ＞ 鳥類 ＞ カイツブリ目．ペンギン科
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::598.234`

- FACET: `subject`
- NODE_KEY: `subject::598.234`
- CODE: `598.234`
- LABEL: ミズナギドリ類
- PARENT_KEY: `subject::598.2`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `598` > `598.2` > `598.234`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ トカゲ型類 ＞ 鳥類 ＞ ミズナギドリ類
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::598.235`

- FACET: `subject`
- NODE_KEY: `subject::598.235`
- CODE: `598.235`
- LABEL: ペリカン類
- PARENT_KEY: `subject::598.2`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `598` > `598.2` > `598.235`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ トカゲ型類 ＞ 鳥類 ＞ ペリカン類
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::598.24`

- FACET: `subject`
- NODE_KEY: `subject::598.24`
- CODE: `598.24`
- LABEL: ツル類．チドリ目．コウノトリ類
- PARENT_KEY: `subject::598.2`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `598` > `598.2` > `598.24`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ トカゲ型類 ＞ 鳥類 ＞ ツル類．チドリ目．コウノトリ類
- LEAF: false
- DIRECT_CHILDREN_COUNT: 3

### DIRECT_CHILDREN

- `subject::598.241` | CODE `598.241` | ツル類
- `subject::598.243` | CODE `598.243` | チドリ目
- `subject::598.244` | CODE `598.244` | コウノトリ類

<!-- END_FACET_NODE -->

## FACET_NODE `subject::598.241`

- FACET: `subject`
- NODE_KEY: `subject::598.241`
- CODE: `598.241`
- LABEL: ツル類
- PARENT_KEY: `subject::598.24`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `598` > `598.2` > `598.24` > `598.241`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ トカゲ型類 ＞ 鳥類 ＞ ツル類．チドリ目．コウノトリ類 ＞ ツル類
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::598.243`

- FACET: `subject`
- NODE_KEY: `subject::598.243`
- CODE: `598.243`
- LABEL: チドリ目
- PARENT_KEY: `subject::598.24`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `598` > `598.2` > `598.24` > `598.243`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ トカゲ型類 ＞ 鳥類 ＞ ツル類．チドリ目．コウノトリ類 ＞ チドリ目
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::598.244`

- FACET: `subject`
- NODE_KEY: `subject::598.244`
- CODE: `598.244`
- LABEL: コウノトリ類
- PARENT_KEY: `subject::598.24`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `598` > `598.2` > `598.24` > `598.244`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ トカゲ型類 ＞ 鳥類 ＞ ツル類．チドリ目．コウノトリ類 ＞ コウノトリ類
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::598.25`

- FACET: `subject`
- NODE_KEY: `subject::598.25`
- CODE: `598.25`
- LABEL: ガンカモ目
- PARENT_KEY: `subject::598.2`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `598` > `598.2` > `598.25`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ トカゲ型類 ＞ 鳥類 ＞ ガンカモ目
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::598.26`

- FACET: `subject`
- NODE_KEY: `subject::598.26`
- CODE: `598.26`
- LABEL: キジ目.ハト科
- PARENT_KEY: `subject::598.2`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `598` > `598.2` > `598.26`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ トカゲ型類 ＞ 鳥類 ＞ キジ目.ハト科
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::598.271`

- FACET: `subject`
- NODE_KEY: `subject::598.271`
- CODE: `598.271`
- LABEL: オウム，インコ目
- PARENT_KEY: `subject::598.2`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `598` > `598.2` > `598.271`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ トカゲ型類 ＞ 鳥類 ＞ オウム，インコ目
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::598.272`

- FACET: `subject`
- NODE_KEY: `subject::598.272`
- CODE: `598.272`
- LABEL: キツツキ類
- PARENT_KEY: `subject::598.2`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `598` > `598.2` > `598.272`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ トカゲ型類 ＞ 鳥類 ＞ キツツキ類
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::598.274`

- FACET: `subject`
- NODE_KEY: `subject::598.274`
- CODE: `598.274`
- LABEL: ホトトギス類.ツメバケイ
- PARENT_KEY: `subject::598.2`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `598` > `598.2` > `598.274`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ トカゲ型類 ＞ 鳥類 ＞ ホトトギス類.ツメバケイ
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::598.279`

- FACET: `subject`
- NODE_KEY: `subject::598.279`
- CODE: `598.279`
- LABEL: ワシタカ．ワシタカ目．フクロウ目
- PARENT_KEY: `subject::598.2`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `598` > `598.2` > `598.279`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ トカゲ型類 ＞ 鳥類 ＞ ワシタカ．ワシタカ目．フクロウ目
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::598.282`

- FACET: `subject`
- NODE_KEY: `subject::598.282`
- CODE: `598.282`
- LABEL: コトドリ．ムシクイ．ホウセキドリ．ミツスイ
- PARENT_KEY: `subject::598.2`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `598` > `598.2` > `598.282`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ トカゲ型類 ＞ 鳥類 ＞ コトドリ．ムシクイ．ホウセキドリ．ミツスイ
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::598.283`

- FACET: `subject`
- NODE_KEY: `subject::598.283`
- CODE: `598.283`
- LABEL: ヒバリ科
- PARENT_KEY: `subject::598.2`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `598` > `598.2` > `598.283`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ トカゲ型類 ＞ 鳥類 ＞ ヒバリ科
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::598.284`

- FACET: `subject`
- NODE_KEY: `subject::598.284`
- CODE: `598.284`
- LABEL: ツバメ科
- PARENT_KEY: `subject::598.2`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `598` > `598.2` > `598.284`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ トカゲ型類 ＞ 鳥類 ＞ ツバメ科
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::598.285`

- FACET: `subject`
- NODE_KEY: `subject::598.285`
- CODE: `598.285`
- LABEL: セキレイ科
- PARENT_KEY: `subject::598.2`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `598` > `598.2` > `598.285`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ トカゲ型類 ＞ 鳥類 ＞ セキレイ科
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::598.286`

- FACET: `subject`
- NODE_KEY: `subject::598.286`
- CODE: `598.286`
- LABEL: ヒヨドリ科．エナガ科．ヨシキリ科
- PARENT_KEY: `subject::598.2`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `598` > `598.2` > `598.286`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ トカゲ型類 ＞ 鳥類 ＞ ヒヨドリ科．エナガ科．ヨシキリ科
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::598.287`

- FACET: `subject`
- NODE_KEY: `subject::598.287`
- CODE: `598.287`
- LABEL: 亜目スズメ科．カツオドリ
- PARENT_KEY: `subject::598.2`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `598` > `598.2` > `598.287`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ トカゲ型類 ＞ 鳥類 ＞ 亜目スズメ科．カツオドリ
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::598.288`

- FACET: `subject`
- NODE_KEY: `subject::598.288`
- CODE: `598.288`
- LABEL: カワガラス．コマドリ．マウシツグミ．イワヒバリ
- PARENT_KEY: `subject::598.2`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `598` > `598.2` > `598.288`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ トカゲ型類 ＞ 鳥類 ＞ カワガラス．コマドリ．マウシツグミ．イワヒバリ
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::598.289`

- FACET: `subject`
- NODE_KEY: `subject::598.289`
- CODE: `598.289`
- LABEL: シジュウカラ，ゴジュウカラ，キバシリ，ハシリチルドリ
- PARENT_KEY: `subject::598.2`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `598` > `598.2` > `598.289`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ トカゲ型類 ＞ 鳥類 ＞ シジュウカラ，ゴジュウカラ，キバシリ，ハシリチルドリ
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::598.291`

- FACET: `subject`
- NODE_KEY: `subject::598.291`
- CODE: `598.291`
- LABEL: Nectariniidae(タイヨウチョウ)
- PARENT_KEY: `subject::598.2`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `598` > `598.2` > `598.291`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ トカゲ型類 ＞ 鳥類 ＞ Nectariniidae(タイヨウチョウ)
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::598.292`

- FACET: `subject`
- NODE_KEY: `subject::598.292`
- CODE: `598.292`
- LABEL: コウライウグイス．モズ科(モズ)
- PARENT_KEY: `subject::598.2`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `598` > `598.2` > `598.292`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ トカゲ型類 ＞ 鳥類 ＞ コウライウグイス．モズ科(モズ)
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::598.293`

- FACET: `subject`
- NODE_KEY: `subject::598.293`
- CODE: `598.293`
- LABEL: カラス科．フウチョウ科(極楽鳥)
- PARENT_KEY: `subject::598.2`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `598` > `598.2` > `598.293`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ トカゲ型類 ＞ 鳥類 ＞ カラス科．フウチョウ科(極楽鳥)
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::598.294`

- FACET: `subject`
- NODE_KEY: `subject::598.294`
- CODE: `598.294`
- LABEL: ムクドリ科．スズメ．ハタオリド科
- PARENT_KEY: `subject::598.2`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `598` > `598.2` > `598.294`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ トカゲ型類 ＞ 鳥類 ＞ ムクドリ科．スズメ．ハタオリド科
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::598.296`

- FACET: `subject`
- NODE_KEY: `subject::598.296`
- CODE: `598.296`
- LABEL: アトリ科．アメリカムシクイ
- PARENT_KEY: `subject::598.2`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `598` > `598.2` > `598.296`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ トカゲ型類 ＞ 鳥類 ＞ アトリ科．アメリカムシクイ
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::599`

- FACET: `subject`
- NODE_KEY: `subject::599`
- CODE: `599`
- LABEL: 哺乳綱．哺乳動物
- PARENT_KEY: `subject::597/599`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `599`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 哺乳綱．哺乳動物
- LEAF: false
- DIRECT_CHILDREN_COUNT: 3

### DIRECT_CHILDREN

- `subject::599.1` | CODE `599.1` | 無胎盤類一般
- `subject::599.2` | CODE `599.2` | 有袋類(袋に入れられた哺乳動物)
- `subject::599.3/.8` | CODE `599.3/.8` | 有胎盤哺乳類

<!-- END_FACET_NODE -->

## FACET_NODE `subject::599.1`

- FACET: `subject`
- NODE_KEY: `subject::599.1`
- CODE: `599.1`
- LABEL: 無胎盤類一般
- PARENT_KEY: `subject::599`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `599` > `599.1`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 哺乳綱．哺乳動物 ＞ 無胎盤類一般
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::599.2`

- FACET: `subject`
- NODE_KEY: `subject::599.2`
- CODE: `599.2`
- LABEL: 有袋類(袋に入れられた哺乳動物)
- PARENT_KEY: `subject::599`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `599` > `599.2`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 哺乳綱．哺乳動物 ＞ 有袋類(袋に入れられた哺乳動物)
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::599.3/.8`

- FACET: `subject`
- NODE_KEY: `subject::599.3/.8`
- CODE: `599.3/.8`
- LABEL: 有胎盤哺乳類
- PARENT_KEY: `subject::599`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `599` > `599.3/.8`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 哺乳綱．哺乳動物 ＞ 有胎盤哺乳類
- LEAF: false
- DIRECT_CHILDREN_COUNT: 10

### DIRECT_CHILDREN

- `subject::599.31` | CODE `599.31` | 貧歯類
- `subject::599.32` | CODE `599.32` | げっ歯類．げっ歯動物
- `subject::599.35/.38` | CODE `599.35/.38` | 食虫類(食虫哺乳類)
- `subject::599.39` | CODE `599.39` | 皮翼類
- `subject::599.4` | CODE `599.4` | 翼手類．コウモリ
- `subject::599.5` | CODE `599.5` | 鯨類. 海牛類
- `subject::599.61/.73` | CODE `599.61/.73` | 有蹄類:有蹄の哺乳動物
- `subject::599.74` | CODE `599.74` | 食肉類．食肉の哺乳類
- `subject::599.78` | CODE `599.78` | ツパイ目（ツパイ）
- `subject::599.8` | CODE `599.8` | 霊長類

<!-- END_FACET_NODE -->

## FACET_NODE `subject::599.31`

- FACET: `subject`
- NODE_KEY: `subject::599.31`
- CODE: `599.31`
- LABEL: 貧歯類
- PARENT_KEY: `subject::599.3/.8`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `599` > `599.3/.8` > `599.31`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 哺乳綱．哺乳動物 ＞ 有胎盤哺乳類 ＞ 貧歯類
- LEAF: false
- DIRECT_CHILDREN_COUNT: 2

### DIRECT_CHILDREN

- `subject::599.311` | CODE `599.311` | 有麟類．セイザンコウ
- `subject::599.312` | CODE `599.312` | アリクイ目／魚歯目

<!-- END_FACET_NODE -->

## FACET_NODE `subject::599.311`

- FACET: `subject`
- NODE_KEY: `subject::599.311`
- CODE: `599.311`
- LABEL: 有麟類．セイザンコウ
- PARENT_KEY: `subject::599.31`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `599` > `599.3/.8` > `599.31` > `599.311`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 哺乳綱．哺乳動物 ＞ 有胎盤哺乳類 ＞ 貧歯類 ＞ 有麟類．セイザンコウ
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::599.312`

- FACET: `subject`
- NODE_KEY: `subject::599.312`
- CODE: `599.312`
- LABEL: アリクイ目／魚歯目
- PARENT_KEY: `subject::599.31`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `599` > `599.3/.8` > `599.31` > `599.312`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 哺乳綱．哺乳動物 ＞ 有胎盤哺乳類 ＞ 貧歯類 ＞ アリクイ目／魚歯目
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::599.32`

- FACET: `subject`
- NODE_KEY: `subject::599.32`
- CODE: `599.32`
- LABEL: げっ歯類．げっ歯動物
- PARENT_KEY: `subject::599.3/.8`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `599` > `599.3/.8` > `599.32`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 哺乳綱．哺乳動物 ＞ 有胎盤哺乳類 ＞ げっ歯類．げっ歯動物
- LEAF: false
- DIRECT_CHILDREN_COUNT: 3

### DIRECT_CHILDREN

- `subject::599.322` | CODE `599.322` | リス類．ビーバー類．ウロコウリス科
- `subject::599.324` | CODE `599.324` | ヤマアラシ亜目
- `subject::599.325` | CODE `599.325` | ウサギ目(ウサギ類)

<!-- END_FACET_NODE -->

## FACET_NODE `subject::599.322`

- FACET: `subject`
- NODE_KEY: `subject::599.322`
- CODE: `599.322`
- LABEL: リス類．ビーバー類．ウロコウリス科
- PARENT_KEY: `subject::599.32`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `599` > `599.3/.8` > `599.32` > `599.322`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 哺乳綱．哺乳動物 ＞ 有胎盤哺乳類 ＞ げっ歯類．げっ歯動物 ＞ リス類．ビーバー類．ウロコウリス科
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::599.324`

- FACET: `subject`
- NODE_KEY: `subject::599.324`
- CODE: `599.324`
- LABEL: ヤマアラシ亜目
- PARENT_KEY: `subject::599.32`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `599` > `599.3/.8` > `599.32` > `599.324`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 哺乳綱．哺乳動物 ＞ 有胎盤哺乳類 ＞ げっ歯類．げっ歯動物 ＞ ヤマアラシ亜目
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::599.325`

- FACET: `subject`
- NODE_KEY: `subject::599.325`
- CODE: `599.325`
- LABEL: ウサギ目(ウサギ類)
- PARENT_KEY: `subject::599.32`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `599` > `599.3/.8` > `599.32` > `599.325`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 哺乳綱．哺乳動物 ＞ 有胎盤哺乳類 ＞ げっ歯類．げっ歯動物 ＞ ウサギ目(ウサギ類)
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::599.35/.38`

- FACET: `subject`
- NODE_KEY: `subject::599.35/.38`
- CODE: `599.35/.38`
- LABEL: 食虫類(食虫哺乳類)
- PARENT_KEY: `subject::599.3/.8`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `599` > `599.3/.8` > `599.35/.38`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 哺乳綱．哺乳動物 ＞ 有胎盤哺乳類 ＞ 食虫類(食虫哺乳類)
- LEAF: false
- DIRECT_CHILDREN_COUNT: 1

### DIRECT_CHILDREN

- `subject::599.36` | CODE `599.36` | トガリネズミ目．ハリオネズミ目

<!-- END_FACET_NODE -->

## FACET_NODE `subject::599.36`

- FACET: `subject`
- NODE_KEY: `subject::599.36`
- CODE: `599.36`
- LABEL: トガリネズミ目．ハリオネズミ目
- PARENT_KEY: `subject::599.35/.38`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `599` > `599.3/.8` > `599.35/.38` > `599.36`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 哺乳綱．哺乳動物 ＞ 有胎盤哺乳類 ＞ 食虫類(食虫哺乳類) ＞ トガリネズミ目．ハリオネズミ目
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::599.39`

- FACET: `subject`
- NODE_KEY: `subject::599.39`
- CODE: `599.39`
- LABEL: 皮翼類
- PARENT_KEY: `subject::599.3/.8`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `599` > `599.3/.8` > `599.39`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 哺乳綱．哺乳動物 ＞ 有胎盤哺乳類 ＞ 皮翼類
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::599.4`

- FACET: `subject`
- NODE_KEY: `subject::599.4`
- CODE: `599.4`
- LABEL: 翼手類．コウモリ
- PARENT_KEY: `subject::599.3/.8`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `599` > `599.3/.8` > `599.4`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 哺乳綱．哺乳動物 ＞ 有胎盤哺乳類 ＞ 翼手類．コウモリ
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::599.5`

- FACET: `subject`
- NODE_KEY: `subject::599.5`
- CODE: `599.5`
- LABEL: 鯨類. 海牛類
- PARENT_KEY: `subject::599.3/.8`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `599` > `599.3/.8` > `599.5`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 哺乳綱．哺乳動物 ＞ 有胎盤哺乳類 ＞ 鯨類. 海牛類
- LEAF: false
- DIRECT_CHILDREN_COUNT: 3

### DIRECT_CHILDREN

- `subject::599.51` | CODE `599.51` | ヒゲ鯨類
- `subject::599.53` | CODE `599.53` | 歯鯨類(歯鯨)
- `subject::599.55` | CODE `599.55` | 海牛目(海牛目／ジュゴン)

<!-- END_FACET_NODE -->

## FACET_NODE `subject::599.51`

- FACET: `subject`
- NODE_KEY: `subject::599.51`
- CODE: `599.51`
- LABEL: ヒゲ鯨類
- PARENT_KEY: `subject::599.5`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `599` > `599.3/.8` > `599.5` > `599.51`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 哺乳綱．哺乳動物 ＞ 有胎盤哺乳類 ＞ 鯨類. 海牛類 ＞ ヒゲ鯨類
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::599.53`

- FACET: `subject`
- NODE_KEY: `subject::599.53`
- CODE: `599.53`
- LABEL: 歯鯨類(歯鯨)
- PARENT_KEY: `subject::599.5`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `599` > `599.3/.8` > `599.5` > `599.53`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 哺乳綱．哺乳動物 ＞ 有胎盤哺乳類 ＞ 鯨類. 海牛類 ＞ 歯鯨類(歯鯨)
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::599.55`

- FACET: `subject`
- NODE_KEY: `subject::599.55`
- CODE: `599.55`
- LABEL: 海牛目(海牛目／ジュゴン)
- PARENT_KEY: `subject::599.5`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `599` > `599.3/.8` > `599.5` > `599.55`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 哺乳綱．哺乳動物 ＞ 有胎盤哺乳類 ＞ 鯨類. 海牛類 ＞ 海牛目(海牛目／ジュゴン)
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::599.61/.73`

- FACET: `subject`
- NODE_KEY: `subject::599.61/.73`
- CODE: `599.61/.73`
- LABEL: 有蹄類:有蹄の哺乳動物
- PARENT_KEY: `subject::599.3/.8`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `599` > `599.3/.8` > `599.61/.73`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 哺乳綱．哺乳動物 ＞ 有胎盤哺乳類 ＞ 有蹄類:有蹄の哺乳動物
- LEAF: false
- DIRECT_CHILDREN_COUNT: 5

### DIRECT_CHILDREN

- `subject::599.61` | CODE `599.61` | 長鼻類．象．マンモス(絶滅)
- `subject::599.62` | CODE `599.62` | ヒズメウサギ類．イワダヌキ類
- `subject::599.68` | CODE `599.68` | Tubulidentata．Orycteropodidae．ツチブタ
- `subject::599.72` | CODE `599.72` | Perissodactyla．奇蹄類
- `subject::599.73` | CODE `599.73` | Artiodactyla(偶蹄類)

<!-- END_FACET_NODE -->

## FACET_NODE `subject::599.61`

- FACET: `subject`
- NODE_KEY: `subject::599.61`
- CODE: `599.61`
- LABEL: 長鼻類．象．マンモス(絶滅)
- PARENT_KEY: `subject::599.61/.73`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `599` > `599.3/.8` > `599.61/.73` > `599.61`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 哺乳綱．哺乳動物 ＞ 有胎盤哺乳類 ＞ 有蹄類:有蹄の哺乳動物 ＞ 長鼻類．象．マンモス(絶滅)
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::599.62`

- FACET: `subject`
- NODE_KEY: `subject::599.62`
- CODE: `599.62`
- LABEL: ヒズメウサギ類．イワダヌキ類
- PARENT_KEY: `subject::599.61/.73`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `599` > `599.3/.8` > `599.61/.73` > `599.62`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 哺乳綱．哺乳動物 ＞ 有胎盤哺乳類 ＞ 有蹄類:有蹄の哺乳動物 ＞ ヒズメウサギ類．イワダヌキ類
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::599.68`

- FACET: `subject`
- NODE_KEY: `subject::599.68`
- CODE: `599.68`
- LABEL: Tubulidentata．Orycteropodidae．ツチブタ
- PARENT_KEY: `subject::599.61/.73`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `599` > `599.3/.8` > `599.61/.73` > `599.68`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 哺乳綱．哺乳動物 ＞ 有胎盤哺乳類 ＞ 有蹄類:有蹄の哺乳動物 ＞ Tubulidentata．Orycteropodidae．ツチブタ
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::599.72`

- FACET: `subject`
- NODE_KEY: `subject::599.72`
- CODE: `599.72`
- LABEL: Perissodactyla．奇蹄類
- PARENT_KEY: `subject::599.61/.73`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `599` > `599.3/.8` > `599.61/.73` > `599.72`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 哺乳綱．哺乳動物 ＞ 有胎盤哺乳類 ＞ 有蹄類:有蹄の哺乳動物 ＞ Perissodactyla．奇蹄類
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::599.73`

- FACET: `subject`
- NODE_KEY: `subject::599.73`
- CODE: `599.73`
- LABEL: Artiodactyla(偶蹄類)
- PARENT_KEY: `subject::599.61/.73`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `599` > `599.3/.8` > `599.61/.73` > `599.73`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 哺乳綱．哺乳動物 ＞ 有胎盤哺乳類 ＞ 有蹄類:有蹄の哺乳動物 ＞ Artiodactyla(偶蹄類)
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::599.74`

- FACET: `subject`
- NODE_KEY: `subject::599.74`
- CODE: `599.74`
- LABEL: 食肉類．食肉の哺乳類
- PARENT_KEY: `subject::599.3/.8`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `599` > `599.3/.8` > `599.74`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 哺乳綱．哺乳動物 ＞ 有胎盤哺乳類 ＞ 食肉類．食肉の哺乳類
- LEAF: false
- DIRECT_CHILDREN_COUNT: 6

### DIRECT_CHILDREN

- `subject::599.742.5` | CODE `599.742.5` | ジャコウネコ科
- `subject::599.742.6` | CODE `599.742.6` | ハイエナ科
- `subject::599.742.7` | CODE `599.742.7` | ネコ科
- `subject::599.743` | CODE `599.743` | マングース科．マダカスカルマングース科
- `subject::599.744` | CODE `599.744` | イヌ科．クマ科．イタチ科
- `subject::599.745` | CODE `599.745` | アシカ亜目

<!-- END_FACET_NODE -->

## FACET_NODE `subject::599.742.5`

- FACET: `subject`
- NODE_KEY: `subject::599.742.5`
- CODE: `599.742.5`
- LABEL: ジャコウネコ科
- PARENT_KEY: `subject::599.74`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `599` > `599.3/.8` > `599.74` > `599.742.5`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 哺乳綱．哺乳動物 ＞ 有胎盤哺乳類 ＞ 食肉類．食肉の哺乳類 ＞ ジャコウネコ科
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::599.742.6`

- FACET: `subject`
- NODE_KEY: `subject::599.742.6`
- CODE: `599.742.6`
- LABEL: ハイエナ科
- PARENT_KEY: `subject::599.74`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `599` > `599.3/.8` > `599.74` > `599.742.6`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 哺乳綱．哺乳動物 ＞ 有胎盤哺乳類 ＞ 食肉類．食肉の哺乳類 ＞ ハイエナ科
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::599.742.7`

- FACET: `subject`
- NODE_KEY: `subject::599.742.7`
- CODE: `599.742.7`
- LABEL: ネコ科
- PARENT_KEY: `subject::599.74`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `599` > `599.3/.8` > `599.74` > `599.742.7`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 哺乳綱．哺乳動物 ＞ 有胎盤哺乳類 ＞ 食肉類．食肉の哺乳類 ＞ ネコ科
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::599.743`

- FACET: `subject`
- NODE_KEY: `subject::599.743`
- CODE: `599.743`
- LABEL: マングース科．マダカスカルマングース科
- PARENT_KEY: `subject::599.74`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `599` > `599.3/.8` > `599.74` > `599.743`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 哺乳綱．哺乳動物 ＞ 有胎盤哺乳類 ＞ 食肉類．食肉の哺乳類 ＞ マングース科．マダカスカルマングース科
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::599.744`

- FACET: `subject`
- NODE_KEY: `subject::599.744`
- CODE: `599.744`
- LABEL: イヌ科．クマ科．イタチ科
- PARENT_KEY: `subject::599.74`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `599` > `599.3/.8` > `599.74` > `599.744`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 哺乳綱．哺乳動物 ＞ 有胎盤哺乳類 ＞ 食肉類．食肉の哺乳類 ＞ イヌ科．クマ科．イタチ科
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::599.745`

- FACET: `subject`
- NODE_KEY: `subject::599.745`
- CODE: `599.745`
- LABEL: アシカ亜目
- PARENT_KEY: `subject::599.74`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `599` > `599.3/.8` > `599.74` > `599.745`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 哺乳綱．哺乳動物 ＞ 有胎盤哺乳類 ＞ 食肉類．食肉の哺乳類 ＞ アシカ亜目
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::599.78`

- FACET: `subject`
- NODE_KEY: `subject::599.78`
- CODE: `599.78`
- LABEL: ツパイ目（ツパイ）
- PARENT_KEY: `subject::599.3/.8`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `599` > `599.3/.8` > `599.78`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 哺乳綱．哺乳動物 ＞ 有胎盤哺乳類 ＞ ツパイ目（ツパイ）
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::599.8`

- FACET: `subject`
- NODE_KEY: `subject::599.8`
- CODE: `599.8`
- LABEL: 霊長類
- PARENT_KEY: `subject::599.3/.8`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `599` > `599.3/.8` > `599.8`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 哺乳綱．哺乳動物 ＞ 有胎盤哺乳類 ＞ 霊長類
- LEAF: false
- DIRECT_CHILDREN_COUNT: 2

### DIRECT_CHILDREN

- `subject::599.81` | CODE `599.81` | 原猿亜目．原猿類
- `subject::599.82/.89` | CODE `599.82/.89` | 真猿亜目(サル)

<!-- END_FACET_NODE -->

## FACET_NODE `subject::599.81`

- FACET: `subject`
- NODE_KEY: `subject::599.81`
- CODE: `599.81`
- LABEL: 原猿亜目．原猿類
- PARENT_KEY: `subject::599.8`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `599` > `599.3/.8` > `599.8` > `599.81`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 哺乳綱．哺乳動物 ＞ 有胎盤哺乳類 ＞ 霊長類 ＞ 原猿亜目．原猿類
- LEAF: false
- DIRECT_CHILDREN_COUNT: 3

### DIRECT_CHILDREN

- `subject::599.813` | CODE `599.813` | ロリス科
- `subject::599.815` | CODE `599.815` | キツネザル科
- `subject::599.818` | CODE `599.818` | メガネザル下目．メガネザル

<!-- END_FACET_NODE -->

## FACET_NODE `subject::599.813`

- FACET: `subject`
- NODE_KEY: `subject::599.813`
- CODE: `599.813`
- LABEL: ロリス科
- PARENT_KEY: `subject::599.81`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `599` > `599.3/.8` > `599.8` > `599.81` > `599.813`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 哺乳綱．哺乳動物 ＞ 有胎盤哺乳類 ＞ 霊長類 ＞ 原猿亜目．原猿類 ＞ ロリス科
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::599.815`

- FACET: `subject`
- NODE_KEY: `subject::599.815`
- CODE: `599.815`
- LABEL: キツネザル科
- PARENT_KEY: `subject::599.81`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `599` > `599.3/.8` > `599.8` > `599.81` > `599.815`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 哺乳綱．哺乳動物 ＞ 有胎盤哺乳類 ＞ 霊長類 ＞ 原猿亜目．原猿類 ＞ キツネザル科
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::599.818`

- FACET: `subject`
- NODE_KEY: `subject::599.818`
- CODE: `599.818`
- LABEL: メガネザル下目．メガネザル
- PARENT_KEY: `subject::599.81`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `599` > `599.3/.8` > `599.8` > `599.81` > `599.818`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 哺乳綱．哺乳動物 ＞ 有胎盤哺乳類 ＞ 霊長類 ＞ 原猿亜目．原猿類 ＞ メガネザル下目．メガネザル
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::599.82/.89`

- FACET: `subject`
- NODE_KEY: `subject::599.82/.89`
- CODE: `599.82/.89`
- LABEL: 真猿亜目(サル)
- PARENT_KEY: `subject::599.8`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `599` > `599.3/.8` > `599.8` > `599.82/.89`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 哺乳綱．哺乳動物 ＞ 有胎盤哺乳類 ＞ 霊長類 ＞ 真猿亜目(サル)
- LEAF: false
- DIRECT_CHILDREN_COUNT: 3

### DIRECT_CHILDREN

- `subject::599.82` | CODE `599.82` | 真猿類
- `subject::599.85` | CODE `599.85` | オナガザル上科.オナガザル科
- `subject::599.88/.89` | CODE `599.88/.89` | ヒト類

<!-- END_FACET_NODE -->

## FACET_NODE `subject::599.82`

- FACET: `subject`
- NODE_KEY: `subject::599.82`
- CODE: `599.82`
- LABEL: 真猿類
- PARENT_KEY: `subject::599.82/.89`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `599` > `599.3/.8` > `599.8` > `599.82/.89` > `599.82`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 哺乳綱．哺乳動物 ＞ 有胎盤哺乳類 ＞ 霊長類 ＞ 真猿亜目(サル) ＞ 真猿類
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::599.85`

- FACET: `subject`
- NODE_KEY: `subject::599.85`
- CODE: `599.85`
- LABEL: オナガザル上科.オナガザル科
- PARENT_KEY: `subject::599.82/.89`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `599` > `599.3/.8` > `599.8` > `599.82/.89` > `599.85`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 哺乳綱．哺乳動物 ＞ 有胎盤哺乳類 ＞ 霊長類 ＞ 真猿亜目(サル) ＞ オナガザル上科.オナガザル科
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::599.88/.89`

- FACET: `subject`
- NODE_KEY: `subject::599.88/.89`
- CODE: `599.88/.89`
- LABEL: ヒト類
- PARENT_KEY: `subject::599.82/.89`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `599` > `599.3/.8` > `599.8` > `599.82/.89` > `599.88/.89`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 哺乳綱．哺乳動物 ＞ 有胎盤哺乳類 ＞ 霊長類 ＞ 真猿亜目(サル) ＞ ヒト類
- LEAF: false
- DIRECT_CHILDREN_COUNT: 2

### DIRECT_CHILDREN

- `subject::599.88` | CODE `599.88` | テナガザル(類人猿)
- `subject::599.89` | CODE `599.89` | ヒト科（ヒト科の動物/大型類人猿)

<!-- END_FACET_NODE -->

## FACET_NODE `subject::599.88`

- FACET: `subject`
- NODE_KEY: `subject::599.88`
- CODE: `599.88`
- LABEL: テナガザル(類人猿)
- PARENT_KEY: `subject::599.88/.89`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `599` > `599.3/.8` > `599.8` > `599.82/.89` > `599.88/.89` > `599.88`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 哺乳綱．哺乳動物 ＞ 有胎盤哺乳類 ＞ 霊長類 ＞ 真猿亜目(サル) ＞ ヒト類 ＞ テナガザル(類人猿)
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `subject::599.89`

- FACET: `subject`
- NODE_KEY: `subject::599.89`
- CODE: `599.89`
- LABEL: ヒト科（ヒト科の動物/大型類人猿)
- PARENT_KEY: `subject::599.88/.89`
- PATH_CODES: `5` > `59` > `592/599` > `596/599` > `597/599` > `599` > `599.3/.8` > `599.8` > `599.82/.89` > `599.88/.89` > `599.89`
- PATH_LABELS: 数学．自然科学 ＞ 動物学 ＞ 動物分類学 ＞ 脊策動物 ＞ 脊椎動物．脊椎動物亜門 ＞ 哺乳綱．哺乳動物 ＞ 有胎盤哺乳類 ＞ 霊長類 ＞ 真猿亜目(サル) ＞ ヒト類 ＞ ヒト科（ヒト科の動物/大型類人猿)
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->
