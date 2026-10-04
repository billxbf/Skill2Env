# Selectables

フォーム用選択項目情報

## GET /api/1/forms/selectables — フォーム用選択項目情報の取得

概要 指定した事業所で勘定科目の入力フォームを構築するための、勘定科目カテゴリー、勘定科目、デフォルト税区分、決算書表示名を取得します。

注意点
includes に account_item を指定した場合に、 account_categories と account_groups を返します。 includes を指定しない場合、レスポンスは空のオブジェクトになります。

### パラメータ

- company_id*: integer(int64) - 事業所ID
- includes: string - 取得する選択項目
  * `account_item` - 勘定科目カテゴリー、勘定科目、デフォルト税区分、決算書表示名 (選択肢: account_item)

### レスポンス

フォーム用選択項目情報の取得に成功
- account_categories: array[object] - 勘定科目を用途別に分類したカテゴリーの一覧
- account_groups: array[object] - 勘定科目を決算書上で集約するための決算書表示名（小カテゴリー）の一覧
