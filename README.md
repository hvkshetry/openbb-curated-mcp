# OpenBB MCP Server - Curated Tools Edition

## Overview

This is a modified version of the OpenBB MCP server that loads only a curated set of 65 essential financial tools, reducing context consumption by ~65% (from 184 to 65 tools). All tools use free data sources (FRED, yfinance, SEC, FINRA, ECB, OECD, IMF, EconDB) or FMP with the configured API key.

## Changes Made

1. **Created `curated_tools.py`**: Defines a hardcoded, immutable set of tools with documentation
2. **Modified `main.py`**: 
   - Only enables tools in the curated list
   - Disables tool discovery features (available_categories, available_tools, activate_tools, deactivate_tools)
3. **Modified `settings.py`**: Forces `enable_tool_discovery = False`
4. **Modified `config.py`**: Ensures tool discovery cannot be re-enabled
5. **Added FMP API configuration**: Created `user_settings.json` with FMP API key for ETF analysis tools

## Important Tool Updates

### Corrected Tool Names
- `commodity_price_spot` (was: commodity_price_historical)
- `news_world` (was: news_general)
- `index_available` (was: index_market)
- `fixedincome_spreads_treasury_effr` (was: fixedincome_spreads_treasury_yield)

### Tools Requiring Date Parameters
To avoid token limit errors, these tools MUST include date parameters:
- `economy_balance_of_payments` - Use start_date (e.g., 1 year ago)
- `fixedincome_rate_sofr` - Use start_date and end_date (1 year range)
- `fixedincome_rate_effr` - Use start_date and end_date (1 year range)
- `fixedincome_government_treasury_rates` - Use start_date and end_date (6-12 months)

### Free Alternatives for Premium Tools
- `equity_discovery_filings` - Recent SEC filings (replaces compare_peers)
- `equity_fundamental_multiples` - Valuation multiples (replaces fundamental_ratios)
- `equity_ownership_form_13f` - 13F filings (replaces institutional ownership)
- `fixedincome_spreads_tcm` - Treasury constant maturity spreads
- Use `economy_fred_series` to calculate custom risk premiums

## Curated Tools (65 total)

### Economy (20 tools)
- GDP: real, nominal, forecast
- Inflation: CPI, retail prices, house price index
- Rates: interest rates (unified function)
- Employment & Trade: unemployment, balance of payments, nonfarm payrolls
- Data Access: FRED series/search, BLS series/search
- Indicators: composite leading indicator
- **Trade & International Analysis (5 new tools)**:
  - Direction of Trade: Bilateral merchandise trade flows (IMF)
  - Export Destinations: Top export partners by country (EconDB)
  - Economic Indicators: International reserves, financial soundness (IMF/EconDB)
  - Country Profile: Comprehensive economic overview (EconDB)
  - Port Volume: Shipping volumes as trade flow indicators (EconDB/IMF)

### Equity (19 tools)
- Search & Quotes: search, price quote, historical, performance
- Fundamentals: balance, income, cash, dividends, metrics, multiples, trailing dividend yield
- Research: profile, estimates consensus, discovery filings
- Screening: discovery gainers, undervalued large caps, growth tech equities
- Ownership: insider trading, form 13F

### Fixed Income (6 tools)
- Treasury rates, yield curve, TCM spreads, treasury-EFFR spreads
- Indices: bond indices, mortgage indices

### ETF (8 tools)
- Search, info, holdings, performance, historical
- Portfolio Analysis: sectors, countries, equity exposure (FMP provider)

### Index (3 tools)
- Historical prices, constituents, available indices

### Derivatives (4 tools)
- Options chains, unusual activity, snapshots, futures curve

### News (2 tools)
- World news, company news

### Currency (1 tool)
- Historical prices

### Commodity (1 tool)
- Spot prices

### Cryptocurrency (1 tool)
- Historical prices (YFinance/FMP)

## API Configuration

All API keys are configured in `~/.openbb_platform/user_settings.json`. See `user_settings.json.example` for the required format.

Required API keys:
- **FRED API Key**: Free from https://fred.stlouisfed.org/docs/api/api_key.html
- **BLS API Key**: Free from https://www.bls.gov/developers/api_registration.htm
- **FMP API Key**: Free tier available from https://site.financialmodelingprep.com/developer/docs/

Note: While FRED and BLS are free public services, they still require API keys for access.

## Usage

1. Start the MCP server with:
   ```bash
   openbb-mcp --no-tool-discovery
   ```

2. Or configure your MCP client with the provided `mcp_config.json`:
   ```json
   {
     "transport": "stdio",
     "args": ["--no-tool-discovery"],
     "describe_responses": false
   }
   ```

## Benefits

- **65% reduction in context usage**: Only 65 tools instead of 184
- **Focused on free data sources**: yfinance, FRED, SEC, FINRA, IMF, EconDB
- **No dynamic tool management**: Consistent, predictable tool availability
- **Optimized for investment analysis**: All essential tools included
- **Trade analysis capabilities**: Monitor deglobalization and tariff impacts

## Trade Analysis Capabilities

The 5 new trade tools enable monitoring of:
- **Trade relationship shifts**: Track bilateral flows between specific countries
- **Supply chain vulnerabilities**: Identify export dependencies and concentration
- **Early warning indicators**: Port congestion and dwelling times signal disruptions
- **Financial stability**: Monitor international reserves and soundness indicators
- **Portfolio exposure**: Assess which trade corridors affect your investments

These tools are essential for investment advisory in an era of increasing trade tensions, tariffs, and supply chain restructuring.

## Notes

- Tool discovery is permanently disabled
- The curated tool list cannot be modified at runtime
- All tools are loaded at startup for maximum performance