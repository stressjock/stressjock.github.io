🤖 ABOT Market Simulator v14.0 (Margin Arrest Edition)

Welcome to the ABOT Market Simulator, a fast-paced command-line trading game where the goal is simple: Get Rich, Stay Solvent. You control a virtual trading account in a simplified, volatile market.

This game is all about managing risk, especially with the introduction of Margin Trading. Use the command line at the bottom of the screen to execute trades and check your status.

🚀 Getting Started

Goal: Reach a Net Worth of over $1,000,000 to win the game.

Risk: If your Margin Account Value falls below $0, you are subject to a Margin Arrest (Game Over).

Simulation: The market runs on a daily simulation loop. Every few seconds, the market price of assets changes, and your margin interest is calculated.

🎮 Command Reference

Enter commands into the input box at the bottom and press Enter. Commands are case-insensitive.

Command

Usage Example

Description

HELP

HELP

Displays a list of all available commands and basic syntax.

PORTFOLIO

PORTFOLIO

Your daily summary. Displays your current stock holdings, cash, net worth, and, crucially, your margin account status.

PRICES

PRICES

Lists the current trading price for all available assets (e.g., BOT100, DEFENSE).

BUY

BUY BOT100 10

Purchases assets. Buys 10 shares of BOT100 using your available cash.

SELL

SELL DEFENSE 5

Sells assets. Sells 5 shares of DEFENSE, converting them to cash.

BORROW

BORROW 5000

Opens a short position. Borrows $5,000 from the bank (uses the margin account).

PAY

PAY 2000

Repays debt. Repays $2,000 toward your margin debt. Highly recommended to manage interest and margin risk.

🚨 Understanding Margin & Risk

The Margin Account value is your primary risk indicator.

Net Worth: This is the true value of your empire (Cash + Assets - Debt). This is what you must grow to win.

Margin Account Value: This is your Available Collateral. It is calculated as: Total Asset Value + Cash - Borrowed Funds.

If Margin > $0: You are safe and can safely borrow more.

If Margin < $0: You have negative capital. You are paying high interest, and if the market moves against you, you risk an automatic Margin Arrest and game over!

Pro-Tip: Use the PORTFOLIO command constantly to monitor your Margin Account Value. Don't let it hit zero!