# Mark F. Young — Resume

**Email:** mark.francis.young@gmail.com
**Phone:** (903) 392-0105
**LinkedIn:** https://www.linkedin.com/in/mark-f-young-37a4a21/
**GitHub:** https://github.com/markfyoung0711

## Professional Summary

Senior data engineer and architect with 20+ years of experience designing, building, and optimizing data warehouses, ETL pipelines, and data governance frameworks across financial services and technology. Deep expertise in relational databases (PostgreSQL, MySQL, MS SQL Server, Snowflake), Python-based data pipelines, cloud platforms (AWS, GCP), and scalable data architectures. Proven leader who translates business requirements into technical specifications, mentors engineering teams, and drives continuous improvement through KPIs and Agile practices. Experienced with AI/ML tooling to enhance data analytics and processing capabilities.

---

## Work History

### Senior Software Engineer — Jump Trading
**May 2013 – July 2023**

**Instrument Data Warehouse & Architecture (5 years)**
- Designed and created instrument master data warehouses for futures, options, equities, cryptos, currencies, and bonds — establishing robust data architectures to meet trading business objectives.
- Managed data acquisition and warehouse pipelines for accuracy and timeliness, extracting, transforming, and loading data from multiple vendors and exchanges.
- Reduced trading errors by 10% across all trading teams via improved data integrity checks and governance.
- Retired legacy data systems while maintaining backward compatibility and implementing data retention/backup protocols.
- Django/Swagger REST APIs for instrument queries by type, ticker, exchange, and symbol ID (2yrs).
- React.js GUI for investigating and visualizing financial instrument details (1yr).
- Trained data scientists and quant researchers on instrument data APIs and financial instrument lifecycles.

**Data Pipeline & ETL Optimization (2 years)**
- Reduced reference data ETL flow from 3 hours to 3 minutes through pipeline redesign and optimization.
- Partnered with data vendors to acquire new, improved, and more timely data formats (e.g., CME).

**Database Architecture & System Quality (10 years)**
- Expert-level SQL and Python across OLAP, OLTP, MS SQL Server, Sybase ASE, MySQL, and PostgreSQL (10yrs).
- DevOps for entire DB and market data product line: Docker, Alembic migrations (3yrs), Kubernetes (<1yr).
- Introduced automated testing using pytest + SQLAlchemy for stored procedure validation.
- Contributed SQL stored procedure code across 200+ projects.
- AWS S3 as backing store for DB backups and logs (2yrs).
- OAuth2 implementation in Python for SQL DB server connectivity.
- Improved mean time to critical failure from 3 days to 1 year through monitoring and KPI-driven improvement.
- Jupyter notebooks for data exploration, debugging, and training (5yrs); Pandas for data analysis (10yrs).
- Jenkins CI/CD with Groovy for GitHub integration and deployment (5yrs).

**Data Governance, Risk & Clearing Support (10 years)**
- Led data governance, provenance, and data engineering initiatives firm-wide.
- Partnered with Risk on margin rates, fungibility strategies, and risk profiles.
- Partnered with Clearing on settlement investigations and currency settlement date analysis.
- Established and monitored data quality KPIs for 20 trade desks across multiple asset classes.

**Jump Crypto (2 years)**
- Integrated hundreds of crypto coins/pairs for 40+ DeFi exchanges.
- Innovated intraday ICO method for trading new coins.

**Exchange/Vendor Relations & Spec Analysis (5 years)**
- Managed changes in futures, currency pairs, equities, spreads (tick sizes, exchange symbols, etc.).
- Studied and implemented new exchange specs for accurate data ingestion and trading.

**Leadership**
- Led $1.2M annual development budgets (8–10 direct reports); met all deadlines.
- Communicated results to firm owners and management; translated business requirements into technical specifications.
- Instituted Agile/Scrum; taught SDLC best practices to developers and cross-functional stakeholders.
- Mentored team of DBAs; taught git, Agile, SDLC, and Python.
- Introduced 24/7 follow-the-sun production support systems across Asia, Europe, LATAM, and North America.
- JIRA and GitHub Projects for tracking; introduced peer code review culture.

**Tech summary:** Linux (10yr), Python (10yr), Pandas (10yr), SQL (10yr), SQLAlchemy (5yr), MySQL (5yr), PostgreSQL, MS SQL Server, Sybase ASE, Django REST API (3yr), pytest (10yr), Docker (1yr), Kubernetes (<1yr), Jenkins/Groovy, AWS S3, Anaconda, JIRA, Git.

---

### Senior Software Engineer — Buckstop Labs
**July 2023 – August 2024**

Portfolio: https://github.com/markfyoung0711/myfsm

- **Snowflake:** Completed Snowflake training — data loading and retrieval via `snowflake.snowpark`.
- GCP App Engine deployment of North Dakota Oil/Gas data parsing app, feeding BigQuery for anomaly detection. Dockerized; gcloud CLI DevOps.
- Selenium automation of historical daily oil/gas records downloads with full pytest coverage — end-to-end data pipeline.
- PostgreSQL + Tableau/RocketBI/Power BI dashboards for Smith System (Dallas, TX): financial scorecard with product, region, and margin breakdowns. Salesforce OAuth integration.
- ANTLR4 parsing of COBOL copybooks to extract Python structs from EBCDIC files — complex ETL transformation.
- Django REST API with ORM: modeled Students, Classes, and Assignments; SwaggerHub API design.
- Law Student Success ML modeling with scikit-learn; generated sample data; admin interface for importing live data.
- Consulting with Odoo dev team (gobonum.com) for integrating data warehousing for furniture manufacturer.
- Couchbase Capella (NoSQL) evaluation; CRUD API design using OpenAPI standards.
- **AWS:** Lambda, IAM, API Gateway, DynamoDB (NoSQL), Cloud9; AWS ECS and EKS familiarity via training; AWS Serverless Patterns training project.
- **Tech stack:** Python, Pandas, PostgreSQL, Snowflake, Tableau BI, Rocket BI, Power BI, Airbyte, pytest, Jupyter, GCP, Vertex AI, Google App Engine, scikit-learn, GitHub Actions, Docker, Anaconda, OAuth libraries, Claude (Anthropic API).

---

### Senior Software Engineer — Blizzard Entertainment / Microsoft
**August 2024 – Present**

- Developed and hardened APIs: cross-product authorities, regression testing, security feature rollout. Tools: Flask, pytest, SQLAlchemy, Python.
- Complex SQL queries using SQLAlchemy ORM for data retrieval and reporting.
- Designed auto-heal container to monitor Celery worker health; reduced dependency on task failures. Skills: Celery, RabbitMQ, asyncio, threads, queues.
- Kubernetes Helm charts for secret management with GCP Secret Manager; ArgoCD for pod deployment.
- Integrated `trace_id` tracing between smoke tests and TACT API; enabled Grafana/Loki log queries for performance monitoring.
- Expanded CI integration testing pipeline; integrated mypy and ruff for code quality. Jenkins declarative/Groovy CI.
- Requirements gathering: translated vague JIRA tickets into detailed development and test approaches.
- Mentored SDETs on code compartmentalization, automated e2e testing (Playwright, TestRail), and Python best practices.
- Debugged AWS S3 encoding issues for game CDN endpoints; participated in S3 code reviews.
- C++: revised Battle.net pipeline3 for game content delivery; Python 2→3 conversion; debugged thread locking and shared-resource lock management.
- **Skills summary:** Docker (1yr), Kubernetes/Helm (<1yr), Flask/Python/SQLAlchemy REST API (1yr), CI/CD/GitHub Actions (1yr), GCP, AWS S3.

---

### Senior Software Engineer — Citadel Investment Group
**January 2003 – January 2013**

- Managed team of 5 C++ developers building tick data warehouses; created and maintained 100+ tick data warehouses.
- Analyzed and decoded exchange market data captures to code new market data parsers; 100% automated unit tests.
- Reduced time-to-market via configurable reference data for ETL pipelines.
- Instructed quant researchers in processing historical data archives.
- Promoted to team lead in HFT department; managed 5 testers; mentored devs on automated testing.
- Designed and executed tests for event-driven servers and monitors.
- **Tech:** C++ (10yr), STL (10yr), Python (2yr), SQL (10yr), Git, Google Test, FIX, JIRA, ETL (5yr).
- **Data sources:** US and EU ECNs, Reuters, OPRA, CME, ICE.

---

### Software Engineer / SDET — Exelon
**January 2002 – January 2003**

- Automated Informatica ETL testing for accounting migration across 4 power companies; reduced manual testing by 80%.

---

### Senior Software Engineer — TD Waterhouse
**May 2000 – January 2002**

- Developed handheld trading platform; tested all code and DB interfaces.
- Worked with trading staff to gather requirements and translate into technical specifications.

---

### Member of Technical Staff — AT&T Bell Labs
**August 1996 – May 2000**

- Added DB features to finite state machine language (C++, C, lex, yacc) for Lucent A-I-Net Service Creation Environment.
- Created persistence class structure with static data via Oracle PL/SQL.
- Became team lead for Service Creation Environment development; trained technical staff.
- **Tech:** Linux, C++, C, Oracle PL/SQL, cppunit.

---

## Education

**University of St. Francis** — B.S. Computer Science — GPA: 3.63/4.0