# partner_management_orderer_project_partners

partner_management_orderer_project_partners

## GET /hub/partner_management/orderer/projects/{project_id}/project_partners — プロジェクトパートナー一覧取得（β版）

指定したプロジェクトにアサインされているパートナーの一覧を取得する。 ##

注意点
- パートナーの詳細情報は返さないため、必要な場合はレスポンスの `partner_id` を使って パートナー詳細取得 API を呼び出す。 - 招待を承諾していないパートナーもプロジェクトにアサインできるため、一覧に含まれる。 その場合 `name` には招待時に指定した名前を返す。

### パラメータ

- freee-using-beta* (header): string - オープンベータのエンドポイントのため `true` を指定（必須） (選択肢: true)
- company_id*: integer(int64) - freee事業所ID
- project_id* (path): integer(int32) - 取得対象のプロジェクトID
- page_size: integer(int32) - 1ページあたりの取得件数（デフォルト20、最大100）
- page_token: string - カーソルトークン。前回レスポンスの next_page_token を指定する

### レスポンス

プロジェクトパートナー一覧レスポンス
- data*: array[object] - プロジェクトパートナーのリスト
- next_page_token*: string - 次ページのカーソルトークン。最終ページは null
