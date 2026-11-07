# Bambinos AI Sales Intelligence — Take-Home Prototype

A no-code/low-code prototype design and reproducible, data-grounded sample outputs for the Bambinos Sales take-home case.

## What is included
- `sample_data/`: masked source CSVs and six supplied transcripts.
- `prompts/`: four deterministic system prompts.
- `results/call_audit_scorecards.csv`: six evidence-informed call audits.
- `results/cleaned_crm_leads_12.csv` and `.json`: normalized view of all 12 leads.
- `results/whatsapp_followup_sequences.csv`: three-touch drafts or explicit STOP/HOLD instructions.
- `results/pipeline_leak_and_compliance_alerts.csv`: critical operational and compliance alerts.
- `workflows/`: architecture, hard stops and human-in-the-loop rules.
- `report/`: PDF case report.
- `src/analyze_sales.py`: reproducible rule-based analysis generator.

## Run locally
Requirements: Python 3.10+ and pandas.

```bash
python -m pip install pandas
python src/analyze_sales.py
```

The script reads `sample_data/data` and writes reproducible CSV/JSON outputs to `results/`.

## Key findings
- 6 recorded calls audited; 12 CRM rows reviewed.
- LEAD-803: critical compliance breach and explicit do-not-contact request.
- LEAD-804: paid USD 265; stale CRM stage must be corrected to `Enrolled_Paid`.
- LEAD-805 and LEAD-809: failed payments routed to support, not generic sales.
- LEAD-806: child age/batch mismatch and distress; academic review required.
- LEAD-807 and LEAD-812: high-intent demos remain uncalled.
- LEAD-811: duplicate of LEAD-801.
- LEAD-802: order amount/currency conflicts with official AED 1,200 pricing; finance reconciliation required.

## Important prototype limitation
The supplied data are processed using transparent deterministic rules and analyst-authored evidence-based audit judgments. This repository does **not** claim that a live LLM, telephony integration, CRM API, WhatsApp API or n8n workflow was executed. The prompts and architecture specify how to productionize the pipeline. WhatsApp messages are drafts, not sent messages.

## Safety
Never send a follow-up without consent and local-time/frequency checks. Paid, duplicate, do-not-contact, compliance-hold and child-welfare cases are suppressed or routed for human review.
