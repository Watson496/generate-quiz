# place ファセットカタログ — 全階層

各 `FACET_NODE` ブロックは一つの親ノードと、その直接の子を自己完結的に収録しています。
細分化する場合は、検索で得た親ブロックの `DIRECT_CHILDREN` を全件比較してください。
ラベル・コード・注記は元データ由来です。独自ノードを追加しないでください。

## FACET_NODE `place::(1/9)`

- FACET: `place`
- NODE_KEY: `place::(1/9)`
- CODE: `(1/9)`
- LABEL: 場所の共通補助番号．表1e
- PARENT_KEY: `place::ROOT`
- PATH_CODES: `(1/9)`
- PATH_LABELS: 場所の共通補助番号．表1e
- LEAF: false
- DIRECT_CHILDREN_COUNT: 3

### DIRECT_CHILDREN

- `place::(1)` | CODE `(1)` | 場所と空間一般．配置．位置づけ
- `place::(2)` | CODE `(2)` | 自然地理学的名称
- `place::(3/9)` | CODE `(3/9)` | 古代および現代世界の個々の場所

### USAGE_NOTE

(1/9)の補助番号は,場所の側面が主題に対して第二義的であれば,主番号全体を通じて使用できる．通常は主番号あるいは主題記号の後に置くが，必要に応じて番号の順序を逆にして，同一の場所に関するすべての資料をまとめても良い．例　339.5(73)外国貿易－アメリカ合衆国，(73)339.5 アメリカ合衆国－外国貿易．例外として，場所の観点以外によって探索されることがないと思われる資料（ある種の地図のように）については，場所の補助表のみを用いて分類するのが適当であろう．UDC要約版では,地理・政治的区分(4/9)には国レベル以下の下位区分がないが，固有補助番号(1-2/-4)とアルファベット拡張(表1h)の少なくとも一方を用いることで，より小さな単位を表すことができる．

### SCOPE_NOTE

場所の補助番号は，主番号で示されている主題の地理的な範囲，地域またはその他の空間的な側面を示す．例えば，331.2(44)フランスの賃金，338.47(81)ブラジルの交通経済学．場所の補助番号の最も重要な用法は,913「地域の地理」,94「歴史」において下位区分のための主要ファセットとして用いることである．

<!-- END_FACET_NODE -->

## FACET_NODE `place::(1)`

- FACET: `place`
- NODE_KEY: `place::(1)`
- CODE: `(1)`
- LABEL: 場所と空間一般．配置．位置づけ
- PARENT_KEY: `place::(1/9)`
- PATH_CODES: `(1/9)` > `(1)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 場所と空間一般．配置．位置づけ
- LEAF: false
- DIRECT_CHILDREN_COUNT: 2

### DIRECT_CHILDREN

- `place::(100)` | CODE `(100)` | 場所に関する普遍性．国際的．万国的
- `place::(1-0/-9)` | CODE `(1-0/-9)` | 各種の境界および空間的形態のための固有補助番号の下位区分

<!-- END_FACET_NODE -->

## FACET_NODE `place::(100)`

- FACET: `place`
- NODE_KEY: `place::(100)`
- CODE: `(100)`
- LABEL: 場所に関する普遍性．国際的．万国的
- PARENT_KEY: `place::(1)`
- PATH_CODES: `(1/9)` > `(1)` > `(100)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 場所と空間一般．配置．位置づけ ＞ 場所に関する普遍性．国際的．万国的
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(1-0/-9)`

- FACET: `place`
- NODE_KEY: `place::(1-0/-9)`
- CODE: `(1-0/-9)`
- LABEL: 各種の境界および空間的形態のための固有補助番号の下位区分
- PARENT_KEY: `place::(1)`
- PATH_CODES: `(1/9)` > `(1)` > `(1-0/-9)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 場所と空間一般．配置．位置づけ ＞ 各種の境界および空間的形態のための固有補助番号の下位区分
- LEAF: false
- DIRECT_CHILDREN_COUNT: 8

### DIRECT_CHILDREN

- `place::(1-0)` | CODE `(1-0)` | ゾーン
- `place::(1-1)` | CODE `(1-1)` | 位置づけ．方位．相対位置
- `place::(1-2/-4)` | CODE `(1-2/-4)` | 政治的単位．行政単位
- `place::(1-5)` | CODE `(1-5)` | 従属または半従属の地域
- `place::(1-6)` | CODE `(1-6)` | 様々な観点からの国家または国家群
- `place::(1-7)` | CODE `(1-7)` | 私的・公共的などの性質による場所・領域
- `place::(1-8)` | CODE `(1-8)` | 所在地．発生地．通過地．目的地
- `place::(1-9)` | CODE `(1-9)` | 特殊な観点からの地域区分

### USAGE_NOTE

(1-0/-9)の固有補助番号は，(2/9)の共通補助番号に結び付けて特定地域の部分あるいは観点を与えるのに用いる．また，(1)に結び付けることによって，特定の場所ではなく一般の意味を表すのに用いる．例えば，(1-0)地帯

<!-- END_FACET_NODE -->

## FACET_NODE `place::(1-0)`

- FACET: `place`
- NODE_KEY: `place::(1-0)`
- CODE: `(1-0)`
- LABEL: ゾーン
- PARENT_KEY: `place::(1-0/-9)`
- PATH_CODES: `(1/9)` > `(1)` > `(1-0/-9)` > `(1-0)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 場所と空間一般．配置．位置づけ ＞ 各種の境界および空間的形態のための固有補助番号の下位区分 ＞ ゾーン
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

### INCLUDING

地帯を制限．境界．軍事地帯．未踏の地域

<!-- END_FACET_NODE -->

## FACET_NODE `place::(1-1)`

- FACET: `place`
- NODE_KEY: `place::(1-1)`
- CODE: `(1-1)`
- LABEL: 位置づけ．方位．相対位置
- PARENT_KEY: `place::(1-0/-9)`
- PATH_CODES: `(1/9)` > `(1)` > `(1-0/-9)` > `(1-1)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 場所と空間一般．配置．位置づけ ＞ 各種の境界および空間的形態のための固有補助番号の下位区分 ＞ 位置づけ．方位．相対位置
- LEAF: false
- DIRECT_CHILDREN_COUNT: 9

### DIRECT_CHILDREN

- `place::(1-11)` | CODE `(1-11)` | 東．東方
- `place::(1-12)` | CODE `(1-12)` | 南東．南東方
- `place::(1-13)` | CODE `(1-13)` | 南．南方
- `place::(1-14)` | CODE `(1-14)` | 西南．西南方
- `place::(1-15)` | CODE `(1-15)` | 西．西方
- `place::(1-16)` | CODE `(1-16)` | 北西．北西部
- `place::(1-17)` | CODE `(1-17)` | 北．北方
- `place::(1-18)` | CODE `(1-18)` | 北東
- `place::(1-19)` | CODE `(1-19)` | 相対位置，相対方位

### SCOPE_NOTE

相対位置か方位にだけ(…-11)を使用． 慣習的に東洋を指す東方【訂正】については(5)を見よ

<!-- END_FACET_NODE -->

## FACET_NODE `place::(1-11)`

- FACET: `place`
- NODE_KEY: `place::(1-11)`
- CODE: `(1-11)`
- LABEL: 東．東方
- PARENT_KEY: `place::(1-1)`
- PATH_CODES: `(1/9)` > `(1)` > `(1-0/-9)` > `(1-1)` > `(1-11)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 場所と空間一般．配置．位置づけ ＞ 各種の境界および空間的形態のための固有補助番号の下位区分 ＞ 位置づけ．方位．相対位置 ＞ 東．東方
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(1-12)`

- FACET: `place`
- NODE_KEY: `place::(1-12)`
- CODE: `(1-12)`
- LABEL: 南東．南東方
- PARENT_KEY: `place::(1-1)`
- PATH_CODES: `(1/9)` > `(1)` > `(1-0/-9)` > `(1-1)` > `(1-12)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 場所と空間一般．配置．位置づけ ＞ 各種の境界および空間的形態のための固有補助番号の下位区分 ＞ 位置づけ．方位．相対位置 ＞ 南東．南東方
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(1-13)`

- FACET: `place`
- NODE_KEY: `place::(1-13)`
- CODE: `(1-13)`
- LABEL: 南．南方
- PARENT_KEY: `place::(1-1)`
- PATH_CODES: `(1/9)` > `(1)` > `(1-0/-9)` > `(1-1)` > `(1-13)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 場所と空間一般．配置．位置づけ ＞ 各種の境界および空間的形態のための固有補助番号の下位区分 ＞ 位置づけ．方位．相対位置 ＞ 南．南方
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(1-14)`

- FACET: `place`
- NODE_KEY: `place::(1-14)`
- CODE: `(1-14)`
- LABEL: 西南．西南方
- PARENT_KEY: `place::(1-1)`
- PATH_CODES: `(1/9)` > `(1)` > `(1-0/-9)` > `(1-1)` > `(1-14)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 場所と空間一般．配置．位置づけ ＞ 各種の境界および空間的形態のための固有補助番号の下位区分 ＞ 位置づけ．方位．相対位置 ＞ 西南．西南方
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(1-15)`

- FACET: `place`
- NODE_KEY: `place::(1-15)`
- CODE: `(1-15)`
- LABEL: 西．西方
- PARENT_KEY: `place::(1-1)`
- PATH_CODES: `(1/9)` > `(1)` > `(1-0/-9)` > `(1-1)` > `(1-15)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 場所と空間一般．配置．位置づけ ＞ 各種の境界および空間的形態のための固有補助番号の下位区分 ＞ 位置づけ．方位．相対位置 ＞ 西．西方
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(1-16)`

- FACET: `place`
- NODE_KEY: `place::(1-16)`
- CODE: `(1-16)`
- LABEL: 北西．北西部
- PARENT_KEY: `place::(1-1)`
- PATH_CODES: `(1/9)` > `(1)` > `(1-0/-9)` > `(1-1)` > `(1-16)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 場所と空間一般．配置．位置づけ ＞ 各種の境界および空間的形態のための固有補助番号の下位区分 ＞ 位置づけ．方位．相対位置 ＞ 北西．北西部
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(1-17)`

- FACET: `place`
- NODE_KEY: `place::(1-17)`
- CODE: `(1-17)`
- LABEL: 北．北方
- PARENT_KEY: `place::(1-1)`
- PATH_CODES: `(1/9)` > `(1)` > `(1-0/-9)` > `(1-1)` > `(1-17)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 場所と空間一般．配置．位置づけ ＞ 各種の境界および空間的形態のための固有補助番号の下位区分 ＞ 位置づけ．方位．相対位置 ＞ 北．北方
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(1-18)`

- FACET: `place`
- NODE_KEY: `place::(1-18)`
- CODE: `(1-18)`
- LABEL: 北東
- PARENT_KEY: `place::(1-1)`
- PATH_CODES: `(1/9)` > `(1)` > `(1-0/-9)` > `(1-1)` > `(1-18)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 場所と空間一般．配置．位置づけ ＞ 各種の境界および空間的形態のための固有補助番号の下位区分 ＞ 位置づけ．方位．相対位置 ＞ 北東
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(1-19)`

- FACET: `place`
- NODE_KEY: `place::(1-19)`
- CODE: `(1-19)`
- LABEL: 相対位置，相対方位
- PARENT_KEY: `place::(1-1)`
- PATH_CODES: `(1/9)` > `(1)` > `(1-0/-9)` > `(1-1)` > `(1-19)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 場所と空間一般．配置．位置づけ ＞ 各種の境界および空間的形態のための固有補助番号の下位区分 ＞ 位置づけ．方位．相対位置 ＞ 相対位置，相対方位
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(1-2/-4)`

- FACET: `place`
- NODE_KEY: `place::(1-2/-4)`
- CODE: `(1-2/-4)`
- LABEL: 政治的単位．行政単位
- PARENT_KEY: `place::(1-0/-9)`
- PATH_CODES: `(1/9)` > `(1)` > `(1-0/-9)` > `(1-2/-4)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 場所と空間一般．配置．位置づけ ＞ 各種の境界および空間的形態のための固有補助番号の下位区分 ＞ 政治的単位．行政単位
- LEAF: false
- DIRECT_CHILDREN_COUNT: 3

### DIRECT_CHILDREN

- `place::(1-2)` | CODE `(1-2)` | 行政の最小．市町村など
- `place::(1-3)` | CODE `(1-3)` | 国家内のより大きな単位
- `place::(1-4)` | CODE `(1-4)` | 最高レベルの単位．国家．連邦

### USAGE_NOTE

固有補助表(1-2/-4)は,(3/9)に適用した場合は特定の地域を意味し，ここに列挙する形式で用いた場合は行政単位一般またはそれに関連する事柄を意味する．

<!-- END_FACET_NODE -->

## FACET_NODE `place::(1-2)`

- FACET: `place`
- NODE_KEY: `place::(1-2)`
- CODE: `(1-2)`
- LABEL: 行政の最小．市町村など
- PARENT_KEY: `place::(1-2/-4)`
- PATH_CODES: `(1/9)` > `(1)` > `(1-0/-9)` > `(1-2/-4)` > `(1-2)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 場所と空間一般．配置．位置づけ ＞ 各種の境界および空間的形態のための固有補助番号の下位区分 ＞ 政治的単位．行政単位 ＞ 行政の最小．市町村など
- LEAF: false
- DIRECT_CHILDREN_COUNT: 2

### DIRECT_CHILDREN

- `place::(1-24)` | CODE `(1-24)` | 広域行政単位
- `place::(1-25)` | CODE `(1-25)` | 首都．中心都市

### INCLUDING

地区．市町村自治体,地方自治体

<!-- END_FACET_NODE -->

## FACET_NODE `place::(1-24)`

- FACET: `place`
- NODE_KEY: `place::(1-24)`
- CODE: `(1-24)`
- LABEL: 広域行政単位
- PARENT_KEY: `place::(1-2)`
- PATH_CODES: `(1/9)` > `(1)` > `(1-0/-9)` > `(1-2/-4)` > `(1-2)` > `(1-24)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 場所と空間一般．配置．位置づけ ＞ 各種の境界および空間的形態のための固有補助番号の下位区分 ＞ 政治的単位．行政単位 ＞ 行政の最小．市町村など ＞ 広域行政単位
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

### INCLUDING

カントン

<!-- END_FACET_NODE -->

## FACET_NODE `place::(1-25)`

- FACET: `place`
- NODE_KEY: `place::(1-25)`
- CODE: `(1-25)`
- LABEL: 首都．中心都市
- PARENT_KEY: `place::(1-2)`
- PATH_CODES: `(1/9)` > `(1)` > `(1-0/-9)` > `(1-2/-4)` > `(1-2)` > `(1-25)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 場所と空間一般．配置．位置づけ ＞ 各種の境界および空間的形態のための固有補助番号の下位区分 ＞ 政治的単位．行政単位 ＞ 行政の最小．市町村など ＞ 首都．中心都市
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(1-3)`

- FACET: `place`
- NODE_KEY: `place::(1-3)`
- CODE: `(1-3)`
- LABEL: 国家内のより大きな単位
- PARENT_KEY: `place::(1-2/-4)`
- PATH_CODES: `(1/9)` > `(1)` > `(1-0/-9)` > `(1-2/-4)` > `(1-3)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 場所と空間一般．配置．位置づけ ＞ 各種の境界および空間的形態のための固有補助番号の下位区分 ＞ 政治的単位．行政単位 ＞ 国家内のより大きな単位
- LEAF: false
- DIRECT_CHILDREN_COUNT: 3

### DIRECT_CHILDREN

- `place::(1-32)` | CODE `(1-32)` | より高水準行政単位．行政区
- `place::(1-35)` | CODE `(1-35)` | 中間の行政単位
- `place::(1-37)` | CODE `(1-37)` | より低レベルの行政単位

<!-- END_FACET_NODE -->

## FACET_NODE `place::(1-32)`

- FACET: `place`
- NODE_KEY: `place::(1-32)`
- CODE: `(1-32)`
- LABEL: より高水準行政単位．行政区
- PARENT_KEY: `place::(1-3)`
- PATH_CODES: `(1/9)` > `(1)` > `(1-0/-9)` > `(1-2/-4)` > `(1-3)` > `(1-32)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 場所と空間一般．配置．位置づけ ＞ 各種の境界および空間的形態のための固有補助番号の下位区分 ＞ 政治的単位．行政単位 ＞ 国家内のより大きな単位 ＞ より高水準行政単位．行政区
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(1-35)`

- FACET: `place`
- NODE_KEY: `place::(1-35)`
- CODE: `(1-35)`
- LABEL: 中間の行政単位
- PARENT_KEY: `place::(1-3)`
- PATH_CODES: `(1/9)` > `(1)` > `(1-0/-9)` > `(1-2/-4)` > `(1-3)` > `(1-35)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 場所と空間一般．配置．位置づけ ＞ 各種の境界および空間的形態のための固有補助番号の下位区分 ＞ 政治的単位．行政単位 ＞ 国家内のより大きな単位 ＞ 中間の行政単位
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

### INCLUDING

郡,県など

<!-- END_FACET_NODE -->

## FACET_NODE `place::(1-37)`

- FACET: `place`
- NODE_KEY: `place::(1-37)`
- CODE: `(1-37)`
- LABEL: より低レベルの行政単位
- PARENT_KEY: `place::(1-3)`
- PATH_CODES: `(1/9)` > `(1)` > `(1-0/-9)` > `(1-2/-4)` > `(1-3)` > `(1-37)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 場所と空間一般．配置．位置づけ ＞ 各種の境界および空間的形態のための固有補助番号の下位区分 ＞ 政治的単位．行政単位 ＞ 国家内のより大きな単位 ＞ より低レベルの行政単位
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

### INCLUDING

区,地区

<!-- END_FACET_NODE -->

## FACET_NODE `place::(1-4)`

- FACET: `place`
- NODE_KEY: `place::(1-4)`
- CODE: `(1-4)`
- LABEL: 最高レベルの単位．国家．連邦
- PARENT_KEY: `place::(1-2/-4)`
- PATH_CODES: `(1/9)` > `(1)` > `(1-0/-9)` > `(1-2/-4)` > `(1-4)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 場所と空間一般．配置．位置づけ ＞ 各種の境界および空間的形態のための固有補助番号の下位区分 ＞ 政治的単位．行政単位 ＞ 最高レベルの単位．国家．連邦
- LEAF: false
- DIRECT_CHILDREN_COUNT: 2

### DIRECT_CHILDREN

- `place::(1-43)` | CODE `(1-43)` | 連邦構成国．連邦国家．自治共和国
- `place::(1-44)` | CODE `(1-44)` | 帝国．本国・自治領・植民地の総体

<!-- END_FACET_NODE -->

## FACET_NODE `place::(1-43)`

- FACET: `place`
- NODE_KEY: `place::(1-43)`
- CODE: `(1-43)`
- LABEL: 連邦構成国．連邦国家．自治共和国
- PARENT_KEY: `place::(1-4)`
- PATH_CODES: `(1/9)` > `(1)` > `(1-0/-9)` > `(1-2/-4)` > `(1-4)` > `(1-43)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 場所と空間一般．配置．位置づけ ＞ 各種の境界および空間的形態のための固有補助番号の下位区分 ＞ 政治的単位．行政単位 ＞ 最高レベルの単位．国家．連邦 ＞ 連邦構成国．連邦国家．自治共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(1-44)`

- FACET: `place`
- NODE_KEY: `place::(1-44)`
- CODE: `(1-44)`
- LABEL: 帝国．本国・自治領・植民地の総体
- PARENT_KEY: `place::(1-4)`
- PATH_CODES: `(1/9)` > `(1)` > `(1-0/-9)` > `(1-2/-4)` > `(1-4)` > `(1-44)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 場所と空間一般．配置．位置づけ ＞ 各種の境界および空間的形態のための固有補助番号の下位区分 ＞ 政治的単位．行政単位 ＞ 最高レベルの単位．国家．連邦 ＞ 帝国．本国・自治領・植民地の総体
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(1-5)`

- FACET: `place`
- NODE_KEY: `place::(1-5)`
- CODE: `(1-5)`
- LABEL: 従属または半従属の地域
- PARENT_KEY: `place::(1-0/-9)`
- PATH_CODES: `(1/9)` > `(1)` > `(1-0/-9)` > `(1-5)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 場所と空間一般．配置．位置づけ ＞ 各種の境界および空間的形態のための固有補助番号の下位区分 ＞ 従属または半従属の地域
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(1-6)`

- FACET: `place`
- NODE_KEY: `place::(1-6)`
- CODE: `(1-6)`
- LABEL: 様々な観点からの国家または国家群
- PARENT_KEY: `place::(1-0/-9)`
- PATH_CODES: `(1/9)` > `(1)` > `(1-0/-9)` > `(1-6)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 場所と空間一般．配置．位置づけ ＞ 各種の境界および空間的形態のための固有補助番号の下位区分 ＞ 様々な観点からの国家または国家群
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(1-7)`

- FACET: `place`
- NODE_KEY: `place::(1-7)`
- CODE: `(1-7)`
- LABEL: 私的・公共的などの性質による場所・領域
- PARENT_KEY: `place::(1-0/-9)`
- PATH_CODES: `(1/9)` > `(1)` > `(1-0/-9)` > `(1-7)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 場所と空間一般．配置．位置づけ ＞ 各種の境界および空間的形態のための固有補助番号の下位区分 ＞ 私的・公共的などの性質による場所・領域
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(1-8)`

- FACET: `place`
- NODE_KEY: `place::(1-8)`
- CODE: `(1-8)`
- LABEL: 所在地．発生地．通過地．目的地
- PARENT_KEY: `place::(1-0/-9)`
- PATH_CODES: `(1/9)` > `(1)` > `(1-0/-9)` > `(1-8)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 場所と空間一般．配置．位置づけ ＞ 各種の境界および空間的形態のための固有補助番号の下位区分 ＞ 所在地．発生地．通過地．目的地
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(1-9)`

- FACET: `place`
- NODE_KEY: `place::(1-9)`
- CODE: `(1-9)`
- LABEL: 特殊な観点からの地域区分
- PARENT_KEY: `place::(1-0/-9)`
- PATH_CODES: `(1/9)` > `(1)` > `(1-0/-9)` > `(1-9)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 場所と空間一般．配置．位置づけ ＞ 各種の境界および空間的形態のための固有補助番号の下位区分 ＞ 特殊な観点からの地域区分
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(2)`

- FACET: `place`
- NODE_KEY: `place::(2)`
- CODE: `(2)`
- LABEL: 自然地理学的名称
- PARENT_KEY: `place::(1/9)`
- PATH_CODES: `(1/9)` > `(2)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 自然地理学的名称
- LEAF: false
- DIRECT_CHILDREN_COUNT: 7

### DIRECT_CHILDREN

- `place::(20)` | CODE `(20)` | 生態圏
- `place::(21)` | CODE `(21)` | 地表面一般．特に陸地．自然的地帯，地域
- `place::(23)` | CODE `(23)` | 海面上．地表の起伏．地上一般．山
- `place::(24)` | CODE `(24)` | 海面下．地下
- `place::(25)` | CODE `(25)` | 平地．耕地．居住地
- `place::(26)` | CODE `(26)` | 海洋，海との接続
- `place::(28)` | CODE `(28)` | 陸水

<!-- END_FACET_NODE -->

## FACET_NODE `place::(20)`

- FACET: `place`
- NODE_KEY: `place::(20)`
- CODE: `(20)`
- LABEL: 生態圏
- PARENT_KEY: `place::(2)`
- PATH_CODES: `(1/9)` > `(2)` > `(20)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 自然地理学的名称 ＞ 生態圏
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(21)`

- FACET: `place`
- NODE_KEY: `place::(21)`
- CODE: `(21)`
- LABEL: 地表面一般．特に陸地．自然的地帯，地域
- PARENT_KEY: `place::(2)`
- PATH_CODES: `(1/9)` > `(2)` > `(21)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 自然地理学的名称 ＞ 地表面一般．特に陸地．自然的地帯，地域
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(23)`

- FACET: `place`
- NODE_KEY: `place::(23)`
- CODE: `(23)`
- LABEL: 海面上．地表の起伏．地上一般．山
- PARENT_KEY: `place::(2)`
- PATH_CODES: `(1/9)` > `(2)` > `(23)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 自然地理学的名称 ＞ 海面上．地表の起伏．地上一般．山
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(24)`

- FACET: `place`
- NODE_KEY: `place::(24)`
- CODE: `(24)`
- LABEL: 海面下．地下
- PARENT_KEY: `place::(2)`
- PATH_CODES: `(1/9)` > `(2)` > `(24)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 自然地理学的名称 ＞ 海面下．地下
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(25)`

- FACET: `place`
- NODE_KEY: `place::(25)`
- CODE: `(25)`
- LABEL: 平地．耕地．居住地
- PARENT_KEY: `place::(2)`
- PATH_CODES: `(1/9)` > `(2)` > `(25)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 自然地理学的名称 ＞ 平地．耕地．居住地
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(26)`

- FACET: `place`
- NODE_KEY: `place::(26)`
- CODE: `(26)`
- LABEL: 海洋，海との接続
- PARENT_KEY: `place::(2)`
- PATH_CODES: `(1/9)` > `(2)` > `(26)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 自然地理学的名称 ＞ 海洋，海との接続
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(28)`

- FACET: `place`
- NODE_KEY: `place::(28)`
- CODE: `(28)`
- LABEL: 陸水
- PARENT_KEY: `place::(2)`
- PATH_CODES: `(1/9)` > `(2)` > `(28)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 自然地理学的名称 ＞ 陸水
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(3/9)`

- FACET: `place`
- NODE_KEY: `place::(3/9)`
- CODE: `(3/9)`
- LABEL: 古代および現代世界の個々の場所
- PARENT_KEY: `place::(1/9)`
- PATH_CODES: `(1/9)` > `(3/9)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所
- LEAF: false
- DIRECT_CHILDREN_COUNT: 2

### DIRECT_CHILDREN

- `place::(3)` | CODE `(3)` | 古代，中世の世界の場所
- `place::(4/9)` | CODE `(4/9)` | 現代の世界の国と場所

<!-- END_FACET_NODE -->

## FACET_NODE `place::(3)`

- FACET: `place`
- NODE_KEY: `place::(3)`
- CODE: `(3)`
- LABEL: 古代，中世の世界の場所
- PARENT_KEY: `place::(3/9)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(3)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 古代，中世の世界の場所
- LEAF: false
- DIRECT_CHILDREN_COUNT: 9

### DIRECT_CHILDREN

- `place::(31)` | CODE `(31)` | 古代の中国と日本
- `place::(32)` | CODE `(32)` | 古代エジプト
- `place::(33)` | CODE `(33)` | ユダヤ．ローマのユダヤ属州．聖地．イスラエル人の領域
- `place::(34)` | CODE `(34)` | 古代インド
- `place::(35)` | CODE `(35)` | メディア・ペルシア
- `place::(36)` | CODE `(36)` | いわゆるバルバロイ（非ギリシャ民族）の地域
- `place::(37)` | CODE `(37)` | イタリア．古代ローマと古代イタリア
- `place::(38)` | CODE `(38)` | 古代ギリシア
- `place::(399)` | CODE `(399)` | 他の地域．ギリシャ・ローマ古典時代のもの以外の古代の地理的な部門

<!-- END_FACET_NODE -->

## FACET_NODE `place::(31)`

- FACET: `place`
- NODE_KEY: `place::(31)`
- CODE: `(31)`
- LABEL: 古代の中国と日本
- PARENT_KEY: `place::(3)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(3)` > `(31)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 古代，中世の世界の場所 ＞ 古代の中国と日本
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(32)`

- FACET: `place`
- NODE_KEY: `place::(32)`
- CODE: `(32)`
- LABEL: 古代エジプト
- PARENT_KEY: `place::(3)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(3)` > `(32)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 古代，中世の世界の場所 ＞ 古代エジプト
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(33)`

- FACET: `place`
- NODE_KEY: `place::(33)`
- CODE: `(33)`
- LABEL: ユダヤ．ローマのユダヤ属州．聖地．イスラエル人の領域
- PARENT_KEY: `place::(3)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(3)` > `(33)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 古代，中世の世界の場所 ＞ ユダヤ．ローマのユダヤ属州．聖地．イスラエル人の領域
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

### INCLUDING

エルサレム，ナザレ，ベツレヘム，シケム，ジェリコ

<!-- END_FACET_NODE -->

## FACET_NODE `place::(34)`

- FACET: `place`
- NODE_KEY: `place::(34)`
- CODE: `(34)`
- LABEL: 古代インド
- PARENT_KEY: `place::(3)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(3)` > `(34)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 古代，中世の世界の場所 ＞ 古代インド
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(35)`

- FACET: `place`
- NODE_KEY: `place::(35)`
- CODE: `(35)`
- LABEL: メディア・ペルシア
- PARENT_KEY: `place::(3)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(3)` > `(35)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 古代，中世の世界の場所 ＞ メディア・ペルシア
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(36)`

- FACET: `place`
- NODE_KEY: `place::(36)`
- CODE: `(36)`
- LABEL: いわゆるバルバロイ（非ギリシャ民族）の地域
- PARENT_KEY: `place::(3)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(3)` > `(36)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 古代，中世の世界の場所 ＞ いわゆるバルバロイ（非ギリシャ民族）の地域
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

### INCLUDING

ゲルマン諸部族．ケルト族．スラヴ族．北欧諸民族．フン族．アヴァール族

<!-- END_FACET_NODE -->

## FACET_NODE `place::(37)`

- FACET: `place`
- NODE_KEY: `place::(37)`
- CODE: `(37)`
- LABEL: イタリア．古代ローマと古代イタリア
- PARENT_KEY: `place::(3)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(3)` > `(37)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 古代，中世の世界の場所 ＞ イタリア．古代ローマと古代イタリア
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(38)`

- FACET: `place`
- NODE_KEY: `place::(38)`
- CODE: `(38)`
- LABEL: 古代ギリシア
- PARENT_KEY: `place::(3)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(3)` > `(38)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 古代，中世の世界の場所 ＞ 古代ギリシア
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(399)`

- FACET: `place`
- NODE_KEY: `place::(399)`
- CODE: `(399)`
- LABEL: 他の地域．ギリシャ・ローマ古典時代のもの以外の古代の地理的な部門
- PARENT_KEY: `place::(3)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(3)` > `(399)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 古代，中世の世界の場所 ＞ 他の地域．ギリシャ・ローマ古典時代のもの以外の古代の地理的な部門
- LEAF: false
- DIRECT_CHILDREN_COUNT: 1

### DIRECT_CHILDREN

- `place::(399.7)` | CODE `(399.7)` | 古代アメリカ文化地域．コロンブス到来以前のアメリカ

<!-- END_FACET_NODE -->

## FACET_NODE `place::(399.7)`

- FACET: `place`
- NODE_KEY: `place::(399.7)`
- CODE: `(399.7)`
- LABEL: 古代アメリカ文化地域．コロンブス到来以前のアメリカ
- PARENT_KEY: `place::(399)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(3)` > `(399)` > `(399.7)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 古代，中世の世界の場所 ＞ 他の地域．ギリシャ・ローマ古典時代のもの以外の古代の地理的な部門 ＞ 古代アメリカ文化地域．コロンブス到来以前のアメリカ
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(4/9)`

- FACET: `place`
- NODE_KEY: `place::(4/9)`
- CODE: `(4/9)`
- LABEL: 現代の世界の国と場所
- PARENT_KEY: `place::(3/9)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所
- LEAF: false
- DIRECT_CHILDREN_COUNT: 5

### DIRECT_CHILDREN

- `place::(4)` | CODE `(4)` | ヨーロッパ
- `place::(5)` | CODE `(5)` | アジア
- `place::(6)` | CODE `(6)` | アフリカ
- `place::(7/8)` | CODE `(7/8)` | アメリカ．南北アメリカ大陸
- `place::(9)` | CODE `(9)` | 南太平洋およびオーストラリアの国・地域．北極，南極

### USAGE_NOTE

詳細は固有補助表(1-0/-9)とアルファベット拡張(表1h)の少なくとも一方によって表示．

<!-- END_FACET_NODE -->

## FACET_NODE `place::(4)`

- FACET: `place`
- NODE_KEY: `place::(4)`
- CODE: `(4)`
- LABEL: ヨーロッパ
- PARENT_KEY: `place::(4/9)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(4)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ ヨーロッパ
- LEAF: false
- DIRECT_CHILDREN_COUNT: 29

### DIRECT_CHILDREN

- `place::(41)` | CODE `(41)` | ブリテン諸島の諸国
- `place::(430)` | CODE `(430)` | ドイツ連邦共和国
- `place::(435.9)` | CODE `(435.9)` | ルクセンブルク大公国
- `place::(436)` | CODE `(436)` | オーストリア共和国
- `place::(437.3)` | CODE `(437.3)` | チェコ共和国
- `place::(437.6)` | CODE `(437.6)` | スロバキア共和国
- `place::(438)` | CODE `(438)` | ポーランド共和国
- `place::(439)` | CODE `(439)` | ハンガリー共和国
- `place::(44)` | CODE `(44)` | フランス共和国
- `place::(450)` | CODE `(450)` | イタリア共和国
- `place::(454.4)` | CODE `(454.4)` | サンマリノ共和国
- `place::(456.31)` | CODE `(456.31)` | バチカン市(教皇庁)
- `place::(458.2)` | CODE `(458.2)` | マルタ共和国
- `place::(46)` | CODE `(46)` | イベリア半島
- `place::(470+571)` | CODE `(470+571)` | ロシア連邦共和国
- `place::(474)` | CODE `(474)` | バルト海沿岸諸国
- `place::(476)` | CODE `(476)` | ベラルーシ共和国
- `place::(477)` | CODE `(477)` | ウクライナ
- `place::(478)` | CODE `(478)` | モルドバ共和国
- `place::(479)` | CODE `(479)` | コーカサス地域
- `place::(48)` | CODE `(48)` | スカンジナビア諸国
- `place::(492)` | CODE `(492)` | オランダ王国
- `place::(493)` | CODE `(493)` | ベルギー王国
- `place::(494)` | CODE `(494)` | スイス連邦
- `place::(495)` | CODE `(495)` | ギリシャ共和国
- `place::(497)` | CODE `(497)` | バルカン諸国
- `place::(498)` | CODE `(498)` | ルーマニア共和国
- `place::(491.1)` | CODE `(491.1)` | アイスランド共和国
- `place::(496.5)` | CODE `(496.5)` | アルバニア共和国

<!-- END_FACET_NODE -->

## FACET_NODE `place::(41)`

- FACET: `place`
- NODE_KEY: `place::(41)`
- CODE: `(41)`
- LABEL: ブリテン諸島の諸国
- PARENT_KEY: `place::(4)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(4)` > `(41)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ ヨーロッパ ＞ ブリテン諸島の諸国
- LEAF: false
- DIRECT_CHILDREN_COUNT: 2

### DIRECT_CHILDREN

- `place::(410)` | CODE `(410)` | イギリスおよび北部アイルランド連合王国
- `place::(417)` | CODE `(417)` | アイルランド共和国

### INCLUDING

英国，アイルランド，小島嶼

<!-- END_FACET_NODE -->

## FACET_NODE `place::(410)`

- FACET: `place`
- NODE_KEY: `place::(410)`
- CODE: `(410)`
- LABEL: イギリスおよび北部アイルランド連合王国
- PARENT_KEY: `place::(41)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(4)` > `(41)` > `(410)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ ヨーロッパ ＞ ブリテン諸島の諸国 ＞ イギリスおよび北部アイルランド連合王国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(417)`

- FACET: `place`
- NODE_KEY: `place::(417)`
- CODE: `(417)`
- LABEL: アイルランド共和国
- PARENT_KEY: `place::(41)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(4)` > `(41)` > `(417)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ ヨーロッパ ＞ ブリテン諸島の諸国 ＞ アイルランド共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(430)`

- FACET: `place`
- NODE_KEY: `place::(430)`
- CODE: `(430)`
- LABEL: ドイツ連邦共和国
- PARENT_KEY: `place::(4)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(4)` > `(430)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ ヨーロッパ ＞ ドイツ連邦共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(435.9)`

- FACET: `place`
- NODE_KEY: `place::(435.9)`
- CODE: `(435.9)`
- LABEL: ルクセンブルク大公国
- PARENT_KEY: `place::(4)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(4)` > `(435.9)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ ヨーロッパ ＞ ルクセンブルク大公国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(436)`

- FACET: `place`
- NODE_KEY: `place::(436)`
- CODE: `(436)`
- LABEL: オーストリア共和国
- PARENT_KEY: `place::(4)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(4)` > `(436)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ ヨーロッパ ＞ オーストリア共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(437.3)`

- FACET: `place`
- NODE_KEY: `place::(437.3)`
- CODE: `(437.3)`
- LABEL: チェコ共和国
- PARENT_KEY: `place::(4)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(4)` > `(437.3)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ ヨーロッパ ＞ チェコ共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(437.6)`

- FACET: `place`
- NODE_KEY: `place::(437.6)`
- CODE: `(437.6)`
- LABEL: スロバキア共和国
- PARENT_KEY: `place::(4)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(4)` > `(437.6)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ ヨーロッパ ＞ スロバキア共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(438)`

- FACET: `place`
- NODE_KEY: `place::(438)`
- CODE: `(438)`
- LABEL: ポーランド共和国
- PARENT_KEY: `place::(4)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(4)` > `(438)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ ヨーロッパ ＞ ポーランド共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(439)`

- FACET: `place`
- NODE_KEY: `place::(439)`
- CODE: `(439)`
- LABEL: ハンガリー共和国
- PARENT_KEY: `place::(4)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(4)` > `(439)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ ヨーロッパ ＞ ハンガリー共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(44)`

- FACET: `place`
- NODE_KEY: `place::(44)`
- CODE: `(44)`
- LABEL: フランス共和国
- PARENT_KEY: `place::(4)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(4)` > `(44)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ ヨーロッパ ＞ フランス共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(450)`

- FACET: `place`
- NODE_KEY: `place::(450)`
- CODE: `(450)`
- LABEL: イタリア共和国
- PARENT_KEY: `place::(4)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(4)` > `(450)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ ヨーロッパ ＞ イタリア共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(454.4)`

- FACET: `place`
- NODE_KEY: `place::(454.4)`
- CODE: `(454.4)`
- LABEL: サンマリノ共和国
- PARENT_KEY: `place::(4)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(4)` > `(454.4)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ ヨーロッパ ＞ サンマリノ共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(456.31)`

- FACET: `place`
- NODE_KEY: `place::(456.31)`
- CODE: `(456.31)`
- LABEL: バチカン市(教皇庁)
- PARENT_KEY: `place::(4)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(4)` > `(456.31)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ ヨーロッパ ＞ バチカン市(教皇庁)
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(458.2)`

- FACET: `place`
- NODE_KEY: `place::(458.2)`
- CODE: `(458.2)`
- LABEL: マルタ共和国
- PARENT_KEY: `place::(4)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(4)` > `(458.2)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ ヨーロッパ ＞ マルタ共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(46)`

- FACET: `place`
- NODE_KEY: `place::(46)`
- CODE: `(46)`
- LABEL: イベリア半島
- PARENT_KEY: `place::(4)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(4)` > `(46)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ ヨーロッパ ＞ イベリア半島
- LEAF: false
- DIRECT_CHILDREN_COUNT: 3

### DIRECT_CHILDREN

- `place::(460)` | CODE `(460)` | スペイン王国
- `place::(467)` | CODE `(467)` | アンドラ公国
- `place::(469)` | CODE `(469)` | ポルトガル共和国

### INCLUDING

スペイン，アンドラ，ポルトガル

<!-- END_FACET_NODE -->

## FACET_NODE `place::(460)`

- FACET: `place`
- NODE_KEY: `place::(460)`
- CODE: `(460)`
- LABEL: スペイン王国
- PARENT_KEY: `place::(46)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(4)` > `(46)` > `(460)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ ヨーロッパ ＞ イベリア半島 ＞ スペイン王国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(467)`

- FACET: `place`
- NODE_KEY: `place::(467)`
- CODE: `(467)`
- LABEL: アンドラ公国
- PARENT_KEY: `place::(46)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(4)` > `(46)` > `(467)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ ヨーロッパ ＞ イベリア半島 ＞ アンドラ公国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(469)`

- FACET: `place`
- NODE_KEY: `place::(469)`
- CODE: `(469)`
- LABEL: ポルトガル共和国
- PARENT_KEY: `place::(46)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(4)` > `(46)` > `(469)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ ヨーロッパ ＞ イベリア半島 ＞ ポルトガル共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(470+571)`

- FACET: `place`
- NODE_KEY: `place::(470+571)`
- CODE: `(470+571)`
- LABEL: ロシア連邦共和国
- PARENT_KEY: `place::(4)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(4)` > `(470+571)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ ヨーロッパ ＞ ロシア連邦共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(474)`

- FACET: `place`
- NODE_KEY: `place::(474)`
- CODE: `(474)`
- LABEL: バルト海沿岸諸国
- PARENT_KEY: `place::(4)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(4)` > `(474)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ ヨーロッパ ＞ バルト海沿岸諸国
- LEAF: false
- DIRECT_CHILDREN_COUNT: 3

### DIRECT_CHILDREN

- `place::(474.2)` | CODE `(474.2)` | エストニア共和国
- `place::(474.3)` | CODE `(474.3)` | ラトビア共和国
- `place::(474.5)` | CODE `(474.5)` | リトアニア共和国

### INCLUDING

エストニア，ラトビア，リトアニア

<!-- END_FACET_NODE -->

## FACET_NODE `place::(474.2)`

- FACET: `place`
- NODE_KEY: `place::(474.2)`
- CODE: `(474.2)`
- LABEL: エストニア共和国
- PARENT_KEY: `place::(474)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(4)` > `(474)` > `(474.2)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ ヨーロッパ ＞ バルト海沿岸諸国 ＞ エストニア共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(474.3)`

- FACET: `place`
- NODE_KEY: `place::(474.3)`
- CODE: `(474.3)`
- LABEL: ラトビア共和国
- PARENT_KEY: `place::(474)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(4)` > `(474)` > `(474.3)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ ヨーロッパ ＞ バルト海沿岸諸国 ＞ ラトビア共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(474.5)`

- FACET: `place`
- NODE_KEY: `place::(474.5)`
- CODE: `(474.5)`
- LABEL: リトアニア共和国
- PARENT_KEY: `place::(474)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(4)` > `(474)` > `(474.5)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ ヨーロッパ ＞ バルト海沿岸諸国 ＞ リトアニア共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(476)`

- FACET: `place`
- NODE_KEY: `place::(476)`
- CODE: `(476)`
- LABEL: ベラルーシ共和国
- PARENT_KEY: `place::(4)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(4)` > `(476)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ ヨーロッパ ＞ ベラルーシ共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(477)`

- FACET: `place`
- NODE_KEY: `place::(477)`
- CODE: `(477)`
- LABEL: ウクライナ
- PARENT_KEY: `place::(4)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(4)` > `(477)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ ヨーロッパ ＞ ウクライナ
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(478)`

- FACET: `place`
- NODE_KEY: `place::(478)`
- CODE: `(478)`
- LABEL: モルドバ共和国
- PARENT_KEY: `place::(4)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(4)` > `(478)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ ヨーロッパ ＞ モルドバ共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(479)`

- FACET: `place`
- NODE_KEY: `place::(479)`
- CODE: `(479)`
- LABEL: コーカサス地域
- PARENT_KEY: `place::(4)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(4)` > `(479)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ ヨーロッパ ＞ コーカサス地域
- LEAF: false
- DIRECT_CHILDREN_COUNT: 3

### DIRECT_CHILDREN

- `place::(479.22)` | CODE `(479.22)` | グルジア共和国
- `place::(479.24)` | CODE `(479.24)` | アゼルバイジャン共和国
- `place::(479.25)` | CODE `(479.25)` | アルメニア共和国

### INCLUDING

グルジア，アゼルバイジャン，アルメニア

<!-- END_FACET_NODE -->

## FACET_NODE `place::(479.22)`

- FACET: `place`
- NODE_KEY: `place::(479.22)`
- CODE: `(479.22)`
- LABEL: グルジア共和国
- PARENT_KEY: `place::(479)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(4)` > `(479)` > `(479.22)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ ヨーロッパ ＞ コーカサス地域 ＞ グルジア共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(479.24)`

- FACET: `place`
- NODE_KEY: `place::(479.24)`
- CODE: `(479.24)`
- LABEL: アゼルバイジャン共和国
- PARENT_KEY: `place::(479)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(4)` > `(479)` > `(479.24)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ ヨーロッパ ＞ コーカサス地域 ＞ アゼルバイジャン共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(479.25)`

- FACET: `place`
- NODE_KEY: `place::(479.25)`
- CODE: `(479.25)`
- LABEL: アルメニア共和国
- PARENT_KEY: `place::(479)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(4)` > `(479)` > `(479.25)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ ヨーロッパ ＞ コーカサス地域 ＞ アルメニア共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(48)`

- FACET: `place`
- NODE_KEY: `place::(48)`
- CODE: `(48)`
- LABEL: スカンジナビア諸国
- PARENT_KEY: `place::(4)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(4)` > `(48)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ ヨーロッパ ＞ スカンジナビア諸国
- LEAF: false
- DIRECT_CHILDREN_COUNT: 4

### DIRECT_CHILDREN

- `place::(480)` | CODE `(480)` | フィンランド共和国
- `place::(481)` | CODE `(481)` | ノルウェー王国
- `place::(485)` | CODE `(485)` | スウェーデン王国
- `place::(489)` | CODE `(489)` | デンマーク王国

### INCLUDING

フィンランド，ノルウェー，スウェーデン，デンマーク

<!-- END_FACET_NODE -->

## FACET_NODE `place::(480)`

- FACET: `place`
- NODE_KEY: `place::(480)`
- CODE: `(480)`
- LABEL: フィンランド共和国
- PARENT_KEY: `place::(48)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(4)` > `(48)` > `(480)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ ヨーロッパ ＞ スカンジナビア諸国 ＞ フィンランド共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(481)`

- FACET: `place`
- NODE_KEY: `place::(481)`
- CODE: `(481)`
- LABEL: ノルウェー王国
- PARENT_KEY: `place::(48)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(4)` > `(48)` > `(481)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ ヨーロッパ ＞ スカンジナビア諸国 ＞ ノルウェー王国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(485)`

- FACET: `place`
- NODE_KEY: `place::(485)`
- CODE: `(485)`
- LABEL: スウェーデン王国
- PARENT_KEY: `place::(48)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(4)` > `(48)` > `(485)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ ヨーロッパ ＞ スカンジナビア諸国 ＞ スウェーデン王国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(489)`

- FACET: `place`
- NODE_KEY: `place::(489)`
- CODE: `(489)`
- LABEL: デンマーク王国
- PARENT_KEY: `place::(48)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(4)` > `(48)` > `(489)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ ヨーロッパ ＞ スカンジナビア諸国 ＞ デンマーク王国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(492)`

- FACET: `place`
- NODE_KEY: `place::(492)`
- CODE: `(492)`
- LABEL: オランダ王国
- PARENT_KEY: `place::(4)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(4)` > `(492)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ ヨーロッパ ＞ オランダ王国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(493)`

- FACET: `place`
- NODE_KEY: `place::(493)`
- CODE: `(493)`
- LABEL: ベルギー王国
- PARENT_KEY: `place::(4)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(4)` > `(493)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ ヨーロッパ ＞ ベルギー王国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(494)`

- FACET: `place`
- NODE_KEY: `place::(494)`
- CODE: `(494)`
- LABEL: スイス連邦
- PARENT_KEY: `place::(4)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(4)` > `(494)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ ヨーロッパ ＞ スイス連邦
- LEAF: false
- DIRECT_CHILDREN_COUNT: 1

### DIRECT_CHILDREN

- `place::(494.9)` | CODE `(494.9)` | リヒテンシュタイン公国

<!-- END_FACET_NODE -->

## FACET_NODE `place::(494.9)`

- FACET: `place`
- NODE_KEY: `place::(494.9)`
- CODE: `(494.9)`
- LABEL: リヒテンシュタイン公国
- PARENT_KEY: `place::(494)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(4)` > `(494)` > `(494.9)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ ヨーロッパ ＞ スイス連邦 ＞ リヒテンシュタイン公国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(495)`

- FACET: `place`
- NODE_KEY: `place::(495)`
- CODE: `(495)`
- LABEL: ギリシャ共和国
- PARENT_KEY: `place::(4)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(4)` > `(495)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ ヨーロッパ ＞ ギリシャ共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(497)`

- FACET: `place`
- NODE_KEY: `place::(497)`
- CODE: `(497)`
- LABEL: バルカン諸国
- PARENT_KEY: `place::(4)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(4)` > `(497)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ ヨーロッパ ＞ バルカン諸国
- LEAF: false
- DIRECT_CHILDREN_COUNT: 7

### DIRECT_CHILDREN

- `place::(497.11)` | CODE `(497.11)` | セルビア共和国
- `place::(497.16)` | CODE `(497.16)` | モンテネグロ
- `place::(497.2)` | CODE `(497.2)` | ブルガリア共和国
- `place::(497.4)` | CODE `(497.4)` | スロベニア共和国
- `place::(497.5)` | CODE `(497.5)` | クロアチア共和国
- `place::(497.6)` | CODE `(497.6)` | ボスニア・ヘルツェゴビナ共和国
- `place::(497.7)` | CODE `(497.7)` | マケドニア

### INCLUDING

セルビア，モンテネグロ，ブルガリア，スロベニア，クロアチア，ボスニア・ヘルツェゴビナ，マケドニア

<!-- END_FACET_NODE -->

## FACET_NODE `place::(497.11)`

- FACET: `place`
- NODE_KEY: `place::(497.11)`
- CODE: `(497.11)`
- LABEL: セルビア共和国
- PARENT_KEY: `place::(497)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(4)` > `(497)` > `(497.11)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ ヨーロッパ ＞ バルカン諸国 ＞ セルビア共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(497.16)`

- FACET: `place`
- NODE_KEY: `place::(497.16)`
- CODE: `(497.16)`
- LABEL: モンテネグロ
- PARENT_KEY: `place::(497)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(4)` > `(497)` > `(497.16)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ ヨーロッパ ＞ バルカン諸国 ＞ モンテネグロ
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(497.2)`

- FACET: `place`
- NODE_KEY: `place::(497.2)`
- CODE: `(497.2)`
- LABEL: ブルガリア共和国
- PARENT_KEY: `place::(497)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(4)` > `(497)` > `(497.2)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ ヨーロッパ ＞ バルカン諸国 ＞ ブルガリア共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(497.4)`

- FACET: `place`
- NODE_KEY: `place::(497.4)`
- CODE: `(497.4)`
- LABEL: スロベニア共和国
- PARENT_KEY: `place::(497)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(4)` > `(497)` > `(497.4)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ ヨーロッパ ＞ バルカン諸国 ＞ スロベニア共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(497.5)`

- FACET: `place`
- NODE_KEY: `place::(497.5)`
- CODE: `(497.5)`
- LABEL: クロアチア共和国
- PARENT_KEY: `place::(497)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(4)` > `(497)` > `(497.5)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ ヨーロッパ ＞ バルカン諸国 ＞ クロアチア共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(497.6)`

- FACET: `place`
- NODE_KEY: `place::(497.6)`
- CODE: `(497.6)`
- LABEL: ボスニア・ヘルツェゴビナ共和国
- PARENT_KEY: `place::(497)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(4)` > `(497)` > `(497.6)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ ヨーロッパ ＞ バルカン諸国 ＞ ボスニア・ヘルツェゴビナ共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(497.7)`

- FACET: `place`
- NODE_KEY: `place::(497.7)`
- CODE: `(497.7)`
- LABEL: マケドニア
- PARENT_KEY: `place::(497)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(4)` > `(497)` > `(497.7)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ ヨーロッパ ＞ バルカン諸国 ＞ マケドニア
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(498)`

- FACET: `place`
- NODE_KEY: `place::(498)`
- CODE: `(498)`
- LABEL: ルーマニア共和国
- PARENT_KEY: `place::(4)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(4)` > `(498)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ ヨーロッパ ＞ ルーマニア共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(491.1)`

- FACET: `place`
- NODE_KEY: `place::(491.1)`
- CODE: `(491.1)`
- LABEL: アイスランド共和国
- PARENT_KEY: `place::(4)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(4)` > `(491.1)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ ヨーロッパ ＞ アイスランド共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(496.5)`

- FACET: `place`
- NODE_KEY: `place::(496.5)`
- CODE: `(496.5)`
- LABEL: アルバニア共和国
- PARENT_KEY: `place::(4)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(4)` > `(496.5)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ ヨーロッパ ＞ アルバニア共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(5)`

- FACET: `place`
- NODE_KEY: `place::(5)`
- CODE: `(5)`
- LABEL: アジア
- PARENT_KEY: `place::(4/9)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア
- LEAF: false
- DIRECT_CHILDREN_COUNT: 15

### DIRECT_CHILDREN

- `place::(510)` | CODE `(510)` | 中国．中華人民共和国
- `place::(512.317)` | CODE `(512.317)` | 香港
- `place::(512.318)` | CODE `(512.318)` | マカオ
- `place::(515)` | CODE `(515)` | チベット自治区
- `place::(517.9)` | CODE `(517.9)` | モンゴル
- `place::(519)` | CODE `(519)` | 朝鮮
- `place::(52)` | CODE `(52)` | 日本国および隣接諸島
- `place::(53)` | CODE `(53)` | アラブ諸国
- `place::(54)` | CODE `(54)` | インド亜大陸諸国
- `place::(55)` | CODE `(55)` | イラン・イスラム共和国
- `place::(56)` | CODE `(56)` | レバント．小アジア
- `place::(57)` | CODE `(57)` | 旧ソビエト連邦のアジア地域
- `place::(581)` | CODE `(581)` | アフガニスタン共和国
- `place::(59)` | CODE `(59)` | 南東アジア諸国と地域
- `place::(596/598)` | CODE `(596/598)` | インドシナ

<!-- END_FACET_NODE -->

## FACET_NODE `place::(510)`

- FACET: `place`
- NODE_KEY: `place::(510)`
- CODE: `(510)`
- LABEL: 中国．中華人民共和国
- PARENT_KEY: `place::(5)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(510)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 中国．中華人民共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(512.317)`

- FACET: `place`
- NODE_KEY: `place::(512.317)`
- CODE: `(512.317)`
- LABEL: 香港
- PARENT_KEY: `place::(5)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(512.317)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 香港
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(512.318)`

- FACET: `place`
- NODE_KEY: `place::(512.318)`
- CODE: `(512.318)`
- LABEL: マカオ
- PARENT_KEY: `place::(5)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(512.318)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ マカオ
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(515)`

- FACET: `place`
- NODE_KEY: `place::(515)`
- CODE: `(515)`
- LABEL: チベット自治区
- PARENT_KEY: `place::(5)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(515)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ チベット自治区
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(517.9)`

- FACET: `place`
- NODE_KEY: `place::(517.9)`
- CODE: `(517.9)`
- LABEL: モンゴル
- PARENT_KEY: `place::(5)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(517.9)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ モンゴル
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(519)`

- FACET: `place`
- NODE_KEY: `place::(519)`
- CODE: `(519)`
- LABEL: 朝鮮
- PARENT_KEY: `place::(5)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(519)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 朝鮮
- LEAF: false
- DIRECT_CHILDREN_COUNT: 2

### DIRECT_CHILDREN

- `place::(519.3)` | CODE `(519.3)` | 北朝鮮．朝鮮民主主義人民共和国
- `place::(519.5)` | CODE `(519.5)` | 韓国．大韓民国

<!-- END_FACET_NODE -->

## FACET_NODE `place::(519.3)`

- FACET: `place`
- NODE_KEY: `place::(519.3)`
- CODE: `(519.3)`
- LABEL: 北朝鮮．朝鮮民主主義人民共和国
- PARENT_KEY: `place::(519)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(519)` > `(519.3)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 朝鮮 ＞ 北朝鮮．朝鮮民主主義人民共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(519.5)`

- FACET: `place`
- NODE_KEY: `place::(519.5)`
- CODE: `(519.5)`
- LABEL: 韓国．大韓民国
- PARENT_KEY: `place::(519)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(519)` > `(519.5)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 朝鮮 ＞ 韓国．大韓民国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(52)`

- FACET: `place`
- NODE_KEY: `place::(52)`
- CODE: `(52)`
- LABEL: 日本国および隣接諸島
- PARENT_KEY: `place::(5)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島
- LEAF: false
- DIRECT_CHILDREN_COUNT: 2

### DIRECT_CHILDREN

- `place::(520)` | CODE `(520)` | 日本国
- `place::(529)` | CODE `(529)` | 台湾．中華民国

<!-- END_FACET_NODE -->

## FACET_NODE `place::(520)`

- FACET: `place`
- NODE_KEY: `place::(520)`
- CODE: `(520)`
- LABEL: 日本国
- PARENT_KEY: `place::(52)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国
- LEAF: false
- DIRECT_CHILDREN_COUNT: 6

### DIRECT_CHILDREN

- `place::(521)` | CODE `(521)` | 本州
- `place::(522)` | CODE `(522)` | 九州
- `place::(523)` | CODE `(523)` | 四国地方
- `place::(524)` | CODE `(524)` | 北海道
- `place::(527)` | CODE `(527)` | 日本本土より北の島嶼部（-1945）
- `place::(528)` | CODE `(528)` | 日本本土より南の島嶼部

### INCLUDING

本州，九州，四国，北海道，沖縄県，小笠原諸島

<!-- END_FACET_NODE -->

## FACET_NODE `place::(521)`

- FACET: `place`
- NODE_KEY: `place::(521)`
- CODE: `(521)`
- LABEL: 本州
- PARENT_KEY: `place::(520)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(521)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 本州
- LEAF: false
- DIRECT_CHILDREN_COUNT: 8

### DIRECT_CHILDREN

- `place::(521.1)` | CODE `(521.1)` | 東北地方
- `place::(521.2)` | CODE `(521.2)` | 関東地方
- `place::(521.3)` | CODE `(521.3)` | 中部地方
- `place::(521.4)` | CODE `(521.4)` | 北陸地方
- `place::(521.5)` | CODE `(521.5)` | 東山地方
- `place::(521.6)` | CODE `(521.6)` | 東海地方
- `place::(521.7)` | CODE `(521.7)` | 近畿地方
- `place::(521.8)` | CODE `(521.8)` | 中国地方

<!-- END_FACET_NODE -->

## FACET_NODE `place::(521.1)`

- FACET: `place`
- NODE_KEY: `place::(521.1)`
- CODE: `(521.1)`
- LABEL: 東北地方
- PARENT_KEY: `place::(521)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(521)` > `(521.1)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 本州 ＞ 東北地方
- LEAF: false
- DIRECT_CHILDREN_COUNT: 6

### DIRECT_CHILDREN

- `place::(521.11)` | CODE `(521.11)` | 青森県
- `place::(521.12)` | CODE `(521.12)` | 岩手県
- `place::(521.13)` | CODE `(521.13)` | 宮城県
- `place::(521.14)` | CODE `(521.14)` | 秋田県
- `place::(521.15)` | CODE `(521.15)` | 山形県
- `place::(521.16)` | CODE `(521.16)` | 福島県

<!-- END_FACET_NODE -->

## FACET_NODE `place::(521.11)`

- FACET: `place`
- NODE_KEY: `place::(521.11)`
- CODE: `(521.11)`
- LABEL: 青森県
- PARENT_KEY: `place::(521.1)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(521)` > `(521.1)` > `(521.11)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 本州 ＞ 東北地方 ＞ 青森県
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(521.12)`

- FACET: `place`
- NODE_KEY: `place::(521.12)`
- CODE: `(521.12)`
- LABEL: 岩手県
- PARENT_KEY: `place::(521.1)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(521)` > `(521.1)` > `(521.12)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 本州 ＞ 東北地方 ＞ 岩手県
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(521.13)`

- FACET: `place`
- NODE_KEY: `place::(521.13)`
- CODE: `(521.13)`
- LABEL: 宮城県
- PARENT_KEY: `place::(521.1)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(521)` > `(521.1)` > `(521.13)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 本州 ＞ 東北地方 ＞ 宮城県
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(521.14)`

- FACET: `place`
- NODE_KEY: `place::(521.14)`
- CODE: `(521.14)`
- LABEL: 秋田県
- PARENT_KEY: `place::(521.1)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(521)` > `(521.1)` > `(521.14)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 本州 ＞ 東北地方 ＞ 秋田県
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(521.15)`

- FACET: `place`
- NODE_KEY: `place::(521.15)`
- CODE: `(521.15)`
- LABEL: 山形県
- PARENT_KEY: `place::(521.1)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(521)` > `(521.1)` > `(521.15)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 本州 ＞ 東北地方 ＞ 山形県
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(521.16)`

- FACET: `place`
- NODE_KEY: `place::(521.16)`
- CODE: `(521.16)`
- LABEL: 福島県
- PARENT_KEY: `place::(521.1)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(521)` > `(521.1)` > `(521.16)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 本州 ＞ 東北地方 ＞ 福島県
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(521.2)`

- FACET: `place`
- NODE_KEY: `place::(521.2)`
- CODE: `(521.2)`
- LABEL: 関東地方
- PARENT_KEY: `place::(521)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(521)` > `(521.2)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 本州 ＞ 関東地方
- LEAF: false
- DIRECT_CHILDREN_COUNT: 7

### DIRECT_CHILDREN

- `place::(521.22)` | CODE `(521.22)` | 茨城県
- `place::(521.23)` | CODE `(521.23)` | 栃木県
- `place::(521.24)` | CODE `(521.24)` | 群馬県
- `place::(521.25)` | CODE `(521.25)` | 埼玉県
- `place::(521.27)` | CODE `(521.27)` | 東京都
- `place::(521.28)` | CODE `(521.28)` | 神奈川県
- `place::(521.29)` | CODE `(521.29)` | 千葉県

<!-- END_FACET_NODE -->

## FACET_NODE `place::(521.22)`

- FACET: `place`
- NODE_KEY: `place::(521.22)`
- CODE: `(521.22)`
- LABEL: 茨城県
- PARENT_KEY: `place::(521.2)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(521)` > `(521.2)` > `(521.22)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 本州 ＞ 関東地方 ＞ 茨城県
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(521.23)`

- FACET: `place`
- NODE_KEY: `place::(521.23)`
- CODE: `(521.23)`
- LABEL: 栃木県
- PARENT_KEY: `place::(521.2)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(521)` > `(521.2)` > `(521.23)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 本州 ＞ 関東地方 ＞ 栃木県
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(521.24)`

- FACET: `place`
- NODE_KEY: `place::(521.24)`
- CODE: `(521.24)`
- LABEL: 群馬県
- PARENT_KEY: `place::(521.2)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(521)` > `(521.2)` > `(521.24)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 本州 ＞ 関東地方 ＞ 群馬県
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(521.25)`

- FACET: `place`
- NODE_KEY: `place::(521.25)`
- CODE: `(521.25)`
- LABEL: 埼玉県
- PARENT_KEY: `place::(521.2)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(521)` > `(521.2)` > `(521.25)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 本州 ＞ 関東地方 ＞ 埼玉県
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(521.27)`

- FACET: `place`
- NODE_KEY: `place::(521.27)`
- CODE: `(521.27)`
- LABEL: 東京都
- PARENT_KEY: `place::(521.2)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(521)` > `(521.2)` > `(521.27)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 本州 ＞ 関東地方 ＞ 東京都
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(521.28)`

- FACET: `place`
- NODE_KEY: `place::(521.28)`
- CODE: `(521.28)`
- LABEL: 神奈川県
- PARENT_KEY: `place::(521.2)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(521)` > `(521.2)` > `(521.28)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 本州 ＞ 関東地方 ＞ 神奈川県
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(521.29)`

- FACET: `place`
- NODE_KEY: `place::(521.29)`
- CODE: `(521.29)`
- LABEL: 千葉県
- PARENT_KEY: `place::(521.2)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(521)` > `(521.2)` > `(521.29)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 本州 ＞ 関東地方 ＞ 千葉県
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(521.3)`

- FACET: `place`
- NODE_KEY: `place::(521.3)`
- CODE: `(521.3)`
- LABEL: 中部地方
- PARENT_KEY: `place::(521)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(521)` > `(521.3)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 本州 ＞ 中部地方
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(521.4)`

- FACET: `place`
- NODE_KEY: `place::(521.4)`
- CODE: `(521.4)`
- LABEL: 北陸地方
- PARENT_KEY: `place::(521)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(521)` > `(521.4)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 本州 ＞ 北陸地方
- LEAF: false
- DIRECT_CHILDREN_COUNT: 4

### DIRECT_CHILDREN

- `place::(521.41)` | CODE `(521.41)` | 新潟県
- `place::(521.42)` | CODE `(521.42)` | 富山県
- `place::(521.43)` | CODE `(521.43)` | 石川県
- `place::(521.44)` | CODE `(521.44)` | 福井県

<!-- END_FACET_NODE -->

## FACET_NODE `place::(521.41)`

- FACET: `place`
- NODE_KEY: `place::(521.41)`
- CODE: `(521.41)`
- LABEL: 新潟県
- PARENT_KEY: `place::(521.4)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(521)` > `(521.4)` > `(521.41)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 本州 ＞ 北陸地方 ＞ 新潟県
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(521.42)`

- FACET: `place`
- NODE_KEY: `place::(521.42)`
- CODE: `(521.42)`
- LABEL: 富山県
- PARENT_KEY: `place::(521.4)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(521)` > `(521.4)` > `(521.42)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 本州 ＞ 北陸地方 ＞ 富山県
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(521.43)`

- FACET: `place`
- NODE_KEY: `place::(521.43)`
- CODE: `(521.43)`
- LABEL: 石川県
- PARENT_KEY: `place::(521.4)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(521)` > `(521.4)` > `(521.43)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 本州 ＞ 北陸地方 ＞ 石川県
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(521.44)`

- FACET: `place`
- NODE_KEY: `place::(521.44)`
- CODE: `(521.44)`
- LABEL: 福井県
- PARENT_KEY: `place::(521.4)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(521)` > `(521.4)` > `(521.44)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 本州 ＞ 北陸地方 ＞ 福井県
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(521.5)`

- FACET: `place`
- NODE_KEY: `place::(521.5)`
- CODE: `(521.5)`
- LABEL: 東山地方
- PARENT_KEY: `place::(521)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(521)` > `(521.5)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 本州 ＞ 東山地方
- LEAF: false
- DIRECT_CHILDREN_COUNT: 3

### DIRECT_CHILDREN

- `place::(521.51)` | CODE `(521.51)` | 山梨県
- `place::(521.52)` | CODE `(521.52)` | 長野県
- `place::(521.53)` | CODE `(521.53)` | 岐阜県

<!-- END_FACET_NODE -->

## FACET_NODE `place::(521.51)`

- FACET: `place`
- NODE_KEY: `place::(521.51)`
- CODE: `(521.51)`
- LABEL: 山梨県
- PARENT_KEY: `place::(521.5)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(521)` > `(521.5)` > `(521.51)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 本州 ＞ 東山地方 ＞ 山梨県
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(521.52)`

- FACET: `place`
- NODE_KEY: `place::(521.52)`
- CODE: `(521.52)`
- LABEL: 長野県
- PARENT_KEY: `place::(521.5)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(521)` > `(521.5)` > `(521.52)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 本州 ＞ 東山地方 ＞ 長野県
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(521.53)`

- FACET: `place`
- NODE_KEY: `place::(521.53)`
- CODE: `(521.53)`
- LABEL: 岐阜県
- PARENT_KEY: `place::(521.5)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(521)` > `(521.5)` > `(521.53)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 本州 ＞ 東山地方 ＞ 岐阜県
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(521.6)`

- FACET: `place`
- NODE_KEY: `place::(521.6)`
- CODE: `(521.6)`
- LABEL: 東海地方
- PARENT_KEY: `place::(521)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(521)` > `(521.6)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 本州 ＞ 東海地方
- LEAF: false
- DIRECT_CHILDREN_COUNT: 2

### DIRECT_CHILDREN

- `place::(521.61)` | CODE `(521.61)` | 静岡県
- `place::(521.62)` | CODE `(521.62)` | 愛知県

<!-- END_FACET_NODE -->

## FACET_NODE `place::(521.61)`

- FACET: `place`
- NODE_KEY: `place::(521.61)`
- CODE: `(521.61)`
- LABEL: 静岡県
- PARENT_KEY: `place::(521.6)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(521)` > `(521.6)` > `(521.61)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 本州 ＞ 東海地方 ＞ 静岡県
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(521.62)`

- FACET: `place`
- NODE_KEY: `place::(521.62)`
- CODE: `(521.62)`
- LABEL: 愛知県
- PARENT_KEY: `place::(521.6)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(521)` > `(521.6)` > `(521.62)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 本州 ＞ 東海地方 ＞ 愛知県
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(521.7)`

- FACET: `place`
- NODE_KEY: `place::(521.7)`
- CODE: `(521.7)`
- LABEL: 近畿地方
- PARENT_KEY: `place::(521)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(521)` > `(521.7)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 本州 ＞ 近畿地方
- LEAF: false
- DIRECT_CHILDREN_COUNT: 7

### DIRECT_CHILDREN

- `place::(521.71)` | CODE `(521.71)` | 三重県
- `place::(521.72)` | CODE `(521.72)` | 滋賀県
- `place::(521.73)` | CODE `(521.73)` | 京都府
- `place::(521.74)` | CODE `(521.74)` | 大阪府
- `place::(521.75)` | CODE `(521.75)` | 兵庫県
- `place::(521.76)` | CODE `(521.76)` | 奈良県
- `place::(521.77)` | CODE `(521.77)` | 和歌山県

<!-- END_FACET_NODE -->

## FACET_NODE `place::(521.71)`

- FACET: `place`
- NODE_KEY: `place::(521.71)`
- CODE: `(521.71)`
- LABEL: 三重県
- PARENT_KEY: `place::(521.7)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(521)` > `(521.7)` > `(521.71)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 本州 ＞ 近畿地方 ＞ 三重県
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(521.72)`

- FACET: `place`
- NODE_KEY: `place::(521.72)`
- CODE: `(521.72)`
- LABEL: 滋賀県
- PARENT_KEY: `place::(521.7)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(521)` > `(521.7)` > `(521.72)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 本州 ＞ 近畿地方 ＞ 滋賀県
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(521.73)`

- FACET: `place`
- NODE_KEY: `place::(521.73)`
- CODE: `(521.73)`
- LABEL: 京都府
- PARENT_KEY: `place::(521.7)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(521)` > `(521.7)` > `(521.73)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 本州 ＞ 近畿地方 ＞ 京都府
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(521.74)`

- FACET: `place`
- NODE_KEY: `place::(521.74)`
- CODE: `(521.74)`
- LABEL: 大阪府
- PARENT_KEY: `place::(521.7)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(521)` > `(521.7)` > `(521.74)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 本州 ＞ 近畿地方 ＞ 大阪府
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(521.75)`

- FACET: `place`
- NODE_KEY: `place::(521.75)`
- CODE: `(521.75)`
- LABEL: 兵庫県
- PARENT_KEY: `place::(521.7)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(521)` > `(521.7)` > `(521.75)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 本州 ＞ 近畿地方 ＞ 兵庫県
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(521.76)`

- FACET: `place`
- NODE_KEY: `place::(521.76)`
- CODE: `(521.76)`
- LABEL: 奈良県
- PARENT_KEY: `place::(521.7)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(521)` > `(521.7)` > `(521.76)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 本州 ＞ 近畿地方 ＞ 奈良県
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(521.77)`

- FACET: `place`
- NODE_KEY: `place::(521.77)`
- CODE: `(521.77)`
- LABEL: 和歌山県
- PARENT_KEY: `place::(521.7)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(521)` > `(521.7)` > `(521.77)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 本州 ＞ 近畿地方 ＞ 和歌山県
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(521.8)`

- FACET: `place`
- NODE_KEY: `place::(521.8)`
- CODE: `(521.8)`
- LABEL: 中国地方
- PARENT_KEY: `place::(521)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(521)` > `(521.8)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 本州 ＞ 中国地方
- LEAF: false
- DIRECT_CHILDREN_COUNT: 5

### DIRECT_CHILDREN

- `place::(521.81)` | CODE `(521.81)` | 鳥取県
- `place::(521.82)` | CODE `(521.82)` | 島根県
- `place::(521.83)` | CODE `(521.83)` | 岡山県
- `place::(521.84)` | CODE `(521.84)` | 広島県
- `place::(521.85)` | CODE `(521.85)` | 山口県

<!-- END_FACET_NODE -->

## FACET_NODE `place::(521.81)`

- FACET: `place`
- NODE_KEY: `place::(521.81)`
- CODE: `(521.81)`
- LABEL: 鳥取県
- PARENT_KEY: `place::(521.8)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(521)` > `(521.8)` > `(521.81)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 本州 ＞ 中国地方 ＞ 鳥取県
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(521.82)`

- FACET: `place`
- NODE_KEY: `place::(521.82)`
- CODE: `(521.82)`
- LABEL: 島根県
- PARENT_KEY: `place::(521.8)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(521)` > `(521.8)` > `(521.82)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 本州 ＞ 中国地方 ＞ 島根県
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(521.83)`

- FACET: `place`
- NODE_KEY: `place::(521.83)`
- CODE: `(521.83)`
- LABEL: 岡山県
- PARENT_KEY: `place::(521.8)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(521)` > `(521.8)` > `(521.83)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 本州 ＞ 中国地方 ＞ 岡山県
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(521.84)`

- FACET: `place`
- NODE_KEY: `place::(521.84)`
- CODE: `(521.84)`
- LABEL: 広島県
- PARENT_KEY: `place::(521.8)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(521)` > `(521.8)` > `(521.84)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 本州 ＞ 中国地方 ＞ 広島県
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(521.85)`

- FACET: `place`
- NODE_KEY: `place::(521.85)`
- CODE: `(521.85)`
- LABEL: 山口県
- PARENT_KEY: `place::(521.8)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(521)` > `(521.8)` > `(521.85)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 本州 ＞ 中国地方 ＞ 山口県
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(522)`

- FACET: `place`
- NODE_KEY: `place::(522)`
- CODE: `(522)`
- LABEL: 九州
- PARENT_KEY: `place::(520)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(522)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 九州
- LEAF: false
- DIRECT_CHILDREN_COUNT: 7

### DIRECT_CHILDREN

- `place::(522.1)` | CODE `(522.1)` | 福岡県
- `place::(522.2)` | CODE `(522.2)` | 長崎県
- `place::(522.3)` | CODE `(522.3)` | 佐賀県
- `place::(522.5)` | CODE `(522.5)` | 熊本県
- `place::(522.6)` | CODE `(522.6)` | 大分県
- `place::(522.7)` | CODE `(522.7)` | 宮崎県
- `place::(522.8)` | CODE `(522.8)` | 鹿児島県

<!-- END_FACET_NODE -->

## FACET_NODE `place::(522.1)`

- FACET: `place`
- NODE_KEY: `place::(522.1)`
- CODE: `(522.1)`
- LABEL: 福岡県
- PARENT_KEY: `place::(522)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(522)` > `(522.1)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 九州 ＞ 福岡県
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(522.2)`

- FACET: `place`
- NODE_KEY: `place::(522.2)`
- CODE: `(522.2)`
- LABEL: 長崎県
- PARENT_KEY: `place::(522)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(522)` > `(522.2)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 九州 ＞ 長崎県
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(522.3)`

- FACET: `place`
- NODE_KEY: `place::(522.3)`
- CODE: `(522.3)`
- LABEL: 佐賀県
- PARENT_KEY: `place::(522)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(522)` > `(522.3)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 九州 ＞ 佐賀県
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(522.5)`

- FACET: `place`
- NODE_KEY: `place::(522.5)`
- CODE: `(522.5)`
- LABEL: 熊本県
- PARENT_KEY: `place::(522)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(522)` > `(522.5)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 九州 ＞ 熊本県
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(522.6)`

- FACET: `place`
- NODE_KEY: `place::(522.6)`
- CODE: `(522.6)`
- LABEL: 大分県
- PARENT_KEY: `place::(522)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(522)` > `(522.6)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 九州 ＞ 大分県
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(522.7)`

- FACET: `place`
- NODE_KEY: `place::(522.7)`
- CODE: `(522.7)`
- LABEL: 宮崎県
- PARENT_KEY: `place::(522)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(522)` > `(522.7)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 九州 ＞ 宮崎県
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(522.8)`

- FACET: `place`
- NODE_KEY: `place::(522.8)`
- CODE: `(522.8)`
- LABEL: 鹿児島県
- PARENT_KEY: `place::(522)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(522)` > `(522.8)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 九州 ＞ 鹿児島県
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(523)`

- FACET: `place`
- NODE_KEY: `place::(523)`
- CODE: `(523)`
- LABEL: 四国地方
- PARENT_KEY: `place::(520)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(523)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 四国地方
- LEAF: false
- DIRECT_CHILDREN_COUNT: 4

### DIRECT_CHILDREN

- `place::(523.1)` | CODE `(523.1)` | 徳島県
- `place::(523.2)` | CODE `(523.2)` | 香川県
- `place::(523.4)` | CODE `(523.4)` | 愛媛県
- `place::(523.5)` | CODE `(523.5)` | 高知県

<!-- END_FACET_NODE -->

## FACET_NODE `place::(523.1)`

- FACET: `place`
- NODE_KEY: `place::(523.1)`
- CODE: `(523.1)`
- LABEL: 徳島県
- PARENT_KEY: `place::(523)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(523)` > `(523.1)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 四国地方 ＞ 徳島県
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(523.2)`

- FACET: `place`
- NODE_KEY: `place::(523.2)`
- CODE: `(523.2)`
- LABEL: 香川県
- PARENT_KEY: `place::(523)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(523)` > `(523.2)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 四国地方 ＞ 香川県
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(523.4)`

- FACET: `place`
- NODE_KEY: `place::(523.4)`
- CODE: `(523.4)`
- LABEL: 愛媛県
- PARENT_KEY: `place::(523)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(523)` > `(523.4)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 四国地方 ＞ 愛媛県
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(523.5)`

- FACET: `place`
- NODE_KEY: `place::(523.5)`
- CODE: `(523.5)`
- LABEL: 高知県
- PARENT_KEY: `place::(523)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(523)` > `(523.5)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 四国地方 ＞ 高知県
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(524)`

- FACET: `place`
- NODE_KEY: `place::(524)`
- CODE: `(524)`
- LABEL: 北海道
- PARENT_KEY: `place::(520)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(524)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 北海道
- LEAF: false
- DIRECT_CHILDREN_COUNT: 15

### DIRECT_CHILDREN

- `place::(524.11)` | CODE `(524.11)` | 檜山振興局
- `place::(524.12)` | CODE `(524.12)` | 渡島総合振興局
- `place::(524.21)` | CODE `(524.21)` | 後志総合振興局
- `place::(524.22)` | CODE `(524.22)` | 胆振総合振興局
- `place::(524.31)` | CODE `(524.31)` | 石狩振興局
- `place::(524.32)` | CODE `(524.32)` | 空知総合振興局
- `place::(524.41)` | CODE `(524.41)` | 上川総合振興局
- `place::(524.42)` | CODE `(524.42)` | 留萌振興局
- `place::(524.51)` | CODE `(524.51)` | 宗谷総合振興局
- `place::(524.52)` | CODE `(524.52)` | オホーツク総合振興局
- `place::(524.61)` | CODE `(524.61)` | 日高振興局
- `place::(524.62)` | CODE `(524.62)` | 十勝総合振興局
- `place::(524.71)` | CODE `(524.71)` | 釧路総合振興局
- `place::(524.72)` | CODE `(524.72)` | 根室振興局
- `place::(524.728)` | CODE `(524.728)` | 歯舞群島・色丹島

<!-- END_FACET_NODE -->

## FACET_NODE `place::(524.11)`

- FACET: `place`
- NODE_KEY: `place::(524.11)`
- CODE: `(524.11)`
- LABEL: 檜山振興局
- PARENT_KEY: `place::(524)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(524)` > `(524.11)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 北海道 ＞ 檜山振興局
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(524.12)`

- FACET: `place`
- NODE_KEY: `place::(524.12)`
- CODE: `(524.12)`
- LABEL: 渡島総合振興局
- PARENT_KEY: `place::(524)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(524)` > `(524.12)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 北海道 ＞ 渡島総合振興局
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(524.21)`

- FACET: `place`
- NODE_KEY: `place::(524.21)`
- CODE: `(524.21)`
- LABEL: 後志総合振興局
- PARENT_KEY: `place::(524)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(524)` > `(524.21)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 北海道 ＞ 後志総合振興局
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(524.22)`

- FACET: `place`
- NODE_KEY: `place::(524.22)`
- CODE: `(524.22)`
- LABEL: 胆振総合振興局
- PARENT_KEY: `place::(524)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(524)` > `(524.22)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 北海道 ＞ 胆振総合振興局
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(524.31)`

- FACET: `place`
- NODE_KEY: `place::(524.31)`
- CODE: `(524.31)`
- LABEL: 石狩振興局
- PARENT_KEY: `place::(524)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(524)` > `(524.31)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 北海道 ＞ 石狩振興局
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(524.32)`

- FACET: `place`
- NODE_KEY: `place::(524.32)`
- CODE: `(524.32)`
- LABEL: 空知総合振興局
- PARENT_KEY: `place::(524)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(524)` > `(524.32)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 北海道 ＞ 空知総合振興局
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(524.41)`

- FACET: `place`
- NODE_KEY: `place::(524.41)`
- CODE: `(524.41)`
- LABEL: 上川総合振興局
- PARENT_KEY: `place::(524)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(524)` > `(524.41)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 北海道 ＞ 上川総合振興局
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(524.42)`

- FACET: `place`
- NODE_KEY: `place::(524.42)`
- CODE: `(524.42)`
- LABEL: 留萌振興局
- PARENT_KEY: `place::(524)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(524)` > `(524.42)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 北海道 ＞ 留萌振興局
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(524.51)`

- FACET: `place`
- NODE_KEY: `place::(524.51)`
- CODE: `(524.51)`
- LABEL: 宗谷総合振興局
- PARENT_KEY: `place::(524)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(524)` > `(524.51)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 北海道 ＞ 宗谷総合振興局
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(524.52)`

- FACET: `place`
- NODE_KEY: `place::(524.52)`
- CODE: `(524.52)`
- LABEL: オホーツク総合振興局
- PARENT_KEY: `place::(524)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(524)` > `(524.52)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 北海道 ＞ オホーツク総合振興局
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(524.61)`

- FACET: `place`
- NODE_KEY: `place::(524.61)`
- CODE: `(524.61)`
- LABEL: 日高振興局
- PARENT_KEY: `place::(524)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(524)` > `(524.61)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 北海道 ＞ 日高振興局
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(524.62)`

- FACET: `place`
- NODE_KEY: `place::(524.62)`
- CODE: `(524.62)`
- LABEL: 十勝総合振興局
- PARENT_KEY: `place::(524)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(524)` > `(524.62)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 北海道 ＞ 十勝総合振興局
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(524.71)`

- FACET: `place`
- NODE_KEY: `place::(524.71)`
- CODE: `(524.71)`
- LABEL: 釧路総合振興局
- PARENT_KEY: `place::(524)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(524)` > `(524.71)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 北海道 ＞ 釧路総合振興局
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(524.72)`

- FACET: `place`
- NODE_KEY: `place::(524.72)`
- CODE: `(524.72)`
- LABEL: 根室振興局
- PARENT_KEY: `place::(524)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(524)` > `(524.72)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 北海道 ＞ 根室振興局
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(524.728)`

- FACET: `place`
- NODE_KEY: `place::(524.728)`
- CODE: `(524.728)`
- LABEL: 歯舞群島・色丹島
- PARENT_KEY: `place::(524)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(524)` > `(524.728)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 北海道 ＞ 歯舞群島・色丹島
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(527)`

- FACET: `place`
- NODE_KEY: `place::(527)`
- CODE: `(527)`
- LABEL: 日本本土より北の島嶼部（-1945）
- PARENT_KEY: `place::(520)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(527)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 日本本土より北の島嶼部（-1945）
- LEAF: false
- DIRECT_CHILDREN_COUNT: 2

### DIRECT_CHILDREN

- `place::(527.1)` | CODE `(527.1)` | 千島列島（-1945）
- `place::(527.5)` | CODE `(527.5)` | 樺太

<!-- END_FACET_NODE -->

## FACET_NODE `place::(527.1)`

- FACET: `place`
- NODE_KEY: `place::(527.1)`
- CODE: `(527.1)`
- LABEL: 千島列島（-1945）
- PARENT_KEY: `place::(527)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(527)` > `(527.1)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 日本本土より北の島嶼部（-1945） ＞ 千島列島（-1945）
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(527.5)`

- FACET: `place`
- NODE_KEY: `place::(527.5)`
- CODE: `(527.5)`
- LABEL: 樺太
- PARENT_KEY: `place::(527)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(527)` > `(527.5)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 日本本土より北の島嶼部（-1945） ＞ 樺太
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(528)`

- FACET: `place`
- NODE_KEY: `place::(528)`
- CODE: `(528)`
- LABEL: 日本本土より南の島嶼部
- PARENT_KEY: `place::(520)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(528)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 日本本土より南の島嶼部
- LEAF: false
- DIRECT_CHILDREN_COUNT: 2

### DIRECT_CHILDREN

- `place::(528.1)` | CODE `(528.1)` | 小笠原諸島・硫黄列島
- `place::(528.3)` | CODE `(528.3)` | 琉球諸島

<!-- END_FACET_NODE -->

## FACET_NODE `place::(528.1)`

- FACET: `place`
- NODE_KEY: `place::(528.1)`
- CODE: `(528.1)`
- LABEL: 小笠原諸島・硫黄列島
- PARENT_KEY: `place::(528)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(528)` > `(528.1)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 日本本土より南の島嶼部 ＞ 小笠原諸島・硫黄列島
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(528.3)`

- FACET: `place`
- NODE_KEY: `place::(528.3)`
- CODE: `(528.3)`
- LABEL: 琉球諸島
- PARENT_KEY: `place::(528)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(520)` > `(528)` > `(528.3)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 日本国 ＞ 日本本土より南の島嶼部 ＞ 琉球諸島
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(529)`

- FACET: `place`
- NODE_KEY: `place::(529)`
- CODE: `(529)`
- LABEL: 台湾．中華民国
- PARENT_KEY: `place::(52)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(52)` > `(529)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 日本国および隣接諸島 ＞ 台湾．中華民国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(53)`

- FACET: `place`
- NODE_KEY: `place::(53)`
- CODE: `(53)`
- LABEL: アラブ諸国
- PARENT_KEY: `place::(5)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(53)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ アラブ諸国
- LEAF: false
- DIRECT_CHILDREN_COUNT: 4

### DIRECT_CHILDREN

- `place::(532)` | CODE `(532)` | サウジアラビア王国
- `place::(533)` | CODE `(533)` | イエメン共和国
- `place::(535)` | CODE `(535)` | オマーン
- `place::(536)` | CODE `(536)` | 東アラブ諸国（湾岸諸国）

<!-- END_FACET_NODE -->

## FACET_NODE `place::(532)`

- FACET: `place`
- NODE_KEY: `place::(532)`
- CODE: `(532)`
- LABEL: サウジアラビア王国
- PARENT_KEY: `place::(53)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(53)` > `(532)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ アラブ諸国 ＞ サウジアラビア王国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(533)`

- FACET: `place`
- NODE_KEY: `place::(533)`
- CODE: `(533)`
- LABEL: イエメン共和国
- PARENT_KEY: `place::(53)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(53)` > `(533)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ アラブ諸国 ＞ イエメン共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(535)`

- FACET: `place`
- NODE_KEY: `place::(535)`
- CODE: `(535)`
- LABEL: オマーン
- PARENT_KEY: `place::(53)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(53)` > `(535)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ アラブ諸国 ＞ オマーン
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(536)`

- FACET: `place`
- NODE_KEY: `place::(536)`
- CODE: `(536)`
- LABEL: 東アラブ諸国（湾岸諸国）
- PARENT_KEY: `place::(53)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(53)` > `(536)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ アラブ諸国 ＞ 東アラブ諸国（湾岸諸国）
- LEAF: false
- DIRECT_CHILDREN_COUNT: 4

### DIRECT_CHILDREN

- `place::(536.2)` | CODE `(536.2)` | アラブ首長国連邦
- `place::(536.4)` | CODE `(536.4)` | カタール
- `place::(536.5)` | CODE `(536.5)` | バーレーン王国
- `place::(536.8)` | CODE `(536.8)` | クウェート

### INCLUDING

アラブ首長国連邦，カタール，バーレーン，クウェート

<!-- END_FACET_NODE -->

## FACET_NODE `place::(536.2)`

- FACET: `place`
- NODE_KEY: `place::(536.2)`
- CODE: `(536.2)`
- LABEL: アラブ首長国連邦
- PARENT_KEY: `place::(536)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(53)` > `(536)` > `(536.2)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ アラブ諸国 ＞ 東アラブ諸国（湾岸諸国） ＞ アラブ首長国連邦
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(536.4)`

- FACET: `place`
- NODE_KEY: `place::(536.4)`
- CODE: `(536.4)`
- LABEL: カタール
- PARENT_KEY: `place::(536)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(53)` > `(536)` > `(536.4)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ アラブ諸国 ＞ 東アラブ諸国（湾岸諸国） ＞ カタール
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(536.5)`

- FACET: `place`
- NODE_KEY: `place::(536.5)`
- CODE: `(536.5)`
- LABEL: バーレーン王国
- PARENT_KEY: `place::(536)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(53)` > `(536)` > `(536.5)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ アラブ諸国 ＞ 東アラブ諸国（湾岸諸国） ＞ バーレーン王国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(536.8)`

- FACET: `place`
- NODE_KEY: `place::(536.8)`
- CODE: `(536.8)`
- LABEL: クウェート
- PARENT_KEY: `place::(536)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(53)` > `(536)` > `(536.8)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ アラブ諸国 ＞ 東アラブ諸国（湾岸諸国） ＞ クウェート
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(54)`

- FACET: `place`
- NODE_KEY: `place::(54)`
- CODE: `(54)`
- LABEL: インド亜大陸諸国
- PARENT_KEY: `place::(5)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(54)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ インド亜大陸諸国
- LEAF: false
- DIRECT_CHILDREN_COUNT: 7

### DIRECT_CHILDREN

- `place::(540)` | CODE `(540)` | インド共和国
- `place::(541.31)` | CODE `(541.31)` | ブータン王国
- `place::(541.35)` | CODE `(541.35)` | ネパール王国
- `place::(548.7)` | CODE `(548.7)` | スリランカ民主社会主義共和国
- `place::(548.82)` | CODE `(548.82)` | モルジブ共和国
- `place::(549.1)` | CODE `(549.1)` | パキスタン・イスラム共和国
- `place::(549.3)` | CODE `(549.3)` | バングラデシュ人民共和国

### INCLUDING

バングラデシュ，ブータン，インド，モルジブ，ネパール，パキスタン，スリランカ

<!-- END_FACET_NODE -->

## FACET_NODE `place::(540)`

- FACET: `place`
- NODE_KEY: `place::(540)`
- CODE: `(540)`
- LABEL: インド共和国
- PARENT_KEY: `place::(54)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(54)` > `(540)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ インド亜大陸諸国 ＞ インド共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(541.31)`

- FACET: `place`
- NODE_KEY: `place::(541.31)`
- CODE: `(541.31)`
- LABEL: ブータン王国
- PARENT_KEY: `place::(54)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(54)` > `(541.31)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ インド亜大陸諸国 ＞ ブータン王国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(541.35)`

- FACET: `place`
- NODE_KEY: `place::(541.35)`
- CODE: `(541.35)`
- LABEL: ネパール王国
- PARENT_KEY: `place::(54)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(54)` > `(541.35)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ インド亜大陸諸国 ＞ ネパール王国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(548.7)`

- FACET: `place`
- NODE_KEY: `place::(548.7)`
- CODE: `(548.7)`
- LABEL: スリランカ民主社会主義共和国
- PARENT_KEY: `place::(54)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(54)` > `(548.7)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ インド亜大陸諸国 ＞ スリランカ民主社会主義共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(548.82)`

- FACET: `place`
- NODE_KEY: `place::(548.82)`
- CODE: `(548.82)`
- LABEL: モルジブ共和国
- PARENT_KEY: `place::(54)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(54)` > `(548.82)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ インド亜大陸諸国 ＞ モルジブ共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(549.1)`

- FACET: `place`
- NODE_KEY: `place::(549.1)`
- CODE: `(549.1)`
- LABEL: パキスタン・イスラム共和国
- PARENT_KEY: `place::(54)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(54)` > `(549.1)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ インド亜大陸諸国 ＞ パキスタン・イスラム共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(549.3)`

- FACET: `place`
- NODE_KEY: `place::(549.3)`
- CODE: `(549.3)`
- LABEL: バングラデシュ人民共和国
- PARENT_KEY: `place::(54)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(54)` > `(549.3)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ インド亜大陸諸国 ＞ バングラデシュ人民共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(55)`

- FACET: `place`
- NODE_KEY: `place::(55)`
- CODE: `(55)`
- LABEL: イラン・イスラム共和国
- PARENT_KEY: `place::(5)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(55)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ イラン・イスラム共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(56)`

- FACET: `place`
- NODE_KEY: `place::(56)`
- CODE: `(56)`
- LABEL: レバント．小アジア
- PARENT_KEY: `place::(5)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(56)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ レバント．小アジア
- LEAF: false
- DIRECT_CHILDREN_COUNT: 7

### DIRECT_CHILDREN

- `place::(560)` | CODE `(560)` | トルコ共和国
- `place::(564.3)` | CODE `(564.3)` | キプロス共和国
- `place::(567)` | CODE `(567)` | イラク共和国
- `place::(569.1)` | CODE `(569.1)` | シリア・アラブ共和国
- `place::(569.3)` | CODE `(569.3)` | レバノン共和国
- `place::(569.4)` | CODE `(569.4)` | イスラエル
- `place::(569.5)` | CODE `(569.5)` | ヨルダン・ハシミテ共和国

### INCLUDING

トルコ，キプロス，イラク，シリア，レバノン，イスラエル，ヨルダン

<!-- END_FACET_NODE -->

## FACET_NODE `place::(560)`

- FACET: `place`
- NODE_KEY: `place::(560)`
- CODE: `(560)`
- LABEL: トルコ共和国
- PARENT_KEY: `place::(56)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(56)` > `(560)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ レバント．小アジア ＞ トルコ共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(564.3)`

- FACET: `place`
- NODE_KEY: `place::(564.3)`
- CODE: `(564.3)`
- LABEL: キプロス共和国
- PARENT_KEY: `place::(56)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(56)` > `(564.3)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ レバント．小アジア ＞ キプロス共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(567)`

- FACET: `place`
- NODE_KEY: `place::(567)`
- CODE: `(567)`
- LABEL: イラク共和国
- PARENT_KEY: `place::(56)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(56)` > `(567)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ レバント．小アジア ＞ イラク共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(569.1)`

- FACET: `place`
- NODE_KEY: `place::(569.1)`
- CODE: `(569.1)`
- LABEL: シリア・アラブ共和国
- PARENT_KEY: `place::(56)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(56)` > `(569.1)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ レバント．小アジア ＞ シリア・アラブ共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(569.3)`

- FACET: `place`
- NODE_KEY: `place::(569.3)`
- CODE: `(569.3)`
- LABEL: レバノン共和国
- PARENT_KEY: `place::(56)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(56)` > `(569.3)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ レバント．小アジア ＞ レバノン共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(569.4)`

- FACET: `place`
- NODE_KEY: `place::(569.4)`
- CODE: `(569.4)`
- LABEL: イスラエル
- PARENT_KEY: `place::(56)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(56)` > `(569.4)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ レバント．小アジア ＞ イスラエル
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(569.5)`

- FACET: `place`
- NODE_KEY: `place::(569.5)`
- CODE: `(569.5)`
- LABEL: ヨルダン・ハシミテ共和国
- PARENT_KEY: `place::(56)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(56)` > `(569.5)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ レバント．小アジア ＞ ヨルダン・ハシミテ共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(57)`

- FACET: `place`
- NODE_KEY: `place::(57)`
- CODE: `(57)`
- LABEL: 旧ソビエト連邦のアジア地域
- PARENT_KEY: `place::(5)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(57)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 旧ソビエト連邦のアジア地域
- LEAF: false
- DIRECT_CHILDREN_COUNT: 6

### DIRECT_CHILDREN

- `place::(571)` | CODE `(571)` | ロシア連邦のアジア地域
- `place::(574)` | CODE `(574)` | カザフスタン共和国
- `place::(575.1)` | CODE `(575.1)` | ウズベキスタン共和国
- `place::(575.2)` | CODE `(575.2)` | キルギスタン共和国
- `place::(575.3)` | CODE `(575.3)` | タジキスタン共和国
- `place::(575.4)` | CODE `(575.4)` | トルクメニスタン共和国

<!-- END_FACET_NODE -->

## FACET_NODE `place::(571)`

- FACET: `place`
- NODE_KEY: `place::(571)`
- CODE: `(571)`
- LABEL: ロシア連邦のアジア地域
- PARENT_KEY: `place::(57)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(57)` > `(571)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 旧ソビエト連邦のアジア地域 ＞ ロシア連邦のアジア地域
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(574)`

- FACET: `place`
- NODE_KEY: `place::(574)`
- CODE: `(574)`
- LABEL: カザフスタン共和国
- PARENT_KEY: `place::(57)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(57)` > `(574)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 旧ソビエト連邦のアジア地域 ＞ カザフスタン共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(575.1)`

- FACET: `place`
- NODE_KEY: `place::(575.1)`
- CODE: `(575.1)`
- LABEL: ウズベキスタン共和国
- PARENT_KEY: `place::(57)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(57)` > `(575.1)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 旧ソビエト連邦のアジア地域 ＞ ウズベキスタン共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(575.2)`

- FACET: `place`
- NODE_KEY: `place::(575.2)`
- CODE: `(575.2)`
- LABEL: キルギスタン共和国
- PARENT_KEY: `place::(57)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(57)` > `(575.2)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 旧ソビエト連邦のアジア地域 ＞ キルギスタン共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(575.3)`

- FACET: `place`
- NODE_KEY: `place::(575.3)`
- CODE: `(575.3)`
- LABEL: タジキスタン共和国
- PARENT_KEY: `place::(57)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(57)` > `(575.3)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 旧ソビエト連邦のアジア地域 ＞ タジキスタン共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(575.4)`

- FACET: `place`
- NODE_KEY: `place::(575.4)`
- CODE: `(575.4)`
- LABEL: トルクメニスタン共和国
- PARENT_KEY: `place::(57)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(57)` > `(575.4)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 旧ソビエト連邦のアジア地域 ＞ トルクメニスタン共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(581)`

- FACET: `place`
- NODE_KEY: `place::(581)`
- CODE: `(581)`
- LABEL: アフガニスタン共和国
- PARENT_KEY: `place::(5)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(581)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ アフガニスタン共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(59)`

- FACET: `place`
- NODE_KEY: `place::(59)`
- CODE: `(59)`
- LABEL: 南東アジア諸国と地域
- PARENT_KEY: `place::(5)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(59)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 南東アジア諸国と地域
- LEAF: false
- DIRECT_CHILDREN_COUNT: 7

### DIRECT_CHILDREN

- `place::(591)` | CODE `(591)` | ミャンマー(ビルマ)
- `place::(593)` | CODE `(593)` | タイ王国
- `place::(594)` | CODE `(594)` | インドネシア共和国
- `place::(595)` | CODE `(595)` | マレーシア連邦
- `place::(599)` | CODE `(599)` | フィリピン共和国
- `place::(592.3)` | CODE `(592.3)` | シンガポール共和国
- `place::(592.6)` | CODE `(592.6)` | ブルネイ

### INCLUDING

ビルマ(ミャンマー)，シンガポール，ブルネイ，インドネシア，マレーシア

<!-- END_FACET_NODE -->

## FACET_NODE `place::(591)`

- FACET: `place`
- NODE_KEY: `place::(591)`
- CODE: `(591)`
- LABEL: ミャンマー(ビルマ)
- PARENT_KEY: `place::(59)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(59)` > `(591)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 南東アジア諸国と地域 ＞ ミャンマー(ビルマ)
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(593)`

- FACET: `place`
- NODE_KEY: `place::(593)`
- CODE: `(593)`
- LABEL: タイ王国
- PARENT_KEY: `place::(59)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(59)` > `(593)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 南東アジア諸国と地域 ＞ タイ王国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(594)`

- FACET: `place`
- NODE_KEY: `place::(594)`
- CODE: `(594)`
- LABEL: インドネシア共和国
- PARENT_KEY: `place::(59)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(59)` > `(594)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 南東アジア諸国と地域 ＞ インドネシア共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(595)`

- FACET: `place`
- NODE_KEY: `place::(595)`
- CODE: `(595)`
- LABEL: マレーシア連邦
- PARENT_KEY: `place::(59)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(59)` > `(595)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 南東アジア諸国と地域 ＞ マレーシア連邦
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(599)`

- FACET: `place`
- NODE_KEY: `place::(599)`
- CODE: `(599)`
- LABEL: フィリピン共和国
- PARENT_KEY: `place::(59)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(59)` > `(599)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 南東アジア諸国と地域 ＞ フィリピン共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(592.3)`

- FACET: `place`
- NODE_KEY: `place::(592.3)`
- CODE: `(592.3)`
- LABEL: シンガポール共和国
- PARENT_KEY: `place::(59)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(59)` > `(592.3)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 南東アジア諸国と地域 ＞ シンガポール共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(592.6)`

- FACET: `place`
- NODE_KEY: `place::(592.6)`
- CODE: `(592.6)`
- LABEL: ブルネイ
- PARENT_KEY: `place::(59)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(59)` > `(592.6)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ 南東アジア諸国と地域 ＞ ブルネイ
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(596/598)`

- FACET: `place`
- NODE_KEY: `place::(596/598)`
- CODE: `(596/598)`
- LABEL: インドシナ
- PARENT_KEY: `place::(5)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(596/598)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ インドシナ
- LEAF: false
- DIRECT_CHILDREN_COUNT: 3

### DIRECT_CHILDREN

- `place::(596)` | CODE `(596)` | カンボジア王国
- `place::(597)` | CODE `(597)` | ベトナム社会主義共和国
- `place::(598)` | CODE `(598)` | ラオス人民民主共和国

### INCLUDING

カンボジア，ベトナム，ラオス

<!-- END_FACET_NODE -->

## FACET_NODE `place::(596)`

- FACET: `place`
- NODE_KEY: `place::(596)`
- CODE: `(596)`
- LABEL: カンボジア王国
- PARENT_KEY: `place::(596/598)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(596/598)` > `(596)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ インドシナ ＞ カンボジア王国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(597)`

- FACET: `place`
- NODE_KEY: `place::(597)`
- CODE: `(597)`
- LABEL: ベトナム社会主義共和国
- PARENT_KEY: `place::(596/598)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(596/598)` > `(597)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ インドシナ ＞ ベトナム社会主義共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(598)`

- FACET: `place`
- NODE_KEY: `place::(598)`
- CODE: `(598)`
- LABEL: ラオス人民民主共和国
- PARENT_KEY: `place::(596/598)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(5)` > `(596/598)` > `(598)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アジア ＞ インドシナ ＞ ラオス人民民主共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(6)`

- FACET: `place`
- NODE_KEY: `place::(6)`
- CODE: `(6)`
- LABEL: アフリカ
- PARENT_KEY: `place::(4/9)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ
- LEAF: false
- DIRECT_CHILDREN_COUNT: 11

### DIRECT_CHILDREN

- `place::(61)` | CODE `(61)` | 北アフリカ諸国．マグレブ．バーバリ
- `place::(620)` | CODE `(620)` | エジプトアラブ共和国
- `place::(624)` | CODE `(624)` | スーダン共和国．南スーダン共和国
- `place::(630)` | CODE `(630)` | エチオピア連邦民主共和国
- `place::(635)` | CODE `(635)` | エリトリア共和国
- `place::(64)` | CODE `(64)` | モロッコ王国
- `place::(65)` | CODE `(65)` | アルジェリア民主人民共和国
- `place::(66)` | CODE `(66)` | 西アフリカ諸国と地域
- `place::(67)` | CODE `(67)` | 赤道アフリカ，中央アフリカ，東アフリカ諸国および地域
- `place::(68)` | CODE `(68)` | 南部アフリカ諸国と地域
- `place::(69)` | CODE `(69)` | インド洋と南大西洋のアフリカの島々

<!-- END_FACET_NODE -->

## FACET_NODE `place::(61)`

- FACET: `place`
- NODE_KEY: `place::(61)`
- CODE: `(61)`
- LABEL: 北アフリカ諸国．マグレブ．バーバリ
- PARENT_KEY: `place::(6)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(61)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ 北アフリカ諸国．マグレブ．バーバリ
- LEAF: false
- DIRECT_CHILDREN_COUNT: 2

### DIRECT_CHILDREN

- `place::(611)` | CODE `(611)` | チュニジア共和国
- `place::(612)` | CODE `(612)` | 社会主義人民リビア・アラブ国

### INCLUDING

チュニジア，リビア，エジプト，スーダン，エチオピア，エリトリア(モロッコ)アルジェリア

<!-- END_FACET_NODE -->

## FACET_NODE `place::(611)`

- FACET: `place`
- NODE_KEY: `place::(611)`
- CODE: `(611)`
- LABEL: チュニジア共和国
- PARENT_KEY: `place::(61)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(61)` > `(611)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ 北アフリカ諸国．マグレブ．バーバリ ＞ チュニジア共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(612)`

- FACET: `place`
- NODE_KEY: `place::(612)`
- CODE: `(612)`
- LABEL: 社会主義人民リビア・アラブ国
- PARENT_KEY: `place::(61)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(61)` > `(612)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ 北アフリカ諸国．マグレブ．バーバリ ＞ 社会主義人民リビア・アラブ国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(620)`

- FACET: `place`
- NODE_KEY: `place::(620)`
- CODE: `(620)`
- LABEL: エジプトアラブ共和国
- PARENT_KEY: `place::(6)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(620)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ エジプトアラブ共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(624)`

- FACET: `place`
- NODE_KEY: `place::(624)`
- CODE: `(624)`
- LABEL: スーダン共和国．南スーダン共和国
- PARENT_KEY: `place::(6)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(624)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ スーダン共和国．南スーダン共和国
- LEAF: false
- DIRECT_CHILDREN_COUNT: 2

### DIRECT_CHILDREN

- `place::(624.1)` | CODE `(624.1)` | スーダン．アルスーダン．スーダン共和国
- `place::(624.4)` | CODE `(624.4)` | 南スーダン共和国

### SCOPE_NOTE

2011年問題解決以前のスーダン国家はここに分類．

<!-- END_FACET_NODE -->

## FACET_NODE `place::(624.1)`

- FACET: `place`
- NODE_KEY: `place::(624.1)`
- CODE: `(624.1)`
- LABEL: スーダン．アルスーダン．スーダン共和国
- PARENT_KEY: `place::(624)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(624)` > `(624.1)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ スーダン共和国．南スーダン共和国 ＞ スーダン．アルスーダン．スーダン共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(624.4)`

- FACET: `place`
- NODE_KEY: `place::(624.4)`
- CODE: `(624.4)`
- LABEL: 南スーダン共和国
- PARENT_KEY: `place::(624)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(624)` > `(624.4)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ スーダン共和国．南スーダン共和国 ＞ 南スーダン共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(630)`

- FACET: `place`
- NODE_KEY: `place::(630)`
- CODE: `(630)`
- LABEL: エチオピア連邦民主共和国
- PARENT_KEY: `place::(6)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(630)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ エチオピア連邦民主共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(635)`

- FACET: `place`
- NODE_KEY: `place::(635)`
- CODE: `(635)`
- LABEL: エリトリア共和国
- PARENT_KEY: `place::(6)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(635)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ エリトリア共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(64)`

- FACET: `place`
- NODE_KEY: `place::(64)`
- CODE: `(64)`
- LABEL: モロッコ王国
- PARENT_KEY: `place::(6)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(64)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ モロッコ王国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(65)`

- FACET: `place`
- NODE_KEY: `place::(65)`
- CODE: `(65)`
- LABEL: アルジェリア民主人民共和国
- PARENT_KEY: `place::(6)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(65)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ アルジェリア民主人民共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(66)`

- FACET: `place`
- NODE_KEY: `place::(66)`
- CODE: `(66)`
- LABEL: 西アフリカ諸国と地域
- PARENT_KEY: `place::(6)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(66)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ 西アフリカ諸国と地域
- LEAF: false
- DIRECT_CHILDREN_COUNT: 14

### DIRECT_CHILDREN

- `place::(661.2)` | CODE `(661.2)` | モーリタニア共和国
- `place::(662.1)` | CODE `(662.1)` | マリ共和国
- `place::(662.5)` | CODE `(662.5)` | ブルキナファソ民主共和国
- `place::(662.6)` | CODE `(662.6)` | ニジェール共和国
- `place::(663)` | CODE `(663)` | セネガル共和国
- `place::(664)` | CODE `(664)` | シエラレオネ共和国
- `place::(665)` | CODE `(665)` | ガンビアとギニア
- `place::(666.2)` | CODE `(666.2)` | リベリア共和国
- `place::(666.8)` | CODE `(666.8)` | コートディヴォアール共和国
- `place::(667)` | CODE `(667)` | ガーナ共和国
- `place::(668.1)` | CODE `(668.1)` | トーゴ人共和国
- `place::(668.2)` | CODE `(668.2)` | ベナン共和国
- `place::(669.1)` | CODE `(669.1)` | ナイジェリア連邦共和国
- `place::(669.95)` | CODE `(669.95)` | サントメ・プリンシペ民主共和国

### INCLUDING

モーリタニア，マリ，ブルキナファソ，ニジェール，セネガル，シエラレオネ，ガンビア，ギニア，ギニアビサウ，カーボベルデ，リベリア，コートディヴォアール，ガーナ，トーゴ，ベナン，ナイジェリア，サントメ・プリンシペ

<!-- END_FACET_NODE -->

## FACET_NODE `place::(661.2)`

- FACET: `place`
- NODE_KEY: `place::(661.2)`
- CODE: `(661.2)`
- LABEL: モーリタニア共和国
- PARENT_KEY: `place::(66)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(66)` > `(661.2)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ 西アフリカ諸国と地域 ＞ モーリタニア共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(662.1)`

- FACET: `place`
- NODE_KEY: `place::(662.1)`
- CODE: `(662.1)`
- LABEL: マリ共和国
- PARENT_KEY: `place::(66)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(66)` > `(662.1)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ 西アフリカ諸国と地域 ＞ マリ共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(662.5)`

- FACET: `place`
- NODE_KEY: `place::(662.5)`
- CODE: `(662.5)`
- LABEL: ブルキナファソ民主共和国
- PARENT_KEY: `place::(66)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(66)` > `(662.5)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ 西アフリカ諸国と地域 ＞ ブルキナファソ民主共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(662.6)`

- FACET: `place`
- NODE_KEY: `place::(662.6)`
- CODE: `(662.6)`
- LABEL: ニジェール共和国
- PARENT_KEY: `place::(66)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(66)` > `(662.6)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ 西アフリカ諸国と地域 ＞ ニジェール共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(663)`

- FACET: `place`
- NODE_KEY: `place::(663)`
- CODE: `(663)`
- LABEL: セネガル共和国
- PARENT_KEY: `place::(66)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(66)` > `(663)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ 西アフリカ諸国と地域 ＞ セネガル共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(664)`

- FACET: `place`
- NODE_KEY: `place::(664)`
- CODE: `(664)`
- LABEL: シエラレオネ共和国
- PARENT_KEY: `place::(66)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(66)` > `(664)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ 西アフリカ諸国と地域 ＞ シエラレオネ共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(665)`

- FACET: `place`
- NODE_KEY: `place::(665)`
- CODE: `(665)`
- LABEL: ガンビアとギニア
- PARENT_KEY: `place::(66)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(66)` > `(665)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ 西アフリカ諸国と地域 ＞ ガンビアとギニア
- LEAF: false
- DIRECT_CHILDREN_COUNT: 4

### DIRECT_CHILDREN

- `place::(665.1)` | CODE `(665.1)` | ガンビア共和国
- `place::(665.2)` | CODE `(665.2)` | ギニア共和国
- `place::(665.7)` | CODE `(665.7)` | ギニアビサウ共和国
- `place::(665.8)` | CODE `(665.8)` | カーボベルデ共和国

<!-- END_FACET_NODE -->

## FACET_NODE `place::(665.1)`

- FACET: `place`
- NODE_KEY: `place::(665.1)`
- CODE: `(665.1)`
- LABEL: ガンビア共和国
- PARENT_KEY: `place::(665)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(66)` > `(665)` > `(665.1)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ 西アフリカ諸国と地域 ＞ ガンビアとギニア ＞ ガンビア共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(665.2)`

- FACET: `place`
- NODE_KEY: `place::(665.2)`
- CODE: `(665.2)`
- LABEL: ギニア共和国
- PARENT_KEY: `place::(665)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(66)` > `(665)` > `(665.2)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ 西アフリカ諸国と地域 ＞ ガンビアとギニア ＞ ギニア共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(665.7)`

- FACET: `place`
- NODE_KEY: `place::(665.7)`
- CODE: `(665.7)`
- LABEL: ギニアビサウ共和国
- PARENT_KEY: `place::(665)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(66)` > `(665)` > `(665.7)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ 西アフリカ諸国と地域 ＞ ガンビアとギニア ＞ ギニアビサウ共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(665.8)`

- FACET: `place`
- NODE_KEY: `place::(665.8)`
- CODE: `(665.8)`
- LABEL: カーボベルデ共和国
- PARENT_KEY: `place::(665)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(66)` > `(665)` > `(665.8)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ 西アフリカ諸国と地域 ＞ ガンビアとギニア ＞ カーボベルデ共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(666.2)`

- FACET: `place`
- NODE_KEY: `place::(666.2)`
- CODE: `(666.2)`
- LABEL: リベリア共和国
- PARENT_KEY: `place::(66)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(66)` > `(666.2)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ 西アフリカ諸国と地域 ＞ リベリア共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(666.8)`

- FACET: `place`
- NODE_KEY: `place::(666.8)`
- CODE: `(666.8)`
- LABEL: コートディヴォアール共和国
- PARENT_KEY: `place::(66)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(66)` > `(666.8)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ 西アフリカ諸国と地域 ＞ コートディヴォアール共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(667)`

- FACET: `place`
- NODE_KEY: `place::(667)`
- CODE: `(667)`
- LABEL: ガーナ共和国
- PARENT_KEY: `place::(66)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(66)` > `(667)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ 西アフリカ諸国と地域 ＞ ガーナ共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(668.1)`

- FACET: `place`
- NODE_KEY: `place::(668.1)`
- CODE: `(668.1)`
- LABEL: トーゴ人共和国
- PARENT_KEY: `place::(66)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(66)` > `(668.1)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ 西アフリカ諸国と地域 ＞ トーゴ人共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(668.2)`

- FACET: `place`
- NODE_KEY: `place::(668.2)`
- CODE: `(668.2)`
- LABEL: ベナン共和国
- PARENT_KEY: `place::(66)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(66)` > `(668.2)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ 西アフリカ諸国と地域 ＞ ベナン共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(669.1)`

- FACET: `place`
- NODE_KEY: `place::(669.1)`
- CODE: `(669.1)`
- LABEL: ナイジェリア連邦共和国
- PARENT_KEY: `place::(66)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(66)` > `(669.1)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ 西アフリカ諸国と地域 ＞ ナイジェリア連邦共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(669.95)`

- FACET: `place`
- NODE_KEY: `place::(669.95)`
- CODE: `(669.95)`
- LABEL: サントメ・プリンシペ民主共和国
- PARENT_KEY: `place::(66)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(66)` > `(669.95)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ 西アフリカ諸国と地域 ＞ サントメ・プリンシペ民主共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(67)`

- FACET: `place`
- NODE_KEY: `place::(67)`
- CODE: `(67)`
- LABEL: 赤道アフリカ，中央アフリカ，東アフリカ諸国および地域
- PARENT_KEY: `place::(6)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(67)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ 赤道アフリカ，中央アフリカ，東アフリカ諸国および地域
- LEAF: false
- DIRECT_CHILDREN_COUNT: 14

### DIRECT_CHILDREN

- `place::(671.1)` | CODE `(671.1)` | カメルーン連邦共和国
- `place::(671.8)` | CODE `(671.8)` | 赤道ギニア共和国
- `place::(672.1)` | CODE `(672.1)` | ガボン共和国
- `place::(672.4)` | CODE `(672.4)` | コンゴ共和国
- `place::(673)` | CODE `(673)` | アンゴラ共和国
- `place::(674.1)` | CODE `(674.1)` | 中央アフリカ共和国
- `place::(674.3)` | CODE `(674.3)` | チャド共和国
- `place::(675)` | CODE `(675)` | コンゴ民主共和国
- `place::(676.1)` | CODE `(676.1)` | ウガンダ共和国
- `place::(676.2)` | CODE `(676.2)` | ケニア共和国
- `place::(677.8)` | CODE `(677.8)` | ソマリア民主共和国
- `place::(677.9)` | CODE `(677.9)` | ジブチ共和国
- `place::(678)` | CODE `(678)` | タンザニア連合共和国
- `place::(679)` | CODE `(679)` | モザンビーク共和国

### INCLUDING

カメルーン，赤道ギニア，ガボン，コンゴ(ブラザビル)，アンゴラ，中央アフリカ共和国，チャド，コンゴ民主共和国(旧ザイール)，ブルンジ，ルワンダ，ウガンダ，ケニア，ソマリア，ジブチ，タンザニア，モザンビーク

<!-- END_FACET_NODE -->

## FACET_NODE `place::(671.1)`

- FACET: `place`
- NODE_KEY: `place::(671.1)`
- CODE: `(671.1)`
- LABEL: カメルーン連邦共和国
- PARENT_KEY: `place::(67)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(67)` > `(671.1)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ 赤道アフリカ，中央アフリカ，東アフリカ諸国および地域 ＞ カメルーン連邦共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(671.8)`

- FACET: `place`
- NODE_KEY: `place::(671.8)`
- CODE: `(671.8)`
- LABEL: 赤道ギニア共和国
- PARENT_KEY: `place::(67)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(67)` > `(671.8)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ 赤道アフリカ，中央アフリカ，東アフリカ諸国および地域 ＞ 赤道ギニア共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(672.1)`

- FACET: `place`
- NODE_KEY: `place::(672.1)`
- CODE: `(672.1)`
- LABEL: ガボン共和国
- PARENT_KEY: `place::(67)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(67)` > `(672.1)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ 赤道アフリカ，中央アフリカ，東アフリカ諸国および地域 ＞ ガボン共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(672.4)`

- FACET: `place`
- NODE_KEY: `place::(672.4)`
- CODE: `(672.4)`
- LABEL: コンゴ共和国
- PARENT_KEY: `place::(67)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(67)` > `(672.4)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ 赤道アフリカ，中央アフリカ，東アフリカ諸国および地域 ＞ コンゴ共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(673)`

- FACET: `place`
- NODE_KEY: `place::(673)`
- CODE: `(673)`
- LABEL: アンゴラ共和国
- PARENT_KEY: `place::(67)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(67)` > `(673)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ 赤道アフリカ，中央アフリカ，東アフリカ諸国および地域 ＞ アンゴラ共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(674.1)`

- FACET: `place`
- NODE_KEY: `place::(674.1)`
- CODE: `(674.1)`
- LABEL: 中央アフリカ共和国
- PARENT_KEY: `place::(67)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(67)` > `(674.1)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ 赤道アフリカ，中央アフリカ，東アフリカ諸国および地域 ＞ 中央アフリカ共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(674.3)`

- FACET: `place`
- NODE_KEY: `place::(674.3)`
- CODE: `(674.3)`
- LABEL: チャド共和国
- PARENT_KEY: `place::(67)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(67)` > `(674.3)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ 赤道アフリカ，中央アフリカ，東アフリカ諸国および地域 ＞ チャド共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(675)`

- FACET: `place`
- NODE_KEY: `place::(675)`
- CODE: `(675)`
- LABEL: コンゴ民主共和国
- PARENT_KEY: `place::(67)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(67)` > `(675)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ 赤道アフリカ，中央アフリカ，東アフリカ諸国および地域 ＞ コンゴ民主共和国
- LEAF: false
- DIRECT_CHILDREN_COUNT: 2

### DIRECT_CHILDREN

- `place::(675.97)` | CODE `(675.97)` | ブルンジ共和国
- `place::(675.98)` | CODE `(675.98)` | ルワンダ共和国

<!-- END_FACET_NODE -->

## FACET_NODE `place::(675.97)`

- FACET: `place`
- NODE_KEY: `place::(675.97)`
- CODE: `(675.97)`
- LABEL: ブルンジ共和国
- PARENT_KEY: `place::(675)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(67)` > `(675)` > `(675.97)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ 赤道アフリカ，中央アフリカ，東アフリカ諸国および地域 ＞ コンゴ民主共和国 ＞ ブルンジ共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(675.98)`

- FACET: `place`
- NODE_KEY: `place::(675.98)`
- CODE: `(675.98)`
- LABEL: ルワンダ共和国
- PARENT_KEY: `place::(675)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(67)` > `(675)` > `(675.98)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ 赤道アフリカ，中央アフリカ，東アフリカ諸国および地域 ＞ コンゴ民主共和国 ＞ ルワンダ共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(676.1)`

- FACET: `place`
- NODE_KEY: `place::(676.1)`
- CODE: `(676.1)`
- LABEL: ウガンダ共和国
- PARENT_KEY: `place::(67)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(67)` > `(676.1)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ 赤道アフリカ，中央アフリカ，東アフリカ諸国および地域 ＞ ウガンダ共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(676.2)`

- FACET: `place`
- NODE_KEY: `place::(676.2)`
- CODE: `(676.2)`
- LABEL: ケニア共和国
- PARENT_KEY: `place::(67)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(67)` > `(676.2)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ 赤道アフリカ，中央アフリカ，東アフリカ諸国および地域 ＞ ケニア共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(677.8)`

- FACET: `place`
- NODE_KEY: `place::(677.8)`
- CODE: `(677.8)`
- LABEL: ソマリア民主共和国
- PARENT_KEY: `place::(67)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(67)` > `(677.8)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ 赤道アフリカ，中央アフリカ，東アフリカ諸国および地域 ＞ ソマリア民主共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(677.9)`

- FACET: `place`
- NODE_KEY: `place::(677.9)`
- CODE: `(677.9)`
- LABEL: ジブチ共和国
- PARENT_KEY: `place::(67)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(67)` > `(677.9)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ 赤道アフリカ，中央アフリカ，東アフリカ諸国および地域 ＞ ジブチ共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(678)`

- FACET: `place`
- NODE_KEY: `place::(678)`
- CODE: `(678)`
- LABEL: タンザニア連合共和国
- PARENT_KEY: `place::(67)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(67)` > `(678)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ 赤道アフリカ，中央アフリカ，東アフリカ諸国および地域 ＞ タンザニア連合共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(679)`

- FACET: `place`
- NODE_KEY: `place::(679)`
- CODE: `(679)`
- LABEL: モザンビーク共和国
- PARENT_KEY: `place::(67)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(67)` > `(679)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ 赤道アフリカ，中央アフリカ，東アフリカ諸国および地域 ＞ モザンビーク共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(68)`

- FACET: `place`
- NODE_KEY: `place::(68)`
- CODE: `(68)`
- LABEL: 南部アフリカ諸国と地域
- PARENT_KEY: `place::(6)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(68)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ 南部アフリカ諸国と地域
- LEAF: false
- DIRECT_CHILDREN_COUNT: 8

### DIRECT_CHILDREN

- `place::(680)` | CODE `(680)` | 南アフリカ共和国
- `place::(688.1)` | CODE `(688.1)` | ナミビア共和国
- `place::(688.3)` | CODE `(688.3)` | ボツワナ共和国
- `place::(688.5)` | CODE `(688.5)` | レソト王国
- `place::(688.7)` | CODE `(688.7)` | スワジランド王国
- `place::(689.1)` | CODE `(689.1)` | ジンバブエ共和国
- `place::(689.4)` | CODE `(689.4)` | ザンビア共和国
- `place::(689.7)` | CODE `(689.7)` | マラウイ共和国

### INCLUDING

南アフリカ，ナミビア，ボツワナ，レソト，スワジランド，ジンバブエ，ザンビア，マラウィ

<!-- END_FACET_NODE -->

## FACET_NODE `place::(680)`

- FACET: `place`
- NODE_KEY: `place::(680)`
- CODE: `(680)`
- LABEL: 南アフリカ共和国
- PARENT_KEY: `place::(68)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(68)` > `(680)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ 南部アフリカ諸国と地域 ＞ 南アフリカ共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(688.1)`

- FACET: `place`
- NODE_KEY: `place::(688.1)`
- CODE: `(688.1)`
- LABEL: ナミビア共和国
- PARENT_KEY: `place::(68)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(68)` > `(688.1)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ 南部アフリカ諸国と地域 ＞ ナミビア共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(688.3)`

- FACET: `place`
- NODE_KEY: `place::(688.3)`
- CODE: `(688.3)`
- LABEL: ボツワナ共和国
- PARENT_KEY: `place::(68)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(68)` > `(688.3)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ 南部アフリカ諸国と地域 ＞ ボツワナ共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(688.5)`

- FACET: `place`
- NODE_KEY: `place::(688.5)`
- CODE: `(688.5)`
- LABEL: レソト王国
- PARENT_KEY: `place::(68)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(68)` > `(688.5)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ 南部アフリカ諸国と地域 ＞ レソト王国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(688.7)`

- FACET: `place`
- NODE_KEY: `place::(688.7)`
- CODE: `(688.7)`
- LABEL: スワジランド王国
- PARENT_KEY: `place::(68)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(68)` > `(688.7)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ 南部アフリカ諸国と地域 ＞ スワジランド王国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(689.1)`

- FACET: `place`
- NODE_KEY: `place::(689.1)`
- CODE: `(689.1)`
- LABEL: ジンバブエ共和国
- PARENT_KEY: `place::(68)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(68)` > `(689.1)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ 南部アフリカ諸国と地域 ＞ ジンバブエ共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(689.4)`

- FACET: `place`
- NODE_KEY: `place::(689.4)`
- CODE: `(689.4)`
- LABEL: ザンビア共和国
- PARENT_KEY: `place::(68)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(68)` > `(689.4)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ 南部アフリカ諸国と地域 ＞ ザンビア共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(689.7)`

- FACET: `place`
- NODE_KEY: `place::(689.7)`
- CODE: `(689.7)`
- LABEL: マラウイ共和国
- PARENT_KEY: `place::(68)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(68)` > `(689.7)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ 南部アフリカ諸国と地域 ＞ マラウイ共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(69)`

- FACET: `place`
- NODE_KEY: `place::(69)`
- CODE: `(69)`
- LABEL: インド洋と南大西洋のアフリカの島々
- PARENT_KEY: `place::(6)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(69)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ インド洋と南大西洋のアフリカの島々
- LEAF: false
- DIRECT_CHILDREN_COUNT: 6

### DIRECT_CHILDREN

- `place::(691)` | CODE `(691)` | マダガスカル民主共和国
- `place::(694)` | CODE `(694)` | マダガスカル北方の諸島
- `place::(696)` | CODE `(696)` | セイシェル共和国
- `place::(697)` | CODE `(697)` | イギリスのインド洋領土(BIOT)(イギリス)
- `place::(698)` | CODE `(698)` | マスカリン諸島
- `place::(699)` | CODE `(699)` | 南インド洋，南大西洋海洋に散在する島々

### INCLUDING

マダガスカル，コモロ，マイヨット，セイシェル，イギリスのインド洋領土(イギリス)，レユニオン(フランス)，モーリシャス，南インド・南大西洋海洋の離れ島

<!-- END_FACET_NODE -->

## FACET_NODE `place::(691)`

- FACET: `place`
- NODE_KEY: `place::(691)`
- CODE: `(691)`
- LABEL: マダガスカル民主共和国
- PARENT_KEY: `place::(69)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(69)` > `(691)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ インド洋と南大西洋のアフリカの島々 ＞ マダガスカル民主共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(694)`

- FACET: `place`
- NODE_KEY: `place::(694)`
- CODE: `(694)`
- LABEL: マダガスカル北方の諸島
- PARENT_KEY: `place::(69)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(69)` > `(694)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ インド洋と南大西洋のアフリカの島々 ＞ マダガスカル北方の諸島
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

### INCLUDING

コモロ，マイヨット(フランス)

<!-- END_FACET_NODE -->

## FACET_NODE `place::(696)`

- FACET: `place`
- NODE_KEY: `place::(696)`
- CODE: `(696)`
- LABEL: セイシェル共和国
- PARENT_KEY: `place::(69)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(69)` > `(696)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ インド洋と南大西洋のアフリカの島々 ＞ セイシェル共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

### INCLUDING

マヘ島，プラスリン島，シルエット島，ラ・ディーグ島，ノース島，キュリウーズ島，デロシュ島，ファーカー諸島，サーフ島，プロヴィデンス島，サン・ピエール島，コスモレド諸島，アルダブラ島，アサンプション島，アストヴ島

<!-- END_FACET_NODE -->

## FACET_NODE `place::(697)`

- FACET: `place`
- NODE_KEY: `place::(697)`
- CODE: `(697)`
- LABEL: イギリスのインド洋領土(BIOT)(イギリス)
- PARENT_KEY: `place::(69)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(69)` > `(697)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ インド洋と南大西洋のアフリカの島々 ＞ イギリスのインド洋領土(BIOT)(イギリス)
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

### INCLUDING

チャゴス諸島，デインジャー島，ディアゴ・ガルシア，イーグル，ペロス・バニョス，サロモン，シックス諸島(エグモント諸島)，スリーブラザーズ(トロワ・フレール)

<!-- END_FACET_NODE -->

## FACET_NODE `place::(698)`

- FACET: `place`
- NODE_KEY: `place::(698)`
- CODE: `(698)`
- LABEL: マスカリン諸島
- PARENT_KEY: `place::(69)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(69)` > `(698)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ インド洋と南大西洋のアフリカの島々 ＞ マスカリン諸島
- LEAF: false
- DIRECT_CHILDREN_COUNT: 2

### DIRECT_CHILDREN

- `place::(698.1)` | CODE `(698.1)` | レユニオン(フランス)
- `place::(698.2)` | CODE `(698.2)` | モーリシャス共和国

### INCLUDING

レユニオン(フランス)，モーリシャス

<!-- END_FACET_NODE -->

## FACET_NODE `place::(698.1)`

- FACET: `place`
- NODE_KEY: `place::(698.1)`
- CODE: `(698.1)`
- LABEL: レユニオン(フランス)
- PARENT_KEY: `place::(698)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(69)` > `(698)` > `(698.1)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ インド洋と南大西洋のアフリカの島々 ＞ マスカリン諸島 ＞ レユニオン(フランス)
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(698.2)`

- FACET: `place`
- NODE_KEY: `place::(698.2)`
- CODE: `(698.2)`
- LABEL: モーリシャス共和国
- PARENT_KEY: `place::(698)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(69)` > `(698)` > `(698.2)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ インド洋と南大西洋のアフリカの島々 ＞ マスカリン諸島 ＞ モーリシャス共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(699)`

- FACET: `place`
- NODE_KEY: `place::(699)`
- CODE: `(699)`
- LABEL: 南インド洋，南大西洋海洋に散在する島々
- PARENT_KEY: `place::(69)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(6)` > `(69)` > `(699)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アフリカ ＞ インド洋と南大西洋のアフリカの島々 ＞ 南インド洋，南大西洋海洋に散在する島々
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

### INCLUDING

セントヘレナ，アセンション，トリスタン・ダ・クーニャ（イギリス）

<!-- END_FACET_NODE -->

## FACET_NODE `place::(7/8)`

- FACET: `place`
- NODE_KEY: `place::(7/8)`
- CODE: `(7/8)`
- LABEL: アメリカ．南北アメリカ大陸
- PARENT_KEY: `place::(4/9)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸
- LEAF: false
- DIRECT_CHILDREN_COUNT: 2

### DIRECT_CHILDREN

- `place::(7)` | CODE `(7)` | 北アメリカおよび中央アメリカ
- `place::(8)` | CODE `(8)` | 南アメリカ．南米諸国と地域．ラテンアメリカ

<!-- END_FACET_NODE -->

## FACET_NODE `place::(7)`

- FACET: `place`
- NODE_KEY: `place::(7)`
- CODE: `(7)`
- LABEL: 北アメリカおよび中央アメリカ
- PARENT_KEY: `place::(7/8)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(7)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 北アメリカおよび中央アメリカ
- LEAF: false
- DIRECT_CHILDREN_COUNT: 3

### DIRECT_CHILDREN

- `place::(71)` | CODE `(71)` | カナダ
- `place::(72)` | CODE `(72)` | メキシコ．中央アメリカ諸国．カリブ海地域
- `place::(73)` | CODE `(73)` | アメリカ合衆国

<!-- END_FACET_NODE -->

## FACET_NODE `place::(71)`

- FACET: `place`
- NODE_KEY: `place::(71)`
- CODE: `(71)`
- LABEL: カナダ
- PARENT_KEY: `place::(7)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(7)` > `(71)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 北アメリカおよび中央アメリカ ＞ カナダ
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(72)`

- FACET: `place`
- NODE_KEY: `place::(72)`
- CODE: `(72)`
- LABEL: メキシコ．中央アメリカ諸国．カリブ海地域
- PARENT_KEY: `place::(7)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(7)` > `(72)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 北アメリカおよび中央アメリカ ＞ メキシコ．中央アメリカ諸国．カリブ海地域
- LEAF: false
- DIRECT_CHILDREN_COUNT: 3

### DIRECT_CHILDREN

- `place::(721/727)` | CODE `(721/727)` | メキシコ合衆国
- `place::(728)` | CODE `(728)` | 中央アメリカ諸国
- `place::(729)` | CODE `(729)` | カリブ海地域．西インド諸島(アンティル諸島)

<!-- END_FACET_NODE -->

## FACET_NODE `place::(721/727)`

- FACET: `place`
- NODE_KEY: `place::(721/727)`
- CODE: `(721/727)`
- LABEL: メキシコ合衆国
- PARENT_KEY: `place::(72)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(7)` > `(72)` > `(721/727)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 北アメリカおよび中央アメリカ ＞ メキシコ．中央アメリカ諸国．カリブ海地域 ＞ メキシコ合衆国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(728)`

- FACET: `place`
- NODE_KEY: `place::(728)`
- CODE: `(728)`
- LABEL: 中央アメリカ諸国
- PARENT_KEY: `place::(72)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(7)` > `(72)` > `(728)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 北アメリカおよび中央アメリカ ＞ メキシコ．中央アメリカ諸国．カリブ海地域 ＞ 中央アメリカ諸国
- LEAF: false
- DIRECT_CHILDREN_COUNT: 7

### DIRECT_CHILDREN

- `place::(728.1)` | CODE `(728.1)` | グアテマラ共和国
- `place::(728.2)` | CODE `(728.2)` | ベリーズ
- `place::(728.3)` | CODE `(728.3)` | ホンジュラス共和国
- `place::(728.4)` | CODE `(728.4)` | エルサルバドル共和国
- `place::(728.5)` | CODE `(728.5)` | ニカラグア共和国
- `place::(728.6)` | CODE `(728.6)` | コスタリカ共和国
- `place::(728.7)` | CODE `(728.7)` | パナマ共和国

### INCLUDING

グアテマラ，ベリーズ，ホンジュラス，エルサルバドル，ニカラグア，コスタリカ，パナマ

<!-- END_FACET_NODE -->

## FACET_NODE `place::(728.1)`

- FACET: `place`
- NODE_KEY: `place::(728.1)`
- CODE: `(728.1)`
- LABEL: グアテマラ共和国
- PARENT_KEY: `place::(728)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(7)` > `(72)` > `(728)` > `(728.1)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 北アメリカおよび中央アメリカ ＞ メキシコ．中央アメリカ諸国．カリブ海地域 ＞ 中央アメリカ諸国 ＞ グアテマラ共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(728.2)`

- FACET: `place`
- NODE_KEY: `place::(728.2)`
- CODE: `(728.2)`
- LABEL: ベリーズ
- PARENT_KEY: `place::(728)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(7)` > `(72)` > `(728)` > `(728.2)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 北アメリカおよび中央アメリカ ＞ メキシコ．中央アメリカ諸国．カリブ海地域 ＞ 中央アメリカ諸国 ＞ ベリーズ
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(728.3)`

- FACET: `place`
- NODE_KEY: `place::(728.3)`
- CODE: `(728.3)`
- LABEL: ホンジュラス共和国
- PARENT_KEY: `place::(728)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(7)` > `(72)` > `(728)` > `(728.3)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 北アメリカおよび中央アメリカ ＞ メキシコ．中央アメリカ諸国．カリブ海地域 ＞ 中央アメリカ諸国 ＞ ホンジュラス共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(728.4)`

- FACET: `place`
- NODE_KEY: `place::(728.4)`
- CODE: `(728.4)`
- LABEL: エルサルバドル共和国
- PARENT_KEY: `place::(728)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(7)` > `(72)` > `(728)` > `(728.4)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 北アメリカおよび中央アメリカ ＞ メキシコ．中央アメリカ諸国．カリブ海地域 ＞ 中央アメリカ諸国 ＞ エルサルバドル共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(728.5)`

- FACET: `place`
- NODE_KEY: `place::(728.5)`
- CODE: `(728.5)`
- LABEL: ニカラグア共和国
- PARENT_KEY: `place::(728)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(7)` > `(72)` > `(728)` > `(728.5)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 北アメリカおよび中央アメリカ ＞ メキシコ．中央アメリカ諸国．カリブ海地域 ＞ 中央アメリカ諸国 ＞ ニカラグア共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(728.6)`

- FACET: `place`
- NODE_KEY: `place::(728.6)`
- CODE: `(728.6)`
- LABEL: コスタリカ共和国
- PARENT_KEY: `place::(728)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(7)` > `(72)` > `(728)` > `(728.6)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 北アメリカおよび中央アメリカ ＞ メキシコ．中央アメリカ諸国．カリブ海地域 ＞ 中央アメリカ諸国 ＞ コスタリカ共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(728.7)`

- FACET: `place`
- NODE_KEY: `place::(728.7)`
- CODE: `(728.7)`
- LABEL: パナマ共和国
- PARENT_KEY: `place::(728)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(7)` > `(72)` > `(728)` > `(728.7)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 北アメリカおよび中央アメリカ ＞ メキシコ．中央アメリカ諸国．カリブ海地域 ＞ 中央アメリカ諸国 ＞ パナマ共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(729)`

- FACET: `place`
- NODE_KEY: `place::(729)`
- CODE: `(729)`
- LABEL: カリブ海地域．西インド諸島(アンティル諸島)
- PARENT_KEY: `place::(72)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(7)` > `(72)` > `(729)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 北アメリカおよび中央アメリカ ＞ メキシコ．中央アメリカ諸国．カリブ海地域 ＞ カリブ海地域．西インド諸島(アンティル諸島)
- LEAF: false
- DIRECT_CHILDREN_COUNT: 3

### DIRECT_CHILDREN

- `place::(729.1/.5)` | CODE `(729.1/.5)` | 大アンテｨル諸島
- `place::(729.7/.8)` | CODE `(729.7/.8)` | 小アンティル(東カリブ海)
- `place::(729.9)` | CODE `(729.9)` | バミューダ(ソマーク諸島)UK)

### INCLUDING

キューバ，ジャマイカ，ケイマン諸島(イギリス)，ドミニカ共和国，ハイチ，プエルトリコ，バハマ，タークス・カイコス，ヴァージン諸島，セントクリストファー・ネイビス，アンギラ，アンティグア・バーブーダ，モントセラット，グアドループ，マルティニーク，ドミニカ，セントルシア，セントヴィンセント・グレナディーン，グレナダ，バルバドス，トリニダード・トバゴ，オランダ領アンティル諸島，アルバ，バミューダ

<!-- END_FACET_NODE -->

## FACET_NODE `place::(729.1/.5)`

- FACET: `place`
- NODE_KEY: `place::(729.1/.5)`
- CODE: `(729.1/.5)`
- LABEL: 大アンテｨル諸島
- PARENT_KEY: `place::(729)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(7)` > `(72)` > `(729)` > `(729.1/.5)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 北アメリカおよび中央アメリカ ＞ メキシコ．中央アメリカ諸国．カリブ海地域 ＞ カリブ海地域．西インド諸島(アンティル諸島) ＞ 大アンテｨル諸島
- LEAF: false
- DIRECT_CHILDREN_COUNT: 5

### DIRECT_CHILDREN

- `place::(729.1)` | CODE `(729.1)` | キューバ共和国
- `place::(729.2)` | CODE `(729.2)` | ジャマイカ
- `place::(729.3/.4)` | CODE `(729.3/.4)` | イスパニョーラ島
- `place::(729.5)` | CODE `(729.5)` | プエルトリコ連邦(USA)
- `place::(729.68)` | CODE `(729.68)` | タークス・カイコス島(UK)

<!-- END_FACET_NODE -->

## FACET_NODE `place::(729.1)`

- FACET: `place`
- NODE_KEY: `place::(729.1)`
- CODE: `(729.1)`
- LABEL: キューバ共和国
- PARENT_KEY: `place::(729.1/.5)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(7)` > `(72)` > `(729)` > `(729.1/.5)` > `(729.1)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 北アメリカおよび中央アメリカ ＞ メキシコ．中央アメリカ諸国．カリブ海地域 ＞ カリブ海地域．西インド諸島(アンティル諸島) ＞ 大アンテｨル諸島 ＞ キューバ共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(729.2)`

- FACET: `place`
- NODE_KEY: `place::(729.2)`
- CODE: `(729.2)`
- LABEL: ジャマイカ
- PARENT_KEY: `place::(729.1/.5)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(7)` > `(72)` > `(729)` > `(729.1/.5)` > `(729.2)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 北アメリカおよび中央アメリカ ＞ メキシコ．中央アメリカ諸国．カリブ海地域 ＞ カリブ海地域．西インド諸島(アンティル諸島) ＞ 大アンテｨル諸島 ＞ ジャマイカ
- LEAF: false
- DIRECT_CHILDREN_COUNT: 1

### DIRECT_CHILDREN

- `place::(729.29)` | CODE `(729.29)` | ケイマン島（英国）

<!-- END_FACET_NODE -->

## FACET_NODE `place::(729.29)`

- FACET: `place`
- NODE_KEY: `place::(729.29)`
- CODE: `(729.29)`
- LABEL: ケイマン島（英国）
- PARENT_KEY: `place::(729.2)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(7)` > `(72)` > `(729)` > `(729.1/.5)` > `(729.2)` > `(729.29)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 北アメリカおよび中央アメリカ ＞ メキシコ．中央アメリカ諸国．カリブ海地域 ＞ カリブ海地域．西インド諸島(アンティル諸島) ＞ 大アンテｨル諸島 ＞ ジャマイカ ＞ ケイマン島（英国）
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(729.3/.4)`

- FACET: `place`
- NODE_KEY: `place::(729.3/.4)`
- CODE: `(729.3/.4)`
- LABEL: イスパニョーラ島
- PARENT_KEY: `place::(729.1/.5)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(7)` > `(72)` > `(729)` > `(729.1/.5)` > `(729.3/.4)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 北アメリカおよび中央アメリカ ＞ メキシコ．中央アメリカ諸国．カリブ海地域 ＞ カリブ海地域．西インド諸島(アンティル諸島) ＞ 大アンテｨル諸島 ＞ イスパニョーラ島
- LEAF: false
- DIRECT_CHILDREN_COUNT: 2

### DIRECT_CHILDREN

- `place::(729.3)` | CODE `(729.3)` | ドミニカ共和国
- `place::(729.4)` | CODE `(729.4)` | ハイチ．ハイチ共和国

<!-- END_FACET_NODE -->

## FACET_NODE `place::(729.3)`

- FACET: `place`
- NODE_KEY: `place::(729.3)`
- CODE: `(729.3)`
- LABEL: ドミニカ共和国
- PARENT_KEY: `place::(729.3/.4)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(7)` > `(72)` > `(729)` > `(729.1/.5)` > `(729.3/.4)` > `(729.3)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 北アメリカおよび中央アメリカ ＞ メキシコ．中央アメリカ諸国．カリブ海地域 ＞ カリブ海地域．西インド諸島(アンティル諸島) ＞ 大アンテｨル諸島 ＞ イスパニョーラ島 ＞ ドミニカ共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(729.4)`

- FACET: `place`
- NODE_KEY: `place::(729.4)`
- CODE: `(729.4)`
- LABEL: ハイチ．ハイチ共和国
- PARENT_KEY: `place::(729.3/.4)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(7)` > `(72)` > `(729)` > `(729.1/.5)` > `(729.3/.4)` > `(729.4)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 北アメリカおよび中央アメリカ ＞ メキシコ．中央アメリカ諸国．カリブ海地域 ＞ カリブ海地域．西インド諸島(アンティル諸島) ＞ 大アンテｨル諸島 ＞ イスパニョーラ島 ＞ ハイチ．ハイチ共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(729.5)`

- FACET: `place`
- NODE_KEY: `place::(729.5)`
- CODE: `(729.5)`
- LABEL: プエルトリコ連邦(USA)
- PARENT_KEY: `place::(729.1/.5)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(7)` > `(72)` > `(729)` > `(729.1/.5)` > `(729.5)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 北アメリカおよび中央アメリカ ＞ メキシコ．中央アメリカ諸国．カリブ海地域 ＞ カリブ海地域．西インド諸島(アンティル諸島) ＞ 大アンテｨル諸島 ＞ プエルトリコ連邦(USA)
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(729.68)`

- FACET: `place`
- NODE_KEY: `place::(729.68)`
- CODE: `(729.68)`
- LABEL: タークス・カイコス島(UK)
- PARENT_KEY: `place::(729.1/.5)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(7)` > `(72)` > `(729)` > `(729.1/.5)` > `(729.68)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 北アメリカおよび中央アメリカ ＞ メキシコ．中央アメリカ諸国．カリブ海地域 ＞ カリブ海地域．西インド諸島(アンティル諸島) ＞ 大アンテｨル諸島 ＞ タークス・カイコス島(UK)
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(729.7/.8)`

- FACET: `place`
- NODE_KEY: `place::(729.7/.8)`
- CODE: `(729.7/.8)`
- LABEL: 小アンティル(東カリブ海)
- PARENT_KEY: `place::(729)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(7)` > `(72)` > `(729)` > `(729.7/.8)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 北アメリカおよび中央アメリカ ＞ メキシコ．中央アメリカ諸国．カリブ海地域 ＞ カリブ海地域．西インド諸島(アンティル諸島) ＞ 小アンティル(東カリブ海)
- LEAF: false
- DIRECT_CHILDREN_COUNT: 2

### DIRECT_CHILDREN

- `place::(729.7)` | CODE `(729.7)` | リーワード諸島
- `place::(729.8)` | CODE `(729.8)` | ウインドワード諸島

<!-- END_FACET_NODE -->

## FACET_NODE `place::(729.7)`

- FACET: `place`
- NODE_KEY: `place::(729.7)`
- CODE: `(729.7)`
- LABEL: リーワード諸島
- PARENT_KEY: `place::(729.7/.8)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(7)` > `(72)` > `(729)` > `(729.7/.8)` > `(729.7)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 北アメリカおよび中央アメリカ ＞ メキシコ．中央アメリカ諸国．カリブ海地域 ＞ カリブ海地域．西インド諸島(アンティル諸島) ＞ 小アンティル(東カリブ海) ＞ リーワード諸島
- LEAF: false
- DIRECT_CHILDREN_COUNT: 5

### DIRECT_CHILDREN

- `place::(729.71)` | CODE `(729.71)` | 米国領ヴァージン諸島(アメリカのヴァージン諸島)(USA)
- `place::(729.724)` | CODE `(729.724)` | セントキッツ-ネヴィス,セントキッツ-ネヴィス連邦
- `place::(729.726)` | CODE `(729.726)` | アンティグア・バーブーダ
- `place::(729.727)` | CODE `(729.727)` | モントセラト(UK)
- `place::(729.74)` | CODE `(729.74)` | 小アンティルのフランス領土

<!-- END_FACET_NODE -->

## FACET_NODE `place::(729.71)`

- FACET: `place`
- NODE_KEY: `place::(729.71)`
- CODE: `(729.71)`
- LABEL: 米国領ヴァージン諸島(アメリカのヴァージン諸島)(USA)
- PARENT_KEY: `place::(729.7)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(7)` > `(72)` > `(729)` > `(729.7/.8)` > `(729.7)` > `(729.71)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 北アメリカおよび中央アメリカ ＞ メキシコ．中央アメリカ諸国．カリブ海地域 ＞ カリブ海地域．西インド諸島(アンティル諸島) ＞ 小アンティル(東カリブ海) ＞ リーワード諸島 ＞ 米国領ヴァージン諸島(アメリカのヴァージン諸島)(USA)
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(729.724)`

- FACET: `place`
- NODE_KEY: `place::(729.724)`
- CODE: `(729.724)`
- LABEL: セントキッツ-ネヴィス,セントキッツ-ネヴィス連邦
- PARENT_KEY: `place::(729.7)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(7)` > `(72)` > `(729)` > `(729.7/.8)` > `(729.7)` > `(729.724)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 北アメリカおよび中央アメリカ ＞ メキシコ．中央アメリカ諸国．カリブ海地域 ＞ カリブ海地域．西インド諸島(アンティル諸島) ＞ 小アンティル(東カリブ海) ＞ リーワード諸島 ＞ セントキッツ-ネヴィス,セントキッツ-ネヴィス連邦
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(729.726)`

- FACET: `place`
- NODE_KEY: `place::(729.726)`
- CODE: `(729.726)`
- LABEL: アンティグア・バーブーダ
- PARENT_KEY: `place::(729.7)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(7)` > `(72)` > `(729)` > `(729.7/.8)` > `(729.7)` > `(729.726)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 北アメリカおよび中央アメリカ ＞ メキシコ．中央アメリカ諸国．カリブ海地域 ＞ カリブ海地域．西インド諸島(アンティル諸島) ＞ 小アンティル(東カリブ海) ＞ リーワード諸島 ＞ アンティグア・バーブーダ
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(729.727)`

- FACET: `place`
- NODE_KEY: `place::(729.727)`
- CODE: `(729.727)`
- LABEL: モントセラト(UK)
- PARENT_KEY: `place::(729.7)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(7)` > `(72)` > `(729)` > `(729.7/.8)` > `(729.7)` > `(729.727)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 北アメリカおよび中央アメリカ ＞ メキシコ．中央アメリカ諸国．カリブ海地域 ＞ カリブ海地域．西インド諸島(アンティル諸島) ＞ 小アンティル(東カリブ海) ＞ リーワード諸島 ＞ モントセラト(UK)
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(729.74)`

- FACET: `place`
- NODE_KEY: `place::(729.74)`
- CODE: `(729.74)`
- LABEL: 小アンティルのフランス領土
- PARENT_KEY: `place::(729.7)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(7)` > `(72)` > `(729)` > `(729.7/.8)` > `(729.7)` > `(729.74)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 北アメリカおよび中央アメリカ ＞ メキシコ．中央アメリカ諸国．カリブ海地域 ＞ カリブ海地域．西インド諸島(アンティル諸島) ＞ 小アンティル(東カリブ海) ＞ リーワード諸島 ＞ 小アンティルのフランス領土
- LEAF: false
- DIRECT_CHILDREN_COUNT: 2

### DIRECT_CHILDREN

- `place::(729.741)` | CODE `(729.741)` | グアドループ(地域と部門)(フランス)
- `place::(729.745)` | CODE `(729.745)` | マルチニーク(地域と部門)(フランス)

<!-- END_FACET_NODE -->

## FACET_NODE `place::(729.741)`

- FACET: `place`
- NODE_KEY: `place::(729.741)`
- CODE: `(729.741)`
- LABEL: グアドループ(地域と部門)(フランス)
- PARENT_KEY: `place::(729.74)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(7)` > `(72)` > `(729)` > `(729.7/.8)` > `(729.7)` > `(729.74)` > `(729.741)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 北アメリカおよび中央アメリカ ＞ メキシコ．中央アメリカ諸国．カリブ海地域 ＞ カリブ海地域．西インド諸島(アンティル諸島) ＞ 小アンティル(東カリブ海) ＞ リーワード諸島 ＞ 小アンティルのフランス領土 ＞ グアドループ(地域と部門)(フランス)
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(729.745)`

- FACET: `place`
- NODE_KEY: `place::(729.745)`
- CODE: `(729.745)`
- LABEL: マルチニーク(地域と部門)(フランス)
- PARENT_KEY: `place::(729.74)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(7)` > `(72)` > `(729)` > `(729.7/.8)` > `(729.7)` > `(729.74)` > `(729.745)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 北アメリカおよび中央アメリカ ＞ メキシコ．中央アメリカ諸国．カリブ海地域 ＞ カリブ海地域．西インド諸島(アンティル諸島) ＞ 小アンティル(東カリブ海) ＞ リーワード諸島 ＞ 小アンティルのフランス領土 ＞ マルチニーク(地域と部門)(フランス)
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(729.8)`

- FACET: `place`
- NODE_KEY: `place::(729.8)`
- CODE: `(729.8)`
- LABEL: ウインドワード諸島
- PARENT_KEY: `place::(729.7/.8)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(7)` > `(72)` > `(729)` > `(729.7/.8)` > `(729.8)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 北アメリカおよび中央アメリカ ＞ メキシコ．中央アメリカ諸国．カリブ海地域 ＞ カリブ海地域．西インド諸島(アンティル諸島) ＞ 小アンティル(東カリブ海) ＞ ウインドワード諸島
- LEAF: false
- DIRECT_CHILDREN_COUNT: 8

### DIRECT_CHILDREN

- `place::(729.821)` | CODE `(729.821)` | ドミニカ．ドミニカ連邦
- `place::(729.822)` | CODE `(729.822)` | セイトルシア
- `place::(729.824)` | CODE `(729.824)` | セントヴィンセント．セントヴィンセントとグレナディーン諸島
- `place::(729.828)` | CODE `(729.828)` | グレナダ
- `place::(729.86)` | CODE `(729.86)` | バルバドス
- `place::(729.87)` | CODE `(729.87)` | トリニダード・トバゴ．トリニダード・トバゴ共和国
- `place::(729.88)` | CODE `(729.88)` | オランダ領小アンティル(西インド諸島).オランダ領アンティル
- `place::(729.885)` | CODE `(729.885)` | アルーバ(オランダ王国)

<!-- END_FACET_NODE -->

## FACET_NODE `place::(729.821)`

- FACET: `place`
- NODE_KEY: `place::(729.821)`
- CODE: `(729.821)`
- LABEL: ドミニカ．ドミニカ連邦
- PARENT_KEY: `place::(729.8)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(7)` > `(72)` > `(729)` > `(729.7/.8)` > `(729.8)` > `(729.821)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 北アメリカおよび中央アメリカ ＞ メキシコ．中央アメリカ諸国．カリブ海地域 ＞ カリブ海地域．西インド諸島(アンティル諸島) ＞ 小アンティル(東カリブ海) ＞ ウインドワード諸島 ＞ ドミニカ．ドミニカ連邦
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(729.822)`

- FACET: `place`
- NODE_KEY: `place::(729.822)`
- CODE: `(729.822)`
- LABEL: セイトルシア
- PARENT_KEY: `place::(729.8)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(7)` > `(72)` > `(729)` > `(729.7/.8)` > `(729.8)` > `(729.822)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 北アメリカおよび中央アメリカ ＞ メキシコ．中央アメリカ諸国．カリブ海地域 ＞ カリブ海地域．西インド諸島(アンティル諸島) ＞ 小アンティル(東カリブ海) ＞ ウインドワード諸島 ＞ セイトルシア
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(729.824)`

- FACET: `place`
- NODE_KEY: `place::(729.824)`
- CODE: `(729.824)`
- LABEL: セントヴィンセント．セントヴィンセントとグレナディーン諸島
- PARENT_KEY: `place::(729.8)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(7)` > `(72)` > `(729)` > `(729.7/.8)` > `(729.8)` > `(729.824)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 北アメリカおよび中央アメリカ ＞ メキシコ．中央アメリカ諸国．カリブ海地域 ＞ カリブ海地域．西インド諸島(アンティル諸島) ＞ 小アンティル(東カリブ海) ＞ ウインドワード諸島 ＞ セントヴィンセント．セントヴィンセントとグレナディーン諸島
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(729.828)`

- FACET: `place`
- NODE_KEY: `place::(729.828)`
- CODE: `(729.828)`
- LABEL: グレナダ
- PARENT_KEY: `place::(729.8)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(7)` > `(72)` > `(729)` > `(729.7/.8)` > `(729.8)` > `(729.828)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 北アメリカおよび中央アメリカ ＞ メキシコ．中央アメリカ諸国．カリブ海地域 ＞ カリブ海地域．西インド諸島(アンティル諸島) ＞ 小アンティル(東カリブ海) ＞ ウインドワード諸島 ＞ グレナダ
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(729.86)`

- FACET: `place`
- NODE_KEY: `place::(729.86)`
- CODE: `(729.86)`
- LABEL: バルバドス
- PARENT_KEY: `place::(729.8)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(7)` > `(72)` > `(729)` > `(729.7/.8)` > `(729.8)` > `(729.86)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 北アメリカおよび中央アメリカ ＞ メキシコ．中央アメリカ諸国．カリブ海地域 ＞ カリブ海地域．西インド諸島(アンティル諸島) ＞ 小アンティル(東カリブ海) ＞ ウインドワード諸島 ＞ バルバドス
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(729.87)`

- FACET: `place`
- NODE_KEY: `place::(729.87)`
- CODE: `(729.87)`
- LABEL: トリニダード・トバゴ．トリニダード・トバゴ共和国
- PARENT_KEY: `place::(729.8)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(7)` > `(72)` > `(729)` > `(729.7/.8)` > `(729.8)` > `(729.87)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 北アメリカおよび中央アメリカ ＞ メキシコ．中央アメリカ諸国．カリブ海地域 ＞ カリブ海地域．西インド諸島(アンティル諸島) ＞ 小アンティル(東カリブ海) ＞ ウインドワード諸島 ＞ トリニダード・トバゴ．トリニダード・トバゴ共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(729.88)`

- FACET: `place`
- NODE_KEY: `place::(729.88)`
- CODE: `(729.88)`
- LABEL: オランダ領小アンティル(西インド諸島).オランダ領アンティル
- PARENT_KEY: `place::(729.8)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(7)` > `(72)` > `(729)` > `(729.7/.8)` > `(729.8)` > `(729.88)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 北アメリカおよび中央アメリカ ＞ メキシコ．中央アメリカ諸国．カリブ海地域 ＞ カリブ海地域．西インド諸島(アンティル諸島) ＞ 小アンティル(東カリブ海) ＞ ウインドワード諸島 ＞ オランダ領小アンティル(西インド諸島).オランダ領アンティル
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(729.885)`

- FACET: `place`
- NODE_KEY: `place::(729.885)`
- CODE: `(729.885)`
- LABEL: アルーバ(オランダ王国)
- PARENT_KEY: `place::(729.8)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(7)` > `(72)` > `(729)` > `(729.7/.8)` > `(729.8)` > `(729.885)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 北アメリカおよび中央アメリカ ＞ メキシコ．中央アメリカ諸国．カリブ海地域 ＞ カリブ海地域．西インド諸島(アンティル諸島) ＞ 小アンティル(東カリブ海) ＞ ウインドワード諸島 ＞ アルーバ(オランダ王国)
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(729.9)`

- FACET: `place`
- NODE_KEY: `place::(729.9)`
- CODE: `(729.9)`
- LABEL: バミューダ(ソマーク諸島)UK)
- PARENT_KEY: `place::(729)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(7)` > `(72)` > `(729)` > `(729.9)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 北アメリカおよび中央アメリカ ＞ メキシコ．中央アメリカ諸国．カリブ海地域 ＞ カリブ海地域．西インド諸島(アンティル諸島) ＞ バミューダ(ソマーク諸島)UK)
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(73)`

- FACET: `place`
- NODE_KEY: `place::(73)`
- CODE: `(73)`
- LABEL: アメリカ合衆国
- PARENT_KEY: `place::(7)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(7)` > `(73)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 北アメリカおよび中央アメリカ ＞ アメリカ合衆国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(8)`

- FACET: `place`
- NODE_KEY: `place::(8)`
- CODE: `(8)`
- LABEL: 南アメリカ．南米諸国と地域．ラテンアメリカ
- PARENT_KEY: `place::(7/8)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(8)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 南アメリカ．南米諸国と地域．ラテンアメリカ
- LEAF: false
- DIRECT_CHILDREN_COUNT: 11

### DIRECT_CHILDREN

- `place::(81)` | CODE `(81)` | ブラジル連邦共和国
- `place::(82)` | CODE `(82)` | アルゼンチン共和国
- `place::(83)` | CODE `(83)` | チリ共和国
- `place::(84)` | CODE `(84)` | ボリビア共和国
- `place::(85)` | CODE `(85)` | ペルー共和国
- `place::(862)` | CODE `(862)` | コロンビア共和国
- `place::(866)` | CODE `(866)` | エクアドル共和国
- `place::(87)` | CODE `(87)` | ベネズエラ共和国
- `place::(88)` | CODE `(88)` | ギアナ
- `place::(893)` | CODE `(893)` | パラグアイ共和国
- `place::(899)` | CODE `(899)` | ウルグアイ東方共和国

### INCLUDING

ブラジル，アルゼンチン，チリ，ボリビア，ペルー，コロンビア，エクアドル，ベネズエラ，ガイアナ，仏領ギアナ，スリナム，パラグアイ，ウルグアイ

<!-- END_FACET_NODE -->

## FACET_NODE `place::(81)`

- FACET: `place`
- NODE_KEY: `place::(81)`
- CODE: `(81)`
- LABEL: ブラジル連邦共和国
- PARENT_KEY: `place::(8)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(8)` > `(81)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 南アメリカ．南米諸国と地域．ラテンアメリカ ＞ ブラジル連邦共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(82)`

- FACET: `place`
- NODE_KEY: `place::(82)`
- CODE: `(82)`
- LABEL: アルゼンチン共和国
- PARENT_KEY: `place::(8)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(8)` > `(82)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 南アメリカ．南米諸国と地域．ラテンアメリカ ＞ アルゼンチン共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(83)`

- FACET: `place`
- NODE_KEY: `place::(83)`
- CODE: `(83)`
- LABEL: チリ共和国
- PARENT_KEY: `place::(8)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(8)` > `(83)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 南アメリカ．南米諸国と地域．ラテンアメリカ ＞ チリ共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(84)`

- FACET: `place`
- NODE_KEY: `place::(84)`
- CODE: `(84)`
- LABEL: ボリビア共和国
- PARENT_KEY: `place::(8)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(8)` > `(84)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 南アメリカ．南米諸国と地域．ラテンアメリカ ＞ ボリビア共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(85)`

- FACET: `place`
- NODE_KEY: `place::(85)`
- CODE: `(85)`
- LABEL: ペルー共和国
- PARENT_KEY: `place::(8)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(8)` > `(85)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 南アメリカ．南米諸国と地域．ラテンアメリカ ＞ ペルー共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(862)`

- FACET: `place`
- NODE_KEY: `place::(862)`
- CODE: `(862)`
- LABEL: コロンビア共和国
- PARENT_KEY: `place::(8)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(8)` > `(862)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 南アメリカ．南米諸国と地域．ラテンアメリカ ＞ コロンビア共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(866)`

- FACET: `place`
- NODE_KEY: `place::(866)`
- CODE: `(866)`
- LABEL: エクアドル共和国
- PARENT_KEY: `place::(8)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(8)` > `(866)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 南アメリカ．南米諸国と地域．ラテンアメリカ ＞ エクアドル共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(87)`

- FACET: `place`
- NODE_KEY: `place::(87)`
- CODE: `(87)`
- LABEL: ベネズエラ共和国
- PARENT_KEY: `place::(8)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(8)` > `(87)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 南アメリカ．南米諸国と地域．ラテンアメリカ ＞ ベネズエラ共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(88)`

- FACET: `place`
- NODE_KEY: `place::(88)`
- CODE: `(88)`
- LABEL: ギアナ
- PARENT_KEY: `place::(8)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(8)` > `(88)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 南アメリカ．南米諸国と地域．ラテンアメリカ ＞ ギアナ
- LEAF: false
- DIRECT_CHILDREN_COUNT: 3

### DIRECT_CHILDREN

- `place::(881)` | CODE `(881)` | ガイアナ協同共和国
- `place::(882)` | CODE `(882)` | 仏領ギアナ
- `place::(883)` | CODE `(883)` | スリナム共和国

<!-- END_FACET_NODE -->

## FACET_NODE `place::(881)`

- FACET: `place`
- NODE_KEY: `place::(881)`
- CODE: `(881)`
- LABEL: ガイアナ協同共和国
- PARENT_KEY: `place::(88)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(8)` > `(88)` > `(881)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 南アメリカ．南米諸国と地域．ラテンアメリカ ＞ ギアナ ＞ ガイアナ協同共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(882)`

- FACET: `place`
- NODE_KEY: `place::(882)`
- CODE: `(882)`
- LABEL: 仏領ギアナ
- PARENT_KEY: `place::(88)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(8)` > `(88)` > `(882)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 南アメリカ．南米諸国と地域．ラテンアメリカ ＞ ギアナ ＞ 仏領ギアナ
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(883)`

- FACET: `place`
- NODE_KEY: `place::(883)`
- CODE: `(883)`
- LABEL: スリナム共和国
- PARENT_KEY: `place::(88)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(8)` > `(88)` > `(883)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 南アメリカ．南米諸国と地域．ラテンアメリカ ＞ ギアナ ＞ スリナム共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(893)`

- FACET: `place`
- NODE_KEY: `place::(893)`
- CODE: `(893)`
- LABEL: パラグアイ共和国
- PARENT_KEY: `place::(8)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(8)` > `(893)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 南アメリカ．南米諸国と地域．ラテンアメリカ ＞ パラグアイ共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(899)`

- FACET: `place`
- NODE_KEY: `place::(899)`
- CODE: `(899)`
- LABEL: ウルグアイ東方共和国
- PARENT_KEY: `place::(8)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(7/8)` > `(8)` > `(899)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ アメリカ．南北アメリカ大陸 ＞ 南アメリカ．南米諸国と地域．ラテンアメリカ ＞ ウルグアイ東方共和国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(9)`

- FACET: `place`
- NODE_KEY: `place::(9)`
- CODE: `(9)`
- LABEL: 南太平洋およびオーストラリアの国・地域．北極，南極
- PARENT_KEY: `place::(4/9)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(9)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ 南太平洋およびオーストラリアの国・地域．北極，南極
- LEAF: false
- DIRECT_CHILDREN_COUNT: 9

### DIRECT_CHILDREN

- `place::(931)` | CODE `(931)` | ニュージーランド
- `place::(932/935)` | CODE `(932/935)` | メラネシア．メラネシア諸国と地域
- `place::(94)` | CODE `(94)` | オーストラリア連邦
- `place::(954)` | CODE `(954)` | パプアニューギニア独立国
- `place::(961/964)` | CODE `(961/964)` | ポリネシア．ポリネシア諸国と地域
- `place::(966/968)` | CODE `(966/968)` | ミクロネシア．ミクロネシア諸国と地域
- `place::(97)` | CODE `(97)` | 太平洋の孤島
- `place::(98)` | CODE `(98)` | 北極
- `place::(99)` | CODE `(99)` | 南極地域

<!-- END_FACET_NODE -->

## FACET_NODE `place::(931)`

- FACET: `place`
- NODE_KEY: `place::(931)`
- CODE: `(931)`
- LABEL: ニュージーランド
- PARENT_KEY: `place::(9)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(9)` > `(931)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ 南太平洋およびオーストラリアの国・地域．北極，南極 ＞ ニュージーランド
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(932/935)`

- FACET: `place`
- NODE_KEY: `place::(932/935)`
- CODE: `(932/935)`
- LABEL: メラネシア．メラネシア諸国と地域
- PARENT_KEY: `place::(9)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(9)` > `(932/935)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ 南太平洋およびオーストラリアの国・地域．北極，南極 ＞ メラネシア．メラネシア諸国と地域
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(94)`

- FACET: `place`
- NODE_KEY: `place::(94)`
- CODE: `(94)`
- LABEL: オーストラリア連邦
- PARENT_KEY: `place::(9)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(9)` > `(94)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ 南太平洋およびオーストラリアの国・地域．北極，南極 ＞ オーストラリア連邦
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(954)`

- FACET: `place`
- NODE_KEY: `place::(954)`
- CODE: `(954)`
- LABEL: パプアニューギニア独立国
- PARENT_KEY: `place::(9)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(9)` > `(954)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ 南太平洋およびオーストラリアの国・地域．北極，南極 ＞ パプアニューギニア独立国
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(961/964)`

- FACET: `place`
- NODE_KEY: `place::(961/964)`
- CODE: `(961/964)`
- LABEL: ポリネシア．ポリネシア諸国と地域
- PARENT_KEY: `place::(9)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(9)` > `(961/964)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ 南太平洋およびオーストラリアの国・地域．北極，南極 ＞ ポリネシア．ポリネシア諸国と地域
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(966/968)`

- FACET: `place`
- NODE_KEY: `place::(966/968)`
- CODE: `(966/968)`
- LABEL: ミクロネシア．ミクロネシア諸国と地域
- PARENT_KEY: `place::(9)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(9)` > `(966/968)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ 南太平洋およびオーストラリアの国・地域．北極，南極 ＞ ミクロネシア．ミクロネシア諸国と地域
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(97)`

- FACET: `place`
- NODE_KEY: `place::(97)`
- CODE: `(97)`
- LABEL: 太平洋の孤島
- PARENT_KEY: `place::(9)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(9)` > `(97)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ 南太平洋およびオーストラリアの国・地域．北極，南極 ＞ 太平洋の孤島
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(98)`

- FACET: `place`
- NODE_KEY: `place::(98)`
- CODE: `(98)`
- LABEL: 北極
- PARENT_KEY: `place::(9)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(9)` > `(98)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ 南太平洋およびオーストラリアの国・地域．北極，南極 ＞ 北極
- LEAF: false
- DIRECT_CHILDREN_COUNT: 1

### DIRECT_CHILDREN

- `place::(988)` | CODE `(988)` | グリーンランド(デンマーク領)

<!-- END_FACET_NODE -->

## FACET_NODE `place::(988)`

- FACET: `place`
- NODE_KEY: `place::(988)`
- CODE: `(988)`
- LABEL: グリーンランド(デンマーク領)
- PARENT_KEY: `place::(98)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(9)` > `(98)` > `(988)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ 南太平洋およびオーストラリアの国・地域．北極，南極 ＞ 北極 ＞ グリーンランド(デンマーク領)
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->

## FACET_NODE `place::(99)`

- FACET: `place`
- NODE_KEY: `place::(99)`
- CODE: `(99)`
- LABEL: 南極地域
- PARENT_KEY: `place::(9)`
- PATH_CODES: `(1/9)` > `(3/9)` > `(4/9)` > `(9)` > `(99)`
- PATH_LABELS: 場所の共通補助番号．表1e ＞ 古代および現代世界の個々の場所 ＞ 現代の世界の国と場所 ＞ 南太平洋およびオーストラリアの国・地域．北極，南極 ＞ 南極地域
- LEAF: true
- DIRECT_CHILDREN_COUNT: 0

### DIRECT_CHILDREN

なし

<!-- END_FACET_NODE -->
