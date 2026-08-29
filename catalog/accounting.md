# accounting

14 skills. Fetch a skill's real instructions from its URL before applying it.
Descriptions are the authors' own, unedited -- including the "Do NOT use for" clauses,
which are load-bearing: they are how you tell near-misses apart.

## green-invoice  `Sx`
Integrate Green Invoice (Morning) API for Israeli invoicing, receipts, client management, and payment processing. Use when user asks to create invoices via Green Invoice, generate hashbonit mas through Morning API, manage clients in Green Invoice, set up webhook automation for document creation, query documents or expenses, or mentions "Green Invoice", "Morning", "hashbonit yeruka", "greeninvoice API", Israeli cloud invoicing, or needs to create tax invoice-receipt (cheshbonit mas/kabala). Covers all 15 document types, 8 payment types, client CRUD, item catalog, and webhook integration. Do NOT use for SHAAM allocation numbers or Tax Authority e-invoice compliance (use israeli-e-invoice), Cardcom payment processing (use cardcom-payment-gateway), or Tranzila integration (use tranzila-payment-gateway).
`https://raw.githubusercontent.com/skills-il/accounting/master/green-invoice/SKILL.md`

## gws-israeli-business-sheets  `Sc`
Google Sheets financial tracking and automation for Israeli freelancers and small businesses using the Google Workspace CLI (gws). Use when user asks to create income/expense sheets with Shekel formatting, track VAT (18%) calculations, generate tax-period summaries for accountants, backup spreadsheets as CSV, or auto-log payments. Do NOT use for direct bank API integrations, payroll processing, or filing taxes with the Israel Tax Authority.
`https://raw.githubusercontent.com/skills-il/accounting/master/gws-israeli-business-sheets/SKILL.md`

## hashavshevet-data-tools  `-`
Import and export data between Hashavshevet accounting software and modern formats (JSON, CSV, Excel). Use when you need to extract journal entries, chart of accounts, trial balances, or customer/supplier lists from Hashavshevet, import bank transactions and invoices into Hashavshevet format, migrate data from Hashavshevet to cloud-based solutions (iCount, Rivhit, Invoice4U), or handle Hebrew encoding conversions (Windows-1255 to UTF-8). Supports Hashavshevet Gold, Hashavshevet 2000+, and newer versions. Validates data integrity during import/export operations. Do NOT use for real-time Hashavshevet API integrations, direct database modifications, or live bookkeeping within Hashavshevet.
`https://raw.githubusercontent.com/skills-il/accounting/master/hashavshevet-data-tools/SKILL.md`

## israeli-annual-reports  `Sc`
Not investment advice and not a recommendation to buy or sell. Navigate and analyze Israeli corporate annual reports (dochot titkuftiim), financial filings, and regulatory disclosures. Use when user asks about Israeli annual reports, MAYA filings, IFRS financial statements, doch titkufti, dochot kaspiyim, or Companies Law reporting requirements. Covers TASE filing types, Israeli GAAP to IFRS transition, Hebrew financial terminology, and key financial statement analysis.
`https://raw.githubusercontent.com/skills-il/accounting/master/israeli-annual-reports/SKILL.md`

## israeli-attendance-wage-checker  `Sc`
>-
`https://raw.githubusercontent.com/skills-il/accounting/master/israeli-attendance-wage-checker/SKILL.md`

## israeli-bank-reconciliation  `-`
Not accounting or tax advice. Automates bank reconciliation for Israeli banks and credit-card issuers (Leumi, Hapoalim, Discount, Mizrahi Tefahot, Beinleumi/FIBI, Otsar Hahayal, Mercantile, Massad, Yahav, OneZero, and the card issuers Isracard, Max, Visa Cal, Amex) using the israeli-bank-scrapers library. Matches scraped or imported transactions to invoices and receipts, detects discrepancies, and generates reconciliation reports with matched, unmatched, and suspicious entries. Handles shekel amounts, Hebrew merchant names, and Israeli date formats. Use when you need to reconcile bank statements against your accounting records, identify missing invoices, or prepare monthly closing reports for Israeli business accounts. Do NOT use for international bank accounts, cryptocurrency wallets, or investment portfolio reconciliation.
`https://raw.githubusercontent.com/skills-il/accounting/master/israeli-bank-reconciliation/SKILL.md`

## israeli-bookkeeping-automation  `-`
Generate proper double-entry journal entries (pkudat yoman) for common Israeli business transactions including payroll with all statutory components, VAT handling, asset depreciation, and revenue recognition. Use when you need to create accurate bookkeeping entries using an illustrative Israeli account-numbering convention that you map onto the business's own kartesset and its Form 6111 codes. Supports both Osek Murshe (authorized dealer) double-entry and Osek Patur (exempt dealer) single-entry bookkeeping. Handles salary payments with income tax, bituach leumi, health insurance, pension, keren hishtalmut, and convalescence pay. Do NOT use for tax filing submissions, annual financial statement audits, or replacing a certified public accountant (roeh heshbon).
`https://raw.githubusercontent.com/skills-il/accounting/master/israeli-bookkeeping-automation/SKILL.md`

## israeli-e-invoice  `Sc`
Generate, validate, and manage Israeli e-invoices (hashbonit electronit) per Tax Authority (SHAAM) standards. Use when user asks to create Israeli invoices, request allocation numbers, validate invoice compliance, or asks about "hashbonit", "e-invoice", "SHAAM", "allocation number", or Israeli invoicing requirements. Uses the official SHAAM document type codes including transaction invoice (300), tax invoice (305), periodic tax invoice (310), tax invoice/receipt (320), credit invoice (330), and proforma (332). Do NOT use for general accounting, bookkeeping, or non-Israeli invoice formats.
`https://raw.githubusercontent.com/skills-il/accounting/master/israeli-e-invoice/SKILL.md`

## israeli-expense-categorizer  `-`
AI-powered categorization of business expenses into Israeli tax-deductible categories based on current Israeli Tax Ordinance rules. Applies the correct deduction mechanics (vehicle = the higher of running-costs-minus-use-value or 45%, mobile phone with the ~50% disallowance floor, home office and internet proportional), maps to a common Israeli chart of accounts, and handles Osek Patur vs Osek Murshe differences for VAT eligibility (private-car VAT not deductible, running-cost VAT two-thirds). Use when you need to classify business expenses for Israeli tax reporting, prepare expense reports for your accountant, or verify deduction eligibility. Do NOT use for final tax filing, legal tax advice, or payroll-related expense processing.
`https://raw.githubusercontent.com/skills-il/accounting/master/israeli-expense-categorizer/SKILL.md`

## israeli-financial-reports  `-`
Generate Israeli-standard financial reports including profit and loss (Doch Revach VeHefsed), balance sheet (Maazan), trial balance (Maazan Bochein), and cash flow statements. Supports bilingual Hebrew/English output with NIS formatting, VAT summary reports for bi-monthly and monthly filing, year-end annual report preparation, and comparison periods. Works with Osek Patur, Osek Murshe, and Chevra (company) business types. Reflects the Israeli accounting-standards regime where full IFRS is mandatory only for public companies while private companies may use Israeli GAAP or IFRS for SMEs. Use when you need to produce financial statements, tax-related summaries, or periodic reports for Israeli businesses. Exports to PDF, Excel, and CSV formats. Do NOT use for tax filing submissions, payroll processing, or bank reconciliation workflows.
`https://raw.githubusercontent.com/skills-il/accounting/master/israeli-financial-reports/SKILL.md`

## israeli-healthcare-payroll  `Sc`
Explains and sanity-checks the salary of Israeli public-healthcare-sector workers (nurses / achim ve'achayot, allied-health / miktzo'ot habriut such as physiotherapists, occupational therapists, dietitians, and speech clinicians, hospital pharmacists, and doctors / rofim), which is set by public-sector collective agreements, not private-sector negotiation. Use when a user asks how a healthcare payslip is built: which wage grade (dirug) applies, the base combined-salary cell (grade daraga by seniority vetek), healthcare tosafot like the nurses' tosefet achayot or the allied-health training supplement, shift and on-call pay (mishmarot, kononut, toranut), and how gross becomes net. Do NOT use for standard private-sector gross-to-net payroll (use israeli-payroll-calculator), teachers' pay (use israeli-teacher-payroll), or private home caregivers (use foreign-caregiver-payroll).
`https://raw.githubusercontent.com/skills-il/accounting/master/israeli-healthcare-payroll/SKILL.md`

## israeli-payroll-calculator  `Sc`
Calculate Israeli payroll including income tax, Bituach Leumi (National Insurance), health tax, pension contributions, shovi rechev (company-car use value), and net salary. Use when user asks to calculate salary, "tlush maskoret", payroll deductions, "bruto to neto", employer cost, tax credits (nekudot zikui), company car impact on salary, or needs help understanding Israeli payslip items. Covers employees, freelancers (atzmai), and employer cost calculations. This skill starts from an AGREED GROSS. Do NOT use it to work out what gross is owed from a timesheet, or to check overtime, weekly-rest premium or a missing hours record (use israeli-attendance-wage-checker), and do NOT use it for US, UK, or other countries' payroll calculations.
`https://raw.githubusercontent.com/skills-il/accounting/master/israeli-payroll-calculator/SKILL.md`

## israeli-receipt-scanner  `-`
OCR and parse Israeli receipts and invoices with Hebrew and English text extraction. Extracts merchant name, date, total amount in NIS, VAT amount, receipt or invoice number, payment method, and VAT registration number (osek murshe). Handles common Israeli retail formats including supermarkets, gas stations, restaurants, and online purchases. Auto-categorizes expenses into standard Israeli accounting categories and outputs structured JSON or CSV ready for import into accounting software. Use when you need to digitize, extract data from, or categorize Israeli receipts and tax invoices. Do NOT use for non-Israeli receipt formats, handwritten notes without printed text, or bank statement reconciliation.
`https://raw.githubusercontent.com/skills-il/accounting/master/israeli-receipt-scanner/SKILL.md`

## israeli-teacher-payroll  `Sc`
Computes and explains the salary of Israeli teachers (ovdei horaa / sachar ovdei horaa) under the two collective-agreement reforms: Ofek Chadash (ofek chadash, New Horizon, covering kindergartens, elementary, and junior-high) and Oz LaTmura (oz latmura, upper-secondary only). Use when a user asks how a teacher's pay is built: reform, rank (daraga), seniority (vetek), the weekly work-week split between front-of-class hours and private (pratani) hours, gmul (gmul) increments like gmul hishtalmut or gmul chinuch, and how gross becomes net. Also handles the split appointment, where one teacher teaches in both a junior-high and a high school and earns under both reforms at once, each part by its position fraction. Do NOT use for standard private-sector gross-to-net payroll (use israeli-payroll-calculator), bookkeeping journal entries (use israeli-bookkeeping-automation), or Bagrut and school-system navigation (use israeli-education-system).
`https://raw.githubusercontent.com/skills-il/accounting/master/israeli-teacher-payroll/SKILL.md`
