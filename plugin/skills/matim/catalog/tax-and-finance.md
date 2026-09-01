# tax-and-finance

40 skills. Fetch a skill's real instructions from its URL before applying it.
Descriptions are the authors' own, unedited -- including the "Do NOT use for" clauses,
which are load-bearing: they are how you tell near-misses apart.

## american-freelancer-israel-tax  `Sc`
Not tax advice and not a filed return. Works out the US self-employment tax an American osek patur or osek murshe in Israel owes on top of Bituach Leumi, because there is no US-Israel totalization agreement and the foreign earned income exclusion does not reduce SE tax. Projects the yearly bill from net earnings, explains the quarterly estimated payment cycle, and lays out the structural options and their trade-offs without recommending one. Use when a US citizen or green card holder freelancing in Israel asks why they owe US tax despite paying Israeli tax, what SE tax is, whether the exclusion covers it, or how much to set aside. Produces a projection worksheet, never a filed return. Do NOT use for annual filing mechanics or FBAR, for classifying Israeli funds as PFICs, for Israeli-side bookkeeping or VAT, or for advice on whether to incorporate.
https://agentskills.co.il/he/skills/american-freelancer-israel-tax
`https://raw.githubusercontent.com/skills-il/tax-and-finance/master/american-freelancer-israel-tax/SKILL.md`

## boi-economic-data  `Si`
Fetch and analyze Bank of Israel (BOI) economic data: interest rates, CPI (madad hamchirim), exchange rates (sha'ar yatzig), and CBS statistics. Use when user asks about BOI interest rate, ribit Bank Israel, exchange rates, sha'ar yatzig, CPI index, madad, inflation data, or Israeli economic indicators. Foundation skill for Israeli financial analytics. Provides API access to the BOI SDMX API at edge.boi.gov.il and CBS data. Do NOT use for stock market data (use tase-stock-analysis instead) or for currency conversion (use shekel-currency-converter instead).
https://agentskills.co.il/he/skills/boi-economic-data
`https://raw.githubusercontent.com/skills-il/tax-and-finance/master/boi-economic-data/SKILL.md`

## cardcom-payment-gateway  `Sc`
Not tax or accounting advice. Integrate Cardcom payment processing and Israeli invoice generation into applications, covering Low Profile payments, tokenization, recurring billing, and automatic tax invoice/receipt creation per Israeli law. Use when user asks to accept payments via Cardcom, generate Israeli invoices with payments, set up "slikat ashrai" with hashbonit, handle recurring billing (hora'ot keva), or mentions "Cardcom", "CardCom API", "Low Profile", Israeli payment with invoicing, or needs combined payment plus document generation. Targets the REST API V11. Do NOT use for Tranzila integration (use tranzila-payment-gateway), general accounting, or non-payment queries.
https://agentskills.co.il/he/skills/cardcom-payment-gateway
`https://raw.githubusercontent.com/skills-il/tax-and-finance/master/cardcom-payment-gateway/SKILL.md`

## dual-listed-arbitrage  `Sc`
>-
https://agentskills.co.il/he/skills/dual-listed-arbitrage
`https://raw.githubusercontent.com/skills-il/tax-and-finance/master/dual-listed-arbitrage/SKILL.md`

## grow-payment-gateway  `-`
Integrate Grow by Meshulam payment gateway into Israeli applications -- covers payment pages (iframe/redirect/SDK), tokenization, recurring billing, payment links, refunds, invoices, webhooks, and 3DS authentication via the Grow Light API. Use when user asks to accept payments via Grow or Meshulam, set up "slikat ashrai" with Grow, create payment links (drishat tashlum), handle recurring charges (hora'ot keva) via Grow tokens, process refunds or Bit cancellations, integrate Grow webhooks, or mentions "Grow", "Meshulam", "grow-il", "meshulam.co.il", Grow payment page, or Grow API. Prevents costly integration mistakes by guiding correct FormData request format, server-side-only restrictions, and the mandatory approveTransaction step that many developers miss. Do NOT use for Cardcom integration (use cardcom-payment-gateway), Tranzila integration (use tranzila-payment-gateway), general payment orchestration across multiple gateways (use israeli-payment-orchestrator), or non-payment queries.
https://agentskills.co.il/he/skills/grow-payment-gateway
`https://raw.githubusercontent.com/skills-il/tax-and-finance/master/grow-payment-gateway/SKILL.md`

## il-invoice-organizer  `Sc`
Parse and organize Hebrew invoices for Israeli bookkeeping: VAT 1/6 extraction, Tax Authority expense categories, Osek Murshe/Patur recognition, and accountant-ready export. Use when user asks about organizing invoices, cheshbonit, expense categorization, sivug hotza'ot, VAT extraction from totals, Osek Murshe vs Osek Patur rules, or preparing documents for their accountant (ro'eh cheshbon). Supports Hebrew OCR text parsing and automatic categorization per Tax Authority standards. Do NOT use for invoice generation (use israeli-e-invoice instead) or for VAT report filing (use israeli-vat-reporting instead).
https://agentskills.co.il/he/skills/il-invoice-organizer
`https://raw.githubusercontent.com/skills-il/tax-and-finance/master/il-invoice-organizer/SKILL.md`

## israeli-arnona-optimizer  `Sc`
Calculate municipal property tax (arnona) for Israeli properties, check discount eligibility, and draft appeal letters to arnona committees. Use when a user needs to estimate arnona payments by municipality, zone, and property usage type, verify eligibility for discounts (olim, soldiers, elderly, disabled, low income, students, single parents), or prepare formal appeals with legal references. Covers all major Israeli municipalities including Tel Aviv, Jerusalem, Haifa, and Beer Sheva. Do NOT use for income tax (mas hachnasa), VAT (maam), or national insurance (bituach leumi) calculations, which fall under separate Israeli tax authorities.
https://agentskills.co.il/he/skills/israeli-arnona-optimizer
`https://raw.githubusercontent.com/skills-il/tax-and-finance/master/israeli-arnona-optimizer/SKILL.md`

## israeli-bank-connector  `Sc`
Analyze Israeli bank transactions, spending patterns, and financial data across Israeli banks and credit card companies. Use when user asks about bank transactions, spending analysis, "cheshbon bank", budget tracking, or needs to categorize Israeli banking data. Pairs with israeli-bank-mcp and il-bank-mcp servers (which wrap the israeli-bank-scrapers library) to add financial-analysis workflows. Supports Hapoalim, Leumi, Discount, Mercantile, Mizrahi-Tefahot, First International (FIBI), Otsar HaHayal, Pagi, Union, Yahav, Massad, OneZero, Behatsdaa, Beyahad Bishvilha, Visa Cal, Max, Isracard, and Amex. Do NOT use for payment initiation, money transfers, or investment advice.
https://agentskills.co.il/he/skills/israeli-bank-connector
`https://raw.githubusercontent.com/skills-il/tax-and-finance/master/israeli-bank-connector/SKILL.md`

## israeli-budget-planner  `Sc`
Not tax, pension or investment advice, and not a mortgage approval. Plan household and personal budgets with Israeli-specific costs, rates, and financial products. Use when user asks about budgeting in Israel, mortgage (mashkanta) calculations, arnona rates, cost of living, takciv, or monthly expense planning. Covers Bank of Israel prime rate, mashkanta tracks, arnona, household health costs (mas briut / health-tax), and Israeli household benchmarks.
https://agentskills.co.il/he/skills/israeli-budget-planner
`https://raw.githubusercontent.com/skills-il/tax-and-finance/master/israeli-budget-planner/SKILL.md`

## israeli-client-payment-chaser  `-`
Chase unpaid invoices and manage debt collection for Israeli freelancers and businesses. Use when user asks about "unpaid invoices Israel", "payment reminder", "invoice aging", "debt collection freelancer", "Michtav Drisha (pre-suit demand letter)", "demand letter Hebrew", "tvi'ot ktanot", or "גביית חובות". Covers graduated WhatsApp/email reminder escalation, Hebrew demand letter generation, Small Claims Court eligibility assessment, and Shabbat/holiday-aware scheduling. Do NOT use for invoice generation (use israeli-e-invoice) or general accounting.
https://agentskills.co.il/he/skills/israeli-client-payment-chaser
`https://raw.githubusercontent.com/skills-il/tax-and-finance/master/israeli-client-payment-chaser/SKILL.md`

## israeli-company-valuation  `Sc`
Builds an indicative valuation range for an Israeli private company using DCF, market multiples, and the asset approach, with a WACC build-up that uses a live Israeli risk-free rate, the current Israel country risk premium, and the company's own effective tax rate rather than a generic 23%. Use when someone asks what their company is worth, is buying or selling a private Israeli business, needs a valuation for a share transfer or a Section 104 reorganization, or wants to sanity-check a valuation someone else produced. A US-textbook valuation misses Israel's country risk premium, taxes a preferred-enterprise company at the statutory rate, and returns one point estimate instead of a range. Early-stage companies are in scope via round-based methods. Do NOT use for real estate appraisal, listed shares, a startup investment memo, salary versus dividend planning, employee option tax, or a signed valuation opinion for filing.
https://agentskills.co.il/he/skills/israeli-company-valuation
`https://raw.githubusercontent.com/skills-il/tax-and-finance/master/israeli-company-valuation/SKILL.md`

## israeli-consumer-fee-fighter  `Sc`
Use when an Israeli consumer wants to cut recurring bank and credit-card charges: cancel a credit card cleanly (bitul kartis ashrai), switch to a cheaper fixed-price bank fee track (maslul amlot: basic maslul basi or expanded maslul murchav), switch banks in one click (niud / maavar beklik), stop a recurring debit (bitul harshaa lechiyuv / horaat keva), or negotiate lower fees and commissions (amlot including overdraft, FX, and securities fees). Produces a ready-to-send Hebrew cancellation letter, a rights-grounded negotiation script, and a short rights summary, grounded in Bank of Israel fee rules and Israeli consumer-banking law. Do NOT use for maximizing cashback or deals (use israeli-smart-saver), coupon hunting (use israeli-coupon-code-finder), analyzing bank transactions (use israeli-bank-connector), or household budgeting (use israeli-budget-planner).
https://agentskills.co.il/he/skills/israeli-consumer-fee-fighter
`https://raw.githubusercontent.com/skills-il/tax-and-finance/master/israeli-consumer-fee-fighter/SKILL.md`

## israeli-corporate-tax-strategy  `Sc`
Strategic tax analysis for Israeli company owners (baalei shlita) comparing salary, dividends, shareholder loans, and management fees as profit extraction methods. Use when user asks about paying personal tax from company funds, dividend vs salary comparison, shareholder loan tax implications, Section 3(tet) deemed interest, corporate profit extraction strategy, halokat dividendim, mashichat rvaachim, or baal shlita tax planning. Calculates total tax burden across methods, identifies optimal strategy based on assessment amount and company structure, and verifies compliance with Israeli Tax Authority rules. Prevents costly extraction mistakes by analyzing withholding, Bituach Leumi, surtax, and corporate tax interactions. Do NOT use for VAT reporting (use israeli-vat-reporting), payroll processing (use israeli-payroll-calculator), annual tax return filing (use israeli-tax-returns), or crypto tax (use israeli-crypto-tax-reporter).
https://agentskills.co.il/he/skills/israeli-corporate-tax-strategy
`https://raw.githubusercontent.com/skills-il/tax-and-finance/master/israeli-corporate-tax-strategy/SKILL.md`

## israeli-coupon-code-finder  `Sc`
Hunt for currently-valid discount and coupon codes for an Israeli online-store checkout, verify each candidate, and return one ranked summary instead of asking five chatbots the same question. Runs a fixed Israeli source map (coupon aggregators, cashback platforms, credit-card benefit hubs, gift-card stacking, store-direct levers, seasonal sale windows) plus a Hebrew search playbook, then checks every candidate for expiry, minimum cart, new-customer-only, and stacking rules. Use when a user is about to buy on an Israeli store and asks to find coupon codes, a discount code, kod kupon, kupon hanacha, or 'is this coupon site legit'. Never invents codes: it only reports codes found via live web search, each with source and date. Do NOT use for ongoing savings strategy or cashback-account setup (israeli-smart-saver), cross-store price comparison (israeli-product-price-comparator), or grocery prices (israeli-grocery-price-intelligence).
https://agentskills.co.il/he/skills/israeli-coupon-code-finder
`https://raw.githubusercontent.com/skills-il/tax-and-finance/master/israeli-coupon-code-finder/SKILL.md`

## israeli-crypto-tax-reporter  `Sc`
Calculate cryptocurrency capital gains tax per Israeli Tax Authority (Reshut HaMisim) regulations and generate capital-gains reporting data and Form 1399י advance-payment data (within 30 days of disposal). Use when a user needs to compute crypto tax obligations using FIFO cost basis, classify DeFi income (staking, liquidity mining, airdrops) for Israeli tax purposes, prepare annual tax filing data, understand reporting thresholds and advance payment (mikdamot) requirements, or evaluate the Voluntary Disclosure Procedure (Nohal Gilui Mirtzon) for unreported crypto, checking whether the window is currently open before relying on it. Covers Section 88 of the Income Tax Ordinance, Circular 2018/05, the 25% capital gains rate for individuals, and the 5% surtax on capital income above NIS 721,560 (threshold frozen through 2027). Do NOT use for non-Israeli tax jurisdictions, general income tax calculations, or VAT (maam) on crypto business activities, which require separate professional consultation.
https://agentskills.co.il/he/skills/israeli-crypto-tax-reporter
`https://raw.githubusercontent.com/skills-il/tax-and-finance/master/israeli-crypto-tax-reporter/SKILL.md`

## israeli-customs-duty-calculator  `Sc`
Not customs advice. Classify products into Israeli 8-digit HS codes and calculate full landed cost for imports to Israel: customs duty, VAT 18%, and purchase tax (mas kniya). Use when user asks about Israel import tax, personal import threshold, customs duty on an online order from Amazon/AliExpress, FTA preferences from US/EU/UK/Canada, Shaar Olami tariff lookup, or the cost of bringing goods into Israel. Do NOT use for domestic VAT bookkeeping (use israeli-vat-reporting) or for export documentation (use israeli-export-shipping-kit).
https://agentskills.co.il/he/skills/israeli-customs-duty-calculator
`https://raw.githubusercontent.com/skills-il/tax-and-finance/master/israeli-customs-duty-calculator/SKILL.md`

## israeli-employee-tax-refund  `Sc`
Walk salaried Israeli employees through the voluntary tax-refund process with Reshut HaMisim. Reads Form 106, detects refund triggers (job change, unemployment, maternity leave, reserve duty, Section 46 donations, yishuv mezakeh, missed credit points, disability, alimony, early keren hishtalmut withdrawal), estimates the refund using 2026 brackets and credit-point values, generates a per-trigger document checklist, and fills Form 135 or routes the user to the online refund portal. Knows the 6-year window (Section 160 ITO). Use when a salaried employee asks about Israeli tax refund, החזר מס לשכירים, טופס 135, miluim refund, or refunds for previous tax years. Do NOT use for self-employed Form 1301 filers (use israeli-tax-returns), payroll math (use israeli-payroll-calculator), stock options (use israeli-stock-options-tax), crypto (use israeli-crypto-tax-reporter), or VAT (use israeli-vat-reporting).
https://agentskills.co.il/he/skills/israeli-employee-tax-refund
`https://raw.githubusercontent.com/skills-il/tax-and-finance/master/israeli-employee-tax-refund/SKILL.md`

## israeli-export-shipping-kit  `Sc`
Generate the full export document set for Israeli exporters: commercial invoice (HE+EN), packing list, bill of lading / AWB / CMR, proforma, and origin documents (EUR.1, invoice origin declaration, US-Israel Origin Invoice Declaration, CIFTA Form B239). Use when user asks about exporting from Israel, Incoterms (FOB, CIF, DDP, EXW), EUR.1 certificate, approved exporter status, US-Israel FTA certificate of origin, commercial invoice template, or packing list. Do NOT use for import calculations (use israeli-customs-duty-calculator) or domestic VAT bookkeeping (use il-invoice-organizer).
https://agentskills.co.il/he/skills/israeli-export-shipping-kit
`https://raw.githubusercontent.com/skills-il/tax-and-finance/master/israeli-export-shipping-kit/SKILL.md`

## israeli-freelancer-ops  `-`
Manage daily operations for Israeli freelancers (osek murshe, osek patur) - invoice aging with collection reminders, utility bill collection via browser automation, tax deadline alerts (VAT, Bituach Leumi, mkdamot, annual report), osek patur threshold monitoring, and organized accountant packages (havila). Use when a freelancer needs help tracking invoices, preparing documents for their accountant, monitoring their osek patur revenue ceiling, or staying on top of Israeli tax filing deadlines. Prevents missed VAT filings (which trigger automatic penalties), forgotten invoice follow-ups, and disorganized handoffs to accountants. Do NOT use for VAT return preparation (use israeli-vat-reporting), e-invoice generation (use israeli-e-invoice), or payroll/employee management.
https://agentskills.co.il/he/skills/israeli-freelancer-ops
`https://raw.githubusercontent.com/skills-il/tax-and-finance/master/israeli-freelancer-ops/SKILL.md`

## israeli-insurance-comparator  `-`
Not insurance advice and not insurance marketing. Compare car insurance (mandatory hova, comprehensive makif, third-party), home insurance, and health supplementary insurance across 20+ Israeli insurers using official government calculators and private comparison platforms. Use when a user needs to find the cheapest insurance quote, understand policy differences, or prepare for annual renewal negotiations. Guides through CMA calculator at car.cma.gov.il, Hova.co.il, Shukabit, Wobi, and Bestie. Do NOT use for life insurance, pension fund selection, or travel insurance comparisons.
https://agentskills.co.il/he/skills/israeli-insurance-comparator
`https://raw.githubusercontent.com/skills-il/tax-and-finance/master/israeli-insurance-comparator/SKILL.md`

## israeli-insurance-duplication-checker  `-`
Not insurance advice and not insurance marketing. Audits the insurance an Israeli household already pays for, across health, long-term care, dental, disability, life, personal accident, motor, home, mortgage, travel and service riders, and separates real duplication from cover that legitimately stacks. Use when a user asks whether they are paying twice for insurance, wants to cut insurance costs, mentions כפל ביטוחי, holds a שב\"ן plan alongside a private health policy, has surgery cover through an employer or professional group, pays for a private ביטוח סיעודי next to the kupa group policy, wonders whether a private אכ\"ע policy is redundant next to the pension fund, or asks which policy to cancel first. Do NOT use for comparing or buying new policies (israeli-insurance-comparator), for co-pays and costs inside the public health system (israeli-hmo-navigator), or for the pension savings product itself (israeli-pension-advisor).
https://agentskills.co.il/he/skills/israeli-insurance-duplication-checker
`https://raw.githubusercontent.com/skills-il/tax-and-finance/master/israeli-insurance-duplication-checker/SKILL.md`

## israeli-mortgage-comparator  `-`
Compare mortgage tracks (maslulei mashkanta) across Israeli banks, calculate monthly payments for mixed-track portfolios, and understand Bank of Israel Directive 329 limits including LTV ceilings, the payment-to-income prohibition, and the cap on the variable-rate share. Use when a user needs to evaluate mortgage offers from different banks, calculate refinancing savings, or understand how Prime rate changes affect their payments. Covers Leumi, Hapoalim, Discount, Mizrachi-Tefahot, FIBI, Mercantile, and Yahav. Do NOT use for commercial real estate loans, business credit lines, or non-Israeli mortgage products.
https://agentskills.co.il/he/skills/israeli-mortgage-comparator
`https://raw.githubusercontent.com/skills-il/tax-and-finance/master/israeli-mortgage-comparator/SKILL.md`

## israeli-payment-orchestrator  `Sc`
Orchestrate Israeli payment gateways (Cardcom, Tranzila, PayMe, Meshulam, iCredit, Pelecard) with unified routing, fallback, and installments (tashlumim). Use when user asks about multi-gateway payment integration, "slikat kartisim", "tashlumim", payment routing, Shva network, BOI payment-services regulation, gateway comparison, or building a payment abstraction layer for Israeli merchants. Provides unified API patterns, installment handling, Shva clearing rules, and regulatory compliance. Do NOT use for single gateway setup (use cardcom-payment-gateway or tranzila-payment-gateway instead).
https://agentskills.co.il/he/skills/israeli-payment-orchestrator
`https://raw.githubusercontent.com/skills-il/tax-and-finance/master/israeli-payment-orchestrator/SKILL.md`

## israeli-pension-advisor  `Sc`
Navigate the Israeli pension and savings system including pension funds (keren pensia), manager's insurance (bituach menahalim), training funds (keren hishtalmut), severance handling at Form 161, Tikun 190 post-60 deposits, and retirement planning. Use when user asks about Israeli pension, \"pensia\", \"keren hishtalmut\", retirement savings, \"bituach menahalim\", pension contributions, tax benefits from savings, severance withdrawal vs continuity, or pension at divorce / relocation. Uninformed pension decisions cost hundreds of thousands of NIS over a lifetime. Covers mandatory pension, voluntary savings, withdrawal rules, and life events (divorce, relocation, death). Do NOT provide specific investment recommendations or fund performance comparisons.
https://agentskills.co.il/he/skills/israeli-pension-advisor
`https://raw.githubusercontent.com/skills-il/tax-and-finance/master/israeli-pension-advisor/SKILL.md`

## israeli-price-quote-generator  `Sc`
Generate compliant Hebrew price quotes (hatzaat mechir / הצעת מחיר) for Israeli freelancers and small businesses. Use when user asks to create a price quote, quote a client, build a pre-sale proposal with VAT, send a hatzaat mechir, or draft a הצעת מחיר. Covers 18% VAT math (or VAT-exempt for oseik patur), validity period (תוקף ההצעה), payment terms aligned with Chok Moser Tashlumim leSapakim 5777-2017 (the Late Payment Law: shotef+30, statutory default shotef+45 for B2B), oseik murshe vs oseik patur header rules, escalation and cancellation clauses, Bit/PayBox/bank transfer payment details, and bilingual HE/EN layout. Outputs ready-to-send Hebrew markdown or printable HTML. Do NOT use for government tender proposals (use israeli-tender-proposal-builder), for generating actual tax invoices after the quote is accepted (use green-invoice), or for chasing unpaid invoices (use israeli-client-payment-chaser).
https://agentskills.co.il/he/skills/israeli-price-quote-generator
`https://raw.githubusercontent.com/skills-il/tax-and-finance/master/israeli-price-quote-generator/SKILL.md`

## israeli-property-appraisal  `Sx`
>-
https://agentskills.co.il/he/skills/israeli-property-appraisal
`https://raw.githubusercontent.com/skills-il/tax-and-finance/master/israeli-property-appraisal/SKILL.md`

## israeli-smart-saver  `-`
Not legal advice. Save money in Israel through smart shopping, cashback optimization, subscription auditing, and deal hunting. Covers Zap.co.il price comparison, BuyMe gift card strategies, Cashback.co.il and Cashdo rebate programs, credit card perks maximization (Visa Cal, Max, Isracard), loyalty program stacking, seasonal sale timing, and recurring expense optimization. Use when user asks about "lachsoch kesef", saving money in Israel, Israeli coupons, cashback, "hashvaat mechirim", subscription audit, "kamah ani meshalem", credit card benefits, "hotza'ot", reducing expenses, or smart shopping tips. Helps Israelis reduce monthly spending by identifying unnecessary subscriptions, switching to cheaper alternatives, and maximizing cashback on everyday purchases. Do NOT use for investment advice (use israeli-pension-advisor), mortgage comparison (use israeli-mortgage-comparator), or grocery price comparison (use israeli-grocery-price-intelligence).
https://agentskills.co.il/he/skills/israeli-smart-saver
`https://raw.githubusercontent.com/skills-il/tax-and-finance/master/israeli-smart-saver/SKILL.md`

## israeli-startup-investment-analyzer  `Sc`
Generate a structured investment memo for an Israeli startup deal: market, team, metrics sanity-check, valuation and dilution math, key risks, and a prioritized list of diligence questions. Built for angel and VC investors evaluating an inbound deck or data room. Catches Israel-specific landmines a generic analysis misses: Innovation Authority (rashut hachadshanut) grant overhang and IP-out restrictions, the Delaware flip, Section 102 option plans, founder vesting, and Companies Registrar standing. Use when an investor asks to evaluate a startup, screen a deal, review a pitch deck, write an investment memo, run dilution math, or list diligence questions. Why it matters: an Innovation Authority royalty or IP-out overhang can shrink or block an exit. Do NOT use for founder-side company formation or fundraising (israeli-startup-toolkit), employee option taxation (israeli-stock-options-tax), or public-market TASE stock analysis (tase-stock-analysis).
https://agentskills.co.il/he/skills/israeli-startup-investment-analyzer
`https://raw.githubusercontent.com/skills-il/tax-and-finance/master/israeli-startup-investment-analyzer/SKILL.md`

## israeli-stock-options-tax  `-`
Calculate tax on stock options and RSUs for Israeli tech employees under Section 102. Use when user asks about option exercise tax, RSU taxation, startup exit proceeds, Section 102 tracks, trustee holding period, capital gains vs income track comparison, or 'how much tax on my options'. Walks through a detailed tax breakdown with net proceeds. Do NOT use for crypto tax (use israeli-crypto-tax-reporter), ESOP plan setup (use israeli-startup-toolkit), controlling shareholder profit extraction (use israeli-corporate-tax-strategy), annual tax returns (use israeli-tax-returns), or payroll (use israeli-payroll-calculator).
https://agentskills.co.il/he/skills/israeli-stock-options-tax
`https://raw.githubusercontent.com/skills-il/tax-and-finance/master/israeli-stock-options-tax/SKILL.md`

## israeli-tax-returns  `-`
Prepare and file Israeli tax returns with Reshut HaMisim. Covers Form 1301 (individual), Form 1214 (corporate), Form 126 (employer salary), Form 856 (supplier payments), Form 6111 (financial statements), mikdamot (advance payments), Mas Shevach (real estate capital gains), and securities capital gains (Forms 1322/1325). Use when user asks about "doch shnati", "tax return Israel", "Form 1301", "Form 1214", "mas hachnasa", "mikdamot", "mas shevach declaration", "capital gains report", "nekudot zikui", "mas yesafim", or "דוח שנתי". Guides income classification, deductions, tax credits, surtax, deadlines, and SHAAM submission. Do NOT use for VAT reporting (use israeli-vat-reporting), withholding tax (use israeli-tax-withholding), crypto tax (use israeli-crypto-tax-reporter), payroll (use israeli-payroll-calculator), invoicing (use israeli-e-invoice), or Section 102 employee stock options (use israeli-stock-options-tax).
https://agentskills.co.il/he/skills/israeli-tax-returns
`https://raw.githubusercontent.com/skills-il/tax-and-finance/master/israeli-tax-returns/SKILL.md`

## israeli-tax-withholding  `Sc`
Israeli tax withholding (nikui mas bemakor) rates, certificates, and calculations. Use when user asks about withholding tax, "nikui mas", withholding certificates, "ishur nikui", tax coordination (tium mas), or needs to calculate withholding amounts. Covers payments to suppliers, freelancers, landlords, and cross-border payments. Do NOT use for employee payroll tax (see israeli-payroll-calculator) or VAT reporting.
https://agentskills.co.il/he/skills/israeli-tax-withholding
`https://raw.githubusercontent.com/skills-il/tax-and-finance/master/israeli-tax-withholding/SKILL.md`

## israeli-toshav-chozer-vatik-tax-planner  `Sc`
Plans Section 14 tax exemption for an Israeli toshav chozer vatik (10+ years abroad). Distinguishes vatik (full 10-year foreign-income exemption) from regular toshav chozer (5-year passive + 10-year capital gains only), pins the 10-year clock to the tax-residency date (not arrival), surfaces the 2026 reporting change (Amendment 272 cancels 134b + 135(1)(b); tax stays exempt, reporting required for residents from 1.1.2026), flags the US-citizen dual-tax trap, and outputs a 10-year cash-flow projection. Triggers on "תושב חוזר ותיק", "סעיף 14", "פטור 10 שנים", "תיקון 272". Do NOT use for the returning-resident process (use israeli-returning-resident-navigator), vehicle/customs (use israeli-returning-resident-customs-vehicle), olim chadashim (use israeli-aliyah-navigator), or people leaving Israel (use israeli-relocation-abroad). Planning aid only, not binding tax advice.
https://agentskills.co.il/he/skills/israeli-toshav-chozer-vatik-tax-planner
`https://raw.githubusercontent.com/skills-il/tax-and-finance/master/israeli-toshav-chozer-vatik-tax-planner/SKILL.md`

## israeli-utility-rates-comparator  `-`
Compare electricity providers, water tariffs, cooking-gas (LPG) rates, cellular plans, fiber internet packages, and arnona (municipal property tax) across Israeli municipalities and utility companies. Use when a user needs to understand IEC tariff structures, calculate solar panel ROI, compare tiered water pricing, pick a cheap cellular plan, switch to fiber internet, or evaluate arnona differences between cities. Covers electricity market deregulation, independent power producers, Mekorot water pricing, cellular operators and MVNOs, fiber-optic infrastructure, and municipal rate variations. Do NOT use for commercial/industrial utility contracts at scale, or utility infrastructure investment analysis.
https://agentskills.co.il/he/skills/israeli-utility-rates-comparator
`https://raw.githubusercontent.com/skills-il/tax-and-finance/master/israeli-utility-rates-comparator/SKILL.md`

## israeli-vat-reporting  `Sc`
Prepare, validate, and guide submission of Israeli VAT reports (Doch Maam) per Tax Authority standards. Use when user asks about VAT reporting, VAT calculation, "doch maam", "maam", Israeli VAT filing, VAT deadlines, or input/output VAT reconciliation. Supports monthly, bi-monthly, and annual reporting. Handles zero-rated exports, exempt transactions, and Eilat zone rules. Do NOT use for income tax, corporate tax, or non-Israeli VAT systems.
https://agentskills.co.il/he/skills/israeli-vat-reporting
`https://raw.githubusercontent.com/skills-il/tax-and-finance/master/israeli-vat-reporting/SKILL.md`

## pelecard-payment-gateway  `Si`
Integrate Pelecard payment processing into Israeli web and mobile apps -- covers the iframe payment flow on gateway21.pelecard.biz, ActionType selection (J2/J4/J5/J5h), tashlumim (installments), tokenization, ConfirmationKey server-side validation via PaymentGW/GetTransaction, refunds, 3D Secure 2, Bit wallet, and Apple Pay via ClientSecure.js. Use when user asks to accept payments via Pelecard, set up slikat ashrai with Pelecard, validate a Pelecard callback, charge a saved Pelecard token, or mentions Pelecard, gateway21, PelecardStatusCode, or ConfirmationKey. Do NOT use for Cardcom (use cardcom-payment-gateway), Tranzila (use tranzila-payment-gateway), Grow/Meshulam (use grow-payment-gateway), multi-gateway orchestration (use israeli-payment-orchestrator), or invoice generation (use green-invoice).
https://agentskills.co.il/he/skills/pelecard-payment-gateway
`https://raw.githubusercontent.com/skills-il/tax-and-finance/master/pelecard-payment-gateway/SKILL.md`

## shekel-currency-converter  `Si`
Convert currencies to/from Israeli New Shekel (NIS/ILS) using Bank of Israel official representative rates (shaar yatzig). Use when user asks to convert shekels, NIS, ILS, asks about exchange rates, "shaar yatzig" (representative rate), or needs currency conversion for Israeli tax or business purposes. Covers the official Bank of Israel published currencies (14 currencies) with current and historical (tax-date) rates. Do NOT use for cryptocurrency or unofficial money exchange rates.
https://agentskills.co.il/he/skills/shekel-currency-converter
`https://raw.githubusercontent.com/skills-il/tax-and-finance/master/shekel-currency-converter/SKILL.md`

## tase-stock-analysis  `Sx`
Analyze Israeli stocks on TASE (Tel Aviv Stock Exchange), track TA-35 and TA-125 indices, and evaluate dual-listed companies (TASE + NASDAQ). Use when user asks about Israeli stocks, "boorsa", "TA-35", "TASE", Maya filings, dual-listed companies, or Israeli capital gains tax on securities. Provides index composition, Maya (TASE disclosure) filings lookup, capital gains tax calculations (25% on securities), and Bank of Israel interest rate context for valuation. Do NOT use for general international stock analysis unrelated to Israel, or for cryptocurrency trading.
https://agentskills.co.il/he/skills/tase-stock-analysis
`https://raw.githubusercontent.com/skills-il/tax-and-finance/master/tase-stock-analysis/SKILL.md`

## tranzila-payment-gateway  `Si`
Integrate Tranzila payment processing into Israeli applications -- covers iframe payments, tokenization, installments (tashlumim), refunds, 3D Secure, and Bit wallet. Use when user asks to accept payments via Tranzila, integrate Israeli credit card processing, set up "slikat ashrai", handle tashlumim (installment payments), create payment tokens, process refunds through Tranzila, or mentions "Tranzila", "tranzila API", "secure5", or Israeli online payments. Supports both legacy CGI endpoints and modern API V2. Do NOT use for Cardcom integration (use cardcom-payment-gateway), general accounting, or non-payment financial queries.
https://agentskills.co.il/he/skills/tranzila-payment-gateway
`https://raw.githubusercontent.com/skills-il/tax-and-finance/master/tranzila-payment-gateway/SKILL.md`

## us-israel-dual-tax-navigator  `Sc`
Not tax advice and not a filed return. Maps what a US-Israel dual citizen actually has to file in both systems for a tax year: the US 1040, FBAR (FinCEN 114), Form 8938, and how those line up against the Israeli calendar. Compares the Foreign Earned Income Exclusion against the Foreign Tax Credit, flags the revocation trap, and lays out the Streamlined Foreign Offshore route for someone who never filed after making aliyah. Use when a US citizen or green card holder in Israel asks what they owe the IRS, whether they need an FBAR, which years to catch up, or how to brief an accountant. Produces a filing-obligation map and a document checklist, never a completed or signed return. Do NOT use for Israeli-side filing, for classifying Israeli funds as PFICs, for self-employment tax, or for renouncing citizenship.
https://agentskills.co.il/he/skills/us-israel-dual-tax-navigator
`https://raw.githubusercontent.com/skills-il/tax-and-finance/master/us-israel-dual-tax-navigator/SKILL.md`

## us-person-israeli-investment-check  `Sc`
Not tax advice and not a filed return. Screens the Israeli savings and investment products a US person holds, keren hishtalmut, kupat gemel, pension, kranot neemanut, TASE ETFs, bituach menahalim, for two separate US exposures: whether the holding is a PFIC needing Form 8621, and whether it is a foreign trust needing Forms 3520 and 3520-A. Walks the actual statutory tests and the Revenue Procedure 2020-17 exemption criteria rather than guessing, and outputs a per-product table saying which test each product passes or fails and what to ask a preparer. Use when a US citizen or green card holder in Israel asks whether their keren hishtalmut, pension, kupat gemel or Israeli fund creates a US reporting problem, or is deciding what to buy. Do NOT use for annual filing mechanics or FBAR, for Israeli-side tax, for self-employment tax, or to obtain a final classification of any specific product.
https://agentskills.co.il/he/skills/us-person-israeli-investment-check
`https://raw.githubusercontent.com/skills-il/tax-and-finance/master/us-person-israeli-investment-check/SKILL.md`
