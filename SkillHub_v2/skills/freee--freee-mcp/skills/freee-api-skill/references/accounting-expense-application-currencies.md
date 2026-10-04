# Expense application currencies

経費精算の外貨

## GET /api/1/expense_applications/currencies — 経費精算の外貨一覧の取得

概要 指定した事業所の経費精算で利用する外貨の一覧を取得します。

### パラメータ

- company_id*: integer(int64) - 事業所ID
- search_status: string - 利用状態での絞り込み (usable: 利用可能, unusable: 利用不可) (選択肢: usable, unusable)

### レスポンス

- data*: array[object] - 外貨一覧

## POST /api/1/expense_applications/currencies — 経費精算の外貨の作成

概要 指定した事業所の経費精算で利用する外貨を作成します。

### リクエストボディ*

- company_id*: integer(int64) - 事業所ID 例: `1` (最小: 1)
- name*: string - 外貨名 (30文字以内、前後の空白を除去した上で事業所内で重複不可) 例: `ベトナム・ドン`
- code*: string - 通貨コード (半角英大文字3文字) 例: `VND` (パターン: ^[A-Z]{3}$)
- search_status*: string - 利用状態 (usable: 利用可能, unusable: 利用不可) (選択肢: usable, unusable) 例: `usable`
- description: string - 備考 例: `ハノイ支社経費用`

### レスポンス

- id*: integer(int64) - 外貨ID
- name*: string - 外貨名 (30文字以内)
- code*: string - 通貨コード (半角英大文字3文字)
- description*: string - 備考
- search_status*: string - 利用状態 (usable: 利用可能, unusable: 利用不可)
- updated_at*: string - 更新日時 (ISO8601形式)

## GET /api/1/expense_applications/currencies/{id} — 経費精算の外貨の取得

概要 指定した事業所の経費精算で利用する外貨を取得します。

### パラメータ

- id* (path): integer(int64) - 外貨ID
- company_id*: integer(int64) - 事業所ID

### レスポンス

POST /api/1/expense_applications/currencies と同じ

## PUT /api/1/expense_applications/currencies/{id} — 経費精算の外貨の更新

概要 指定した事業所の経費精算で利用する外貨を更新します。

### パラメータ

- id* (path): integer(int64) - 外貨ID

### リクエストボディ*

POST /api/1/expense_applications/currencies と同じ

### レスポンス

POST /api/1/expense_applications/currencies と同じ

## DELETE /api/1/expense_applications/currencies/{id} — 経費精算の外貨の削除

概要 指定した事業所の経費精算で利用する外貨を削除します。

### パラメータ

GET /api/1/expense_applications/currencies/{id} と同じ
