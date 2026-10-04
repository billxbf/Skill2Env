# partner_management_orderer_project_company_users

partner_management_orderer_project_company_users

## GET /hub/partner_management/orderer/projects/{project_id}/project_company_users — プロジェクト担当者一覧取得（β版）

指定プロジェクトの担当者（アサインされている企業ユーザー）の一覧を取得する

### パラメータ

- freee-using-beta* (header): string - オープンベータのエンドポイントのため `true` を指定（必須） (選択肢: true)
- company_id*: integer(int64) - freee事業所ID
- project_id* (path): integer(int32) - 取得対象のプロジェクト ID
- page_size: integer(int32) - 1ページあたりの取得件数（デフォルト20、最大100）
- page_token: string - カーソルトークン。前回レスポンスの next_page_token を指定する

### レスポンス

プロジェクトの担当者一覧レスポンス
- data*: array[object] - 担当者一覧
- next_page_token*: string - 次ページのカーソルトークン。最終ページは null
