#!/usr/bin/env python3
"""
Financial Analysis Workflow Example
Demonstrates multi-agent coordination for portfolio analysis
"""

import asyncio
import json
from pathlib import Path

# This would be imported from the main package
# from claude_swarm import ClaudeSwarm, ClaudeAgent

def example_portfolio_analysis():
    """
    Example workflow for comprehensive portfolio analysis
    using multiple coordinated agents
    """
    
    # Sample portfolio data
    portfolio = {
        "AAPL": 0.25,
        "GOOGL": 0.20,
        "MSFT": 0.15,
        "AMZN": 0.15,
        "TSLA": 0.10,
        "NVDA": 0.10,
        "META": 0.05
    }
    
    print("🎯 Portfolio Analysis Workflow Example")
    print("=" * 50)
    
    # Step 1: Data Analysis
    print("\n📊 Step 1: Data Collection and Preparation")
    print("Data Analyst would:")
    print("- Fetch historical price data for all holdings")
    print("- Calculate returns and volatility metrics")
    print("- Prepare correlation matrix")
    print("- Validate data quality")
    
    # Step 2: Risk Assessment
    print("\n⚠️  Step 2: Risk Analysis")
    print("Risk Analyst would:")
    print("- Calculate portfolio VaR (95% and 99%)")
    print("- Perform stress testing scenarios")
    print("- Analyze concentration risk")
    print("- Generate risk metrics report")
    
    # Expected VaR calculation (example)
    estimated_var_95 = 0.035  # 3.5% daily VaR
    print(f"  - Estimated 95% VaR: {estimated_var_95:.1%}")
    
    # Step 3: Portfolio Optimization
    print("\n🔄 Step 3: Portfolio Optimization")
    print("Portfolio Manager would:")
    print("- Apply Modern Portfolio Theory")
    print("- Calculate efficient frontier")
    print("- Recommend rebalancing")
    print("- Consider transaction costs")
    
    # Step 4: Research Insights
    print("\n📈 Step 4: Investment Research")
    print("Research Analyst would:")
    print("- Analyze sector allocation (100% Technology)")
    print("- Review market outlook for tech sector")
    print("- Identify potential risks and opportunities")
    print("- Provide forward-looking recommendations")
    
    # Step 5: Final Recommendations
    print("\n💡 Step 5: Coordinated Recommendations")
    print("Combined team analysis:")
    print("- High concentration risk in technology sector")
    print("- Consider diversification into other sectors")
    print("- Potential defensive positions for volatility")
    print("- Regular rebalancing schedule recommended")
    
    return {
        "portfolio": portfolio,
        "risk_metrics": {
            "var_95": estimated_var_95,
            "concentration_risk": "High - 100% Technology"
        },
        "recommendations": [
            "Diversify across sectors",
            "Consider defensive allocations",
            "Implement regular rebalancing"
        ]
    }

def example_agent_coordination():
    """
    Example of how agents would coordinate in the actual system
    """
    
    print("\n🤖 Agent Coordination Example")
    print("=" * 40)
    
    # Simulated agent conversation flow
    agents_flow = [
        {
            "agent": "Risk Analyst",
            "action": "Analyze portfolio risk",
            "output": "High volatility (28%), concentrated risk",
            "next_agent": "Portfolio Manager",
            "reason": "User needs optimization recommendations"
        },
        {
            "agent": "Portfolio Manager", 
            "action": "Optimize allocation based on risk analysis",
            "output": "Recommended diversification strategy",
            "next_agent": "Research Analyst",
            "reason": "Need market outlook for recommendations"
        },
        {
            "agent": "Research Analyst",
            "action": "Provide market context and outlook",
            "output": "Tech sector analysis and alternatives",
            "next_agent": None,
            "reason": "Analysis complete"
        }
    ]
    
    for i, step in enumerate(agents_flow, 1):
        print(f"\n{i}. 🤖 **{step['agent']}**")
        print(f"   Action: {step['action']}")
        print(f"   Output: {step['output']}")
        if step['next_agent']:
            print(f"   → Transfer to: {step['next_agent']}")
            print(f"   → Reason: {step['reason']}")
        else:
            print("   ✅ Analysis complete")

def example_custom_functions():
    """
    Example custom functions that could be added to agents
    """
    
    print("\n🛠️  Custom Function Examples")
    print("=" * 35)
    
    # Risk calculation functions
    def calculate_portfolio_var(returns, confidence_level=0.05):
        """Calculate Historical Value at Risk"""
        import numpy as np
        sorted_returns = np.sort(returns)
        var_index = int(confidence_level * len(sorted_returns))
        return sorted_returns[var_index]
    
    def calculate_sharpe_ratio(returns, risk_free_rate=0.02):
        """Calculate Sharpe Ratio"""
        import numpy as np
        excess_returns = np.mean(returns) - risk_free_rate
        volatility = np.std(returns)
        return excess_returns / volatility if volatility > 0 else 0
    
    def optimize_portfolio(expected_returns, cov_matrix, risk_tolerance=1.0):
        """Mean-variance optimization"""
        # Simplified example - in reality would use scipy.optimize
        return {
            "optimal_weights": [0.2, 0.2, 0.2, 0.2, 0.2],
            "expected_return": 0.10,
            "portfolio_risk": 0.15
        }
    
    print("Functions that could be added to agents:")
    print("- calculate_portfolio_var(): Historical VaR calculation")
    print("- calculate_sharpe_ratio(): Risk-adjusted return metric")
    print("- optimize_portfolio(): Mean-variance optimization")
    print("- stress_test_portfolio(): Scenario analysis")
    print("- calculate_beta(): Market sensitivity analysis")

def main():
    """
    Run the complete workflow example
    """
    print("🚀 Claude Swarm Financial Analysis Example")
    print("=" * 50)
    
    # Run examples
    portfolio_result = example_portfolio_analysis()
    example_agent_coordination() 
    example_custom_functions()
    
    print("\n" + "=" * 50)
    print("✅ Example workflow complete!")
    print("\nTo use with actual Claude Swarm:")
    print('1. Create finance team: "Create finance team"')
    print('2. Start analysis: "Chat with agent: \'Analyze my portfolio...\'"')
    print("3. Agents will coordinate automatically for complete analysis")

if __name__ == "__main__":
    main()
