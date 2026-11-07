from pathlib import Path
import pandas as pd, json
ROOT=Path(__file__).resolve().parents[1]
D=ROOT/"sample_data"/"data"; O=ROOT/"results"; O.mkdir(exist_ok=True)
crm=pd.read_csv(D/"1_crm_leads.csv")
demo=pd.read_csv(D/"2_demo_class_evaluations.csv")
calls=pd.read_csv(D/"3_sales_call_logs.csv")
orders=pd.read_csv(D/"4_live_orders_and_invoices.csv")
# The detailed analyst-reviewed classifications are preserved in the supplied results.
# This script performs a reproducible source-data integrity summary and lead-level joins.
joined=crm.merge(demo[["lead_id","child_engagement_score_1_to_5","learning_gaps_observed","demo_magic_moment_for_parent"]],
                 left_on="id",right_on="lead_id",how="left")
joined=joined.merge(calls[["lead_id","call_id","call_duration_sec","rep_talk_time_pct","parent_talk_time_pct","transcript_filename"]],
                    left_on="id",right_on="lead_id",how="left",suffixes=("","_call"))
joined=joined.merge(orders[["lead_id","order_id","currency","standard_amount","discount_applied","net_payable_amount","payment_link_status","gateway_error_reason","paid_at"]],
                    left_on="id",right_on="lead_id",how="left",suffixes=("","_order"))
joined.to_csv(O/"source_joined_lead_view.csv",index=False)
summary={
 "crm_leads":int(len(crm)),"demo_evaluations":int(len(demo)),"call_logs":int(len(calls)),
 "orders":int(len(orders)),"transcripts":len(list((ROOT/"sample_data"/"call_transcripts").glob("*.txt"))),
 "crm_duplicate_student_ids":int(crm.student_id.duplicated(keep=False).sum()),
 "leads_without_call_log":int((~crm.id.isin(calls.lead_id)).sum()),
 "leads_without_demo":int((~crm.id.isin(demo.lead_id)).sum()),
 "orders_paid":int((orders.payment_link_status=="Paid").sum()),
 "orders_failed":int(orders.payment_link_status.astype(str).str.contains("Failed").sum())
}
(O/"data_quality_summary.json").write_text(json.dumps(summary,indent=2))
print(json.dumps(summary,indent=2))
