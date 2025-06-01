import { Component } from "react"
import Header from "./components/header"
import Sidebar from "./components/sidebar"
import HomePage from "./components/home-page"
import "./styles.css"

class App extends Component {
  constructor(props) {
    super(props)
    this.state = {
      searchQuery: "",
      selectedCategory: "all",
      newsData: [
        {
          id: 1,
          title: "Federal Reserve Signals Potential Rate Cut in 2025",
          summary:
            "The Federal Reserve indicated a possible shift in monetary policy as inflation shows signs of cooling, suggesting potential rate cuts in the coming year.",
          image: "/placeholder.svg?height=200&width=300",
          category: "Monetary Policy",
          importance: "high",
          date: "2025-01-31",
        },
        {
          id: 2,
          title: "Tech Stocks Rally on Strong Earnings Reports",
          summary: "Major technology companies exceeded quarterly expectations, driving market optimism.",
          image: "/placeholder.svg?height=150&width=250",
          category: "Markets",
          importance: "medium",
          date: "2025-01-31",
        },
        {
          id: 3,
          title: "Global Supply Chain Disruptions Ease",
          summary: "International shipping costs decline as port congestion clears and supply chains normalize.",
          image: "/placeholder.svg?height=180&width=280",
          category: "Trade",
          importance: "medium",
          date: "2025-01-31",
        },
        {
          id: 4,
          title: "Unemployment Rate Hits Historic Low",
          summary:
            "The national unemployment rate dropped to 3.2%, marking the lowest level in decades as job creation continues.",
          image: "/placeholder.svg?height=220&width=320",
          category: "Employment",
          importance: "high",
          date: "2025-01-31",
        },
        {
          id: 5,
          title: "Oil Prices Stabilize Amid OPEC Agreement",
          summary: "Crude oil prices find equilibrium following new production agreements.",
          image: "/placeholder.svg?height=160&width=240",
          category: "Energy",
          importance: "low",
          date: "2025-01-31",
        },
        {
          id: 6,
          title: "Housing Market Shows Signs of Recovery",
          summary: "Home sales increase for third consecutive month as mortgage rates decline.",
          image: "/placeholder.svg?height=190&width=290",
          category: "Real Estate",
          importance: "medium",
          date: "2025-01-31",
        },
        {
          id: 7,
          title: "Cryptocurrency Regulation Framework Announced",
          summary: "Government unveils comprehensive guidelines for digital asset trading and taxation.",
          image: "/placeholder.svg?height=170&width=260",
          category: "Crypto",
          importance: "high",
          date: "2025-01-31",
        },
        {
          id: 8,
          title: "Consumer Spending Exceeds Expectations",
          summary: "Retail sales surge 5.2% month-over-month, signaling strong consumer confidence.",
          image: "/placeholder.svg?height=200&width=300",
          category: "Consumer",
          importance: "medium",
          date: "2025-01-31",
        },
      ],
      cryptoData: [
        { symbol: "BTC", name: "Bitcoin", price: "$43,250", change: "+2.4%", positive: true },
        { symbol: "ETH", name: "Ethereum", price: "$2,580", change: "+1.8%", positive: true },
        { symbol: "ADA", name: "Cardano", price: "$0.52", change: "-0.9%", positive: false },
        { symbol: "SOL", name: "Solana", price: "$98.40", change: "+3.2%", positive: true },
        { symbol: "DOT", name: "Polkadot", price: "$7.85", change: "-1.2%", positive: false },
        { symbol: "MATIC", name: "Polygon", price: "$0.89", change: "+0.7%", positive: true },
      ],
      theme: "dark",
    }
  }

  handleSearch = (query) => {
    this.setState({ searchQuery: query })
  }

  handleCategorySelect = (category) => {
    this.setState({ selectedCategory: category })
  }

  getFilteredNews = () => {
    const { newsData, searchQuery, selectedCategory } = this.state
    let filtered = newsData

    if (selectedCategory !== "all") {
      filtered = filtered.filter((news) => news.category.toLowerCase() === selectedCategory.toLowerCase())
    }

    if (searchQuery) {
      filtered = filtered.filter(
        (news) =>
          news.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
          news.summary.toLowerCase().includes(searchQuery.toLowerCase()) ||
          news.category.toLowerCase().includes(searchQuery.toLowerCase()),
      )
    }

    return filtered
  }

  render() {
    const { theme } = this.state
    return (
      <div className={`app ${theme}`}>
        <Header onSearch={this.handleSearch} />
        <div className="app-body">
          <Sidebar
            onCategorySelect={this.handleCategorySelect}
            onSearch={this.handleSearch}
            cryptoData={this.state.cryptoData}
          />
          <main className="main-content">
            <HomePage newsData={this.getFilteredNews()} />
          </main>
        </div>
      </div>
    )
  }
}

export default App
