import { Component } from "react"
import Header from "./components/header"
import HomePage from "./components/home-page"
import "./styles.css"

class App extends Component {
  constructor(props) {
    super(props)
    // Initialize theme from localStorage or default to 'light'
    const savedTheme = typeof window !== "undefined" ? localStorage.getItem("theme") : "light"
    this.state = {
      searchQuery: "",
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
      theme: savedTheme || "light",
    }
  }

  handleSearch = (query) => {
    this.setState({ searchQuery: query })
  }

  toggleTheme = () => {
    this.setState((prevState) => {
      const newTheme = prevState.theme === "light" ? "dark" : "light"
      if (typeof window !== "undefined") localStorage.setItem("theme", newTheme)
      return { theme: newTheme }
    })
  }
  getFilteredNews = () => {
    const { newsData, searchQuery } = this.state
    if (!searchQuery) return newsData

    return newsData.filter(
      (news) =>
        news.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
        news.summary.toLowerCase().includes(searchQuery.toLowerCase()) ||
        news.category.toLowerCase().includes(searchQuery.toLowerCase()),
    )
  }

  render() {
    const { theme } = this.state
    return (
      <div className={`app ${theme}`}>
        <Header onSearch={this.handleSearch} theme={theme} toggleTheme={this.toggleTheme} />
        <main className="main-content">
          <HomePage newsData={this.getFilteredNews()} />
        </main>
      </div>
    )
  }
}

export default App
