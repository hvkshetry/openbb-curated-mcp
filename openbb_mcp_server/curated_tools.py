"""Curated list of OpenBB tools for MCP server.

This module defines a fixed set of 60 essential tools that provide comprehensive
financial analysis capabilities while minimizing context consumption.

IMPORTANT NOTES:
- Tools requiring date parameters to avoid token limits:
  * economy_balance_of_payments - Use start_date (e.g., 1 year ago)
  * fixedincome_government_treasury_rates - Use start_date and end_date (6-12 months)

- Tools requiring careful parameter usage:
  * economy_survey_bls_search - Use specific queries, set category, include_extras=False

- Tools replaced with free alternatives:
  * equity_compare_peers → equity_discovery_filings
  * equity_fundamental_ratios → equity_fundamental_multiples
  * equity_ownership_institutional → equity_ownership_form_13f
  * economy_risk_premium → Use economy_fred_series to calculate spreads

- Deprecated tools removed:
  * economy_long_term_interest_rate → Use economy_interest_rates(duration="long")
  * economy_short_term_interest_rate → Use economy_interest_rates(duration="short")
  * fixedincome_rate_effr → Use economy_fred_series("EFFR")
  * fixedincome_rate_sofr → Use economy_fred_series("SOFR")

- New wealth management tools added (10 tools):
  * ETF portfolio analysis: sectors, countries, equity_exposure (FMP provider)
  * Fixed income indices: bond_indices, mortgage_indices (FRED provider)
  * Equity screening: gainers, undervalued_large_caps, growth_tech_equities (YFinance)
  * Alternative markets: futures_curve (YFinance), crypto_price_historical (YFinance/FMP)
"""

# Immutable set of curated tools - these are the ONLY tools that will be available
CURATED_TOOLS = frozenset({
    # Economy Tools (15 tools - all working with proper parameters)
    # GDP & Growth
    "economy_gdp_real",
    "economy_gdp_nominal", 
    "economy_gdp_forecast",
    
    # Inflation & Prices
    "economy_cpi",
    "economy_retail_prices",
    "economy_house_price_index",
    
    # Interest Rates & Money (excluding non-working money_measures)
    "economy_interest_rates",
    
    # Employment & Trade
    "economy_unemployment",
    "economy_balance_of_payments",  # Requires date parameters
    "economy_survey_nonfarm_payrolls",  # Added as free alternative
    
    # FRED & BLS Access
    "economy_fred_series",
    "economy_fred_search",
    "economy_survey_bls_series",
    "economy_survey_bls_search",
    
    # Leading Indicators
    "economy_composite_leading_indicator",
    
    # Equity Tools (17 tools - mix of working and free alternatives)
    # Search & Quotes
    "equity_search",
    "equity_price_quote",
    "equity_price_historical",
    "equity_price_performance",  # Added free tool
    
    # Fundamental Analysis (using free alternatives)
    "equity_fundamental_balance",
    "equity_fundamental_income",
    "equity_fundamental_cash",
    "equity_fundamental_dividends",
    "equity_fundamental_metrics",
    "equity_fundamental_multiples",  # Free alternative to ratios
    "equity_fundamental_trailing_dividend_yield",  # Added free tool
    
    # Company Research (using free alternatives)
    "equity_profile",
    "equity_estimates_consensus",
    "equity_discovery_filings",  # Free alternative to compare_peers
    # New discovery/screening tools (YFinance provider)
    "equity_discovery_gainers",  # Top gaining stocks
    "equity_discovery_undervalued_large_caps",  # Value screening
    "equity_discovery_growth_tech_equities",  # Growth stock screening
    
    # Ownership Data (using free alternatives)
    "equity_ownership_insider_trading",
    "equity_ownership_form_13f",  # Free alternative to institutional
    
    # Fixed Income Tools (6 tools - all working with parameters)
    "fixedincome_government_treasury_rates",  # Requires date parameters
    "fixedincome_government_yield_curve",
    "fixedincome_spreads_tcm",  # Free alternative to treasury_yield
    "fixedincome_spreads_treasury_effr",  # Correct name
    # New fixed income indices (FRED provider)
    "fixedincome_bond_indices",  # Bond market indices
    "fixedincome_mortgage_indices",  # Mortgage rate indices
    
    # ETF Tools (8 tools - all working)
    "etf_search",
    "etf_info",
    "etf_holdings",
    "etf_price_performance",
    "etf_historical",
    # New ETF portfolio analysis tools (FMP provider)
    "etf_sectors",  # Sector breakdown of ETF holdings
    "etf_countries",  # Geographic exposure analysis
    "etf_equity_exposure",  # Individual stock exposure in ETFs
    
    # Index Tools (3 tools - with corrected names)
    "index_price_historical",
    "index_constituents",
    "index_available",  # Corrected from index_market
    
    # Derivatives Tools (4 tools - all working)
    "derivatives_options_chains",
    "derivatives_options_unusual",
    "derivatives_options_snapshots",
    "derivatives_futures_curve",  # Futures curve analysis (YFinance)
    
    # News Tools (2 tools - with corrected names)
    "news_world",  # Corrected from news_general
    "news_company",
    
    # Currency Tools (1 tool - removed non-existent)
    "currency_price_historical",
    
    # Commodity Tools (1 tool - with corrected name)
    "commodity_price_spot",  # Corrected from commodity_price_historical
    
    # Cryptocurrency Tools (1 tool - new)
    "crypto_price_historical",  # Cryptocurrency prices (YFinance/FMP)
})

def is_curated_tool(tool_name: str) -> bool:
    """Check if a tool is in the curated list.
    
    Args:
        tool_name: The name of the tool to check
        
    Returns:
        True if the tool is in the curated list, False otherwise
    """
    return tool_name in CURATED_TOOLS

def get_curated_tools_count() -> int:
    """Get the total number of curated tools.
    
    Returns:
        The number of tools in the curated list
    """
    return len(CURATED_TOOLS)