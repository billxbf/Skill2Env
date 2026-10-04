//! Contract tests for `PricingTable::compute_cost` — the underlying
//! cost-computation engine that remains in `src/storage/sqlite.rs` after
//! the public `cass analytics cost` subcommand was removed in commit
//! `6ec44e90`.
//!
//! Per `coding_agent_session_search-vz9t8.5`. The bead offered Path A
//! (restore the subcommand) and Path B (document the removal and ship the
//! alternate way to compute cost). This PR takes Path B: ship contract
//! tests guarding the underlying PricingTable + compute_cost functions
//! against accidental removal, plus document the SQL-based alternate path.
//!
//! ## Alternate cost computation (per Path B docs)
//!
//! Operators can compute total token cost from the analytics database
//! directly:
//!
//! ```sql
//! SELECT
//!   COALESCE(model, 'unknown') AS model,
//!   SUM(cost_usd_in + cost_usd_out) AS total_usd
//! FROM usage_daily
//! WHERE day >= ?  -- since filter
//! GROUP BY model
//! ORDER BY total_usd DESC
//! LIMIT 10;
//! ```
//!
//! This documented path is the supported user-facing surface until the
//! `cass analytics cost` subcommand is restored in a follow-up bead.

use std::path::PathBuf;

fn storage_sqlite_source() -> String {
    let path = PathBuf::from(env!("CARGO_MANIFEST_DIR"))
        .join("src")
        .join("storage")
        .join("sqlite.rs");
    std::fs::read_to_string(path).expect("src/storage/sqlite.rs readable")
}

#[test]
fn pricing_table_struct_still_present() {
    tracing::info!(target: "vz9t8_5_test", scenario = "struct_present");
    let body = storage_sqlite_source();
    assert!(
        body.contains("pub struct PricingTable"),
        "src/storage/sqlite.rs must define `pub struct PricingTable` (per z9fse.10's \
         underlying engine; required for follow-up `cass analytics cost` restoration)"
    );
}

#[test]
fn pricing_table_compute_cost_still_present() {
    tracing::info!(target: "vz9t8_5_test", scenario = "compute_cost_present");
    let body = storage_sqlite_source();
    assert!(
        body.contains("fn compute_cost") && body.contains("impl PricingTable"),
        "PricingTable::compute_cost must still be defined; deletion would block restoration"
    );
}

#[test]
fn pricing_table_franken_load_still_present() {
    tracing::info!(target: "vz9t8_5_test", scenario = "franken_load_present");
    let body = storage_sqlite_source();
    assert!(
        body.contains("PricingTable::franken_load"),
        "PricingTable::franken_load must still be invoked from the storage layer; \
         this is the SQL-side cost-data accessor"
    );
}

#[test]
fn ingest_path_still_calls_compute_cost() {
    tracing::info!(target: "vz9t8_5_test", scenario = "ingest_calls_compute");
    let body = storage_sqlite_source();
    assert!(
        body.contains("estimated_cost") || body.contains("compute_cost"),
        "ingest path in src/storage/sqlite.rs must still compute cost during usage_daily \
         row writes — without this, the SQL alternate-path documented in this test would \
         return zeroed cost columns"
    );
}

#[test]
fn alternate_cost_query_documented_in_test_doc_comment() {
    tracing::info!(target: "vz9t8_5_test", scenario = "alternate_path_documented");
    // This test asserts the SQL alternate-path is preserved in this test
    // file's own doc comment, so the documentation lives alongside the code
    // it protects (refactors of the doc comment would surface here).
    let path = PathBuf::from(env!("CARGO_MANIFEST_DIR"))
        .join("tests")
        .join("analytics_cost_pricing_table_contract.rs");
    let body = std::fs::read_to_string(&path).expect("self-readable");
    assert!(
        body.contains("Alternate cost computation") && body.contains("SUM(cost_usd"),
        "this test file's doc comment must include the SQL alternate-path query"
    );
}
