# partner_management_orderer_projects

partner_management_orderer_projects

## GET /hub/partner_management/orderer/projects — プロジェクト一覧取得（β版）

プロジェクトを一覧で取得する

### パラメータ

- freee-using-beta* (header): string - オープンベータのエンドポイントのため `true` を指定（必須） (選択肢: true)
- company_id*: integer(int64) - freee事業所ID
- company_user_ids[]: array[integer] - 担当者（企業ユーザー）のIDで絞り込む。指定したIDをすべて含むプロジェクトだけを返す（AND条件）
- partner_ids[]: array[integer] - パートナー（ログインあり）のIDで絞り込む。指定したIDをすべて含むプロジェクトだけを返す（AND条件）
- business_partner_ids[]: array[integer] - ログインなしパートナーのIDで絞り込む。指定したIDをすべて含むプロジェクトだけを返す（AND条件）
- project_ids[]: array[integer] - プロジェクトIDで絞り込む。指定したいずれかのIDに一致するプロジェクトを返す（OR条件）
- name_contains: string - プロジェクト名で絞り込む（部分一致）
- description_contains: string - 説明で絞り込む（部分一致）
- page_size: integer(int32) - 1ページあたりの取得件数（デフォルト20、最大100）
- page_token: string - カーソルトークン。前回レスポンスの next_page_token を指定する

### レスポンス

プロジェクト一覧レスポンス
- data*: array[object] - プロジェクトの一覧
- next_page_token*: string - 次ページのカーソルトークン。最終ページは null

## GET /hub/partner_management/orderer/projects/{id} — プロジェクト詳細取得（β版）

プロジェクト情報を取得する

### パラメータ

- freee-using-beta* (header): string - オープンベータのエンドポイントのため `true` を指定（必須） (選択肢: true)
- company_id*: integer(int64) - freee事業所ID
- id* (path): integer(int32) - 取得対象のプロジェクトID

### レスポンス

プロジェクト詳細レスポンス
- id*: integer(int32) - プロジェクトID
- is_archived*: boolean - アーカイブ済みかどうか
- archived_at*: string(date-time) - アーカイブ日時
- name*: string - プロジェクト名
- description*: string - 説明
- require_hide_other_freelancers*: boolean - 他パートナーのアカウントを非表示にするか
- default_inspection_date_days*: integer(int32) - 検収日のデフォルト設定
- default_task_order_note*: string - 発注書の備考欄のデフォルト設定
- default_invoice_note*: string - 請求書の備考欄のデフォルト設定
- approval_flow_pattern_task_order_id*: integer(int64) - タスク発注の社内承認フローID
- approval_flow_pattern_task_submit_id*: integer(int64) - タスク検収の社内承認フローID
- approval_flow_pattern_invoice_submit_id*: integer(int64) - 請求書の社内承認フローID
- created_at*: string(date-time) - 作成日時
