# partner_management_orderer_tasks

partner_management_orderer_tasks

## GET /hub/partner_management/orderer/tasks — タスク一覧取得（β版）

タスク（発注書）の一覧を取得する

### パラメータ

- freee-using-beta* (header): string - オープンベータのエンドポイントのため `true` を指定（必須） (選択肢: true)
- company_id*: integer(int64) - freee事業所ID
- page_size: integer(int32) - 1ページあたりの取得件数（デフォルト20、最大100）
- page_token: string - カーソルトークン。前回レスポンスの next_page_token を指定する
- project_id: integer(int32) - プロジェクトのIDで絞り込む
- assignee_type: string - パートナー (Partner: パートナー, BusinessPartner: ログインなしパートナー) (選択肢: Partner, BusinessPartner)
- assignee_id: integer(int64) - アサインされているパートナーのIDで絞り込み、そのパートナーがアサインされているタスクのみを返す。
  指定できるのは1人のみ（複数指定は不可）。assignee_type と必ずセットで指定する（単独指定は不可）。
  利用停止中・削除済みのパートナーを指定した場合も、該当タスクを検索結果として返す
- company_user_id: integer(int32) - 担当者（企業ユーザー）のIDで絞り込む
- status[]: array[object] - ステータスで絞り込む（複数指定。OR 条件）。opened / not_accepted は廃止済みステータスのため、通常は該当なし
- title: string - タスクタイトルで絞り込む（部分一致）
- estimate_grand_total_from: integer(int32) - 発注額（税込）の下限で絞り込む
- estimate_grand_total_to: integer(int32) - 発注額（税込）の上限で絞り込む
- deadline_from: string(date) - 納期の下限で絞り込む。submit_date_type が period のタスクは submit_period_end_date（終了日）で判定する
- deadline_to: string(date) - 納期の上限で絞り込む。submit_date_type が period のタスクは submit_period_end_date（終了日）で判定する
- assigned_at_from: string(date) - 発行日の下限で絞り込む
- assigned_at_to: string(date) - 発行日の上限で絞り込む
- submitted_at_from: string(date) - 初回提出日の下限で絞り込む
- submitted_at_to: string(date) - 初回提出日の上限で絞り込む
- last_submitted_at_from: string(date) - 最終提出日の下限で絞り込む
- last_submitted_at_to: string(date) - 最終提出日の上限で絞り込む
- inspection_date_from: string(date) - 検収日の下限で絞り込む
- inspection_date_to: string(date) - 検収日の上限で絞り込む
- created_at_from: string(date) - 作成日時の下限で絞り込む
- created_at_to: string(date) - 作成日時の上限で絞り込む

### レスポンス

タスク一覧レスポンス
- data*: array[object] - タスクの一覧
- next_page_token*: string - 次ページのカーソルトークン。最終ページは null

## GET /hub/partner_management/orderer/projects/{project_id}/tasks/{id} — タスク詳細取得（β版）

タスク（発注書）情報を取得する

### パラメータ

- freee-using-beta* (header): string - オープンベータのエンドポイントのため `true` を指定（必須） (選択肢: true)
- company_id*: integer(int64) - freee事業所ID
- project_id* (path): integer(int32) - 所属プロジェクトのID
- id* (path): integer(int32) - 取得対象のタスクID

### レスポンス

タスク詳細レスポンス
- id*: integer(int32) - タスクID
- project_id*: integer(int32) - プロジェクトID
- status*: string - ステータス
- title*: string - タスクタイトル
- submit_date_type*: string - 納期または期間 (deadline: 納期, period: 期間)
- deadline*: string(date-time) - 納期。submit_date_type が deadline のときに入る
- submit_period_start_date*: string(date) - 提出期間の開始日。submit_date_type が period のときに入る
- submit_period_end_date*: string(date) - 提出期間の終了日。submit_date_type が period のときに入る
- inspection_date*: string(date) - 検収日
- payment_date_type*: string - 支払期日の指定方式 (note: テキスト, next_month_end: 納期/終了日の翌月末日を反映, days_from_deadline: 納期/終了日から日数反映, fixed_date: 指定日)
- payment_date_note*: string - 支払期日（テキスト）。payment_date_type が note のときに入り、それ以外のときは null
- payment_date*: string(date) - 支払期日 (日付)。payment_date_type が next_month_end / days_from_deadline / fixed_date のときに指定方式に即して計算された日付が入る
- delivery_types*: array[object] - 納品形式
- task_work_report_configuration*: object - 稼働時間の丸め設定。delivery_types に work_report / work_report_quantity が含まれるときに入る
- deliverables_detail*: string - 納品内容
- delivery_place*: string - 納品場所
- subcontracted*: boolean - 再委託ありかどうか
- client_name*: string - 元委託者の氏名又は名称。subcontracted が true のときに入る
- client_contract_due_date*: string - 元委託業務の対価の支払期日。subcontracted が true のときに入る
- body*: string - タスク内容
- enable_change_quantity_on_submit*: boolean - 提出時の数量変更を可能にするか
- enable_undecided_amount_order*: boolean - 発注額を未定で発注するか
- undecided_amount_reason*: string - 発注額未定の理由。enable_undecided_amount_order が true のときに入る
- amount_decided_date*: string(date) - 発注額確定予定日。enable_undecided_amount_order が true のときに入る
- orderer_company_user_id*: integer(int32) - 担当者の企業ユーザーID
- watcher_company_user_ids*: array[integer] - 担当者（参加）の企業ユーザーIDの配列
- assignee*: object - パートナー
- watcher_partner_ids*: array[integer] - パートナー（参加）
- worker_partner_id*: integer(int32) - パートナー（タスク実行）
- order_note*: string - 備考
- estimate_total*: integer(int32) - 見積小計 (税抜)。金額の閲覧権限が無い場合は null
- estimate_grand_total*: integer(int32) - 見積総額 (税込)。金額の閲覧権限が無い場合は null
- total*: integer(int32) - 実績小計 (税抜)。金額の閲覧権限が無い場合は null
- grand_total*: integer(int32) - 実績総額 (税込)。金額の閲覧権限が無い場合は null
- tax_expression*: string - 消費税表示 (external: 外税, internal: 内税)
- delivery_data*: object - 納品データ
- special_note*: string - 特記事項
- tax_calculation_type*: string - 消費税の計算単位 (gross: 総額まとめ, each_item: 明細行ごと)
- sales_tax_fraction_type*: string - 消費税端数処理 (floor: 切り捨て, ceil: 切り上げ, round: 四捨五入)
- task_line_item_ids*: array[integer] - タスク明細のIDの配列。明細の表示順 (row_order) の昇順で返す
- task_order_approval_flow_id*: integer(int64) - 発注承認フローID
- task_submit_approval_flow_id*: integer(int64) - 検収承認フローID
- created_at*: string(date-time) - 作成日時
- assigned_at*: string(date-time) - 発注時刻
- submitted_at*: string(date-time) - 直近の提出時刻
- last_submitted_at*: string(date-time) - 最終提出時刻
