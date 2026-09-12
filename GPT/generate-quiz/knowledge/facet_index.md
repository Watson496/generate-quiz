# ファセットカタログ索引

この索引と各カタログは、元のファセットYAMLをGPT検索向けに変換したものです。分類内容・コード・階層は変更していません。あるノードを細分化するときは、該当する `FACET_NODE` ブロックの `DIRECT_CHILDREN` を全件候補にしてください。

## 検索方法

1. 現在の親を `FACET::CODE` 形式の `NODE_KEY` で検索する。
2. 取得した一つの親ブロック内の `DIRECT_CHILDREN` を漏れなく読む。
3. 子へ進んだ場合は、選んだ子の `NODE_KEY` で次の親ブロックを検索する。
4. 出力時の階層パスには `PATH_LABELS` を使い、コードは表示しない。
5. 同名ラベルがあっても `NODE_KEY` が異なれば別ノードとして扱う。

## FACET_ROOT `subject::ROOT`

- FACET: `subject`
- FILES: `facet_subject_0.md`, `facet_subject_1.md`, `facet_subject_2.md`, `facet_subject_3.md`, `facet_subject_5.md`, `facet_subject_6.md`, `facet_subject_7.md`, `facet_subject_8.md`, `facet_subject_9.md`

### DIRECT_CHILDREN

- `subject::0` | CODE `0` | 序説.知識と文化の基礎
- `subject::1` | CODE `1` | 哲学．心理学
- `subject::2` | CODE `2` | 宗教．神学
- `subject::3` | CODE `3` | 社会科学．統計学．政治学．経済学．商業．法律．行政．軍事．福祉．保険．教育．民俗学
- `subject::5` | CODE `5` | 数学．自然科学
- `subject::6` | CODE `6` | 応用科学．医学．工学
- `subject::7` | CODE `7` | 芸術．レクリエーション．娯楽．スポーツ
- `subject::8` | CODE `8` | 言語．言語学．文学
- `subject::9` | CODE `9` | 地理．伝記．歴史

<!-- END_FACET_ROOT -->

## FACET_ROOT `place::ROOT`

- FACET: `place`
- FILES: `facet_place.md`

### DIRECT_CHILDREN

- `place::(1/9)` | CODE `(1/9)` | 場所の共通補助番号．表1e

<!-- END_FACET_ROOT -->

## FACET_ROOT `time::ROOT`

- FACET: `time`
- FILES: `facet_time.md`

### DIRECT_CHILDREN

- `time::"0/2"` | CODE `"0/2"` | キリスト教暦（グレゴリウス暦）による日付および期間
- `time::"3/7"` | CODE `"3/7"` | キリスト教暦（グレゴリウス暦）以外の時代区分
- `time::"..."` | CODE `"..."` | 時の共通補助番号．表1g

<!-- END_FACET_ROOT -->

## FACET_ROOT `type::ROOT`

- FACET: `type`
- FILES: `facet_type.md`

### DIRECT_CHILDREN

- `type::ontology` | CODE `ontology` | オントロジー型ファセット

<!-- END_FACET_ROOT -->
