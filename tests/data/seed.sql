PRAGMA foreign_keys = OFF;
BEGIN TRANSACTION;
INSERT INTO edgar_explorer_filing (
        id,
        cik,
        company_name,
        form_type,
        date_filed,
        accession_number,
        chunks_used,
        num_entities,
        info,
        relevant_text,
        batch_id,
        info_type
    )
VALUES(
        1,
        '1327374',
        'YieldQuest Funds Trust',
        '',
        '2009-02-27',
        '0001209286-09-000121',
        '[106]',
        0,
        replace(
            '\n{\n  "compensation_info_present": false,\n  "trustees": [],\n  "notes": "The provided text describes the fees paid to the Advisor, not the Trustees.  There is no compensation information for Trustees or Board members in this SEC filing snippet."\n}\n',
            '\n',
            char(10)
        ),
        replace(
            'founder, controlling member and Managing Director of the Advisor.\n\nUnder the terms of an Investment Advisory Agreement (the "Agreement"), the\n\nAdvisor manages each Fund''s investments subject to approval of the Board of\n\nTrustees.\n\nAs compensation for its management services, each Fund is obligated to\n\npay the Advisor a fee (based on average daily net assets) computed and accrued\n\ndaily and paid monthly at the following annual rates: Equity Fund, 0.99%; Total\n\nReturn Fund, 0.59%; Tax-Exempt Fund, 0.59%; Flexible Income Fund, 0.75%; Low\n\nDuration Fund, 0.45%, Low Duration Tax-Exempt Fund, 0.45%, Core Fund 0.34%, and\n\nCore Tax-Exempt Fund 0.40%.\n\nThe Advisor contractually has agreed to waive its\n\nfees and/or reimburse certain operating expenses through February 28, 2010, but\n\nonly to the extent necessary to maintain\n\n<PAGE>\n\neach Fund''s total operating expenses, excluding brokerage costs, borrowing costs\n\n(such as interest expense and dividends on securities sold short), taxes, a\n\nextraordinary expenses, any indirect expenses (such as expenses incurred by\n\nother investment companies in which a Fund invests), 12b-1 fees and\n\nadministrative fees, as follows: Equity Fund, 1.19%; Total Return Fund, 0.79%;\n\nTax-Exempt Fund, 0.79%; Flexible Income Fund, 0.95%; Low Duration Fund, 0.65%;\n\nLow Duration Tax-Exempt Fund, 0.65%; Core Fund, 0.49%; and Core Tax-Exempt Fund,\n\nFor the fiscal years ended October 31, 2006, October 31, 2007 and October\n\n31, 2008, the Advisor received the following fees:\n\n<TABLE>\n\n<CAPTION>\n\nFUND               MANAGEMENT FEES       MANAGEMENT FEES        MANAGEMENT FEES\n\nEARNED BY THE     WAIVED AND REIMBURSED       PAID TO THE\n\nADVISOR           BY THE ADVISOR             ADVISOR\n\nEquity Fund                         $82,418              $139,158                  $0\n\nTotal Return Fund                  $344,538               $90,174               $254,364\n\nTax-Exempt Fund                    $210,425              $106,345               $104,080\n\n<CAPTION>\n\nFUND               MANAGEMENT FEES       MANAGEMENT FEES        MANAGEMENT FEES\n\nEARNED BY THE     WAIVED AND REIMBURSED       PAID TO THE\n\nADVISOR           BY THE ADVISOR             ADVISOR\n\nEquity Fund                        $212,406               $120,628               $91,778\n\nTotal Return Fund                 $1,627,171                 $0                 $1,627,171\n\nTax-Exempt Fund                    $881,785                  $0                  $881,785\n\nFlexible Income Fund               $24,505                 $21,750                $2,755\n\nLow Duration Fund                  $10,670                 $23,833                  $0\n\nLow Duration Tax-Exempt Fund        $2,053                 $27,631                  $0\n\n</TABLE>\n\n<TABLE>\n\n<CAPTION>\n\nFUND               MANAGEMENT FEES       MANAGEMENT FEES        MANAGEMENT FEES\n\nEARNED BY THE     WAIVED AND REIMBURSED       PAID TO THE\n\nADVISOR           BY THE ADVISOR             ADVISOR\n\nEquity Fund                        $225,054               $68,701                $156,353\n\nTotal Return Fund                 $1,581,867              $109,585              $1,472,282\n\nTax-Exempt Fund                    $887,513               $157,375               $730,138\n\nFlexible Income Fund               $238,430               $68,963                $169,467\n\nLow Duration Fund                  $49,190                $56,551                   $0\n\nLow Duration Tax-Exempt Fund       $26,767                $52,460                   $0\n\n</TABLE>\n\n*\n\nThe Core Fund and Core Tax-Exempt Fund had not commenced operations during the\n\nperiods shown.',
            '\n',
            char(10)
        ),
        '20250328130753-wdm',
        'trustee'
    );
INSERT INTO edgar_explorer_filing (
        id,
        cik,
        company_name,
        form_type,
        date_filed,
        accession_number,
        chunks_used,
        num_entities,
        info,
        relevant_text,
        batch_id,
        info_type
    )
VALUES(
        2,
        '44201',
        'GROWTH FUND OF AMERICA INC',
        '',
        '2009-04-08',
        '0000044201-09-000025',
        '[119]',
        0,
        replace(
            '\n{\n  "compensation_info_present": false,\n  "trustees": [],\n  "notes": "The provided text is a section of an SEC filing (485BPOS) detailing various agreements and forms, but it does not contain any information regarding trustee compensation.  The document mentions a ''Deferred Compensation Plan'' (f), but doesn''t provide details about who receives it or the amounts involved.  No names or compensation figures for trustees or similar roles are present."\n}\n',
            '\n',
            char(10)
        ),
        replace(
            'Form of Institutional Selling Group Agreement (see P/E Amendment No. 78 filed 11/1/04); Form of Amendment to Selling Group Agreement effective 2/1/07 – previously filed (see P/E Amendment No. 81 filed 10/31/07); Form of Amendment to Institutional Selling Group Agreement effective 2/1/07 – previously filed (see P/E Amendment No. 81 filed 10/31/07); Form of Amended and Restated Principal Underwriting Agreement dated 6/16/08 – previously filed (see P/E Amendment No. 82 filed 7/1/2008); Form of Amendment to Selling Group Agreement effective 10/1/08 – previously filed (see P/E Amendment No. 82 filed 10/31/08); Form of Amendment to Institutional Selling Group Agreement effective 10/1/08 – previously filed (see P/E Amendment No. 82 filed 10/31/08); Form of Class F Participation Agreement – previously filed (see P/E Amendment No. 82 filed 10/31/08); Form of Amendment to Class F Participation Agreement effective 8/1/08 – previously filed (see P/E Amendment No. 82 filed 10/31/08); Form of Bank/Trust Company Participation Agreement for Class F Shares – previously filed (see P/E Amendment No. 82 filed 10/31/08); and Form of Amendment to Bank/Trust Company Participation Agreement for Class F Shares effective 8/1/08 – previously filed (see P/E Amendment No. 82 filed 10/31/08)\n\n(e-2) |  Form of Amended and Restated Principal Underwriting Agreement effective 5/1/09; Form of Amendment to Selling Group Agreement effective 5/1/09; Form of Amendment to Institutional Selling Group Agreement effective 5/1/09; Form of Amendment to Bank/Trust Company Selling Group Agreement effective 5/1/09; Form of Amendment to Class F Share Participation Agreement effective 5/1/09; and Form of Amendment to Bank/Trust Company Participation Agreement for Class F Shares effective 5/1/09\n\n(f) |  Bonus or Profit Sharing Contracts – Deferred Compensation Plan as amended 1/1/08 – previously filed (see P/E Amendment No. 82 filed 7/1/2008)\n\n(g) |  Custodian Agreements – Form of Global Custody Agreement dated 12/14/06 – previously filed (see P/E Amendment No. 81 filed 10/31/07)\n\n(h-1) |  Other Material Contracts – Amended Shareholder Services Agreement dated April 1, 2003 - previously filed (see P/E Amendment No. 78 filed 11/1/04)\n\nForm of Indemnification Agreement dated July 1, 2004 - previously filed (see P/E Amendment No. 78 filed 11/1/04); Form of Amendment to Shareholder Services Agreement dated 11/1/06 – previously filed (see P/E Amendment No. 81 filed 10/31/07) and Form of Amended and Restated Administrative Service Agreement dated 6/16/08 – previously filed (see P/E Amendment No. 82 filed 7/1/2008)\n\n(h-2) |  Form of Amendment of Amended Shareholder Services dated 11/1/08\n\n(h-3)\n\n|  Form of Amended and Restated Administrative Services Agreement effective 5/1/09\n\n(i-1) |  Legal Opinion – Legal Opinion previously filed (see P/E Amendment No. 70 filed 3/10/00, No. 72 filed 3/8/01, No. 74 filed 2/14/02, No. 75 filed 5/13/02 and No. 82 filed 7/1/08)\n\n(i-2) |  Legal Opinion\n\n(j) |  Other Opinions – Consent of Independent Registered Public Accounting Firm\n\n(k) |  Omitted financial statements \- none\n\n(l) |  Initial capital agreements \- not applicable to this filing',
            '\n',
            char(10)
        ),
        '20250328130753-wdm',
        'trustee'
    );
INSERT INTO edgar_explorer_filing (
        id,
        cik,
        company_name,
        form_type,
        date_filed,
        accession_number,
        chunks_used,
        num_entities,
        info,
        relevant_text,
        batch_id,
        info_type
    )
VALUES(
        3,
        '311884',
        'FIDELITY BEACON STREET TRUST',
        '',
        '2009-12-29',
        '0000311884-09-000012',
        '[103]',
        0,
        replace(
            '\n{\n  "compensation_info_present": false,\n  "trustees": [],\n  "notes": "The provided text describes fee structures for 12b-1 plans paid to FDC (presumably a fund manager) by different share classes (Class T, Class B, Class C).  It does not contain any compensation information for Trustees themselves.  The Trustees have the authority to set the 12b-1 fee for Class T, but their own compensation is not disclosed."\n}\n',
            '\n',
            char(10)
        ),
        replace(
            'Except as provided below, during the first year of investment and thereafter, FDC may reallow up to the full amount of this 12b-1 (service) fee to intermediaries (such as banks, broker-dealers, and other service-providers), including its affiliates, for providing shareholder support services.\n\nFor purchases of Class A shares on which a finder''s fee was paid to intermediaries, after the first year of investment, FDC may reallow up to the full amount of the 12b-1 (service) fee paid by such shares to intermediaries, including its affiliates, for providing shareholder support services.\n\nClass T has adopted a Distribution and Service Plan pursuant to Rule 12b-1 under the 1940 Act.\n\nUnder the plan, Class T is authorized to pay FDC a monthly 12b-1 (distribution) fee as compensation for providing services intended to result in the sale of Class T shares.\n\nClass T may pay this 12b-1 (distribution) fee at an annual rate of 0.50% of its average net assets, or such lesser amount as the Trustees may determine from time to time.\n\nClass T currently pays FDC a monthly 12b-1 (distribution) fee at an annual rate of 0.25% of its average net assets throughout the month.\n\nClass T''s 12b-1 (distribution) fee rate may be increased only when the Trustees believe that it is in the best interests of Class T shareholders to do so.\n\nFDC may reallow up to the full amount of this 12b-1 (distribution) fee to intermediaries (such as banks, broker-dealers, and other service-providers), including its affiliates, for providing services intended to result in the sale of Class T shares.\n\nIn addition, pursuant to the Class T plan, Class T pays FDC a monthly 12b-1 (service) fee at an annual rate of 0.25% of Class T''s average net assets throughout the month for providing shareholder support services.\n\nFDC may reallow up to the full amount of this 12b-1 (service) fee to intermediaries (such as banks, broker-dealers, and other service-providers), including its affiliates, for providing shareholder support services.\n\nClass B has adopted a Distribution and Service Plan pursuant to Rule 12b-1 under the 1940 Act.\n\nUnder the plan, Class B is authorized to pay FDC a monthly 12b-1 (distribution) fee as compensation for providing services intended to result in the sale of Class B shares.\n\nClass B currently pays FDC a monthly 12b-1 (distribution) fee at an annual rate of 0.75% of its average net assets throughout the month.\n\nIn addition, pursuant to the Class B plan, Class B pays FDC a monthly 12b-1 (service) fee at an annual rate of 0.25% of Class B''s average net assets throughout the month for providing shareholder support services.\n\nProspectus\n\nFDC may reallow up to the full amount of this 12b-1 (service) fee to intermediaries (such as banks, broker-dealers, and other service-providers), including its affiliates, for providing shareholder support services.\n\nClass C has adopted a Distribution and Service Plan pursuant to Rule 12b-1 under the 1940 Act.\n\nUnder the plan, Class C is authorized to pay FDC a monthly 12b-1 (distribution) fee as compensation for providing services intended to result in the sale of Class C shares.\n\nClass C currently pays FDC a monthly 12b-1 (distribution) fee at an annual rate of 0.75% of its average net assets throughout the month.\n\nIn addition, pursuant to the Class C plan, Class C pays FDC a monthly 12b-1 (service) fee at an annual rate of 0.25% of Class C''s average net assets throughout the month for providing shareholder support services.',
            '\n',
            char(10)
        ),
        '20250328130753-wdm',
        'trustee'
    );
INSERT INTO edgar_explorer_filing (
        id,
        cik,
        company_name,
        form_type,
        date_filed,
        accession_number,
        chunks_used,
        num_entities,
        info,
        relevant_text,
        batch_id,
        info_type
    )
VALUES(
        4,
        '880366',
        'LEGG MASON PARTNERS EQUITY TRUST',
        '',
        '2009-10-01',
        '0001193125-09-202123',
        '[1, 2]',
        0,
        replace(
            '\n{\n  "compensation_info_present": true,\n  "trustees": [],\n  "notes": "The provided text mentions ''Emeritus Retirement Plan'' and ''Trustee Retirement Plan'', indicating the existence of retirement plans for trustees. However, no specific compensation details (amounts, names, etc.) for individual trustees are provided in this snippet.  The snippet only references the existence of these plans within incorporated documents (Post-Effective Amendments). To obtain the actual compensation figures, one would need to access the referenced Post-Effective Amendments 60 and 61."\n}\n',
            '\n',
            char(10)
        ),
        replace(
            '(f) Amended and Restated Designation of Series of Shares of Beneficial Interests in the Trust effective as of February 7, 2008 is incorporated herein by reference to Post-Effective Amendment No. 87 as filed with the SEC on February 15, 2008 (“Post-Effective Amendment No. 87”).\n\n(g) Amended and Restated Designation of Classes effective as of February 7, 2008 is incorporated herein by reference to Post-Effective Amendment No. 87.\n\n(h) Amended and Restated Designation of Series of Shares of Beneficial Interests in the Trust effective as of May 8, 2008 is incorporated herein by reference to Post-Effective Amendment No. 109 as filed with the SEC on June 3, 2008 (“Post-Effective Amendment No. 109”).\n\n(i) Amended and Restated Designation of Classes effective as of May 8, 2008 is incorporated herein by reference to Post-Effective Amendment No. 109.\n\n(j) Amended and Restated Designation of Series of Shares of Beneficial Interests in the Trust effective as of June 6, 2008 is incorporated herein by reference to Post-Effective Amendment No. 110 as filed with the SEC on June 6, 2008 (“Post-Effective Amendment No. 110”).\n\n(k) Amended and Restated Designation of Classes effective as of June 6, 2008 is incorporated herein by reference to Post-Effective Amendment No. 110.\n\n(l) Amended and Restated Designation of Series of Shares of Beneficial Interests in the Trust effective as of January 28, 2009 is incorporated herein by reference to Post-Effective Amendment No. 133 as filed with the SEC on January 28, 2009 (“Post-Effective Amendment No. 133”).\n\n(m) Amended and Restated Designation of Classes effective as of January 28, 2009 is incorporated herein by reference to Post-Effective Amendment No. 133.\n\n(n) Amended and Restated Designation of Classes effective as of February 26, 2009 is incorporated herein by reference to Post-Effective Amendment No. 137 as filed with the SEC on February 27, 2009 (“Post-Effective Amendment No. 137”).\n\n(o) Amended and Restated Designation of Classes effective as of February 26, 2009 is incorporated herein by reference to Post-Effective Amendment No. 146 as filed with the SEC on June 25, 2009 (“Post-Effective Amendment No. 146”).\n\n(2) The Registrant’s By-Laws dated October 4, 2006 are incorporated herein by reference to Post-Effective Amendment No. 70.\n\n(3) Not Applicable.\n\n(4) Form of Agreement and Plan of Reorganization included in Part A of the Registration Statement on Form N-14 is incorporated herein by reference to the Registrant’s Registration Statement on Form N-14 filed on August 21, 2009.\n\n(5) Not Applicable.\n\n(6)(a) Form of Management Agreement between the Registrant, on behalf of Legg Mason Partners Investors Value Fund, and Legg Mason Partners Fund Advisor, LLC (“LMPFA”) is incorporated herein by reference to Post-Effective Amendment No. 78 as filed with the SEC on December 14, 2007 (“Post-Effective Amendment No. 78”).\n\n(b) Form of Subadvisory Agreement between LMPFA and ClearBridge Advisers, LLC (“ClearBridge”), with respect to Legg Mason Partners Investors Value Fund, is incorporated herein by reference to Post-Effective Amendment No. 78.\n\n(7)(a) Form of Distribution Agreement with Citigroup Global Markets Inc. (“CGMI”) is incorporated herein by reference to Post-Effective Amendment No. 30 as filed with the SEC on August 16, 2000 (“Post-Effective Amendment No. 30”).\n\n(b) Form of Distribution Agreement with PFS Distributors, Inc. is incorporated herein by reference to Post-Effective Amendment No. 30.\n\n(c) Form of Amendment to the Distribution Agreement with CGMI dated as of December 1, 2005, is incorporated herein by reference to Post-Effective Amendment No. 56 as filed with the SEC on January 27, 2006 (“Post-Effective Amendment No. 56”).\n\n(d) Form of Amendment of Distribution Agreement and Assumption of Duties and Responsibilities, among the Registrant, PFS Distributors, Inc. and PFS Investments, Inc. (“PFS”), dated as of December 1, 2005, is incorporated herein by reference to Post-Effective Amendment No. 56.\n\n(e) Letter Agreement amending the Distribution Agreements with CGMI dated April 10, 2007, is incorporated herein by reference to Post-Effective Amendment No. 76.\n\n(f) Letter Agreement amending the Distribution Agreements with PFS dated April 6, 2007, is incorporated herein by reference to Post-Effective Amendment No. 76.\n\n(g) Form of Distribution Agreement with Legg Mason Investor Services, LLC (“LMIS”) is incorporated herein by reference to Post-Effective Amendment No. 128 as filed with the SEC on December 15, 2008.\n\n(8)(a) Emeritus Retirement Plan relating to certain funds, established effective as of January 1, 2007, is incorporated herein by reference to Post-Effective Amendment No. 60 as filed with the SEC on December 5, 2006 (“Post-Effective Amendment No. 60”).\n\n(b) Amended and Restated Trustee Retirement Plan relating to certain funds dated as of January 1, 2005 (the “General Retirement Plan”), is incorporated herein by reference to Post-Effective Amendment No. 61 as filed with the SEC on January 8, 2007 (“Post-Effective Amendment No. 61”).\n\n(c) Legg Mason Investment Series (f/k/a Smith Barney Investment Series)\n\nAmended and Restated Trustees Retirement Plan dated as of January 1, 2005, is incorporated herein by reference to Post-Effective Amendment No. 61.\n\n(d) Amendment to the General Retirement Plan and the Legg Mason Partners Investment Series Amended and Restated Trustees Retirement Plan is incorporated herein by reference to Post-Effective Amendment No. 61.\n\n(e) Amended and Restated Emeritus Retirement Plan relating to certain funds, established effective as of January 1, 2007, is incorporated herein by reference to Post-Effective Amendment No. 61.\n\n(9)(a) Custodian Services Agreement with State Street Bank and Trust Company (“State Street”), dated January 1, 2007, is incorporated herein by reference to Post-Effective Amendment No. 76.\n\n(b) Letter Agreement amending the Custodian Services Agreement with State Street, dated April 9, 2007, is incorporated herein by reference to Post-Effective Amendment No. 76.\n\n(10)(a) Amended Shareholder Services and Distribution Plan relating to Class A, B, C, FI, R and I Shares is incorporated herein by reference to Post-Effective Amendment No. 74.\n\n(b) Amended Shareholder Services and Distribution Plan relating to Class A, B, C, FI, R and I Shares is incorporated herein by reference to Post-Effective Amendment No. 81 as filed with the SEC on January 29, 2008.\n\n(c) Amended Shareholder Services and Distribution Plan relating to Class A, B, C, FI, R, I and IS Shares dated as of February 7, 2008 is incorporated herein by reference to Post-Effective Amendment No. 86 as filed with the SEC on February 15, 2008.\n\n(d) Amended Shareholder Services and Distribution Plan relating to Class A, B, C, FI, R, I and IS Shares dated as of August 7, 2008 is incorporated herein by reference to Post-Effective Amendment No. 119.',
            '\n',
            char(10)
        ),
        '20250328130753-wdm',
        'trustee'
    );
INSERT INTO edgar_explorer_filing (
        id,
        cik,
        company_name,
        form_type,
        date_filed,
        accession_number,
        chunks_used,
        num_entities,
        info,
        relevant_text,
        batch_id,
        info_type
    )
VALUES(
        5,
        '1137360',
        'MARKET VECTORS ETF TRUST',
        '',
        '2009-08-14',
        '0000930413-09-004290',
        '[305]',
        0,
        replace(
            '\n{\n  "compensation_info_present": false,\n  "trustees": [],\n  "notes": "The provided text mentions indemnification for Trustees but does not contain any information regarding their compensation (salary, bonuses, etc.).  The document focuses on the legal protection offered to Trustees, not their financial remuneration."\n}\n',
            '\n',
            char(10)
        ),
        replace(
            '(l) |  Not applicable.\n\n(m) |  Not applicable.\n\n(n) |  Not applicable.\n\n(o) |  Not applicable.\n\n(p)(1)\n\n|  Code of Ethics.\n\n‡‡‡‡‡\n\n* |  Incorporated by the reference to the Registrant’s Registration Statement filed on April 28, 2006.\n\n** |  Incorporated by reference to the Registrant’s Registration Statement filed on May 11, 2006.\n\n*** |  Incorporated by reference to the Registrant’s Registration Statement filed on October 6, 2006.\n\n**** |  Incorporated by reference to the Registrant’s Registration Statement filed on April 9, 2007.\n\n***** |  Incorporated by reference to the Registrant’s Registration Statement filed on July 30, 2007.\n\n****** |  Incorporated by reference to the Registrant’s Registration Statement filed on November 2, 2007.\n\n† |  Incorporated by reference to the Registrant’s Registration Statement filed on December 31, 2007.\n\n†† |  Incorporated by reference to the Registrant’s Registration Statement filed on February 15, 2008.\n\n††† |  Incorporated by reference to the Registrant’s Registration Statement filed on April 21, 2008.\n\n†††† |  Incorporated by reference to the Registrant’s Registration Statement filed on July 8, 2008.\n\n††††† |  Incorporated by reference to the Registrant’s Registration Statement filed on August 8, 2008.\n\n‡ |  Incorporated by reference to the Registrant’s Registration Statement filed on November 25, 2008.\n\n‡‡ |  Incorporated by reference to the Registrant’s Registration Statement filed on December 23, 2008.\n\n‡‡‡ |  Incorporated by reference to the Registrant’s Registration Statement filed on January 28, 2009.\n\n‡‡‡‡ |  Incorporated by reference to the Registrant’s Registration Statement filed on February 6, 2009.\n\n‡‡‡‡‡ |  Incorporated by reference to the Registrant’s Registration Statement filed on April 21, 2009.\n\n‡‡‡‡‡‡ |  Incorporated by reference to the Registrant’s Registration Statement filed on May 8, 2009.\n\n^ |  Filed herewith.\n\n^^ |  To be filed by amendment.\n\nItem 24.\n\n|  Persons Controlled by or Under Common Control with Registrant\n\nNone.\n\nItem 25.\n\n|  Indemnification\n\nPursuant to Section 10.2 of the Amended and Restated Declaration of Trust, all persons that are or have been a Trustee or officer of the Trust (collectively, the “Covered Persons”) shall be indemnified by the Trust to the fullest extent permitted by law against liability and against all expenses reasonably incurred or paid by him in connection with any claim, action, suit, or proceeding in which he or she becomes involved as a party or otherwise by virtue of his being or having been a Trustee or officer and against amounts paid or incurred by him in the settlement thereof.\n\nNo indemnification will be provided to a Covered Person who shall have been adjudicated by a court or body before which the proceeding was brought to be liable to the Trust or its shareholders by reason of willful misfeasance, bad faith, gross negligence or reckless disregard of the duties involved in the conduct of his office or not to have acted in good faith in the reasonable belief that his action was in the best interest of the Trust; or in the event of a settlement, unless there has been a determination that such Trustee or officer did not engage in willful misfeasance, bad faith, gross negligence, or reckless disregard of the duties involved in the conduct of his office.',
            '\n',
            char(10)
        ),
        '20250328130753-wdm',
        'trustee'
    );
INSERT INTO edgar_explorer_filing (
        id,
        cik,
        company_name,
        form_type,
        date_filed,
        accession_number,
        chunks_used,
        num_entities,
        info,
        relevant_text,
        batch_id,
        info_type
    )
VALUES(
        6,
        '1370177',
        'RiverNorth Funds',
        '',
        '2009-02-02',
        '0001035449-09-000073',
        '[57]',
        0,
        replace(
            '\n{\n  "compensation_info_present": false,\n  "trustees": [],\n  "notes": "The provided text focuses on fees paid to service providers (Unified Financial Securities, MSS, Cohen Fund Audit Services) and does not contain any compensation information for Trustees or Board members.  The document mentions a ''Board of Trustees'' in relation to the establishment of policies for brokerage allocation, but provides no details regarding their compensation."\n}\n',
            '\n',
            char(10)
        ),
        replace(
            'For services as the Fund''s distributor, Unified Financial Securities, Inc. receives a fee of 0.01% of the average daily net assets of the Fund, subject to an annual minimum fee of $9,000.\n\nFund Services\n\nUnified also acts as the transfer agent ("Transfer Agent") for the Fund.\n\nUnified maintains the records of each shareholder''s account, answers shareholders'' inquiries concerning their accounts, processes purchases and redemptions of the Fund''s shares, acts as dividend and distribution disbursing agent and performs other transfer agent and shareholder service functions.\n\nUnified receives an annual fee from the Fund of $18 per shareholder account, subject to an annual minimum fee of $20,000 for these transfer agency services.\n\nIn addition, Unified provides the Fund with fund accounting services, which includes certain monthly reports, record-keeping and other management-related services.\n\nFor its services as fund accountant, Unified receives an annual fee from the Fund based on the average value of the Fund.\n\nThe fee is: 0.04% for the first $100 million in average net assets, 0.02% from $100 to $250 million in average net assets, and 0.01% for assets in excess of $250 million, subject to an annual minimum fee of $25,000.\n\nPrior to October 1, 2008, Mutual Shareholder Services ("MSS") acted as the Fund''s fund accountant and transfer agent.\n\nFor the period December 27, 2006 (commencement of operations) through September 30, 2007, MSS received $19,149 from the Fund for fund accounting and transfer agent services.\n\nFor the fiscal year ended September 30, 2008, the Fund paid MSS $39,725 for fund accounting and transfer agent services.\n\nIndependent Registered Public Accounting Firm\n\nThe firm of Cohen Fund Audit Services, Inc., 800 Westpoint Parkway, Suite 1100, Westlake, OH 44145-1524, has been selected as independent registered public accounting firm for the Fund for the fiscal year ending September 30, 2009.\n\nCohen Fund Audit Services, Inc. will perform an annual audit of the Fund''s financial statements and provides financial, tax and accounting services as requested.\n\nBROKERAGE ALLOCATION AND OTHER PRACTICES\n\nSubject to policies established by the Board of Trustees, the Adviser is responsible for the Fund''s portfolio decisions and the placing of the Fund''s portfolio transactions.\n\nIn placing portfolio transactions, the Adviser seeks the best qualitative execution for the Fund, taking into account such factors as price (including the applicable brokerage commission or dealer spread), the execution capability, financial responsibility and responsiveness of the broker or dealer and the brokerage and research services provided by the broker or dealer.\n\nThe Adviser generally seeks favorable prices and commission rates that are reasonable in relation to the benefits received.\n\nThe Adviser is specifically authorized to select brokers or dealers who also provide brokerage and research services to the Fund and/or the other accounts over which the Adviser exercises investment discretion, and to pay such brokers or dealers a commission in excess of the commission another broker or dealer would charge if the Adviser determines in good faith that the commission is reasonable in relation to the value of the brokerage and research services provided.\n\nThe determination may be viewed in terms of a particular transaction or the Adviser''s overall responsibilities with respect to the Trust and to other accounts over which it exercises investment discretion.',
            '\n',
            char(10)
        ),
        '20250328130753-wdm',
        'trustee'
    );
INSERT INTO edgar_explorer_filing (
        id,
        cik,
        company_name,
        form_type,
        date_filed,
        accession_number,
        chunks_used,
        num_entities,
        info,
        relevant_text,
        batch_id,
        info_type
    )
VALUES(
        7,
        '1217286',
        'JPMorgan Trust I',
        '',
        '2009-10-28',
        '0001145443-09-002631',
        '[1010]',
        0,
        replace(
            '\n{\n  "compensation_info_present": false,\n  "trustees": [],\n  "notes": "The provided text snippet is a table header describing the structure of asset information for different types of investment accounts.  It does not contain any compensation information for Trustees or any other individuals."\n}\n',
            '\n',
            char(10)
        ),
        replace(
            '|  |  |  | Non-Performance Based Fee Advisory Accounts |\n|  |  |  | Registered Investment\nCompanies |  | Other Pooled Investment\nVehicles |  | Other Accounts |\n|  |  |  | Number of\nAccounts |  | Total Assets\n($millions) |  | Number of\nAccounts |  | Total Assets\n($millions) |  | Number of\nAccounts |  | Total Assets\n\n($millions)',
            '\n',
            char(10)
        ),
        '20250328130753-wdm',
        'trustee'
    );
INSERT INTO edgar_explorer_filing (
        id,
        cik,
        company_name,
        form_type,
        date_filed,
        accession_number,
        chunks_used,
        num_entities,
        info,
        relevant_text,
        batch_id,
        info_type
    )
VALUES(
        8,
        '1217286',
        'JPMorgan Trust I',
        '',
        '2009-10-28',
        '0001145443-09-002631',
        '[1010]',
        0,
        replace(
            '\n{\n  "compensation_info_present": false,\n  "trustees": [],\n  "notes": "The provided text snippet is a table header describing the structure of asset information for different types of investment accounts.  It does not contain any compensation information for Trustees or any other individuals."\n}\n',
            '\n',
            char(10)
        ),
        replace(
            '|  |  |  | Non-Performance Based Fee Advisory Accounts |\n|  |  |  | Registered Investment\nCompanies |  | Other Pooled Investment\nVehicles |  | Other Accounts |\n|  |  |  | Number of\nAccounts |  | Total Assets\n($millions) |  | Number of\nAccounts |  | Total Assets\n($millions) |  | Number of\nAccounts |  | Total Assets\n\n($millions)',
            '\n',
            char(10)
        ),
        '20250328130753-wdm',
        'trustee'
    );
COMMIT;
