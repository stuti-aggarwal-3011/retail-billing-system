# Retail Billing System

An interactive terminal-based retail point-of-sale simulator that tracks live store inventory levels, manages user shopping carts, and processes automated customer checkout logic.

## 🚀 How It Works

The script allows a user to dynamically shop from a list of store items using continuous loop execution and strict inventory checks:

* **Real-Time Data Sync:** It tracks items using a parallel list infrastructure. Buying an item updates the global stock index immediately.
* **Stock Guarding:** The script strictly checks if the store has enough items. If a user asks for more items than are currently available, the order is rejected safely.
* **Tiered & Code Discounting:** During checkout, the program applies custom business logic. It checks for specific promo codes to apply a flat 20% reduction, or applies a tiered 10% loyalty discount if the transaction amount exceeds Rs. 1000.

## 🛠️ Variables Evaluated

| Variable | Type | Description |
| :--- | :--- | :--- |
| `item_names` | `list[str]` | Contains the names of the available inventory goods. |
| `item_prices` | `list[int]` | Contains the exact unit prices mapped directly to the items. |
| `item_quantity` | `list[int]` | Tracks live count changes of remaining available store inventory. |
| `total_bill` | `float` | Holds the running transactional price balance for the customer. |

## 💻 Tech Stack
* **Language:** Python 3.x
* **Concepts:** Parallel list indexing, loop control flow (`break`), input tracking, data mutability.

```
