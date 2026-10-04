# Expense application forms

## GET /api/1/expense_applications/form — 経費申請フォームの取得

概要 指定した事業所の経費申請フォームの設定を取得します。設定が未作成の場合は初期値を返します。

### パラメータ

- company_id*: integer(int64) - 事業所ID

### レスポンス

- section_setting*: string - 部門の入力設定 (optional: 任意入力, required: 必須入力)
- tag_setting*: string - メモタグの入力設定 (optional: 任意入力, required: 必須入力, disable: 非表示)
- line_template_setting*: string - 経費科目の入力設定 (optional: 任意入力, required: 必須入力, disable: 非表示)。経費科目は `/api/1/expense_application_line_templates` で取得できます。
- segment_1_tag_setting*: string - セグメント1タグの入力設定 (optional: 任意入力, required: 必須入力, disable: 非表示)
- segment_2_tag_setting*: string - セグメント2タグの入力設定 (optional: 任意入力, required: 必須入力, disable: 非表示)
- segment_3_tag_setting*: string - セグメント3タグの入力設定 (optional: 任意入力, required: 必須入力, disable: 非表示)
- description_setting*: string - 備考の入力設定 (optional: 任意入力, required: 必須入力)
- commuter_pass_deduction*: string - 定期券区間控除の利用設定 (disable: 利用しない, enable: 利用する)
- default_flow_route_src_id*: integer(int64) - デフォルトで選択する申請経路のID (未設定の場合は null)。申請経路一覧の取得API (`/api/1/approval_flow_routes`) のレスポンス id と同じ値です。
- observer_addition*: string - 承認者以外の閲覧者追加の利用設定 (disable: 利用しない, enable: 利用する)
- receipt_partner_name_setting*: string - 支払先の入力設定 (optional: 任意入力, required: 必須入力, disable: 非表示)
- default_title*: string - 申請タイトルの初期値 (255文字以内)
- use_currency*: boolean - 外貨の利用設定
- auto_calculation_amount_fraction*: string - 金額の自動計算結果の端数処理 (omit: 切り捨て, round_up: 切り上げ, round: 四捨五入)
- allow_modify_parent_application_by_applicant*: boolean - 申請者による親申請の変更を許可するか
- allow_modify_parent_application_by_approver*: boolean - 承認者による親申請の変更を許可するか
- allow_modify_parent_application_by_admin*: boolean - 管理者による親申請の変更を許可するか
- require_parent_purchase_request*: boolean - 親となる購買申請を必須にするか
- allow_modify_on_approval*: boolean - 承認中の申請の変更を許可するか

## PUT /api/1/expense_applications/form — 経費申請フォームの更新

概要 指定した事業所の経費申請フォームの設定を更新します。設定が未作成の場合は作成します。

### リクエストボディ*

- company_id*: integer(int64) - 事業所ID 例: `1` (最小: 1)
- section_setting*: string - 部門の入力設定 (optional: 任意入力, required: 必須入力) (選択肢: optional, required) 例: `optional`
- tag_setting*: string - メモタグの入力設定 (optional: 任意入力, required: 必須入力, disable: 非表示) (選択肢: optional, required, disable) 例: `optional`
- line_template_setting*: string - 経費科目の入力設定 (optional: 任意入力, required: 必須入力, disable: 非表示)。経費科目は `/api/1/expense_application_line_templates` で取得できます。 (選択肢: optional, required, disable) 例: `optional`
- segment_1_tag_setting*: string - セグメント1タグの入力設定 (optional: 任意入力, required: 必須入力, disable: 非表示) (選択肢: optional, required, disable) 例: `optional`
- segment_2_tag_setting*: string - セグメント2タグの入力設定 (optional: 任意入力, required: 必須入力, disable: 非表示) (選択肢: optional, required, disable) 例: `optional`
- segment_3_tag_setting*: string - セグメント3タグの入力設定 (optional: 任意入力, required: 必須入力, disable: 非表示) (選択肢: optional, required, disable) 例: `optional`
- description_setting*: string - 備考の入力設定 (optional: 任意入力, required: 必須入力) (選択肢: optional, required) 例: `optional`
- commuter_pass_deduction*: string - 定期券区間控除の利用設定 (disable: 利用しない, enable: 利用する) (選択肢: disable, enable) 例: `disable`
- default_flow_route_src_id*: integer(int64) - デフォルトで選択する申請経路のID (未設定の場合は null)。申請経路一覧の取得API (`/api/1/approval_flow_routes`) のレスポンス id と同じ値です。 例: `101` (最小: 1)
- observer_addition*: string - 承認者以外の閲覧者追加の利用設定 (disable: 利用しない, enable: 利用する) (選択肢: disable, enable) 例: `disable`
- receipt_partner_name_setting*: string - 支払先の入力設定 (optional: 任意入力, required: 必須入力, disable: 非表示) (選択肢: optional, required, disable) 例: `disable`
- default_title*: string - 申請タイトルの初期値 (255文字以内) 例: `交通費精算`
- use_currency*: boolean - 外貨の利用設定 例: `true`
- auto_calculation_amount_fraction*: string - 金額の自動計算結果の端数処理 (omit: 切り捨て, round_up: 切り上げ, round: 四捨五入) (選択肢: omit, round_up, round) 例: `round_up`
- allow_modify_parent_application_by_applicant*: boolean - 申請者による親申請の変更を許可するか 例: `true`
- allow_modify_parent_application_by_approver*: boolean - 承認者による親申請の変更を許可するか 例: `false`
- allow_modify_parent_application_by_admin*: boolean - 管理者による親申請の変更を許可するか 例: `false`
- require_parent_purchase_request*: boolean - 親となる購買申請を必須にするか 例: `false`
- allow_modify_on_approval*: boolean - 承認中の申請の変更を許可するか 例: `false`

### レスポンス

GET /api/1/expense_applications/form と同じ
