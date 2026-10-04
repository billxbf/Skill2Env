# partner_management_orderer_project_business_partners

partner_management_orderer_project_business_partners

## GET /hub/partner_management/orderer/projects/{project_id}/project_business_partners — プロジェクトのログインなしパートナー一覧取得（β版）

指定プロジェクトにアサインされているログインなしパートナー一覧を取得する

### パラメータ

- freee-using-beta* (header): string - オープンベータのエンドポイントのため `true` を指定（必須） (選択肢: true)
- project_id* (path): integer(int32) - 取得対象のプロジェクトID
- company_id*: integer(int64) - freee事業所ID
- page_size: integer(int32) - 1ページあたりの取得件数（デフォルト20、最大100）
- page_token: string - カーソルトークン。前回レスポンスの next_page_token を指定する

### レスポンス

プロジェクトのログインなしパートナー一覧レスポンス
- data*: array[object] - ログインなしパートナーのリスト
- next_page_token*: string - 次ページのカーソルトークン。最終ページは null
